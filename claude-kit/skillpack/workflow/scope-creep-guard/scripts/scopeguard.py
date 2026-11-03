#!/usr/bin/env python3
"""scopeguard.py - enforce the swap rule on a frozen scope. Stdlib only.

  python scopeguard.py scope.csv
  python scopeguard.py --selftest

CSV columns: item,status,days,swap_for     status: frozen | added | swapped_out | done
Rule: nothing enters a frozen scope for free. Every `added` item must name in swap_for a `frozen` or `swapped_out` item of at least
equal days that leaves the scope (status swapped_out), unless the item is a bug fix marked status `fix`. The sum of `added` days
may not exceed the sum of `swapped_out` days, and the live total (frozen + added + done) may not exceed the original frozen
total. Each swapped_out item can pay for only one added item. Exit 0 pass, 1 fail; the message names the item to cut.
"""
import csv
import io
import sys


def check(rows):
    errs = []
    by = {r["item"]: r for r in rows}
    frozen_total = sum(float(r["days"]) for r in rows if r["status"] in ("frozen", "swapped_out", "done"))
    live = sum(float(r["days"]) for r in rows if r["status"] in ("frozen", "added", "done", "fix"))
    used = {}
    for r in rows:
        if r["status"] != "added":
            continue
        sw = (r.get("swap_for") or "").strip()
        if not sw:
            errs.append("%s: added with no swap_for (name the item that leaves)" % r["item"])
            continue
        t = by.get(sw)
        if not t or t["status"] != "swapped_out":
            errs.append("%s: swap_for %r is not a swapped_out item" % (r["item"], sw))
            continue
        if sw in used:
            errs.append("%s: %r already pays for %s" % (r["item"], sw, used[sw]))
        used[sw] = r["item"]
        if float(t["days"]) < float(r["days"]):
            errs.append("%s: needs %.1f days but %r frees only %.1f" % (r["item"], float(r["days"]), sw, float(t["days"])))
    if live > frozen_total + 1e-9:
        errs.append("live scope %.1f days > frozen %.1f days: cut %.1f" % (live, frozen_total, live - frozen_total))
    return errs


def selftest():
    ok = "item,status,days,swap_for\nloop,frozen,3,\nshop,frozen,2,\npets,swapped_out,2,\negg-anim,added,2,pets\n"
    assert check(list(csv.DictReader(io.StringIO(ok)))) == []
    free = ok.replace("egg-anim,added,2,pets", "egg-anim,added,2,")
    assert any("no swap_for" in e for e in check(list(csv.DictReader(io.StringIO(free)))))
    big = ok.replace("egg-anim,added,2,pets", "egg-anim,added,3,pets")
    assert any("frees only" in e for e in check(list(csv.DictReader(io.StringIO(big)))))
    two = ok + "trail,added,1,pets\n"
    e = check(list(csv.DictReader(io.StringIO(two))))
    assert any("already pays" in x for x in e), e
    wrong = ok.replace("pets,swapped_out", "pets,frozen")
    assert any("not a swapped_out" in e for e in check(list(csv.DictReader(io.StringIO(wrong)))))
    print("selftest ok (5 cases)")
    return 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv:
        print(__doc__)
        return 1
    with open(argv[0], encoding="utf-8", newline="") as f:
        errs = check(list(csv.DictReader(f)))
    for e in errs:
        print("FAIL:", e)
    print("PASS" if not errs else "FAIL (%d)" % len(errs))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
