#!/usr/bin/env python3
"""hotfix.py - start and check a hotfix record (one text file per incident). Stdlib only.

  python hotfix.py new --title "Pets vanish after trade" --severity S1 > hotfix-2026-11-02-pets.md
  python hotfix.py check hotfix-2026-11-02-pets.md
  python hotfix.py --selftest

Severity scale is this skill's own (the vault has no incident severity levels, see updates-live-ops.md 'Not covered'): S1 = data loss, exploit or game unplayable;
S2 = major feature broken or economy harm; S3 = annoying bug. The vault rules it encodes: roll back severe regressions first and profile after; ship critical
bug fixes as same-day silent patches instead of waiting for the weekly cycle; test before release and watch the first minutes after publishing; set a crash-rate alert;
post status updates during outages; list the fix in the changelog afterwards. 'check' fails (exit 1) when a required field is empty or a rule is broken.
"""
import argparse
import datetime
import re
import sys

FIELDS = ["Title", "Severity", "Detected", "Impact", "Cause", "Fix", "Rollback", "Tested", "Verify-metric", "Verify-after", "Status-post", "Changelog"]
PLACEHOLDER = re.compile(r"^(|todo|tbd|\?|-|n/a)$", re.I)


def template(title, severity):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = {"Title": title, "Severity": severity, "Detected": now + " by ", "Impact": "", "Cause": "", "Fix": "", "Rollback": "",
            "Tested": "", "Verify-metric": "", "Verify-after": "", "Status-post": "", "Changelog": "pending (add after the fix ships)"}
    return "\n".join("%s: %s" % (k, rows[k]) for k in FIELDS) + "\n"


def parse(text):
    d = {}
    for ln in text.splitlines():
        m = re.match(r"^([A-Za-z-]+):\s*(.*)$", ln)
        if m:
            d[m.group(1)] = m.group(2).strip()
    return d


def check(text):
    d = parse(text)
    errs = []
    for f in FIELDS:
        if f not in d or PLACEHOLDER.match(d.get(f, "")):
            errs.append("empty field: %s" % f)
    sev = d.get("Severity", "")
    if sev and sev not in ("S1", "S2", "S3"):
        errs.append("Severity must be S1, S2 or S3")
    if sev == "S1" and re.match(r"^(none|no)\b", d.get("Rollback", ""), re.I):
        errs.append("S1 needs a rollback path (vault: roll back severe regressions first, profile after)")
    if d.get("Tested", "") and re.match(r"^(no|not|skipped)\b", d["Tested"], re.I):
        errs.append("untested fix: vault says test every update, even a hotfix, and watch the first minutes after publishing")
    if sev in ("S1", "S2") and d.get("Status-post", "").lower() in ("no", "none"):
        errs.append("S1/S2 incidents need a status post (Discord), not silence")
    return errs


def selftest():
    t = template("Pets vanish", "S1")
    assert check(t), "template must fail until filled in"
    full = "\n".join("%s: %s" % (k, v) for k, v in [("Title", "x"), ("Severity", "S2"), ("Detected", "2026-11-02 10:00 UTC by bot"), ("Impact", "5% of trades"),
                                                    ("Cause", "race in trade"), ("Fix", "lock both profiles"), ("Rollback", "republish v40"), ("Tested", "2-client test"),
                                                    ("Verify-metric", "error count"), ("Verify-after", "30 min"), ("Status-post", "posted"), ("Changelog", "added")])
    assert check(full) == [], check(full)
    assert check(full.replace("Tested: 2-client test", "Tested: no")) != []
    assert check(full.replace("Severity: S2", "Severity: S9")) != []
    assert any("S1 needs" in e for e in check(full.replace("Severity: S2", "Severity: S1").replace("Rollback: republish v40", "Rollback: none")))
    print("selftest ok (5 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", choices=["new", "check"])
    ap.add_argument("file", nargs="?")
    ap.add_argument("--title", default="TITLE")
    ap.add_argument("--severity", default="S2")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if a.cmd == "new":
        sys.stdout.write(template(a.title, a.severity))
        return 0
    if a.cmd == "check" and a.file:
        errs = check(open(a.file, encoding="utf-8").read())
        for e in errs:
            print("FAIL:", e)
        print("%d problem(s)" % len(errs))
        return 1 if errs else 0
    ap.error("use: new | check FILE")


if __name__ == "__main__":
    sys.exit(main())
