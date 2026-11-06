#!/usr/bin/env python3
"""vault-mode.py: INTERNAL tool of the vault kit (users never type it): it keeps the VAULT FOLDER permanently loaded. Standard library only. Never edits settings.json, never touches ~/.claude/CLAUDE.md.

The vault folder (the clone of the notes repository, e.g. ~/Obsidian/claudes-vault) is THE loaded environment: a Claude session started in it has all vault skills, agents and the vault rules, with no load command.
The kit's skills and agents are kept in an on-demand store (NOT read by other Claude sessions):
    <config>/claude-kit/vault-mode/.claude/skills/<name>/   <config>/claude-kit/vault-mode/.claude/agents/<name>.md   <config>/claude-kit/vault-mode/CLAUDE.md (the vault rules)
Only the names in <config>/claude-kit/vault-mode/always-on.txt (rbx-update, rbx-check, rbx-uninstall) stay in <config>/skills.

  home   [--kit DIR]                               print the vault folder this machine uses (the clone that holds the installing claude-kit folder, env CLAUDES_VAULT, the registered one, ~/Obsidian/claudes-vault); empty when none
  load   --project VAULT [--quiet] [--announce]    (installer / updater) copy the store's skills/agents + the rules block into VAULT/.claude (overwritten: the vault owns them), list them in VAULT/.claude/vault-mode.json,
                                                   hide them AND Games/ + Models/ from git (.git/info/exclude), register VAULT as the home, then remove the vault copies of every older loaded project folder (Games/ and Models/ there are left in place)
  unload [--project DIR | --all]                   remove exactly what load added (migration / uninstall)
  status [--project DIR]                           is DIR the loaded vault folder, where the vault is, store/migration summary
  sync   [--quiet]                                 refresh the registered vault folder (same as load --quiet) after an update
  migrate [--dry-run | --revert] [--old-manifest F] move the old always-on kit skills/agents out of <config>/skills|agents into the store (backup + manifest, idempotent, reversible)
  mode-text                                        print the vault rules
  cold   [TOPIC[/FILE]] [--path]                   cold area (<store>/cold: bulk that skills point to with [cold:TOPIC/FILE]; never copied into folders): no argument lists topics, TOPIC lists files,
                                                   TOPIC/FILE prints the file (--path: only its path)
Config dir: --config DIR, else $CLAUDE_CONFIG_DIR, else $CLAUDE_KIT_HOME/.claude, else ~/.claude.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

ALWAYS_ON_DEFAULT = ["rbx-update", "rbx-check", "rbx-uninstall"]
MB = "# >>> roblox-vault-mode (managed by the vault update) >>>"
ME = "# <<< roblox-vault-mode <<<"
MB_PREFIX = "# >>> roblox-vault-mode ("


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
    if m.get("rules_file") not in ("created", "user"):
        m.pop("rules_file", None)
    if m.get("rules_pre") not in ("", "\n", "\n\n"):
        m.pop("rules_pre", None)
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


def exclude_write(proj, keys, extra=()):
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
        lines = [MB, "/" + pre + ".claude/vault-mode.json"] + ["/" + pre + ".claude/" + k + ("/" if k.startswith("skills/") else "") for k in sorted(keys)] + ["/" + pre + x for x in extra] + [ME]
        base = (base.rstrip("\n") + "\n" if base.strip() else "") + "\n".join(lines) + "\n"
    try:
        os.makedirs(os.path.dirname(ex), exist_ok=True)
        with open(ex, "w", encoding="utf-8", errors="surrogateescape", newline="\n") as f:
            f.write(base)
    except OSError:
        return False
    return True


RB = "<!-- >>> roblox-vault-mode rules (managed by the vault update; rewritten on every update; edit outside it) >>> -->"
RB_PREFIX = "<!-- >>> roblox-vault-mode rules"
RE = "<!-- <<< roblox-vault-mode rules <<< -->"


def rules_path(proj):
    return os.path.join(proj, ".claude", "CLAUDE.md")


def rules_split(t):
    """(before, after) around the managed block, or None."""
    i = t.find(RB_PREFIX)
    if i < 0:
        return None
    j = t.find(RE, i)
    if j < 0:
        return None
    k = j + len(RE)
    if t[k:k + 2] == "\r\n":
        k += 2
    elif t[k:k + 1] == "\n":
        k += 1
    return t[:i], t[k:]


def rules_block(p):
    try:
        body = open(p["rules"], encoding="utf-8").read()
    except OSError:
        return None
    return RB + "\n" + body.rstrip("\n") + "\n" + RE + "\n"


def rules_write(proj, p, marker):
    """write/refresh the mode rules block in <proj>/.claude/CLAUDE.md. True when the file changed."""
    blk = rules_block(p)
    if not blk:
        return False
    f = rules_path(proj)
    try:
        old = open(f, encoding="utf-8", newline="").read() if os.path.isfile(f) else None
    except (OSError, UnicodeError):
        return False
    if old is None:
        new = blk
        marker["rules_file"] = "created"
    else:
        sp = rules_split(old)
        if sp:
            new = sp[0] + blk + sp[1]
        else:
            pre = "" if (not old or old.endswith("\n\n")) else ("\n" if old.endswith("\n") else "\n\n")
            new = old + pre + blk
            marker["rules_file"] = "user"
            marker["rules_pre"] = pre
    if new == old:
        return False
    try:
        os.makedirs(os.path.dirname(f), exist_ok=True)
        with open(f, "w", encoding="utf-8", newline="") as fh:
            fh.write(new)
    except OSError:
        return False
    return True


def rules_remove(proj, marker):
    f = rules_path(proj)
    if not marker.get("rules_file") or not os.path.isfile(f):
        return
    try:
        old = open(f, encoding="utf-8", newline="").read()
    except (OSError, UnicodeError):
        return
    sp = rules_split(old)
    if not sp:
        return
    before, after = sp
    pre = marker.get("rules_pre") or ""
    if pre and before.endswith(pre):
        before = before[:-len(pre)]
    new = before + after
    try:
        if not new.strip() and marker.get("rules_file") == "created":
            os.remove(f)
        else:
            with open(f, "w", encoding="utf-8", newline="") as fh:
                fh.write(new)
    except OSError:
        pass


def excl_keys(marker):
    ks = list(marker["items"].keys())
    if marker.get("rules_file") == "created" or marker.get("home"):
        ks.append("CLAUDE.md")
    return ks


HOME_EXTRA = ("Games/", "Models/")


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
        return "%s is (or is inside) your Claude config folder; its .claude folder would be your user-wide setup, which would load the vault in EVERY session. The vault folder is the only folder that is loaded." % proj
    if rp == os.path.realpath(os.path.expanduser("~")):
        return "your home folder is not the vault folder: loading here would put the vault into every session started below it."
    return None


def default_vault():
    base = os.environ.get("CLAUDE_KIT_HOME") or os.path.expanduser("~")
    return os.path.join(base, "Obsidian", "claudes-vault")


def is_vault_dir(d):
    return bool(d) and os.path.isdir(d) and os.path.exists(os.path.join(d, ".git"))


def registered_home(p):
    h = jread(p["reg"], {"projects": {}}).get("home")
    return h if isinstance(h, str) and h else None


def resolve_home(p, kit=None):
    """the vault folder: the clone that holds the installing claude-kit folder (it has vault-update.sh and a .git), env CLAUDES_VAULT, the registered one, ~/Obsidian/claudes-vault. None when there is no clone."""
    if kit:
        par = os.path.dirname(os.path.abspath(kit))
        if os.path.basename(os.path.abspath(kit)) == "claude-kit" and os.path.isfile(os.path.join(par, "vault-update.sh")) and is_vault_dir(par):
            return par
    env = os.environ.get("CLAUDES_VAULT")
    if env and os.path.isdir(env):
        return os.path.abspath(env)
    h = registered_home(p)
    if h and is_vault_dir(h):
        return h
    d = default_vault()
    return d if is_vault_dir(d) else None


def vault_hint(p):
    return resolve_home(p) or registered_home(p) or default_vault()


def is_vault_folder(proj, p):
    """True when proj is the loaded vault folder (marker with home:true)"""
    m = jread(os.path.join(proj, ".claude", "vault-mode.json"), None)
    return isinstance(m, dict) and m.get("home") is True


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


def link(proj, p, force=False):
    """create/refresh the folder copies (force: the vault folder, the vault owns them: overwritten, no keep logic). Returns (marker, notes, changed)"""
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
        if not force and not mine and os.path.exists(user_path):
            notes.append("skipped %s: you already have one of that name in %s (yours wins)" % (key, os.path.dirname(user_path)))
            continue
        dst = dest_of(proj, key)
        if not force and not mine and os.path.exists(dst):
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
            os.makedirs(os.path.dirname(fd), exist_ok=True)
            put_file(file_src(src, key, rel), fd)
            newrec[rel] = h
            changed = True
        for rel, h in rec.items():          # file left the kit: remove (project copies are vault-owned)
            if rel not in files:
                fd = file_dest(proj, key, rel)
                if os.path.isfile(fd) and owned(proj, fd):
                    os.remove(fd)
                    rmdirs_up(fd, os.path.join(proj, ".claude", key.split("/")[0]))
                    changed = True
        marker["items"][key] = {"files": newrec}
    for key in [k for k in marker["items"] if k not in items]:   # whole skill/agent left the kit
        for rel, h in marker["items"][key]["files"].items():
            fd = file_dest(proj, key, rel)
            if os.path.isfile(fd) and owned(proj, fd):
                os.remove(fd)
                rmdirs_up(fd, os.path.join(proj, ".claude", key.split("/")[0]))
        del marker["items"][key]
        changed = True
    if changed or "loaded_at" not in marker:
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
        if reg.get("home") == proj:
            reg.pop("home", None)
    else:
        s, a = counts(marker["items"])
        reg["projects"][proj] = {"at": marker.get("loaded_at"), "skills": s, "agents": a}
        if marker.get("home"):
            reg["home"] = proj
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


def elsewhere(what, p):
    return "%s: start a session in %s (Games/ and Models/ live in the vault folder; nothing is created here)" % (what, vault_hint(p))


def games_line(proj, p):
    if not is_vault_folder(proj, p):
        return elsewhere("Games folder", p)
    gd, found = os.path.join(proj, "Games"), []
    for d in sorted(os.listdir(gd)) if os.path.isdir(gd) else []:
        try:
            found.append("%s %s" % (d, re.search(r"^stage:\s*(\S+)", open(os.path.join(gd, d, "GAME.md"), encoding="utf-8", errors="replace").read(3000), re.M).group(1)))
        except (OSError, AttributeError):
            pass
    return "Games folder: %s (%s)" % (os.path.join(proj, "Games"), ("%d game%s: %s%s" % (len(found), "s"[:len(found) != 1], ", ".join(found[:4]), ", ..." * (len(found) > 4))) if found else "none yet")


def models_line(proj, p):
    if not is_vault_folder(proj, p):
        return elsewhere("Models library", p)
    md, n = os.path.join(proj, "Models"), 0
    for c in sorted(os.listdir(md)) if os.path.isdir(md) else []:
        cd = os.path.join(md, c)
        n += sum(1 for s in os.listdir(cd) if os.path.isfile(os.path.join(cd, s, "model.md"))) if os.path.isdir(cd) else 0
    return "Models library: %s (%d model%s)" % (md, n, "s"[:n != 1]) if n else "Models library: %s (empty)" % md


def retire_old(p, home):
    """remove the vault copies (and rules block) from every folder that an older kit loaded, except the vault folder. Games/ and Models/ there stay. Returns how many folders were cleaned."""
    reg = jread(p["reg"], {"projects": {}})
    n = 0
    for proj in list(reg.get("projects", {}).keys()):
        if os.path.realpath(proj) == os.path.realpath(home):
            continue
        if os.path.isfile(os.path.join(proj, ".claude", "vault-mode.json")):
            unload_one(p, proj, lambda s: None)
            n += 1
        registry_set(p, proj, None)
    return n


def cmd_home(a):
    p = P(cfg_dir(a))
    h = resolve_home(p, getattr(a, "kit", None))
    if h:
        print(h)
    return 0


def cmd_load(a):
    p = P(cfg_dir(a))
    q = getattr(a, "quiet", False)
    if not a.project:
        print("vault-mode: load needs --project <vault folder> (internal command; the installer and the updater run it).")
        return 2
    proj = os.path.abspath(a.project)
    items = store_items(p)
    if not items:
        print("vault-mode: the vault kit is not installed (nothing in %s). Run /rbx-update, or the setup in SETUP-FOR-CLAUDE.md." % p["store"])
        return 2
    why = guard(proj, p)
    if why:
        print("vault-mode: " + why)
        return 2
    if not os.path.isdir(proj):
        print("vault-mode: %s does not exist." % proj)
        return 2
    first = not os.path.isfile(os.path.join(proj, ".claude", "vault-mode.json"))
    marker, notes, changed = link(proj, p, force=True)
    marker["home"] = True
    rules_write(proj, p, marker)
    jwrite(os.path.join(proj, ".claude", "vault-mode.json"), marker)
    hidden = exclude_write(proj, excl_keys(marker), HOME_EXTRA)
    registry_set(p, proj, marker)
    n_old = retire_old(p, proj)
    s, g = counts(marker["items"])
    if not q:
        print("Vault folder loaded: %s (%d skills, %d agents, vault rules in .claude/CLAUDE.md, %s)" % (proj, s, g, "hidden from git, with your Games/ and Models/" if hidden else "not a git repository, nothing to hide"))
        print("  " + games_line(proj, p))
        print("  " + models_line(proj, p))
    if n_old:
        print("Vault copies removed from %d old project folder%s (your Games/ and Models/ there were left in place). Start sessions in %s instead." % (n_old, "s"[:n_old != 1], proj))
    if getattr(a, "announce", False) and (first or n_old):
        print("To use the vault, start a new Claude session in %s (that folder is loaded automatically; no load command is needed)." % proj)
    return 0


def cmd_mode_text(a):
    p = P(cfg_dir(a))
    try:
        sys.stdout.write(open(p["rules"], encoding="utf-8").read())
    except OSError:
        print("(mode rules file missing: %s)" % p["rules"])
    return 0


def unload_one(p, proj, say):
    """remove exactly what load added to proj. Returns (removed, kept) or None when proj had no marker."""
    mpath = os.path.join(proj, ".claude", "vault-mode.json")
    marker = clean_marker(jread(mpath, None))
    if not marker:
        return None
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
                say("  kept %s (outside the folder's .claude folder)" % fd)
            else:
                os.remove(fd)
                removed += 1
    rules_remove(proj, marker)
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
    return removed, kept


def cmd_unload(a):
    p = P(cfg_dir(a))
    if a.all:
        projs = list(jread(p["reg"], {"projects": {}})["projects"].keys())
    else:
        projs = [os.path.abspath(a.project or os.getcwd())]
    if not projs:
        print("The vault is not loaded in any folder.")
        return 0
    for proj in projs:
        r = unload_one(p, proj, print)
        if r is None:
            print("The vault was not loaded in %s (no .claude/vault-mode.json); nothing removed." % proj)
            registry_set(p, proj, None)
            continue
        print("Vault copies removed from %s: %d file(s)%s. Games/ and Models/ were not touched." % (proj, r[0], (", left %d outside the folder's .claude folder" % r[1]) if r[1] else ""))
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
    mpath = os.path.join(proj, ".claude", "vault-mode.json")
    marker = clean_marker(jread(mpath, None))
    vh = vault_hint(p)
    if marker and marker.get("home"):
        ls, lg = counts(marker["items"])
        print("Vault folder: this folder (%s) is the loaded vault: dev mode ON (%d skills, %d agents, refreshed %s)" % (proj, ls, lg, marker.get("loaded_at", "?")))
    elif os.path.isdir(vh) and os.path.realpath(proj).startswith(os.path.realpath(vh) + os.sep):
        print("Vault folder: you are inside the vault (%s) but not at its top: start the session in %s itself so its skills and rules load" % (proj, vh))
    else:
        print("Vault folder: dev mode is OFF in %s (not the vault folder). The vault is %s: start a Claude session there to use it%s" % (proj, vh, "" if os.path.isdir(vh) else " (folder not found: run the setup)"))
    print(games_line(proj, p))
    print(models_line(proj, p))
    print("vault store: %s (%d skills, %d agents) %s" % (p["store"], s, g, "" if items else "NOT INSTALLED: run /rbx-update"))
    print("always-on commands: " + ", ".join("/" + x for x in always_on(p)))
    cf = cold_files(p)
    print("cold area: %s (%d files in %d topics; read on demand, never copied into folders)" % (p["cold"], sum(len(v) for v in cf.values()), len(cf)))
    rl = jread(os.path.join(p["store"], "rename-last.json"), None)
    if rl and rl.get("moved"):
        print("commands renamed or merged on %s: every vault command now starts with %s- (old -> new list: %s)" % (rl.get("at", "?"), rl.get("prefix", "rbx"), os.path.join(p["c"], "claude-kit", "COMMANDS-RENAMED.txt")))
    old = [k for k in old_layout(p)]
    if old:
        print("OLD LAYOUT: %d vault skill/agent files are still in %s (they load in every session). Run /rbx-update to move them." % (len(old), p["c"]))
    print(ref_line(p))
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
    h = registered_home(p)
    if not h or not is_vault_dir(h):
        h = resolve_home(p)
    if not h:
        return 0
    a.project, a.quiet, a.announce = h, a.quiet, False
    return cmd_load(a)


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
        if parts[0] == "skills" and len(parts) >= 3 and parts[1] in ("rbx-load", "rbx-unload"):
            continue            # retired commands: the installer removes their old global files
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
          "Claude sessions no longer load the vault unless they are started in the vault folder; your own skills, agents and CLAUDE.md were not touched. Undo: vault-mode.py migrate --revert."
          % (ns, na, c, backup))
    for m in moved:
        if m["edited"]:
            print("  you had edited %s: your version is in the backup" % m["rel"])
    for d in left:
        print("  left in place (contains files that are not from the kit): %s" % d)
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
    for name in ("home", "load", "unload", "status", "sync", "migrate", "mode-text", "cold"):
        s = sp.add_parser(name)
        s.add_argument("--config", default=argparse.SUPPRESS)
        if name in ("load", "unload", "status"):
            s.add_argument("--project")
        if name == "load":
            s.add_argument("--quiet", action="store_true")
            s.add_argument("--announce", action="store_true")
        if name == "home":
            s.add_argument("--kit")
        if name == "unload":
            s.add_argument("--all", action="store_true")
        if name == "sync":
            s.add_argument("--quiet", action="store_true")
        if name == "migrate":
            s.add_argument("--dry-run", action="store_true")
            s.add_argument("--revert", action="store_true")
            s.add_argument("--force", action="store_true")
            s.add_argument("--old-manifest")
        if name == "cold":
            s.add_argument("target", nargs="?")
            s.add_argument("--path", action="store_true")
    a = ap.parse_args(argv)
    fn = {"home": cmd_home, "load": cmd_load, "unload": cmd_unload, "status": cmd_status, "sync": cmd_sync, "migrate": cmd_migrate, "mode-text": cmd_mode_text, "cold": cmd_cold}[a.cmd]
    store = P(cfg_dir(a))["store"]
    try:
        if a.cmd in ("load", "unload", "sync", "migrate") and os.path.isdir(store):
            with Lock(os.path.join(store, ".mode.lock")):
                return fn(a) or 0
        return fn(a) or 0
    except Exception as e:      # never break a hook or the refresh
        if a.cmd == "sync":
            return 0
        print("vault-mode: failed: %r" % (e,), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
