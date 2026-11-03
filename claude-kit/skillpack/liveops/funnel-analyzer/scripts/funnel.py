#!/usr/bin/env python3
"""funnel.py - read an onboarding or purchase funnel: per-step conversion, drop, and the biggest drop to fix first. Stdlib only.

  python funnel.py --steps "Spawn:1000,Moved:860,FirstCoin:640,FirstUpgrade:300,Returned:120"
  python funnel.py --csv funnel.csv        (columns: step,count   in funnel order)
  python funnel.py --selftest

Counts are distinct players (or sessions) that REACHED each step, from kit Analytics LogOnboardingFunnelStepEvent / LogFunnelStepEvent data in Creator Hub.
Vault (analytics-metrics.md): fix the biggest red drop first; funnel steps only show on days a user reached them, so discover steps with a 90-day
lookback. The 'big drop' cut-off (default 30 percent lost at one step) is this skill's default, not a sourced number.
"""
import argparse
import csv
import sys


def parse_steps(s):
    out = []
    for part in s.split(","):
        name, _, n = part.rpartition(":")
        out.append((name.strip(), float(n)))
    return out


def analyse(steps, big=30.0):
    rows, warns = [], []
    top = steps[0][1]
    if top <= 0:
        return rows, ["first step has no players"]
    if top < 100:
        warns.append("fewer than 100 players at step 1: percentages are noisy")
    prev = top
    for i, (name, n) in enumerate(steps):
        if n > prev and i:
            warns.append("step %r has MORE players (%g) than the step before (%g): wrong order, or steps counted per event not per player" % (name, n, prev))
        step_conv = 100.0 * n / prev if prev else 0.0
        rows.append(dict(step=name, count=n, of_first=100.0 * n / top, of_prev=step_conv, lost=100.0 - step_conv if i else 0.0, abs_lost=max(prev - n, 0) if i else 0))
        prev = n
    cand = [r for r in rows[1:] if r["lost"] >= big]
    worst = max(rows[1:], key=lambda r: r["abs_lost"]) if len(rows) > 1 else None
    return dict(rows=rows, worst=worst, big=[r["step"] for r in cand], overall=100.0 * steps[-1][1] / top), warns


def selftest():
    r, w = analyse(parse_steps("A:1000,B:900,C:450,D:400"))
    assert round(r["rows"][2]["lost"]) == 50 and r["worst"]["step"] == "C" and r["big"] == ["C"]
    assert round(r["overall"]) == 40 and not w
    r, w = analyse(parse_steps("A:50,B:60"))
    assert len(w) == 2, w
    r, w = analyse(parse_steps("Tutorial: part 1:100,Buy:90"))
    assert r["rows"][0]["step"] == "Tutorial: part 1"
    assert analyse([("A", 0)])[1]
    print("selftest ok (4 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps")
    ap.add_argument("--csv")
    ap.add_argument("--big", type=float, default=30.0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if a.csv:
        with open(a.csv, newline="", encoding="utf-8") as f:
            steps = [(r["step"], float(r["count"])) for r in csv.DictReader(f)]
    elif a.steps:
        steps = parse_steps(a.steps)
    else:
        ap.error("--steps or --csv required")
    r, w = analyse(steps, a.big)
    if isinstance(r, list):
        print("ERROR:", "; ".join(w))
        return 1
    print("%-22s %8s %9s %9s %7s" % ("step", "players", "of first", "of prev", "lost"))
    for x in r["rows"]:
        print("%-22s %8g %8.1f%% %8.1f%% %6.1f%%" % (x["step"], x["count"], x["of_first"], x["of_prev"], x["lost"]))
    print("overall %.1f%%; biggest absolute loss: %s (%g players); steps losing >= %g%%: %s" % (r["overall"], r["worst"]["step"] if r["worst"] else "-", r["worst"]["abs_lost"] if r["worst"] else 0, a.big, ", ".join(r["big"]) or "none"))
    for x in w:
        print("WARN:", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
