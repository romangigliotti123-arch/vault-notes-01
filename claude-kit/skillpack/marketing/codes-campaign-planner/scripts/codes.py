#!/usr/bin/env python3
"""codes.py - generate unguessable redeem codes, one set per creator/campaign, as a CSV. Stdlib only (secrets module).

  python codes.py --campaign launch --creator ethan --creator mia --per-creator 1 --prefix EGG --length 8 --expires 2026-12-31 --max-uses 5000 [--out codes.csv]
  python codes.py --selftest

Why random and not "EGG100": guessable codes leak the reward to everyone (vault: give each YouTuber a unique code to measure which
performs best, so each code must belong to one creator and be hard to guess). The alphabet drops look-alikes (0 O 1 I L) and
vowels, so a code cannot spell a word by accident. Output columns: campaign, creator, code, reward, expires, max_uses.
The reward column is a label you fill in the design doc; this tool never grants anything. Codes are stored in YOUR server code
(see CodeBook.luau); never in a LocalScript or any place the client can read.
"""
import argparse
import csv
import secrets
import sys

ALPHABET = "BCDFGHJKMNPQRSTVWXYZ23456789"


def make_code(prefix, length):
    body = "".join(secrets.choice(ALPHABET) for _ in range(length))
    return "%s-%s" % (prefix, body) if prefix else body


def generate(campaign, creators, per_creator, prefix, length, expires, max_uses, reward=""):
    if length < 6:
        raise ValueError("length under 6 is guessable; use 6 or more")
    seen = set()
    rows = []
    for c in creators:
        for _ in range(per_creator):
            code = make_code(prefix, length)
            while code in seen:
                code = make_code(prefix, length)
            seen.add(code)
            rows.append({"campaign": campaign, "creator": c, "code": code, "reward": reward, "expires": expires or "", "max_uses": max_uses or ""})
    return rows


def selftest():
    rows = generate("launch", ["a", "b", "c"], 50, "EGG", 8, "2026-12-31", 100)
    codes = [r["code"] for r in rows]
    assert len(codes) == 150 and len(set(codes)) == 150
    assert all(c.startswith("EGG-") and len(c) == 12 for c in codes)
    assert not any(ch in c.split("-", 1)[1] for c in codes for ch in "AEIOUL01")
    try:
        generate("x", ["a"], 1, "", 4, None, None)
        raise SystemExit("short length accepted")
    except ValueError:
        pass
    print("selftest ok (4 checks, 150 codes unique)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--campaign", default="campaign")
    ap.add_argument("--creator", action="append", default=[])
    ap.add_argument("--per-creator", type=int, default=1, dest="per_creator")
    ap.add_argument("--prefix", default="")
    ap.add_argument("--length", type=int, default=8)
    ap.add_argument("--expires")
    ap.add_argument("--max-uses", type=int, dest="max_uses")
    ap.add_argument("--reward", default="")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.creator:
        ap.error("give at least one --creator (use 'public' for a community code)")
    rows = generate(a.campaign, a.creator, a.per_creator, a.prefix, a.length, a.expires, a.max_uses, a.reward)
    f = open(a.out, "w", encoding="utf-8", newline="") if a.out else sys.stdout
    w = csv.DictWriter(f, fieldnames=["campaign", "creator", "code", "reward", "expires", "max_uses"])
    w.writeheader()
    w.writerows(rows)
    if a.out:
        f.close()
        print("wrote %d codes to %s" % (len(rows), a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
