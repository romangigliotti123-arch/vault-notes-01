#!/usr/bin/env python3
"""snapshot.py - append the day's numbers to a CSV log and compare them with the same weekday last week. Stdlib only.

  python snapshot.py --log metrics-log.csv --date 2026-11-02 --set DailyActiveUsers=5400 --set ForwardD1Retention=11.8 [--note "update 12 live"]
  python snapshot.py --log metrics-log.csv --from-pull pull.json [--date 2026-11-02]      pull.json = `analytics-pull.py --universe N --json` output; the LAST point of each series is used
  python snapshot.py --log metrics-log.csv --report
  python snapshot.py --selftest

Log format: date,metric,value,note (long format, one row per metric per day, re-running a day REPLACES that day's value for that metric, nothing else is touched).
Vault (analytics-metrics.md): compare each day with the same weekday last week (PeriodOverPeriod 7 days) to remove weekly seasonality; read the post-spike
baseline a week later, not the spike; do not sum daily uniques into weekly totals (this log stores each day's value separately and never adds them); data lags
(most signals 24 h, monetisation KPIs 2 days, ad metrics 48 h), so log a metric only once it has settled and pass --date accordingly. The +/- flag threshold (10 percent vs
last week) is this skill's default. The log is plain numbers about your own game: it contains no keys; keep it out of public repos if the numbers are private.
"""
import argparse
import csv
import datetime
import json
import os
import sys


def read(path):
    if not os.path.isfile(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(path, rows):
    rows.sort(key=lambda r: (r["date"], r["metric"]))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "metric", "value", "note"])
        w.writeheader()
        w.writerows(rows)


def upsert(rows, date, metric, value, note=""):
    rows[:] = [r for r in rows if not (r["date"] == date and r["metric"] == metric)]
    rows.append(dict(date=date, metric=metric, value=repr(float(value)) if not float(value).is_integer() else str(int(float(value))), note=note))


def compare(rows, date, thresh=10.0):
    d = datetime.date.fromisoformat(date)
    prev = (d - datetime.timedelta(days=7)).isoformat()
    cur = {r["metric"]: float(r["value"]) for r in rows if r["date"] == date}
    old = {r["metric"]: float(r["value"]) for r in rows if r["date"] == prev}
    out = []
    for m, v in sorted(cur.items()):
        if m in old and old[m]:
            ch = 100.0 * (v - old[m]) / abs(old[m])
            out.append((m, v, old[m], ch, "CHECK" if abs(ch) >= thresh else "ok"))
        else:
            out.append((m, v, None, None, "no value on %s" % prev))
    return out


def from_pull(js):
    vals = {}
    for metric, series in js.items():
        if isinstance(series, dict):  # error entry
            continue
        for s in series:
            if s.get("breakdowns"):
                continue  # only unbroken series go in the log
            pts = [p for p in s.get("points", []) if isinstance(p[1], (int, float))]
            if pts:
                vals[metric] = (pts[-1][0], pts[-1][1])
    return vals


def selftest():
    import tempfile
    p = os.path.join(tempfile.mkdtemp(), "m.csv")
    rows = read(p)
    assert rows == []
    upsert(rows, "2026-10-26", "DAU", 5000)
    upsert(rows, "2026-11-02", "DAU", 5600)
    upsert(rows, "2026-11-02", "D1", 11.5)
    write(p, rows)
    rows = read(p)
    assert len(rows) == 3
    upsert(rows, "2026-11-02", "DAU", 5700)  # replace, not duplicate
    assert sum(1 for r in rows if r["metric"] == "DAU" and r["date"] == "2026-11-02") == 1
    c = {x[0]: x for x in compare(rows, "2026-11-02")}
    assert c["DAU"][4] == "CHECK" and round(c["DAU"][3]) == 14 and "no value" in c["D1"][4]
    v = from_pull({"DailyActiveUsers": [{"breakdowns": [], "points": [["2026-11-01", 100], ["2026-11-02", 120]]}, {"breakdowns": [{"dimension": "Platform"}], "points": [["x", 1]]}], "Bad": {"error": "x"}})
    assert v == {"DailyActiveUsers": ("2026-11-02", 120)}
    print("selftest ok (5 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log")
    ap.add_argument("--date")
    ap.add_argument("--set", action="append", default=[])
    ap.add_argument("--from-pull")
    ap.add_argument("--note", default="")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--threshold", type=float, default=10.0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not a.log:
        ap.error("--log required")
    rows = read(a.log)
    date = a.date or (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    changed = False
    for kv in a.set:
        k, _, v = kv.partition("=")
        upsert(rows, date, k.strip(), float(v), a.note)
        changed = True
    if a.from_pull:
        for m, (d, v) in from_pull(json.load(open(a.from_pull, encoding="utf-8"))).items():
            upsert(rows, a.date or d, m, v, a.note)
            changed = True
    if changed:
        write(a.log, rows)
    if a.report or changed:
        latest = max((r["date"] for r in rows), default=None) if not a.date and a.report else date
        if latest:
            print("vs same weekday last week, %s:" % latest)
            for m, v, o, ch, st in compare(rows, latest, a.threshold):
                print("  %-22s %10g  last wk %s  %s  %s" % (m, v, "%g" % o if o is not None else "-", "%+.1f%%" % ch if ch is not None else "", st))
    return 0


if __name__ == "__main__":
    sys.exit(main())
