#!/usr/bin/env python3
"""cadence.py - turn team capacity into a realistic update calendar (minor cadence drops + periodic major updates). Stdlib only.

  python cadence.py --team 2 --start 2026-11-09 [--weeks 12] [--minor-days 4] [--major-days 30] [--days-per-week 4] [--major-every 10]
  python cadence.py --selftest

Rules used (Roblox/roblox-kb/updates-live-ops.md): ship cadence drops on existing systems, each under about 3 weeks of effort; weekly is the
ideal and monthly the floor; major updates about quarterly (here every N weeks, default 10 = a 2-3 month gap); launch on Friday with the dev cutoff
Wednesday night; announcements at least 3 days apart. Team capacity and the effort estimates are YOUR inputs; the split of capacity between cadence work
(60 percent) and major-update work (40 percent) is this skill's default, not a sourced rule.
"""
import argparse
import datetime
import math
import sys

CAD_SHARE = 0.6


def next_friday(d):
    return d + datetime.timedelta(days=(4 - d.weekday()) % 7)


def plan(team, start, weeks, minor_days, major_days, dpw, major_every):
    cap = team * dpw  # person-days per week
    cad_cap = cap * CAD_SHARE
    # weeks of cadence capacity needed per minor drop -> interval between drops, rounded up to 1, 2 or 4 weeks (4 = the monthly floor)
    need = minor_days / cad_cap
    interval = 1 if need <= 1 else 2 if need <= 2 else 4 if need <= 4 else None
    maj_cap = cap * (1 - CAD_SHARE) * major_every
    major_fits = major_days <= maj_cap
    notes = []
    if interval is None:
        notes.append("Minor drops need %.1f weeks of cadence capacity each: below the monthly floor. Cut scope or add people." % need)
    if minor_days / dpw > 15:
        notes.append("A minor drop is over 3 weeks of effort; vault rule is under three weeks.")
    if not major_fits:
        notes.append("Major update needs %d person-days but %d weeks of the major share gives %.0f: lengthen major_every or cut scope." % (major_days, major_every, maj_cap))
    first = next_friday(start)
    slots, w = [], 0
    while w < weeks:
        d = first + datetime.timedelta(weeks=w)
        major = (w + 1) % major_every == 0 and w > 0
        if major or (interval and w % interval == 0):
            slots.append(dict(date=d, kind="MAJOR" if major else "minor", cutoff=d - datetime.timedelta(days=2), announce=d - datetime.timedelta(days=7 if major else 3)))
        w += 1
    # announcements at least 3 days apart
    for a, b in zip(slots, slots[1:]):
        if (b["announce"] - a["announce"]).days < 3:
            b["announce"] = a["announce"] + datetime.timedelta(days=3)
    return dict(capacity_pd_week=cap, interval=interval, slots=slots, notes=notes, need=need)


def show(r):
    print("capacity %.0f person-days/week; cadence interval: %s" % (r["capacity_pd_week"], ("every %d week(s)" % r["interval"]) if r["interval"] else "NOT SUSTAINABLE"))
    for s in r["slots"]:
        print("%s  %-5s  dev cutoff %s (Wed)  announce %s" % (s["date"], s["kind"], s["cutoff"], s["announce"]))
    for n in r["notes"]:
        print("NOTE:", n)


def selftest():
    s = datetime.date(2026, 11, 9)
    r = plan(2, s, 12, 4, 30, 4, 10)  # cap 8, cad_cap 4.8, need .83 -> weekly
    assert r["interval"] == 1, r
    assert r["slots"][0]["date"] == datetime.date(2026, 11, 13) and r["slots"][0]["date"].weekday() == 4
    assert sum(1 for x in r["slots"] if x["kind"] == "MAJOR") == 1
    assert all((b["announce"] - a["announce"]).days >= 3 for a, b in zip(r["slots"], r["slots"][1:]))
    r2 = plan(1, s, 12, 12, 30, 4, 10)  # cap 4, cad 2.4, need 5 -> unsustainable
    assert r2["interval"] is None and r2["notes"]
    r3 = plan(2, s, 8, 8, 20, 4, 8)  # cap 8, cad 4.8, need 1.67 -> every 2 weeks
    assert r3["interval"] == 2
    assert not plan(2, s, 12, 4, 200, 4, 10)["notes"] == []
    print("selftest ok (5 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--team", type=float, default=1)
    ap.add_argument("--start", default=datetime.date.today().isoformat())
    ap.add_argument("--weeks", type=int, default=12)
    ap.add_argument("--minor-days", type=float, default=4)
    ap.add_argument("--major-days", type=float, default=30)
    ap.add_argument("--days-per-week", type=float, default=4)
    ap.add_argument("--major-every", type=int, default=10)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    show(plan(a.team, datetime.date.fromisoformat(a.start), a.weeks, a.minor_days, a.major_days, a.days_per_week, a.major_every))
    return 0


if __name__ == "__main__":
    sys.exit(main())
