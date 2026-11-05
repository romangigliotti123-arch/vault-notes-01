#!/usr/bin/env python3
"""vault-mode.py: Roblox dev mode for the vault kit. Standard library only. Never edits settings.json, never touches ~/.claude/CLAUDE.md.

The kit's skills and agents are NOT installed where every Claude Code session reads them. They live in an on-demand store:
    <config>/claude-kit/vault-mode/.claude/skills/<name>/   <config>/claude-kit/vault-mode/.claude/agents/<name>.md   <config>/claude-kit/vault-mode/CLAUDE.md (the mode rules)
Only the names in <config>/claude-kit/vault-mode/always-on.txt (rbx-load, rbx-unload, rbx-update, rbx-check, rbx-uninstall) stay in <config>/skills.

  load   [--project DIR] [--no-link] [--no-text]   copy the store's skills/agents into DIR/.claude/skills|agents (DIR = current folder), list them in DIR/.claude/vault-mode.json,
                                                   hide them from git (.git/info/exclude; never Games/), print the confirmation, the Games folder line + the mode rules. --no-link: write nothing (session started with --add-dir).
                                                   In HOME / the config folder / inside it, load is session-only: writes nothing, prints the rules + a skill/agent index.
  unload [--project DIR | --all]                   remove exactly what load added (files whose content is unchanged); never a file of yours
  status [--project DIR]                           mode state of this folder + store/migration summary
  sync   [--quiet]                                 after an update: refresh every folder that has the mode loaded (kit-refresh runs this)
  migrate [--dry-run | --revert] [--old-manifest F] move the old always-on kit skills/agents out of <config>/skills|agents into the store (backup + manifest, idempotent, reversible)
  auto   [--project DIR] [--always]                for an OPT-IN SessionStart hook: load when DIR looks like a Roblox project (or --always), print the mode rules; silent otherwise
  autoload-snippet                                 print the settings.json hook an owner can add by hand to enable auto
  mode-text                                        print the mode rules
  cold   [TOPIC[/FILE]] [--path]                   cold area (<store>/cold: bulk that skills point to with [cold:TOPIC/FILE]; never copied into projects): no argument lists topics, TOPIC lists files,
                                                   TOPIC/FILE prints the file (--path: only its path)
Config dir: --config DIR, else $CLAUDE_CONFIG_DIR, else $CLAUDE_KIT_HOME/.claude, else ~/.claude.
"""
import argparse
import datetime
import fnmatch
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

ALWAYS_ON_DEFAULT = ["rbx-load", "rbx-unload", "rbx-update", "rbx-check", "rbx-uninstall"]
MB = "# >>> roblox-vault-mode (managed by /rbx-load, removed by /rbx-unload) >>>"
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


def nsha(p):
    with open(p, "rb") as f:
        d = f.read()
    return hashlib.sha256(d if b"\0" in d[:8192] else d.replace(b"\r\n", b"\n")).hexdigest()


def conflict_note(p, proj, key, rel, fd, srcf, h):
    """a project copy you edited is kept: save the incoming version under claude-kit/state/conflicts/projects/ and list it (kit-conflicts.py)"""
    cf = os.path.join(p["c"], "claude-kit", "state", "conflicts.json")
    doc = jread(cf, {})
    items = doc["items"] if isinstance(doc.get("items"), dict) else {}
    acked = doc["acked"] if isinstance(doc.get("acked"), dict) else {}
    ek = "project:%s|%s/%s" % (proj, key, rel)
    prev = items.get(ek)
    if acked.get(ek) == h or (prev and prev.get("incoming") == h):
        return
    sv = os.path.join(p["c"], "claude-kit", "state", "conflicts", "projects", hashlib.sha1(proj.encode("utf-8")).hexdigest()[:8], *(key + "/" + rel + ".vault-new").split("/"))
    try:
        os.makedirs(os.path.dirname(sv), exist_ok=True)
        shutil.copyfile(srcf, sv)
    except OSError:
        sv = ""
    items[ek] = {"kind": "project", "project": proj, "key": key, "rel": rel, "file": fd, "incoming": h, "notified": False, "at": datetime.date.today().isoformat(),
                 "saved": os.path.relpath(sv, p["c"]).replace(os.sep, "/") if sv else ""}
    doc["items"], doc["acked"] = items, acked
    doc.setdefault("v", 1)
    jwrite(cf, doc)


def jread(p, default):
    try:
        with open(p, "r", encoding="utf-8") as f:
            v = json.load(f)
    except (OSError, ValueError):
        return default
    return v if default is None or isinstance(v, type(default)) else default


def jwrite(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = "%s.%d.tmp" % (p, os.getpid())
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


KEY_RX = re.compile(r"skills/[A-Za-z0-9][A-Za-z0-9._-]*|agents/[A-Za-z0-9][A-Za-z0-9._-]*\.md")


def rel_ok(rel):
    return isinstance(rel, str) and bool(rel) and not rel.startswith("/") and ":" not in rel and "\\" not in rel and all(x not in ("", ".", "..") for x in rel.split("/"))


def clean_marker(m):
    """a project's .claude/vault-mode.json is untrusted data (a repository can ship one): keep only well-formed skill/agent keys and plain relative file names"""
    if not isinstance(m, dict):
        return m
    items = {}
    for k, rec in (m.get("items") if isinstance(m.get("items"), dict) else {}).items():
        files = rec.get("files") if isinstance(rec, dict) else None
        if not isinstance(k, str) or not KEY_RX.fullmatch(k) or not isinstance(files, dict):
            continue
        items[k] = {"files": {r: h for r, h in files.items() if rel_ok(r) and isinstance(h, str)}}
    m["items"] = items
    m["created"] = [c for c in (m.get("created") if isinstance(m.get("created"), list) else []) if c in (".claude/skills", ".claude/agents")]
    return m


def owned(proj, fd):
    """True when fd really lies inside <proj>/.claude (symlinks resolved): nothing outside it is ever deleted"""
    rc = os.path.realpath(os.path.join(proj, ".claude"))
    return os.path.realpath(fd).startswith(rc + os.sep)


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


def glob_escape(s):
    return re.sub(r"([\\*?\[])", r"\\\1", s)


def exclude_write(proj, keys):
    g = git_exclude(proj)
    if not g:
        return False
    ex, pre = g
    pre = glob_escape(pre)
    try:
        old = open(ex, encoding="utf-8", errors="surrogateescape").read() if os.path.exists(ex) else ""
    except OSError:
        return False
    base = exclude_strip(old)
    if keys:
        lines = [MB, "/" + pre + ".claude/vault-mode.json"] + ["/" + pre + ".claude/" + k + ("/" if k.startswith("skills/") else "") for k in sorted(keys)] + [ME]
        base = (base.rstrip("\n") + "\n" if base.strip() else "") + "\n".join(lines) + "\n"
    try:
        os.makedirs(os.path.dirname(ex), exist_ok=True)
        with open(ex, "w", encoding="utf-8", errors="surrogateescape", newline="\n") as f:
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
                "Open Claude in a project folder (for example your Roblox game's folder) and run /rbx-load there." % proj)
    if rp == os.path.realpath(os.path.expanduser("~")):
        return "your home folder is not a project: loading here would put the vault into every session started below it. Open Claude in a project folder and run /rbx-load there."
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
    return "reference images not downloaded yet (/rbx-update fetches them)"


def learn_line(p):
    if not os.path.isfile(os.path.join(p["c"], "claude-kit", "tools", "learn.py")):
        return "learn step unavailable (learn.py missing)"
    pend = os.path.join(p["c"], "claude-kit", "state", "learnings-queue", "pending")
    if not os.path.isdir(pend):
        pend = os.path.join(p["c"], "claude-kit", "learnings-queue", "pending")
    n = len([x for x in os.listdir(pend)]) if os.path.isdir(pend) else 0
    return "learn step on" + (" (%d note%s queued)" % (n, "" if n == 1 else "s") if n else "")


def counts(keys):
    return sum(1 for k in keys if k.startswith("skills/")), sum(1 for k in keys if k.startswith("agents/"))


class Lock(object):
    """advisory lock file: waits up to 30 s for another run, takes over a lock older than 120 s, never blocks for good"""

    def __init__(self, path):
        self.path, self.have = path, False

    def __enter__(self):
        end = time.time() + 30
        while True:
            try:
                os.makedirs(os.path.dirname(self.path), exist_ok=True)
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                self.have = True
                return self
            except FileExistsError:
                try:
                    if time.time() - os.path.getmtime(self.path) > 120:
                        os.remove(self.path)
                        continue
                except OSError:
                    pass
            except OSError:
                return self
            if time.time() > end:
                return self
            time.sleep(0.2)

    def __exit__(self, *exc):
        if self.have:
            try:
                os.remove(self.path)
            except OSError:
                pass
        return False


def put_file(s, d):
    t = d + ".vmtmp"
    if os.path.lexists(t):
        os.remove(t)
    shutil.copyfile(s, t)
    try:
        os.replace(t, d)
    except PermissionError:
        os.chmod(d, 0o644)
        os.replace(t, d)


def link(proj, p, quiet=False):
    """create/refresh the project copies. Returns (marker, notes, changed)"""
    items = store_items(p)
    mpath = os.path.join(proj, ".claude", "vault-mode.json")
    marker = clean_marker(jread(mpath, {"items": {}, "created": []}))
    if not isinstance(marker, dict):
        marker = {"items": {}, "created": []}
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
        if not mine:
            marker["items"][key] = {"files": dict(files)}
            jwrite(mpath, marker)
            mine = marker["items"][key]
        rec = dict((mine or {}).get("files", {}))
        newrec = {}
        for rel, h in files.items():
            fd = file_dest(proj, key, rel)
            cur = sha(fd) if os.path.isfile(fd) else None
            if cur == h:
                newrec[rel] = h
                continue
            if cur is not None and rec.get(rel) != cur:
                newrec[rel] = rec.get(rel, cur)
                sf = file_src(src, key, rel)
                if nsha(fd) == nsha(sf):
                    continue
                notes.append("kept your edited %s (not refreshed)" % os.path.relpath(fd, proj))
                conflict_note(p, proj, key, rel, fd, sf, h)
                continue
            os.makedirs(os.path.dirname(fd), exist_ok=True)
            put_file(file_src(src, key, rel), fd)
            newrec[rel] = h
            changed = True
        for rel, h in rec.items():          # file left the kit: remove if unchanged
            if rel not in files:
                fd = file_dest(proj, key, rel)
                if os.path.isfile(fd) and owned(proj, fd) and sha(fd) == h:
                    os.remove(fd)
                    rmdirs_up(fd, os.path.join(proj, ".claude", key.split("/")[0]))
                    changed = True
        marker["items"][key] = {"files": newrec}
    for key in [k for k in marker["items"] if k not in items]:   # whole skill/agent left the kit
        for rel, h in marker["items"][key]["files"].items():
            fd = file_dest(proj, key, rel)
            if os.path.isfile(fd) and owned(proj, fd) and sha(fd) == h:
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
    if not isinstance(reg.get("projects"), dict):
        reg["projects"] = {}
    if marker is None:
        reg["projects"].pop(proj, None)
    else:
        s, a = counts(marker["items"])
        reg["projects"][proj] = {"at": marker.get("loaded_at"), "skills": s, "agents": a}
    jwrite(p["reg"], reg)


def one_line(path):
    try:
        t = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""
    m = re.search(r"^description:\s*(.+?)\s*$", t, re.M)
    d = (m.group(1) if m else "").strip().strip("\"'")
    d = re.split(r"(?<=[.:;])\s", d, 1)[0]
    return d if len(d) <= 110 else d[:107].rstrip() + "..."


def games_line(proj, p):
    if guard(proj, p):
        return "Games folder: open a project folder to build games (nothing is created in HOME)"
    gd, found = os.path.join(proj, "Games"), []
    for d in sorted(os.listdir(gd)) if os.path.isdir(gd) else []:
        try:
            found.append("%s %s" % (d, re.search(r"^stage:\s*(\S+)", open(os.path.join(gd, d, "GAME.md"), encoding="utf-8", errors="replace").read(3000), re.M).group(1)))
        except (OSError, AttributeError):
            pass
    return "Games folder: ./Games (%s)" % (("%d game%s: %s%s" % (len(found), "s"[:len(found) != 1], ", ".join(found[:4]), ", ..." * (len(found) > 4))) if found else "none yet")


def session_only(a, p, items):
    s, g = counts(items)
    ao = set(always_on(p))
    print("Roblox dev mode loaded for this session only (no folder changed): %d skills, %d agents, %s, %s" % (s, g, ref_line(p), learn_line(p)))
    print("  a project folder gives the full persistent mode (slash commands, agents listed).")
    print("  " + games_line(os.path.abspath(a.project or os.getcwd()), p))
    if not a.no_text:
        print()
        cmd_mode_text(a)
        print()
        print("Session index (nothing is installed here): when a task matches, Read that SKILL.md first and follow it; for an agent, spawn a general-purpose subagent with its file as the brief.")
        for key, (src, files) in items.items():
            name = key.split("/", 1)[1]
            if name in ao:
                continue
            path = os.path.join(src, "SKILL.md") if key.startswith("skills/") else src
            print("- %s: %s [%s]" % (name[:-3] if name.endswith(".md") else name, one_line(path), path))
    return 0


def cmd_load(a, quiet_text=False):
    p = P(cfg_dir(a))
    proj = os.path.abspath(a.project or os.getcwd())
    items = store_items(p)
    if not items:
        print("vault-mode: the vault kit is not installed (nothing in %s). Run /rbx-update, or the setup in SETUP-FOR-CLAUDE.md." % p["store"])
        return 2
    if a.no_link:
        s, g = counts(items)
        print("Roblox dev mode on (this session only, nothing written): %d skills, %d agents, %s, %s" % (s, g, ref_line(p), learn_line(p)))
        print("  " + games_line(proj, p))
        if not a.no_text:
            print()
            cmd_mode_text(a)
        return 0
    if guard(proj, p):
        return session_only(a, p, items)
    had_sk = os.path.isdir(os.path.join(proj, ".claude", "skills"))
    first = not os.path.isfile(os.path.join(proj, ".claude", "vault-mode.json"))
    marker, notes, changed = link(proj, p)
    hidden = exclude_write(proj, marker["items"].keys())
    registry_set(p, proj, marker)
    s, g = counts(marker["items"])
    print("Roblox dev mode on: %d skills, %d agents, %s, %s" % (s, g, ref_line(p), learn_line(p)))
    print("  " + games_line(proj, p))
    print("  folder: %s  (copies in .claude/skills and .claude/agents, %s; /rbx-unload removes exactly these)" % (proj, "hidden from git" if hidden else "not a git repository, nothing to hide"))
    if first and not had_sk:
        print("  RESTART NEEDED for the slash commands: Claude Code reads a new .claude/skills folder only at start. Type /exit, then run `claude -c` (continues this conversation) and /rbx-workflow etc. are listed.")
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
        marker = clean_marker(jread(mpath, None))
        if not marker:
            if guard(proj, p):
                print("Nothing to remove in %s: Roblox dev mode here was session-only and wrote nothing. Stop following the vault mode rules; a new session starts clean." % proj)
                registry_set(p, proj, None)
                continue
            print("Roblox dev mode was not loaded in %s (no .claude/vault-mode.json); nothing removed." % proj)
            registry_set(p, proj, None)
            continue
        removed = kept = 0
        left = []
        for key, rec in marker.get("items", {}).items():
            for rel, h in (rec.get("files") or {}).items():
                fd = file_dest(proj, key, rel)
                if os.path.lexists(fd + ".vmtmp"):
                    os.remove(fd + ".vmtmp")
                if not os.path.isfile(fd):
                    continue
                if not owned(proj, fd):
                    kept += 1
                    print("  kept %s (outside the project's .claude folder)" % fd)
                elif sha(fd) == h:
                    os.remove(fd)
                    removed += 1
                else:
                    kept += 1
                    print("  kept %s (you changed it)" % os.path.relpath(fd, proj))
        os.remove(mpath)
        for key in marker.get("items", {}):
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
            print("  (empty folders could not be deleted while Claude is running; they are removed by the next /rbx-update or when you run /rbx-unload again after quitting)")
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
        print("vault-mode: no cold area at %s (run /rbx-update)." % p["cold"], file=sys.stderr)
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
    marker = clean_marker(jread(os.path.join(proj, ".claude", "vault-mode.json"), None))
    if marker:
        ls, lg = counts(marker["items"])
        print("Roblox dev mode: ON in %s (%d skills, %d agents, since %s)" % (proj, ls, lg, marker.get("loaded_at", "?")))
    else:
        print("Roblox dev mode: off in %s (type /rbx-load to turn it on%s)" % (proj, "; here it loads for the session only, nothing is written" if guard(proj, p) else ""))
    print(games_line(proj, p))
    print("vault store: %s (%d skills, %d agents) %s" % (p["store"], s, g, "" if items else "NOT INSTALLED: run /rbx-update"))
    others = [k for k in jread(p["reg"], {"projects": {}})["projects"] if os.path.realpath(k) != os.path.realpath(proj)]
    if others:
        print("also loaded in: " + ", ".join(others[:8]) + (" ..." if len(others) > 8 else ""))
    print("always-on commands: " + ", ".join("/" + x for x in always_on(p)))
    cf = cold_files(p)
    print("cold area: %s (%d files in %d topics; read on demand, never copied into projects)" % (p["cold"], sum(len(v) for v in cf.values()), len(cf)))
    rl = jread(os.path.join(p["store"], "rename-last.json"), None)
    if rl and rl.get("moved"):
        print("commands renamed or merged on %s: every vault command now starts with %s- (old -> new list: %s)" % (rl.get("at", "?"), rl.get("prefix", "rbx"), os.path.join(p["c"], "claude-kit", "COMMANDS-RENAMED.txt")))
    old = [k for k in old_layout(p)]
    if old:
        print("OLD LAYOUT: %d vault skill/agent files are still in %s (they load in every session). Run /rbx-update to move them." % (len(old), p["c"]))
    print("%s; %s" % (ref_line(p), learn_line(p)))
    kc = jread(os.path.join(p["c"], "claude-kit", "state", "conflicts.json"), {}).get("items")
    if isinstance(kc, dict) and kc:
        print("kept vault files: %d (you changed them, so updates left them as they are; review: python %s list)" % (len(kc), os.path.join(p["c"], "claude-kit", "tools", "kit-conflicts.py")))
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
        keep_lum = "rbx-low-usage/scripts/lum" in open(os.path.join(p["c"], "settings.json"), encoding="utf-8", errors="replace").read()
    except OSError:
        pass
    res = []
    for rel, h in manifest.items():
        parts = rel.split("/")
        if parts[0] == "skills" and len(parts) >= 3 and parts[1] not in ao:
            if keep_lum and parts[1] == "rbx-low-usage" and parts[2] == "scripts":
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
    if not a.dry_run:
        planned = [{"rel": rel, "edited": sha(os.path.join(c, *rel.split("/"))) != h, "sha": h} for rel, h in ents if os.path.isfile(os.path.join(c, *rel.split("/")))]
        if planned:
            jwrite(os.path.join(c, "claude-kit", "vault-mode", "migration-last.json"), {"at": stamp, "backup": backup, "moved": planned, "manifest": mfile})
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
          "Claude sessions no longer load the vault unless you type /rbx-load; your own skills, agents and CLAUDE.md were not touched. Undo: vault-mode.py migrate --revert."
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
    print("Roblox dev mode on (auto-loaded for this Roblox project): %d skills, %d agents, %s, %s. /rbx-unload turns it off." % (s, g, ref_line(p), learn_line(p)))
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
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(errors="replace")
        except Exception:
            pass
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
    store = P(cfg_dir(a))["store"]
    try:
        if a.cmd in ("load", "unload", "sync", "auto", "migrate") and os.path.isdir(store):
            with Lock(os.path.join(store, ".mode.lock")):
                return fn(a) or 0
        return fn(a) or 0
    except Exception as e:      # never break a hook or the refresh
        if a.cmd in ("auto", "sync"):
            return 0
        print("vault-mode: failed: %r" % (e,), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
