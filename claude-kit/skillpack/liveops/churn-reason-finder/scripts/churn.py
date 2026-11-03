#!/usr/bin/env python3
"""churn.py - rank where players leave from per-session records: the last thing they did, and whether they came back. Stdlib only.

  python churn.py --csv sessions.csv [--min-group 30]
        columns: user_id,session_minutes,last_stage,returned_d1[,platform]      returned_d1 = 1/0, last_stage = the funnel step, area or
        activity the player was in when the session ended (from kit Analytics funnel/progression events or your own server log)
  python churn.py --selftest

Per last_stage: sessions that ended there, how many of those players did NOT return the next day, median minutes, and a 'lost players' rank
(the stages that lose the most players, not the highest percentages). Vault (retention-d1-d7.md, analytics-metrics.md): low D1 is onboarding, slice by
platform/device to find the smallest affected segment, pair telemetry with qualitative feedback because telemetry shows how many and not why. Groups
under --min-group sessions are listed as 'too small'. Correlation only: a stage with high churn can be a symptom of who arrives there.
"""
import argparse
import csv
import statistics
import sys
from collections import defaultdict


def rank(rows, min_group=30, split=None):
    g = defaultdict(list)
    for r in rows:
        key = r["last_stage"] if not split else "%s | %s" % (r["last_stage"], r.get(split, "?"))
        g[key].append((float(r["session_minutes"]), int(r["returned_d1"])))
    total_lost = sum(1 for v in g.values() for m, ret in v if not ret)
    out, small = [], []
    for k, v in g.items():
        if len(v) < min_group:
            small.append((k, len(v)))
            continue
        lost = sum(1 for m, ret in v if not ret)
        out.append(dict(stage=k, sessions=len(v), lost=lost, lost_pct=100.0 * lost / len(v), share_of_all_lost=100.0 * lost / total_lost if total_lost else 0.0, median_min=statistics.median(m for m, _ in v)))
    out.sort(key=lambda x: -x["lost"])
    return out, small, total_lost


def selftest():
    rows = []
    for i in range(100):
        rows.append(dict(user_id=i, session_minutes="2", last_stage="tutorial", returned_d1="0" if i < 70 else "1", platform="phone"))
    for i in range(100):
        rows.append(dict(user_id=1000 + i, session_minutes="14", last_stage="boss1", returned_d1="0" if i < 20 else "1", platform="pc"))
    for i in range(10):
        rows.append(dict(user_id=2000 + i, session_minutes="30", last_stage="rare", returned_d1="0"))
    out, small, lost = rank(rows)
    assert out[0]["stage"] == "tutorial" and out[0]["lost"] == 70 and round(out[0]["lost_pct"]) == 70
    assert small == [("rare", 10)] and lost == 100
    assert out[1]["median_min"] == 14
    o2, _, _ = rank(rows, split="platform")
    assert any(x["stage"].endswith("phone") for x in o2)
    print("selftest ok (4 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--min-group", type=int, default=30)
    ap.add_argument("--split", help="extra column to split by, e.g. platform")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not a.csv:
        ap.error("--csv required")
    with open(a.csv, newline="", encoding="utf-8") as f:
        out, small, lost = rank(list(csv.DictReader(f)), a.min_group, a.split)
    print("players not back next day: %d. Stages ranked by players lost:" % lost)
    print("%-28s %8s %6s %7s %8s %8s" % ("stage", "sessions", "lost", "lost%", "of-all%", "med min"))
    for x in out:
        print("%-28s %8d %6d %6.1f%% %7.1f%% %8.1f" % (x["stage"], x["sessions"], x["lost"], x["lost_pct"], x["share_of_all_lost"], x["median_min"]))
    if small:
        print("too small to read (<%d sessions): %s" % (a.min_group, ", ".join("%s(%d)" % s for s in small)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
