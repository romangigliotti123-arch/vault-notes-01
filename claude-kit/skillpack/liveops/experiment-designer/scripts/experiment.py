#!/usr/bin/env python3
"""experiment.py - size and sanity-check a Creator Hub experiment plan before you start it. Stdlib only.

  python experiment.py --metric d1 --baseline 12 --mde-rel 25 --daily-new 400 [--exposure 50] [--treatments 1] [--days 14]
  python experiment.py --selftest

--baseline is the current rate in percent (a proportion metric such as D1 or payer conversion). --mde-rel is the smallest RELATIVE lift worth detecting in percent.
Output: players needed per arm (two-sided alpha 0.05, power 0.80, normal approximation), the days that takes with your traffic, and checks against the
platform limits in Roblox/roblox-kb/ab-testing-and-experiments.md (all Roblox Creator Docs 2026-10, live-check before relying): duration 14-60 days, 1
baseline + up to 2 treatments, harm decisions need at least 10,000 enrolled players across variant and control, first-24-hour early-harm check is a stop signal only.
The sample-size formula is textbook; it is a planning aid, not what Creator Hub computes. For mean metrics (playtime, ARPU) it cannot size: supply a
standard deviation from your own data and use the two-sample formula by hand, or rely on the Creator Hub MDE display.
"""
import argparse
import math
import sys

ZA, ZB = 1.959964, 0.841621  # alpha .05 two-sided, power .80


def n_per_arm(p1, p2):
    pbar = (p1 + p2) / 2
    num = (ZA * math.sqrt(2 * pbar * (1 - pbar)) + ZB * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2)


def plan(baseline_pct, mde_rel_pct, daily_new, exposure_pct=50.0, treatments=1, days=None):
    p1 = baseline_pct / 100.0
    p2 = p1 * (1 + mde_rel_pct / 100.0)
    out = dict(notes=[], errors=[])
    if not 0 < p1 < 1 or p2 >= 1 or mde_rel_pct <= 0:
        out["errors"].append("baseline/mde out of range")
        return out
    n = n_per_arm(p1, p2)
    arms = 1 + treatments
    per_day_enrolled = daily_new * exposure_pct / 100.0
    per_arm_day = per_day_enrolled / arms
    need_days = math.ceil(n / per_arm_day) if per_arm_day else 10 ** 6
    chosen = days if days is not None else max(14, need_days)
    enrolled = per_day_enrolled * chosen
    out.update(n_per_arm=n, arms=arms, need_days=need_days, chosen_days=chosen, enrolled=round(enrolled), p1=p1, p2=p2)
    if treatments > 2 or treatments < 1:
        out["errors"].append("an in-experience experiment allows 1 baseline plus up to 2 treatments")
    if chosen < 14 or chosen > 60:
        out["errors"].append("duration must be 14-60 days (plan needs %d)" % need_days if need_days > 60 else "duration must be 14-60 days")
    if enrolled < 10000:
        out["notes"].append("expected enrollment %d is under 10,000: lift is shown but no harm decisions are made; raise exposure or run longer" % round(enrolled))
    if need_days > chosen:
        out["notes"].append("underpowered: %d days needed for %d per arm, you plan %d. Raise MDE (bolder variant), exposure, or accept a weaker read" % (need_days, n, chosen))
    if mde_rel_pct < 10:
        out["notes"].append("MDE under 10 percent relative is rarely detectable at Roblox traffic; vault (indie): make variants bold, 50-100 percent value changes")
    if exposure_pct > 50 and treatments >= 1:
        out["notes"].append("exposure above 50 percent leaves little control traffic if the variant is risky: vault says contain risky tests to a small slice")
    return out


def selftest():
    assert n_per_arm(0.10, 0.125) in range(2500, 2800), n_per_arm(0.10, 0.125)  # known ~2.5-2.7k per arm
    p = plan(10, 25, 400, 50, 1)
    assert p["need_days"] == math.ceil(p["n_per_arm"] / 100.0), p
    assert not p["errors"]
    assert plan(10, 25, 400, 50, 3)["errors"]
    assert plan(10, 25, 50, 20, 1, days=70)["errors"]
    q = plan(10, 5, 100, 10, 1, days=14)
    assert any("underpowered" in n for n in q["notes"]) and any("10,000" in n for n in q["notes"])
    assert plan(0, 25, 100)["errors"]
    print("selftest ok (6 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metric", default="d1")
    ap.add_argument("--baseline", type=float)
    ap.add_argument("--mde-rel", type=float, default=25)
    ap.add_argument("--daily-new", type=float)
    ap.add_argument("--exposure", type=float, default=50)
    ap.add_argument("--treatments", type=int, default=1)
    ap.add_argument("--days", type=int)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if a.baseline is None or a.daily_new is None:
        ap.error("--baseline and --daily-new required")
    p = plan(a.baseline, a.mde_rel, a.daily_new, a.exposure, a.treatments, a.days)
    if "n_per_arm" in p:
        print("metric %s: %.2f%% -> %.2f%% (%+g%% relative). Need %d players per arm x %d arms. With %g new players/day at %g%% exposure: %d days needed; plan %d days; expected enrolled %d." % (
            a.metric, p["p1"] * 100, p["p2"] * 100, a.mde_rel, p["n_per_arm"], p["arms"], a.daily_new, a.exposure, p["need_days"], p["chosen_days"], p["enrolled"]))
    for e in p["errors"]:
        print("ERROR:", e)
    for n in p["notes"]:
        print("NOTE:", n)
    return 1 if p["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
