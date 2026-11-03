#!/usr/bin/env python3
"""title_screen.py - screen game title / tagline candidates against the vault's rules. Stdlib only.

  python title_screen.py "Steal an Egg" "OBBY OBBY Run!!" [--file candidates.txt] [--min-words 2] [--max-words 4] [--max-emoji 2] [--max-chars N] [--json]
  python title_screen.py --selftest

Checks (each PASS/WARN/FAIL; exit 1 when any FAIL):
  words      word count inside min..max (vault: literal, as few words as possible)
  repeat     a word repeated (vault: repeated words like OBBY OBBY OBBY may be demoted)
  caps       more than one ALL-CAPS word (random capitals)
  emoji      emoji / pictograph count over --max-emoji (vault: official advice moved from none to one or two)
  symbols    runs of punctuation or tag-like characters (#, @, <, >, [ ], repeated !)
  money      leads with a reward or giveaway promise (vault: giveaway-led metadata reduces exposure)
  reading    words of 4+ syllables (vault: aim for about third-grade words); WARN only
  length     over --max-chars when given. The real limit is NOT built in: live-check Creator Docs and pass it.
Nothing here knows Roblox's current character limit or rules; the skill passes the numbers it live-checked.
"""
import argparse
import json
import re
import sys

MONEY = re.compile(r"\b(free\s+robux|robux|giveaway|win\s+\$|\$\d|prize|cash\s*out|gift\s*card)\b", re.I)
EMOJI = re.compile("[←-⇿⌀-⏿☀-➿\U0001F000-\U0001FAFF]")


def syllables(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w:
        return 0
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(n, 1)


def screen(title, min_words=2, max_words=4, max_emoji=2, max_chars=None):
    res = []
    plain = EMOJI.sub(" ", title)
    words = re.findall(r"[A-Za-z0-9']+", plain)
    n = len(words)
    res.append(("words", "PASS" if min_words <= n <= max_words else "FAIL", "%d words (want %d-%d)" % (n, min_words, max_words)))
    low = [w.lower() for w in words]
    rep = sorted({w for w in low if low.count(w) > 1 and len(w) > 2})
    res.append(("repeat", "FAIL" if rep else "PASS", "repeated: " + ", ".join(rep) if rep else "no repeats"))
    caps = [w for w in words if len(w) > 1 and w.isupper() and not any(c.isdigit() for c in w)]
    res.append(("caps", "FAIL" if len(caps) > 1 else "PASS", "ALL-CAPS words: %s" % (", ".join(caps) or "none")))
    ne = len(EMOJI.findall(title))
    res.append(("emoji", "FAIL" if ne > max_emoji else "PASS", "%d emoji (max %d)" % (ne, max_emoji)))
    sym = re.search(r"[!?]{2,}|[#@<>\[\]{}|~*_]|[.]{3,}", title)
    res.append(("symbols", "WARN" if sym else "PASS", "odd symbols: %r" % sym.group(0) if sym else "clean"))
    m = MONEY.search(title)
    res.append(("money", "FAIL" if m else "PASS", "reward promise: %r" % m.group(0) if m else "no reward promise"))
    hard = [w for w in words if syllables(w) >= 4]
    res.append(("reading", "WARN" if hard else "PASS", "long words: %s" % ", ".join(hard) if hard else "short words"))
    if max_chars:
        res.append(("length", "PASS" if len(title) <= max_chars else "FAIL", "%d chars (max %d)" % (len(title), max_chars)))
    return res


def selftest():
    def st(t, **k):
        return {r[0]: r[1] for r in screen(t, **k)}

    assert all(v == "PASS" for v in st("Steal an Egg").values()), st("Steal an Egg")
    assert st("OBBY OBBY OBBY")["repeat"] == "FAIL"
    assert st("FREE ROBUX Tycoon")["money"] == "FAIL"
    assert st("BIG MEGA Run")["caps"] == "FAIL"
    assert st("Egg Hunt \U0001F95A\U0001F95A\U0001F95A")["emoji"] == "FAIL"
    assert st("Egg Hunt \U0001F95A")["emoji"] == "PASS"
    assert st("Egg")["words"] == "FAIL"
    assert st("Steal an Egg", max_chars=5)["length"] == "FAIL"
    assert st("Extraordinarily Enthusiastic Hamster")["reading"] == "WARN"
    assert syllables("tycoon") == 2 and syllables("egg") == 1
    print("selftest ok (10 assertions)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("titles", nargs="*")
    ap.add_argument("--file")
    ap.add_argument("--min-words", type=int, default=2)
    ap.add_argument("--max-words", type=int, default=4)
    ap.add_argument("--max-emoji", type=int, default=2)
    ap.add_argument("--max-chars", type=int)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if a.selftest:
        return selftest()
    titles = list(a.titles)
    if a.file:
        titles += [ln.strip() for ln in open(a.file, encoding="utf-8") if ln.strip()]
    if not titles:
        ap.error("give at least one title")
    bad = 0
    out = []
    for t in titles:
        r = screen(t, a.min_words, a.max_words, a.max_emoji, a.max_chars)
        fails = [x for x in r if x[1] == "FAIL"]
        bad += 1 if fails else 0
        out.append({"title": t, "verdict": "FAIL" if fails else "PASS", "checks": r})
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        for o in out:
            print("%s  %s" % (o["verdict"], o["title"]))
            for name, st, msg in o["checks"]:
                if st != "PASS":
                    print("   %-5s %-8s %s" % (st, name, msg))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
