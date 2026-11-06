#!/usr/bin/env python3
"""kit-rename.py: one-time migration of an installed kit to the current vault names (<prefix>-<short-name>, e.g. rbx-update). Standard library only.

The names come from vault-names.json next to this script: "prefix" and "renamed" = EVERY previous name of every item -> its current name
(generation 1 = the original unsuffixed names, generation 2 = the -rbxdev-vault names and the long game-dev-* / roblox-* names). Run by install.sh / install.ps1
BEFORE the kit files are copied (so the old manifest <config>/claude-kit/installed.tsv still lists the old names); loaded project folders are refreshed
afterwards by `vault-mode.py sync`.

  migrate [--config DIR] [--dry-run] [--quiet] [--force]   remove the OLD-named vault skills/agents (store and ~/.claude/skills|agents) that the kit installed and that are unchanged;
                                                           move them to <config>/claude-kit/backup/rename-migration-<time>/. Never touches
                                                           - a skill/agent with an old name that is NOT in the kit manifest (yours: left alone, one warning line)
                                                           - an old-named kit file you edited (kept, named in a warning)
                                                           Also moves the low-usage state marker (state/low-usage-mode.on or state/low-usage-mode-rbxdev-vault.on -> state/rbx-low-usage.on),
                                                           repoints kit hooks in settings.json that call an old low-usage-mode path (backup first),
                                                           writes claude-kit/COMMANDS-RENAMED.txt (the full old -> new table) and prints ONE message the first time.
                                                           Idempotent: a second run finds nothing and prints nothing.
  migrate --revert                                          restore the files of the last migration (and the settings.json backup if unchanged since); automatic migration is then off
  plugins [--config DIR] [--dry-run]                        rename the enabledPlugins keys of the kit mods in settings.json (workflow-hud / hud-rbxdev-vault -> rbx-subagent-hud,
                                                           vault-graph / graph-rbxdev-vault -> rbx-graph; backup first); the installers run it with --with-mods
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
COLD_BASE = "claude-kit/vault-mode"
OLD_LUM_STATES = ["state/low-usage-mode.on", "state/low-usage-mode-rbxdev-vault.on"]     # state marker names of generation 1 and 2
NEW_LUM_STATE = "state/rbx-low-usage.on"
LUM_OLD = r"low-usage-mode(?:-rbxdev-vault)?/scripts/lum"                                   # hook paths of generation 1 and 2
LUM_QUOTED_RX = re.compile(r'"[^"]*' + LUM_OLD + r'"')
LUM_BARE_RX = re.compile(r'[^\s"]*' + LUM_OLD)
LUM_ANY_RX = re.compile(LUM_OLD)
MODS_MK = "roblox-vault-kit-mods"


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
    tmp = "%s.%d.tmp" % (p, os.getpid())
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(tmp, p)


def load_names():
    return jread(os.path.join(HERE, "vault-names.json"), {"prefix": "", "renamed": [], "removed": []})


def all_items(names):
    """renamed entries (every generation) plus merged/removed ones (their 'new' is the item that took over; merged=True)"""
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
    cold = "%s/cold/%s/" % (COLD_BASE, o)      # cold-area topic folder, named like the skill/agent it belongs to
    if item["kind"] == "skill":
        return {"dir": ["skills/%s/" % o, "%s/skills/%s/" % (STORE, o), cold]}
    if item["kind"] == "agent":
        return {"exact": ["agents/%s.md" % o, "%s/agents/%s.md" % (STORE, o)], "dir": [cold]}
    return None


def cmd_table(a):
    n = load_names()
    print("prefix: %s   pattern: %s" % (n.get("prefix"), n.get("pattern", "")))
    for e in n["renamed"]:
        extra = ("  (command /%s -> /%s)" % (e["command_old"], e["command_new"])) if e.get("command_old") else ""
        print("%-8s gen%s %-42s -> %s%s" % (e["kind"], e.get("gen", "?"), e["old"], e["new"], extra))
    for e in n.get("removed", []):
        print("%-8s      %-42s merged into %s (removed)" % (e["kind"], e["old"], e.get("into", "")))
    return 0


def _repoint(node, new_path, counter):
    """walk parsed settings; rewrite hook commands that call an old low-usage-mode script path"""
    if isinstance(node, dict):
        for k, v in list(node.items()):
            if k == "command" and isinstance(v, str) and LUM_ANY_RX.search(v):
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


def write_settings(sp, data):
    tmp = "%s.%d.tmp" % (sp, os.getpid())
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, sp)


def lum_skill_name(names):
    for e in names["renamed"]:
        if e["kind"] == "skill" and e["old"] == "low-usage-mode":
            return e["new"]
    return names.get("prefix", "rbx") + "-low-usage"


def fix_settings(c, stamp, dry):
    """repoint kit hooks that still call an old low-usage-mode path (JSON-aware; backup first). Returns info dict or None."""
    sp = os.path.join(c, "settings.json")
    try:
        txt = open(sp, encoding="utf-8-sig").read()
        data = json.loads(txt)
    except (OSError, ValueError):
        return None
    if not LUM_ANY_RX.search(txt):
        return None
    new_path = '"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/%s/skills/%s/scripts/lum"' % (STORE, lum_skill_name(load_names()))
    counter = [0]
    _repoint(data, new_path, counter)
    if not counter[0]:
        return None
    if dry:
        return {"would": True}
    bk = sp + ".rename-bak-" + stamp
    shutil.copyfile(sp, bk)
    write_settings(sp, data)
    return {"backup": bk, "sha_after": sha(sp), "hooks": counter[0]}


def cmd_plugins(a):
    """rename enabledPlugins keys of the kit mods (old plugin name @ marketplace -> new name @ marketplace) in settings.json"""
    c = cfg_dir(a)
    names = load_names()
    mp = {e["old"]: e["new"] for e in names["renamed"] if e["kind"] == "plugin"}
    sp = os.path.join(c, "settings.json")
    try:
        data = json.loads(open(sp, encoding="utf-8-sig").read())
    except (OSError, ValueError):
        return 0
    ep = data.get("enabledPlugins")
    if not isinstance(ep, dict):
        return 0
    changes = []
    for k in list(ep):
        nm, _, mk = k.partition("@")
        if mk == MODS_MK and nm in mp and mp[nm] != nm:
            changes.append((k, "%s@%s" % (mp[nm], mk)))
    if getattr(a, "drop_legacy", False):
        # no new mods installed: drop the legacy keys instead of renaming them (a renamed key would point at a plugin that is not installed)
        drops = [k for k, _ in changes]
        if not drops or a.dry_run:
            return 0
        shutil.copyfile(sp, sp + ".rename-bak-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        for k in drops:
            ep.pop(k, None)
        write_settings(sp, data)
        return 0
    if not changes:
        return 0
    if a.dry_run:
        print("kit-rename: would rename %d enabledPlugins key(s): %s" % (len(changes), ", ".join("%s -> %s" % x for x in changes)))
        return 0
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    bk = sp + ".rename-bak-" + stamp
    shutil.copyfile(sp, bk)
    for old, new in changes:
        val = ep.pop(old)
        if new not in ep:
            ep[new] = val
    write_settings(sp, data)
    print("kit-rename: settings.json enabledPlugins renamed: %s (backup: %s)" % (", ".join("%s -> %s" % x for x in changes), bk))
    return 0


def message(names, moved_items, kept, foreign, backup):
    pairs, merged, seen = [], [], set()
    for e in all_items(names):
        if e["old"] not in moved_items.get(e["kind"], ()):
            continue
        if e.get("merged"):
            if e["kind"] == "skill":
                merged.append("/%s is gone, use /%s" % (e["old"], e["new"]))
            else:
                merged.append("agent %s is gone, use agent %s" % (e["old"], e["new"]))
            continue
        key = (e["kind"], e["old"], e["new"])
        if key in seen:
            continue
        seen.add(key)
        if e["kind"] == "agent":
            pairs.append("agent %s is now %s" % (e["old"], e["new"]))
        else:
            pairs.append("/%s is now /%s" % (e["old"], e["new"]))
    pre = names.get("prefix", "rbx")
    lines = []
    if pairs:
        lines.append("NOTICE FOR THE USER (show this): commands renamed, one time: " + ", ".join(pairs) + ".")
        lines.append("  Why: every command of this vault now starts with %s- (type /%s- to list them all) and is short, so it cannot clash with another vault or with your own skills. Nothing else changed; the old names no longer exist on this machine." % (pre, pre))
    if merged:
        lines.append("NOTICE FOR THE USER (show this): %scommands merged, one time: " % ("also " if pairs else "") + ", ".join(merged) + ".")
        lines.append("  Why: near-duplicate vault skills/agents were merged into one (same job, fewer entries in your context). Nothing else changed; the old ones no longer exist on this machine.")
    if backup:
        lines.append("  The removed old files are saved in %s (undo: kit-rename.py migrate --revert). The full old -> new table stays in claude-kit/COMMANDS-RENAMED.txt." % backup)
    for k in kept:
        lines.append("  kept (you edited it, so it was not removed): %s" % k)
    for f in foreign:
        lines.append("  left alone (not from the vault, yours): %s" % f)
    return "\n".join(lines)


def write_table_file(c, names, stamp):
    try:
        with open(os.path.join(c, "claude-kit", "COMMANDS-RENAMED.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write("Commands renamed on %s (vault prefix: %s; rule <prefix>-<short-name>; type /%s- to list every vault command)\n\n" % (stamp, names.get("prefix"), names.get("prefix")))
            for e in names["renamed"]:
                f.write("%-6s %-44s -> %s\n" % (e["kind"], e["old"], e["new"]))
            for e in names.get("removed", []):
                f.write("%-6s %-44s merged into %s (removed)\n" % (e["kind"], e["old"], e.get("into", "")))
            f.write("\nTool files (claude-kit/tools/*.py) and the router /%s kept their names.\n" % names.get("prefix"))
    except OSError:
        pass


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
    if not a.dry_run:
        planned = []
        for item in all_items(names):
            spec = entries_for(item)
            if spec:
                for rel, h in man.items():
                    f = os.path.join(c, *rel.split("/"))
                    if (any(rel.startswith(q) for q in spec.get("dir", [])) or rel in spec.get("exact", [])) and os.path.isfile(f) and sha(f) == h:
                        planned.append({"rel": rel, "sha": h, "old": item["old"], "new": item["new"], "kind": item["kind"]})
        if planned:
            jwrite(last_path, {"at": stamp, "backup": backup, "moved": planned, "kept": [], "foreign": [], "state_moved": "", "settings": {}, "prefix": names.get("prefix")})
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
                    if cand not in foreign:
                        foreign.append(cand)
    # state marker of the low usage mode (generation 1 or 2 name -> rbx-low-usage.on)
    st_new = os.path.join(c, *NEW_LUM_STATE.split("/"))
    state_moved = ""
    for so in OLD_LUM_STATES:
        sp_ = os.path.join(c, *so.split("/"))
        if os.path.isfile(sp_):
            if not os.path.exists(st_new):
                if not a.dry_run:
                    os.replace(sp_, st_new)
                state_moved = so
            elif not a.dry_run:
                os.remove(sp_)       # the new marker already exists; the stale old one is dropped
    st = fix_settings(c, stamp, a.dry_run)
    if not moved and not kept and not state_moved and not st:
        if not a.dry_run and lay.get("rename") != names.get("prefix"):
            lay["rename"] = names.get("prefix")
            jwrite(lay_path, lay)
        return 0
    if a.dry_run:
        print("kit-rename: would remove %d old-named vault file(s) (%d edited by you are kept, %d old-named items are yours and stay)%s."
              % (len(moved), len(kept), len(foreign), "; would repoint the low-usage hooks in settings.json" if st else ""))
        return 0
    for f in prune:
        for stop in (os.path.join(c, "skills"), os.path.join(c, "agents"), os.path.join(c, *STORE.split("/"), "skills"), os.path.join(c, *STORE.split("/"), "agents"), os.path.join(c, *COLD_BASE.split("/"), "cold")):
            if os.path.realpath(f).startswith(os.path.realpath(stop) + os.sep):
                rmdirs_up(os.path.dirname(f), stop)
                break
    info = {"at": stamp, "backup": backup if moved else "", "moved": moved, "kept": kept, "foreign": foreign,
            "state_moved": state_moved, "settings": st or {}, "prefix": names.get("prefix")}
    if moved:
        jwrite(os.path.join(backup, "migration.json"), info)
    jwrite(last_path, info)
    lay.update({"rename": names.get("prefix"), "rename_auto": True, "renamed_at": stamp})
    jwrite(lay_path, lay)
    write_table_file(c, names, stamp)
    msg = message(names, moved_items, kept, foreign, backup if moved else "")
    if msg and (not a.quiet or moved or kept):
        print(msg)
    if st:
        print("  hooks: the low-usage hooks in %s now call the new path (backup: %s)" % (os.path.join(c, "settings.json"), st.get("backup")))
    if state_moved:
        print("  low usage mode state moved to %s" % NEW_LUM_STATE)
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
    mp = os.path.join(c, "claude-kit", "installed.tsv")
    if os.path.isfile(mp) and last.get("moved"):          # the restored files are vault-owned again (so `migrate --force` can remove them once more)
        have = read_manifest(mp)
        add = [(r["rel"] + chr(9) + r["sha"] + chr(10)) for r in last["moved"] if r["rel"] not in have]
        if add:
            with open(mp, "a", encoding="utf-8", newline="") as f:
                f.writelines(add)
    if last.get("state_moved"):
        new = os.path.join(c, *NEW_LUM_STATE.split("/"))
        old = os.path.join(c, *str(last["state_moved"] if isinstance(last["state_moved"], str) else OLD_LUM_STATES[0]).split("/"))
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
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(errors="replace")
        except Exception:
            pass
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
    p = sp.add_parser("plugins")
    p.add_argument("--config")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--drop-legacy", action="store_true")
    a = ap.parse_args(argv)
    try:
        return {"migrate": cmd_migrate, "table": cmd_table, "plugins": cmd_plugins}[a.cmd](a) or 0
    except Exception as e:      # never break an install
        print("kit-rename: failed: %r" % (e,), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
