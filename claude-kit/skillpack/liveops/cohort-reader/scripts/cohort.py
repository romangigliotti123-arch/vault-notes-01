#!/usr/bin/env python3
"""cohort.py - compare retention of two groups of first-play-date cohorts (before vs after a change). Stdlib only.

  python cohort.py --csv cohorts.csv --change 2026-10-20 [--window d1|d7] [--as-of 2026-11-01]
        columns: first_play_date,new_users,d1_returned,d7_returned   (counts, from Creator Hub retention or your own logs; leave blank if unknown)
  python cohort.py --selftest

Vault (analytics-metrics.md): retention charts use FIRST PLAY DATE on the x-axis, so a change shows in that day's new cohort; D7 and D30 are empty for
recent dates. This script drops immature cohorts (D1 needs 1 day, D7 needs 7 days since first play), pools cohorts before and after --change, and
reports the rate difference with a two-proportion z test (normal approximation, two sided). Skip the change day itself. Pooling cohorts is
an approximation: it ignores day-of-week and traffic-source mix, so check those separately (slice by source/platform before believing a lift).
"""
import argparse
import csv
import datetime
import math
import sys


def ztest(x1, n1, x2, n2):
    p1, p2 = x1 / n1, x2 / n2
    p = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se if se else 0.0
    pv = math.erfc(abs(z) / math.sqrt(2))
    se_d = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    return p1, p2, z, pv, (p2 - p1 - 1.96 * se_d, p2 - p1 + 1.96 * se_d)


def compare(rows, change, window, as_of):
    need = 1 if window == "d1" else 7
    col = "%s_returned" % window
    before, after, dropped = [0, 0], [0, 0], 0
    for r in rows:
        d = datetime.date.fromisoformat(r["first_play_date"])
        if r.get(col, "") in ("", None) or (as_of - d).days < need or d == change:
            dropped += 1
            continue
        tgt = before if d < change else after
        tgt[0] += int(r["new_users"])
        tgt[1] += int(r[col])
    if min(before[0], after[0]) < 200:
        return dict(error="fewer than 200 users in a group (before %d, after %d): too small to read" % (before[0], after[0]), dropped=dropped)
    p1, p2, z, pv, ci = ztest(before[1], before[0], after[1], after[0])
    return dict(before_n=before[0], after_n=after[0], before=p1 * 100, after=p2 * 100, diff_pts=(p2 - p1) * 100, z=z, p=pv, ci_pts=(ci[0] * 100, ci[1] * 100), dropped=dropped)


def selftest():
    import random
    random.seed(1)
    rows = []
    for i in range(1, 29):
        d = datetime.date(2026, 10, 1) + datetime.timedelta(days=i - 1)
        n = 400
        rate = 0.10 if d < datetime.date(2026, 10, 15) else 0.14
        rows.append(dict(first_play_date=d.isoformat(), new_users=str(n), d1_returned=str(int(n * rate)), d7_returned=str(int(n * rate / 4))))
    r = compare(rows, datetime.date(2026, 10, 15), "d1", datetime.date(2026, 11, 5))
    assert r["after"] > r["before"] and r["p"] < 0.01 and r["ci_pts"][0] > 0, r
    r7 = compare(rows, datetime.date(2026, 10, 15), "d7", datetime.date(2026, 10, 25))
    assert "error" in r7 or r7["dropped"] > 0  # recent cohorts dropped as immature
    flat = [dict(r, d1_returned="40") for r in rows]
    rf = compare(flat, datetime.date(2026, 10, 15), "d1", datetime.date(2026, 11, 5))
    assert rf["p"] > 0.5 and abs(rf["diff_pts"]) < 0.01, rf
    assert "error" in compare(rows[:2], datetime.date(2026, 10, 2), "d1", datetime.date(2026, 11, 5))
    print("selftest ok (4 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--change")
    ap.add_argument("--window", default="d1", choices=["d1", "d7"])
    ap.add_argument("--as-of", default=datetime.date.today().isoformat())
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not (a.csv and a.change):
        ap.error("--csv and --change required")
    with open(a.csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    r = compare(rows, datetime.date.fromisoformat(a.change), a.window, datetime.date.fromisoformat(a.as_of))
    if "error" in r:
        print("CANNOT READ:", r["error"], "(immature/blank/change-day cohorts skipped: %d)" % r["dropped"])
        return 1
    print("%s retention: before %.2f%% (n=%d)  after %.2f%% (n=%d)  diff %+.2f pts  95%% CI [%+.2f, %+.2f]  z=%.2f  p=%.4f  (skipped cohorts: %d)" % (
        a.window.upper(), r["before"], r["before_n"], r["after"], r["after_n"], r["diff_pts"], r["ci_pts"][0], r["ci_pts"][1], r["z"], r["p"], r["dropped"]))
    print("Reading: an observed before/after gap is not proof of cause; check traffic source mix, day-of-week and other releases in the window.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
