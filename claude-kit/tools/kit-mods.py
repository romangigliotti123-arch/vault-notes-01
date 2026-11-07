#!/usr/bin/env python3
"""kit-mods.py: INTERNAL tool of the vault kit, run by install.sh / install.ps1 for the two kit mods (Claude Code plugins rbx-subagent-hud and rbx-graph). Users never type it.
The mods are installed at PROJECT scope of the VAULT FOLDER (claude plugin ... --scope project, run inside the vault folder): the hooks apply only to Claude sessions started in that folder, enabledPlugins lives in <vault>/.claude/settings.json
(hidden from git by vault-mode.py). No user-scope plugin or user settings are written. An older USER-scope install of the two mods is migrated (uninstalled from user scope, installed at project scope, one notice line).
Prints ONE of: `Mods installed: ...` / `Mods up to date: ...` / `Mods skipped: <reason>. Run again later: <command>` (+ the migration notice) and writes <config>/claude-kit/state/mods-block.txt (the closing-block section) and mods-choice (on|off).
Never fails the install: always exits 0. Standard library only.
Usage: kit-mods.py --kit DIR --config DIR [--vault DIR] [--no-mods | --with-mods] [--dry-run] [--on-cmd TEXT] [--off-cmd TEXT]"""
import argparse, json, os, re, shutil, subprocess, sys

MK = "roblox-vault-kit-mods"
MODS = ("rbx-subagent-hud", "rbx-graph")
LEGACY = ("workflow-hud", "vault-graph", "hud-rbxdev-vault", "graph-rbxdev-vault")


def first(t):
    for ln in (t or "").splitlines():
        if ln.strip():
            return ln.strip()[:120]
    return ""


def norm(p):
    try:
        return os.path.normcase(os.path.realpath(p))
    except OSError:
        return os.path.normcase(p or "")


def hide_settings(vault):
    """keep <vault>/.claude/settings.json (enabledPlugins of the mods) out of `git status` of the vault clone (also done by vault-mode.py load; this covers callers that install first)"""
    try:
        r = subprocess.run(["git", "-C", vault, "rev-parse", "--git-path", "info/exclude"], capture_output=True, text=True, timeout=30)
        if r.returncode != 0 or not r.stdout.strip():
            return
        ex = r.stdout.strip().splitlines()[0]
        if not os.path.isabs(ex):
            ex = os.path.join(vault, ex)
        cur = open(ex, encoding="utf-8", errors="replace").read() if os.path.exists(ex) else ""
        if "/.claude/settings.json" in cur.splitlines():
            return
        os.makedirs(os.path.dirname(ex), exist_ok=True)
        with open(ex, "a", encoding="utf-8", newline="\n") as f:
            f.write(("" if cur.endswith("\n") or not cur else "\n") + "/.claude/settings.json\n")
    except (OSError, subprocess.SubprocessError):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kit", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--vault", default="")
    ap.add_argument("--no-mods", action="store_true")
    ap.add_argument("--with-mods", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--on-cmd", default="")
    ap.add_argument("--off-cmd", default="")
    a = ap.parse_args()
    kit, cfg = os.path.abspath(a.kit), os.path.abspath(a.config)
    vault = os.path.abspath(a.vault) if a.vault and os.path.isdir(a.vault) else ""
    sd = os.path.join(cfg, "claude-kit", "state")
    on_cmd = a.on_cmd or ("python -I %s --kit %s --config %s --vault %s --with-mods" % (os.path.join(kit, "tools", "kit-mods.py"), kit, cfg, vault))
    off_cmd = a.off_cmd or on_cmd.replace("--with-mods", "--no-mods").replace("-WithMods", "-NoMods")
    modes_on = not a.no_mods
    force = a.with_mods and modes_on
    notes = []
    state, why = "", ""

    def mset(v):
        if a.dry_run:
            return
        try:
            os.makedirs(sd, exist_ok=True)
            with open(os.path.join(sd, "mods-choice"), "w", encoding="utf-8", newline="\n") as f:
                f.write(v + "\n")
        except OSError:
            pass

    choice = ""
    try:
        choice = open(os.path.join(sd, "mods-choice"), encoding="utf-8").read().strip()
    except OSError:
        pass
    # the marketplace folder: the vault's own copy (a path that survives; the installer may run from a temporary clone), else the kit's
    mods_dir = kit and os.path.join(kit, "mods")
    if vault and os.path.isfile(os.path.join(vault, "claude-kit", "mods", ".claude-plugin", "marketplace.json")):
        mods_dir = os.path.join(vault, "claude-kit", "mods")
    cl = shutil.which("claude")
    env = dict(os.environ, CLAUDE_CONFIG_DIR=cfg)

    def run(args, cwd=None):
        try:
            r = subprocess.run([cl] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, cwd=cwd or vault or kit, timeout=300)
            return r.returncode, (r.stdout or "") + (r.stderr or "")
        except (OSError, subprocess.SubprocessError) as e:
            return 1, str(e)

    def entries():
        rc, out = run(["plugin", "list", "--json"])
        if rc != 0:
            return None, out
        try:
            j = json.loads(out[out.index("["):out.rindex("]") + 1])
        except ValueError:
            return [], out
        return [e for e in j if isinstance(e, dict)], out

    try:
        if a.dry_run:
            state, why = "skipped", "dry run"
        elif not os.path.isfile(os.path.join(mods_dir, ".claude-plugin", "marketplace.json")):
            state, why = "skipped", "the mods folder is missing from this kit"
        elif not cl:
            state, why = "skipped", "the claude command was not found on this computer"
            if not modes_on:
                mset("off")
                why = "--no-mods was used"
        else:
            es, out = entries()
            if es is None:
                state, why = "skipped", "claude plugin list failed (%s)" % first(out)
            else:
                def mine(e, names):
                    i = str(e.get("id", ""))
                    return i.split("@")[0] in names and i.endswith("@" + MK)

                def here(e):
                    return e.get("scope") == "project" and vault and norm(str(e.get("projectPath", ""))) == norm(vault)

                def uninstall(e):
                    scope = e.get("scope")
                    cwd = e.get("projectPath") if scope in ("project", "local") and os.path.isdir(str(e.get("projectPath", ""))) else None
                    run(["plugin", "uninstall", e["id"]] + (["--scope", scope] if scope else []), cwd=cwd)

                leg = [e for e in es if mine(e, LEGACY)]
                for e in leg:
                    uninstall(e)
                if leg:
                    kr = os.path.join(kit, "tools", "kit-rename.py")
                    if os.path.isfile(kr):
                        subprocess.run([sys.executable, "-I", kr, "plugins", "--drop-legacy", "--config", cfg], capture_output=True, env=env)
                    run(["plugin", "marketplace", "update", MK])
                user_copies = [e for e in es if mine(e, MODS) and e.get("scope") == "user"]
                have_here = {str(e["id"]).split("@")[0] for e in es if mine(e, MODS) and here(e)}
                have = set(MODS) <= have_here
                if not modes_on:    # opt out: remove the two mods from every scope they are in (user scope copies and this vault's project scope)
                    for e in es:
                        if mine(e, MODS) and (e.get("scope") == "user" or here(e)):
                            uninstall(e)
                    mset("off")
                    state, why = "skipped", "--no-mods was used"
                elif not vault:
                    state, why = "skipped", "the vault folder was not found on this computer (the mods are installed into it)"
                elif not force and choice == "off":
                    state, why = "skipped", "you turned the mods off earlier"
                elif not force and choice == "on" and not have and not leg and not user_copies:
                    state, why = "skipped", "you removed them earlier with /plugin"
                else:
                    ok, w = True, ""
                    migrated = bool(user_copies)
                    if user_copies:      # migrate: the user-scope copies went in with an older kit and would hook ALL sessions
                        for e in user_copies:
                            uninstall(e)
                        run(["plugin", "marketplace", "remove", MK, "--scope", "user"])
                    if not have:
                        rc, r = run(["plugin", "marketplace", "add", mods_dir, "--scope", "project"])
                        if rc != 0 and "already" not in r.lower():
                            ok, w = False, "marketplace add failed (%s)" % first(r)
                        for m in MODS:
                            if not ok or m in have_here:
                                continue
                            rc, r = run(["plugin", "install", "%s@%s" % (m, MK), "--scope", "project"])
                            if rc != 0 and "already" not in r.lower():
                                ok, w = False, "install of %s failed (%s)" % (m, first(r))
                    if ok:   # copy semantics: an installed plugin keeps its old copy until updated
                        run(["plugin", "marketplace", "update", MK])
                        for m in MODS:
                            run(["plugin", "update", "%s@%s" % (m, MK), "--scope", "project"])
                        mset("on")
                        hide_settings(vault)
                        state = "installed" if (not have or migrated) else "uptodate"
                        if migrated:
                            notes.append("Mods moved: the two mods were in your Claude user settings (all sessions); they are now installed for the vault folder only (%s)." % vault)
                    else:
                        state, why = "skipped", w
    except Exception as e:      # never fail the install
        state, why = "skipped", "the mods step failed (%s)" % str(e)[:100]

    if state == "installed":
        line = "Mods installed: rbx-subagent-hud, rbx-graph"
    elif state == "uptodate":
        line = "Mods up to date: rbx-subagent-hud, rbx-graph"
    else:
        line = "Mods skipped: %s. Run again later: %s" % (why, on_cmd)
    for n in notes:
        print(n)
    print(line)
    if state in ("installed", "uptodate"):
        blk = "\n".join([
            "**THE TWO MODS (ALREADY INSTALLED)**",
            "- Type /reload-plugins once; they run in the vault folder only. Remove: /plugin, or the installer's --no-mods."])
    else:
        blk = "\n".join([
            "**THE TWO MODS (NOT INSTALLED)**",
            "- Skipped: %s. Install them: %s   then start a new session in the vault folder." % (why, on_cmd)])
    if not a.dry_run:
        try:
            os.makedirs(sd, exist_ok=True)
            with open(os.path.join(sd, "mods-block.txt"), "w", encoding="utf-8", newline="\n") as f:
                f.write(blk + "\n")
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print("Mods skipped: the mods step failed (%s). Run again later: install again with the same command" % str(e)[:100])
        sys.exit(0)
