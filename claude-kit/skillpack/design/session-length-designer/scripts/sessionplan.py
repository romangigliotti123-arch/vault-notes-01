#!/usr/bin/env python3
"""sessionplan.py - check a planned session timeline for reward gaps, stop points and return hooks. Stdlib only.

  python sessionplan.py plan.csv [--target 12]      columns: minute,beat,kind     kind = reward|goal|decision|stop|hook|social|paywall
  python sessionplan.py --selftest

Flags: any gap of more than 3 minutes between reward/goal beats, no 'stop' beat, no 'hook' (reason to return) at or after the last stop, first reward
later than minute 1, a 'paywall' at or before the first reward, a plan that ends more than 2 minutes short of the target. Vault (retention-d1-d7,
first-session-onboarding): hooked within about 5 minutes, playtime rewards at about 10/30/60 minutes (official suggestion), a reward or number jump
every few minutes, finish with a moment of joy and a reason to return. The 3-minute gap and 2-minute tolerance are THIS SKILL'S DEFAULTS. The target
length is a goal, measured later with session-length-analyzer.
"""
import csv
import sys


def analyse(beats, target):
    fl = []
    bs = sorted(beats, key=lambda b: float(b["minute"]))
    pay = [b for b in bs if b["kind"] == "paywall"]
    rew = [b for b in bs if b["kind"] in ("reward", "goal")]
    if not rew:
        return ["no reward or goal beats at all"]
    if float(rew[0]["minute"]) > 1:
        fl.append("first reward at minute %s, later than minute 1" % rew[0]["minute"])
    if pay and float(pay[0]["minute"]) <= float(rew[0]["minute"]):
        fl.append("paywall at minute %s comes before the first reward" % pay[0]["minute"])
    for a, b in zip(rew, rew[1:]):
        gap = float(b["minute"]) - float(a["minute"])
        if gap > 3:
            fl.append("%.1f min with no reward or goal between minute %s and %s" % (gap, a["minute"], b["minute"]))
    stops = [b for b in bs if b["kind"] == "stop"]
    hooks = [b for b in bs if b["kind"] == "hook"]
    if not stops:
        fl.append("no natural stop point planned")
    if not hooks:
        fl.append("no return hook planned")
    elif stops and float(hooks[-1]["minute"]) < float(stops[-1]["minute"]):
        fl.append("last return hook (minute %s) comes before the last stop (minute %s)" % (hooks[-1]["minute"], stops[-1]["minute"]))
    if float(bs[-1]["minute"]) < target - 2:
        fl.append("plan ends at minute %s, more than 2 min short of the %s min target" % (bs[-1]["minute"], target))
    return fl


def selftest():
    B = lambda m, k: dict(minute=m, beat="x", kind=k)
    good = [B(0.5, "reward"), B(2, "goal"), B(4, "reward"), B(6, "reward"), B(8, "decision"), B(9, "reward"), B(11, "stop"), B(11.5, "hook")]
    assert analyse(good, 12) == []
    assert any("later than minute 1" in x for x in analyse([B(2, "reward"), B(3, "stop"), B(3, "hook")], 3))
    assert any("with no reward" in x for x in analyse([B(0.5, "reward"), B(6, "reward"), B(7, "stop"), B(7, "hook")], 7))
    assert any("no natural stop" in x for x in analyse([B(0.5, "reward"), B(2, "hook")], 2))
    assert any("no return hook" in x for x in analyse([B(0.5, "reward"), B(2, "stop")], 2))
    assert any("before the first reward" in x for x in analyse([B(0.2, "paywall"), B(0.5, "reward"), B(2, "stop"), B(2, "hook")], 2))
    assert any("short of" in x for x in analyse([B(0.5, "reward"), B(2, "stop"), B(2, "hook")], 12))
    print("selftest ok (7 checks)")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    tg = float(sys.argv[sys.argv.index("--target") + 1]) if "--target" in sys.argv else 12.0
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        fl = analyse(list(csv.DictReader(f)), tg)
    for x in fl:
        print("FLAG", x)
    print("OK" if not fl else "%d flag(s)" % len(fl))
    sys.exit(1 if fl else 0)


if __name__ == "__main__":
    main()
