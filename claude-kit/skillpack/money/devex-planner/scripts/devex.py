#!/usr/bin/env python3
"""devex.py - estimate a Developer Exchange (DevEx) cash-out and check the eligibility floor. Stdlib only.

  python devex.py --standard 40000 [--plus18 5000] [--legacy 0] [--json]
  python devex.py --selftest

Earned Robux are split by rate class (the vault, business-and-payouts.md, 2026-10 sources):
  --legacy    balance earned before the Sept 2025 rate change, cashed out FIRST (default rate 0.0035 USD per Robux)
  --plus18    Robux from purchases by eligible verified 18+ US players (default rate 0.0054, launched June 2026)
  --standard  everything else (default rate 0.0038)
The rates are INPUTS with the vault's values as defaults. They change: override with --legacy-rate/--plus18-rate/--standard-rate
after checking the DevEx page the same day. The tool prints that warning every run. It estimates the gross payout only:
it does not model payout-method fees, FX, taxes or the review wait (ask the user to read those on the DevEx portal).
Eligibility floor checked: at least 30,000 Earned Robux in total (vault; live-check). One request per calendar month.
Exit 1 when below the floor.
"""
import argparse
import json
import sys

MIN_EARNED = 30000
DEFAULT_RATES = {"legacy": 0.0035, "plus18": 0.0054, "standard": 0.0038}


def estimate(legacy, plus18, standard, rates=None):
    rates = dict(DEFAULT_RATES, **(rates or {}))
    for name, v in (("legacy", legacy), ("plus18", plus18), ("standard", standard)):
        if v < 0 or v != int(v):
            raise ValueError("%s must be a whole number >= 0" % name)
    total = legacy + plus18 + standard
    parts = {
        "legacy": legacy * rates["legacy"],
        "plus18": plus18 * rates["plus18"],
        "standard": standard * rates["standard"],
    }
    usd = sum(parts.values())
    return {
        "earned_total": total,
        "eligible": total >= MIN_EARNED,
        "shortfall": max(0, MIN_EARNED - total),
        "usd_by_class": {k: round(v, 2) for k, v in parts.items()},
        "usd_gross": round(usd, 2),
        "rates": rates,
        "blended_rate": round(usd / total, 6) if total else 0,
    }


def selftest():
    r = estimate(0, 0, 40000)
    assert r["eligible"] and r["usd_gross"] == 152.0, r
    r = estimate(10000, 5000, 20000)
    assert r["earned_total"] == 35000 and r["usd_gross"] == round(35 + 27 + 76, 2), r
    r = estimate(0, 0, 29999)
    assert not r["eligible"] and r["shortfall"] == 1, r
    r = estimate(0, 0, 30000, {"standard": 0.01})
    assert r["usd_gross"] == 300.0
    try:
        estimate(-1, 0, 0)
        raise AssertionError("negative accepted")
    except ValueError:
        pass
    print("devex selftest: 4 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--legacy", type=int, default=0)
    ap.add_argument("--plus18", type=int, default=0)
    ap.add_argument("--standard", type=int, default=0)
    ap.add_argument("--legacy-rate", type=float)
    ap.add_argument("--plus18-rate", type=float)
    ap.add_argument("--standard-rate", type=float)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    rates = {k: v for k, v in (("legacy", a.legacy_rate), ("plus18", a.plus18_rate), ("standard", a.standard_rate)) if v is not None}
    r = estimate(a.legacy, a.plus18, a.standard, rates)
    if a.json:
        print(json.dumps(r, indent=2))
    else:
        print("Earned Robux: %d (floor %d: %s)" % (r["earned_total"], MIN_EARNED, "eligible" if r["eligible"] else "SHORT by %d" % r["shortfall"]))
        for k in ("legacy", "plus18", "standard"):
            print("  %-8s rate %.4f  -> USD %.2f" % (k, r["rates"][k], r["usd_by_class"][k]))
        print("Gross estimate: USD %.2f (blended %.4f per Robux)" % (r["usd_gross"], r["blended_rate"]))
        print("LIVE-CHECK: rates, the 30,000 floor and fees change; confirm on the DevEx page. Not modelled: payout fees, FX, taxes, the roughly 5-10 business day review.")
    return 0 if r["eligible"] else 1


if __name__ == "__main__":
    sys.exit(main())
