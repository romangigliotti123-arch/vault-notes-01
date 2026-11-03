#!/usr/bin/env python3
"""session.py - session length distribution: percentiles, buckets, stop points and the short-session share. Stdlib only.

  python session.py --minutes minutes.txt          (one number per line; or --csv file.csv --col session_minutes)
  python session.py --selftest

Vault (analytics-metrics.md): use percentiles (P10/P50/P90), not averages, because averages hide outliers; judge session length in context (social games
10+ min; stage-gated targets of 10+ min during ad-driven traffic and 20+ min once on the algorithm; average session ~10 min in an official sample
2024-09 - see BENCHMARKS.md for flags). Buckets and the 'stop point' rule (a bucket holding at least 1.8x the share of its neighbours' average) are this
skill's defaults. A stop point is a CANDIDATE: connect it to a game event (match end, shop close, tutorial end) with the churn and funnel skills.
"""
import argparse
import csv
import sys

EDGES = [1, 2, 3, 5, 8, 12, 20, 30, 60, 10 ** 9]
LABELS = ["<1", "1-2", "2-3", "3-5", "5-8", "8-12", "12-20", "20-30", "30-60", "60+"]


def pct(sorted_vals, p):
    if not sorted_vals:
        return 0.0
    k = (len(sorted_vals) - 1) * p / 100.0
    f = int(k)
    c = min(f + 1, len(sorted_vals) - 1)
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


def analyse(vals):
    v = sorted(x for x in vals if x >= 0)
    n = len(v)
    if n < 50:
        return dict(error="only %d sessions: need at least 50 for percentiles to mean anything" % n)
    counts = [0] * len(EDGES)
    for x in v:
        for i, e in enumerate(EDGES):
            if x < e:
                counts[i] += 1
                break
    shares = [c / n for c in counts]
    stops = []
    for i in range(1, len(shares) - 1):
        nb = (shares[i - 1] + shares[i + 1]) / 2
        if shares[i] >= 0.08 and shares[i] >= 1.8 * nb:
            stops.append(LABELS[i])
    return dict(n=n, mean=sum(v) / n, p10=pct(v, 10), p50=pct(v, 50), p90=pct(v, 90), short_lt2=100.0 * (counts[0] + counts[1]) / n, buckets=list(zip(LABELS, counts, [100 * s for s in shares])), stop_candidates=stops)


def selftest():
    import random
    random.seed(7)
    vals = [random.uniform(0.2, 1.8) for _ in range(300)] + [random.uniform(5, 8) for _ in range(500)] + [random.uniform(20, 40) for _ in range(200)]
    a = analyse(vals)
    assert a["p50"] > 3 and a["p10"] < 2 and a["p90"] > 20, a
    assert "5-8" in a["stop_candidates"], a["stop_candidates"]
    assert 25 < a["short_lt2"] < 35
    assert "error" in analyse([1, 2, 3])
    assert round(pct([1, 2, 3, 4, 5], 50), 2) == 3.0
    print("selftest ok (5 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes")
    ap.add_argument("--csv")
    ap.add_argument("--col", default="session_minutes")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if a.csv:
        with open(a.csv, newline="", encoding="utf-8") as f:
            vals = [float(r[a.col]) for r in csv.DictReader(f)]
    elif a.minutes:
        vals = [float(l) for l in open(a.minutes, encoding="utf-8") if l.strip()]
    else:
        ap.error("--minutes or --csv required")
    r = analyse(vals)
    if "error" in r:
        print("ERROR:", r["error"])
        return 1
    print("sessions %d | mean %.1f | P10 %.1f | P50 %.1f | P90 %.1f min | under 2 min: %.1f%%" % (r["n"], r["mean"], r["p10"], r["p50"], r["p90"], r["short_lt2"]))
    for lab, c, s in r["buckets"]:
        print("%7s min %6d %5.1f%% %s" % (lab, c, s, "#" * int(s / 2)))
    print("stop-point candidate buckets:", ", ".join(r["stop_candidates"]) or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
