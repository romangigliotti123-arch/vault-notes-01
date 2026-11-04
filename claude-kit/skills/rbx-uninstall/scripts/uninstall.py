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
"""
import argparse, datetime, hashlib, json, os, re, shutil, stat, subprocess, sys

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


# ---------------------------------------------------------------- locate
def find_vault(a, home, ambient):
    if a.vault:
        return norm(a.vault), []
    cands = []
    if ambient:
        e = os.environ.get("CLAUDES_VAULT")
        if e:
            cands.append(norm(e))
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
    man = os.path.join(config, "claude-kit", "installed.tsv")
    ent = {}
    src = "manifest"
    if os.path.isfile(man):
        for ln in open(man, encoding="utf-8", errors="replace").read().splitlines():
            p = ln.split("\t")
            if len(p) >= 2 and p[0].strip():
                ent[p[0].strip().replace("\\", "/")] = p[1].strip()
    else:
        # no manifest: derive the expected files from the kit source in the vault (files that differ count as edited)
        src = "kit source in vault (installed.tsv missing)"
        kit = os.path.join(vault, "claude-kit")
        ao = ["rbx-load", "rbx-unload", "rbx-update", "rbx-check", "rbx-uninstall"]
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
                    rel = ("skills/%s" % r) if r.split("/")[0] in ao else ("%s/.claude/skills/%s" % (sm, r))
                ent[rel] = sha(a)
    return ent, src


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
    # research kept too
    for n in sorted(os.listdir(vault)):
        d = os.path.join(vault, n)
        if os.path.isdir(d) and not os.path.islink(d) and n != "Games":
            if n == "My Research" or os.path.isfile(os.path.join(d, "PROTECTED-RESEARCH.md")):
                research.append(n)
    P["research"] = research
    # kit
    ent, src = read_manifest(config, vault)
    P["manifest_src"] = src
    present, edited, missing, areas = [], [], [], {}
    for rel, want in sorted(ent.items()):
        f = os.path.join(config, rel.replace("/", os.sep))
        if not os.path.isfile(f):
            missing.append(rel)
            continue
        present.append(rel)
        areas[area_of(rel)] = areas.get(area_of(rel), 0) + 1
        if want and sha(f) != want:
            edited.append(rel)
    P["ent"], P["present"], P["missing"], P["edited"], P["areas"] = ent, present, missing, edited, areas
    # leftovers
    new_files = [r + ".new" for r in present if os.path.isfile(os.path.join(config, (r + ".new").replace("/", os.sep)))]
    P["new_files"] = new_files
    kitroot = os.path.join(config, "claude-kit")
    extras = []
    if os.path.isdir(kitroot):
        for r, f in walk_files(kitroot):
            rel = "claude-kit/" + r
            if rel in ent or r in ("installed.tsv", "installed.tsv.pre-mode") or "__pycache__" in r or r.endswith(".pyc"):
                continue
            if r in ("vault-mode/loaded.json", "vault-mode/layout.json", "vault-mode/migration-last.json"):
                continue            # the mode's own bookkeeping, not user data
            extras.append(rel)
    P["extras"] = extras
    try:
        P["mode_projects"] = sorted(json.load(open(os.path.join(kitroot, "vault-mode", "loaded.json"), encoding="utf-8")).get("projects", {}).keys())
    except (OSError, ValueError):
        P["mode_projects"] = []
    st = []
    for n in ("rbx-low-usage.on", "low-usage-mode.on", "mentor-hook.off"):  # legacy marker name included
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
    lines = []
    for cm in (os.path.join(config, "CLAUDE.md"),):
        if os.path.isfile(cm):
            for i, ln in enumerate(open(cm, encoding="utf-8", errors="replace").read().splitlines(), 1):
                if KIT_RE.search(ln):
                    lines.append((cm, i, ln.strip()[:160]))
    P["claude_md"] = lines
    # vault totals
    vc, vs = count(vault)
    P["vault_files"], P["vault_bytes"] = vc, vs
    # outside-the-vault things (machine wide, only when not a --home test)
    P["sys"] = sys_items(a, home, vault)
    return P


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


def print_plan(P, keep_final, keep_note, a, real_run):
    say("=" * 70)
    say("UNINSTALL PLAN (%s)" % ("REAL RUN" if real_run else "DRY RUN - nothing is changed"))
    say("=" * 70)
    say("config folder : %s" % P["config"])
    say("vault folder  : %s  (%d files, %s)" % (P["vault"], P["vault_files"], hsize(P["vault_bytes"])))
    say("kit file list : %s" % P["manifest_src"])
    say("")
    say("KEEP - your games. They are copied to: %s" % keep_final)
    if keep_note:
        say("  (%s)" % keep_note)
    if not P["games"]:
        say("  (no game folders found in %s)" % os.path.join(P["vault"], "Games"))
    for g in P["games"]:
        say("  %-28s %-9s %5d files %9s%s" % (g["slug"], g["kind"], g["files"], hsize(g["bytes"]), "  +project/" if g["project_dir"] else ""))
    say("  whole Games/ folder: %d files, %s -> %s" % (P["games_files"], hsize(P["games_bytes"]), os.path.join(keep_final, "Games")))
    for r in P["research"]:
        say("  also kept (your own notes): %s -> %s" % (r, os.path.join(keep_final, r)))
    for slug, pp in P["external"]:
        say("  project of %s lives outside the vault, stays IN PLACE (not copied, not touched): %s" % (slug, pp))
    say("  The copy is verified by file count, size and sha256 before anything is deleted.")
    say("")
    say("REMOVE")
    say("  kit files by area : %s" % (", ".join("%s %d" % (k, v) for k, v in sorted(P["areas"].items())) or "none"))
    say("  total kit files   : %d present (%d listed but already missing)" % (len(P["present"]), len(P["missing"])))
    say("  leftovers         : %d .new files, %d state files, %d unlisted files under <config>/claude-kit" % (len(P["new_files"]), len(P["state_files"]), len(P["extras"])))
    say("  <config>/claude-kit folder (tools, systems, skillpack, the on-demand store of vault skills/agents, installed.tsv)")
    say("  Roblox dev mode copies (/rbx-load) in project folders: %d%s (removed first, only files that are still unchanged)" % (len(P["mode_projects"]), (" -> " + ", ".join(P["mode_projects"][:5])) if P["mode_projects"] else ""))
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
        s = os.path.join(config, rel.replace("/", os.sep))
        if not os.path.isfile(s) and rel.startswith("skills/") and os.path.isfile(os.path.join(config, "claude-kit", "vault-mode", ".claude", "skills", "rbx-low-usage", "scripts", "lum.py")):
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
    return [["claude", "plugin", "uninstall", "%s@%s" % (m, MARKET)] for m in MODS] + [["claude", "plugin", "marketplace", "remove", MARKET]]


def remove_mods(a, config):
    """Kit mods (Claude Code plugins). Runs BEFORE the vault is deleted. Skipped under --home tests (like schtasks)."""
    if a.home:
        say("mods: skipped (--home test)")
        return
    exe = shutil.which("claude")
    if not exe:
        say("mods: claude CLI not found; if the kit mods are installed run /plugin uninstall rbx-subagent-hud@%s, rbx-graph@%s and /plugin marketplace remove %s" % (MARKET, MARKET, MARKET))
        return
    env = dict(os.environ, CLAUDE_CONFIG_DIR=config)
    for c in mod_cmds():
        try:
            r = subprocess.run([exe] + c[1:], capture_output=True, text=True, timeout=120, env=env, stdin=subprocess.DEVNULL)
            out = (r.stdout + r.stderr).strip().splitlines()
            say("mods: %s -> %s" % (" ".join(c[1:]), "ok" if r.returncode == 0 else "exit %d (%s)" % (r.returncode, out[-1][:100] if out else "")))
        except Exception as e:
            say("mods: %s -> could not run (%s)" % (" ".join(c[1:]), e))


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
    # 1 copy + verify
    say("[1/6] copying games to %s" % keep_final)
    os.makedirs(keep_final, exist_ok=True)
    try:
        if os.path.isdir(os.path.join(vault, "Games")):
            n, s = copy_verified(os.path.join(vault, "Games"), os.path.join(keep_final, "Games"))
            say("      Games: %d files, %s verified (sha256 + size)" % (n, hsize(s)))
        for r in P["research"]:
            n, s = copy_verified(os.path.join(vault, r), os.path.join(keep_final, r))
            say("      %s: %d files, %s verified" % (r, n, hsize(s)))
        if not a.keep_edited:
            for rel in P["edited"] + P["extras"]:
                src = os.path.join(config, rel.replace("/", os.sep))
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
    vm = os.path.join(config, "claude-kit", "tools", "vault-mode.py")
    if os.path.isfile(vm) and P["mode_projects"]:
        try:
            code, out = py_run(vm, ["unload", "--all", "--config", config], config)
            say("      Roblox dev mode: %s" % (" | ".join(out.splitlines()[-3:]) if out else "exit %d" % code))
        except Exception as e:
            say("      Roblox dev mode: could not unload (%s); the copies in your project folders' .claude are listed in %s" % (e, os.path.join(config, "claude-kit", "vault-mode", "loaded.json")))
    hooks_ok = remove_hooks(P, keep_final)
    remove_sync(P)
    remove_mods(a, config)
    # 3 manifest files
    say("[3/6] deleting kit files listed in installed.tsv")
    skip = set(P["edited"] + P["extras"]) if a.keep_edited else set()
    removed = failed = 0
    stops = [config, os.path.join(config, "skills"), os.path.join(config, "agents"), os.path.join(config, "claude-kit")]
    for rel in P["present"]:
        if rel.startswith(SELF_PREFIX) or rel in skip:
            continue
        f = os.path.join(config, rel.replace("/", os.sep))
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
            climb(os.path.join(config, rel.replace("/", os.sep)), stops)
    try:
        os.rmdir(os.path.join(config, "state"))
    except OSError:
        pass
    say("      removed %d files%s" % (removed, (", %d could not be deleted" % failed) if failed else ""))
    # 4 claude-kit
    say("[4/6] deleting %s" % os.path.join(config, "claude-kit"))
    kr = os.path.join(config, "claude-kit")
    kb = os.path.join(kr, "backup")
    if os.path.isdir(kb) and not a.keep_edited:
        try:
            n, sz = copy_verified(kb, os.path.join(keep_final, "_kit-backups"))
            say("      %d backed-up originals of yours (replaced by installs) copied to %s" % (n, os.path.join(keep_final, "_kit-backups")))
        except Exception as e:
            say("      WARNING: could not copy %s (%s); it is kept, delete it by hand later" % (kb, e))
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
    rmtree(vault)
    vault_gone = not os.path.exists(vault)
    say("      %s" % ("vault folder deleted" if vault_gone else "WARNING: vault folder still exists (some files locked); delete it by hand"))
    # 6 self
    say("[6/6] removing the /rbx-uninstall skill")
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
    say("DONE" if vault_gone and not failed and hooks_ok else "DONE WITH WARNINGS (see above)")
    say("=" * 70)
    say("Your games are now in: %s" % keep_final)
    say("  %s" % os.path.join(keep_final, "Games"))
    for r in P["research"]:
        say("  %s" % os.path.join(keep_final, r))
    for slug, pp in P["external"]:
        say("  (project of %s, untouched, still at: %s)" % (slug, pp))
    if not a.keep_edited and (P["edited"] or P["extras"]):
        say("Edited kit files: %s" % os.path.join(keep_final, "_edited-kit-files"))
    say("settings.json backup: %s" % os.path.join(keep_final, "_uninstall-backups", "settings.json"))
    if P["claude_md"]:
        say("CLAUDE.md still mentions the kit/vault on %d line(s) (not edited): %s" % (len(P["claude_md"]), P["claude_md"][0][0]))
    say("Start a new Claude session so the removed skills disappear from the list.")
    say("To reinstall later: follow the website setup (SETUP-FOR-CLAUDE.md at https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main/SETUP-FOR-CLAUDE.md) or the README of the claudes-vault repo (romangigliotti123-arch/claudes-vault). Your games folder can be copied back into <vault>/Games.")
    return 0 if vault_gone and not failed and hooks_ok else 1


def main(argv):
    try:
        sys.stdout.reconfigure(errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Remove the Roblox Dev Mastery Vault kit and keep only your games (dry run unless --yes).")
    ap.add_argument("--vault")
    ap.add_argument("--keep-dir", help="where the games are copied (default ~/Roblox Games)")
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
    keep_dir = norm(a.keep_dir) if a.keep_dir else os.path.join(home, "Roblox Games")
    keep_final, keep_note = pick_keep_final(keep_dir)
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
        say("Dry run only. To do it for real the user must confirm; then run the same command with --yes.")
        return 0
    return run_real(a, P, keep_final, keep_note)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
