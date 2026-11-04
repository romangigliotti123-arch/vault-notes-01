#!/usr/bin/env python3
"""vault-mode.py: Roblox dev mode for the vault kit. Standard library only. Never edits settings.json, never touches ~/.claude/CLAUDE.md.

The kit's skills and agents are NOT installed where every Claude Code session reads them. They live in an on-demand store:
    <config>/claude-kit/vault-mode/.claude/skills/<name>/   <config>/claude-kit/vault-mode/.claude/agents/<name>.md   <config>/claude-kit/vault-mode/CLAUDE.md (the mode rules)
Only the names in <config>/claude-kit/vault-mode/always-on.txt (load-rbxdev-vault, unload-rbxdev-vault, update-rbxdev-vault, update-check-rbxdev-vault, uninstall-rbxdev-vault) stay in <config>/skills.

  load   [--project DIR] [--no-link] [--no-text]   copy the store's skills/agents into DIR/.claude/skills|agents (DIR = current folder), list them in DIR/.claude/vault-mode.json,
                                                   hide them from git (.git/info/exclude), print the confirmation + the mode rules. --no-link: write nothing (session started with --add-dir).
  unload [--project DIR | --all]                   remove exactly what load added (files whose content is unchanged); never a file of yours
  status [--project DIR]                           mode state of this folder + store/migration summary
  sync   [--quiet]                                 after an update: refresh every folder that has the mode loaded (kit-refresh runs this)
  migrate [--dry-run | --revert] [--old-manifest F] move the old always-on kit skills/agents out of <config>/skills|agents into the store (backup + manifest, idempotent, reversible)
  auto   [--project DIR] [--always]                for an OPT-IN SessionStart hook: load when DIR looks like a Roblox project (or --always), print the mode rules; silent otherwise
  autoload-snippet                                 print the settings.json hook an owner can add by hand to enable auto
  mode-text                                        print the mode rules
  cold   [TOPIC[/FILE]] [--path]                   cold area (<store>/cold: bulk that skills point to with [cold:TOPIC/FILE]; never copied into projects): no argument lists topics, TOPIC lists files,
                                                   TOPIC/FILE prints the file (--path prints only its path)
Config dir: --config DIR, else $CLAUDE_CONFIG_DIR, else $CLAUDE_KIT_HOME/.claude, else ~/.claude.
"""
import argparse
import datetime
import fnmatch
import hashlib
import json
import os
import shutil
import subprocess
import sys

ALWAYS_ON_DEFAULT = ["load-rbxdev-vault", "unload-rbxdev-vault", "update-rbxdev-vault", "update-check-rbxdev-vault", "uninstall-rbxdev-vault"]
MB = "# >>> roblox-vault-mode (managed by /load-rbxdev-vault, removed by /unload-rbxdev-vault) >>>"
ME = "# <<< roblox-vault-mode <<<"
MB_PREFIX = "# >>> roblox-vault-mode ("
ROBLOX_MARKERS = ["default.project.json", "*.project.json", "*.rbxl", "*.rbxlx", "*.rbxm", "*.rbxmx", "rokit.toml", "aftman.toml", "wally.toml", "selene.toml", "stylua.toml"]


def cfg_dir(a=None):
    d = getattr(a, "config", None) or os.environ.get("CLAUDE_CONFIG_DIR")
    if d:
        return os.path.abspath(os.path.expanduser(d))
    if os.environ.get("CLAUDE_KIT_HOME"):
        return os.path.abspath(os.path.join(os.path.expanduser(os.environ["CLAUDE_KIT_HOME"]), ".claude"))
    return os.path.join(os.path.expanduser("~"), ".claude")


def P(c):
    s = os.path.join(c, "claude-kit", "vault-mode")
    return {"c": c, "store": s, "sk": os.path.join(s, ".claude", "skills"), "ag": os.path.join(s, ".claude", "agents"), "rules": os.path.join(s, "CLAUDE.md"),
            "cold": os.path.join(s, "cold"), "always": os.path.join(s, "always-on.txt"), "reg": os.path.join(s, "loaded.json"), "layout": os.path.join(s, "layout.json")}


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


def always_on(p):
    try:
        with open(p["always"], encoding="utf-8") as f:
            v = [x.strip() for x in f if x.strip() and not x.startswith("#")]
        return v or ALWAYS_ON_DEFAULT
    except OSError:
        return ALWAYS_ON_DEFAULT


def tree(d):
    out = {}
    for dp, dn, fn in os.walk(d):
        dn[:] = [x for x in dn if x != "__pycache__"]
        for f in fn:
            if f.endswith(".pyc"):
                continue
            full = os.path.join(dp, f)
            out[os.path.relpath(full, d).replace(os.sep, "/")] = sha(full)
    return out


def store_items(p):
    """{key: (src_dir_or_file, {rel: sha})} for every store skill/agent. key = skills/<n> | agents/<n>.md"""
    items = {}
    if os.path.isdir(p["sk"]):
        for n in sorted(os.listdir(p["sk"])):
            d = os.path.join(p["sk"], n)
            if os.path.isfile(os.path.join(d, "SKILL.md")):
                items["skills/" + n] = (d, tree(d))
    if os.path.isdir(p["ag"]):
        for f in sorted(os.listdir(p["ag"])):
            fp = os.path.join(p["ag"], f)
            if f.endswith(".md") and os.path.isfile(fp):
                items["agents/" + f] = (fp, {f: sha(fp)})
    return items


def dest_of(proj, key):
    return os.path.join(proj, ".claude", *key.split("/"))


def file_dest(proj, key, rel):
    d = dest_of(proj, key)
    return d if key.startswith("agents/") else os.path.join(d, *rel.split("/"))


def file_src(src, key, rel):
    return src if key.startswith("agents/") else os.path.join(src, *rel.split("/"))


def rmdirs_up(path, stop):
    path = path if os.path.isdir(path) else os.path.dirname(path)
    while path and os.path.realpath(path) != os.path.realpath(stop) and os.path.isdir(path):
        try:
            junk = os.path.join(path, "__pycache__")
            if os.path.isdir(junk) and os.listdir(path) == ["__pycache__"]:
                shutil.rmtree(junk, ignore_errors=True)
            os.rmdir(path)
        except OSError:
            return
        path = os.path.dirname(path)


def prune_empty(path):
    """remove path and its sub-folders when they contain no files (on Windows a folder that a running Claude Code watches cannot be deleted until it exits). True when path is gone."""
    if not os.path.isdir(path):
        return True
    for dp, dn, fn in os.walk(path, topdown=False):
        for d in dn:
            try:
                os.rmdir(os.path.join(dp, d))
            except OSError:
                pass
    try:
        os.rmdir(path)
    except OSError:
        pass
    return not os.path.exists(path)


def has_files(d):
    return any(fs for _, _, fs in os.walk(d))


def git_exclude(proj):
    """(exclude_file, prefix) or None. prefix = path of proj below the repo top ('' or 'sub/dir/')."""
    try:
        r = subprocess.run(["git", "-C", proj, "rev-parse", "--show-toplevel", "--git-path", "info/exclude"], capture_output=True, text=True, timeout=20)
        if r.returncode != 0:
            return None
        top, ex = r.stdout.strip().splitlines()[:2]
        if not os.path.isabs(ex):
            ex = os.path.join(proj, ex)
        rel = os.path.relpath(os.path.realpath(proj), os.path.realpath(top)).replace(os.sep, "/")
        return ex, ("" if rel == "." else rel + "/")
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def exclude_write(proj, keys):
    g = git_exclude(proj)
    if not g:
        return False
    ex, pre = g
    try:
        old = open(ex, encoding="utf-8").read() if os.path.exists(ex) else ""
    except OSError:
        return False
    base = exclude_strip(old)
    if keys:
        lines = [MB, "/" + pre + ".claude/vault-mode.json"] + ["/" + pre + ".claude/" + k + ("/" if k.startswith("skills/") else "") for k in sorted(keys)] + [ME]
        base = (base.rstrip("\n") + "\n" if base.strip() else "") + "\n".join(lines) + "\n"
    try:
        os.makedirs(os.path.dirname(ex), exist_ok=True)
        with open(ex, "w", encoding="utf-8", newline="\n") as f:
            f.write(base)
    except OSError:
        return False
    return True


def exclude_strip(t):
    out, skip = [], False
    for ln in t.splitlines():
        if ln.strip() == MB or ln.strip().startswith(MB_PREFIX):      # also the block written by a kit with the previous (unsuffixed) command names
            skip = True
            continue
        if skip and ln.strip() == ME:
            skip = False
            continue
        if not skip:
            out.append(ln)
    return ("\n".join(out) + "\n") if out else ""


def guard(proj, p):
    rc = os.path.realpath(p["c"])
    rp = os.path.realpath(proj)
    if os.path.realpath(os.path.join(proj, ".claude")) == rc or rp == rc or rp.startswith(rc + os.sep):
        return ("%s is (or is inside) your Claude config folder; its .claude folder would be your user-wide setup, which would load the vault in EVERY session. "
                "Open Claude in a project folder (for example your Roblox game's folder) and run /load-rbxdev-vault there." % proj)
    if rp == os.path.realpath(os.path.expanduser("~")):
        return "your home folder is not a project: loading here would put the vault into every session started below it. Open Claude in a project folder and run /load-rbxdev-vault there."
    return None


def ref_line(p):
    f = os.path.join(p["c"], "claude-kit", "reference-path.txt")
    try:
        d = open(f, encoding="utf-8").read().splitlines()[0].strip()
        n = sum(1 for ln in open(os.path.join(d, "INDEX.md"), encoding="utf-8") if ln.startswith("img/"))
        if n:
            return "reference images ready (%d)" % n
    except (OSError, IndexError):
        pass
    return "reference images not downloaded yet (/update-rbxdev-vault fetches them)"


def learn_line(p):
    if not os.path.isfile(os.path.join(p["c"], "claude-kit", "tools", "learn.py")):
        return "learn step unavailable (learn.py missing)"
    pend = os.path.join(p["c"], "claude-kit", "learnings-queue", "pending")
    n = len([x for x in os.listdir(pend)]) if os.path.isdir(pend) else 0
    return "learn step on" + (" (%d note%s queued)" % (n, "" if n == 1 else "s") if n else "")


def counts(keys):
    return sum(1 for k in keys if k.startswith("skills/")), sum(1 for k in keys if k.startswith("agents/"))


def link(proj, p, quiet=False):
    """create/refresh the project copies. Returns (marker, notes, changed)"""
    items = store_items(p)
    mpath = os.path.join(proj, ".claude", "vault-mode.json")
    marker = jread(mpath, {"items": {}, "created": []})
    marker.setdefault("items", {})
    marker.setdefault("created", [])
    notes, changed = [], False
    ao = set(always_on(p))
    if not os.path.isdir(os.path.join(proj, ".claude")):
        os.makedirs(os.path.join(proj, ".claude"))
        marker["created_claude"] = True
    for sub in ("skills", "agents"):
        d = os.path.join(proj, ".claude", sub)
        if not os.path.isdir(d) and any(k.startswith(sub + "/") for k in items):
            os.makedirs(d, exist_ok=True)
            if ".claude/" + sub not in marker["created"]:
                marker["created"].append(".claude/" + sub)
            changed = True
    for key, (src, files) in items.items():
        name = key.split("/", 1)[1]
        mine = marker["items"].get(key)
        user_path = os.path.join(p["c"], "skills", name) if key.startswith("skills/") else os.path.join(p["c"], "agents", name)
        if name in ao:
            continue
        if not mine and os.path.exists(user_path):
            notes.append("skipped %s: you already have one of that name in %s (yours wins)" % (key, os.path.dirname(user_path)))
            continue
        dst = dest_of(proj, key)
        if not mine and os.path.exists(dst):
            notes.append("skipped %s: %s already exists and is not from the vault (left untouched)" % (key, dst))
            continue
        rec = dict((mine or {}).get("files", {}))
        newrec = {}
        for rel, h in files.items():
            fd = file_dest(proj, key, rel)
            cur = sha(fd) if os.path.isfile(fd) else None
            if cur == h:
                newrec[rel] = h
                continue
            if cur is not None and rec.get(rel) != cur:
                notes.append("kept your edited %s (not refreshed)" % os.path.relpath(fd, proj))
                newrec[rel] = rec.get(rel, cur)
                continue
            os.makedirs(os.path.dirname(fd), exist_ok=True)
            shutil.copyfile(file_src(src, key, rel), fd)
            newrec[rel] = h
            changed = True
        for rel, h in rec.items():          # file left the kit: remove if unchanged
            if rel not in files:
                fd = file_dest(proj, key, rel)
                if os.path.isfile(fd) and sha(fd) == h:
                    os.remove(fd)
                    rmdirs_up(fd, os.path.join(proj, ".claude", key.split("/")[0]))
                    changed = True
        marker["items"][key] = {"files": newrec}
    for key in [k for k in marker["items"] if k not in items]:   # whole skill/agent left the kit
        for rel, h in marker["items"][key]["files"].items():
            fd = file_dest(proj, key, rel)
            if os.path.isfile(fd) and sha(fd) == h:
                os.remove(fd)
                rmdirs_up(fd, os.path.join(proj, ".claude", key.split("/")[0]))
        del marker["items"][key]
        changed = True
    marker["loaded_at"] = datetime.datetime.now().isoformat(timespec="seconds")
    marker["store"] = p["store"]
    jwrite(mpath, marker)
    return marker, notes, changed


def registry_set(p, proj, marker):
    reg = jread(p["reg"], {"projects": {}})
    if marker is None:
        reg["projects"].pop(proj, None)
    else:
        s, a = counts(marker["items"])
        reg["projects"][proj] = {"at": marker.get("loaded_at"), "skills": s, "agents": a}
    jwrite(p["reg"], reg)


def cmd_load(a, quiet_text=False):
    p = P(cfg_dir(a))
    proj = os.path.abspath(a.project or os.getcwd())
    items = store_items(p)
    if not items:
        print("vault-mode: the vault kit is not installed (nothing in %s). Run /update-rbxdev-vault, or the setup in SETUP-FOR-CLAUDE.md." % p["store"])
        return 2
    if a.no_link:
        s, g = counts(items)
        print("Roblox dev mode on (this session only, nothing written): %d skills, %d agents, %s, %s" % (s, g, ref_line(p), learn_line(p)))
        if not a.no_text:
            print()
            cmd_mode_text(a)
        return 0
    why = guard(proj, p)
    if why:
        print("vault-mode: not loaded. " + why)
        return 2
    had_sk = os.path.isdir(os.path.join(proj, ".claude", "skills"))
    first = not os.path.isfile(os.path.join(proj, ".claude", "vault-mode.json"))
    marker, notes, changed = link(proj, p)
    hidden = exclude_write(proj, marker["items"].keys())
    registry_set(p, proj, marker)
    s, g = counts(marker["items"])
    print("Roblox dev mode on: %d skills, %d agents, %s, %s" % (s, g, ref_line(p), learn_line(p)))
    print("  folder: %s  (copies in .claude/skills and .claude/agents, %s; /unload-rbxdev-vault removes exactly these)" % (proj, "hidden from git" if hidden else "not a git repository, nothing to hide"))
    if first and not had_sk:
        print("  RESTART NEEDED for the slash commands: Claude Code reads a new .claude/skills folder only at start. Type /exit, then run `claude -c` (continues this conversation) and /game-dev-workflow etc. are listed.")
        print("  Until then the mode already works: use the vault skills by reading their SKILL.md in %s." % p["sk"])
    elif first:
        print("  skills are usable now (this folder already had .claude/skills when the session started)")
    print("  agents are registered at session start (restart as above for them to be listed); until then spawn a general-purpose subagent with the agent file from %s as its brief" % p["ag"])
    for n in notes:
        print("  note: " + n)
    if not a.no_text:
        print()
        cmd_mode_text(a)
    return 0


def cmd_mode_text(a):
    p = P(cfg_dir(a))
    try:
        sys.stdout.write(open(p["rules"], encoding="utf-8").read())
    except OSError:
        print("(mode rules file missing: %s)" % p["rules"])
    return 0


def cmd_unload(a):
    p = P(cfg_dir(a))
    if a.all:
        projs = list(jread(p["reg"], {"projects": {}})["projects"].keys())
    else:
        projs = [os.path.abspath(a.project or os.getcwd())]
    if not projs:
        print("Roblox dev mode is not loaded in any folder.")
        return 0
    for proj in projs:
        mpath = os.path.join(proj, ".claude", "vault-mode.json")
        marker = jread(mpath, None)
        if not marker:
            print("Roblox dev mode was not loaded in %s (no .claude/vault-mode.json); nothing removed." % proj)
            registry_set(p, proj, None)
            continue
        removed = kept = 0
        left = []
        for key, rec in marker["items"].items():
            for rel, h in rec["files"].items():
                fd = file_dest(proj, key, rel)
                if not os.path.isfile(fd):
                    continue
                if sha(fd) == h:
                    os.remove(fd)
                    removed += 1
                else:
                    kept += 1
                    print("  kept %s (you changed it)" % os.path.relpath(fd, proj))
        os.remove(mpath)
        for key in marker["items"]:
            d = dest_of(proj, key)
            if key.startswith("skills/") and not prune_empty(d) and not has_files(d):
                left.append(d)
        for c in sorted(marker.get("created", []), key=len, reverse=True):
            d = os.path.join(proj, *c.split("/"))
            if not prune_empty(d) and not has_files(d):
                left.append(d)
        if marker.get("created_claude"):
            d = os.path.join(proj, ".claude")
            try:
                os.rmdir(d)
            except OSError:
                if os.path.isdir(d) and not has_files(d):
                    left.append(d)
        exclude_write(proj, [])
        registry_set(p, proj, None)
        if left:
            reg = jread(p["reg"], {"projects": {}})
            reg.setdefault("leftovers", [])
            reg["leftovers"] = sorted(set(reg["leftovers"]) | set(left))
            jwrite(p["reg"], reg)
            print("  (empty folders could not be deleted while Claude is running; they are removed by the next /update-rbxdev-vault or when you run /unload-rbxdev-vault again after quitting)")
        print("Roblox dev mode off in %s: removed %d vault file(s)%s. Skills/agents already listed in this session stay listed until you restart Claude (/exit, then `claude -c`); the mode rules no longer apply." % (proj, removed, (", kept %d you changed" % kept) if kept else ""))
    return 0


def cold_files(p):
    out = {}
    for rel in sorted(tree(p["cold"])) if os.path.isdir(p["cold"]) else []:
        out.setdefault(rel.split("/")[0], []).append(rel)
    return out


def cmd_cold(a):
    p = P(cfg_dir(a))
    base = os.path.realpath(p["cold"])
    arg = (a.target or "").strip().replace("\\", "/").strip("/")
    files = cold_files(p)
    if not files:
        print("vault-mode: no cold area at %s (run /update-rbxdev-vault)." % p["cold"], file=sys.stderr)
        return 2
    if not arg:
        for t, fs in files.items():
            print("%s: %s" % (t, " ".join(f.split("/", 1)[1] for f in fs)))
        return 0
    full = os.path.realpath(os.path.join(base, *arg.split("/")))
    if full != base and not full.startswith(base + os.sep):
        print("vault-mode: %r is outside the cold area." % arg, file=sys.stderr)
        return 2
    if os.path.isdir(full):
        print(chr(10).join(files.get(arg, [])) or "(empty)")
        return 0
    if not os.path.isfile(full):
        print("vault-mode: no cold file %r. Topics: %s" % (arg, ", ".join(files)), file=sys.stderr)
        return 2
    if a.path:
        print(full)
        return 0
    with open(full, encoding="utf-8", errors="replace") as f:
        sys.stdout.write(f.read())
    return 0


def cmd_status(a):
    p = P(cfg_dir(a))
    proj = os.path.abspath(a.project or os.getcwd())
    items = store_items(p)
    s, g = counts(items)
    marker = jread(os.path.join(proj, ".claude", "vault-mode.json"), None)
    if marker:
        ls, lg = counts(marker["items"])
        print("Roblox dev mode: ON in %s (%d skills, %d agents, since %s)" % (proj, ls, lg, marker.get("loaded_at", "?")))
    else:
        print("Roblox dev mode: off in %s (type /load-rbxdev-vault to turn it on)" % proj)
    print("vault store: %s (%d skills, %d agents) %s" % (p["store"], s, g, "" if items else "NOT INSTALLED: run /update-rbxdev-vault"))
    others = [k for k in jread(p["reg"], {"projects": {}})["projects"] if os.path.realpath(k) != os.path.realpath(proj)]
    if others:
        print("also loaded in: " + ", ".join(others[:8]) + (" ..." if len(others) > 8 else ""))
    print("always-on commands: " + ", ".join("/" + x for x in always_on(p)))
    cf = cold_files(p)
    print("cold area: %s (%d files in %d topics; read on demand, never copied into projects)" % (p["cold"], sum(len(v) for v in cf.values()), len(cf)))
    rl = jread(os.path.join(p["store"], "rename-last.json"), None)
    if rl and rl.get("moved"):
        print("commands renamed or merged on %s: every vault command now ends in -%s-vault (old -> new list: %s)" % (rl.get("at", "?"), rl.get("slug", "?"), os.path.join(p["c"], "claude-kit", "COMMANDS-RENAMED.txt")))
    old = [k for k in old_layout(p)]
    if old:
        print("OLD LAYOUT: %d vault skill/agent files are still in %s (they load in every session). Run /update-rbxdev-vault to move them." % (len(old), p["c"]))
    print("%s; %s" % (ref_line(p), learn_line(p)))
    return 0


def sweep_leftovers(p):
    reg = jread(p["reg"], {"projects": {}})
    keep = [d for d in reg.get("leftovers", []) if os.path.isdir(d) and not prune_empty(d)]
    if keep != reg.get("leftovers", []):
        reg["leftovers"] = keep
        jwrite(p["reg"], reg)


def cmd_sync(a):
    p = P(cfg_dir(a))
    sweep_leftovers(p)
    reg = jread(p["reg"], {"projects": {}})
    n = 0
    for proj in list(reg["projects"].keys()):
        if not os.path.isfile(os.path.join(proj, ".claude", "vault-mode.json")):
            registry_set(p, proj, None)
            continue
        if guard(proj, p):
            continue
        marker, notes, changed = link(proj, p)
        if changed:
            exclude_write(proj, marker["items"].keys())
            registry_set(p, proj, marker)
            n += 1
            if not a.quiet:
                print("vault-mode: refreshed %s" % proj)
    if n and a.quiet:
        print("vault-mode: refreshed Roblox dev mode in %d folder(s)" % n)
    return 0


# ---------------------------------------------------------------- migration of the old always-on layout
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


def old_layout_entries(p, manifest):
    ao = set(always_on(p))
    keep_lum = False
    try:
        keep_lum = "low-usage-mode-rbxdev-vault/scripts/lum" in open(os.path.join(p["c"], "settings.json"), encoding="utf-8", errors="replace").read()
    except OSError:
        pass
    res = []
    for rel, h in manifest.items():
        parts = rel.split("/")
        if parts[0] == "skills" and len(parts) >= 3 and parts[1] not in ao:
            if keep_lum and parts[1] == "low-usage-mode-rbxdev-vault" and parts[2] == "scripts":
                continue            # the user's settings.json hooks call these paths; they stay until the hooks are re-installed
            res.append((rel, h))
        elif parts[0] == "agents" and len(parts) == 2 and parts[1].endswith(".md"):
            res.append((rel, h))
    return res


def old_layout(p):
    man = read_manifest(os.path.join(p["c"], "claude-kit", "installed.tsv"))
    return [rel for rel, h in old_layout_entries(p, man) if os.path.isfile(os.path.join(p["c"], *rel.split("/")))]


def cmd_migrate(a):
    p = P(cfg_dir(a))
    c = p["c"]
    lay = jread(p["layout"], {})
    if a.revert:
        last = jread(os.path.join(c, "claude-kit", "vault-mode", "migration-last.json"), None)
        if not last:
            print("vault-mode: no migration to revert.")
            return 0
        n = 0
        for rec in last["moved"]:
            src = os.path.join(last["backup"], *rec["rel"].split("/"))
            dst = os.path.join(c, *rec["rel"].split("/"))
            if os.path.isfile(src) and not os.path.exists(dst):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(src, dst)
                n += 1
        lay["auto"] = False
        jwrite(p["layout"], lay)
        print("vault-mode: restored %d file(s) to the old always-on layout (they load in every session again). Automatic migration is now off; `vault-mode.py migrate` turns it on again." % n)
        return 0
    if lay.get("auto") is False and not a.force:
        return 0
    mfile = a.old_manifest or os.path.join(c, "claude-kit", "installed.tsv.pre-mode")
    if not os.path.isfile(mfile):
        mfile = os.path.join(c, "claude-kit", "installed.tsv")
    man = read_manifest(mfile)
    ents = old_layout_entries(p, man)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = os.path.join(c, "claude-kit", "backup", "mode-migration-" + stamp)
    moved, edited, dirs = [], [], set()
    for rel, h in ents:
        f = os.path.join(c, *rel.split("/"))
        if not os.path.isfile(f):
            continue
        is_edit = sha(f) != h
        if a.dry_run:
            moved.append({"rel": rel, "edited": is_edit})
            continue
        dst = os.path.join(backup, *rel.split("/"))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(f, dst)
        moved.append({"rel": rel, "edited": is_edit, "sha": h})
        dirs.add((os.path.dirname(f), os.path.join(c, rel.split("/")[0])))
    if not moved:
        if not a.dry_run:
            lay.update({"layout": 1})
            jwrite(p["layout"], lay)
            if os.path.basename(mfile) == "installed.tsv.pre-mode":
                os.remove(mfile)
        return 0
    if a.dry_run:
        print("vault-mode: would move %d old always-on vault file(s) out of %s/skills and %s/agents (%d edited by you; those are backed up too)." % (len(moved), c, c, sum(1 for m in moved if m["edited"])))
        return 0
    for d, stop in sorted(dirs, key=lambda x: len(x[0]), reverse=True):
        rmdirs_up(d, stop)
    left = [os.path.join(c, "skills", n) for n in sorted(set(r["rel"].split("/")[1] for r in moved if r["rel"].startswith("skills/"))) if os.path.isdir(os.path.join(c, "skills", n))]
    if os.path.basename(mfile) == "installed.tsv.pre-mode":
        shutil.move(mfile, os.path.join(backup, "installed.tsv.pre-mode"))
    info = {"at": stamp, "backup": backup, "moved": moved, "manifest": mfile}
    jwrite(os.path.join(backup, "migration.json"), info)
    jwrite(os.path.join(c, "claude-kit", "vault-mode", "migration-last.json"), info)
    lay.update({"layout": 1, "auto": True, "migrated": stamp})
    jwrite(p["layout"], lay)
    ns = len(set(m["rel"].split("/")[1] for m in moved if m["rel"].startswith("skills/")))
    na = len([m for m in moved if m["rel"].startswith("agents/")])
    print("vault-mode: moved %d vault skills and %d agents out of your always-on %s/skills and /agents into the on-demand store (backup + list: %s). "
          "Claude sessions no longer load the vault unless you type /load-rbxdev-vault; your own skills, agents and CLAUDE.md were not touched. Undo: vault-mode.py migrate --revert."
          % (ns, na, c, backup))
    for m in moved:
        if m["edited"]:
            print("  you had edited %s: your version is in the backup" % m["rel"])
    for d in left:
        print("  left in place (contains files that are not from the kit): %s" % d)
    return 0


# ---------------------------------------------------------------- opt-in auto load
def looks_roblox(proj):
    try:
        names = os.listdir(proj)
    except OSError:
        return False
    return any(fnmatch.fnmatch(n, pat) for n in names for pat in ROBLOX_MARKERS)


def cmd_auto(a):
    p = P(cfg_dir(a))
    proj = os.path.abspath(a.project or os.getcwd())
    if not (a.always or looks_roblox(proj)):
        return 0
    if not store_items(p) or guard(proj, p):
        return 0
    marker, notes, changed = link(proj, p)
    exclude_write(proj, marker["items"].keys())
    registry_set(p, proj, marker)
    s, g = counts(marker["items"])
    print("Roblox dev mode on (auto-loaded for this Roblox project): %d skills, %d agents, %s, %s. /unload-rbxdev-vault turns it off." % (s, g, ref_line(p), learn_line(p)))
    print()
    cmd_mode_text(a)
    return 0


def cmd_snippet(a):
    cmd = 'sh "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/pyrun" "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/vault-mode.py" auto'
    print(json.dumps({"hooks": {"SessionStart": [{"matcher": "startup|resume", "hooks": [{"type": "command", "command": cmd, "timeout": 20}]}]}}, indent=2))
    print("\n# Add this to a project's .claude/settings.json (that project only) or ~/.claude/settings.json (every project; the hook still loads only for folders with a Roblox marker: " + ", ".join(ROBLOX_MARKERS) + ").")
    print("# Add `--always` after `auto` to load in every folder. Nothing in the kit adds this for you.")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(prog="vault-mode.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config")
    sp = ap.add_subparsers(dest="cmd", required=True)
    for name in ("load", "unload", "status", "sync", "migrate", "auto", "autoload-snippet", "mode-text", "cold"):
        s = sp.add_parser(name)
        s.add_argument("--config", default=argparse.SUPPRESS)
        if name in ("load", "unload", "status", "auto"):
            s.add_argument("--project")
        if name == "load":
            s.add_argument("--no-link", action="store_true")
            s.add_argument("--no-text", action="store_true")
        if name == "unload":
            s.add_argument("--all", action="store_true")
        if name == "sync":
            s.add_argument("--quiet", action="store_true")
        if name == "migrate":
            s.add_argument("--dry-run", action="store_true")
            s.add_argument("--revert", action="store_true")
            s.add_argument("--force", action="store_true")
            s.add_argument("--old-manifest")
        if name == "auto":
            s.add_argument("--always", action="store_true")
        if name == "cold":
            s.add_argument("target", nargs="?")
            s.add_argument("--path", action="store_true")
    a = ap.parse_args(argv)
    fn = {"load": cmd_load, "unload": cmd_unload, "status": cmd_status, "sync": cmd_sync, "migrate": cmd_migrate, "auto": cmd_auto, "autoload-snippet": cmd_snippet, "mode-text": cmd_mode_text, "cold": cmd_cold}[a.cmd]
    try:
        return fn(a) or 0
    except Exception as e:      # never break a hook or the refresh
        if a.cmd in ("auto", "sync"):
            return 0
        print("vault-mode: failed: %r" % (e,), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
