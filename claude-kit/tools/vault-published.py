#!/usr/bin/env python3
"""Last line of /rbx-update: `Your vault is up to date as of Thursday 5 November 2026, 8:40 am (local time)`.
Time = newest commit date (git log -1 --format=%cI) of the vault clone and of the kit folder's repo (when that is a different repo), in the machine's local time zone.
No git or no date: prints `Your vault is up to date.` Never fails (exit 0). Usage: vault-published.py [--vault DIR] [--kit DIR] [--utc-offset +HH:MM]
--where: first print `Vault: <folder> | Kit: <folder>` (installed kit = $CLAUDE_CONFIG_DIR or ~/.claude + claude-kit; `Vault: not found (set CLAUDES_VAULT)` when no clone). Test hook: env VAULT_PUBLISHED_UTC_OFFSET (same as --utc-offset) fixes the zone."""
import argparse, os, subprocess, sys
from datetime import datetime, timedelta, timezone

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
PLAIN = "Your vault is up to date."


def fmt(dt):
    return "%s %d %s %d, %d:%02d %s" % (DAYS[dt.weekday()], dt.day, MONTHS[dt.month - 1], dt.year, dt.hour % 12 or 12, dt.minute, "am" if dt.hour < 12 else "pm")


def git(d, *a):
    try:
        r = subprocess.run(["git", "-C", d] + list(a), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20,
                           env=dict(os.environ, GIT_TERMINAL_PROMPT="0"))
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def commit_date(d):
    s = git(d, "log", "-1", "--format=%cI")
    try:
        return datetime.fromisoformat(s) if s else None
    except ValueError:
        return None


def repo_dates(dirs):
    seen, out = set(), []
    for d in dirs:
        if not d or not os.path.isdir(d):
            continue
        top = os.path.normcase(os.path.realpath(git(d, "rev-parse", "--show-toplevel") or d))
        if top in seen:
            continue
        seen.add(top)
        dt = commit_date(d)
        if dt is not None and dt.tzinfo is not None:
            out.append(dt)
    return out


def parse_offset(s):
    sign = -1 if s.startswith("-") else 1
    h, _, m = s.lstrip("+-").partition(":")
    return timezone(sign * timedelta(hours=int(h), minutes=int(m or 0)))


def where(vault):
    home = os.path.expanduser("~")
    v = next((os.path.normpath(c) for c in (vault, os.path.join(home, "Obsidian", "claudes-vault")) if c and os.path.exists(os.path.join(c, ".git"))), "")
    k = os.path.join(os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.environ.get("CLAUDE_KIT_HOME") or home, ".claude"), "claude-kit")
    return "Vault: %s | Kit: %s" % (v or "not found (set CLAUDES_VAULT)", os.path.normpath(k))


def line(dirs, tz=None):
    dates = repo_dates(dirs)
    if not dates:
        return PLAIN
    return "Your vault is up to date as of %s (local time)" % fmt(max(dates).astimezone(tz))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault")
    ap.add_argument("--kit")
    ap.add_argument("--where", action="store_true")
    ap.add_argument("--utc-offset", default=os.environ.get("VAULT_PUBLISHED_UTC_OFFSET", ""))
    a = ap.parse_args(argv)
    vault = a.vault or os.environ.get("CLAUDES_VAULT") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if a.where:
        try:
            print(where(vault))
        except Exception:
            print("Vault: not found (set CLAUDES_VAULT)")
    try:
        kit = a.kit or os.path.join(vault, "claude-kit")
        print(line([vault, kit], parse_offset(a.utc_offset) if a.utc_offset else None))
    except Exception:
        print(PLAIN)
    return 0


if __name__ == "__main__":
    sys.exit(main())
