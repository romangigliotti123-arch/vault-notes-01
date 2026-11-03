#!/usr/bin/env python3
"""privserver.py - project 12 months of private-server subscription income from a price, a creator share and churn. Stdlib only.

  python privserver.py --price 200 --share 0.7 --new-per-month 40 --churn 0.25 [--months 12]
  python privserver.py --selftest

--share is the fraction of the Robux price that reaches you. It is NOT in the vault as a fixed number for private servers, so it is required:
read it in Creator Hub / the Creator Docs the same day and pass it in. Also from the vault (monetisation-other.md "Paid access and private servers rules",
business-and-payouts.md): private servers need a public game, are a monthly Robux fee, cannot coexist with paid access, and split percentages for group games
are locked when a subscription is bought. The projection assumes a constant number of NEW subscribers each month and a constant monthly churn; real
curves differ, so treat it as a sanity check for "is this worth the support work", not a forecast.
"""
import argparse
import sys


def project(price, share, new_per_month, churn, months=12):
    if not (0 < share <= 1):
        raise ValueError("share must be in (0, 1]")
    if not (0 <= churn < 1):
        raise ValueError("churn must be in [0, 1)")
    if price < 1 or new_per_month < 0 or months < 1:
        raise ValueError("price >= 1, new-per-month >= 0, months >= 1")
    subs = 0.0
    rows = []
    total = 0.0
    for m in range(1, months + 1):
        subs = subs * (1 - churn) + new_per_month
        income = subs * price * share
        total += income
        rows.append({"month": m, "active": round(subs, 1), "robux": round(income)})
    steady = new_per_month / churn if churn else None
    return {"rows": rows, "total_robux": round(total), "steady_state_subs": round(steady, 1) if steady else None}


def selftest():
    r = project(200, 0.7, 10, 0.5, 3)
    assert [x["active"] for x in r["rows"]] == [10.0, 15.0, 17.5], r
    assert r["rows"][0]["robux"] == 1400 and r["total_robux"] == round((10 + 15 + 17.5) * 140), r
    assert r["steady_state_subs"] == 20.0
    assert project(100, 1.0, 5, 0, 2)["steady_state_subs"] is None
    for bad in ((100, 0, 1, 0.1), (100, 0.7, 1, 1.0), (0, 0.7, 1, 0.1)):
        try:
            project(*bad)
            raise AssertionError("bad input accepted: %r" % (bad,))
        except ValueError:
            pass
    print("privserver selftest: 5 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--price", type=int)
    ap.add_argument("--share", type=float)
    ap.add_argument("--new-per-month", type=float)
    ap.add_argument("--churn", type=float)
    ap.add_argument("--months", type=int, default=12)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    for k in ("price", "share", "new_per_month", "churn"):
        if getattr(a, k) is None:
            ap.error("--%s is required" % k.replace("_", "-"))
    r = project(a.price, a.share, a.new_per_month, a.churn, a.months)
    print("%-6s %8s %10s" % ("month", "active", "Robux"))
    for x in r["rows"]:
        print("%-6d %8.1f %10d" % (x["month"], x["active"], x["robux"]))
    print("total %d Robux over %d months; steady state about %s subscribers" % (r["total_robux"], a.months, r["steady_state_subs"]))
    print("LIVE-CHECK the private-server share and rules; this is a constant-rate model.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
