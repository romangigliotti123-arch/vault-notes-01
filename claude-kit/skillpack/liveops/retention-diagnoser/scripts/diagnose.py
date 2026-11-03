#!/usr/bin/env python3
"""diagnose.py - compare a game's headline numbers with the vault's sourced benchmarks and name the likely cause and first test. Stdlib only.

  python diagnose.py [--d1 12] [--d7 2.5] [--ptr 2.5] [--conv 1.5] [--session-min 10] [--first-session-drop 40] [--json]
  python diagnose.py --selftest

The "healthy floor" for D1 (10), D7 (2) and PTR (2) is the lower edge of the sourced target range; the floors for payer conversion (1.0) and session length (8 min) are CHOSEN by this skill below the single sourced sample values and are not sourced rules.
All inputs are percentages (or minutes) from the Creator Hub analytics page for the SAME date range. Thresholds are the lower edge of the
"healthy" band in Roblox/roblox-kb/_tools/BENCHMARKS.md; each carries its source flag. They are rules of thumb from creators and Roblox
talks, not guarantees, and vary by genre: use the Creator Hub "similar experiences" benchmark when you have access (it overrides these).
"""
import argparse
import json
import sys

# metric -> (healthy_floor, strong, source label, what low means, first test)
RULES = {
    "d1": (10.0, 15.0, "D1: 10-15% target, 12-15% very good (indie 2026-08); official 2023 same-genre percentiles 12.4-24.1% (devforum)",
           "onboarding: players do not reach fun fast enough or do not know why to return", "replay the first 5 minutes with a timer, find the drop-off in the first-session funnel, fix the single biggest stall; add a reason to return tomorrow (daily reward, unfinished goal)"),
    "d7": (2.0, 3.0, "D7: 2-3% (indie 2026-08)",
           "mid-game: the first session works but there is no hook across days", "add one return hook (streak, timed reward, social/friend loop, event) and test it with an experiment"),
    "ptr": (2.0, 3.0, "play-through rate 2-3% very good, 4% amazing (indie 2026-07)",
            "packaging or first impression: people click but do not stay or never click", "A/B the thumbnail/icon (3+ variants), check the first 30 seconds, make title and thumbnail match the gameplay"),
    "conv": (1.0, 2.0, "payer conversion 1.63% in an official sample (2024-09); 2-3% good (indie 2026-08); floor 1.0 chosen by this skill",
             "offers: players do not see a reason or a moment to buy", "add a cheap first purchase at a natural need moment (see money skills), many shop entry points, then measure first-purchase rate"),
    "session": (8.0, 12.0, "average session ~10 min in an official sample (2024-09); floor 8 chosen by this skill",
                "pacing: sessions end early", "find the stop points (where sessions end), add a goal 2-3 minutes ahead at each"),
}


def verdict(value, floor, strong):
    return "strong" if value >= strong else "ok" if value >= floor else "LOW"


def diagnose(m):
    rows = []
    for key, (floor, strong, src, cause, test) in RULES.items():
        if m.get(key) is None:
            continue
        v = verdict(m[key], floor, strong)
        rows.append(dict(metric=key, value=m[key], status=v, source=src, likely_cause=cause if v == "LOW" else "", first_test=test if v == "LOW" else ""))
    fsd = m.get("first_session_drop")
    if fsd is not None and fsd >= 40:
        rows.append(dict(metric="first_session_drop", value=fsd, status="LOW", source="no sourced number; vault rule: 'free players not hooked in ~5 min are exponentially unlikely to return'",
                         likely_cause="players leave inside the first session", first_test="use the New User First Session Retention curve, shorten the path to the first reward"))
    low = [r for r in rows if r["status"] == "LOW"]
    order = ["d1", "ptr", "first_session_drop", "d7", "conv", "session"]
    low.sort(key=lambda r: order.index(r["metric"]) if r["metric"] in order else 9)
    return rows, low


def selftest():
    rows, low = diagnose({"d1": 8, "d7": 2.5, "ptr": 3.5, "conv": 0.5})
    assert [r["metric"] for r in low] == ["d1", "conv"], low
    assert [r["status"] for r in rows] == ["LOW", "ok", "strong", "LOW"]
    rows, low = diagnose({"d1": 20, "d7": 4})
    assert low == []
    print("selftest ok")
    return 0


def main():
    ap = argparse.ArgumentParser()
    for k in ("d1", "d7", "ptr", "conv", "session-min", "first-session-drop"):
        ap.add_argument("--" + k, type=float)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    m = dict(d1=a.d1, d7=a.d7, ptr=a.ptr, conv=a.conv, session=a.session_min, first_session_drop=a.first_session_drop)
    if all(v is None for v in m.values()):
        ap.error("give at least one metric (--d1 --d7 --ptr --conv --session-min --first-session-drop)")
    rows, low = diagnose(m)
    if a.json:
        print(json.dumps(dict(rows=rows, fix_first=[r["metric"] for r in low])))
        return 0
    for r in rows:
        print("%-18s %6.2f  %-6s %s" % (r["metric"], r["value"], r["status"], r["source"]))
    if low:
        print("\nFix first (in this order, one change at a time):")
        for i, r in enumerate(low, 1):
            print("%d. %s: %s -> %s" % (i, r["metric"], r["likely_cause"], r["first_test"]))
    else:
        print("\nNo metric below its healthy floor. Compare with the Creator Hub similar-experience benchmark before concluding the game is healthy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
