#!/usr/bin/env python3
"""milestone.py - verdict on a milestone from its acceptance table. Stdlib only.

  python milestone.py review.md
  python milestone.py --selftest

Reads a markdown table whose header has the columns  criterion | result | evidence  (result: met, unmet, untested).
Verdict: PASS only if every row is `met` with non-empty evidence that is not narration; HOLD if any row is `untested`
(untested is not a pass: say what is needed to run it); FAIL if any row is `unmet` or a `met` row has no evidence.
Prints the gaps to close. A PASS means the table is complete, not that the evidence is true: the worker-verifier skill
re-runs one check per load-bearing row. Exit 0 PASS, 1 otherwise.
"""
import re
import sys

NARR = re.compile(r"^(looks good|works|fine|ok|done|yes|verified|checked)\.?$", re.I)


def verdict(text):
    rows, header = [], None
    for ln in text.splitlines():
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        low = [c.lower() for c in cells]
        if header is None and "criterion" in low and "result" in low:
            header = {n: i for i, n in enumerate(low)}
            continue
        if header is not None and len(cells) >= len(header):
            rows.append(cells)
    if header is None:
        return "FAIL", ["no table with columns criterion | result | evidence"]
    ci, ri, ei = header["criterion"], header["result"], header.get("evidence")
    gaps, fail, hold = [], False, False
    for c in rows:
        res = c[ri].lower().strip("[] `")
        ev = c[ei].strip() if ei is not None and ei < len(c) else ""
        if res == "met":
            if not ev or NARR.match(ev):
                fail = True
                gaps.append("%s: met without real evidence" % c[ci])
        elif res == "untested":
            hold = True
            gaps.append("%s: untested, say what is needed to run it" % c[ci])
        else:
            fail = True
            gaps.append("%s: %s" % (c[ci], res or "no result"))
    if not rows:
        return "FAIL", ["table has no rows"]
    return ("FAIL" if fail else "HOLD" if hold else "PASS"), gaps


def selftest():
    t = "| criterion | result | evidence |\n|---|---|---|\n| loop plays | met | `lune run a.luau` -> PASS 4/4 |\n| shop buys | met | playtest 2026-11-01, no errors in Output |\n"
    assert verdict(t) == ("PASS", [])
    h = t + "| mobile tap | untested | |\n"
    v, g = verdict(h)
    assert v == "HOLD" and "mobile tap" in g[0]
    f = t + "| saves | unmet | data lost on rejoin |\n"
    assert verdict(f)[0] == "FAIL"
    n = t.replace("`lune run a.luau` -> PASS 4/4", "works")
    assert verdict(n)[0] == "FAIL"
    assert verdict("no table")[0] == "FAIL"
    print("selftest ok (5 cases)")
    return 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv:
        print(__doc__)
        return 1
    v, gaps = verdict(open(argv[0], encoding="utf-8").read())
    print("VERDICT:", v)
    for g in gaps:
        print("GAP:", g)
    return 0 if v == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
