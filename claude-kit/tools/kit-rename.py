#!/usr/bin/env python3
"""kit-rename.py: one-time migration of an installed kit to the vault-suffixed names (<verb>-<slug>-vault). Standard library only.

The names come from vault-names.json next to this script (slug, old -> new table). Run by install.sh / install.ps1 BEFORE the kit files are copied
(so the old manifest <config>/claude-kit/installed.tsv still lists the old names); loaded project folders are refreshed afterwards by `vault-mode.py sync`.

  migrate [--config DIR] [--dry-run] [--quiet] [--force]   remove the OLD-named vault skills/agents (store and ~/.claude/skills|agents) that the kit installed and that are unchanged;
                                                           move them to <config>/claude-kit/backup/rename-migration-<time>/. Never touches
                                                           - a skill/agent with an old name that is NOT in the kit manifest (yours: left alone, one warning line)
                                                           - an old-named kit file you edited (kept, named in a warning)
                                                           Also moves state/low-usage-mode.on, repoints kit hooks in settings.json that call the old low-usage-mode path (backup first),
                                                           writes claude-kit/COMMANDS-RENAMED.txt and prints ONE message the first time ("commands renamed: /vault-update is now ...").
                                                           Idempotent: a second run finds nothing and prints nothing.
  migrate --revert                                          restore the files of the last migration (and the settings.json backup if unchanged since); automatic migration is then off
  table                                                     print the old -> new table (and the merged/removed items)

The names file also has a "removed" list: skills/agents that were MERGED into another item and no longer exist ("into" names the item that took over).
They are handled exactly like renamed ones (unchanged vault file -> backup, edited or yours -> left alone with a warning), but nothing is installed in their place.
Config dir: --config DIR, else $CLAUDE_CONFIG_DIR, else $CLAUDE_KIT_HOME/.claude, else ~/.claude.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = "claude-kit/vault-mode/.claude"
OLD_LUM_STATE = "state/low-usage-mode.on"
NEW_LUM_STATE = "state/low-usage-mode-%s-vault.on"
LUM_QUOTED_RX = re.compile(r'"[^"]*low-usage-mode/scripts/lum"')
LUM_BARE_RX = re.compile(r'[^\s"]*low-usage-mode/scripts/lum')


def cfg_dir(a=None):
    d = getattr(a, "config", None) or os.environ.get("CLAUDE_CONFIG_DIR")
    if d:
        return os.path.abspath(os.path.expanduser(d))
    if os.environ.get("CLAUDE_KIT_HOME"):
        return os.path.abspath(os.path.join(os.path.expanduser(os.environ["CLAUDE_KIT_HOME"]), ".claude"))
    return os.path.join(os.path.expanduser("~"), ".claude")


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def jread(p, default):
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def jwrite(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(tmp, p)


def load_names():
    return jread(os.path.join(HERE, "vault-names.json"), {"slug": "", "renamed": [], "removed": []})


def all_items(names):
    """renamed entries plus merged/removed ones (their 'new' is the item that took over; merged=True)"""
    out = list(names.get("renamed", []))
    for e in names.get("removed", []):
        out.append(dict(e, new=e.get("into", ""), merged=True))
    return out


def read_manifest(path):
    out = {}
    try:
        for ln in open(path, encoding="utf-8"):
            parts = ln.rstrip("\n").split("\t")
            if len(parts) >= 2 and not parts[0].startswith("#"):
                out[parts[0]] = parts[1]
    except OSError:
        pass
    return out


def rmdirs_up(path, stop):
    path = path if os.path.isdir(path) else os.path.dirname(path)
    stop = os.path.realpath(stop)
    while path and os.path.realpath(path) != stop and os.path.isdir(path):
        try:
            junk = os.path.join(path, "__pycache__")
            if os.path.isdir(junk) and os.listdir(path) == ["__pycache__"]:
                shutil.rmtree(junk, ignore_errors=True)
            os.rmdir(path)
        except OSError:
            return
        path = os.path.dirname(path)


def entries_for(item):
    """(prefix_or_exact list) of manifest keys that belong to an old-named item"""
    o = item["old"]
    if item["kind"] == "skill":
        return {"dir": ["skills/%s/" % o, "%s/skills/%s/" % (STORE, o)]}
    if item["kind"] == "agent":
        return {"exact": ["agents/%s.md" % o, "%s/agents/%s.md" % (STORE, o)]}
    return None


def cmd_table(a):
    n = load_names()
    print("slug: %s   pattern: %s" % (n["slug"], n.get("pattern", "")))
    for e in n["renamed"]:
        extra = ("  (command /%s -> /%s)" % (e["command_old"], e["command_new"])) if e.get("command_old") else ""
        print("%-8s %-30s -> %s%s" % (e["kind"], e["old"], e["new"], extra))
    for e in n.get("removed", []):
        print("%-8s %-30s merged into %s (removed)" % (e["kind"], e["old"], e.get("into", "")))
    return 0


def _repoint(node, new_path, counter):
    """walk parsed settings; rewrite hook commands that call the old low-usage-mode script path"""
    if isinstance(node, dict):
        for k, v in list(node.items()):
            if k == "command" and isinstance(v, str) and "low-usage-mode/scripts/lum" in v:    # legacy path
                nv = LUM_QUOTED_RX.sub(lambda m: new_path, v)
                if nv == v:
                    nv = LUM_BARE_RX.sub(lambda m: new_path.strip('"'), v)
                if nv != v:
                    node[k] = nv
                    counter[0] += 1
            else:
                _repoint(v, new_path, counter)
    elif isinstance(node, list):
        for v in node:
            _repoint(v, new_path, counter)


def fix_settings(c, stamp, dry):
    """repoint kit hooks that still call the old low-usage-mode path (JSON-aware; backup first). Returns info dict or None."""
    sp = os.path.join(c, "settings.json")
    try:
        txt = open(sp, encoding="utf-8-sig").read()
        data = json.loads(txt)
    except (OSError, ValueError):
        return None
    if "low-usage-mode/scripts/lum" not in txt:
        return None
    new_path = '"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/%s/skills/low-usage-mode-%s-vault/scripts/lum"' % (STORE, load_names()["slug"])
    counter = [0]
    _repoint(data, new_path, counter)
    if not counter[0]:
        return None
    if dry:
        return {"would": True}
    bk = sp + ".rename-bak-" + stamp
    shutil.copyfile(sp, bk)
    with open(sp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return {"backup": bk, "sha_after": sha(sp), "hooks": counter[0]}


def message(names, moved_items, kept, foreign, backup):
    pairs = []
    merged = []
    seen = set()
    for e in all_items(names):
        if e["old"] in moved_items.get(e["kind"], ()) and e.get("merged"):
            if e["kind"] == "skill":
                merged.append("/%s is gone, use /%s" % (e["old"], e["new"]))
            else:
                merged.append("agent %s is gone, use agent %s" % (e["old"], e["new"]))
            continue
        if e["old"] in moved_items.get(e["kind"], ()):
            tag = "/" if e["kind"] == "skill" else ""
            key = (e["old"], e["new"])
            if e["kind"] == "agent" and (e["old"], e["new"]) in seen:
                continue
            seen.add(key)
            if e["kind"] == "agent":
                pairs.append("agent %s is now %s" % (e["old"], e["new"]))
            else:
                pairs.append("%s%s is now %s%s" % (tag, e["old"], tag, e["new"]))
    lines = []
    if pairs:
        lines.append("NOTICE FOR THE USER (show this): commands renamed, one time: " + ", ".join(pairs) + ".")
        lines.append("  Why: every command of this vault now ends in -%s-vault, so it cannot clash with another vault or with your own skills. Nothing else changed; the old names no longer exist on this machine." % names["slug"])
    if merged:
        lines.append("NOTICE FOR THE USER (show this): %scommands merged, one time: " % ("also " if pairs else "") + ", ".join(merged) + ".")
        lines.append("  Why: near-duplicate vault skills/agents were merged into one (same job, fewer entries in your context). Nothing else changed; the old ones no longer exist on this machine.")
    if backup:
        lines.append("  The removed old files are saved in %s (undo: kit-rename.py migrate --revert). The list stays in claude-kit/COMMANDS-RENAMED.txt." % backup)
    for k in kept:
        lines.append("  kept (you edited it, so it was not removed): %s" % k)
    for f in foreign:
        lines.append("  left alone (not from the vault, yours): %s" % f)
    return "\n".join(lines)


def cmd_migrate(a):
    c = cfg_dir(a)
    names = load_names()
    lay_path = os.path.join(c, "claude-kit", "vault-mode", "layout.json")
    lay = jread(lay_path, {})
    last_path = os.path.join(c, "claude-kit", "vault-mode", "rename-last.json")
    if a.revert:
        return revert(c, lay, lay_path, last_path)
    if lay.get("rename_auto") is False and not a.force:
        return 0
    man = read_manifest(os.path.join(c, "claude-kit", "installed.tsv"))
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = os.path.join(c, "claude-kit", "backup", "rename-migration-" + stamp)
    moved, kept, foreign, moved_items = [], [], [], {"skill": set(), "agent": set()}
    prune = []
    for item in all_items(names):
        spec = entries_for(item)
        if not spec:
            continue
        owned = [(rel, h) for rel, h in man.items()
                 if any(rel.startswith(p) for p in spec.get("dir", [])) or rel in spec.get("exact", [])]
        for rel, h in owned:
            f = os.path.join(c, *rel.split("/"))
            if not os.path.isfile(f):
                continue
            if sha(f) != h:
                kept.append(os.path.relpath(f, c) if not a.dry_run else rel)
                continue
            if not a.dry_run:
                dst = os.path.join(backup, *rel.split("/"))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.move(f, dst)
                prune.append(f)
            moved.append({"rel": rel, "sha": h, "old": item["old"], "new": item["new"], "kind": item["kind"]})
            moved_items[item["kind"]].add(item["old"])
        # an old-named skill/agent that the kit manifest does not know = the user's own
        cands = [os.path.join(c, "skills", item["old"]), os.path.join(c, *STORE.split("/"), "skills", item["old"])] if item["kind"] == "skill" else \
                [os.path.join(c, "agents", item["old"] + ".md"), os.path.join(c, *STORE.split("/"), "agents", item["old"] + ".md")]
        for cand in cands:
            if os.path.exists(cand):
                crel = os.path.relpath(cand, c).replace(os.sep, "/")
                if not any(rel == crel or rel.startswith(crel + "/") for rel, _ in owned):
                    foreign.append(cand)
    # state marker of /low-usage-mode
    slug = names["slug"]
    st_old, st_new = os.path.join(c, *OLD_LUM_STATE.split("/")), os.path.join(c, *(NEW_LUM_STATE % slug).split("/"))
    state_moved = False
    if os.path.isfile(st_old) and not os.path.exists(st_new) and moved_items["skill"] & {"low-usage-mode"}:
        if not a.dry_run:
            os.replace(st_old, st_new)
        state_moved = True
    st = fix_settings(c, stamp, a.dry_run) if moved_items["skill"] & {"low-usage-mode"} or moved else None
    if not moved and not kept and not state_moved and not st:
        if not a.dry_run and lay.get("rename") != slug:
            lay["rename"] = slug
            jwrite(lay_path, lay)
        return 0
    if a.dry_run:
        print("kit-rename: would remove %d old-named vault file(s) (%d edited by you are kept, %d old-named items are yours and stay)%s."
              % (len(moved), len(kept), len(foreign), "; would repoint the low-usage-mode hooks in settings.json" if st else ""))
        return 0
    for f in prune:
        top = f.replace(os.sep, "/")
        for stop in (os.path.join(c, "skills"), os.path.join(c, "agents"), os.path.join(c, *STORE.split("/"), "skills"), os.path.join(c, *STORE.split("/"), "agents")):
            if os.path.realpath(f).startswith(os.path.realpath(stop) + os.sep):
                rmdirs_up(os.path.dirname(f), stop)
                break
    info = {"at": stamp, "backup": backup if moved else "", "moved": moved, "kept": kept, "foreign": foreign,
            "state_moved": state_moved, "settings": st or {}, "slug": slug}
    if moved:
        jwrite(os.path.join(backup, "migration.json"), info)
    jwrite(last_path, info)
    lay.update({"rename": slug, "rename_auto": True, "renamed_at": stamp})
    jwrite(lay_path, lay)
    msg = message(names, moved_items, kept, foreign, backup if moved else "")
    try:
        with open(os.path.join(c, "claude-kit", "COMMANDS-RENAMED.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write("Commands renamed on %s (vault slug: %s; rule <verb>-<slug>-vault)\n\n" % (stamp, slug))
            for e in names["renamed"]:
                f.write("%-6s %-30s -> %s\n" % (e["kind"], e["old"], e["new"]))
            for e in names.get("removed", []):
                f.write("%-6s %-30s merged into %s (removed)\n" % (e["kind"], e["old"], e.get("into", "")))
            f.write("\nTool files (claude-kit/tools/*.py) and the other vault commands (game-dev-*, roblox-*, make-roblox-game, rbx) kept their names.\n")
    except OSError:
        pass
    if not a.quiet or moved or kept:
        print(msg)
    if st:
        print("  hooks: the low-usage-mode hooks in %s now call the new path (backup: %s)" % (os.path.join(c, "settings.json"), st.get("backup")))
    if state_moved:
        print("  low usage mode state moved to %s" % (NEW_LUM_STATE % slug))
    return 0


def revert(c, lay, lay_path, last_path):
    last = jread(last_path, None)
    if not last:
        print("kit-rename: no rename migration to revert.")
        return 0
    n = 0
    for rec in last.get("moved", []):
        src = os.path.join(last["backup"], *rec["rel"].split("/"))
        dst = os.path.join(c, *rec["rel"].split("/"))
        if os.path.isfile(src) and not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
            n += 1
    names = load_names()
    mp = os.path.join(c, "claude-kit", "installed.tsv")
    if os.path.isfile(mp) and last.get("moved"):          # the restored files are vault-owned again (so `migrate --force` can remove them once more)
        have = read_manifest(mp)
        add = [(r["rel"] + chr(9) + r["sha"] + chr(10)) for r in last["moved"] if r["rel"] not in have]
        if add:
            with open(mp, "a", encoding="utf-8", newline="") as f:
                f.writelines(add)
    if last.get("state_moved"):
        new = os.path.join(c, *(NEW_LUM_STATE % last.get("slug", names["slug"])).split("/"))
        old = os.path.join(c, *OLD_LUM_STATE.split("/"))
        if os.path.isfile(new) and not os.path.exists(old):
            os.replace(new, old)
    stt = last.get("settings") or {}
    sp = os.path.join(c, "settings.json")
    if stt.get("backup") and os.path.isfile(stt["backup"]):
        if os.path.isfile(sp) and sha(sp) == stt.get("sha_after"):
            shutil.copyfile(stt["backup"], sp)
        else:
            print("kit-rename: settings.json changed since the migration; not restored (the backup is %s)" % stt["backup"])
    lay["rename_auto"] = False
    jwrite(lay_path, lay)
    print("kit-rename: restored %d old-named file(s). The new-named commands stay installed too. Automatic rename migration is now off; `kit-rename.py migrate --force` runs it again (right after the revert, before the next kit install rewrites the manifest)." % n)
    return 0


def main(argv):
    ap = argparse.ArgumentParser(prog="kit-rename.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("migrate")
    s.add_argument("--config")
    s.add_argument("--dry-run", action="store_true")
    s.add_argument("--revert", action="store_true")
    s.add_argument("--quiet", action="store_true")
    s.add_argument("--force", action="store_true")
    t = sp.add_parser("table")
    t.add_argument("--config")
    a = ap.parse_args(argv)
    try:
        return {"migrate": cmd_migrate, "table": cmd_table}[a.cmd](a) or 0
    except Exception as e:      # never break an install
        print("kit-rename: failed: %r" % (e,), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
