#!/usr/bin/env python3
"""ladder.py - build a Robux price ladder from an entry price. Stdlib only.

  python ladder.py --entry 49 [--tiers 6] [--rule double100|x2|x2.5] [--cap 10000] [--json]
  python ladder.py --selftest

Rules (both are starting points to TEST, not formulas; the vault says "there is no pricing formula"):
  double100  next = previous * 2 + 100   (one DevForum guide's spacing example, e.g. 450 / 1000 / 2200; indie-labelled)
  x2, x2.5   geometric spacing
Prices are rounded to a friendly step (5 below 100, 10 below 500, 50 below 2000, 100 above). Bands come from
Roblox/roblox-kb/_tools/PRICE-LADDER.md (default ladder, creator-reported = indie flag).
"""
import argparse
import json
import sys

BANDS = [(0, 100, "impulse/entry (~25-100)"), (100, 400, "core (~100-400)"), (400, 2000, "premium (~400-2000+)"), (2000, 6000, "high"), (6000, 10**9, "whale (6000-10000+)")]


def step_for(n):
    return 5 if n < 100 else 10 if n < 500 else 50 if n < 2000 else 100


def snap(n):
    s = step_for(n)
    return max(1, int(round(n / s)) * s)


def band(n):
    for lo, hi, name in BANDS:
        if lo <= n < hi:
            return name
    return "?"


def ladder(entry, tiers, rule, cap):
    out = [snap(entry)]
    while len(out) < tiers:
        p = out[-1]
        nxt = p * 2 + 100 if rule == "double100" else p * (2.5 if rule == "x2.5" else 2)
        nxt = snap(nxt)
        if nxt > cap:
            break
        if nxt <= out[-1]:
            nxt = out[-1] + step_for(out[-1])
        out.append(nxt)
    return out


def selftest():
    assert ladder(49, 4, "double100", 10**6) == [50, 200, 500, 1100], ladder(49, 4, "double100", 10**6)
    assert ladder(100, 3, "x2", 10**6) == [100, 200, 400]
    assert ladder(100, 10, "x2", 500) == [100, 200, 400]
    assert snap(7) == 5 and snap(333) == 330 and snap(1234) == 1250 and snap(3333) == 3300
    assert band(50).startswith("impulse") and band(7000).startswith("whale")
    print("selftest ok")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entry", type=float)
    ap.add_argument("--tiers", type=int, default=6)
    ap.add_argument("--rule", default="double100", choices=["double100", "x2", "x2.5"])
    ap.add_argument("--cap", type=int, default=10000)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.entry or a.entry < 1:
        ap.error("--entry <robux> is required (>= 1)")
    rows = [{"tier": i + 1, "robux": p, "band": band(p)} for i, p in enumerate(ladder(a.entry, a.tiers, a.rule, a.cap))]
    if a.json:
        print(json.dumps(rows))
    else:
        for r in rows:
            print("tier %d: %5d Robux  %s" % (r["tier"], r["robux"], r["band"]))
        print("Starting points only: test live (Price Optimization if eligible), lower if few buy, raise on the next version.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
