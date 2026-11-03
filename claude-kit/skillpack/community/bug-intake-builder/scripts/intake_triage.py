#!/usr/bin/env python3
"""intake_triage.py - dedupe and rank community bug reports. Stdlib only.

  python intake_triage.py reports.csv [--sim 0.6]
  python intake_triage.py --selftest

CSV columns: title, steps, device, severity (1 cosmetic, 2 annoying, 3 breaks a feature, 4 blocker/data loss/crash), reporter.
Reports whose titles share at least --sim of their words (Jaccard) are one bug. Priority = max severity * sqrt(report count).
Reports missing steps or device are listed as INCOMPLETE (ask the reporter once, in public or the ticket, never by DM to a minor).
Exit 0 always except for unreadable input (2): this ranks, it does not judge.
"""
import csv
import math
import re
import sys

STOP = {"the", "a", "an", "is", "in", "on", "when", "i", "my", "it", "to", "of", "and", "with", "after", "bug", "game"}


def toks(t):
    return {w for w in re.findall(r"[a-z0-9]+", (t or "").lower()) if w not in STOP and len(w) > 1}


def triage(rows, sim=0.6):
    groups = []
    for r in rows:
        t = toks(r.get("title"))
        for g in groups:
            u = t | g["toks"]
            if u and len(t & g["toks"]) / len(u) >= sim:
                g["rows"].append(r)
                g["toks"] |= t
                break
        else:
            groups.append({"toks": set(t), "rows": [r]})
    out = []
    for g in groups:
        rs = g["rows"]
        sev = max(int((r.get("severity") or "1").strip() or 1) for r in rs)
        out.append({
            "title": min((r.get("title") or "" for r in rs), key=len),
            "count": len(rs),
            "severity": sev,
            "priority": round(sev * math.sqrt(len(rs)), 2),
            "incomplete": [r.get("reporter", "?") for r in rs if not (r.get("steps") or "").strip() or not (r.get("device") or "").strip()],
        })
    return sorted(out, key=lambda x: (-x["priority"], x["title"]))


def selftest():
    rows = [
        {"title": "Pet disappears after trade", "steps": "trade", "device": "pc", "severity": "3", "reporter": "a"},
        {"title": "pet disappears after trading", "steps": "x", "device": "ios", "severity": "4", "reporter": "b"},
        {"title": "Pet vanishes in trade", "steps": "", "device": "", "severity": "3", "reporter": "c"},
        {"title": "Typo in shop header", "steps": "open shop", "device": "pc", "severity": "1", "reporter": "d"},
    ]
    t = triage(rows, 0.4)
    assert len(t) == 2, t
    assert t[0]["count"] == 3 and t[0]["severity"] == 4 and t[0]["priority"] == round(4 * math.sqrt(3), 2), t[0]
    assert t[0]["incomplete"] == ["c"], t[0]
    assert t[1]["priority"] == 1.0
    print("selftest ok (5 asserts)")
    return 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv:
        print(__doc__)
        return 2
    sim = float(argv[argv.index("--sim") + 1]) if "--sim" in argv else 0.6
    with open(argv[0], encoding="utf-8-sig", newline="") as f:
        res = triage(list(csv.DictReader(f)), sim)
    for x in res:
        print("P%-6s sev%d x%-3d %s%s" % (x["priority"], x["severity"], x["count"], x["title"], "  INCOMPLETE: " + ",".join(x["incomplete"]) if x["incomplete"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
