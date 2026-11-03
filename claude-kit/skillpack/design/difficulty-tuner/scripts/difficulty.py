#!/usr/bin/env python3
"""difficulty.py - find difficulty spikes and walls in per-stage playtest data. Stdlib only.

  python difficulty.py stages.csv         columns: stage,attempts,fails,quits[,reached]
  python difficulty.py --selftest

Per stage: fail rate = fails/attempts; quit rate = quits/reached (reached defaults to attempts). Flags: fail rate above 1.6x the median of the previous
3 stages (spike), a quit rate above 8 percent (wall), or a fail rate that fell for 3 stages in a row (slack ramp). All thresholds are THIS SKILL'S
DEFAULTS; the vault says only "ramp up, peak at bosses, then dip", launch slightly harder and ease later, use drop-off data to tune. A stage with
fewer than 30 attempts is marked LOW N and not judged.
"""
import csv
import statistics
import sys


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(dict(stage=r["stage"], attempts=int(r["attempts"]), fails=int(r["fails"]), quits=int(r["quits"]), reached=int(r.get("reached") or r["attempts"])))
    return rows


def analyse(rows):
    out = []
    rates = []
    for r in rows:
        fr = r["fails"] / r["attempts"] if r["attempts"] else 0.0
        qr = r["quits"] / r["reached"] if r["reached"] else 0.0
        fl = []
        if r["attempts"] < 30:
            fl.append("LOW N")
        prev = rates[-3:]
        if len(prev) >= 2 and r["attempts"] >= 30:
            med = statistics.median(prev)
            if med > 0 and fr > 1.6 * med:
                fl.append("spike %.0f%% vs %.0f%% before" % (100 * fr, 100 * med))
        if qr > 0.08 and r["attempts"] >= 30:
            fl.append("wall: %.0f%% quit here" % (100 * qr))
        rates.append(fr)
        out.append((r["stage"], r["attempts"], fr, qr, fl))
    for i in range(3, len(rates)):
        if rates[i] < rates[i - 1] < rates[i - 2] < rates[i - 3] and out[i][4] == []:
            out[i][4].append("slack: fail rate fell 3 stages running")
    return out


def selftest():
    rows = [dict(stage=str(i), attempts=100, fails=f, quits=q, reached=100) for i, (f, q) in enumerate([(20, 1), (22, 1), (25, 2), (60, 12), (30, 2)])]
    res = analyse(rows)
    assert res[3][4] and "spike" in res[3][4][0] and any("wall" in x for x in res[3][4])
    assert res[1][4] == [] and res[4][4] == []
    assert "LOW N" in analyse([dict(stage="a", attempts=5, fails=1, quits=0, reached=5)])[0][4]
    slack = analyse([dict(stage=str(i), attempts=100, fails=f, quits=1, reached=100) for i, f in enumerate([50, 40, 30, 20])])
    assert any("slack" in x for x in slack[3][4])
    print("selftest ok (5 checks)")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    res = analyse(load(sys.argv[1]))
    bad = 0
    print("stage  attempts  fail%  quit%  flags")
    for s, n, fr, qr, fl in res:
        print("%-6s %8d  %4.0f   %4.1f  %s" % (s, n, 100 * fr, 100 * qr, "; ".join(fl)))
        bad += sum(1 for x in fl if x != "LOW N")
    print("OK" if not bad else "%d flag(s)" % bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
