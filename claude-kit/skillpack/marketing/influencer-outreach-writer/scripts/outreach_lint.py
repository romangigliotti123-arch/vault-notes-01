#!/usr/bin/env python3
"""outreach_lint.py - lint a creator outreach message against the vault's pitch rules. Stdlib only.

  python outreach_lint.py message.txt [--max-words 150]
  python outreach_lint.py --selftest

Rules checked (vault: influencer-and-creator-marketing, social-features-and-virality):
  link        a playable link is present (Make the first pitch self-contained: screenshots, trailer, direct playable link)
  offer       a concrete reason to play / benefit is named (early access, exclusive item, code, admin, assets, payment)
  bare-ask    does not read as a bare "play my game" (never send a bare play-my-game DM)
  length      under --max-words (short enough to read in one go); the number is a judgement default, not a vault figure
  personal    mentions something specific from the creator's own content (a <<video/series name>> or the word "your")
  pressure    no deadline threats, guilt or "everyone else already" pressure
  money       if it names a payment, it says amount or the placeholder AMOUNT and does NOT promise views or income
  placeholder no unfilled <<...>> placeholders left (a draft is not ready to send while any remain)
The tool cannot judge tone or truth. The user sends the message; nothing is sent from here.
"""
import argparse
import re
import sys

LINK = re.compile(r"https?://\S+|roblox\.com/games/\S+", re.I)
OFFER = re.compile(r"\b(early access|exclusive|code|admin|free|reward|pet|item|skin|asset|render|thumbnail|paid|payment|robux|\$\d|revenue|commission|private server)\b", re.I)
BARE = re.compile(r"^\W*(hi|hey|hello)?\W*(please\s+)?(play|check out|try)\s+my\s+game\W*$", re.I | re.S)
PRESSURE = re.compile(r"\b(last chance|only today|everyone else|you will regret|don'?t miss out|deadline|or else)\b", re.I)
PROMISE = re.compile(r"\b(guarantee[sd]?|will (get|earn|make) you|millions? of views|go viral|make you rich)\b", re.I)


def lint(text, max_words=150):
    out = []
    words = len(text.split())
    out.append(("link", "PASS" if LINK.search(text) else "FAIL", "playable link present" if LINK.search(text) else "no link: the creator cannot play at once"))
    out.append(("offer", "PASS" if OFFER.search(text) else "FAIL", "offer named" if OFFER.search(text) else "no concrete reason to play"))
    bare = bool(BARE.match(text.strip())) or words < 12
    out.append(("bare-ask", "FAIL" if bare else "PASS", "reads as a bare ask" if bare else "has substance"))
    out.append(("length", "PASS" if words <= max_words else "WARN", "%d words (limit %d)" % (words, max_words)))
    personal = bool(re.search(r"<<[^>]*(video|series|channel|stream)[^>]*>>", text, re.I)) or bool(re.search(r"\byour (video|series|channel|stream|last|latest)\b", text, re.I))
    out.append(("personal", "PASS" if personal else "WARN", "refers to their content" if personal else "does not mention anything specific to the creator"))
    pr = PRESSURE.search(text)
    out.append(("pressure", "FAIL" if pr else "PASS", "pressure phrase: %r" % pr.group(0) if pr else "no pressure"))
    pm = PROMISE.search(text)
    out.append(("money", "FAIL" if pm else "PASS", "promises results: %r" % pm.group(0) if pm else "no result promises"))
    ph = re.findall(r"<<[^>]*>>", text)
    out.append(("placeholder", "FAIL" if ph else "PASS", "unfilled: %s" % ", ".join(ph[:5]) if ph else "none left"))
    return out


GOOD = (
    "Hi Mia, I loved your last obby-speedrun video. I made a one-button egg-stealing game and think your audience would like it. "
    "Playable link: https://www.roblox.com/games/123/Steal-an-Egg  Trailer and three screenshots: https://example.com/kit. "
    "For you: early access to the next update and a private server for your lobby, plus a code with your name on it so you can see how many people play. "
    "No obligation. If it is not your style, thank you for reading."
)


def selftest():
    def st(t, **k):
        return {n: s for n, s, m in lint(t, **k)}

    g = st(GOOD)
    assert g["link"] == "PASS" and g["offer"] == "PASS" and g["bare-ask"] == "PASS" and g["pressure"] == "PASS" and g["personal"] == "PASS", g
    assert st("hey play my game")["bare-ask"] == "FAIL"
    assert st("Hi, nice channel. Try it: no link here, free item for you.")["link"] == "FAIL"
    assert st(GOOD + " Last chance, everyone else already did it.")["pressure"] == "FAIL"
    assert st(GOOD + " This will make you rich, guaranteed.")["money"] == "FAIL"
    assert st("Hi <<Name>>, " + GOOD)["placeholder"] == "FAIL"
    assert st(GOOD, max_words=20)["length"] == "WARN"
    print("selftest ok (7 cases)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--max-words", type=int, default=150, dest="max_words")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("give the message file")
    res = lint(open(a.file, encoding="utf-8").read(), a.max_words)
    for n, s, m in res:
        print("%-5s %-12s %s" % (s, n, m))
    return 1 if any(s == "FAIL" for n, s, m in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
