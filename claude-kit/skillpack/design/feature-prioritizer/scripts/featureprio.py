#!/usr/bin/env python3
"""featureprio.py - rank candidate features by loop impact, cost and risk; draw the cut line. Stdlib only.

  python featureprio.py features.csv [--budget-days 14]     columns: feature,loop_layer,impact,cost_days,risk       (impact 0-5, risk 1-5)
  python featureprio.py --selftest

score = impact * layer_weight / (cost_days * risk_factor); layer_weight: 1 = minute-to-minute 1.5, 2 = session 1.2, 3 = progression 1.0, 0 = feeds no layer.
risk_factor = 1 + 0.25 * (risk-1). Features with loop_layer 0 or impact 0 are CUT regardless of cost (vault: every new system must feed the core loop or
be cut). Greedy fill to --budget-days in score order; the rest are DEFERRED. The weights are THIS SKILL'S DEFAULTS; the must-feed-the-loop rule is the vault's.
"""
import csv
import sys

W = {0: 0.0, 1: 1.5, 2: 1.2, 3: 1.0}


def rank(rows, budget):
    out = []
    for r in rows:
        layer, imp, cost, risk = int(r["loop_layer"]), float(r["impact"]), float(r["cost_days"]), float(r["risk"])
        score = 0.0 if layer == 0 or imp == 0 else imp * W.get(layer, 0) / (max(cost, 0.25) * (1 + 0.25 * (risk - 1)))
        out.append(dict(feature=r["feature"], layer=layer, cost=cost, score=score))
    out.sort(key=lambda x: -x["score"])
    used = 0.0
    for o in out:
        if o["score"] == 0:
            o["verdict"] = "CUT (feeds no layer)"
        elif used + o["cost"] <= budget:
            used += o["cost"]
            o["verdict"] = "KEEP"
        else:
            o["verdict"] = "DEFER"
    return out, used


def selftest():
    rows = [dict(feature="sprint", loop_layer=1, impact=4, cost_days=1, risk=1), dict(feature="clans", loop_layer=0, impact=3, cost_days=5, risk=3),
            dict(feature="pets", loop_layer=3, impact=5, cost_days=6, risk=2), dict(feature="trading", loop_layer=2, impact=3, cost_days=8, risk=4)]
    out, used = rank(rows, 8)
    d = {o["feature"]: o for o in out}
    assert out[0]["feature"] == "sprint" and d["clans"]["verdict"].startswith("CUT")
    assert d["pets"]["verdict"] == "KEEP" and d["trading"]["verdict"] == "DEFER" and used == 7
    assert d["clans"]["score"] == 0
    print("selftest ok (4 checks)")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    budget = float(sys.argv[sys.argv.index("--budget-days") + 1]) if "--budget-days" in sys.argv else 14.0
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        out, used = rank(list(csv.DictReader(f)), budget)
    print("feature            layer  days  score  verdict")
    for o in out:
        print("%-18s %5d  %4.1f  %5.2f  %s" % (o["feature"], o["layer"], o["cost"], o["score"], o["verdict"]))
    print("budget used %.1f of %.1f days" % (used, budget))


if __name__ == "__main__":
    main()
