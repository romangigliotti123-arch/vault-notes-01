#!/usr/bin/env python3
"""poll_lint.py - lint community polls before posting. Stdlib only.

  python poll_lint.py polls.txt
  python poll_lint.py --selftest

File format: polls separated by a blank line. First line "Q: <question>", then one "- option" per line.
Checks per poll:
  count    FAIL  fewer than 2 or more than 6 options (people skip long lists)
  leading  FAIL  the question steers the answer (obviously, don't you, wouldn't you, isn't it, amazing, best ever)
  double   WARN  one question asks two things (" and " / " or " before the question mark)
  escape   WARN  no "other / none / not sure" option on a want-poll
  promise  WARN  the wording promises the winner will ship (vault: polls gauge wants, the developer keeps final design control)
  dupes    FAIL  two options are the same after lower-casing
Exit 1 on FAIL. Regexes find leads; a human reads the poll.
"""
import re
import sys

LEAD = re.compile(r"\b(obviously|don'?t you|wouldn'?t you|isn'?t it|amazing|best ever|everyone loves|surely)\b", re.I)
ESC = re.compile(r"\b(other|none|not sure|no opinion|neither)\b", re.I)
PROMISE = re.compile(r"\b(winner will (be added|ship)|we will (add|build) the winner|you decide what we build)\b", re.I)


def parse(text):
    polls = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines or not lines[0].lower().startswith("q:"):
            continue
        polls.append((lines[0][2:].strip(), [l[1:].strip() for l in lines[1:] if l.startswith("-")]))
    return polls


def lint(q, opts):
    out = []
    out.append(("count", "FAIL" if not 2 <= len(opts) <= 6 else "PASS", "%d options" % len(opts)))
    m = LEAD.search(q)
    out.append(("leading", "FAIL" if m else "PASS", m.group(0) if m else "neutral wording"))
    body = q.rstrip("?").lower()
    dbl = " and " in body or " or " in body
    out.append(("double", "WARN" if dbl else "PASS", "asks more than one thing?" if dbl else "single question"))
    out.append(("escape", "PASS" if any(ESC.search(o) for o in opts) else "WARN", "has an escape option" if any(ESC.search(o) for o in opts) else "no other/none option"))
    p = PROMISE.search(q)
    out.append(("promise", "WARN" if p else "PASS", p.group(0) if p else "no promise"))
    low = [o.lower() for o in opts]
    out.append(("dupes", "FAIL" if len(set(low)) != len(low) else "PASS", "duplicate options" if len(set(low)) != len(low) else "options distinct"))
    return out


def selftest():
    good = "Q: Which update should come first?\n- New map\n- New pets\n- Quality-of-life fixes\n- Not sure"
    (q, o), = parse(good)
    assert all(s == "PASS" for n, s, m in lint(q, o)), lint(q, o)
    r = lambda q, o: {n: s for n, s, m in lint(q, o)}
    assert r("Which map?", ["A"])["count"] == "FAIL"
    assert r("Which map?", list("abcdefg"))["count"] == "FAIL"
    assert r("Don't you love the new map?", ["Yes", "No"])["leading"] == "FAIL"
    assert r("Do you want pets and maps?", ["Yes", "No"])["double"] == "WARN"
    assert r("Which map?", ["A", "B"])["escape"] == "WARN"
    assert r("Vote: the winner will be added!", ["A", "B"])["promise"] == "WARN"
    assert r("Which map?", ["A", "a"])["dupes"] == "FAIL"
    assert len(parse(good + "\n\nQ: Two?\n- a\n- b")) == 2
    print("selftest ok (9 cases)")
    return 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv:
        print(__doc__)
        return 2
    rc = 0
    for q, o in parse(open(argv[0], encoding="utf-8-sig").read()):
        print("Q:", q)
        for n, s, m in lint(q, o):
            print("  %-4s %-8s %s" % (s, n, m))
            rc |= s == "FAIL"
    return 1 if rc else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
