#!/usr/bin/env python3
"""econ_drift.py - read a log of currency sources and sinks and say whether the economy is drifting. Stdlib only.

  python econ_drift.py --csv econ.csv [--currency Coins] [--window 7] [--json]
        columns: date,currency,kind,amount[,reason]      kind = source | sink     (one row per day per reason is fine; sum of amounts)
  python econ_drift.py --selftest

Feed it the daily totals of kit Analytics LogEconomyEvent (Flow = Source/Sink) from Creator Hub, or your own server counters. Vault
(analytics-metrics.md, economy rules in money skills): keep sources minus sinks near zero; a constantly growing currency means too few sinks; wallet spikes mean
too few sink options. This script computes per-day net, the sink ratio (sinks / sources), the circulating balance implied by the log (cumulative net from
the first row, so it is a CHANGE, not an absolute wallet), the last-window trend, and the top sources and sinks. Verdict thresholds (sink ratio < 0.6 inflating,
> 1.1 draining, trend slope > 5 percent of daily sources per day = drifting) are this skill's defaults, not sourced numbers; tune them with `economy-balancer` data.
Exclude exploiters and players inactive 15-30 days before logging if you can (vault); the log cannot do it for you.
"""
import argparse
import csv
import json
import sys
from collections import defaultdict


def load(rows, currency=None):
    days = defaultdict(lambda: {"source": 0.0, "sink": 0.0})
    by_reason = {"source": defaultdict(float), "sink": defaultdict(float)}
    for r in rows:
        if currency and r["currency"] != currency:
            continue
        kind = r["kind"].strip().lower()
        if kind not in ("source", "sink"):
            raise ValueError("kind must be source or sink, got %r" % r["kind"])
        a = float(r["amount"])
        days[r["date"]][kind] += a
        by_reason[kind][r.get("reason") or "(none)"] += a
    return days, by_reason


def analyse(days, by_reason, window=7, lo=0.6, hi=1.1):
    dates = sorted(days)
    if len(dates) < 3:
        return dict(error="need at least 3 days of data")
    cum, series = 0.0, []
    for d in dates:
        s, k = days[d]["source"], days[d]["sink"]
        cum += s - k
        series.append(dict(date=d, source=s, sink=k, net=s - k, cum=cum, ratio=(k / s) if s else None))
    tail = series[-window:]
    src = sum(x["source"] for x in tail)
    snk = sum(x["sink"] for x in tail)
    ratio = snk / src if src else None
    # slope of net per day over the tail (least squares), relative to mean daily source
    n = len(tail)
    xs = list(range(n))
    mx, my = sum(xs) / n, sum(x["net"] for x in tail) / n
    den = sum((x - mx) ** 2 for x in xs) or 1.0
    slope = sum((xs[i] - mx) * (tail[i]["net"] - my) for i in range(n)) / den
    rel_slope = slope / (src / n) if src else 0.0
    if ratio is None:
        verdict = "no sources logged"
    elif ratio < lo:
        verdict = "INFLATING: sinks are %.0f%% of sources (default floor %.0f%%)" % (ratio * 100, lo * 100)
    elif ratio > hi:
        verdict = "DRAINING: sinks are %.0f%% of sources (default ceiling %.0f%%)" % (ratio * 100, hi * 100)
    elif rel_slope > 0.05:
        verdict = "DRIFTING UP: ratio ok but net grows each day (%.1f%% of daily sources per day)" % (rel_slope * 100)
    elif rel_slope < -0.05:
        verdict = "DRIFTING DOWN: net shrinks each day (%.1f%% of daily sources per day)" % (rel_slope * 100)
    else:
        verdict = "BALANCED over the last %d days" % n
    top = lambda kind: sorted(by_reason[kind].items(), key=lambda kv: -kv[1])[:3]
    return dict(window_days=n, sources=src, sinks=snk, sink_ratio=ratio, rel_slope=rel_slope, verdict=verdict, top_sources=top("source"), top_sinks=top("sink"), cum_change=cum, series=series)


def selftest():
    def mk(rows):
        return load([dict(date="2026-10-%02d" % d, currency="Coins", kind=k, amount=str(a), reason=r) for d, k, a, r in rows])
    # inflating: sources 1000/day, sinks 300/day
    rows = [(d, "source", 1000, "quest") for d in range(1, 9)] + [(d, "sink", 300, "shop") for d in range(1, 9)]
    a = analyse(*mk(rows))
    assert a["verdict"].startswith("INFLATING") and a["top_sinks"][0][0] == "shop", a["verdict"]
    # balanced
    rows = [(d, "source", 1000, "quest") for d in range(1, 9)] + [(d, "sink", 950, "shop") for d in range(1, 9)]
    assert analyse(*mk(rows))["verdict"].startswith("BALANCED")
    # draining
    rows = [(d, "source", 500, "q") for d in range(1, 9)] + [(d, "sink", 900, "s") for d in range(1, 9)]
    assert analyse(*mk(rows))["verdict"].startswith("DRAINING")
    # ratio ok but sink demand fading: net grows daily
    rows = [(d, "source", 1000, "q") for d in range(1, 9)] + [(d, "sink", 1000 - 60 * d, "s") for d in range(1, 9)]
    assert analyse(*mk(rows))["verdict"].startswith("DRIFTING UP") or analyse(*mk(rows))["verdict"].startswith("INFLATING")
    assert "error" in analyse(*mk([(1, "source", 1, "q")]))
    try:
        mk([(1, "gift", 1, "q")])
        raise SystemExit("bad kind not rejected")
    except ValueError:
        pass
    print("selftest ok (6 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--currency")
    ap.add_argument("--window", type=int, default=7)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not a.csv:
        ap.error("--csv required")
    with open(a.csv, newline="", encoding="utf-8") as f:
        days, br = load(csv.DictReader(f), a.currency)
    r = analyse(days, br, a.window)
    if "error" in r:
        print("ERROR:", r["error"])
        return 1
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    print("%s | last %d days: sources %.0f, sinks %.0f, sink ratio %s, cumulative change since first row %+.0f" % (r["verdict"], r["window_days"], r["sources"], r["sinks"], "%.2f" % r["sink_ratio"] if r["sink_ratio"] is not None else "n/a", r["cum_change"]))
    print("top sources:", ", ".join("%s=%.0f" % kv for kv in r["top_sources"]))
    print("top sinks:  ", ", ".join("%s=%.0f" % kv for kv in r["top_sinks"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
