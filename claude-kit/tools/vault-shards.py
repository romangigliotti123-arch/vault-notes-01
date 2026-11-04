#!/usr/bin/env python3
"""vault-shards.py - overlay the extra repository shards (vault-notes-02, -03, ..., and vault-kit-02, ...) listed in repos.json onto the vault (stdlib + git; Windows/macOS/Linux).

  python vault-shards.py --vault <vault folder> [--base URL ...] [--dry-run]

The vault's main clone is shard 01 (vault-notes-01). When a repository group grows, the publisher moves whole folders into the next numbered repository and lists it in
repos.json (<base>/repos.json; the same file assets-sync.py reads). This tool clones each extra shard into a hidden git directory <vault>/.git/shards/<name> that uses the
vault folder as its work tree, so the files appear at their normal paths; the paths of different shards never overlap. They are added to <vault>/.git/info/exclude so the
main repository ignores them. Read-only: fetch + reset --hard of tracked files of that shard only; nothing else in the vault is touched. Prints nothing when there is
nothing to do (also when repos.json lists no extra shard). Always exits 0 unless --vault is missing (2). Never commits or pushes.
"""
import argparse, json, os, re, subprocess, sys, urllib.request

# filled in by the site build with the vault-kit raw URL and the website
DEFAULT_BASES = ["https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main", "https://vault-hhmi60uo.netlify.app"]
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0")
NAME_RX = re.compile(r"vault-(?:notes|kit)-\d{2,4}")
OWNERS = [o.strip().lower() for o in os.environ.get("VAULT_ALLOWED_OWNERS", "romangigliotti123-arch").split(",") if o.strip()]   # "*" accepts any github.com owner


def repo_allowed(url):
    if os.environ.get("VAULT_SHARDS_TEST_ANY_URL"):
        return True
    m = re.fullmatch(r"https://github\.com/([A-Za-z0-9._-]+)/[A-Za-z0-9._-]+(?:\.git)?", url or "")
    return bool(m) and ("*" in OWNERS or m.group(1).lower() in OWNERS)


def unsafe_mount(m):
    return (not isinstance(m, str)) or not m.strip("/") or m.startswith(("/", ".")) or ".." in m.split("/") or ":" in m or "\\" in m or m.startswith(("My Research", "Games"))


def outside_mount(paths, mount):
    ms = [m.rstrip("/") for m in mount]
    return [p for p in paths if not any(p == m or p.startswith(m + "/") for m in ms)]


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
        return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV, stdin=subprocess.DEVNULL, timeout=900)
    except (OSError, subprocess.SubprocessError):
        return subprocess.CompletedProcess(cmd, 1, "", "git not available or timed out")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True)
    ap.add_argument("--base", action="append")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    vault = os.path.abspath(os.path.expanduser(a.vault))
    if not os.path.isdir(vault):
        print("vault-shards: vault folder not found: %s" % vault)
        return 2
    if not os.path.isdir(os.path.join(vault, ".git")):
        return 0
    bases = [x.strip() for b in (a.base or DEFAULT_BASES) for x in b.split(",") if x.strip()]
    j = fetch_json(bases)
    if not j:
        return 0                       # offline or older manifest: nothing to do
    for group in ("notes", "kit"):
        for sh in (j["groups"].get(group, {}).get("shards") or [])[1:]:
            name, url, mount = str(sh.get("name", "")), str(sh.get("git", "")), sh.get("mount") or []
            if not NAME_RX.fullmatch(name) or not mount or not isinstance(mount, list):
                continue
            if not repo_allowed(url):
                print("vault-shards: skipped %s (repository is not under github.com/%s; set VAULT_ALLOWED_OWNERS to accept another owner)" % (name, OWNERS[0] if OWNERS else "?"))
                continue
            if any(unsafe_mount(m) for m in mount):
                print("vault-shards: skipped %s (unsafe mount list)" % name)
                continue
            if a.dry_run:
                print("vault-shards (dry run): would update %s (%s) -> %s" % (name, ", ".join(mount), vault))
                continue
            gd = os.path.join(vault, ".git", "shards", name)
            first = not os.path.isdir(gd)
            if first:
                os.makedirs(gd, exist_ok=True)
                if git(gd, None, "init", "-q", "--bare").returncode != 0:
                    print("vault-shards: git init failed for %s" % name)
                    if not os.listdir(gd):
                        os.rmdir(gd)
                    continue
                git(gd, None, "config", "core.bare", "false")
            for k, v in (("core.autocrlf", "false"), ("core.safecrlf", "false"), ("core.longpaths", "true"), ("core.symlinks", "false")):
                git(gd, vault, "config", k, v)
            before = git(gd, vault, "rev-parse", "-q", "--verify", "HEAD").stdout.strip()
            f = git(gd, vault, "fetch", "-q", url, "main")
            if f.returncode != 0:
                print("vault-shards: fetch of %s failed (offline?), left as it is" % name)
                continue
            tr = git(gd, vault, "ls-tree", "-r", "-z", "--name-only", "FETCH_HEAD")
            bad = outside_mount([x for x in tr.stdout.split("\0") if x], mount) if tr.returncode == 0 else ["(file list unreadable)"]
            if bad:
                print("vault-shards: refused %s (%d tracked path(s) outside its mount list, first: %s); nothing written" % (name, len(bad), bad[0][:80]))
                continue
            r = git(gd, vault, "reset", "--hard", "-q", "FETCH_HEAD")
            if r.returncode != 0:
                print("vault-shards: could not update %s: %s" % (name, r.stderr.strip()[-200:]))
                continue
            ex = os.path.join(vault, ".git", "info", "exclude")
            try:
                cur = open(ex, encoding="utf-8", errors="replace").read() if os.path.exists(ex) else ""
                add = [("/" + m) for m in mount if ("/" + m) not in cur.splitlines()]
                if add:
                    os.makedirs(os.path.dirname(ex), exist_ok=True)
                    with open(ex, "a", encoding="utf-8") as fh:
                        fh.write(("" if cur.endswith("\n") or not cur else "\n") + "\n".join(add) + "\n")
            except OSError:
                pass
            after = git(gd, vault, "rev-parse", "--short", "HEAD").stdout.strip()
            if first or before != git(gd, vault, "rev-parse", "-q", "--verify", "HEAD").stdout.strip():
                print("vault-shards: %s %s (%s)" % (name, "installed" if first else "updated", after))
    return 0


if __name__ == "__main__":
    sys.exit(main())
