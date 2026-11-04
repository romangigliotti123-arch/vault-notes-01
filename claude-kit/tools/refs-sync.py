#!/usr/bin/env python3
"""refs-sync.py - fetch/update the Roblox reference screenshots (public repos vault-refs-01, -02, ... listed in repos.json) and point the visual-QA step at them (stdlib + git; Windows/macOS/Linux).

  python refs-sync.py [--config-dir DIR] [--dest DIR] [--base URL ...] [--dry-run] [--force-pointer]

What it does
 1. reads <base>/repos.json (groups.refs.shards; the same file assets-sync.py and vault-shards.py read);
 2. clones/updates every refs shard (shallow, read-only) into ONE folder, default <claude config dir>/claude-kit/roblox-reference/, so every path in INDEX.md exists:
    shard 01 holds INDEX.md, README.md, NOTICE.md and most of img/; a later shard holds whole img/<game>/ folders (its "mount" list) and is overlaid on the same folder.
    Each shard keeps its git data in <dest>/.refs-git/<name> (work tree = <dest>); only files that shard tracks are written or removed;
 3. writes <claude config dir>/claude-kit/reference-path.txt (line 1 = absolute path of <dest>), the file the visual-QA and art-direction skills read. An existing pointer that
    leads to another folder holding an INDEX.md (the user's own library) is left alone unless --force-pointer is given.
<claude config dir> = --config-dir, else $CLAUDE_CONFIG_DIR, else $CLAUDE_KIT_HOME/.claude, else ~/.claude.
Silent when nothing changed. Silent (exit 0) when repos.json or GitHub is unreachable or lists no refs group: the references are optional. Prints one line when it installed or updated a shard.
Env CLAUDE_REFS_SKIP=1 does nothing (used by kit-refresh). The images are third-party frames (see NOTICE.md in the folder): comparison only, never copy them into a game.
Exit code 0 always, except 2 for usage errors.
"""
import argparse, json, os, subprocess, sys, urllib.request

# filled in by the site build with the vault-kit raw URL and the website
DEFAULT_BASES = ["https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main", "https://vault-hhmi60uo.netlify.app"]
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0")


def fetch_json(bases):
    for b in bases:
        try:
            with urllib.request.urlopen(b.rstrip("/") + "/repos.json", timeout=20) as r:
                j = json.loads(r.read(1 << 20).decode("utf-8", "replace"))
            if isinstance(j, dict) and isinstance(j.get("groups"), dict):
                return j
        except Exception:
            continue
    return None


def git(gd, wt, *a):
    cmd = ["git", "--git-dir", gd] + (["--work-tree", wt] if wt else []) + list(a)
    try:
        return subprocess.run(cmd, capture_output=True, text=True, env=ENV, stdin=subprocess.DEVNULL, timeout=900)
    except (OSError, subprocess.SubprocessError):
        return subprocess.CompletedProcess(cmd, 1, "", "git not available or timed out")


def config_dir(arg):
    if arg:
        return os.path.abspath(os.path.expanduser(arg))
    if os.environ.get("CLAUDE_CONFIG_DIR"):
        return os.path.abspath(os.path.expanduser(os.environ["CLAUDE_CONFIG_DIR"]))
    if os.environ.get("CLAUDE_KIT_HOME"):
        return os.path.join(os.path.abspath(os.path.expanduser(os.environ["CLAUDE_KIT_HOME"])), ".claude")
    return os.path.join(os.path.expanduser("~"), ".claude")


def unsafe(m):
    return (not isinstance(m, str)) or not m or m.startswith(("/", ".", "\\")) or ".." in m.split("/") or ":" in m or "\\" in m


def write_pointer(cfg, dest, force, say):
    ptr = os.path.join(cfg, "claude-kit", "reference-path.txt")
    want = os.path.abspath(dest)
    try:
        cur = open(ptr, encoding="utf-8", errors="replace").read().splitlines()
        cur = cur[0].strip() if cur else ""
    except OSError:
        cur = ""
    if cur and os.path.abspath(cur) == want:
        return
    if cur and not force and os.path.abspath(cur) != want and os.path.isfile(os.path.join(cur, "INDEX.md")):
        return      # the user's own reference library: do not take it over
    try:
        os.makedirs(os.path.dirname(ptr), exist_ok=True)
        with open(ptr, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(want + "\n")
        say("refs-sync: reference-path.txt -> %s" % want)
    except OSError:
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config-dir")
    ap.add_argument("--dest")
    ap.add_argument("--base", action="append")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force-pointer", action="store_true")
    a = ap.parse_args()
    if os.environ.get("CLAUDE_REFS_SKIP") == "1":
        return 0
    cfg = config_dir(a.config_dir)
    dest = os.path.abspath(os.path.expanduser(a.dest)) if a.dest else os.path.join(cfg, "claude-kit", "roblox-reference")
    bases = [x.strip() for b in (a.base or DEFAULT_BASES) for x in b.split(",") if x.strip()]
    j = fetch_json(bases)
    if not j:
        return 0                       # offline or older manifest: nothing to do
    shards = (j["groups"].get("refs") or {}).get("shards") or []
    shards = [s for s in shards if isinstance(s, dict)]
    if not shards:
        return 0
    out = []
    say = lambda m: (out.append(m), print(m, flush=True))
    ok_any = False
    for i, sh in enumerate(shards):
        name, url, mount = str(sh.get("name", "")), str(sh.get("git", "")), sh.get("mount") or []
        if not name.startswith("vault-refs-") or "/" in name or "\\" in name or ".." in name:
            continue
        if not (url.startswith("https://github.com/") or os.environ.get("VAULT_SHARDS_TEST_ANY_URL")):
            continue
        if any(unsafe(m) for m in mount):
            say("refs-sync: skipped %s (unsafe mount list)" % name)
            continue
        if a.dry_run:
            say("refs-sync (dry run): would update %s (%s) -> %s" % (name, ", ".join(mount) or "all unclaimed files", dest))
            continue
        gd = os.path.join(dest, ".refs-git", name)
        first = not os.path.isdir(gd)
        os.makedirs(gd, exist_ok=True)
        if first:
            if git(gd, None, "init", "-q", "--bare").returncode != 0:
                if not os.listdir(gd):
                    os.rmdir(gd)
                continue
            git(gd, None, "config", "core.bare", "false")
        for k, v in (("core.autocrlf", "false"), ("core.safecrlf", "false"), ("core.longpaths", "true"), ("core.symlinks", "false")):
            git(gd, dest, "config", k, v)
        before = git(gd, dest, "rev-parse", "-q", "--verify", "HEAD").stdout.strip()
        if git(gd, dest, "fetch", "-q", "--depth", "1", url, "main").returncode != 0:
            ok_any = ok_any or bool(before)
            continue                    # offline: keep what is there
        if git(gd, dest, "reset", "--hard", "-q", "FETCH_HEAD").returncode != 0:
            continue
        ok_any = True
        after = git(gd, dest, "rev-parse", "-q", "--verify", "HEAD").stdout.strip()
        if first or before != after:
            say("refs-sync: %s %s (%s) -> %s" % (name, "installed" if first else "updated", after[:7], dest))
    if not a.dry_run and ok_any and os.path.isfile(os.path.join(dest, "INDEX.md")):
        write_pointer(cfg, dest, a.force_pointer, say)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)                    # optional feature: never break the caller
