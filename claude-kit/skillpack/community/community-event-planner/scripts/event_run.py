#!/usr/bin/env python3
"""event_run.py - date-stamped run sheet for a community event. Stdlib only.

  python event_run.py --date 2026-12-05 --hour 18 --title "Pet Parade" [--days-tease 10]
  python event_run.py --selftest

Prints the beats with real dates. Offsets follow the vault: tease early (about 10 days out), always give date AND time with a time zone
label, remind the day before, announce at start, recap after, and close the loop ("you said, we did") a week later.
It does not post anything; the owner posts. Exit 2 on a bad date.
"""
import argparse
import datetime as dt
import sys


def beats(day, hour, tease=10):
    start = dt.datetime.combine(day, dt.time(hour))
    plan = [
        (-tease, "Tease: image or hint + the date and time (state the time zone, e.g. UTC)"),
        (-3, "Reminder: what it is, how to join, the reward (small, no pay-to-win)"),
        (-1, "Last call + rules reminder + mod roster confirmed"),
        (0, "Go live: announce, link, mods online, one named host"),
        (1, "Recap: highlights, thanks, winners if any (handles the winners agreed to show)"),
        (7, "Close the loop: what we heard, what changes (you said, we did)"),
    ]
    return [((start + dt.timedelta(days=d)).strftime("%a %Y-%m-%d %H:%M"), d, what) for d, what in plan]


def selftest():
    b = beats(dt.date(2026, 12, 5), 18)
    assert b[0][0] == "Wed 2026-11-25 18:00", b[0]
    assert b[3][0] == "Sat 2026-12-05 18:00", b[3]
    assert b[-1][0] == "Sat 2026-12-12 18:00", b[-1]
    assert [x[1] for x in b] == [-10, -3, -1, 0, 1, 7]
    assert beats(dt.date(2026, 12, 5), 18, tease=5)[0][1] == -5
    print("selftest ok (5 asserts)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--hour", type=int, default=18)
    ap.add_argument("--title", default="Event")
    ap.add_argument("--days-tease", type=int, default=10)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    try:
        day = dt.date.fromisoformat(a.date or "")
    except ValueError:
        print("give --date YYYY-MM-DD")
        return 2
    print("Run sheet:", a.title)
    for when, d, what in beats(day, a.hour, a.days_tease):
        print("%s  (T%+d)  %s" % (when, d, what))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
