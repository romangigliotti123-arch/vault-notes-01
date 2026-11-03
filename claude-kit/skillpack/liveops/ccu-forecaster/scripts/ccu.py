#!/usr/bin/env python3
"""ccu.py - forecast concurrent players around an event or update from your own history, with a post-spike decay and server need. Stdlib only.

  python ccu.py --history ccu.csv --event 2026-11-13 [--uplift 1.6 --uplift-low 1.25 --uplift-high 2.5] [--decay-days 7] [--post-baseline 1.05] [--players-per-server 30]
        history.csv columns: date,peak_ccu    (at least 28 days, daily peak or daily mean: be consistent)
  python ccu.py --selftest

Baseline for the event day = mean of the same weekday over the last 4 weeks (removes weekday seasonality, vault: compare each day with the same weekday last week).
Uplift multipliers are YOUR assumptions: take them from your own past events (peak on event day / same-weekday baseline). The vault has only reported
extremes (a +75.5% average-CCU lift for one official event, 500%+ for another, both presenter-reported) - do not use those as a forecast. Vault also: spikes
fade, so judge the baseline a week later (--post-baseline is the multiple of the old baseline you expect to settle at). Servers needed = ceil(peak / players-per-server);
players-per-server is your MaxPlayers choice.
"""
import argparse
import csv
import datetime
import math
import sys


def weekday_baseline(hist, day, weeks=4):
    vals = []
    for k in range(1, weeks + 1):
        d = day - datetime.timedelta(days=7 * k)
        if d in hist:
            vals.append(hist[d])
    return (sum(vals) / len(vals), len(vals)) if vals else (None, 0)


def forecast(hist, event, uplift=1.5, low=1.2, high=2.5, decay_days=7, post=1.05, pps=30):
    base, n = weekday_baseline(hist, event)
    if base is None or n < 3:
        return dict(error="need at least 3 same-weekday observations before the event (have %d); supply 4 weeks of history" % n)
    out = dict(base=base, n=n, scenarios={}, decay=[])
    for name, m in (("low", low), ("base", uplift), ("high", high)):
        peak = base * m
        out["scenarios"][name] = dict(multiplier=m, peak=peak, servers=math.ceil(peak / pps))
    for d in range(decay_days + 1):
        day = event + datetime.timedelta(days=d)
        wd, _ = weekday_baseline(hist, day)
        b = wd if wd is not None else base
        f = post + (uplift - post) * math.exp(-d / max(decay_days / 3.0, 0.5))  # decays toward the post-event baseline
        out["decay"].append((day.isoformat(), b * f))
    out["settle_check_date"] = (event + datetime.timedelta(days=7)).isoformat()
    return out


def selftest():
    hist = {}
    start = datetime.date(2026, 10, 1)
    for i in range(40):
        d = start + datetime.timedelta(days=i)
        hist[d] = 1000 + (200 if d.weekday() >= 5 else 0)
    ev = datetime.date(2026, 11, 7)  # a Saturday
    f = forecast(hist, ev, uplift=2.0, low=1.5, high=3.0, pps=30)
    assert round(f["base"]) == 1200 and f["scenarios"]["base"]["peak"] == 2400
    assert f["scenarios"]["base"]["servers"] == 80 and f["scenarios"]["high"]["servers"] == 120
    assert f["decay"][0][1] > f["decay"][-1][1] > 0
    assert "error" in forecast({start: 1}, ev)
    print("selftest ok (4 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--history")
    ap.add_argument("--event")
    ap.add_argument("--uplift", type=float, default=1.5)
    ap.add_argument("--uplift-low", type=float, default=1.2)
    ap.add_argument("--uplift-high", type=float, default=2.5)
    ap.add_argument("--decay-days", type=int, default=7)
    ap.add_argument("--post-baseline", type=float, default=1.05)
    ap.add_argument("--players-per-server", type=int, default=30)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not (a.history and a.event):
        ap.error("--history and --event required")
    with open(a.history, newline="", encoding="utf-8") as f:
        hist = {datetime.date.fromisoformat(r["date"]): float(r["peak_ccu"]) for r in csv.DictReader(f)}
    r = forecast(hist, datetime.date.fromisoformat(a.event), a.uplift, a.uplift_low, a.uplift_high, a.decay_days, a.post_baseline, a.players_per_server)
    if "error" in r:
        print("ERROR:", r["error"])
        return 1
    print("same-weekday baseline %.0f (from %d weeks)" % (r["base"], r["n"]))
    for k, s in r["scenarios"].items():
        print("  %-5s x%.2f -> peak %.0f -> %d servers of %d" % (k, s["multiplier"], s["peak"], s["servers"], a.players_per_server))
    print("expected decay (base scenario): " + ", ".join("%s %.0f" % x for x in r["decay"]))
    print("judge the result against the baseline on %s, not against the spike." % r["settle_check_date"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
