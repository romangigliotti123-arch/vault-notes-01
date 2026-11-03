#!/usr/bin/env python3
"""abread.py - read an A/B result with significance, a confidence interval, the sample-ratio check and guardrail metrics. Stdlib only.

  python abread.py --a-n 6000 --a-x 720 --b-n 5900 --b-x 790 [--guard "playtime:-4.2:-9.0:+0.6"] [--duration-days 14 --planned-days 14] [--split 50]
        a = control, b = treatment; n = enrolled players, x = players who hit the goal (a proportion metric such as D1 or conversion)
        --guard "name:relative_change_pct:ci_low_pct:ci_high_pct"  (repeatable) for a guardrail metric read from Creator Hub
  python abread.py --selftest

Creator Hub computes its own results; use this to double-check a result you copied, or to read a test run by hand. Platform rules from
Roblox/roblox-kb/ab-testing-and-experiments.md (Roblox DevForum 2026-10, live-check): wait for the full duration and daily results, do not decide from the first 24 hours
(early harm detection is a stop signal only: critical harm when the WHOLE confidence interval is below playtime -10 percent, ARPU -20 percent or payer conversion -20 percent),
harm decisions need at least 10,000 enrolled players, restart if sample-ratio mismatch is flagged. Indie heuristic (GameMakers, labelled): about 80 percent confidence with no
negative signals can be worth rolling out. Here: z test for two proportions (normal approximation), SRM by chi-square (1 d.f., p < 0.001 flags), exit 0 always except bad input.
"""
import argparse
import math
import sys

HARM = {"playtime": -10.0, "arpu": -20.0, "conversion": -20.0, "payer": -20.0}


def ztest(an, ax, bn, bx):
    p1, p2 = ax / an, bx / bn
    p = (ax + bx) / (an + bn)
    se0 = math.sqrt(p * (1 - p) * (1 / an + 1 / bn))
    z = (p2 - p1) / se0 if se0 else 0.0
    pv = math.erfc(abs(z) / math.sqrt(2))
    se = math.sqrt(p1 * (1 - p1) / an + p2 * (1 - p2) / bn)
    return p1, p2, z, pv, (p2 - p1 - 1.96 * se, p2 - p1 + 1.96 * se)


def srm(an, bn, split_b=50.0):
    n = an + bn
    ea, eb = n * (1 - split_b / 100.0), n * split_b / 100.0
    chi = (an - ea) ** 2 / ea + (bn - eb) ** 2 / eb
    return chi, math.erfc(math.sqrt(chi / 2.0))  # p for chi-square with 1 d.f.


def read(an, ax, bn, bx, guards=(), days=None, planned=None, split=50.0):
    notes, verdict = [], None
    p1, p2, z, pv, ci = ztest(an, ax, bn, bx)
    chi, srm_p = srm(an, bn, split)
    if srm_p < 0.001:
        notes.append("SRM: split %d/%d differs from %g/%g (p=%.4f): the assignment is broken, DO NOT trust the result; restart the experiment" % (an, bn, 100 - split, split, srm_p))
        verdict = "INVALID (sample ratio mismatch)"
    if an + bn < 10000:
        notes.append("only %d enrolled: under 10,000, the platform makes no harm decisions; treat the lift as a hint" % (an + bn))
    if days is not None and planned is not None and days < planned:
        notes.append("run %d of %d days: wait for the full duration and the daily results (novelty effects swing early)" % (days, planned))
    harm = []
    for g in guards:
        name, ch, lo, hi = g.split(":")
        lim = next((v for k, v in HARM.items() if k in name.lower()), None)
        if lim is not None and float(hi) < lim:
            harm.append("%s: whole CI (%s..%s%%) below the %g%% critical-harm line" % (name, lo, hi, lim))
        elif float(ch) < 0 and float(hi) < 0:
            notes.append("guardrail %s fell %s%% with CI entirely below zero: a real cost, weigh it" % (name, ch))
    if verdict is None:
        if harm:
            verdict = "STOP: critical harm on a guardrail"
        elif pv < 0.05 and ci[0] > 0:
            verdict = "WIN at 95%% confidence (+%.2f pts, CI %+.2f..%+.2f)" % ((p2 - p1) * 100, ci[0] * 100, ci[1] * 100)
        elif pv < 0.05 and ci[1] < 0:
            verdict = "LOSS at 95%% confidence (%.2f pts)" % ((p2 - p1) * 100)
        elif pv < 0.20 and ci[0] > -0.001:
            verdict = "LEAN POSITIVE (~%.0f%% confidence): indie heuristic says ~80%% with no negative signals can be worth rolling out; your call, with a rollback" % (100 * (1 - pv))
        else:
            verdict = "NO DETECTABLE DIFFERENCE (p=%.3f): not proof of no effect; the test may be underpowered" % pv
    return dict(a=p1 * 100, b=p2 * 100, diff=(p2 - p1) * 100, rel=(100 * (p2 - p1) / p1 if p1 else None), z=z, p=pv, ci_pts=(ci[0] * 100, ci[1] * 100), srm_p=srm_p, harm=harm, notes=notes, verdict=verdict)


def selftest():
    r = read(6000, 720, 6000, 840)  # 12% vs 14%
    assert r["verdict"].startswith("WIN") and r["p"] < 0.01, r
    r = read(6000, 720, 6000, 725)
    assert r["verdict"].startswith("NO DETECTABLE"), r["verdict"]
    r = read(8000, 960, 4000, 520)  # 2:1 split but declared 50/50
    assert r["verdict"].startswith("INVALID"), r["verdict"]
    r = read(6000, 720, 6000, 840, guards=["playtime:-14:-18:-11"])
    assert r["verdict"].startswith("STOP"), r["verdict"]
    r = read(300, 36, 300, 45, days=3, planned=14)
    assert any("full duration" in n for n in r["notes"]) and any("10,000" in n for n in r["notes"])
    assert read(6000, 720, 6000, 790)["verdict"].startswith(("LEAN", "WIN", "NO"))
    print("selftest ok (6 checks)")


def main():
    ap = argparse.ArgumentParser()
    for k in ("a-n", "a-x", "b-n", "b-x"):
        ap.add_argument("--" + k, type=float)
    ap.add_argument("--guard", action="append", default=[])
    ap.add_argument("--duration-days", type=int)
    ap.add_argument("--planned-days", type=int)
    ap.add_argument("--split", type=float, default=50.0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if None in (a.a_n, a.a_x, a.b_n, a.b_x):
        ap.error("--a-n --a-x --b-n --b-x required")
    r = read(a.a_n, a.a_x, a.b_n, a.b_x, a.guard, a.duration_days, a.planned_days, a.split)
    print("control %.2f%%  treatment %.2f%%  diff %+.2f pts (%+.1f%% relative)  95%% CI [%+.2f, %+.2f] pts  z=%.2f p=%.4f  SRM p=%.4f" % (
        r["a"], r["b"], r["diff"], r["rel"] or 0, r["ci_pts"][0], r["ci_pts"][1], r["z"], r["p"], r["srm_p"]))
    print("VERDICT:", r["verdict"])
    for h in r["harm"] + r["notes"]:
        print("-", h)
    return 0


if __name__ == "__main__":
    sys.exit(main())
