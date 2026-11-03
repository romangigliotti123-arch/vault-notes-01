#!/usr/bin/env python3
"""seasons.py - draft a year of content slots around holidays and your own cadence. Stdlib only.

  python seasons.py --year 2027 [--hemisphere north] [--majors 4] [--skip valentines,earth-day] [--own "Anniversary:07-15"]
  python seasons.py --selftest

Holiday dates are computed (Easter by the Gregorian algorithm, Thanksgiving = 4th Thursday of November); other dates are fixed calendar dates.
Per the vault (updates-live-ops.md): release a holiday update about a week before the holiday, ship about 60 percent of the content in week one and 40 percent over
the next three weeks, keep scenery 1-2 weeks past the event for late returners (events-and-seasonal-content.md), seasons run about 3 months, a major
update about every quarter, announcements at least 3 days apart, launch on Fridays. Event length 7-30 days performs best for featuring (official). Check
your audience actually cares about a holiday (vault) and that holidays differ by country: this list is a NORTHERN-HEMISPHERE, Western default; replace it.
Flags: a slot closer than 21 days to a major update is marked CLASH; slots are shifted to the Friday on or before the target.
"""
import argparse
import datetime
import sys

HOLIDAYS = [  # key, label, month, day (None = computed)
    ("new-year", "New Year", 1, 1), ("valentines", "Valentine's", 2, 14), ("easter", "Easter / spring egg hunt", None, None),
    ("earth-day", "Earth Day", 4, 22), ("summer", "Summer start", 6, 21), ("back-to-school", "Back to school", 8, 25),
    ("halloween", "Halloween", 10, 31), ("thanksgiving", "Thanksgiving / harvest", None, None), ("winter", "Winter holidays", 12, 25),
]


def easter(y):
    a, b, c = y % 19, y // 100, y % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mo = (h + l - 7 * m + 114) // 31
    return datetime.date(y, mo, ((h + l - 7 * m + 114) % 31) + 1)


def thanksgiving(y):
    d = datetime.date(y, 11, 1)
    d += datetime.timedelta(days=(3 - d.weekday()) % 7)
    return d + datetime.timedelta(days=21)


def friday_on_or_before(d):
    return d - datetime.timedelta(days=(d.weekday() - 4) % 7)


def build(year, majors=4, skip=(), own=(), hemisphere="north"):
    slots = []
    for key, label, m, d in HOLIDAYS:
        if key in skip:
            continue
        date = easter(year) if key == "easter" else thanksgiving(year) if key == "thanksgiving" else datetime.date(year, m, d)
        if hemisphere == "south" and key in ("summer", "winter"):
            date = datetime.date(year, 12 if key == "summer" else 6, 21)
        launch = friday_on_or_before(date - datetime.timedelta(days=7))
        slots.append(dict(kind="seasonal", label=label, holiday=date, launch=launch, week1=60, rest=40, scenery_until=date + datetime.timedelta(days=10), announce=launch - datetime.timedelta(days=5)))
    for lab in own:
        name, _, md = lab.rpartition(":")
        mo, dy = (int(x) for x in md.split("-"))
        date = datetime.date(year, mo, dy)
        launch = friday_on_or_before(date - datetime.timedelta(days=7))
        slots.append(dict(kind="own", label=name, holiday=date, launch=launch, week1=60, rest=40, scenery_until=date + datetime.timedelta(days=10), announce=launch - datetime.timedelta(days=5)))
    gap = 365 // majors
    for i in range(majors):
        day = datetime.date(year, 1, 1) + datetime.timedelta(days=gap * i + gap // 2)
        launch = friday_on_or_before(day)
        slots.append(dict(kind="MAJOR", label="Major update %d" % (i + 1), holiday=None, launch=launch, announce=launch - datetime.timedelta(days=7)))
    slots.sort(key=lambda s: s["launch"])
    majors_l = [s["launch"] for s in slots if s["kind"] == "MAJOR"]
    for s in slots:
        s["clash"] = s["kind"] != "MAJOR" and any(abs((s["launch"] - m).days) < 21 for m in majors_l)
    prev = None
    for s in slots:  # announcements at least 3 days apart
        if prev and (s["announce"] - prev).days < 3:
            s["announce"] = prev + datetime.timedelta(days=3)
        prev = s["announce"]
    return slots


def selftest():
    assert easter(2026) == datetime.date(2026, 4, 5), easter(2026)
    assert easter(2027) == datetime.date(2027, 3, 28), easter(2027)
    assert thanksgiving(2026) == datetime.date(2026, 11, 26), thanksgiving(2026)
    s = build(2027, 4)
    assert all(x["launch"].weekday() == 4 for x in s)
    h = [x for x in s if x["label"] == "Halloween"][0]
    assert (h["holiday"] - h["launch"]).days in range(7, 14)
    assert sum(1 for x in s if x["kind"] == "MAJOR") == 4
    assert all((b["announce"] - a["announce"]).days >= 3 for a, b in zip(s, s[1:]))
    assert not [x for x in build(2027, 4, skip=("halloween",)) if x["label"] == "Halloween"]
    assert any(x["label"] == "Anniversary" for x in build(2027, 4, own=("Anniversary:07-15",)))
    print("selftest ok (8 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=datetime.date.today().year + 1)
    ap.add_argument("--hemisphere", default="north", choices=["north", "south"])
    ap.add_argument("--majors", type=int, default=4)
    ap.add_argument("--skip", default="")
    ap.add_argument("--own", action="append", default=[])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    for s in build(a.year, a.majors, [x for x in a.skip.split(",") if x], a.own, a.hemisphere):
        extra = "" if s["kind"] == "MAJOR" else "  holiday %s, 60%% week 1 / 40%% next 3 weeks, keep scenery to %s%s" % (s["holiday"], s["scenery_until"], "  CLASH: within 21 days of a major" if s["clash"] else "")
        print("%s  %-8s %-26s announce %s%s" % (s["launch"], s["kind"], s["label"], s["announce"], extra))
    return 0


if __name__ == "__main__":
    sys.exit(main())
