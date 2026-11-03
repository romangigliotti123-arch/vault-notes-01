#!/usr/bin/env python3
"""text_lint.py - lint player-facing community text (welcome, rules, FAQ, macros, announcements, replies). Stdlib only.

  python text_lint.py message.txt [--max-words 150] [--require-age]
  python text_lint.py --selftest

Checks (FAIL = fix before posting, WARN = judgement):
  pii      FAIL  asks players to send/share a password, address, phone, email, real name, school, location or photo
  dm       FAIL  invites private contact ("dm me", "add me on ...") - keep help in public or ticket channels, never DM minors
  scam     FAIL  promises free Robux or asks for off-platform payment (paypal, cashapp, venmo, gift card)
  shaming  FAIL  names a player handle next to an accusation (banned, scammer, cheater, toxic) in a public post
  tone     WARN  blaming phrases ("read the rules", "as we already said", "obviously", "you should have")
  length   WARN  more than --max-words words
  age      WARN  with --require-age: no mention of an age requirement or minimum age
Exit 1 on FAIL. Regex checks are leads: a human reads the text.
"""
import argparse
import re
import sys

I = re.I
PII = re.compile(r"\b(send|share|tell|give|post|dm|enter|type)\b[^.\n]{0,40}\b(password|passcode|address|phone|email|e-mail|real name|school|location|photo|selfie|age)\b", I)
DM = re.compile(r"\b(dm me|pm me|message me (privately|in private)|add me on|text me|whisper me)\b", I)
SCAM = re.compile(r"\b(free robux|send me robux|paypal|cash ?app|venmo|gift ?card)\b", I)
SHAME = re.compile(r"(@\w+|\b\w+#\d{4}\b)[^.\n]{0,60}\b(banned|scammer|cheater|toxic|exploiter|racist)\b|\b(banned|scammer|cheater|toxic|exploiter)\b[^.\n]{0,30}(@\w+|\b\w+#\d{4}\b)", I)
TONE = re.compile(r"\b(read the rules|as we (already )?said|obviously|you should have|are you stupid|how many times)\b", I)
AGE = re.compile(r"\b(13\+?|age requirement|minimum age|old enough|years old|age)\b", I)


def hit(rx, text, fail):
    m = rx.search(text)
    return ("FAIL" if fail else "WARN") if m else "PASS", m.group(0) if m else "none"


def lint(text, max_words=150, require_age=False):
    out = []
    for name, rx, fail in (("pii", PII, True), ("dm", DM, True), ("scam", SCAM, True), ("shaming", SHAME, True), ("tone", TONE, False)):
        s, m = hit(rx, text, fail)
        out.append((name, s, m))
    n = len(text.split())
    out.append(("length", "WARN" if n > max_words else "PASS", "%d words (max %d)" % (n, max_words)))
    if require_age:
        ok = bool(AGE.search(text))
        out.append(("age", "PASS" if ok else "WARN", "age rule present" if ok else "no age requirement mentioned"))
    return out


def selftest():
    good = "Welcome! This server is for players of Cool Game. Read #rules, find the game link in #welcome, report bugs in #bug-reports. You must meet the minimum age for Discord."
    r = {n: s for n, s, m in lint(good, require_age=True)}
    assert all(v == "PASS" for v in r.values()), r

    def one(t, k, **kw):
        return {n: s for n, s, m in lint(t, **kw)}[k]

    assert one("Please send me your password to restore it", "pii") == "FAIL"
    assert one("DM me your problem", "dm") == "FAIL"
    assert one("Free Robux for the first 10!", "scam") == "FAIL"
    assert one("@bob123 was banned for cheating", "shaming") == "FAIL"
    assert one("You should have read it.", "tone") == "WARN"
    assert one("word " * 200, "length") == "WARN"
    assert one("hello there", "age", require_age=True) == "WARN"
    print("selftest ok (8 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--max-words", type=int, default=150)
    ap.add_argument("--require-age", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("give the text file")
    res = lint(open(a.file, encoding="utf-8-sig").read(), a.max_words, a.require_age)
    for n, s, m in res:
        print("%-4s %-8s %s" % (s, n, m))
    return 1 if any(s == "FAIL" for n, s, m in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
