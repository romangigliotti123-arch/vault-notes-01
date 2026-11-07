#!/usr/bin/env python3
"""freshness - date the vault notes a skill used and print the one-line freshness report.

  python freshness.py [--vault DIR] [--pull] [--fast-moving] [--stale-days 30] NOTE [NOTE ...]

NOTE is a path (absolute, or relative to the vault), a KB topic name (ads-and-sponsored-experiences) or
_tools/NAME (AD-PLAYBOOK). Nothing is written; the vault is only read (--pull runs `git pull --ff-only`, 60 s limit, never prompts).
Date of a note, first hit wins: front-matter `source_dates: A to B` (B), `_Generated YYYY-MM-DD_`, front-matter
date/updated/created, the last git commit that touched it, the file mtime (weakest: a fresh clone resets it).
Prints one `path | date | how` line per note (newest first), then the FRESHNESS line the skill must show the user.
Exit code 0 always (a stale or missing note is reported, not an error); 2 if no vault was found.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys


def vault_dir(arg):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))      # python -I drops the script folder from sys.path
    import kit_paths  # ONE FOLDER: own location, env, pointer, cwd, defaults
    cands = [arg, os.environ.get("CLAUDES_VAULT"), os.environ.get("RBX_DEV_VAULT"), kit_paths.find_vault(None, os.path.abspath(__file__))] + kit_paths.defaults()
    for c in cands:
        if c and os.path.isdir(os.path.join(c, "Roblox")):
            return os.path.abspath(c)
    return None


def pull(vault):
    if not os.path.isdir(os.path.join(vault, ".git")):
        return "not-a-git-clone"
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    try:
        head0 = subprocess.run(["git", "-C", vault, "rev-parse", "HEAD"], capture_output=True, text=True, timeout=20, env=env).stdout.strip()
        r = subprocess.run(["git", "-C", vault, "pull", "--ff-only", "-q"], capture_output=True, text=True, timeout=60, env=env)
        if r.returncode != 0:
            return "pull-failed(offline-or-diverged)"
        head1 = subprocess.run(["git", "-C", vault, "rev-parse", "HEAD"], capture_output=True, text=True, timeout=20, env=env).stdout.strip()
        return "up-to-date" if head0 == head1 else "pulled-new-commits"
    except Exception as e:  # git missing, timeout
        return "pull-skipped(%s)" % type(e).__name__


def resolve(vault, n):
    kb = os.path.join(vault, "Roblox", "roblox-kb")
    for p in (n, os.path.join(vault, n), os.path.join(kb, n), os.path.join(kb, n + ".md"), os.path.join(kb, "_tools", n + ".md"), os.path.join(vault, n + ".md")):
        if os.path.isfile(p):
            return os.path.abspath(p)
    return None


def note_date(vault, path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            head = f.read(6000)
    except OSError:
        return None, "unreadable"
    m = re.search(r"^source_dates:\s*(\d{4}-\d{2}(?:-\d{2})?)\s+to\s+(\d{4}-\d{2}(?:-\d{2})?)", head, re.M)
    if m:
        return m.group(2), "source_dates"
    m = re.search(r"_Generated (\d{4}-\d{2}-\d{2})", head)
    if m:
        return m.group(1), "generated-line"
    m = re.search(r"^(?:date|updated|created|last_updated|published):\s*[\"']?(\d{4}-\d{2}-\d{2})", head, re.M)
    if m:
        return m.group(1), "frontmatter"
    try:
        rel = os.path.relpath(path, vault)
        r = subprocess.run(["git", "-C", vault, "log", "-1", "--format=%cs", "--", rel], capture_output=True, text=True, timeout=20)
        d = r.stdout.strip()
        if r.returncode == 0 and re.match(r"^\d{4}-\d{2}-\d{2}$", d):
            return d, "git-commit"
    except Exception:
        pass
    return datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat(), "mtime(weak)"


def to_date(s):
    if len(s) == 7:
        s += "-28"  # month-only dates count as end of month (conservative: looks fresher, flagged by "how")
    return datetime.date.fromisoformat(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("notes", nargs="*")
    ap.add_argument("--vault")
    ap.add_argument("--pull", action="store_true")
    ap.add_argument("--fast-moving", action="store_true", help="topic has fast-moving facts (ad costs, policy, image models): live check always required")
    ap.add_argument("--stale-days", type=int, default=30)
    a = ap.parse_args()
    vault = vault_dir(a.vault)
    if not vault:
        print("FRESHNESS: vault NOT FOUND (fix: python \"%s\" --set \"<your vault folder>\" once, or set RBX_DEV_VAULT); live check REQUIRED; say that nothing came from the vault" % os.path.join(os.path.dirname(os.path.abspath(__file__)), "kit_paths.py").replace("\\", "/"))
        return 2
    status = pull(vault) if a.pull else "not-pulled(--pull not given)"
    today = datetime.date.fromisoformat(os.environ["FRESHNESS_TODAY"]) if os.environ.get("FRESHNESS_TODAY") else datetime.date.today()
    rows, missing = [], []
    for n in a.notes:
        p = resolve(vault, n)
        if not p:
            missing.append(n)
            continue
        if any(os.path.abspath(p) == os.path.abspath(os.path.join(vault, r[1])) for r in rows):
            continue
        d, how = note_date(vault, p)
        if d:
            rows.append((to_date(d), os.path.relpath(p, vault).replace("\\", "/"), d, how))
    rows.sort(key=lambda r: r[0], reverse=True)
    for _, rel, d, how in rows:
        print("%s | %s | %s" % (rel, d, how))
    for m in missing:
        print("%s | MISSING | not found in vault (KB gap)" % m)
    if rows:
        newest, oldest = rows[0][0], rows[-1][0]
        age = (today - newest).days
        reasons = []
        if age > a.stale_days:
            reasons.append("newest relevant note is %d days old (> %d)" % (age, a.stale_days))
        if a.fast_moving:
            reasons.append("fast-moving facts")
        if missing:
            reasons.append("%d note(s) missing" % len(missing))
        live = "REQUIRED (" + "; ".join(reasons) + ")" if reasons else "not required"
        print("FRESHNESS: pull=%s; %d note(s) used, newest %s (%d d old), oldest %s (%d d old); live check %s" % (
            status, len(rows), rows[0][2], age, rows[-1][2], (today - oldest).days, live))
    else:
        print("FRESHNESS: pull=%s; no dated notes found; live check REQUIRED" % status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
