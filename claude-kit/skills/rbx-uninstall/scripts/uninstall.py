#!/usr/bin/env python3
"""uninstall.py - remove the whole Roblox Dev Mastery Vault kit and keep only the user's games. Python 3 stdlib only.

  uninstall.py [--vault DIR] [--keep-dir DIR] [--keep-edited] [--config DIR] [--home DIR] [--yes]

Default is a DRY RUN: prints the plan and changes nothing. --yes runs it for real (only after the user confirmed in chat).
Real run order: 1 copy Games/ (+ My Research) to the keep folder and verify byte for byte -> 2 remove hooks (settings.json backed up)
and the auto-sync job -> 3 delete manifest-listed kit files -> 4 delete <config>/claude-kit -> 5 delete the vault folder (only if step 1
verified) -> 6 delete this skill. Nothing is deleted if step 1 fails.
Config dir: --config, else --home/.claude, else $CLAUDE_CONFIG_DIR, else ~/.claude.  --home DIR is for tests: it also turns off every
machine-wide lookup (env CLAUDES_VAULT, scheduled tasks, LOCALAPPDATA state), so a test can never touch the real install.
Never touched: credentials, other skills/agents/settings, MCP servers, Rokit/Luau tools, $ROBLOX_PROJECTS projects, CLAUDE.md (lines are only listed).
ONE FOLDER: the kit lives in <vault>/.rbx, so it goes with the vault folder; outside it only the 3 stub skills and the pointer file rbx-dev-vault.path are removed.
RESCUE: without --keep-dir, Games/, Models/, My-Skills/, My-Agents/ (and My Research) are copied to the PARENT folder of the vault folder (an existing name is never overwritten: "<name> (<vault folder name>)"), verified byte for byte, before anything is deleted.
"""
import argparse, datetime, hashlib, json, os, re, shutil, stat, subprocess, sys, tempfile, time

STUB_NAMES = ("rbx-update", "rbx-check", "rbx-uninstall")
POINTER = "rbx-dev-vault.path"
KIT_RE = re.compile(r"claude-kit|claudes?[- ]vault|Roblox Dev Mastery", re.I)
SELF_PREFIX = "skills/rbx-uninstall/"
OUT = []


def say(s=""):
    print(s)


def norm(p):
    """~ expansion, Git Bash /c/... -> C:\\..., absolute."""
    if not p:
        return p
    p = os.path.expanduser(os.path.expandvars(p))
    if os.name == "nt":
        m = re.match(r"^/([a-zA-Z])(/.*)?$", p)
        if m:
            p = m.group(1).upper() + ":" + (m.group(2) or "/")
    return os.path.abspath(p)


def real(p):
    return os.path.normcase(os.path.realpath(os.path.abspath(p)))


def inside(child, parent):
    c, p = real(child), real(parent)
    return c == p or c.startswith(p.rstrip(os.sep) + os.sep)


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def hsize(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024 or u == "GB":
            return ("%d %s" % (n, u)) if u == "B" else ("%.1f %s" % (n, u))
        n /= 1024.0


def walk_files(root):
    """yield (relpath with /, abspath) of files and symlinks (not followed); skips nothing."""
    for d, dirs, files in os.walk(root, followlinks=False):
        for n in files:
            a = os.path.join(d, n)
            yield os.path.relpath(a, root).replace(os.sep, "/"), a
        for n in list(dirs):
            a = os.path.join(d, n)
            if os.path.islink(a):
                dirs.remove(n)
                yield os.path.relpath(a, root).replace(os.sep, "/"), a


def count(root):
    n = s = 0
    for _, a in walk_files(root):
        n += 1
        try:
            s += os.lstat(a).st_size
        except OSError:
            pass
    return n, s


def tree_sig(root, hashes=True):
    sig = {}
    for r, a in walk_files(root):
        if os.path.islink(a):
            sig[r] = ("link", os.readlink(a))
        else:
            sig[r] = (os.path.getsize(a), sha(a) if hashes else "")
    return sig


def rm_err(func, path, exc):
    try:
        os.chmod(path, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
        func(path)
    except OSError:
        pass


def rmtree(p):
    if os.path.islink(p) or os.path.isfile(p):
        try:
            os.remove(p)
        except OSError:
            rm_err(os.remove, p, None)
        return
    if sys.version_info >= (3, 12):
        shutil.rmtree(p, onexc=lambda f, pa, e: rm_err(f, pa, e))
    else:
        shutil.rmtree(p, onerror=rm_err)


def rmfile(p):
    try:
        os.remove(p)
        return True
    except FileNotFoundError:
        return True
    except OSError:
        rm_err(os.remove, p, None)
        return not os.path.lexists(p)


def is_vault(d):
    return os.path.isdir(os.path.join(d, "Roblox")) and os.path.isdir(os.path.join(d, "Mentor"))


def _norm_text_sha(f, mode):
    """sha256 of the file with line endings normalised ('lf' or 'crlf'); None for binary files"""
    with open(f, "rb") as fh:
        b = fh.read()
    if b"\0" in b[:8192]:
        return None
    b = b.replace(b"\r\n", b"\n")
    if mode == "crlf":
        b = b.replace(b"\n", b"\r\n")
    return hashlib.sha256(b).hexdigest()


def same_content(f, want):
    """True when the installed file is what the manifest recorded. Line endings do not count as an edit (a Windows git/autocrlf checkout turns LF into CRLF and back)."""
    if not want or sha(f) == want:
        return True
    return want in (_norm_text_sha(f, "lf"), _norm_text_sha(f, "crlf"))


# kit files that the kit itself downloads after the install (the reference clone) or that have their own copy step (backup/): never counted as "edited by you", never backed up twice (state/ is NOT here: your ledger, local rules and queued notes live there and are backed up)
GENERATED = ("claude-kit/roblox-reference/", "claude-kit/reference-path.txt", "claude-kit/backup/")
KIT_MARK_BEGIN = "<!-- >>> roblox-vault-mode rules"
KIT_MARK_END = "<!-- <<< roblox-vault-mode rules <<< -->"


def kit_block_span(txt):
    """(start, end) of the kit's managed block (begin marker line .. end marker line incl. its newline), or None unless BOTH exact markers are present"""
    i = txt.find(KIT_MARK_BEGIN)
    if i < 0:
        return None
    ls = txt.rfind("\n", 0, i) + 1
    if txt[ls:i].strip():
        return None
    j = txt.find(KIT_MARK_END, i)
    if j < 0:
        return None
    k = j + len(KIT_MARK_END)
    if txt[k:k + 2] == "\r\n":
        k += 2
    elif txt[k:k + 1] == "\n":
        k += 1
    return ls, k


def strip_kit_block(path, bdir):
    """remove ONLY the kit's marker block from a CLAUDE.md; the file is copied to bdir first. Returns a status string."""
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8", "surrogateescape")
    span = kit_block_span(txt)
    if not span:
        return "no kit marker block found"
    os.makedirs(bdir, exist_ok=True)
    bak = os.path.join(bdir, "CLAUDE.md.before-uninstall")
    n = 1
    while os.path.exists(bak):
        n += 1
        bak = os.path.join(bdir, "CLAUDE.md.before-uninstall-%d" % n)
    with open(bak, "wb") as f:
        f.write(raw)
    new = txt[:span[0]] + txt[span[1]:]
    with open(path, "wb") as f:
        f.write(new.encode("utf-8", "surrogateescape"))
    return "kit block removed (%d lines), original saved to %s" % (txt[span[0]:span[1]].count("\n"), bak)


def unlink_any(p):
    try:
        os.remove(p)
        return True
    except FileNotFoundError:
        return True
    except OSError:
        pass
    try:
        os.chmod(p, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
        os.remove(p)
        return True
    except OSError:
        pass
    try:
        os.rmdir(p)          # directory symlink / junction
        return True
    except OSError:
        return not os.path.lexists(p)


def clear_tree(root, tries=3):
    """delete everything INSIDE root (files, links, subfolders), retrying locked entries; root itself stays. Returns the number of entries that could not be removed."""
    bad = 0
    for d, dirs, files in os.walk(root, topdown=False, followlinks=False):
        for n in files + [x for x in dirs if os.path.islink(os.path.join(d, x))]:
            p = os.path.join(d, n)
            ok = False
            for i in range(tries):
                if unlink_any(p):
                    ok = True
                    break
                time.sleep(0.25 * (i + 1))
            bad += 0 if ok else 1
        for n in dirs:
            p = os.path.join(d, n)
            if os.path.islink(p):
                continue
            ok = False
            for i in range(tries):
                try:
                    os.rmdir(p)
                    ok = True
                    break
                except FileNotFoundError:
                    ok = True
                    break
                except OSError:
                    time.sleep(0.25 * (i + 1))
            bad += 0 if ok else 1
    return bad


# Detached cleanup helper: written to a temp folder (never inside the vault) and started only after the rescue copy was verified.
# It re-checks everything itself, waits until the vault folder can be removed (the Claude session that started the uninstall has its working folder in it),
# deletes ONLY that exact folder, logs to the backups folder and removes itself.
HELPER_SRC = r'''
import json, os, shutil, stat, sys, time, datetime
SENT, TARGET = sys.argv[1], sys.argv[2]
SELF = os.path.abspath(sys.argv[0])
try:
    os.chdir(os.path.dirname(os.path.dirname(SELF)))
except OSError:
    pass
def nz(p):
    return os.path.normcase(os.path.realpath(os.path.abspath(p)))
LOG = None
def log(m):
    if not LOG:
        return
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write("%s %s\n" % (datetime.datetime.now().isoformat(timespec="seconds"), m))
    except OSError:
        pass
def inside(c, p):
    c, p = nz(c), nz(p)
    return c == p or c.startswith(p.rstrip(os.sep) + os.sep)
def clear(t):
    for d, dirs, files in os.walk(t, topdown=False, followlinks=False):
        for n in files + [x for x in dirs if os.path.islink(os.path.join(d, x))]:
            p = os.path.join(d, n)
            try:
                os.remove(p)
            except OSError:
                try:
                    os.chmod(p, stat.S_IWRITE | stat.S_IREAD)
                    os.remove(p)
                except OSError:
                    try:
                        os.rmdir(p)
                    except OSError:
                        pass
        for n in dirs:
            p = os.path.join(d, n)
            if not os.path.islink(p):
                try:
                    os.rmdir(p)
                except OSError:
                    pass
def finish():
    try:
        os.remove(SENT)
    except OSError:
        pass
    try:
        os.remove(SELF)
    except OSError:
        pass
    try:
        os.rmdir(os.path.dirname(SELF))
    except OSError:
        pass
def main():
    global LOG
    try:
        d = json.load(open(SENT, encoding="utf-8"))
        LOG = d.get("log")
        t = d["target"]
        ok = (d.get("kind") == "rbx-uninstall-cleanup" and d.get("rescue_verified") is True and os.path.isabs(t) and nz(t) == nz(TARGET) and os.path.basename(t.rstrip("\\/")) == d["name"]
              and time.time() < d["expires"] and os.path.isabs(d["keep"]) and os.path.isabs(d["home"]))
        if ok:
            r = nz(t)
            parts = [x for x in r.replace("\\", "/").split("/") if x and not (len(x) == 2 and x[1] == ":")]
            ok = len(parts) >= 2 and r != nz(d["home"]) and not inside(d["home"], t) and not inside(d["keep"], t) and not inside(t, d["keep"]) and nz(os.path.dirname(t)) == nz(d["parent"])
        if not ok:
            log("REFUSED: sentinel does not match the target %s; nothing deleted" % TARGET)
            finish()
            return 3
    except Exception as e:
        log("REFUSED: bad sentinel (%s)" % e)
        finish()
        return 3
    allowed = set(d.get("left", []))
    start = time.time()
    log("waiting to delete %s" % t)
    wait = 2.0
    while time.time() < d["expires"]:
        if not os.path.lexists(t):
            log("done: folder already gone")
            finish()
            return 0
        try:
            now = set(os.listdir(t))
        except OSError:
            now = set()
        if now - allowed:
            log("ABORTED: new entries appeared in the folder (%s); nothing more deleted" % ", ".join(sorted(now - allowed))[:200])
            finish()
            return 4
        clear(t)
        try:
            os.rmdir(t)
            log("done: deleted %s after %d s" % (t, time.time() - start))
            finish()
            return 0
        except OSError:
            pass
        time.sleep(wait)
        wait = min(60.0, wait * 1.5 if time.time() - start > 120 else wait)
    log("gave up waiting; delete the folder by hand: %s" % t)
    finish()
    return 5
sys.exit(main())
'''


def start_cleanup(vault, keep_final, home, rescue_ok, hours=12):
    """start the detached helper that removes the (nearly) empty vault folder once nothing holds it. Returns the log path, or None when it must not run."""
    if not rescue_ok or not os.path.isdir(vault):
        return None

    try:
        left = os.listdir(vault)
        tdir = tempfile.mkdtemp(prefix="rbx-uninstall-cleanup-")
        script, sent = os.path.join(tdir, "cleanup.py"), os.path.join(tdir, "target.json")
        log = os.path.join(keep_final, "_uninstall-cleanup.log")
        with open(script, "w", encoding="utf-8") as f:
            f.write(HELPER_SRC)
        with open(sent, "w", encoding="utf-8") as f:
            json.dump({"kind": "rbx-uninstall-cleanup", "rescue_verified": True, "target": vault, "name": os.path.basename(vault), "parent": os.path.dirname(vault), "home": home,
                       "keep": keep_final, "left": left, "log": log, "expires": time.time() + hours * 3600}, f)
        exe = sys.executable
        if os.name == "nt":
            w = os.path.join(os.path.dirname(exe), "pythonw.exe")
            exe = w if os.path.isfile(w) else exe
        cmd = [exe, "-I", script, sent, vault]
        kw = dict(stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True, cwd=tdir)
        if os.name == "nt":
            base = 0x00000008 | 0x00000200       # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
            try:
                subprocess.Popen(cmd, creationflags=base | 0x01000000, **kw)       # | CREATE_BREAKAWAY_FROM_JOB (the Claude shell may run us in a job that is killed on exit)
            except OSError:
                subprocess.Popen(cmd, creationflags=base, **kw)
        else:
            subprocess.Popen(cmd, start_new_session=True, **kw)
        return log
    except Exception as e:
        say("      could not start the cleanup helper (%s)" % e)
        return None


# ---------------------------------------------------------------- locate
def config_of(a, home):
    if a.config:
        return norm(a.config)
    if a.home:
        return os.path.join(home, ".claude")
    return norm(os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(home, ".claude"))


def kit_base(vault, config, rel):
    """claude-kit/... lives in <vault>/.rbx (one folder) when that exists, else in the config folder (old layout); skills/ agents/ stay in the config folder"""
    if rel.startswith("claude-kit/") and os.path.isdir(os.path.join(vault, ".rbx", "claude-kit")):
        return os.path.join(vault, ".rbx")
    return config


def find_vault(a, home, ambient):
    if a.vault:
        return norm(a.vault), []
    cands = []
    if ambient:
        for k in ("RBX_DEV_VAULT", "CLAUDES_VAULT"):
            e = os.environ.get(k)
            if e:
                cands.append(norm(e))
    try:
        pv = open(os.path.join(config_of(a, home), POINTER), encoding="utf-8").read().splitlines()[0].strip()
        if pv:
            cands.append(norm(pv))
    except (OSError, IndexError):
        pass
    cands.append(os.path.join(home, "Obsidian", "rbx-dev-vault"))
    cands.append(os.path.join(home, "Obsidian", "claudes-vault"))
    if ambient:
        p = os.path.dirname(os.path.abspath(__file__))
        while True:
            q = os.path.dirname(p)
            if q == p:
                break
            p = q
            if is_vault(p):
                cands.append(p)
                break
    known = []
    for c in cands:
        if os.path.isdir(c) and is_vault(c) and real(c) not in [real(k) for k in known]:
            known.append(c)
    if known:
        return known[0], known[1:]
    found = []
    for base in ("Downloads", "Documents", "Desktop", "Obsidian", ""):
        b = os.path.join(home, base) if base else home
        try:
            kids = [os.path.join(b, n) for n in sorted(os.listdir(b))]
        except OSError:
            continue
        for k in kids:
            for c in [k] + ([os.path.join(k, n) for n in sorted(os.listdir(k))] if os.path.isdir(k) and base in ("Downloads", "Documents", "Desktop") else []):
                try:
                    if os.path.isdir(c) and is_vault(c) and os.path.isdir(os.path.join(c, "claude-kit")) and real(c) not in [real(f) for f in found]:
                        found.append(c)
                except OSError:
                    pass
    if len(found) == 1:
        return found[0], []
    return None, found


def refuse_vault(v, home, config, keep_final):
    if not v or not os.path.isdir(v):
        return "vault folder not found: %s" % v
    r = real(v)
    if r == real(home):
        return "refusing: the vault path is your home folder (%s)" % v
    if os.path.dirname(r) == r or re.match(r"^[a-z]:[\\/]?$", r, re.I):
        return "refusing: the vault path is a drive/filesystem root (%s)" % v
    if len([x for x in re.split(r"[\\/]+", r) if x and not re.match(r"^[a-z]:$", x, re.I)]) < 2:
        return "refusing: the vault path is too shallow (%s)" % v
    if not is_vault(v):
        return "refusing: %s has no Roblox/ and Mentor/ folders, so it does not look like the vault" % v
    for name, p in (("home folder", home), ("config folder", config)):
        if inside(p, v):
            return "refusing: the %s (%s) is inside the vault path" % (name, p)
    if inside(v, config):
        return "refusing: the vault is inside the config folder"
    if keep_final and (inside(keep_final, v) or inside(v, keep_final)):
        return "refusing: the keep folder (%s) and the vault overlap; choose --keep-dir elsewhere" % keep_final
    return None


# ---------------------------------------------------------------- plan pieces
def read_manifest(config, vault):
    man = os.path.join(kit_base(vault, config, "claude-kit/"), "claude-kit", "installed.tsv")
    if not os.path.isfile(man):
        man = os.path.join(config, "claude-kit", "installed.tsv")      # an old install that was not migrated yet
    ent = {}
    src = "manifest"
    if os.path.isfile(man):
        for ln in open(man, encoding="utf-8", errors="replace").read().splitlines():
            p = ln.split("\t")
            k = p[0].strip().replace("\\", "/") if len(p) >= 2 else ""
            if k and not k.startswith("/") and ":" not in k and ".." not in k.split("/"):
                ent[k] = p[1].strip()
    else:
        # no manifest: derive the expected files from the kit source in the vault (files that differ count as edited)
        src = "kit source in vault (installed.tsv missing)"
        kit = os.path.join(vault, "claude-kit")
        ao = ["rbx-update", "rbx-check", "rbx-uninstall"]
        try:
            ao = [x.strip() for x in open(os.path.join(kit, "mode", "always-on.txt"), encoding="utf-8") if x.strip() and not x.startswith("#")] or ao
        except OSError:
            pass
        sm = "claude-kit/vault-mode"
        for sub in ("agents", "skills", "mode", "tools", "systems", "skillpack"):
            for r, a in walk_files(os.path.join(kit, sub)):
                if "__pycache__" in r or r.endswith(".pyc"):
                    continue
                if sub in ("tools", "systems", "skillpack"):
                    rel = "claude-kit/%s/%s" % (sub, r)
                elif sub == "mode":
                    rel = "%s/%s" % (sm, r)
                elif sub == "agents":
                    rel = "%s/.claude/agents/%s" % (sm, r)
                else:
                    rel = ("skills/%s" % r) if (r.split("/")[0] in ao and not os.path.isdir(os.path.join(vault, ".rbx", "claude-kit"))) else ("%s/.claude/skills/%s" % (sm, r))
                ent[rel] = sha(a)
    return ent, src


def dest_of(name, keep_final, vault, a):
    """where a rescued folder goes: --keep-dir/<name>, else the PARENT of the vault folder; an existing name is never overwritten ("<name> (<vault folder name>)")"""
    if a.keep_dir:
        return os.path.join(keep_final, name)
    parent = os.path.dirname(vault)
    cand = os.path.join(parent, name)
    if not os.path.lexists(cand):
        return cand
    vb = os.path.basename(vault)
    cand, i = os.path.join(parent, "%s (%s)" % (name, vb)), 1
    while os.path.lexists(cand):
        i += 1
        cand = os.path.join(parent, "%s (%s %d)" % (name, vb, i))
    return cand


def area_of(rel):
    if rel.startswith("agents/"):
        return "agents"
    if rel.startswith("skills/"):
        return "skills"
    if rel.startswith("claude-kit/vault-mode/cold/"):
        return "cold area (on-demand bulk read by pointers)"
    if rel.startswith("claude-kit/vault-mode/"):
        return "on-demand store (vault skills/agents)"
    if rel.startswith("claude-kit/tools/"):
        return "tools"
    if rel.startswith("claude-kit/systems/"):
        return "systems"
    if rel.startswith("claude-kit/skillpack/"):
        return "skillpack"
    return "other"


def parse_project(gamedir):
    gm = os.path.join(gamedir, "GAME.md")
    try:
        txt = open(gm, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
    except OSError:
        return None
    m = re.search(r"^project:\s*(.+?)\s*$", txt, re.M)
    if not m:
        return None
    v = m.group(1).strip().strip("\"'`")
    if not v or v.lower() in ("none", "pending", "n/a", "tbd", "-", "null", "~"):
        return None
    p = os.path.expanduser(os.path.expandvars(v))
    if not os.path.isabs(p) and not re.match(r"^[A-Za-z]:|^/", p):
        p = os.path.join(gamedir, p)
    return norm(p)


def plan(a, home, config, vault, keep_final):
    P = {"vault": vault, "config": config, "home": home}
    # games
    games, external, research = [], [], []
    gdir = os.path.join(vault, "Games")
    if os.path.isdir(gdir):
        for n in sorted(os.listdir(gdir)):
            d = os.path.join(gdir, n)
            if os.path.isdir(d) and not os.path.islink(d):
                c, s = count(d)
                games.append({"slug": n, "kind": "reusable" if n == "_Reusable" else "game", "files": c, "bytes": s,
                              "project_dir": os.path.isdir(os.path.join(d, "project"))})
                pp = parse_project(d) if n != "_Reusable" else None
                if pp and os.path.isdir(pp) and not inside(pp, vault):
                    external.append((n, pp))
                elif pp and not os.path.isdir(pp) and not inside(pp, vault):
                    external.append((n, pp + "  (folder not found)"))
        gc, gs = count(gdir)
    else:
        gc = gs = 0
    P["games"], P["external"], P["games_files"], P["games_bytes"] = games, external, gc, gs
    memo = {}
    P["dest"] = lambda name: memo.setdefault(name, dest_of(name, keep_final, vault, a))
    # research kept too
    for n in sorted(os.listdir(vault)):
        d = os.path.join(vault, n)
        if os.path.isdir(d) and not os.path.islink(d) and n != "Games":
            if n == "My Research" or os.path.isfile(os.path.join(d, "PROTECTED-RESEARCH.md")):
                research.append(n)
    for n in ("Models", "My-Skills", "My-Agents"):     # your saved models and your own skills/agents (rbx-new-skill) are yours too: copied and verified like Games/
        d = os.path.join(vault, n)
        if os.path.isdir(d) and not os.path.islink(d) and n not in research:
            research.append(n)
    P["research"] = research
    P["own"] = own_files(vault, research)
    # kit
    ent, src = read_manifest(config, vault)
    P["manifest_src"] = src
    present, edited, missing, areas = [], [], [], {}
    for rel, want in sorted(ent.items()):
        f = os.path.join(kit_base(vault, config, rel), rel.replace("/", os.sep))
        if not os.path.isfile(f):
            missing.append(rel)
            continue
        present.append(rel)
        areas[area_of(rel)] = areas.get(area_of(rel), 0) + 1
        if want and not same_content(f, want):
            edited.append(rel)
    P["ent"], P["present"], P["missing"], P["edited"], P["areas"] = ent, present, missing, edited, areas
    # leftovers
    new_files = [r + ".new" for r in present if os.path.isfile(os.path.join(kit_base(vault, config, r), (r + ".new").replace("/", os.sep)))]
    P["new_files"] = new_files
    kitroot = os.path.join(kit_base(vault, config, "claude-kit/"), "claude-kit")
    extras, generated = [], []
    if os.path.isdir(kitroot):
        for r, f in walk_files(kitroot):
            rel = "claude-kit/" + r
            if rel not in ent and ("__pycache__" not in r and not r.endswith(".pyc")) and any(rel == g or rel.startswith(g) for g in GENERATED):
                generated.append(rel)      # downloaded by the kit itself (reference clone; backup/ has its own copy step): not your edit
                continue
            if rel in ent or r in ("installed.tsv", "installed.tsv.pre-mode", "ui-mockup-notice.done", "state/ui-mockup-notice.done", "state/mods-choice", "state/mods-block.txt") or "__pycache__" in r or r.endswith(".pyc"):
                continue
            if r in ("vault-mode/loaded.json", "vault-mode/layout.json", "vault-mode/migration-last.json"):
                continue            # the mode's own bookkeeping, not user data
            extras.append(rel)
    P["extras"], P["generated"] = extras, generated
    try:
        P["mode_projects"] = sorted(json.load(open(os.path.join(kitroot, "vault-mode", "loaded.json"), encoding="utf-8")).get("projects", {}).keys())
    except (OSError, ValueError):
        P["mode_projects"] = []
    st = []
    for n in ("rbx-low-usage.on", "low-usage-mode.on", "mentor-hook.off", "mods-choice", "mods-block.txt"):  # legacy marker name included
        if os.path.isfile(os.path.join(config, "state", n)):
            st.append("state/" + n)
    P["state_files"] = st
    # unlisted files inside kit skill/agent dirs (left alone)
    owned = sorted({"/".join(r.split("/")[:2]) for r in ent if r.startswith("skills/")})
    left = []
    for od in owned:
        d = os.path.join(config, od.replace("/", os.sep))
        if os.path.isdir(d):
            for r, f in walk_files(d):
                rel = od + "/" + r
                if rel in ent or rel in new_files or "__pycache__" in rel or rel.endswith(".pyc"):
                    continue
                left.append(rel)
    P["left_in_skills"] = left
    # hooks
    sj = os.path.join(config, "settings.json")
    hooks = False
    P["settings"] = os.path.isfile(sj)
    if P["settings"]:
        try:
            t = open(sj, encoding="utf-8", errors="replace").read()
            hooks = bool(re.search(r"mentor-hook|lum\.py|low-usage-mode(-rbxdev-vault)?/scripts", t))  # legacy path included
            json.loads(t)
            P["settings_valid"] = True
        except ValueError:
            P["settings_valid"] = False
    P["hooks"] = hooks
    # CLAUDE.md
    lines, blocks = [], []
    for cm in (os.path.join(config, "CLAUDE.md"), os.path.join(vault, "CLAUDE.md"), os.path.join(vault, ".claude", "CLAUDE.md")):
        if os.path.isfile(cm):
            txt = open(cm, encoding="utf-8", errors="replace").read()
            b = kit_block_span(txt)
            if b and not inside(cm, vault):
                blocks.append(cm)          # the kit's own marker block in a file that outlives the vault: removed (exact markers only), file backed up first
            if inside(cm, vault):
                continue                   # inside the vault: deleted with it (your own edits there are copied to _vault-own-files)
            pos = 0
            for i, ln in enumerate(txt.splitlines(True), 1):
                inb = b and b[0] <= pos < b[1]
                pos += len(ln)
                if not inb and KIT_RE.search(ln):
                    lines.append((cm, i, ln.strip()[:160]))
    P["claude_md"], P["claude_blocks"] = lines, blocks
    # vault totals
    vc, vs = count(vault)
    P["vault_files"], P["vault_bytes"] = vc, vs
    # outside-the-vault things (machine wide, only when not a --home test)
    P["sys"] = sys_items(a, home, vault)
    return P


def own_files(vault, skip):
    """files you added or changed in the vault outside Games/, Assets/ and the kept folders (research, Models/, My-Skills/, My-Agents/) (git: untracked + modified)"""
    try:
        r = subprocess.run(["git", "-C", vault, "-c", "core.quotepath=false", "ls-files", "-z", "-o", "-m", "--exclude-standard"], capture_output=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return []
    if r.returncode != 0:
        return []
    out = set()
    for b in r.stdout.split(b"\0"):
        rel = b.decode("utf-8", "replace")
        if rel and not rel.startswith(("Games/", "Assets/", ".git/", ".obsidian/")) and not any(rel == s or rel.startswith(s + "/") for s in skip):
            out.add(rel)
    return sorted(out)


def sys_items(a, home, vault):
    items = []
    if a.home:
        return items
    if os.name == "nt":
        try:
            r = subprocess.run(["schtasks", "/Query", "/TN", "ClaudesVaultPull"], capture_output=True, text=True, timeout=30)
            if r.returncode == 0:
                items.append(("task", "ClaudesVaultPull"))
        except Exception:
            pass
        la = os.environ.get("LOCALAPPDATA")
        if la and os.path.isdir(os.path.join(la, "claudes-vault-sync")):
            items.append(("dir", os.path.join(la, "claudes-vault-sync")))
    elif sys.platform == "darwin":
        pl = os.path.join(home, "Library", "LaunchAgents", "com.roman.vaultpull.plist")
        if os.path.isfile(pl):
            items.append(("launchd", pl))
        sd = os.path.join(home, "Library", "Application Support", "claudes-vault-sync")
        if os.path.isdir(sd):
            items.append(("dir", sd))
    else:
        ud = os.path.join(home, ".config", "systemd", "user")
        for n in ("claudes-vault-pull.timer", "claudes-vault-pull.service"):
            if os.path.isfile(os.path.join(ud, n)):
                items.append(("systemd", os.path.join(ud, n)))
        sd = os.path.join(os.environ.get("XDG_STATE_HOME") or os.path.join(home, ".local", "state"), "claudes-vault-sync")
        if os.path.isdir(sd):
            items.append(("dir", sd))
    return items


def full_plan(P, keep_final, keep_note, a, real_run):
    L = []
    say = L.append
    say("=" * 70)
    say("UNINSTALL PLAN (%s)" % ("REAL RUN" if real_run else "DRY RUN - nothing is changed"))
    say("=" * 70)
    say("config folder : %s" % P["config"])
    say("vault folder  : %s  (%d files, %s)" % (P["vault"], P["vault_files"], hsize(P["vault_bytes"])))
    say("kit file list : %s" % P["manifest_src"])
    say("")
    say("KEEP - your games. They are copied to: %s" % (keep_final if a.keep_dir else os.path.dirname(P["vault"])))
    if keep_note:
        say("  (%s)" % keep_note)
    if not P["games"]:
        say("  (no game folders found in %s)" % os.path.join(P["vault"], "Games"))
    for g in P["games"]:
        say("  %-28s %-9s %5d files %9s%s" % (g["slug"], g["kind"], g["files"], hsize(g["bytes"]), "  +project/" if g["project_dir"] else ""))
    say("  whole Games/ folder: %d files, %s -> %s" % (P["games_files"], hsize(P["games_bytes"]), P["dest"]("Games")))
    for r in P["research"]:
        say("  also kept (your own folders and notes): %s -> %s" % (r, P["dest"](r)))
    for slug, pp in P["external"]:
        say("  project of %s lives outside the vault, stays IN PLACE (not copied, not touched): %s" % (slug, pp))
    if P["own"]:
        say("  files you added or changed elsewhere in the vault (%d, e.g. %s) -> %s" % (len(P["own"]), ", ".join(P["own"][:3]), os.path.join(keep_final, "_vault-own-files")))
    say("  The copy is verified by file count, size and sha256 before anything is deleted.")
    say("")
    say("REMOVE")
    say("  kit files by area : %s" % (", ".join("%s %d" % (k, v) for k, v in sorted(P["areas"].items())) or "none"))
    say("  total kit files   : %d present (%d listed but already missing)" % (len(P["present"]), len(P["missing"])))
    say("  leftovers         : %d .new files, %d state files, %d unlisted files under <config>/claude-kit" % (len(P["new_files"]), len(P["state_files"]), len(P["extras"])))
    say("  the kit folder claude-kit (tools, systems, skillpack, the on-demand store of vault skills/agents, installed.tsv): %s" % os.path.join(kit_base(P["vault"], P["config"], "claude-kit/"), "claude-kit"))
    say("  the 3 stub skills %s in %s and the pointer file %s" % (", ".join("/" + n for n in STUB_NAMES), os.path.join(P["config"], "skills"), POINTER))
    say("  vault copies in loaded folders (the vault folder's .claude and any older loaded project): %d%s (removed first)" % (len(P["mode_projects"]), (" -> " + ", ".join(P["mode_projects"][:5])) if P["mode_projects"] else ""))
    say("  hooks in settings.json (rbx-low-usage + rbx-mentor): %s" % ("found" if P["hooks"] else "none found") + ("" if P.get("settings_valid", True) else "  WARNING: settings.json is not valid JSON, hooks will NOT be removed"))
    say("  kit mods (plugins): %s" % ("skipped in --home test" if a.home else "claude plugin uninstall rbx-subagent-hud@%s; claude plugin uninstall rbx-graph@%s; claude plugin marketplace remove %s (before the vault is deleted)" % (MARKET, MARKET, MARKET)))
    for k, v in P["sys"]:
        say("  auto-sync %-8s: %s" % (k, v))
    say("  the vault folder: %s (%d files, %s) - only after the games copy is verified" % (P["vault"], P["vault_files"], hsize(P["vault_bytes"])))
    say("  this skill (/rbx-uninstall), last")
    say("")
    say("CHANGED-BY-USER kit files (sha differs from the manifest): %d" % (len(P["edited"]) + len(P["extras"])))
    dst = os.path.join(keep_final, "_edited-kit-files")
    for r in P["edited"] + P["extras"]:
        say("  " + r)
    if P["edited"] or P["extras"]:
        if a.keep_edited:
            say("  --keep-edited: these stay in place, nothing is backed up or deleted for them")
        else:
            say("  they are backed up to %s before deletion (use --keep-edited to leave them in place instead)" % dst)
    say("")
    say("WILL NOT TOUCH")
    for t in ("credentials (.credentials.json and logins)", "all other skills, agents, settings.json content, MCP servers",
              "Rokit / Luau / Rojo tools and anything else outside config, kit and vault",
              "CLAUDE.md (lines listed below are never edited)",
              "settings.json.*-bak-* files next to settings.json (the hook installers' own copies of YOUR settings; delete them yourself if you do not need them)",
              "the companion AI Library Vault folder (ai-library-vault next to the vault), if you have one",
              "Obsidian itself and environment variables such as CLAUDES_VAULT / ROBLOX_PROJECTS"):
        say("  - " + t)
    for r in P["left_in_skills"]:
        say("  - unlisted file in a kit skill folder (left, folder stays): " + r)
    if P["claude_md"]:
        say("")
        say("CLAUDE.md lines that mention the kit or vault (review by hand):")
        for f, i, ln in P["claude_md"]:
            say("  %s:%d: %s" % (f, i, ln))
    say("")
    L.append("")
    L.append("ALL KIT FILES THAT WILL BE REMOVED (%d):" % len(P["present"]))
    L.extend("  " + r for r in P["present"])
    L.append("")
    L.append("KIT-DOWNLOADED FILES (reference clone, backup/ has its own copy step; deleted, not counted as edits) (%d):" % len(P["generated"]))
    L.extend("  " + r for r in P["generated"])
    L.append("")
    L.append("YOUR OWN FILES ELSEWHERE IN THE VAULT (copied to _vault-own-files) (%d):" % len(P["own"]))
    L.extend("  " + r for r in P["own"])
    return L


def confirm_cmd(a):
    py = "python" if shutil.which("python") else sys.executable
    fl = ""
    for flag, val in (("--vault", a.vault), ("--keep-dir", a.keep_dir), ("--config", a.config), ("--home", a.home)):
        if val:
            fl += ' %s "%s"' % (flag, val)
    if a.keep_edited:
        fl += " --keep-edited"
    return '%s "%s"%s --yes' % (py, os.path.abspath(__file__), fl)


def print_plan(P, keep_final, keep_note, a, real_run):
    """SHORT summary on stdout (< 2 KB, so a model never truncates the key facts); the complete file lists go to a file in the temp folder"""
    full = full_plan(P, keep_final, keep_note, a, real_run)
    pf = os.path.join(tempfile.gettempdir(), "rbx-uninstall-plan-%s.txt" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    try:
        with open(pf, "w", encoding="utf-8") as f:
            f.write("\n".join(full) + "\n")
    except OSError:
        pf = None
    parent = keep_final if a.keep_dir else os.path.dirname(P["vault"])
    say("UNINSTALL %s" % ("- REAL RUN" if real_run else "DRY RUN - nothing was changed"))
    say("vault: %s (%d files, %s)" % (P["vault"], P["vault_files"], hsize(P["vault_bytes"])))
    say("RESCUED to %s, verified byte for byte BEFORE anything is deleted:" % parent)
    say("  Games -> %s (%d games, %d files)" % (P["dest"]("Games"), len(P["games"]), P["games_files"]))
    for r in P["research"]:
        say("  %s -> %s" % (r, P["dest"](r)))
    if P["own"]:
        say("  %d other file(s) you added/changed in the vault -> %s" % (len(P["own"]), os.path.join(keep_final, "_vault-own-files")))
    for slug, pp in P["external"]:
        say("  stays in place (outside the vault): project of %s: %s" % (slug, pp))
    say("REMOVED: %d kit files (%s); the kit folder; the 3 stub skills + pointer; %d vault copies; hooks: %s; auto-sync: %s; then the vault folder" % (
        len(P["present"]), ", ".join("%s %d" % (k.split(" (")[0], v) for k, v in sorted(P["areas"].items())) or "none", len(P["mode_projects"]), "found" if P["hooks"] else "none", ", ".join(k for k, v in P["sys"]) or "none"))
    ne = len(P["edited"]) + len(P["extras"])
    say("EDITED BY YOU: %d kit file(s) changed, %d unlisted file(s)%s; %d downloaded kit file(s) (reference clone) are just deleted" % (
        len(P["edited"]), len(P["extras"]), (" -> %s" % os.path.join(keep_final, "_edited-kit-files")) if ne and not a.keep_edited else (" (left in place, --keep-edited)" if ne else ""), len(P["generated"])))
    say("CLAUDE.md: kit marker block %s; %d other line(s) mention the kit (listed, never edited)" % ("removed from " + ", ".join(P["claude_blocks"]) if P["claude_blocks"] else "not present", len(P["claude_md"])))
    say("settings.json is backed up to %s first" % os.path.join(keep_final, "_uninstall-backups"))
    say("NOT TOUCHED: credentials, other skills/agents/settings, MCP servers, projects outside the vault, the folder with your rescued games and backups")
    if keep_note:
        say("(%s)" % keep_note)
    if not P["games"]:
        say("(no game folders found in %s)" % os.path.join(P["vault"], "Games"))
    if pf:
        say("Full file lists: %s" % pf)
    if not real_run:
        say("Run from OUTSIDE the vault folder. After the user says yes: %s" % confirm_cmd(a))


# ---------------------------------------------------------------- execution
def copy_verified(src, dst):
    shutil.copytree(src, dst, symlinks=True)
    s, d = tree_sig(src), tree_sig(dst)
    if s != d:
        bad = sorted(set(s) ^ set(d)) or sorted(k for k in s if s[k] != d.get(k))
        raise RuntimeError("copy verification failed for %s (%d differences, first: %s)" % (src, len(bad), bad[:3]))
    return len(s), sum(v[0] for v in s.values() if isinstance(v[0], int))


def pick_keep_final(keep_dir):
    if not os.path.exists(keep_dir) or (os.path.isdir(keep_dir) and not os.listdir(keep_dir)):
        return keep_dir, ""
    base = os.path.join(keep_dir, "vault-games-" + datetime.date.today().isoformat())
    cand, i = base, 1
    while os.path.exists(cand):
        i += 1
        cand = "%s-%d" % (base, i)
    return cand, "%s already has files; a dated subfolder is used so nothing is overwritten" % keep_dir


def py_run(script, args, config):
    env = dict(os.environ)
    env["CLAUDE_CONFIG_DIR"] = config
    r = subprocess.run([sys.executable, "-I", script] + args, capture_output=True, text=True, env=env, timeout=120)
    return r.returncode, (r.stdout + r.stderr).strip()


def remove_hooks(P, keep_final):
    config, vault = P["config"], P["vault"]
    sj = os.path.join(config, "settings.json")
    if not os.path.isfile(sj):
        say("hooks: no settings.json, nothing to remove")
        return True
    bdir = os.path.join(keep_final, "_uninstall-backups")
    os.makedirs(bdir, exist_ok=True)
    bak = os.path.join(bdir, "settings.json")
    shutil.copy2(sj, bak)
    say("settings.json backed up to %s" % bak)
    ok = True
    for rel, sub in (("claude-kit/vault-mode/.claude/skills/rbx-low-usage/scripts/lum.py", "skills/rbx-low-usage/scripts/lum.py"), ("skills/rbx-low-usage/scripts/lum.py", "skills/rbx-low-usage/scripts/lum.py"), ("claude-kit/tools/mentor-hook.py", "tools/mentor-hook.py")):
        s = os.path.join(kit_base(vault, config, rel), rel.replace("/", os.sep))
        if not os.path.isfile(s) and rel.startswith("skills/") and os.path.isfile(os.path.join(kit_base(vault, config, "claude-kit/"), "claude-kit", "vault-mode", ".claude", "skills", "rbx-low-usage", "scripts", "lum.py")):
            continue            # already handled through the store copy above
        if not os.path.isfile(s):
            s = os.path.join(vault, "claude-kit", sub.replace("/", os.sep))
        if not os.path.isfile(s):
            say("hooks: %s not found, skipped" % rel)
            continue
        try:
            code, out = py_run(s, ["uninstall-hooks", "--config", config], config)
        except Exception as e:
            code, out = 1, str(e)
        say("hooks: %s" % (out.splitlines()[-1] if out else "exit %d" % code))
        if code != 0:
            ok = False
    try:
        json.loads(open(sj, encoding="utf-8").read())
    except ValueError:
        shutil.copy2(bak, sj)
        say("settings.json became invalid, restored from backup")
        ok = False
    return ok


MODS = ("rbx-subagent-hud", "rbx-graph", "rbx-subagent-hud", "workflow-hud", "vault-graph")   # the last three = legacy names before the renames (uninstalled if still present)
MARKET = "roblox-vault-kit-mods"


def mod_cmds():
    # the mods live at PROJECT scope of the vault folder (run with cwd = the vault folder); older kits installed them at user scope: both are removed
    return ([["claude", "plugin", "uninstall", "%s@%s" % (m, MARKET), "--scope", "project"] for m in MODS] + [["claude", "plugin", "uninstall", "%s@%s" % (m, MARKET), "--scope", "user"] for m in MODS]
            + [["claude", "plugin", "marketplace", "remove", MARKET]])


def claude_cli():
    """the claude CLI as an argv prefix; RBX_UNINSTALL_CLAUDE=<script.py> (tests) runs that script with this python instead"""
    t = os.environ.get("RBX_UNINSTALL_CLAUDE")
    if t:
        return [sys.executable, t]
    exe = shutil.which("claude")
    return [exe] if exe else None


NOT_THERE = re.compile(r"not installed|not found|no such|isn't installed|is not installed|unknown plugin|does not exist|not configured|no plugin", re.I)


def remove_mods(a, config, vault=None):
    """Kit mods (Claude Code plugins). Runs BEFORE the vault is deleted. Skipped under --home tests (like schtasks) unless RBX_UNINSTALL_CLAUDE is set.
    Asks `claude plugin list` first and only touches what is installed; 'not installed' is a quiet success; only real failures are printed."""
    if a.home and not os.environ.get("RBX_UNINSTALL_CLAUDE"):
        say("mods: skipped (--home test)")
        return True
    cli = claude_cli()
    if not cli:
        say("mods: claude CLI not found; if the kit mods are installed run /plugin uninstall rbx-subagent-hud@%s, rbx-graph@%s and /plugin marketplace remove %s" % (MARKET, MARKET, MARKET))
        return True
    env = dict(os.environ, CLAUDE_CONFIG_DIR=config)
    cwd = vault if vault and os.path.isdir(vault) else None

    def call(args):
        r = subprocess.run(cli + args, capture_output=True, text=True, timeout=120, env=env, stdin=subprocess.DEVNULL, cwd=cwd)
        return r.returncode, (r.stdout + r.stderr).strip()

    try:
        lc, listing = call(["plugin", "list"])
    except Exception as e:
        lc, listing = 1, ""
        say("mods: could not list plugins (%s); trying the known names" % e)
    known = lc == 0
    done, bad = [], []
    for m in dict.fromkeys(MODS):
        if known and m not in listing:
            continue                      # not installed anywhere: nothing to do, nothing to print
        for scope in ("project", "user"):
            try:
                rc, out = call(["plugin", "uninstall", "%s@%s" % (m, MARKET), "--scope", scope])
            except Exception as e:
                bad.append("%s (%s scope): %s" % (m, scope, e))
                continue
            if rc == 0:
                done.append("%s (%s)" % (m, scope))
            elif not NOT_THERE.search(out):
                bad.append("%s (%s scope): %s" % (m, scope, (out.splitlines() or ["exit %d" % rc])[-1][:100]))
    try:
        mc, ml = call(["plugin", "marketplace", "list"])
    except Exception:
        mc, ml = 1, ""
    if mc != 0 or MARKET in ml:
        try:
            rc, out = call(["plugin", "marketplace", "remove", MARKET])
            if rc == 0:
                done.append("marketplace " + MARKET)
            elif not NOT_THERE.search(out):
                bad.append("marketplace %s: %s" % (MARKET, (out.splitlines() or ["exit %d" % rc])[-1][:100]))
        except Exception as e:
            bad.append("marketplace %s: %s" % (MARKET, e))
    say("mods: removed %s" % (", ".join(done) if done else "nothing (none installed)"))
    for b in bad:
        say("mods: FAILED %s" % b)
    return not bad


def remove_sync(P):
    for k, v in P["sys"]:
        try:
            if k == "task":
                r = subprocess.run(["schtasks", "/Delete", "/TN", v, "/F"], capture_output=True, text=True, timeout=30)
                say("auto-sync task %s: %s" % (v, "removed" if r.returncode == 0 else "NOT removed (" + (r.stderr or r.stdout).strip()[:100] + ")"))
            elif k == "launchd":
                subprocess.run(["launchctl", "unload", v], capture_output=True, timeout=30)
                rmfile(v)
                say("launchd agent removed: " + v)
            elif k == "systemd":
                if v.endswith(".timer"):
                    subprocess.run(["systemctl", "--user", "disable", "--now", os.path.basename(v)], capture_output=True, timeout=30)
                rmfile(v)
                say("systemd unit removed: " + v)
            elif k == "dir":
                rmtree(v)
                say("sync state folder removed: " + v)
        except Exception as e:
            say("auto-sync %s: could not remove (%s)" % (k, e))
    if sys.platform.startswith("linux") and P["sys"]:
        try:
            subprocess.run(["systemctl", "--user", "daemon-reload"], capture_output=True, timeout=30)
            cur = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=30)
            if cur.returncode == 0 and "# claudes-vault-pull" in cur.stdout:
                keep = "\n".join(l for l in cur.stdout.splitlines() if "# claudes-vault-pull" not in l) + "\n"
                subprocess.run(["crontab", "-"], input=keep, text=True, timeout=30)
                say("cron line removed")
        except Exception:
            pass


def climb(path, stop):
    stops = {real(s) for s in stop}
    d = os.path.dirname(path)
    while real(d) not in stops:
        try:
            if os.listdir(d):
                break
            os.rmdir(d)
        except OSError:
            break
        d = os.path.dirname(d)


def run_real(a, P, keep_final, keep_note):
    config, vault = P["config"], P["vault"]
    summary = {}
    kit_backup_ok = True
    # 1 copy + verify
    say("[1/6] copying your folders to %s" % keep_final)
    os.makedirs(keep_final, exist_ok=True)
    try:
        if os.path.isdir(os.path.join(vault, "Games")):
            n, s = copy_verified(os.path.join(vault, "Games"), P["dest"]("Games"))
            say("      Games: %d files, %s verified (sha256 + size) -> %s" % (n, hsize(s), P["dest"]("Games")))
        for r in P["research"]:
            n, s = copy_verified(os.path.join(vault, r), P["dest"](r))
            say("      %s: %d files, %s verified -> %s" % (r, n, hsize(s), P["dest"](r)))
        for rel in P["own"]:
            src = os.path.join(vault, rel.replace("/", os.sep))
            if not os.path.isfile(src):
                continue
            dst = os.path.join(keep_final, "_vault-own-files", rel.replace("/", os.sep))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            if sha(src) != sha(dst):
                raise RuntimeError("backup of %s does not match" % rel)
        if P["own"]:
            say("      %d of your own files in the vault copied to %s" % (len(P["own"]), os.path.join(keep_final, "_vault-own-files")))
        if not a.keep_edited:
            for rel in P["edited"] + P["extras"]:
                src = os.path.join(kit_base(vault, config, rel), rel.replace("/", os.sep))
                dst = os.path.join(keep_final, "_edited-kit-files", rel.replace("/", os.sep))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                if sha(src) != sha(dst):
                    raise RuntimeError("backup of %s does not match" % rel)
            if P["edited"] or P["extras"]:
                say("      %d edited/unlisted kit files backed up to %s" % (len(P["edited"]) + len(P["extras"]), os.path.join(keep_final, "_edited-kit-files")))
    except Exception as e:
        say("COPY FAILED, nothing was deleted: %s" % e)
        return 1
    # 2 hooks + auto-sync
    say("[2/6] removing hooks and auto-sync")
    vm = os.path.join(kit_base(vault, config, "claude-kit/"), "claude-kit", "tools", "vault-mode.py")
    if os.path.isfile(vm) and P["mode_projects"]:
        try:
            code, out = py_run(vm, ["unload", "--all", "--config", config], config)
            say("      vault copies: %s" % (" | ".join(out.splitlines()[-3:]) if out else "exit %d" % code))
        except Exception as e:
            say("      vault copies: could not remove them (%s); the folders are listed in %s" % (e, os.path.join(kit_base(vault, config, "claude-kit/"), "claude-kit", "vault-mode", "loaded.json")))
    hooks_ok = remove_hooks(P, keep_final)
    claude_md_res = []
    for cm in P["claude_blocks"]:
        try:
            claude_md_res.append((cm, strip_kit_block(cm, os.path.join(keep_final, "_uninstall-backups"))))
        except OSError as e:
            claude_md_res.append((cm, "could not edit (%s)" % e))
    remove_sync(P)
    mods_ok = remove_mods(a, config, vault)
    # 3 manifest files
    say("[3/6] deleting kit files listed in installed.tsv")
    skip = set(P["edited"] + P["extras"]) if a.keep_edited else set()
    removed = failed = 0
    stops = [config, os.path.join(config, "skills"), os.path.join(config, "agents"), os.path.join(config, "claude-kit"), os.path.join(vault, ".rbx"), os.path.join(vault, ".rbx", "claude-kit")]
    for rel in P["present"]:
        if rel.startswith(SELF_PREFIX) or rel in skip:
            continue
        f = os.path.join(kit_base(vault, config, rel), rel.replace("/", os.sep))
        if rmfile(f):
            removed += 1
        else:
            failed += 1
        nf = f + ".new"
        if os.path.lexists(nf):
            rmfile(nf)
    for rel in P["state_files"]:
        rmfile(os.path.join(config, rel.replace("/", os.sep)))
    for d, dirs, files in os.walk(os.path.join(config, "skills"), topdown=False):
        if os.path.basename(d) == "__pycache__":
            rmtree(d)
    for rel in P["present"]:
        if not rel.startswith(SELF_PREFIX):
            climb(os.path.join(kit_base(vault, config, rel), rel.replace("/", os.sep)), stops)
    try:
        os.rmdir(os.path.join(config, "state"))
    except OSError:
        pass
    say("      removed %d files%s" % (removed, (", %d could not be deleted" % failed) if failed else ""))
    # 4 claude-kit
    say("[4/6] deleting %s" % os.path.join(kit_base(vault, config, "claude-kit/"), "claude-kit"))
    kr = os.path.join(kit_base(vault, config, "claude-kit/"), "claude-kit")
    kb = os.path.join(kr, "backup")
    if os.path.isdir(kb) and not a.keep_edited:
        try:
            n, sz = copy_verified(kb, os.path.join(keep_final, "_kit-backups"))
            say("      %d backed-up originals of yours (replaced by installs) copied to %s" % (n, os.path.join(keep_final, "_kit-backups")))
        except Exception as e:
            kit_backup_ok = False
            say("      WARNING: could not copy %s (%s); the vault folder is NOT deleted so your backed-up originals stay" % (kb, e))
            for ch in os.listdir(kr):
                if ch != "backup":
                    (rmtree if os.path.isdir(os.path.join(kr, ch)) else rmfile)(os.path.join(kr, ch))
            kr = os.path.join(kr, "__none__")
    if os.path.isdir(kr):
        if skip:
            for r, f in list(walk_files(kr)):
                if ("claude-kit/" + r) not in skip:
                    rmfile(f)
            for d, dirs, files in os.walk(kr, topdown=False):
                try:
                    os.rmdir(d)
                except OSError:
                    pass
        else:
            rmtree(kr)
    # 5 vault
    say("[5/6] deleting vault folder %s" % vault)
    os.chdir(P["home"])
    if not kit_backup_ok:
        say("      skipped (see the warning above)")
        return 1
    stuck = clear_tree(vault)
    gone = False
    for i in range(3):
        try:
            os.rmdir(vault)
            gone = True
            break
        except FileNotFoundError:
            gone = True
            break
        except OSError:
            time.sleep(0.3 * (i + 1))
    vault_gone = gone and not os.path.exists(vault)
    pending = None
    if vault_gone:
        say("      vault folder deleted")
    else:
        pending = start_cleanup(vault, keep_final, P["home"], True)
        if pending:
            say("      The folder is in use by this session; it will be deleted automatically a few seconds after you close this Claude session (or delete it yourself: %s)" % vault)
            say("      (%d entries were locked; cleanup log: %s)" % (stuck, pending))
        else:
            say("      WARNING: the vault folder %s still exists (in use) and the cleanup helper could not start; close this Claude session and delete it by hand" % vault)
    # 6 self
    say("[6/6] removing the /rbx-uninstall skill, the 2 other stub skills and the pointer file")
    for sn in STUB_NAMES:      # ONE FOLDER: thin stubs (SKILL.md + where.py); anything else a user put there stays
        sd = os.path.join(config, "skills", sn)
        if sn != "rbx-uninstall" or not skip:
            for fn in ("SKILL.md", "where.py"):
                fp = os.path.join(sd, fn)
                if os.path.isfile(fp) and (fn == "where.py" or "rbx-stub" in open(fp, encoding="utf-8", errors="replace").read()):
                    rmfile(fp)
            try:
                os.rmdir(sd)
            except OSError:
                pass
    rmfile(os.path.join(config, POINTER))
    selfdir = os.path.join(config, "skills", "rbx-uninstall")
    if os.path.isdir(selfdir):
        if skip:
            for rel in P["present"]:
                if rel.startswith(SELF_PREFIX) and rel not in skip:
                    rmfile(os.path.join(config, rel.replace("/", os.sep)))
            for d, dirs, files in os.walk(selfdir, topdown=False):
                if os.path.basename(d) == "__pycache__":
                    rmtree(d)
                    continue
                try:
                    os.rmdir(d)
                except OSError:
                    pass
        else:
            rmtree(selfdir)
    say("")
    say("=" * 70)
    say("DONE" if vault_gone and not failed and hooks_ok and mods_ok else ("DONE (the empty vault folder is removed automatically after you close this session)" if pending and not failed and hooks_ok and mods_ok else "DONE WITH WARNINGS (see above)"))
    say("=" * 70)
    say("Your games are now in: %s" % (keep_final if a.keep_dir else os.path.dirname(vault)))
    say("  %s" % P["dest"]("Games"))
    for r in P["research"]:
        say("  %s" % P["dest"](r))
    for slug, pp in P["external"]:
        say("  (project of %s, untouched, still at: %s)" % (slug, pp))
    if not a.keep_edited and (P["edited"] or P["extras"]):
        say("Edited kit files: %s" % os.path.join(keep_final, "_edited-kit-files"))
    say("settings.json backup: %s" % os.path.join(keep_final, "_uninstall-backups", "settings.json"))
    for cm, st in claude_md_res:
        say("CLAUDE.md %s: %s" % (cm, st))
    if P["claude_md"]:
        say("CLAUDE.md still mentions the kit/vault on %d line(s) (not edited): %s" % (len(P["claude_md"]), P["claude_md"][0][0]))
    say("Start a new Claude session so the removed skills disappear from the list.")
    say("To reinstall later: follow the website setup (SETUP-FOR-CLAUDE.md at https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main/SETUP-FOR-CLAUDE.md) or the README of the claudes-vault repo (romangigliotti123-arch/claudes-vault). Your games folder can be copied back into <vault>/Games.")
    return 0 if (vault_gone or pending) and not failed and hooks_ok and mods_ok else 1


def main(argv):
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Remove the Roblox Dev Mastery Vault kit and keep only your games (dry run unless --yes).")
    ap.add_argument("--vault")
    ap.add_argument("--keep-dir", help="where the games are copied (default: the PARENT folder of the vault folder)")
    ap.add_argument("--keep-edited", action="store_true", help="leave kit files you edited in place instead of backing them up and deleting them")
    ap.add_argument("--config")
    ap.add_argument("--home", help="use DIR as the home folder (tests)")
    ap.add_argument("--dry-run", action="store_true", help="default; print the plan only")
    ap.add_argument("--yes", action="store_true", help="really do it (only after the user confirmed)")
    a = ap.parse_args(argv)
    home = norm(a.home) if a.home else os.path.expanduser("~")
    if a.config:
        config = norm(a.config)
    elif a.home:
        config = os.path.join(home, ".claude")
    else:
        config = norm(os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(home, ".claude"))
    ambient = not (a.home or a.vault)
    vault, others = find_vault(a, home, ambient)
    if not vault:
        if others:
            say("Several vault folders found, pass --vault DIR with the right one:")
            for o in others:
                say("  " + o)
        else:
            say("Could not find the vault (a folder with Roblox/, Mentor/ and claude-kit/). Pass --vault DIR.")
        return 2
    if a.keep_dir:
        keep_final, keep_note = pick_keep_final(norm(a.keep_dir))
    else:      # ONE FOLDER: Games/ Models/ My-Skills/ My-Agents/ go next to the vault folder; backups of settings.json and edited kit files go to "<vault folder name> uninstall backups" there
        keep_final, keep_note = pick_keep_final(os.path.join(os.path.dirname(vault), os.path.basename(vault) + " uninstall backups"))
    err = refuse_vault(vault, home, config, keep_final)
    if err:
        say(err)
        return 2
    if inside(keep_final, config):
        say("refusing: the keep folder is inside the config folder, which is being cleaned")
        return 2
    if not os.path.isdir(config):
        say("config folder not found: %s" % config)
        return 2
    P = plan(a, home, config, vault, keep_final)
    if others:
        say("note: other vault-like folders exist and are ignored: " + ", ".join(others))
    print_plan(P, keep_final, keep_note, a, a.yes)
    if not a.yes:
        return 0
    return run_real(a, P, keep_final, keep_note)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
