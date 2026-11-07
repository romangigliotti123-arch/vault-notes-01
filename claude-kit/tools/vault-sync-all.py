#!/usr/bin/env python3
"""vault-sync-all.py: INTERNAL tool of the vault kit, run by install.sh / install.ps1 as the last big step of the single installer run (users never type it).
One call does the three downloads for a vault folder, in order: vault-shards.py (extra notes repositories), refs-sync.py (Roblox reference screenshots, ~30 MB) and assets-sync.py (the asset zips, ~1 GB).
Prints short progress lines (`assets: 3/6 zips ...`), FAILS SOFT (always exits 0): a failed or incomplete download prints ONE `Assets incomplete: <reason>. To finish, run (resumes): <command>` line.
Writes .rbx/claude-kit/state/assets-status.txt: line 1 = complete | incomplete | skipped | dryrun, line 2 = the ready-made closing-block bullet. Re-running resumes (assets-sync keeps verified zips and resumes partial ones).
Usage: vault-sync-all.py --vault DIR [--config DIR] [--base URL[,URL]] [--no-assets] [--dry-run] [--retry-cmd TEXT]
Standard library only. Env CLAUDE_REFS_SKIP=1 skips the references (as in refs-sync.py)."""
import argparse, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)      # python -I drops the script folder from sys.path
sys.dont_write_bytecode = True      # no __pycache__ inside the vault folder
import kit_paths  # noqa: E402


def run_stream(args, env, on_line):
    """run a child, call on_line(line) for each output line, return the exit code (255 when it could not start)"""
    try:
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env, text=True, encoding="utf-8", errors="replace")
    except OSError as e:
        on_line("could not start: %s" % e)
        return 255
    for ln in p.stdout:
        ln = ln.rstrip()
        if ln:
            on_line(ln)
    return p.wait()


def dir_gb(path):
    tot = 0
    for r, _d, fs in os.walk(path):
        for f in fs:
            try:
                tot += os.path.getsize(os.path.join(r, f))
            except OSError:
                pass
    return tot / 1e9


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True)
    ap.add_argument("--config")
    ap.add_argument("--base", action="append")
    ap.add_argument("--no-assets", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--retry-cmd", default="")
    a = ap.parse_args()
    vault = os.path.abspath(os.path.expanduser(a.vault))
    cfg = os.path.abspath(a.config) if a.config else os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    env = dict(os.environ, CLAUDE_CONFIG_DIR=cfg, PYTHONIOENCODING="utf-8")
    py = sys.executable or "python"
    base = []
    for b in (a.base or []):
        base += ["--base", b]
    dry = ["--dry-run"] if a.dry_run else []
    retry = a.retry_cmd or ("%s -I %s --vault %s" % (py, os.path.join(HERE, "vault-sync-all.py"), vault))
    state = os.path.join(kit_paths.kit_home(cfg, os.path.abspath(__file__)), "claude-kit", "state", "assets-status.txt")

    def write_state(kind, text):
        try:
            os.makedirs(os.path.dirname(state), exist_ok=True)
            with open(state, "w", encoding="utf-8", newline="\n") as f:
                f.write(kind + "\n" + text + "\n")
        except OSError:
            pass

    if not os.path.isdir(vault):
        print("Assets incomplete: vault folder not found (%s). To finish, run (resumes): %s" % (vault, retry), flush=True)
        write_state("incomplete", "- Assets: INCOMPLETE (vault folder not found). To finish, run this (it resumes): " + retry)
        return 0

    t0 = time.time()
    # 1) extra notes repositories (silent unless there are some)
    sh = os.path.join(HERE, "vault-shards.py")
    if os.path.isfile(sh):
        run_stream([py, "-I", sh, "--vault", vault] + base + dry, env, lambda l: print(l, flush=True))
    # 2) reference screenshots (optional; never blocks)
    rf = os.path.join(HERE, "refs-sync.py")
    if os.path.isfile(rf) and os.environ.get("CLAUDE_REFS_SKIP") != "1":
        print("references: syncing the Roblox reference screenshots ...", flush=True)
        run_stream([py, "-I", rf, "--config-dir", cfg] + base + dry, env, lambda l: print(l, flush=True))
    # 3) assets
    if a.no_assets:
        print("assets: skipped (--no-assets)", flush=True)
        write_state("skipped", "- Assets: not downloaded (opt-out). To download them (about 1 GB, resumes) run: " + retry.replace(" --no-assets", "").replace(" -NoAssets", ""))
        return 0
    asy = os.path.join(HERE, "assets-sync.py")
    if not os.path.isfile(asy):
        print("Assets incomplete: assets-sync.py is missing from this kit. To finish, run (resumes): %s" % retry, flush=True)
        write_state("incomplete", "- Assets: INCOMPLETE (assets-sync.py missing from this kit). To finish, run this: " + retry)
        return 0
    st = {"total": 0, "done": 0, "failed": [], "notes": []}

    def on_asset(l):
        m = re.search(r"zip\(s\) to fetch: (.*)$", l)
        if m:
            names = [x.strip() for x in m.group(1).split(",") if x.strip()]
            st["total"] = len(names)
            print("assets: %d zips to download (%s) ..." % (len(names), ", ".join(names)), flush=True)
            return
        m = re.match(r"assets-sync: (\S+) ok \(", l)
        if m:
            st["done"] += 1
            print("assets: %d/%d zips ... (%s ok)" % (st["done"], st["total"] or st["done"], m.group(1)), flush=True)
            return
        if "FAILED" in l or "could not" in l or "not reachable" in l or "skipped" in l:
            st["failed"].append(l[:160])
            st["notes"].append(l[:160])
            return
        if l.startswith("assets-sync: up to date"):
            print("assets: already up to date", flush=True)
        elif "dry run" in l:
            print("assets (dry run): " + l.split(":", 1)[-1].strip(), flush=True)

    rc = run_stream([py, "-I", asy, "--vault", vault] + base + dry, env, on_asset)
    if a.dry_run:
        write_state("dryrun", "- Assets: not downloaded (dry run, nothing was changed).")
        return 0
    reason = ""
    if rc != 0:
        reason = (st["failed"][0] if st["failed"] else "assets-sync exited with code %d" % rc)
    elif st["failed"]:
        reason = st["failed"][0]
    else:
        # verify: nothing left to fetch (a dry run reports the remaining zips)
        out = []
        run_stream([py, "-I", asy, "--vault", vault] + base + ["--dry-run"], env, out.append)
        txt = " ".join(out)
        m = re.search(r"(\d+) zip\(s\) to download", txt)
        if m and int(m.group(1)) > 0:
            reason = "%s zip(s) still missing" % m.group(1)
        elif not m and "up to date" not in txt:
            reason = "the asset source could not be checked (offline or unreachable)"
    if reason:
        reason = re.sub(r"\s+", " ", reason).strip()
        print("Assets incomplete: %s. To finish, run (resumes): %s" % (reason, retry), flush=True)
        write_state("incomplete", "- Assets: INCOMPLETE (%s). To finish, run this (it resumes where it stopped): %s" % (reason, retry))
        return 0
    if not st["done"] and not st["total"]:
        print("assets: already up to date", flush=True)
    gb = dir_gb(os.path.join(vault, "Assets"))
    print("assets: complete (%.1f GB in %s, %ds)" % (gb, os.path.join(vault, "Assets"), time.time() - t0), flush=True)
    write_state("complete", "- Assets: downloaded and verified (%.1f GB) in %s." % (gb, os.path.join(vault, "Assets")))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # fail soft
        print("Assets incomplete: %s: %s" % (type(e).__name__, str(e)[:120]), flush=True)
        sys.exit(0)
