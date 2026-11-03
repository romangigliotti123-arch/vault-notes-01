#!/usr/bin/env python3
"""odds_check.py <odds.json> | --selftest

Checks a paid-random-item odds table against the disclosure patterns in the Creator Docs paid-random-items page (live-check the page:
policy changes). Input JSON:
  {"cost": 10, "currency": "Robux", "outcomes": [{"name": "Sword", "odds": 5.0, "one_time": false}, ...],
   "modifiers": [{"name": "Luck boost", "effect": "x1.5 rare odds", "disclosed_before_purchase": true}],
   "indirect": [{"name": "Re-roll token", "odds_shown_before_spend": true}], "displayed_percent_note": false}
Checks: odds are numeric and positive; they sum to exactly 100 (tolerance 0.001) or, when rounded, displayed_percent_note must be true;
every outcome named; modifiers and indirect currencies disclose before purchase/spend; one_time outcomes need a re-normalise note.
Prints the expected-value price for each outcome (cost / (odds/100)) as the guaranteed-purchase alternative for restricted players.
This is arithmetic on YOUR table, not legal advice. Exit 1 on FAIL, 2 on bad input.
"""
import json
import sys


def check(t):
    out, ev = [], []
    outs = t.get("outcomes") or []
    cost = t.get("cost")
    if not outs:
        return [("FAIL", "no outcomes listed")], ev
    total = 0.0
    for o in outs:
        name = str(o.get("name", "")).strip()
        try:
            p = float(o.get("odds"))
        except (TypeError, ValueError):
            out.append(("FAIL", "outcome %r has non-numeric odds" % name))
            continue
        if not name:
            out.append(("FAIL", "an outcome has no name"))
        if p <= 0:
            out.append(("FAIL", "outcome %r has odds <= 0 (remove it or fix it)" % name))
            continue
        total += p
        if isinstance(cost, (int, float)) and cost > 0:
            ev.append((name, round(cost / (p / 100.0), 2)))
        if o.get("one_time"):
            out.append(("WARN", "outcome %r is one-time: remaining odds must be re-shown per user after it is awarded" % name))
    if abs(total - 100.0) > 0.001:
        if t.get("displayed_percent_note") and abs(total - 100.0) <= 1.0:
            out.append(("WARN", "odds sum to %.3f; allowed only with the visible 'may not total 100%%' disclaimer" % total))
        else:
            out.append(("FAIL", "odds sum to %.3f, must be 100 (or within 1 with the disclaimer flag)" % total))
    else:
        out.append(("OK", "odds sum to 100"))
    for m in t.get("modifiers") or []:
        if not m.get("disclosed_before_purchase"):
            out.append(("FAIL", "odds modifier %r not disclosed numerically before purchase" % m.get("name")))
    for i in t.get("indirect") or []:
        if not i.get("odds_shown_before_spend"):
            out.append(("FAIL", "indirect currency %r: odds not shown before the user spends it" % i.get("name")))
    if not isinstance(cost, (int, float)) or cost <= 0:
        out.append(("WARN", "cost missing: no expected-value price computed"))
    return out, ev


def selftest():
    good = {"cost": 10, "outcomes": [{"name": "A", "odds": 95}, {"name": "Sword", "odds": 5}]}
    r, ev = check(good)
    assert not any(x[0] == "FAIL" for x in r) and dict(ev)["Sword"] == 200.0, (r, ev)
    bad = {"cost": 10, "outcomes": [{"name": "A", "odds": 90}, {"name": "B", "odds": 5}], "modifiers": [{"name": "Luck", "disclosed_before_purchase": False}],
           "indirect": [{"name": "Key"}]}
    r, _ = check(bad)
    fails = [x[1] for x in r if x[0] == "FAIL"]
    assert len(fails) == 3, fails
    r, _ = check({"outcomes": [{"name": "A", "odds": 33.3}, {"name": "B", "odds": 33.3}, {"name": "C", "odds": 33.3}], "displayed_percent_note": True})
    assert not any(x[0] == "FAIL" for x in r) and any(x[0] == "WARN" for x in r), r
    r, _ = check({"outcomes": [{"name": "A", "odds": "x"}]})
    assert r[0][0] == "FAIL"
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if len(argv) != 1:
        print(__doc__)
        return 2
    try:
        t = json.load(open(argv[0], encoding="utf-8"))
        assert isinstance(t, dict)
    except Exception as e:
        print("bad input: %s" % e)
        return 2
    rows, ev = check(t)
    for lv, msg in rows:
        print("[%s] %s" % (lv, msg))
    for n, price in ev:
        print("expected-value price for guaranteed %s: %s %s" % (n, price, t.get("currency", "")))
    print("arithmetic on your table only: live-check the paid random items page")
    return 1 if any(r[0] == "FAIL" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
