#!/usr/bin/env python3
"""briefcheck.py - lint a worker brief before it is sent. Stdlib only.

  python briefcheck.py brief.md [--max-words 600]
  python briefcheck.py --selftest

A brief passes when it has: GOAL, CONTEXT or INPUTS, a write fence (OWNS or SCOPE), DONE WHEN with numbered items that each
name a check, an evidence rule, a STOP RULE, a BUDGET, a REPORT format with an honest exit (untested / not checked),
is self-contained (no 'as discussed', 'see above', 'based on your findings'), and does not shout (more than 3 all-caps words
outside the field labels). Exit 0 pass, 1 fail. It checks the shape; whether the goal is right is the manager's call.
"""
import argparse
import re
import sys

FIELDS = ["GOAL", "DONE WHEN", "STOP RULE", "BUDGET", "REPORT"]
NOT_SELF = re.compile(r"as discussed|see above|as before|based on your findings|like last time|the previous (?:chat|conversation)", re.I)
CHECKWORD = re.compile(r"`[^`]+`|\brun\b|\bexit\b|\bexists?\b|\bprints?\b|\bpasses?\b|\bhash\b|\bgrep\b|\bcount\b|\bsize\b", re.I)
LABELS = set(
    "GOAL CONTEXT INPUTS OWNS SCOPE VERIFY RESULT CRITERIA CHANGES PROBLEMS NEEDS NOT CHECKED UNTESTED DONE WHEN STOP RULE NEXT "
    "SUGGESTED ARTIFACTS ROMAN HEADLINE PRE REPORT BUDGET PARTIAL YOURSELF FORMAT CHECK JSON HTML UTF SHA".split()
)


def lint(text, max_words=600):
    errs = []
    up = text.upper()
    for f in FIELDS:
        if f not in up:
            errs.append("missing field: " + f)
    if "CONTEXT" not in up and "INPUTS" not in up:
        errs.append("missing CONTEXT or INPUTS (paths to read)")
    if "OWNS" not in up and "SCOPE" not in up:
        errs.append("missing write fence (OWNS or SCOPE)")
    m = re.search(r"DONE WHEN[^\n]*\n((?:\s*\d+[.)].*\n?)+)", text, re.I)
    if not m:
        errs.append("DONE WHEN has no numbered items")
    else:
        items = [ln for ln in m.group(1).splitlines() if ln.strip()]
        weak = [ln.strip()[:40] for ln in items if not CHECKWORD.search(ln)]
        if weak:
            errs.append("DONE WHEN items without a check: " + " | ".join(weak))
    if not re.search(r"untested|not checked|not verified|cannot", text, re.I):
        errs.append("no honest exit (say what to do when a check cannot run)")
    if not re.search(r"evidence|excerpt|output", text, re.I):
        errs.append("no evidence rule (command + output excerpt)")
    hit = NOT_SELF.search(text)
    if hit:
        errs.append("not self-contained: " + hit.group(0))
    caps = [w for w in re.findall(r"\b[A-Z]{4,}\b", text) if w not in LABELS]
    if len(caps) > 3:
        errs.append("shouting: " + ", ".join(sorted(set(caps))[:5]))
    if len(text.split()) > max_words:
        errs.append("too long: %d words > %d (move detail to files, point to paths)" % (len(text.split()), max_words))
    return errs


GOOD = """GOAL: add a rate limit to the Shop purchase remote so a spammed call is rejected.
CONTEXT: read ./src/server/Shop.luau and ./docs/GDD.md section 4. Already ruled out: client-side checks (they are bypassable).
OWNS: ./src/server/Shop.luau and ./src/server/tests/ShopRate.spec.luau. Do not touch anything else.
DONE WHEN:
1. `luau-check.sh src/server/Shop.luau` ends with no errors.
2. `lune run src/server/tests/ShopRate.spec.luau` prints PASS for the 3rd call in one second being rejected.
VERIFY YOURSELF: run each check and paste the command and an exact output excerpt; if a tool is missing write untested.
BUDGET: about 30 tool calls. STOP RULE: one retry per failing step, then report PARTIAL with the exact blocker.
REPORT: RESULT, CRITERIA with evidence, CHANGES, NOT_CHECKED, PROBLEMS. At most 250 words.
"""


def selftest():
    assert lint(GOOD) == [], lint(GOOD)
    assert any("DONE WHEN" in e for e in lint(GOOD.replace("DONE WHEN:", "DONE:")))
    e = lint(GOOD.replace("1. `luau-check.sh src/server/Shop.luau` ends with no errors.", "1. make it good"))
    assert any("without a check" in x for x in e), e
    assert any("self-contained" in x for x in lint(GOOD + "As discussed, fix it.\n"))
    assert any("shouting" in x for x in lint(GOOD + "MUST ALWAYS NEVER ABSOLUTELY DO THIS\n"))
    quiet = GOOD.replace("untested", "fine").replace("NOT_CHECKED", "X").replace("cannot", "can")
    assert any("honest exit" in x for x in lint(quiet)), lint(quiet)
    assert any("too long" in x for x in lint(GOOD + "word " * 700))
    print("selftest ok (7 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--max-words", type=int, default=600)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    errs = lint(open(a.file, encoding="utf-8").read(), a.max_words)
    print("PASS" if not errs else "FAIL:\n- " + "\n- ".join(errs))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
