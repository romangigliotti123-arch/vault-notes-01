#!/usr/bin/env python3
"""idea-brief.py: the shared MARKET BRIEF the idea skills read instead of searching the web every run (stdlib only; run with `py -I` / pyrun).

File: <claude config dir>/claude-kit/state/market-brief.md (path via kit_state.py). Rebuilt only when stale (> 14 days) or on request; how: mode/cold/rbx-ideas/brief-refresh.md.

  idea-brief.py status   fresh (N days old) <path> | stale (N days old, refresh) | missing        (exit 0 always)
  idea-brief.py path     print the file path
  idea-brief.py show     print the brief (exit 1 if missing)
  idea-brief.py write    read the new brief from stdin, validate, store atomically (exit 1 + reasons on a bad brief, nothing stored)
Brief format: first line `# Market brief (YYYY-MM-DD)`, then these headings (exact): ## What is doing well now, ## What is fading, ## Patterns,
## What players ask for, ## Gaps. At most 16000 characters (~4000 tokens). Every URL must have a [source tag] on the same line.
"""
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit_state  # noqa: E402

STALE_DAYS = 14
MAX_CHARS = 16000
SECTIONS = ("What is doing well now", "What is fading", "Patterns", "What players ask for", "Gaps")
HEAD = re.compile(r"^# Market brief \((\d{4}-\d{2}-\d{2})\)\s*$")
URL = re.compile(r"https?://|www\.", re.I)
TAG = re.compile(r"\[[^\]\s][^\]]{0,30}\]")


def brief_path():
    return kit_state.path("market-brief.md")


def header_date(text):
    first = text.lstrip("﻿").split("\n", 1)[0].rstrip("\r")
    m = HEAD.match(first)
    if not m:
        return None
    try:
        return datetime.date.fromisoformat(m.group(1))
    except ValueError:
        return None


def validate(text):
    errs = []
    d = header_date(text)
    if d is None:
        errs.append("first line must be '# Market brief (YYYY-MM-DD)' with a real date")
    elif d > datetime.date.today() + datetime.timedelta(days=1):
        errs.append("header date is in the future")
    heads = {l[3:].strip() for l in text.splitlines() if l.startswith("## ")}
    for s in SECTIONS:
        if s not in heads:
            errs.append("missing section '## %s'" % s)
    if len(text) > MAX_CHARS:
        errs.append("too long: %d chars (max %d, about 4000 tokens)" % (len(text), MAX_CHARS))
    for n, l in enumerate(text.splitlines(), 1):
        if URL.search(l) and not TAG.search(re.sub(r"\]\(https?://[^)]*\)", "]", l)) :
            errs.append("line %d has a URL without a [source tag]" % n)
    return errs


def cmd_status():
    p = brief_path()
    if not os.path.isfile(p):
        print("missing")
        return 0
    d = header_date(open(p, encoding="utf-8", errors="replace").read())
    if d is None:
        print("missing")
        return 0
    age = (datetime.date.today() - d).days
    if age > STALE_DAYS:
        print("stale (%d days old, refresh)" % age)
    else:
        print("fresh (%d days old) %s" % (max(age, 0), p))
    return 0


def cmd_write():
    text = sys.stdin.buffer.read().decode("utf-8", errors="replace").replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    errs = validate(text)
    if errs:
        print("REJECTED, brief not stored:")
        for e in errs:
            print("  - " + e)
        return 1
    p = brief_path()
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, p)
    print("stored %s (%d chars)" % (p, len(text)))
    return 0


def main(argv):
    if argv == ["status"]:
        return cmd_status()
    if argv == ["path"]:
        print(brief_path())
        return 0
    if argv == ["show"]:
        p = brief_path()
        if not os.path.isfile(p):
            print("missing")
            return 1
        sys.stdout.write(open(p, encoding="utf-8", errors="replace").read())
        return 0
    if argv == ["write"]:
        return cmd_write()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
