#!/usr/bin/env python3
"""update-check.py: is a newer vault/kit available? READ-ONLY (stdlib + git; Windows, macOS, Linux).
It runs `git fetch` (updates only the remote-tracking refs; no merge, no checkout, no file in the vault changes),
compares local HEAD with the remote, and compares the installed kit (manifest shas) with the vault's claude-kit.
Usage: update-check.py [--vault DIR] [--config DIR] [--remote NAME] [--no-fetch]
Prints: UP TO DATE, or N new commits (subjects, max 10), the kit skills/agents that changed, and the offer to run /rbx-update.
Exit: 0 up to date, 10 updates available, 3 cannot check."""
import argparse, hashlib, os, subprocess, sys

ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", LC_ALL="C")


def git(vault, *a, timeout=120):
    p = subprocess.run(["git", "-C", vault] + list(a), capture_output=True, text=True, timeout=timeout, env=ENV, stdin=subprocess.DEVNULL)
    return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()


def find_vault(arg):
    for c in (arg, os.environ.get("CLAUDES_VAULT"), os.path.join(os.path.expanduser("~"), "Obsidian", "claudes-vault")):
        if c and os.path.isdir(os.path.join(c, ".git")):
            return c
    return None


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def kit_stale(vault, config):
    """Installed kit (manifest) vs the vault's claude-kit working tree. Returns (n_differ, n_missing_from_install, names)."""
    man = os.path.join(config, "claude-kit", "installed.tsv")
    if not os.path.isfile(man):
        return None
    inst = {}
    for line in open(man, encoding="utf-8", errors="replace"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 2:
            inst[p[0]] = p[1]
    kit = os.path.join(vault, "claude-kit")
    differ, new, names = 0, 0, set()
    ao = ["rbx-load", "rbx-unload", "rbx-update", "rbx-check", "rbx-uninstall"]
    try:
        ao = [x.strip() for x in open(os.path.join(kit, "mode", "always-on.txt"), encoding="utf-8") if x.strip() and not x.startswith("#")] or ao
    except OSError:
        pass
    sm = "claude-kit/vault-mode"
    for sub in ("agents", "skills", "mode", "tools", "systems", "skillpack"):
        root = os.path.join(kit, sub)
        for d, dirs, files in os.walk(root):
            dirs[:] = [x for x in dirs if x != "__pycache__"]
            for fn in files:
                if fn.endswith(".pyc"):
                    continue
                full = os.path.join(d, fn)
                r = os.path.relpath(full, kit).replace(os.sep, "/")
                if sub in ("tools", "systems", "skillpack"):
                    rel = "claude-kit/" + r
                elif sub == "mode":
                    rel = sm + "/" + r[len("mode/"):]
                elif sub == "agents":
                    rel = sm + "/.claude/" + r
                else:
                    rel = r if r.split("/")[1] in ao else sm + "/.claude/" + r
                if rel not in inst:
                    new += 1
                elif inst[rel] != sha(full):
                    differ += 1
                else:
                    continue
                parts = r.split("/")
                if sub in ("skills", "agents") and len(parts) >= 2:
                    names.add(parts[1].replace(".md", "") if sub == "agents" else parts[1])
                else:
                    names.add("cold" if r.startswith("mode/cold/") else sub)
    return differ, new, sorted(names)


def kit_names(paths):
    out = set()
    for p in paths:
        q = p.split("/")
        if len(q) >= 3 and q[0] == "claude-kit" and q[1] in ("skills", "agents"):
            out.add(q[2].replace(".md", "") if q[1] == "agents" else q[2])
        elif len(q) >= 2 and q[0] == "claude-kit":
            out.add("(" + q[1] + ")")
    return sorted(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault"); ap.add_argument("--config"); ap.add_argument("--remote", default="origin"); ap.add_argument("--no-fetch", action="store_true")
    a = ap.parse_args()
    vault = find_vault(a.vault)
    if not vault:
        print("rbx-check: no vault clone found (set CLAUDES_VAULT or pass --vault). Run the vault setup first.")
        return 3
    config = a.config or os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    rc, url, _ = git(vault, "remote", "get-url", a.remote)
    if rc != 0:
        print("rbx-check: vault has no remote '%s'." % a.remote)
        return 3
    print("vault: %s\nremote: %s" % (vault, url))
    if not a.no_fetch:
        rc, _, err = git(vault, "fetch", "--quiet", a.remote)
        if rc != 0:
            print("rbx-check: cannot reach the remote (%s). No network? Nothing was changed." % (err.splitlines()[-1] if err else "fetch failed"))
            return 3
    rc, up, _ = git(vault, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    if rc != 0:
        rc, head, _ = git(vault, "symbolic-ref", "--short", "HEAD")
        up = "%s/%s" % (a.remote, head if rc == 0 else "main")
    rc, behind, err = git(vault, "rev-list", "--count", "HEAD..%s" % up)
    if rc != 0:
        print("rbx-check: cannot compare with %s (%s)." % (up, err))
        return 3
    behind = int(behind)
    _, ahead, _ = git(vault, "rev-list", "--count", "%s..HEAD" % up)
    _, lh, _ = git(vault, "rev-parse", "--short", "HEAD")
    _, rh, _ = git(vault, "rev-parse", "--short", up)
    print("local %s, remote %s (%s): %d new commit(s) on the remote%s" % (lh, rh, up, behind, (", %s local-only" % ahead) if ahead not in ("0", "") else ""))
    changed = []
    if behind:
        _, subj, _ = git(vault, "log", "--format=%s", "-n", "10", "HEAD..%s" % up)
        print("\nNew commits (newest first, max 10):")
        for s in subj.splitlines():
            print("  - " + s[:110])
        if behind > 10:
            print("  ... and %d more" % (behind - 10))
        _, files, _ = git(vault, "diff", "--name-only", "HEAD", up, "--", "claude-kit")
        changed = kit_names(files.splitlines())
        print("\nKit items changed on the remote: " + (", ".join(changed[:40]) if changed else "none"))
    stale = kit_stale(vault, config)
    kit_note = ""
    if stale is None:
        print("\nInstalled kit: no manifest at %s (kit not installed here)." % os.path.join(config, "claude-kit", "installed.tsv"))
    else:
        d, n, names = stale
        if d or n:
            kit_note = "yes"
            print("\nInstalled kit is behind the vault's claude-kit: %d file(s) differ, %d new. Items: %s" % (d, n, ", ".join(names[:30])))
        else:
            print("\nInstalled kit matches the vault's claude-kit.")
    if behind or kit_note:
        print("\nUPDATES AVAILABLE. Nothing was changed. Run /rbx-update (safe, keeps your files) or /rbx-clean (exact copy of the main vault) only if you say yes.")
        return 10
    print("\nUP TO DATE (vault and installed kit). Nothing was changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
