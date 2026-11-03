#!/usr/bin/env python3
"""proof_log.py - lint a social-proof log (quotes, clips, numbers) before it is used in marketing. Stdlib only.

  python proof_log.py proof.csv [--today 2026-11-02] [--stale-days 180]
  python proof_log.py --selftest

CSV columns: kind (quote/clip/number), text, source_url, permission (yes/public/no), date (YYYY-MM-DD), label (measured/self-reported).
Checks:
  source      FAIL  no source_url (an unsourced quote or number is invented)
  permission  FAIL  a quote or clip with permission=no or empty (ask first; credit the maker; public posts still need credit)
  label       FAIL  a number without label measured or self-reported
  stale       WARN  older than --stale-days (player counts and reviews age fast)
  minor       WARN  text contains a handle plus an age-like phrase ("i am 11"): do not publish personal details about players
Exit 1 on FAIL.
"""
import argparse
import csv
import datetime as dt
import re
import sys

MINOR = re.compile(r"\b(i am|i'm|im) \d{1,2}\b|\b\d{1,2} years? old\b", re.I)


def check(rows, today, stale=180):
    bad = {"source": [], "permission": [], "label": [], "stale": [], "minor": []}
    for i, r in enumerate(rows, 1):
        k = (r.get("kind") or "").strip().lower()
        tag = "#%d" % i
        if not (r.get("source_url") or "").strip():
            bad["source"].append(tag)
        if k in ("quote", "clip") and (r.get("permission") or "").strip().lower() not in ("yes", "public"):
            bad["permission"].append(tag)
        if k == "number" and (r.get("label") or "").strip().lower() not in ("measured", "self-reported"):
            bad["label"].append(tag)
        try:
            if (today - dt.date.fromisoformat((r.get("date") or "").strip())).days > stale:
                bad["stale"].append(tag)
        except ValueError:
            bad["stale"].append(tag + "(no date)")
        if MINOR.search(r.get("text") or ""):
            bad["minor"].append(tag)
    out = []
    for n in ("source", "permission", "label", "stale", "minor"):
        sev = "WARN" if n in ("stale", "minor") else "FAIL"
        out.append((n, sev if bad[n] else "PASS", ", ".join(bad[n]) or "ok"))
    return out


def selftest():
    today = dt.date(2026, 11, 2)
    ok = [
        {"kind": "quote", "text": "Best pet game", "source_url": "https://x/1", "permission": "yes", "date": "2026-10-01", "label": ""},
        {"kind": "number", "text": "50k visits", "source_url": "https://x/2", "permission": "", "date": "2026-10-20", "label": "measured"},
    ]
    r = lambda rows: {n: s for n, s, m in check(rows, today)}
    assert all(v == "PASS" for v in r(ok).values()), check(ok, today)
    b = [dict(x) for x in ok]; b[0]["source_url"] = ""; assert r(b)["source"] == "FAIL"
    b = [dict(x) for x in ok]; b[0]["permission"] = "no"; assert r(b)["permission"] == "FAIL"
    b = [dict(x) for x in ok]; b[1]["label"] = ""; assert r(b)["label"] == "FAIL"
    b = [dict(x) for x in ok]; b[0]["date"] = "2025-01-01"; assert r(b)["stale"] == "WARN"
    b = [dict(x) for x in ok]; b[0]["text"] = "I am 11 and love it"; assert r(b)["minor"] == "WARN"
    print("selftest ok (6 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--today", default=None)
    ap.add_argument("--stale-days", type=int, default=180)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.csv:
        ap.error("give the proof csv")
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        res = check(list(csv.DictReader(f)), today, a.stale_days)
    for n, s, m in res:
        print("%-4s %-10s %s" % (s, n, m))
    return 1 if any(s == "FAIL" for n, s, m in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
