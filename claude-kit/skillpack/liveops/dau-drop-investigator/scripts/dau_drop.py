#!/usr/bin/env python3
"""dau_drop.py - measure a drop in daily players against the same weekday last week and classify it (step, slide or one-off), then print the ordered checks. Stdlib only.

  python dau_drop.py --csv dau.csv [--col dau] [--date 2026-11-02]            columns: date,dau
  python dau_drop.py --pull pull.json [--metric DailyActiveUsers] [--date ...]   pull.json = analytics-pull.py --json output
  python dau_drop.py --selftest

Method (vault analytics-metrics.md): compare each day with the same weekday last week (PeriodOverPeriod 7) to remove weekly seasonality; use a 7-day moving average
to see slides; a drop that starts exactly at a publish points to that update; slice by platform/device/source/version/country until the smallest affected segment shows
(a drop on low-memory Android points to resources, not design); a drop in a bot-cleanup window is an accuracy correction, not lost players; before blaming the game for an impression
drop, check your updates, seasonality and platform-wide changes. Classification thresholds (step = single-day fall of 15 percent or more vs last week AND the next 2 days stay below
90 percent of baseline; slide = 7-day average down 8 percent or more with no single step; one-off = the day recovers) are this skill's defaults.
"""
import argparse
import csv
import datetime
import json
import sys


def series_from_csv(path, col):
    with open(path, newline="", encoding="utf-8") as f:
        return {datetime.date.fromisoformat(r["date"]): float(r[col]) for r in csv.DictReader(f)}


def series_from_pull(path, metric):
    js = json.load(open(path, encoding="utf-8"))
    for s in js[metric]:
        if not s.get("breakdowns"):
            return {datetime.date.fromisoformat(p[0]): float(p[1]) for p in s["points"] if p[1] is not None}
    raise SystemExit("no unbroken series for %s in the pull file" % metric)


def wow(s, d):
    p = d - datetime.timedelta(days=7)
    return (100.0 * (s[d] - s[p]) / s[p]) if d in s and p in s and s[p] else None


def ma7(s, d):
    vals = [s[d - datetime.timedelta(days=i)] for i in range(7) if (d - datetime.timedelta(days=i)) in s]
    return sum(vals) / len(vals) if len(vals) == 7 else None


def classify(s, d):
    ch = wow(s, d)
    if ch is None:
        return dict(error="need the day and the same weekday a week earlier")
    nxt = [wow(s, d + datetime.timedelta(days=i)) for i in (1, 2)]
    nxt = [x for x in nxt if x is not None]
    m_now, m_prev = ma7(s, d), ma7(s, d - datetime.timedelta(days=7))
    ma_ch = 100.0 * (m_now - m_prev) / m_prev if m_now and m_prev else None
    if ch <= -15 and nxt and all(x <= -10 for x in nxt):
        kind = "STEP: fell at once and stayed down (look for what changed on that day: publish, config, platform, traffic source)"
    elif ch <= -15 and nxt and all(x > -10 for x in nxt):
        kind = "ONE-OFF: recovered within 2 days (outage, a spike last week, holiday)"
    elif ch <= -15:
        kind = "STEP (recovery not yet visible: only %d day(s) after the drop)" % len(nxt)
    elif ma_ch is not None and ma_ch <= -8:
        kind = "SLIDE: 7-day average down gradually, no single bad day (content staleness, retention, source mix)"
    else:
        kind = "NO CLEAR DROP vs last week (%+.1f%%)" % ch
    return dict(day=s[d], vs_last_week=ch, ma_change=ma_ch, kind=kind)


CHECKS = [
    "1. Dates: did a publish, config change or event end land on or just before the first bad day? (Version history / your changelog)",
    "2. Platform-wide: Roblox status, other games in your genre, bot-removal or accuracy changes (a platform correction is not lost players)",
    "3. Traffic: Acquisition by source and Home Recommendations (play-through rate first); did ads end, a creator video age out, or a thumbnail change?",
    "4. Slice: platform, device tier, country, age, new vs returning, app version; stop at the smallest affected segment",
    "5. Health: crash rate, error count (group by MessageHash), join failures, DataStore/server-start errors for the same hours",
    "6. Retention: did D1 of the new cohorts fall (then it is onboarding) or did returning players stop coming (then content/economy)?",
    "7. Decide: roll back if a publish is the clear cause and the harm is severe (then profile); otherwise one hypothesis, one test",
]


def selftest():
    start = datetime.date(2026, 10, 1)
    base = {start + datetime.timedelta(days=i): 1000.0 for i in range(30)}
    step = dict(base)
    for i in range(20, 30):
        step[start + datetime.timedelta(days=i)] = 700.0
    c = classify(step, start + datetime.timedelta(days=21))
    assert c["kind"].startswith("STEP") and round(c["vs_last_week"]) == -30, c
    one = dict(base)
    one[start + datetime.timedelta(days=21)] = 600.0
    assert classify(one, start + datetime.timedelta(days=21))["kind"].startswith("ONE-OFF")
    slide = {start + datetime.timedelta(days=i): 1000.0 - 15 * max(i - 8, 0) for i in range(30)}
    assert classify(slide, start + datetime.timedelta(days=28))["kind"].startswith("SLIDE"), classify(slide, start + datetime.timedelta(days=28))
    assert classify(base, start + datetime.timedelta(days=21))["kind"].startswith("NO CLEAR")
    assert "error" in classify({start: 1.0}, start)
    print("selftest ok (5 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--col", default="dau")
    ap.add_argument("--pull")
    ap.add_argument("--metric", default="DailyActiveUsers")
    ap.add_argument("--date")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if a.csv:
        s = series_from_csv(a.csv, a.col)
    elif a.pull:
        s = series_from_pull(a.pull, a.metric)
    else:
        ap.error("--csv or --pull required")
    d = datetime.date.fromisoformat(a.date) if a.date else max(s)
    c = classify(s, d)
    if "error" in c:
        print("ERROR:", c["error"])
        return 1
    print("%s: %g vs same weekday last week %+.1f%%; 7-day average change %s" % (d, c["day"], c["vs_last_week"], "%+.1f%%" % c["ma_change"] if c["ma_change"] is not None else "n/a"))
    print("Pattern:", c["kind"])
    print("\n".join(CHECKS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
