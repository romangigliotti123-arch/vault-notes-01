#!/usr/bin/env python3
"""subplan.py - validate an experience-subscription tier plan against the vault's rules and compare it with a one-time pass. Stdlib only.

  python subplan.py tiers.json [--share 0.7] [--months 4] [--pass-price 399] [--json]
  python subplan.py --selftest

tiers.json: {"tiers": [{"name": "Supporter", "priceRobux": 199, "benefits": ["daily gems", "chat tag"], "platformExclusive": false, "extraTasks": false}]}
Rules checked (monetisation-other.md "Experience subscriptions and Roblox Plus", Roblox Creator Docs 2026-10; LIVE-CHECK before launch, they change):
  at most 50 tiers per experience; tier names unique; every tier has benefits; tiers distinct (no two tiers with identical benefit sets);
  the same benefits on all platforms (platformExclusive must be false); no extra tasks demanded of subscribers (extraTasks false);
  the creator share defaults to 0.70 for Robux subscriptions (vault) and is a parameter. Economics printed per tier: net Robux per subscriber-month,
  expected lifetime value over --months retained months (default 4: an ASSUMPTION, use your own retention data), and months until the subscription
  out-earns a one-time pass of --pass-price. Vault note: a tier must be honoured for the full term, so do not promise what you cannot ship.
Exit 1 on any ERROR.
"""
import argparse
import json
import math
import sys


def check(plan, share=0.70, months=4, pass_price=None):
    findings = []
    tiers = plan.get("tiers", [])
    if not tiers:
        findings.append(("ERROR", "-", "no tiers"))
    if len(tiers) > 50:
        findings.append(("ERROR", "-", "more than 50 tiers"))
    names, sets = set(), {}
    econ = []
    for t in tiers:
        n = t.get("name", "?")
        if n in names:
            findings.append(("ERROR", n, "duplicate tier name"))
        names.add(n)
        ben = t.get("benefits") or []
        if not ben:
            findings.append(("ERROR", n, "tier has no benefits"))
        key = frozenset(b.strip().lower() for b in ben)
        if key and key in sets:
            findings.append(("ERROR", n, "same benefits as tier %s: tiers must be distinct" % sets[key]))
        sets[key] = n
        if t.get("platformExclusive"):
            findings.append(("ERROR", n, "benefit is platform-exclusive: benefits must be the same on all platforms"))
        if t.get("extraTasks"):
            findings.append(("ERROR", n, "subscribers must not need extra tasks to receive benefits"))
        p = t.get("priceRobux")
        if not isinstance(p, int) or p < 1:
            findings.append(("ERROR", n, "priceRobux must be a whole number >= 1"))
            continue
        net = p * share
        row = {"tier": n, "net_per_month": round(net, 1), "ltv": round(net * months, 1)}
        if pass_price:
            row["months_to_beat_pass"] = math.ceil(pass_price / net)
        econ.append(row)
    return findings, econ


def selftest():
    good = {"tiers": [{"name": "A", "priceRobux": 100, "benefits": ["x"]}, {"name": "B", "priceRobux": 300, "benefits": ["x", "y"]}]}
    f, e = check(good, pass_price=350)
    assert f == [] and e[0]["net_per_month"] == 70.0 and e[0]["ltv"] == 280.0 and e[0]["months_to_beat_pass"] == 5, (f, e)
    bad = {"tiers": [
        {"name": "A", "priceRobux": 100, "benefits": ["x"]},
        {"name": "A", "priceRobux": 100, "benefits": ["X"], "platformExclusive": True},
        {"name": "C", "priceRobux": 0, "benefits": [], "extraTasks": True},
    ]}
    f, _ = check(bad)
    msgs = " | ".join(m for _, _, m in f)
    for needle in ("duplicate", "same benefits", "platform-exclusive", "extra tasks", "no benefits", "priceRobux"):
        assert needle in msgs, (needle, msgs)
    assert check({"tiers": []})[0][0][0] == "ERROR"
    assert check({"tiers": [{"name": str(i), "priceRobux": 1, "benefits": [str(i)]} for i in range(51)]})[0][0][2] == "more than 50 tiers"
    print("subplan selftest: 5 checks ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--share", type=float, default=0.70)
    ap.add_argument("--months", type=float, default=4)
    ap.add_argument("--pass-price", type=int)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("tiers.json required")
    with open(a.file, encoding="utf-8") as fh:
        plan = json.load(fh)
    f, e = check(plan, a.share, a.months, a.pass_price)
    if a.json:
        print(json.dumps({"findings": f, "economics": e}, indent=2))
    else:
        for s, n, m in f:
            print("%-5s %-14s %s" % (s, n, m))
        for r in e:
            extra = "  beats a %d-Robux pass after %d months" % (a.pass_price, r["months_to_beat_pass"]) if a.pass_price else ""
            print("%-14s net %.1f/month, LTV over %g months %.1f%s" % (r["tier"], r["net_per_month"], a.months, r["ltv"], extra))
        print("%d error(s). Rules and the 70%% share are the vault's 2026-10 values: live-check." % sum(1 for x in f if x[0] == "ERROR"))
    return 1 if any(x[0] == "ERROR" for x in f) else 0


if __name__ == "__main__":
    sys.exit(main())
