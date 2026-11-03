#!/usr/bin/env python3
"""feedback.py - cluster player feedback lines into ranked themes with counts and sample quotes. Stdlib only.

  python feedback.py feedback.txt [--themes themes.json] [--top 8] [--samples 2]     (one comment per line; or a CSV with a 'text' column)
  python feedback.py --selftest

A line can match several themes. Themes are keyword lists: defaults cover common Roblox complaints and requests (lag/performance, bugs/crashes,
grind/progression, monetisation/price, content, controls/mobile, exploiters, social/trading, balance); pass --themes to replace them with your own
({"theme": ["keyword", ...]}). This is keyword matching, NOT sentiment or meaning analysis: read the samples, and re-read 'unmatched' for themes you
missed. Vault (updates-live-ops.md, playtesting-and-feedback.md): drive updates from problems and KPIs, combine community feedback with metrics, check requests against
data before building them, and expect the loudest request to be a minority; the count here is raw mentions, not unique players (de-duplicate by user
before ranking if your source allows).
"""
import argparse
import csv
import json
import re
import sys
from collections import defaultdict

DEFAULT = {
    "lag / performance": ["lag", "lags", "laggy", "fps", "freeze", "freezes", "stutter", "slow load", "loading", "ping"],
    "bugs / crashes": ["bug", "bugged", "glitch", "broken", "crash", "crashes", "stuck", "disappeared", "doesn't work", "doesnt work", "not working"],
    "grind / progression": ["grind", "grindy", "too slow", "takes forever", "boring", "repetitive", "afk", "progress"],
    "price / monetisation": ["expensive", "robux", "pay to win", "p2w", "gamepass", "paywall", "too much", "price", "cost"],
    "more content": ["add", "more", "new", "update", "please add", "want", "when will"],
    "controls / mobile": ["mobile", "phone", "controller", "controls", "button", "tablet", "ipad", "gamepad"],
    "exploiters / cheaters": ["hacker", "hackers", "exploit", "exploiter", "cheater", "cheating", "scripter", "aimbot"],
    "social / trading": ["trade", "trading", "friend", "friends", "party", "server", "chat", "scam", "scammer"],
    "balance": ["op", "overpowered", "nerf", "buff", "broken weapon", "unfair", "too strong", "too weak", "useless"],
}


def tok(line):
    return " " + re.sub(r"[^a-z0-9' ]+", " ", line.lower()) + " "


def cluster(lines, themes, samples=2):
    hits, ex, unmatched = defaultdict(int), defaultdict(list), []
    for ln in lines:
        t = tok(ln)
        m = [k for k, ws in themes.items() if any((" %s " % w) in t for w in ws)]
        if not m:
            unmatched.append(ln)
        for k in m:
            hits[k] += 1
            if len(ex[k]) < samples:
                ex[k].append(ln.strip()[:140])
    ranked = sorted(hits.items(), key=lambda kv: -kv[1])
    return ranked, ex, unmatched


def selftest():
    lines = ["The game lags so much on my phone", "Please add more pets", "pets disappeared after trade, bugged", "too grindy, takes forever",
             "hackers everywhere", "nice game", "lag spikes at the boss", "this sword is op, nerf it"]
    ranked, ex, un = cluster(lines, DEFAULT)
    d = dict(ranked)
    assert d["lag / performance"] == 2 and d["bugs / crashes"] == 1 and d["exploiters / cheaters"] == 1
    assert d["controls / mobile"] == 1 and d["balance"] == 1 and d["grind / progression"] == 1
    assert un == ["nice game"], un
    assert ranked[0][0] == "lag / performance" or ranked[0][1] == 2
    r2, _, _ = cluster(lines, {"x": ["pets"]})
    assert r2 == [("x", 2)]
    print("selftest ok (6 checks)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--themes")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--samples", type=int, default=2)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return 0
    if not a.file:
        ap.error("feedback file required")
    if a.file.lower().endswith(".csv"):
        with open(a.file, newline="", encoding="utf-8") as f:
            lines = [r["text"] for r in csv.DictReader(f)]
    else:
        lines = [l for l in open(a.file, encoding="utf-8").read().splitlines() if l.strip()]
    themes = json.load(open(a.themes, encoding="utf-8")) if a.themes else DEFAULT
    ranked, ex, un = cluster(lines, themes, a.samples)
    print("%d comments, %d unmatched (%.0f%%)" % (len(lines), len(un), 100.0 * len(un) / max(len(lines), 1)))
    for k, n in ranked[: a.top]:
        print("%4d  %5.1f%%  %s" % (n, 100.0 * n / len(lines), k))
        for s in ex[k]:
            print("          - %s" % s)
    if un:
        print("unmatched samples (read these for missed themes):")
        for s in un[:5]:
            print("   -", s[:120])
    return 0


if __name__ == "__main__":
    sys.exit(main())
