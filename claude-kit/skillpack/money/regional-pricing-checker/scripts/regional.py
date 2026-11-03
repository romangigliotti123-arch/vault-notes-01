#!/usr/bin/env python3
"""regional.py - sanity-check a table of base and regional prices before you enter them in Creator Hub. Stdlib only.

  python regional.py prices.json [--min-ratio 0.3] [--max-ratio 1.0] [--json]
  python regional.py --selftest

prices.json:  {"items": [{"name": "VIP", "base": 399, "regions": {"BR": 199, "IN": 149, "DE": 399}}]}
Checks per item: prices are whole Robux >= 1; every regional price is within [min-ratio, max-ratio] of base. The defaults 0.3 and 1.0 are the
vault's reported platform bounds (pricing.md "Set regional prices and mind the bounds": regional prices never exceed the default and never drop more
than 70% below it; Roblox Creator Docs 2026-10, live-check); regions given in --order (poorest to richest) must not invert; every item must cover the same
regions (a gap hides a region on a different price).
The platform's own regional-pricing rules and which levels exist change: the vault points at the Creator Docs regional-pricing page
(monetisation-other.md, "Regional pricing, gifting and Robux transfers"). Read that page the same day; this tool does not know it.
Exit 1 on any ERROR.
"""
import argparse
import json
import sys


def check(data, min_ratio=0.3, max_ratio=1.0, order=None):
    findings = []
    items = data.get("items", [])
    if not items:
        findings.append(("ERROR", "-", "no items"))
    region_sets = []
    for it in items:
        name = it.get("name", "?")
        base = it.get("base")
        regions = it.get("regions", {})
        if not isinstance(base, int) or base < 1:
            findings.append(("ERROR", name, "base must be a whole number >= 1"))
            continue
        region_sets.append((name, set(regions)))
        for reg, price in regions.items():
            if not isinstance(price, int) or price < 1:
                findings.append(("ERROR", name, "%s price %r is not a whole Robux >= 1" % (reg, price)))
                continue
            ratio = price / base
            if ratio < min_ratio:
                findings.append(("ERROR", name, "%s is %.0f%% of base, under the %.0f%% floor" % (reg, ratio * 100, min_ratio * 100)))
            elif ratio > max_ratio:
                findings.append(("ERROR", name, "%s is %.0f%% of base, over the %.0f%% ceiling" % (reg, ratio * 100, max_ratio * 100)))
        if order:
            seq = [regions[r] for r in order if r in regions and isinstance(regions[r], int)]
            if any(seq[i] > seq[i + 1] for i in range(len(seq) - 1)):
                findings.append(("ERROR", name, "prices invert along the order %s" % ">".join(order)))
    if region_sets:
        union = set().union(*[s for _, s in region_sets])
        for name, s in region_sets:
            missing = union - s
            if missing:
                findings.append(("WARN", name, "no price for %s (other items have one)" % ", ".join(sorted(missing))))
    return findings


def selftest():
    ok = {"items": [{"name": "A", "base": 100, "regions": {"BR": 50, "IN": 30, "DE": 100}}]}
    assert check(ok) == []
    f = check({"items": [{"name": "A", "base": 100, "regions": {"BR": 5}}]})
    assert len(f) == 1 and f[0][0] == "ERROR", f
    f = check({"items": [{"name": "A", "base": 100, "regions": {"BR": 150}}]})
    assert any("ceiling" in m for _, _, m in f), f
    f = check({"items": [{"name": "A", "base": 100, "regions": {"BR": 40.5}}]})
    assert any("whole" in m for _, _, m in f), f
    f = check({"items": [{"name": "A", "base": 100, "regions": {"IN": 60, "BR": 40}}]}, order=["IN", "BR"])
    assert any("invert" in m for _, _, m in f), f
    f = check({"items": [{"name": "A", "base": 100, "regions": {"BR": 50}}, {"name": "B", "base": 50, "regions": {}}]})
    assert any(s == "WARN" for s, _, _ in f), f
    assert check({"items": []})[0][0] == "ERROR"
    print("regional selftest: 7 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--min-ratio", type=float, default=0.3)
    ap.add_argument("--max-ratio", type=float, default=1.0)
    ap.add_argument("--order", help="comma list of region codes from poorest to richest economy")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("prices.json required")
    with open(a.file, encoding="utf-8") as fh:
        data = json.load(fh)
    f = check(data, a.min_ratio, a.max_ratio, a.order.split(",") if a.order else None)
    if a.json:
        print(json.dumps([{"level": s, "item": i, "message": m} for s, i, m in f], indent=2))
    else:
        for s, i, m in f:
            print("%-5s %-16s %s" % (s, i, m))
        print("%d error(s), %d warning(s). Live-check the platform's regional pricing page before relying on this." % (
            sum(1 for x in f if x[0] == "ERROR"), sum(1 for x in f if x[0] == "WARN")))
    return 1 if any(x[0] == "ERROR" for x in f) else 0


if __name__ == "__main__":
    sys.exit(main())
