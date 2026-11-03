#!/usr/bin/env python3
"""patchlint.py - lint a patch-notes / update-log text file against the vault's rules. Stdlib only.

  python patchlint.py notes.md [--max-headline 60] [--json]
  python patchlint.py --selftest

Checks (Roblox/roblox-kb/updates-live-ops.md): specific entries, never a vague "bug fixes"; the headline/update text of a platform Events and
Updates entry stays within 60 characters (the 99-character limit is for notification strings, check those separately); balance changes name the
number; paid items are announced as paid; known bugs listed as fixed. Style checks (bullet length, code identifiers) are this skill's defaults.
Notes format: first non-empty line is the headline; sections are lines starting with '#', e.g. '## New', '## Changed', '## Fixed'; bullets start with '-'.
Exit 0 = no errors (warnings may remain), 1 = errors.
"""
import argparse
import json
import re
import sys

VAGUE = re.compile(r"^(?:various |misc(?:ellaneous)? |general |some |minor |other )?(?:bug ?fixes|fixes|improvements|changes|tweaks|stuff|optimi[sz]ations?)\.?$", re.I)
CODEISH = re.compile(r"(?:[a-z]+[A-Z][A-Za-z]+\b|\w+\.\w+\(|::|\bRemoteEvent\b|\bDataStore\b|\bnil\b)")
PAID = re.compile(r"\b(robux|gamepass|game pass|developer product|dev product|vip|premium|paid)\b", re.I)
NUM = re.compile(r"\d")
BALANCE = re.compile(r"\b(buff(?:ed|s)?|nerf(?:ed|s)?|increase[sd]?|decrease[sd]?|reduce[sd]?|raise[sd]?|lower(?:ed)?|rebalance[sd]?|cost|price|damage|drop rate|odds)\b", re.I)


def lint(text, max_headline=60):
    lines = [l.rstrip() for l in text.replace("\r\n", "\n").split("\n")]
    body = [l for l in lines if l.strip()]
    errs, warns = [], []
    if not body:
        return ["empty notes"], []
    head = body[0].lstrip("# ").strip()
    if len(head) > max_headline:
        errs.append("headline is %d chars (limit %d for event/update text): %r" % (len(head), max_headline, head))
    if not re.search(r"\b(v?\d+\.\d+(?:\.\d+)?|update \d+|\d{4}-\d{2}-\d{2}|week \d+|season \d+)\b", head, re.I):
        warns.append("headline has no version, date or update number")
    sections = [l.lstrip("# ").strip().lower() for l in body[1:] if l.startswith("#")]
    if not any(s.startswith("fix") for s in sections):
        warns.append("no Fixed section: vault says list fixed bugs publicly")
    if not any(s.startswith("new") or s.startswith("added") for s in sections):
        warns.append("no New section")
    bullets = [l.lstrip("-*• ").strip() for l in body if re.match(r"^\s*[-*•]\s+", l)]
    if not bullets:
        errs.append("no bullets found")
    for b in bullets:
        if VAGUE.match(b):
            errs.append("vague entry: %r (say what was fixed or changed)" % b)
        if len(b) > 140:
            warns.append("long bullet (%d chars): %r" % (len(b), b[:50]))
        if CODEISH.search(b):
            warns.append("code-like wording, write for players: %r" % b[:60])
        if BALANCE.search(b) and not NUM.search(b):
            warns.append("balance change without a number: %r" % b[:60])
        if PAID.search(b) and not re.search(r"\b(paid|robux|\d+ ?r\$)\b", b, re.I):
            warns.append("paid item without the word paid/Robux: %r" % b[:60])
    return errs, warns


def selftest():
    good = "Update 12: Frost Caves\n## New\n- Frost Caves area with 3 new pets\n## Changed\n- Sled price lowered from 500 to 350 coins\n## Fixed\n- Fixed pets disappearing after trading\n"
    e, w = lint(good)
    assert not e and not w, (e, w)
    bad = "Big update with a very long headline that goes well past sixty characters for sure\n## New\n- bug fixes\n- Nerfed the boss\n- Fixed remoteEvent.FireServer() nil error\n"
    e, w = lint(bad)
    assert any("headline" in x for x in e) and any("vague" in x for x in e), e
    assert any("without a number" in x for x in w) and any("code-like" in x for x in w) and any("no Fixed" in x for x in w), w
    e, w = lint("Update 3\n## New\n- VIP pass with a chat tag\n## Fixed\n- Fixed the lobby music\n")
    assert any("paid item" in x for x in w), w
    assert lint("")[0]
    print("selftest ok (4 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--max-headline", type=int, default=60)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not a.file:
        ap.error("notes file required")
    e, w = lint(open(a.file, encoding="utf-8").read(), a.max_headline)
    if a.json:
        print(json.dumps({"errors": e, "warnings": w}, indent=1))
    else:
        for x in e:
            print("ERROR:", x)
        for x in w:
            print("warn: ", x)
        print("%d error(s), %d warning(s)" % (len(e), len(w)))
    return 1 if e else 0


if __name__ == "__main__":
    sys.exit(main())
