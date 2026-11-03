#!/usr/bin/env python3
"""rewardsched.py - check a drop table and pity rule; simulate opens. Stdlib only.

  python rewardsched.py --table "common:70,rare:25,epic:4,legendary:1" --pity legendary:60 [--sims 20000]
  python rewardsched.py --selftest

Reports: odds sum, mean and 99th-percentile opens to the target tier with and without pity, and flags. Vault (player-psychology-and-game-feel,
core-loops): vary reward size/rarity/timing but show the odds; a visible pity counter is trusted more than a hidden one; keep skill and a free path in the
loop. The 'p99 over 3x the one-in-N expectation' flag and the 100-percent sum rule are THIS SKILL'S DEFAULTS. This is design math, not legal advice:
paid-randomness rules are regional and change; live-check age-ratings-moderation-and-tos before any paid random item.
"""
import argparse
import random
import sys


def parse_table(s):
    t = []
    for part in s.split(","):
        k, v = part.split(":")
        t.append((k.strip(), float(v)))
    return t


def pick(table, rng):
    x = rng.random() * sum(w for _, w in table)
    for k, w in table:
        x -= w
        if x < 0:
            return k
    return table[-1][0]


def opens_until(table, target, pity, rng, cap=100000):
    n = 0
    while n < cap:
        n += 1
        if pick(table, rng) == target:
            return n
        if pity and pity[0] == target and n >= pity[1]:
            return n
    return cap


def simulate(table, target, pity, sims, seed=1):
    rng = random.Random(seed)
    xs = sorted(opens_until(table, target, pity, rng) for _ in range(sims))
    return dict(mean=sum(xs) / sims, p50=xs[sims // 2], p99=xs[max(int(sims * 0.99) - 1, 0)], max=xs[-1])


def analyse(table, target, pity, sims):
    errs = []
    tot = sum(w for _, w in table)
    if abs(tot - 100) > 0.01:
        errs.append("odds sum to %.2f, expected 100 (state odds as percent)" % tot)
    if target not in dict(table):
        errs.append("target tier %r not in table" % target)
        return errs, None, None
    plain = simulate(table, target, None, sims)
    withp = simulate(table, target, pity, sims) if pity else None
    expect = tot / dict(table)[target]
    if not pity and plain["p99"] > 3 * expect:
        errs.append("no pity: 1 in 100 players needs %d opens (%.1fx the average): add a visible pity cap" % (plain["p99"], plain["p99"] / plain["mean"]))
    return errs, plain, withp


def selftest():
    t = parse_table("common:70,rare:25,epic:4,legendary:1")
    assert abs(sum(w for _, w in t) - 100) < 1e-9
    errs, plain, withp = analyse(t, "legendary", ("legendary", 60), 5000)
    assert 80 < plain["mean"] < 125, plain
    assert withp["max"] <= 60 and withp["mean"] < plain["mean"], withp
    errs2, _, _ = analyse(t, "legendary", None, 5000)
    assert any("no pity" in e for e in errs2)
    errs3, _, _ = analyse(parse_table("a:50,b:40"), "a", None, 100)
    assert any("sum to" in e for e in errs3)
    assert analyse(t, "mythic", None, 10)[0][0].startswith("target")
    print("selftest ok (6 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--table")
    ap.add_argument("--target", default=None, help="tier to measure (default: last tier)")
    ap.add_argument("--pity", default=None, help="tier:N guaranteed after N opens")
    ap.add_argument("--sims", type=int, default=20000)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    t = parse_table(a.table)
    target = a.target or t[-1][0]
    pity = None
    if a.pity:
        k, n = a.pity.split(":")
        pity = (k, int(n))
    errs, plain, withp = analyse(t, target, pity, a.sims)
    if plain:
        print("without pity: mean %.1f  median %d  p99 %d  max %d" % (plain["mean"], plain["p50"], plain["p99"], plain["max"]))
    if withp:
        print("with pity %s:%d: mean %.1f  median %d  p99 %d  max %d" % (pity[0], pity[1], withp["mean"], withp["p50"], withp["p99"], withp["max"]))
    for e in errs:
        print("FLAG", e)
    print("OK" if not errs else "%d flag(s)" % len(errs))
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
