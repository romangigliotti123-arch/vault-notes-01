#!/usr/bin/env python3
"""score.py - weighted overall score (1.00-10.00) for rbx-rate. Stdlib only, deterministic.

  python score.py ratings.json            read {"scores": {"loop": 7, ...}, "flags": {...}, "weights": {...}} (stdin if '-')
  python score.py --weights               print the default weights
  python score.py --selftest              built-in checks

scores: integer or half-point 1..10 for each of the 12 criterion ids below (all required).
flags : violates_rules (bool; pay-to-win, paid randomness, real-money gambling, unsafeguarded stranger contact) -> overall capped at 3.00.
weights (optional): override per criterion (relative; need not sum to 100). Defaults come from the vault and are listed in
        references/rubric.md with their note paths; if the freshest DECISION-RULES/BENCHMARKS contradict them, pass the override and say why.
Caps: any GATE criterion (loop, f30, money, scope) <= 2 -> overall capped at 5.00. Prints JSON: overall (2 decimals), raw, caps applied, band, per-criterion contribution.
"""
import json
import sys

CRITERIA = ["loop", "ret", "f30", "feel", "social", "money", "disc", "scope", "diff", "trend", "ad", "upd"]
WEIGHTS = {"loop": 14, "ret": 14, "f30": 10, "feel": 8, "social": 9, "money": 9, "disc": 8, "scope": 8, "diff": 5, "trend": 5, "ad": 3, "upd": 7}
GATES = ["loop", "f30", "money", "scope"]
BANDS = [(8.5, "exceptional: build now"), (7.0, "strong: build, fix the weaknesses on the way"), (5.5, "viable: fix the top weaknesses first"),
         (4.0, "weak: rework the concept before planning"), (0.0, "reject or restart")]


def band(x):
    for lo, name in BANDS:
        if x >= lo:
            return name


def score(data):
    s = data.get("scores", {})
    w = dict(WEIGHTS)
    w.update(data.get("weights", {}) or {})
    missing = [c for c in CRITERIA if c not in s]
    if missing:
        raise ValueError("missing scores: " + ", ".join(missing))
    for c in CRITERIA:
        v = s[c]
        if not isinstance(v, (int, float)) or v < 1 or v > 10 or (v * 2) != int(v * 2):
            raise ValueError("score %s=%r must be 1..10 in steps of 0.5" % (c, v))
    tw = float(sum(w[c] for c in CRITERIA))
    raw = sum(w[c] * s[c] for c in CRITERIA) / tw
    overall, caps = raw, []
    gate_low = [c for c in GATES if s[c] <= 2]
    if gate_low and overall > 5.0:
        overall = 5.0
        caps.append("gate criterion <= 2 (%s): capped at 5.00" % ", ".join(gate_low))
    if (data.get("flags") or {}).get("violates_rules") and overall > 3.0:
        overall = 3.0
        caps.append("violates kid-safety/monetisation hard rule: capped at 3.00")
    vals = [s[c] for c in CRITERIA]
    return {
        "overall": "%.2f" % round(overall + 1e-9, 2),
        "raw_weighted": "%.2f" % round(raw + 1e-9, 2),
        "caps_applied": caps,
        "band": band(round(overall + 1e-9, 2)),
        "spread": {"min": min(vals), "max": max(vals), "range": max(vals) - min(vals)},
        "weakest": sorted(CRITERIA, key=lambda c: (s[c], -w[c]))[:3],
        "strongest": sorted(CRITERIA, key=lambda c: (-s[c], -w[c]))[:3],
        "contribution": {c: round(w[c] * s[c] / tw, 3) for c in CRITERIA},
    }


def selftest():
    all5 = {"scores": {c: 5 for c in CRITERIA}}
    assert score(all5)["overall"] == "5.00"
    assert score({"scores": {c: 10 for c in CRITERIA}})["overall"] == "10.00"
    assert score({"scores": {c: 1 for c in CRITERIA}})["overall"] == "1.00"
    gate = {"scores": dict({c: 9 for c in CRITERIA}, money=2)}
    assert score(gate)["overall"] == "5.00", score(gate)
    viol = {"scores": {c: 9 for c in CRITERIA}, "flags": {"violates_rules": True}}
    assert score(viol)["overall"] == "3.00"
    assert abs(sum(WEIGHTS.values()) - 100) == 0
    try:
        score({"scores": {"loop": 5}})
        raise SystemExit("expected failure")
    except ValueError:
        pass
    print("selftest ok")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        selftest()
    elif len(sys.argv) > 1 and sys.argv[1] == "--weights":
        print(json.dumps(WEIGHTS))
    else:
        src = sys.argv[1] if len(sys.argv) > 1 else "-"
        raw = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
        try:
            print(json.dumps(score(json.loads(raw)), indent=1))
        except ValueError as e:
            print("score.py: " + str(e), file=sys.stderr)
            sys.exit(2)
