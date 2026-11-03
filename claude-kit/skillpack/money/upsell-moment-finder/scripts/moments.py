#!/usr/bin/env python3
"""moments.py - rank the "moment of need" events by how often a purchase follows them. Stdlib only.

  python moments.py events.csv [--window 60] [--purchase purchase] [--min-count 30] [--json]
  python moments.py --selftest

events.csv: header `userId,t,event`, t in seconds (any epoch), one row per logged event. Use the analytics events the kit's Analytics system records
(needs: out_of_currency, inventory_full, death, blocked_by_gate, wait_timer, ...; plus a `purchase` event). For every non-purchase event type the tool
counts occurrences and how many were followed by a purchase from the SAME player within --window seconds (default 60). Ranking is by that rate, only for
event types with at least --min-count occurrences (small samples are listed but marked LOW SAMPLE). This is correlation: a high rate means "players who hit
this often buy soon after", not that the offer caused it. Confirm with an A/B test (ab-testing-and-experiments.md) before moving the shop.
Vault background (monetisation-other.md "Don't push purchases with pop-ups; trigger offers at moments of need"): offer solutions when players are blocked, dying or waiting.
No names or personal data are needed; use hashed ids.
"""
import argparse
import csv
import json
import sys
from collections import defaultdict


def load(path):
    with open(path, encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        rows = [(r["userId"], float(r["t"]), r["event"]) for r in rd]
    return rows


def analyse(rows, purchase="purchase", window=60.0, min_count=30):
    by_user = defaultdict(list)
    for u, t, e in rows:
        by_user[u].append((t, e))
    stats = defaultdict(lambda: [0, 0])  # event -> [count, followed]
    for evs in by_user.values():
        evs.sort()
        buys = [t for t, e in evs if e == purchase]
        for t, e in evs:
            if e == purchase:
                continue
            stats[e][0] += 1
            if any(t < b <= t + window for b in buys):
                stats[e][1] += 1
    out = []
    for e, (n, f) in stats.items():
        out.append({"event": e, "count": n, "followed_by_purchase": f, "rate": round(f / n, 4), "low_sample": n < min_count})
    out.sort(key=lambda r: (r["low_sample"], -r["rate"], r["event"]))
    return out


def selftest():
    rows = []
    for i in range(40):  # 40 users hit out_of_currency; 10 buy within 30 s
        rows.append(("u%d" % i, 100, "out_of_currency"))
        if i < 10:
            rows.append(("u%d" % i, 130, "purchase"))
    for i in range(40):  # death: 2 buy, but 100 s later (outside the window)
        rows.append(("d%d" % i, 10, "death"))
        if i < 2:
            rows.append(("d%d" % i, 110, "purchase"))
    rows.append(("z", 1, "rare_event"))
    r = analyse(rows)
    assert [x["event"] for x in r] == ["out_of_currency", "death", "rare_event"], r
    assert r[0]["rate"] == 0.25 and r[1]["rate"] == 0.0 and r[2]["low_sample"], r
    r = analyse(rows, window=200)
    assert r[1]["event"] == "death" or r[0]["event"] == "out_of_currency"
    assert {x["event"]: x["rate"] for x in r}["death"] == 0.05
    # a purchase BEFORE the event does not count
    r = analyse([("a", 5, "purchase"), ("a", 10, "death")], min_count=1)
    assert r[0]["rate"] == 0.0
    print("moments selftest: 4 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--window", type=float, default=60.0)
    ap.add_argument("--purchase", default="purchase")
    ap.add_argument("--min-count", type=int, default=30)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("events.csv required")
    r = analyse(load(a.file), a.purchase, a.window, a.min_count)
    if a.json:
        print(json.dumps(r, indent=2))
        return 0
    print("%-22s %8s %10s %8s" % ("event", "count", "-> purchase", "rate"))
    for x in r:
        print("%-22s %8d %10d %7.1f%%%s" % (x["event"], x["count"], x["followed_by_purchase"], x["rate"] * 100, "  LOW SAMPLE" if x["low_sample"] else ""))
    print("Correlation only: A/B test the offer placement before trusting the ranking.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
