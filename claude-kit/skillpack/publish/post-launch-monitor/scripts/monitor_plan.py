#!/usr/bin/env python3
"""monitor_plan.py <plan.json> | --template | --selftest

First-72-hours monitoring plan validator and schedule printer. No threshold is built in: healthy/alarm values come from the game's own
test sessions or benchmarks YOU name in "basis" (an invented threshold is a FAIL). Plan JSON:
  {"launch": "2026-11-10 18:00", "checkpoints_h": [1, 6, 24, 48, 72],
   "metrics": [{"name": "Crash/error rate", "source": "Creator Hub > Analytics > Performance", "healthy": "...", "alarm": "...",
                "basis": "playtest run of 2026-11-02", "action": "pause updates; roll back", "owner": "Roman"}],
   "rollback": {"trigger": "...", "how": "Version History restore + publish + restart servers", "restore_point": "..."}}
Checks: >= 4 metrics; each has source, healthy, alarm, basis, action, owner; checkpoints include one <= 2 h and one >= 72 h; rollback
trigger, how and restore_point present; error/crash, data-save failures, purchases and retention-type metrics covered (by name words).
Prints the schedule (checkpoint -> time -> metrics to read). Exit 1 on FAIL, 2 on bad input.
"""
import datetime
import json
import sys

NEED = {"errors": ("error", "crash", "exception"), "data": ("save", "datastore", "data"), "purchases": ("purchase", "receipt", "revenue", "robux"),
        "retention": ("retention", "d1", "playtime", "session", "visits", "ccu")}


def check(p):
    out = []
    ms = p.get("metrics") or []
    if len(ms) < 4:
        out.append(("FAIL", "only %d metrics; need at least 4" % len(ms)))
    for m in ms:
        miss = [k for k in ("source", "healthy", "alarm", "basis", "action", "owner") if not str(m.get(k, "")).strip()]
        if miss:
            out.append(("FAIL", "metric %r missing %s (no invented thresholds: name the basis)" % (m.get("name"), ", ".join(miss))))
    text = " ".join(str(m.get("name", "")).lower() for m in ms)
    for k, words in NEED.items():
        if not any(w in text for w in words):
            out.append(("WARN", "no metric covers %s" % k))
    cps = p.get("checkpoints_h") or []
    if not cps or min(cps) > 2:
        out.append(("FAIL", "need a checkpoint within the first 2 hours"))
    if not cps or max(cps) < 72:
        out.append(("FAIL", "need a checkpoint at 72 hours"))
    rb = p.get("rollback") or {}
    for k in ("trigger", "how", "restore_point"):
        if not str(rb.get(k, "")).strip():
            out.append(("FAIL", "rollback.%s missing" % k))
    if not any(lv == "FAIL" for lv, _ in out):
        out.append(("OK", "plan complete (values still need to be true)"))
    return out


def schedule(p):
    rows = []
    try:
        t0 = datetime.datetime.strptime(p.get("launch", ""), "%Y-%m-%d %H:%M")
    except ValueError:
        t0 = None
    for h in sorted(p.get("checkpoints_h") or []):
        when = (t0 + datetime.timedelta(hours=h)).strftime("%Y-%m-%d %H:%M") if t0 else "+%dh" % h
        rows.append("%-6s %s  read: %s" % ("+%dh" % h, when, "; ".join(str(m.get("name")) for m in p.get("metrics") or [])))
    return rows


def template():
    blank = {"name": "", "source": "", "healthy": "", "alarm": "", "basis": "", "action": "", "owner": ""}
    return {"launch": "YYYY-MM-DD HH:MM", "checkpoints_h": [1, 6, 24, 48, 72],
            "metrics": [dict(blank, name=n) for n in ("Error rate", "Data save failures", "Purchases and receipts", "D1 retention / playtime")],
            "rollback": {"trigger": "", "how": "", "restore_point": ""}}


def selftest():
    t = template()
    assert any(x[0] == "FAIL" for x in check(t)), "blank template must not pass"
    assert len(json.dumps(t)) > 100
    m = lambda n: {"name": n, "source": "s", "healthy": "h", "alarm": "a", "basis": "b", "action": "x", "owner": "o"}
    good = {"launch": "2026-11-10 18:00", "checkpoints_h": [1, 24, 72], "metrics": [m("Error rate"), m("Data save failures"), m("Purchases"), m("D1 retention")],
            "rollback": {"trigger": "t", "how": "h", "restore_point": "r"}}
    assert [x[0] for x in check(good)] == ["OK"], check(good)
    assert schedule(good)[0].startswith("+1h    2026-11-10 19:00")
    bad = {"checkpoints_h": [6], "metrics": [dict(m("Error rate"), basis="")], "rollback": {}}
    f = [x for x in check(bad) if x[0] == "FAIL"]
    assert len(f) == 7, f
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--template" in argv:
        print(json.dumps(template(), indent=2))
        return 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    try:
        p = json.load(open(argv[0], encoding="utf-8"))
        assert isinstance(p, dict)
    except Exception as e:
        print("bad input: %s" % e)
        return 2
    rows = check(p)
    for lv, m in rows:
        print("[%s] %s" % (lv, m))
    for r in schedule(p):
        print(r)
    return 1 if any(r[0] == "FAIL" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
