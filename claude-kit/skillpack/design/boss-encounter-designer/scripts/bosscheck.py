#!/usr/bin/env python3
"""bosscheck.py - fairness and length check for a boss / wave encounter spec. Stdlib only.

  python bosscheck.py boss.json
  python bosscheck.py --selftest

Spec: {"hp": 5000, "player_dps": 60, "reward_on_clear": true, "practice_available": true,
       "phases":[{"name":"a","attacks":[{"name":"slam","windup_s":0.8,"damage_pct":30,"avoidable":true}]}]}
Time to kill = hp / player_dps. Vault (combat-and-gameplay-systems, genre-mechanics): split attacks into anticipation/contact/recovery, exaggerated
wind-ups and clear telegraphs, keep boss fights longer than a minute or two, not tickle damage, the first boss must teach and not be cheesable by running,
practice must be viable. Flags: TTK under 60 s or over 600 s, windup under 0.5 s, a single hit over 50 percent of player hp, an unavoidable attack, fewer
than 2 phases, no practice, no reward. The 0.5 s / 50 percent / 600 s numbers are THIS SKILL'S DEFAULTS (the vault gives only "longer than a minute or
two"); a playtest overrides them.
"""
import json
import sys


def analyse(s):
    fl = []
    ttk = s["hp"] / s["player_dps"] if s.get("player_dps") else 0
    if ttk < 60:
        fl.append("time to kill %.0f s is under 60 s: too short to teach or feel big" % ttk)
    if ttk > 600:
        fl.append("time to kill %.0f s is over 600 s: likely padding" % ttk)
    if len(s.get("phases", [])) < 2:
        fl.append("fewer than 2 phases: no change of pattern")
    for ph in s.get("phases", []):
        for a in ph.get("attacks", []):
            if a.get("windup_s", 0) < 0.5:
                fl.append("%s/%s: windup %.2f s is too short to read" % (ph["name"], a["name"], a.get("windup_s", 0)))
            if a.get("damage_pct", 0) > 50:
                fl.append("%s/%s: one hit takes %d percent of player hp" % (ph["name"], a["name"], a["damage_pct"]))
            if not a.get("avoidable", False):
                fl.append("%s/%s: not avoidable" % (ph["name"], a["name"]))
    if not s.get("practice_available"):
        fl.append("no practice route")
    if not s.get("reward_on_clear"):
        fl.append("no reward on clear")
    return fl


def selftest():
    good = dict(hp=5000, player_dps=60, reward_on_clear=True, practice_available=True,
                phases=[dict(name="p1", attacks=[dict(name="slam", windup_s=0.8, damage_pct=30, avoidable=True)]),
                        dict(name="p2", attacks=[dict(name="sweep", windup_s=0.6, damage_pct=25, avoidable=True)])])
    assert analyse(good) == []
    bad = json.loads(json.dumps(good))
    bad["hp"] = 100
    bad["phases"][0]["attacks"][0].update(windup_s=0.2, damage_pct=80, avoidable=False)
    bad["practice_available"] = False
    f = analyse(bad)
    assert len(f) == 5 and any("under 60" in x for x in f) and any("not avoidable" in x for x in f), f
    assert any("fewer than 2" in x for x in analyse(dict(good, phases=good["phases"][:1])))
    assert any("over 600" in x for x in analyse(dict(good, hp=60000)))
    print("selftest ok (5 checks)")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    fl = analyse(json.load(open(sys.argv[1], encoding="utf-8")))
    for x in fl:
        print("FLAG", x)
    print("OK" if not fl else "%d flag(s)" % len(fl))
    sys.exit(1 if fl else 0)


if __name__ == "__main__":
    main()
