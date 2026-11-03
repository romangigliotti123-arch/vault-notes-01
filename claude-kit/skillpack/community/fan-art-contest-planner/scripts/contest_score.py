#!/usr/bin/env python3
"""contest_score.py - score contest entries on a fixed rubric across judges. Stdlib only.

  python contest_score.py scores.csv --weights creativity=3,theme=2,polish=1 [--max 5] [--spread 0.3]
  python contest_score.py --selftest

CSV columns: entry, judge, criterion, score. Entries are anonymous ids (E01), never player names, until winners are picked and have agreed
to be named. Every judge must score every criterion for every entry (vault: score every entry on the same rubric fixed before judging).
Output: weighted mean per entry (0..100), ranked; WARN when judges disagree by more than --spread of the range; FAIL on missing scores.
Exit 1 on FAIL.
"""
import argparse
import csv
import sys
from collections import defaultdict


def score(rows, weights, mx=5.0, spread=0.3):
    crit = list(weights)
    by = defaultdict(lambda: defaultdict(dict))
    for r in rows:
        by[r["entry"]][r["judge"]][r["criterion"]] = float(r["score"])
    judges = {j for e in by.values() for j in e}
    problems, ranking = [], []
    wsum = sum(weights.values())
    for e, js in by.items():
        tot = {}
        for j in judges:
            s = js.get(j, {})
            miss = [c for c in crit if c not in s]
            if miss:
                problems.append(("FAIL", "%s missing %s from %s" % (e, "/".join(miss), j)))
                continue
            if any(not 0 <= s[c] <= mx for c in crit):
                problems.append(("FAIL", "%s out of range from %s" % (e, j)))
                continue
            tot[j] = 100 * sum(s[c] * weights[c] for c in crit) / (mx * wsum)
        if tot:
            if max(tot.values()) - min(tot.values()) > 100 * spread:
                problems.append(("WARN", "%s judges disagree (%.0f vs %.0f): discuss before ranking" % (e, min(tot.values()), max(tot.values()))))
            ranking.append((e, sum(tot.values()) / len(tot)))
    ranking.sort(key=lambda x: (-x[1], x[0]))
    for a, b in zip(ranking, ranking[1:]):
        if abs(a[1] - b[1]) < 1e-9:
            problems.append(("WARN", "tie between %s and %s: decide by the tie-break rule you published" % (a[0], b[0])))
    return ranking, problems


def selftest():
    w = {"creativity": 3, "theme": 2, "polish": 1}
    rows = []
    for e, vals in (("E01", (5, 5, 5)), ("E02", (3, 3, 3)), ("E03", (5, 1, 0))):
        for j in ("j1", "j2"):
            for c, v in zip(w, vals):
                rows.append({"entry": e, "judge": j, "criterion": c, "score": str(v)})
    rank, prob = score(rows, w)
    assert [r[0] for r in rank] == ["E01", "E02", "E03"], rank
    assert abs(rank[0][1] - 100) < 1e-9 and abs(rank[1][1] - 60) < 1e-9
    assert not prob, prob
    rows2 = [r for r in rows if not (r["entry"] == "E02" and r["judge"] == "j2" and r["criterion"] == "polish")]
    assert any(s == "FAIL" for s, m in score(rows2, w)[1])
    rows3 = [dict(r) for r in rows]
    for r in rows3:
        if r["entry"] == "E02" and r["judge"] == "j2":
            r["score"] = "5"
    assert any(s == "WARN" and "disagree" in m for s, m in score(rows3, w)[1])
    rows4 = [dict(r, score="9") if r["entry"] == "E01" else r for r in rows]
    assert any("out of range" in m for s, m in score(rows4, w)[1])
    print("selftest ok (6 asserts)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--weights")
    ap.add_argument("--max", type=float, default=5)
    ap.add_argument("--spread", type=float, default=0.3)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv or not a.weights:
        ap.error("give the csv and --weights")
    w = {k: float(v) for k, v in (p.split("=") for p in a.weights.split(","))}
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        rank, prob = score(list(csv.DictReader(f)), w, a.max, a.spread)
    for i, (e, s) in enumerate(rank, 1):
        print("%2d. %-8s %5.1f" % (i, e, s))
    for sev, m in prob:
        print(sev, m)
    return 1 if any(s == "FAIL" for s, m in prob) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
