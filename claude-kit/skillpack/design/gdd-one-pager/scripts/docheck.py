#!/usr/bin/env python3
"""docheck.py - structural check for design documents the design skills write. Stdlib only.

  python docheck.py design/pitch.md --kind pitch
  python docheck.py design/x.md --require "Verb,Reward" --max-lines 150
  python docheck.py --selftest

Checks: required headings present (case-insensitive substring of a '#' heading), no TODO/TBD/lorem placeholders, length cap, minimum length.
It checks STRUCTURE only; whether the content is good is the critic's job (game-dev-critic). Exit 0 = pass, 1 = fail.
"""
import argparse
import re
import sys

KINDS = {
    "pitch": dict(req=["Sentence", "Title", "Thumbnail"], max=60),
    "twist": dict(req=["Base formula", "Twist", "Readability"], max=90),
    "teardown": dict(req=["Sources", "Pattern", "Do not copy"], max=150),
    "fantasy": dict(req=["Fantasy", "Feeling", "Feature check"], max=90),
    "sessions": dict(req=["Stop point", "Return hook"], max=120),
    "social": dict(req=["Hook", "Solo", "Metric"], max=100),
    "tutorial": dict(req=["Trigger", "Skip", "Mechanic"], max=120),
    "scope": dict(req=["Keep", "Deferred", "Reason"], max=100),
    "mvp": dict(req=["Acceptance", "Build order", "Out of scope"], max=120),
    "gdd": dict(req=["Pitch", "Core loop", "Progression", "Monetisation", "Scope", "Acceptance"], max=120),
    "feel": dict(req=["Action", "Sound", "Visual"], max=120),
    "quest": dict(req=["Chain", "Reward", "Teaches"], max=120),
    "theme": dict(req=["Setting", "Mobile", "Cost"], max=100),
    "sequel": dict(req=["Evidence", "Decision", "Kill criteria"], max=100),
}
PLACEHOLDER = re.compile(r"\b(TODO|TBD|lorem ipsum|XXX)\b", re.I)


def check(text, require, max_lines):
    errs = []
    heads = [h.lower() for h in re.findall(r"^#+\s*(.+)$", text, re.M)]
    for r in require:
        if not any(r.lower() in h for h in heads):
            errs.append("missing heading: " + r)
    if PLACEHOLDER.search(text):
        errs.append("placeholder text found")
    n = len([ln for ln in text.splitlines() if ln.strip()])
    if max_lines and n > max_lines:
        errs.append("too long: %d non-empty lines > %d" % (n, max_lines))
    if n < 5:
        errs.append("too short: %d non-empty lines" % n)
    return errs


def selftest():
    good = "# Pitch\n## Sentence\nx\n## Title\ny\n## Thumbnail\nz\nmore\nlines\n"
    assert check(good, KINDS["pitch"]["req"], 60) == []
    assert "missing heading: Title" in check(good.replace("## Title", "## Name"), KINDS["pitch"]["req"], 60)
    assert "placeholder text found" in check(good + "TBD\n", [], 60)
    assert any("too long" in e for e in check(good, [], 6))
    assert any("too short" in e for e in check("# a\nb\n", [], 0))
    assert set(KINDS) >= {"gdd", "mvp", "scope"}
    print("selftest ok (6 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--kind", choices=sorted(KINDS))
    ap.add_argument("--require", default="")
    ap.add_argument("--max-lines", type=int, default=0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    req = [x.strip() for x in a.require.split(",") if x.strip()]
    mx = a.max_lines
    if a.kind:
        req = req or KINDS[a.kind]["req"]
        mx = mx or KINDS[a.kind]["max"]
    errs = check(open(a.file, encoding="utf-8").read(), req, mx)
    for e in errs:
        print("FAIL", e)
    print("PASS" if not errs else "%d failure(s)" % len(errs))
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
