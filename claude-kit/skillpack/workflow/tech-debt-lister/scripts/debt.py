#!/usr/bin/env python3
"""debt.py - rank technical debt by pain per hour of fixing. Stdlib only.

  python debt.py debt.csv [--budget-h 6]
  python debt.py --selftest

CSV columns: item,impact,risk,fix_h,blocks   (impact 1-5: how often it slows or breaks work; risk 1-5: chance and cost of a
player-visible or data-loss failure; fix_h: hours to fix including a test; blocks: id or text of the milestone it blocks, may be empty)
score = (impact + 2*risk) / fix_h; an item that blocks a milestone gets x2. Sorted high to low. Verdicts: NOW (score >= 2 with impact+risk >= 5, or
risk 5), NEXT (>= 1), LATER (>= 0.4), ACCEPT (below: record it and stop thinking about it). --budget-h marks how many NOW/NEXT
items fit in the hours you will spend on debt this sprint (rule of thumb in the vault: ship the MVP first, do not over-engineer
one-time content). Exit 0, or 1 on bad input.
"""
import argparse
import csv
import io
import sys


def rank(rows, budget=None):
    out = []
    for r in rows:
        try:
            imp, risk, fix = int(r["impact"]), int(r["risk"]), float(r["fix_h"])
        except (KeyError, ValueError):
            raise ValueError("bad row %r (need item,impact,risk,fix_h)" % (r,))
        if not (1 <= imp <= 5 and 1 <= risk <= 5) or fix <= 0:
            raise ValueError("impact/risk must be 1-5 and fix_h > 0: %r" % (r,))
        score = (imp + 2 * risk) / fix * (2 if (r.get("blocks") or "").strip() else 1)
        verdict = "NOW" if ((score >= 2 and imp + risk >= 5) or risk == 5) else "NEXT" if score >= 1 else "LATER" if score >= 0.4 else "ACCEPT"
        out.append(dict(item=r["item"], score=round(score, 2), verdict=verdict, fix=fix))
    out.sort(key=lambda x: -x["score"])
    left = budget
    for o in out:
        o["fits"] = ""
        if left is not None and o["verdict"] in ("NOW", "NEXT"):
            if o["fix"] <= left:
                o["fits"] = "in budget"
                left -= o["fix"]
            else:
                o["fits"] = "over budget"
    return out


def selftest():
    csvt = "item,impact,risk,fix_h,blocks\nduplicate remote names,3,2,1,\nno data migration,2,5,4,M2\nmagic numbers,2,1,6,\nold unused module,1,1,1,\n"
    r = rank(list(csv.DictReader(io.StringIO(csvt))), budget=5)
    byname = {x["item"]: x for x in r}
    assert r[0]["item"] == "duplicate remote names" and r[0]["score"] == 7.0 and r[0]["verdict"] == "NOW", r
    assert byname["no data migration"]["verdict"] == "NOW" and byname["no data migration"]["score"] == 6.0
    assert byname["no data migration"]["fits"] == "in budget"
    assert byname["old unused module"]["verdict"] == "NEXT" and byname["old unused module"]["fits"] == "over budget"
    assert byname["magic numbers"]["verdict"] == "LATER"
    try:
        rank([{"item": "x", "impact": "9", "risk": "1", "fix_h": "1"}])
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("selftest ok (5 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--budget-h", type=float)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    with open(a.file, encoding="utf-8", newline="") as f:
        try:
            rows = rank(list(csv.DictReader(f)), a.budget_h)
        except ValueError as e:
            print("ERROR:", e)
            return 1
    for o in rows:
        print("%-7s %5.2f  %4.1f h  %-40s %s" % (o["verdict"], o["score"], o["fix"], o["item"][:40], o["fits"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
