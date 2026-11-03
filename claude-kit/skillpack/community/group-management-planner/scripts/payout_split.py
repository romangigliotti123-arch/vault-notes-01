#!/usr/bin/env python3
"""payout_split.py - split a group payout fairly in whole Robux. Stdlib only.

  python payout_split.py --amount 1000 --split ann=50,bob=30,cy=20
  python payout_split.py --selftest

Largest-remainder rounding: every share is a whole number and the shares add up to exactly --amount (nothing lost, nothing invented).
Percentages must add to 100. The amount is what the group actually has to pay out AFTER Roblox's cut and any pending period: read it
from the group revenue page, never from a guess. How payouts are made (percentage vs fixed, one-time vs recurring, who may approve)
changes on the platform: live-check the Creator Hub group payout rules, and keep payout approval with the owner only.
Exit 2 on bad input.
"""
import argparse
import sys


def split(amount, shares):
    if amount < 0 or int(amount) != amount:
        raise ValueError("amount must be a whole number >= 0")
    if not shares or any(p < 0 for p in shares.values()):
        raise ValueError("percentages must be >= 0")
    if abs(sum(shares.values()) - 100) > 1e-9:
        raise ValueError("percentages add up to %s, not 100" % sum(shares.values()))
    raw = {k: amount * p / 100 for k, p in shares.items()}
    out = {k: int(v) for k, v in raw.items()}
    left = int(amount) - sum(out.values())
    for k in sorted(raw, key=lambda k: (-(raw[k] - out[k]), k))[:left]:
        out[k] += 1
    return out


def selftest():
    assert split(1000, {"a": 50, "b": 30, "c": 20}) == {"a": 500, "b": 300, "c": 200}
    r = split(100, {"a": 33.3333333333, "b": 33.3333333333, "c": 33.3333333334})
    assert sum(r.values()) == 100, r
    r = split(7, {"a": 50, "b": 50})
    assert sum(r.values()) == 7 and sorted(r.values()) == [3, 4], r
    assert split(0, {"a": 100}) == {"a": 0}
    for bad in (lambda: split(100, {"a": 60, "b": 30}), lambda: split(-1, {"a": 100}), lambda: split(10, {"a": 120, "b": -20})):
        try:
            bad()
            raise AssertionError("expected ValueError")
        except ValueError:
            pass
    print("selftest ok (7 asserts)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--amount", type=int)
    ap.add_argument("--split")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    try:
        shares = {k.strip(): float(v) for k, v in (p.split("=") for p in (a.split or "").split(","))}
        res = split(a.amount if a.amount is not None else -1, shares)
    except ValueError as e:
        print("error:", e)
        return 2
    for k, v in res.items():
        print("%-12s %8d" % (k, v))
    print("%-12s %8d" % ("total", sum(res.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
