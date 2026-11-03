#!/usr/bin/env python3
"""gate.py <gates.json> | --template | --selftest

Go/no-go arithmetic for a launch. The JSON is a list of gates: {"gate": str, "status": "pass|fail|waived|na", "evidence": str,
"owner": str, "waiver": str}. Rules the script enforces so the verdict cannot be talked into:
  - pass needs non-empty evidence (a command and its output, a path, a link, or a number with its source)
  - waived needs a non-empty waiver reason AND an owner (a person accepting the risk); waived gates are listed in the verdict
  - na needs a one-line reason in evidence
  - any fail, or any missing/unknown status, makes the verdict NO-GO
Verdict GO only if every gate is pass, waived (with reason) or na (with reason). Exit 0 GO, 1 NO-GO, 2 bad input.
"""
import json, sys

TEMPLATE = [
    ("Studio playtest: first minute, core loop, rejoin (2 devices incl. a phone)", "playtest-bot-writer / hand run"),
    ("Data: save, rejoin, shutdown (BindToClose), session lock, no dupe on trade or purchase", "datastore-schema-builder, exploit-audit"),
    ("Purchases: each product and pass tested with a test account; receipts idempotent", "gamepass-maker, devproduct-handler"),
    ("Security: remotes validated and rate-limited; no backdoors in free models", "exploit-audit, remote-guard-builder"),
    ("Performance: mobile frame time, memory, script time within budget", "game-optimizer, lag-hunter"),
    ("Mobile and console UI: touch targets, safe area, no overlap at 3 aspect ratios", "mobile-ui-audit"),
    ("Content rules: maturity questionnaire answered from the real features; paid random odds disclosed", "age-rating-prep"),
    ("Assets: every audio, image and model licensed or owned", "asset-license-checker"),
    ("Store page: title, description, thumbnails, icon final and policy-clean", "game-description-writer, thumbnail-maker"),
    ("Settings: devices, genre, access (public), max players, private servers decided", "experience settings"),
    ("Analytics: funnel + economy events arriving in a test session", "Analytics system"),
    ("Backup and rollback: version saved, restore tested", "version-history-keeper"),
    ("Monitoring plan for the first 72 hours: who watches what, stop rule", "post-launch-monitor"),
]
STATUSES = {"pass", "fail", "waived", "na"}


def evaluate(gates):
    problems, rows = [], []
    for i, g in enumerate(gates, 1):
        name = str(g.get("gate", "")).strip() or "gate %d" % i
        st = str(g.get("status", "")).strip().lower()
        ev = str(g.get("evidence", "")).strip()
        wv = str(g.get("waiver", "")).strip()
        owner = str(g.get("owner", "")).strip()
        why = None
        if st not in STATUSES:
            why = "status missing or unknown (%r)" % st
        elif st == "fail":
            why = "FAILED"
        elif st == "pass" and not ev:
            why = "pass without evidence"
        elif st == "na" and not ev:
            why = "na without a reason"
        elif st == "waived" and not (wv and owner):
            why = "waived without a reason and an accountable owner"
        rows.append((name, st or "?", why))
        if why:
            problems.append("%s: %s" % (name, why))
    waived = [r[0] for r in rows if r[1] == "waived" and not r[2]]
    return ("GO" if not problems else "NO-GO"), problems, waived, rows


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if "--template" in argv:
        print(json.dumps([{"gate": g, "status": "", "evidence": "", "owner": "", "waiver": "", "how": h} for g, h in TEMPLATE], indent=2))
        return 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    try:
        gates = json.load(open(argv[0], encoding="utf-8"))
        assert isinstance(gates, list) and gates
    except Exception as e:
        print("bad input: %s" % e)
        return 2
    verdict, problems, waived, rows = evaluate(gates)
    for name, st, why in rows:
        print("%-7s %s%s" % (st.upper(), name, "  <- " + why if why else ""))
    if waived:
        print("WAIVED (risk accepted): " + "; ".join(waived))
    print("VERDICT: %s%s" % (verdict, "" if verdict == "GO" else " (%d blocking)" % len(problems)))
    return 0 if verdict == "GO" else 1


def selftest():
    ok = [{"gate": "a", "status": "pass", "evidence": "lune run: 8 passed"}, {"gate": "b", "status": "na", "evidence": "no purchases in v1"},
          {"gate": "c", "status": "waived", "waiver": "console UI after launch", "owner": "Roman"}]
    assert evaluate(ok)[0] == "GO" and evaluate(ok)[2] == ["c"]
    for bad in (
        [{"gate": "a", "status": "pass", "evidence": ""}],
        [{"gate": "a", "status": "fail", "evidence": "x"}],
        [{"gate": "a", "status": "waived", "waiver": "later"}],
        [{"gate": "a", "status": "maybe", "evidence": "x"}],
        [{"gate": "a", "evidence": "x"}],
        [{"gate": "a", "status": "na"}],
    ):
        assert evaluate(bad)[0] == "NO-GO", bad
    assert len(TEMPLATE) == 13
    print("selftest ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
