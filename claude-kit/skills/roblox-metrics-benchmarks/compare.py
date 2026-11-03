#!/usr/bin/env python3
"""compare.py - compare a game's numbers with the KB benchmark bands (thresholds.json).

  python compare.py --d1 8 --d7 1.5 --session 3 --ptr 2.2 --conv 0.8 [--ctr 1.1 --cpp 0.02 --join 12 --fs5 40 --fps 45 --bounce 30 --d30 1 --arppu 300 --optin 10]
  python compare.py --json '{"d1": 8, "session": 3}'
Prints a markdown table: metric | yours | KB band | verdict | flag | note | sources. Metrics without a numeric KB band print KB GAP.
Verdicts are a first pass; re-check with `kbq.py num "<metric>"` and with the Creator Hub Similar Experience Benchmarks (50th-90th percentile), which are genre-specific.
"""
import argparse
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "thresholds.json"), encoding="utf-8"))["metrics"]


def band_for(m, v):
    for lo, hi, name in m["bands"]:
        if lo <= v < hi:
            return (lo, hi, name)
    return None


def severity(m, b):
    if not b or not m["bands"]:
        return "unknown"
    names = [x[2] for x in m["bands"]]
    idx = names.index(b[2])
    frac = idx / max(1, len(names) - 1)
    if not m["higher_is_better"]:
        frac = 1 - frac
    return "BELOW" if frac < 0.34 else "WITHIN" if frac < 0.67 else "ABOVE"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for k in T:
        ap.add_argument("--" + k, type=float)
    ap.add_argument("--json")
    a = ap.parse_args()
    vals = {k: getattr(a, k) for k in T if getattr(a, k) is not None}
    if a.json:
        vals.update({k: float(v) for k, v in json.loads(a.json).items() if k in T})
    if not vals:
        print("no metrics given; keys: " + ", ".join(T))
        return
    print("| Metric | Yours | KB band | Verdict | Flag | Note | Sources |\n|---|---|---|---|---|---|---|")
    verdicts = []
    for k, v in vals.items():
        m = T[k]
        b = band_for(m, v)
        if m["bands"] and b:
            hi = "inf" if b[1] >= 1000 else "%g" % b[1]
            bandtxt = "%s (%g-%s %s)" % (b[2], b[0], hi, m["unit"])
            verdict = severity(m, b)
        else:
            bandtxt = "KB GAP (no numeric band)"
            verdict = "unknown"
        verdicts.append((verdict, k))
        print("| %s | %g %s | %s | %s | %s | %s | %s |" % (m["label"], v, m["unit"], bandtxt, verdict, m["flag"], m["note"], " ".join(m["sources"][:2])))
    worst = [T[k]["label"] for vv, k in verdicts if vv == "BELOW"]
    print("\nBELOW band: " + (", ".join(worst) if worst else "none") + ". Fix upstream first: packaging/PTR -> first session -> D1 -> D7 -> monetisation -> acquisition.")
    print("Reminder: indie bands are self-reported; confirm against Creator Hub Similar Experience Benchmarks.")


if __name__ == "__main__":
    main()
