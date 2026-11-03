#!/usr/bin/env python3
"""progcurve.py - XP / unlock curve calculator: time-to-level table and early-win check. Stdlib only.

  python progcurve.py --levels 30 --base 20 --growth 1.35 --xp-per-min 60 [--xp-growth 1.12]
  python progcurve.py --selftest

xp_needed(L) = base * growth^(L-1). Income per minute at level L = xp_per_min * xp_growth^(L-1) (xp_growth 1.0 = flat income).
Vault (core-loops-and-game-design, onboarding docs): early levels take about a minute, something should unlock or a number jump every few minutes, the
long-term goal is visible early. The thresholds below (L1-L3 <= 1.5 min each, any level <= 20 min before level 10, no level more than 2.5x the previous
level's time) are THIS SKILL'S DEFAULTS, not vault numbers. Replace income with measured values after a playtest.
"""
import argparse
import sys


def table(levels, base, growth, xpm, xpg):
    rows, total = [], 0.0
    for lv in range(1, levels + 1):
        need = base * growth ** (lv - 1)
        inc = xpm * xpg ** (lv - 1)
        mins = need / inc
        total += mins
        rows.append((lv, need, inc, mins, total))
    return rows


def flags(rows):
    out = []
    for lv, need, inc, mins, total in rows:
        if lv <= 3 and mins > 1.5:
            out.append("L%d takes %.1f min: early levels should be about a minute" % (lv, mins))
        if 3 < lv < 10 and mins > 20:
            out.append("L%d takes %.1f min before level 10: grind wall" % (lv, mins))
        if lv > 1:
            prev = rows[lv - 2][3]
            if mins > 2.5 * prev and mins > 3:
                out.append("L%d (%.1f min) jumps %.1fx over L%d: spike" % (lv, mins, mins / prev, lv - 1))
    return out


def selftest():
    r = table(10, 20, 1.35, 60, 1.0)
    assert abs(r[0][3] - 20 / 60) < 1e-9 and r[1][1] == 27.0
    assert flags(r) == []
    assert any("L1 takes" in f for f in flags(table(5, 200, 1.2, 60, 1.0)))
    assert any("grind wall" in f for f in flags(table(10, 20, 2.0, 60, 1.0)))
    assert any("spike" in f for f in flags(table(6, 10, 3.5, 60, 1.0)))
    assert table(3, 10, 1.0, 10, 1.0)[2][4] == 3.0
    print("selftest ok (6 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", type=int, default=30)
    ap.add_argument("--base", type=float, default=20)
    ap.add_argument("--growth", type=float, default=1.35)
    ap.add_argument("--xp-per-min", type=float, default=60)
    ap.add_argument("--xp-growth", type=float, default=1.0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    rows = table(a.levels, a.base, a.growth, a.xp_per_min, a.xp_growth)
    print("level  xp_needed  xp/min  minutes  cumulative_min")
    for lv, need, inc, mins, tot in rows:
        print("%5d  %9.0f  %6.0f  %7.1f  %9.1f" % (lv, need, inc, mins, tot))
    fl = flags(rows)
    for f in fl:
        print("FLAG", f)
    print("OK" if not fl else "%d flag(s)" % len(fl))
    sys.exit(1 if fl else 0)


if __name__ == "__main__":
    main()
