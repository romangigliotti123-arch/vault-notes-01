#!/usr/bin/env python3
"""segments.py - split players into spend bands from a CSV and show who pays for the game. Stdlib only.

  python segments.py spend.csv [--bands 1,801,5001] [--json]
  python segments.py --selftest

spend.csv: header `userId,robux` (lifetime or window spend per player, one row per player INCLUDING zero spenders; no names, no personal data).
Bands from --bands are lower bounds: default 1,801,5001 gives 0 | 1-800 | 801-5000 | 5001+. (The vault reports 61% of spenders in the smallest
LTV bucket, 1-800 Robux, in the Roblox 2023 monetisation talk: monetisation-other.md "Offer a tiered price range".) Output per band: players,
share of players, Robux, share of Robux, ARPPU for paying bands; then payer conversion and revenue concentration (top 1/5/10% of payers).
Concentration claims in the vault (75% of revenue from 1-5% of players, ~2% making ~90%, top 15% about 50%) are from different sources and eras:
compare, do not treat as targets. Exit 0 always (it describes; it does not judge).
"""
import argparse
import csv
import json
import sys


def load(path):
    with open(path, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if not rows or "robux" not in rows[0]:
        raise ValueError("CSV needs a header with a robux column")
    return [max(0, int(float(r["robux"]))) for r in rows]


def analyse(spend, bounds=(1, 801, 5001)):
    n = len(spend)
    if n == 0:
        raise ValueError("no players")
    edges = [0] + sorted(bounds)
    labels = []
    for i, lo in enumerate(edges):
        if i == 0:
            labels.append("0 (non-payers)")
        else:
            hi = edges[i + 1] - 1 if i + 1 < len(edges) else None
            labels.append("%d-%d" % (lo, hi) if hi is not None else "%d+" % lo)
    total = sum(spend)
    bands = []
    for i, lo in enumerate(edges):
        hi = edges[i + 1] if i + 1 < len(edges) else float("inf")
        group = [s for s in spend if lo <= s < hi] if i else [s for s in spend if s < edges[1]]
        robux = sum(group)
        bands.append({
            "band": labels[i],
            "players": len(group),
            "share_players": round(len(group) / n, 4),
            "robux": robux,
            "share_robux": round(robux / total, 4) if total else 0,
            "arppu": round(robux / len(group), 1) if group and i else 0,
        })
    payers = sorted([s for s in spend if s > 0], reverse=True)

    def top(p):
        if not payers or not total:
            return 0
        k = max(1, int(round(len(payers) * p)))
        return round(sum(payers[:k]) / total, 4)

    return {
        "players": n,
        "payers": len(payers),
        "payer_conversion": round(len(payers) / n, 4),
        "total_robux": total,
        "bands": bands,
        "top_payers_share": {"top1pct": top(0.01), "top5pct": top(0.05), "top10pct": top(0.10)},
    }


def selftest():
    spend = [0] * 90 + [50] * 6 + [1000] * 3 + [10000]
    r = analyse(spend)
    assert r["players"] == 100 and r["payers"] == 10 and r["payer_conversion"] == 0.1, r
    assert [b["players"] for b in r["bands"]] == [90, 6, 3, 1], r["bands"]
    assert r["total_robux"] == 300 + 3000 + 10000
    assert r["bands"][3]["share_robux"] == round(10000 / 13300, 4)
    assert r["bands"][1]["arppu"] == 50.0
    assert analyse([0, 0, 0])["top_payers_share"]["top5pct"] == 0
    try:
        analyse([])
        raise AssertionError("empty accepted")
    except ValueError:
        pass
    import os
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "s.csv")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("userId,robux\n1,0\n2,99\n")
        assert load(p) == [0, 99]
    print("segments selftest: 6 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--bands", default="1,801,5001")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("spend.csv required")
    r = analyse(load(a.file), tuple(int(x) for x in a.bands.split(",")))
    if a.json:
        print(json.dumps(r, indent=2))
        return 0
    print("players %d, payers %d (conversion %.2f%%), total %d Robux" % (r["players"], r["payers"], r["payer_conversion"] * 100, r["total_robux"]))
    print("%-16s %8s %8s %10s %8s %8s" % ("band", "players", "% players", "robux", "% robux", "ARPPU"))
    for b in r["bands"]:
        print("%-16s %8d %8.1f%% %10d %7.1f%% %8.1f" % (b["band"], b["players"], b["share_players"] * 100, b["robux"], b["share_robux"] * 100, b["arppu"]))
    t = r["top_payers_share"]
    print("revenue from top payers: 1%% -> %.0f%%, 5%% -> %.0f%%, 10%% -> %.0f%%" % (t["top1pct"] * 100, t["top5pct"] * 100, t["top10pct"] * 100))
    return 0


if __name__ == "__main__":
    sys.exit(main())
