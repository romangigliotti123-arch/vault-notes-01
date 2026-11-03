#!/usr/bin/env python3
"""sprint.py - fit a prioritised task list into a week. Stdlib only.

  python sprint.py tasks.csv [--days 5] [--hours-per-day 3] [--solo-factor 2.0] [--buffer 0.2]
  python sprint.py --selftest

CSV columns: id,title,est_h,priority   (priority 1 = most important; est_h = your raw guess in hours)
Capacity = days * hours_per_day * (1 - buffer). Each raw estimate is multiplied by --solo-factor (default 2.0: the vault's
indie rule that solo developers take about twice as long as planned; set 1.0 for a tested team velocity). Tasks are taken in
priority order; a task that does not fit goes to Overflow (next sprint), and smaller later tasks are NOT used to fill gaps
out of order (that hides priority). Prints a plan and utilisation. Exit 0 ok, 1 if nothing fits or the input is bad.
"""
import argparse
import csv
import io
import sys


def plan(rows, days=5, hpd=3.0, solo=2.0, buffer=0.2):
    cap = days * hpd * (1 - buffer)
    items = []
    for r in rows:
        try:
            items.append((int(r["priority"]), r["id"], r.get("title", ""), float(r["est_h"]) * solo))
        except (KeyError, ValueError):
            raise ValueError("bad row (need id,title,est_h,priority numbers): %r" % (r,))
    items.sort(key=lambda x: (x[0], x[1]))
    used, fit, over, blocked = 0.0, [], [], False
    for pr, i, t, h in items:
        if not blocked and used + h <= cap + 1e-9:
            fit.append((i, t, h))
            used += h
        else:
            blocked = True
            over.append((i, t, h))
    return cap, used, fit, over


def selftest():
    rows = list(csv.DictReader(io.StringIO("id,title,est_h,priority\nA,a,2,1\nB,b,3,2\nC,c,1,3\nD,d,2,2\n")))
    cap, used, fit, over = plan(rows, days=5, hpd=3, solo=2.0, buffer=0.2)
    assert abs(cap - 12.0) < 1e-9
    assert [x[0] for x in fit] == ["A", "B"] and abs(used - 10.0) < 1e-9, (fit, used)
    assert [x[0] for x in over] == ["D", "C"], over
    cap, used, fit, over = plan(rows, days=5, hpd=3, solo=1.0, buffer=0.0)
    assert [x[0] for x in fit] == ["A", "B", "D", "C"] and not over
    try:
        plan([{"id": "x", "est_h": "n", "priority": "1"}])
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("selftest ok (4 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--days", type=float, default=5)
    ap.add_argument("--hours-per-day", type=float, default=3.0)
    ap.add_argument("--solo-factor", type=float, default=2.0)
    ap.add_argument("--buffer", type=float, default=0.2)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    with open(a.file, encoding="utf-8", newline="") as f:
        try:
            cap, used, fit, over = plan(list(csv.DictReader(f)), a.days, a.hours_per_day, a.solo_factor, a.buffer)
        except ValueError as e:
            print("ERROR:", e)
            return 1
    print("capacity %.1f h (buffer %d%%), planned %.1f h (%d%% used)" % (cap, a.buffer * 100, used, 100 * used / cap if cap else 0))
    for i, t, h in fit:
        print("PLAN     %-6s %-30s %.1f h" % (i, t[:30], h))
    for i, t, h in over:
        print("OVERFLOW %-6s %-30s %.1f h" % (i, t[:30], h))
    return 0 if fit else 1


if __name__ == "__main__":
    sys.exit(main())
