#!/usr/bin/env python3
"""ladder_check.py - lint a community enforcement ladder (Discord, group or in-game). Stdlib only.

  python ladder_check.py ladder.csv [--severe threats,doxxing,grooming,account-selling,hate]
  python ladder_check.py --selftest

CSV columns: offence, first, repeat, decider, appeal (yes/no), evidence (yes/no), report_platform (yes/no).
first/repeat are one of: warn, timeout, kick, ban. decider is mod, dev or helper.
Checks:
  first-ban     a first offence is a ban for something not in the --severe list (ordinary offences start gentle)
  repeat        repeat is softer than first
  helper-ban    a helper/volunteer can decide a ban (vault: delegate moderation with escalation paths; harsh calls stay with trusted roles)
  evidence      a ban or kick without evidence=yes (screenshot or log kept)
  appeal        an ordinary offence without an appeal route
  severe-report a severe offence not marked report_platform=yes (threats, doxxing, grooming go to platform safety reporting, never only in-house)
  coverage      the ladder lacks any of: harassment, exploit, account-selling, spam
Exit 1 on FAIL. It lints the plan; the live platform policy is checked by the owner.
"""
import argparse
import csv
import sys

RANK = {"warn": 1, "timeout": 2, "kick": 3, "ban": 4}
SEVERE = "threats,doxxing,grooming,account-selling,hate"
NEED = ("harassment", "exploit", "account-selling", "spam")


def g(r, k):
    return (r.get(k) or "").strip().lower()


def check(rows, severe=SEVERE):
    sev = {s.strip().lower() for s in severe.split(",") if s.strip()}
    out = []

    def add(name, bad, okmsg):
        out.append((name, "FAIL" if bad else "PASS", ", ".join(bad) if bad else okmsg))

    add("first-ban", [g(r, "offence") for r in rows if g(r, "first") == "ban" and g(r, "offence") not in sev], "no ordinary first-offence bans")
    add("repeat", [g(r, "offence") for r in rows if RANK.get(g(r, "repeat"), 0) < RANK.get(g(r, "first"), 0)], "repeat is never softer than first")
    add("helper-ban", [g(r, "offence") for r in rows if g(r, "decider") == "helper" and "ban" in (g(r, "first"), g(r, "repeat"))], "helpers cannot ban")
    add("evidence", [g(r, "offence") for r in rows if (g(r, "first") in ("kick", "ban") or g(r, "repeat") in ("kick", "ban")) and g(r, "evidence") != "yes"], "bans and kicks keep evidence")
    add("appeal", [g(r, "offence") for r in rows if g(r, "offence") not in sev and g(r, "appeal") != "yes"], "ordinary offences have an appeal route")
    add("severe-report", [g(r, "offence") for r in rows if g(r, "offence") in sev and g(r, "report_platform") != "yes"], "severe offences go to platform reporting")
    have = {g(r, "offence") for r in rows}
    add("coverage", [n for n in NEED if n not in have], "core offences covered")
    return out


def selftest():
    good = [
        {"offence": "harassment", "first": "timeout", "repeat": "ban", "decider": "mod", "appeal": "yes", "evidence": "yes", "report_platform": "no"},
        {"offence": "exploit", "first": "warn", "repeat": "ban", "decider": "mod", "appeal": "yes", "evidence": "yes", "report_platform": "no"},
        {"offence": "account-selling", "first": "ban", "repeat": "ban", "decider": "dev", "appeal": "no", "evidence": "yes", "report_platform": "yes"},
        {"offence": "spam", "first": "warn", "repeat": "timeout", "decider": "helper", "appeal": "yes", "evidence": "no", "report_platform": "no"},
    ]

    def res(rows):
        return {n: s for n, s, m in check(rows)}

    assert all(s == "PASS" for s in res([dict(r) for r in good]).values()), check(good)

    def mut(i, k, v):
        b = [dict(r) for r in good]
        b[i][k] = v
        return res(b)

    assert mut(0, "first", "ban")["first-ban"] == "FAIL"
    assert mut(0, "repeat", "warn")["repeat"] == "FAIL"
    assert mut(1, "decider", "helper")["helper-ban"] == "FAIL"
    assert mut(1, "evidence", "no")["evidence"] == "FAIL"
    assert mut(0, "appeal", "no")["appeal"] == "FAIL"
    assert mut(2, "report_platform", "no")["severe-report"] == "FAIL"
    assert res(good[:2])["coverage"] == "FAIL"
    print("selftest ok (8 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--severe", default=SEVERE)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv:
        ap.error("give the ladder csv")
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        res = check(list(csv.DictReader(f)), a.severe)
    for n, s, m in res:
        print("%-4s %-14s %s" % (s, n, m))
    return 1 if any(s == "FAIL" for n, s, m in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
