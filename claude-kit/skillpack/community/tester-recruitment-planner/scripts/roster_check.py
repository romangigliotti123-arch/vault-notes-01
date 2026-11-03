#!/usr/bin/env python3
"""roster_check.py - check a playtester roster for coverage and bias. Stdlib only.

  python roster_check.py roster.csv [--min 8 --max 10 --new-share 0.3 --source-cap 0.6]
  python roster_check.py --selftest

CSV columns: handle, platform (pc/mobile/console/tablet), experience (new/regular/veteran), source (where you found them).
Store handles only: no ages, names, schools or contact details. Contact adults/consenting players in public or ticket channels, never DM minors.
Checks:
  dupes     FAIL  the same handle twice
  size      FAIL  fewer than --min (vault: a core group of 8-10), WARN above --max
  platform  WARN  no mobile or no second platform (test where players are)
  newbies   WARN  new-player share below --new-share (veterans hide onboarding problems; design default, not a vault number)
  source    WARN  one source supplies more than --source-cap of the roster (friends-only feedback is biased; weight by source)
Exit 1 on FAIL.
"""
import argparse
import csv
import sys
from collections import Counter


def check(rows, mn=8, mx=10, new_share=0.3, cap=0.6):
    n = len(rows)
    out = []
    h = Counter((r.get("handle") or "").strip().lower() for r in rows)
    d = [k for k, v in h.items() if v > 1]
    out.append(("dupes", "FAIL" if d else "PASS", ", ".join(d) if d else "unique handles"))
    out.append(("size", "FAIL" if n < mn else ("WARN" if n > mx else "PASS"), "%d testers (core %d-%d)" % (n, mn, mx)))
    plats = {(r.get("platform") or "").strip().lower() for r in rows} - {""}
    bad = "mobile" not in plats or len(plats) < 2
    out.append(("platform", "WARN" if bad else "PASS", "platforms: " + (", ".join(sorted(plats)) or "none")))
    nw = sum(1 for r in rows if (r.get("experience") or "").strip().lower() == "new") / n if n else 0
    out.append(("newbies", "WARN" if nw < new_share else "PASS", "%.0f%% new players" % (nw * 100)))
    src = Counter((r.get("source") or "").strip().lower() for r in rows)
    top, c = (src.most_common(1) or [("", 0)])[0]
    out.append(("source", "WARN" if n and c / n > cap else "PASS", "top source %r = %.0f%%" % (top, 100 * c / n if n else 0)))
    return out


def selftest():
    def mk(i, plat="pc", exp="regular", src="discord"):
        return {"handle": "p%d" % i, "platform": plat, "experience": exp, "source": src}

    good = [mk(1, "mobile", "new", "discord"), mk(2, "mobile", "new", "youtube"), mk(3, "pc", "new", "group"), mk(4, "console", "regular", "discord"),
            mk(5, "pc", "regular", "group"), mk(6, "mobile", "veteran", "youtube"), mk(7, "pc", "veteran", "discord"), mk(8, "tablet", "regular", "group")]
    r = lambda rows, **k: {n: s for n, s, m in check(rows, **k)}
    assert all(v == "PASS" for v in r(good).values()), check(good)
    assert r(good[:5])["size"] == "FAIL"
    assert r(good + [mk(9), mk(10), mk(11)])["size"] == "WARN"
    assert r(good + [mk(1)])["dupes"] == "FAIL"
    assert r([mk(i, "pc") for i in range(8)])["platform"] == "WARN"
    assert r([mk(i, "mobile" if i % 2 else "pc", "veteran") for i in range(8)])["newbies"] == "WARN"
    assert r([mk(i, "mobile" if i % 2 else "pc", "new", "friends") for i in range(8)])["source"] == "WARN"
    print("selftest ok (7 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--min", type=int, default=8)
    ap.add_argument("--max", type=int, default=10)
    ap.add_argument("--new-share", type=float, default=0.3)
    ap.add_argument("--source-cap", type=float, default=0.6)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv:
        ap.error("give the roster csv")
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        res = check(list(csv.DictReader(f)), a.min, a.max, a.new_share, a.source_cap)
    for n, s, m in res:
        print("%-4s %-9s %s" % (s, n, m))
    return 1 if any(s == "FAIL" for n, s, m in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
