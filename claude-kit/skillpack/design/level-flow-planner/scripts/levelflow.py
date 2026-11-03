#!/usr/bin/env python3
"""levelflow.py - walking-time check for a planned map: points of interest, rest spots, longest empty stretch. Stdlib only.

  python levelflow.py points.csv [--speed 16]      columns: name,kind,x,z     kind = spawn|poi|rest|checkpoint|hazard|goal   (studs)
  python levelflow.py --selftest

Walks the points in file order. Roblox default WalkSpeed is 16 studs/s (live-check if you change it). Vault (core-loops-and-game-design,
building-and-level-design): keep points of interest within about 10 seconds' walk, offer fast travel after first exploration, use colour and light to
guide, start worlds small. Flags: any leg longer than 10 s (empty stretch), first point more than 10 s from spawn, no goal, and 3 hazards in a row with
more than 60 s of walking since the last rest/checkpoint. The 60 s and 3-hazard numbers are THIS SKILL'S DEFAULTS.
"""
import csv
import math
import sys


def legs(pts, speed):
    return [(a["name"], b["name"], math.hypot(float(b["x"]) - float(a["x"]), float(b["z"]) - float(a["z"])) / speed) for a, b in zip(pts, pts[1:])]


def analyse(pts, speed=16.0):
    fl = []
    if not pts or pts[0]["kind"] != "spawn":
        return ["first point must be the spawn"], []
    ls = legs(pts, speed)
    for a, b, t in ls:
        if t > 10:
            fl.append("%s -> %s is %.0f s of empty walking (> 10 s): add a landmark or shorten" % (a, b, t))
    if ls and ls[0][2] > 10:
        fl.append("first point of interest is %.0f s from spawn" % ls[0][2])
    if not any(p["kind"] == "goal" for p in pts):
        fl.append("no goal point")
    run, since_rest = 0, 0.0
    for i, p in enumerate(pts):
        if i > 0:
            since_rest += ls[i - 1][2]
        if p["kind"] in ("rest", "checkpoint"):
            run, since_rest = 0, 0.0
        elif p["kind"] == "hazard":
            run += 1
            if run >= 3 and since_rest > 60:
                fl.append("%d hazards and %.0f s since the last rest/checkpoint at %s" % (run, since_rest, p["name"]))
                run = 0
    return fl, ls


def selftest():
    P = lambda n, k, x, z: dict(name=n, kind=k, x=x, z=z)
    ok = [P("s", "spawn", 0, 0), P("a", "poi", 80, 0), P("h1", "hazard", 160, 0), P("c", "checkpoint", 240, 0), P("g", "goal", 320, 0)]
    assert analyse(ok)[0] == []
    far = [P("s", "spawn", 0, 0), P("a", "poi", 400, 0), P("g", "goal", 420, 0)]
    f = analyse(far)[0]
    assert any("empty walking" in x for x in f) and any("first point" in x for x in f)
    assert analyse([P("a", "poi", 0, 0)])[0] == ["first point must be the spawn"]
    assert any("no goal" in x for x in analyse([P("s", "spawn", 0, 0), P("a", "poi", 10, 0)])[0])
    hz = [P("s", "spawn", 0, 0)] + [P("h%d" % i, "hazard", 150 * (i + 1), 0) for i in range(8)] + [P("g", "goal", 1300, 0)]
    assert any("hazards" in x for x in analyse(hz, 16)[0])
    assert round(legs(ok, 16)[0][2], 1) == 5.0
    print("selftest ok (6 checks)")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sp = float(sys.argv[sys.argv.index("--speed") + 1]) if "--speed" in sys.argv else 16.0
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        pts = list(csv.DictReader(f))
    fl, ls = analyse(pts, sp)
    for a, b, t in ls:
        print("%-12s -> %-12s %5.1f s" % (a, b, t))
    for x in fl:
        print("FLAG", x)
    print("OK" if not fl else "%d flag(s)" % len(fl))
    sys.exit(1 if fl else 0)


if __name__ == "__main__":
    main()
