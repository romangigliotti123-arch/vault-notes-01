#!/usr/bin/env python3
"""slopscan.py - flag the stock AI-writing patterns in a text file and print the lines to rewrite. Stdlib only.

  python slopscan.py text.md [--max-hits 3]
  python slopscan.py --selftest

Patterns: puffery words, stock openers and closers, filler transitions, vague -ing tails, promo hype, em dashes, plus the
em-dash rate per 100 words. It cannot judge meaning or voice; it finds the lines to rewrite. Exit 0 when hits <= --max-hits, else 1.
"""
import argparse
import re
import sys

PATTERNS = [
    ("puffery", r"\b(pivotal|testament to|evolving landscape|vibrant|rich tapestry|game-changing|cutting-edge|seamless(?:ly)?|robust|elevate|delve|bustling|nestled|in the realm of|stands as)\b"),
    ("chatbot opener or closer", r"\b(i hope this helps|let me know if|feel free to|great question|certainly!|absolutely!|in conclusion|in summary)\b"),
    ("filler transition", r"\b(moreover|furthermore|additionally|it'?s worth noting|it is important to note|at the end of the day)\b"),
    ("vague -ing tail", r",\s+(?:highlighting|underscoring|showcasing|reflecting|ensuring|emphasizing|contributing to)\b"),
    ("promo hype", r"\b(immersive|epic adventure|like never before|ultimate experience|next level|unforgettable|dive into)\b"),
    ("em dash", "—"),
]


def scan(text):
    hits = []
    for name, pat in PATTERNS:
        for m in re.finditer(pat, text, re.I):
            hits.append((name, text.count("\n", 0, m.start()) + 1, m.group(0)))
    hits.sort(key=lambda h: h[1])
    words = max(1, len(text.split()))
    dashes = sum(1 for h in hits if h[0] == "em dash")
    return hits, dashes * 100.0 / words


def selftest():
    bad = "Great question! This pivotal update is a testament to our vibrant community — seamlessly showcasing a robust shop, highlighting growth. Let me know if you want more."
    hits, rate = scan(bad)
    kinds = {h[0] for h in hits}
    assert {"puffery", "chatbot opener or closer", "em dash", "vague -ing tail"} <= kinds, kinds
    assert rate > 3, rate
    good = "Version 1.4 adds a trading limit of 20 items. Last week 312 players hit the old cap."
    assert scan(good)[0] == [], scan(good)
    print("selftest ok (2 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--max-hits", type=int, default=3)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    text = open(a.file, encoding="utf-8").read()
    hits, rate = scan(text)
    for name, line, s in hits:
        print("line %d  %-26s %s" % (line, name, s.replace("—", "(em dash)")))
    ok = len(hits) <= a.max_hits
    print("hits %d, em dashes per 100 words %.1f -> %s" % (len(hits), rate, "PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
