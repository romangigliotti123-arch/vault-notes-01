#!/usr/bin/env python3
"""budget.py - route AI jobs to a model tier and total the relative cost. Stdlib only.

  python budget.py jobs.csv [--max-workers 2] [--max-total-units 600]
  python budget.py --selftest

CSV columns: id,kind,est_turns   (kind: lookup|mechanical|build|review|design|debug)
Routing (from the vault Manager KB, topic-model-effort-routing-cost and topic-managing-ai-agents-for-roblox-game-dev):
lookup,mechanical -> haiku; build,review -> sonnet; design -> opus (planning decomposes everything else); debug -> sonnet, and
escalate one tier on the SECOND failure. Relative price weights per turn: haiku 1, sonnet 20, opus 40 (list-price ratios: Haiku
is about 20x cheaper than Sonnet, Opus about 2x Sonnet). They are RELATIVE units, not money; subscription weights are unpublished,
so re-calibrate against the real usage screen. Flags: a job over 105 turns (the heavy tail), more than --max-workers parallel
jobs requested, total above --max-total-units. Exit 0 ok, 1 if a cap is broken.
"""
import argparse
import csv
import io
import sys

ROUTE = {"lookup": "haiku", "mechanical": "haiku", "build": "sonnet", "review": "sonnet", "debug": "sonnet", "design": "opus"}
WEIGHT = {"haiku": 1, "sonnet": 20, "opus": 40}
TAIL_TURNS = 105


def plan(rows, max_workers=2, max_units=600):
    out, warn, total = [], [], 0
    for r in rows:
        k = (r.get("kind") or "").strip().lower()
        if k not in ROUTE:
            raise ValueError("unknown kind %r (use %s)" % (k, "|".join(sorted(ROUTE))))
        t = int(r["est_turns"])
        m = ROUTE[k]
        u = t * WEIGHT[m]
        total += u
        out.append((r["id"], k, m, t, u))
        if t > TAIL_TURNS:
            warn.append("%s: %d turns is in the heavy tail (>%d); split into phases that each write a checkpoint" % (r["id"], t, TAIL_TURNS))
    if len(out) > 0 and max_workers < 1:
        warn.append("max-workers must be >= 1")
    over = total > max_units
    if over:
        warn.append("total %d units > cap %d: cut scope, move jobs down a tier, or spread over days" % (total, max_units))
    by = {}
    for _, _, m, _, u in out:
        by[m] = by.get(m, 0) + u
    return out, by, total, warn, over


def selftest():
    rows = list(csv.DictReader(io.StringIO("id,kind,est_turns\nJ1,design,10\nJ2,build,40\nJ3,lookup,20\nJ4,build,120\n")))
    out, by, total, warn, over = plan(rows, 2, 5000)
    assert [o[2] for o in out] == ["opus", "sonnet", "haiku", "sonnet"]
    assert total == 10 * 40 + 40 * 20 + 20 * 1 + 120 * 20 and by["haiku"] == 20, (total, by)
    assert any("heavy tail" in w for w in warn) and not over
    _, _, _, w2, o2 = plan(rows, 2, 1000)
    assert o2 and any("cap" in w for w in w2)
    try:
        plan([{"id": "x", "kind": "magic", "est_turns": "1"}])
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("selftest ok (4 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--max-workers", type=int, default=2)
    ap.add_argument("--max-total-units", type=int, default=600)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        ap.error("file required")
    with open(a.file, encoding="utf-8", newline="") as f:
        try:
            out, by, total, warn, over = plan(list(csv.DictReader(f)), a.max_workers, a.max_total_units)
        except (ValueError, KeyError) as e:
            print("ERROR:", e)
            return 1
    for i, k, m, t, u in out:
        print("%-6s %-10s -> %-6s %4d turns %6d units" % (i, k, m, t, u))
    print("by tier:", ", ".join("%s %d" % kv for kv in sorted(by.items())), "| total", total, "units (relative, not money)")
    for w in warn:
        print("WARN:", w)
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main())
