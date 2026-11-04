#!/usr/bin/env python3
"""vault-shards.py - overlay the extra repository shards (vault-notes-02, -03, ..., and vault-kit-02, ...) listed in repos.json onto the vault (stdlib + git; Windows/macOS/Linux).

  python vault-shards.py --vault <vault folder> [--base URL ...] [--dry-run]

The vault's main clone is shard 01 (vault-notes-01). When a repository group grows, the publisher moves whole folders into the next numbered repository and lists it in
repos.json (<base>/repos.json; the same file assets-sync.py reads). This tool clones each extra shard into a hidden git directory <vault>/.git/shards/<name> that uses the
vault folder as its work tree, so the files appear at their normal paths; the paths of different shards never overlap. They are added to <vault>/.git/info/exclude so the
main repository ignores them. Read-only: fetch + reset --hard of tracked files of that shard only; nothing else in the vault is touched. Prints nothing when there is
nothing to do (also when repos.json lists no extra shard). Always exits 0 unless --vault is missing (2). Never commits or pushes.
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
            name, url, mount = sh.get("name", ""), sh.get("git", ""), sh.get("mount") or []
            if not name.startswith("vault-") or not (url.startswith("https://github.com/") or os.environ.get("VAULT_SHARDS_TEST_ANY_URL")) or not mount:
                continue
            if any((not isinstance(m, str)) or m.startswith(("/", ".")) or ".." in m.split("/") or m.startswith("My Research") or m.startswith("Games") for m in mount):
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
