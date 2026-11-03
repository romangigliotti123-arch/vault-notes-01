#!/usr/bin/env python3
"""calendar_gen.py - lay out marketing slots around release dates. Stdlib only. Writes a Markdown table you then fill with real posts.

  python calendar_gen.py month --start 2026-12-01 --release 2026-12-11 [--release 2026-12-25] [--event 2026-12-18] [--short-per-week 3]
  python calendar_gen.py launch --launch "2026-12-11 17:00" [--hours-before 24 --hours-after 48]
  python calendar_gen.py --selftest

Rules baked in (all from the vault, labelled; change the dates in the table, not the rules):
  * Friday release preferred, dev cutoff Wednesday, hype Wednesday, avoid Tuesday (updates-live-ops; indie, multiple creators).
    A release on another weekday is flagged, not blocked.
  * Tease from about 10 days before an event or update, in-game countdown 1-2 weeks, announce on release day, recap 2 days after
    (community-and-discord, updates-live-ops).
  * Short-form 2-3 times a week at least (trailers-and-video-marketing: #7Phantom). Number is a floor to start from, not a target to hit.
  * Always the Details Page URL in every post (trailers-and-video-marketing, RDC26 recap).
No post text is produced here: that is the user's voice (update-announcement-writer, short-video-planner).
"""
import argparse
import datetime as dt
import sys

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def d(s):
    return dt.date.fromisoformat(s)


def month(start, releases, events, per_week=3, weeks=4):
    rows = {}
    flags = []

    def add(day, kind, text):
        rows.setdefault(day, []).append((kind, text))

    for r in releases:
        add(r, "RELEASE", "update goes live (same time every release)")
        add(r - dt.timedelta(days=10), "tease", "first teaser: image/silhouette/hint")
        add(r - dt.timedelta(days=7), "countdown", "in-game countdown starts (1-2 weeks before)")
        add(r - dt.timedelta(days=2), "tease", "second teaser + ask players what they want next")
        add(r, "announce", "release-day post on Roblox group/Discord/X with the Details Page URL")
        add(r + dt.timedelta(days=2), "recap", "recap clip + thank testers; read first-48h numbers")
        if r.weekday() != 4:
            flags.append("%s is a %s: vault prefers Friday release (cutoff Wednesday); avoid Tuesday%s" % (r, DAYS[r.weekday()], " (Tuesday!)" if r.weekday() == 1 else ""))
        else:
            add(r - dt.timedelta(days=2), "cutoff", "dev cutoff Wednesday, hype post")
    for e in events:
        add(e, "EVENT", "event starts (UTC time fixed)")
        add(e - dt.timedelta(days=10), "tease", "event teaser from about 10 days before")
    end = start + dt.timedelta(weeks=weeks)
    day = start
    wk_slots = {0: [0, 2, 4], 1: [1, 3], 2: [0, 2, 4]}.get(per_week - 1, [0, 2, 4])
    while day < end:
        if day.weekday() in wk_slots[:per_week]:
            add(day, "short", "short-form clip (hook in the first 2 s, game name in caption)")
        day += dt.timedelta(days=1)
    lines = ["| date | day | slot | what |", "|---|---|---|---|"]
    for day in sorted(rows):
        if start <= day < end:
            for kind, text in rows[day]:
                lines.append("| %s | %s | %s | %s |" % (day, DAYS[day.weekday()], kind, text))
    outside = [(k, x) for k, v in rows.items() if not (start <= k < end) for x in v]
    if outside:
        flags.append("%d slot(s) fall outside the window %s..%s (move --start earlier to see them)" % (len(outside), start, end))
    return "\n".join(lines), flags


def launch(when, before=24, after=48):
    steps = [
        (-before, "freeze", "code freeze; final smoke test on a phone; thumbnails/icon/title/description final"),
        (-before + 1, "check", "page checks: genre set, Exclude from Recommendations OFF, access public, videos approved"),
        (-3, "prep", "support channels open, rollback plan, Discord announcement drafted with Details Page URL"),
        (-1, "warn", "heads-up post: launching in one hour"),
        (0, "LAUNCH", "publish at the fixed time; post the announcement; start ads only if the readiness gate passed"),
        (1, "watch", "CCU, error/crash reports, bounce; answer players"),
        (3, "watch", "first hotfix window; read first-play bounce and early D1 proxies"),
        (12, "post", "milestone/clip post if something went well"),
        (24, "read", "day-1 numbers: PTR, CTR per thumbnail, bounce; swap poor-CTR thumbnails on days 2-4"),
        (after, "recap", "recap post + decide next update"),
    ]
    out = ["| when | slot | what |", "|---|---|---|"]
    for h, k, t in steps:
        stamp = when + dt.timedelta(hours=h)
        out.append("| %s (%s) | %s | %s |" % (stamp.strftime("%Y-%m-%d %H:%M"), ("T%+dh" % h) if h else "T0", k, t))
    return "\n".join(out)


def selftest():
    tbl, flags = month(d("2026-12-01"), [d("2026-12-11")], [d("2026-12-18")])
    assert not flags, flags
    assert "| 2026-12-01 | Tue | tease |" in tbl and "RELEASE" in tbl and "EVENT" in tbl, tbl
    assert any("Friday" in f for f in month(d("2026-12-01"), [d("2026-12-08")], [])[1])
    assert any("Tuesday!" in f for f in month(d("2026-12-01"), [d("2026-12-08")], [])[1])
    t = launch(dt.datetime(2026, 12, 11, 17, 0))
    assert "2026-12-11 17:00 (T0)" in t and "2026-12-10 17:00 (T-24h)" in t, t
    print("selftest ok (5 assertions)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    m = sub.add_parser("month")
    m.add_argument("--start", required=True)
    m.add_argument("--release", action="append", default=[])
    m.add_argument("--event", action="append", default=[])
    m.add_argument("--short-per-week", type=int, default=3)
    m.add_argument("--weeks", type=int, default=4)
    la = sub.add_parser("launch")
    la.add_argument("--launch", required=True, help='"YYYY-MM-DD HH:MM" in the time zone you will read the table in')
    la.add_argument("--hours-before", type=int, default=24)
    la.add_argument("--hours-after", type=int, default=48)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if a.cmd == "month":
        tbl, flags = month(d(a.start), [d(x) for x in a.release], [d(x) for x in a.event], a.short_per_week, a.weeks)
        print(tbl)
        for f in flags:
            print("FLAG:", f)
        return 0
    if a.cmd == "launch":
        print(launch(dt.datetime.strptime(a.launch, "%Y-%m-%d %H:%M"), a.hours_before, a.hours_after))
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
