#!/usr/bin/env python3
"""funnel.py - find where a shop funnel leaks. Stdlib only.

  python funnel.py --steps sessions=10000,shop_opened=1800,item_viewed=1200,prompt_shown=300,purchased=40
  python funnel.py --selftest

Steps are ordered, first to last, as event COUNTS (unique players per step is best). Output: conversion from the previous step, from the first
step, the biggest relative drop, and a plain-words reading. The only benchmark in the vault is one creator's reported payer conversion of
0.82% (Hack A Business, self-reported, analytics-metrics / monetisation-other.md): a reference point, not a target; compare against similar games
in the creator dashboard. The tool names the leak; the fix (shop placement, item order, starter pack, price) is the skill's judgement.
Exit 1 when counts are not non-increasing (a data or logging bug).
"""
import argparse
import sys


def parse_steps(text):
    steps = []
    for part in text.split(","):
        if not part.strip():
            continue
        name, _, val = part.partition("=")
        steps.append((name.strip(), int(val)))
    if len(steps) < 2:
        raise ValueError("need at least two steps")
    return steps


def analyse(steps):
    out = []
    first = steps[0][1]
    for i, (name, n) in enumerate(steps):
        prev = steps[i - 1][1] if i else n
        out.append({
            "step": name,
            "count": n,
            "from_prev": round(n / prev, 4) if prev else 0,
            "from_first": round(n / first, 4) if first else 0,
        })
    problems = [steps[i][0] for i in range(1, len(steps)) if steps[i][1] > steps[i - 1][1]]
    worst = None
    if not problems:
        drops = [(1 - r["from_prev"], r["step"]) for r in out[1:]]
        worst = max(drops)[1] if drops else None
    return {"rows": out, "overall": out[-1]["from_first"], "worst_step": worst, "non_monotonic": problems}


def selftest():
    r = analyse(parse_steps("a=1000,b=500,c=100,d=10"))
    assert r["overall"] == 0.01 and r["worst_step"] == "d" and not r["non_monotonic"], r
    assert r["rows"][1]["from_prev"] == 0.5
    r = analyse(parse_steps("a=100,b=200"))
    assert r["non_monotonic"] == ["b"] and r["worst_step"] is None
    r = analyse(parse_steps("a=0,b=0"))
    assert r["overall"] == 0
    try:
        parse_steps("a=1")
        raise AssertionError("single step accepted")
    except ValueError:
        pass
    print("funnel selftest: 4 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--steps")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.steps:
        ap.error("--steps required")
    r = analyse(parse_steps(a.steps))
    print("%-16s %8s %10s %10s" % ("step", "count", "from prev", "from first"))
    for row in r["rows"]:
        print("%-16s %8d %9.1f%% %9.2f%%" % (row["step"], row["count"], row["from_prev"] * 100, row["from_first"] * 100))
    if r["non_monotonic"]:
        print("DATA PROBLEM: counts rise at %s; fix event logging before reading the funnel." % ", ".join(r["non_monotonic"]))
        return 1
    print("overall %.2f%%; biggest relative drop at: %s" % (r["overall"] * 100, r["worst_step"]))
    print("reference only: 0.82% payer conversion reported by one creator (self-reported).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
