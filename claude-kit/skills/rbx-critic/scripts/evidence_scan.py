#!/usr/bin/env python3
"""evidence_scan.py: evidence-before-claims check of a final report (stdlib only).

  python evidence_scan.py <report.md | -> [--game ID] [--scorer critic|builder] [--write GAME_FOLDER] [--strict]

The vault rule: no done, fixed or passes without a command and its output in the same report; should, probably and seems mean not verified; a subagent's
success claim is checked against the diff. The scan reads the report text and scores three checks (0-10, pass mark 7):
EV1 hedge words in claim lines, EV2 claim lines (and [met] criteria) with no evidence line near them, EV3 subagent success claims with no diff or re-run check.
Evidence = a backticked command, an exit code, PASS/FAIL, a path:line, or text after "evidence:". Code fences count as evidence for the claim above them.
Lines under NOT_CHECKED, PROBLEMS, NEEDS and SUGGESTED_NEXT and every [untested] line may hedge. Output: JSON in the format of comment_scan.py; with
--write GAME_FOLDER the record is saved as GAME_FOLDER/evidence-scan/gate.json, where rbx-bench finds it. Scored, never a block (exit 0 unless --strict).
"""
import json
import os
import re
import sys
import time

PASS_MIN = 7.0
HEDGE = re.compile(r"\b(should (work|pass|be fine|be ok|now)|probably|seems?|seemingly|appears? to|presumably|likely|i think|i believe|hopefully|ought to|supposedly|looks (fine|good|right|ok))\b", re.I)
CLAIM = re.compile(r"\b(done|fixed|pass|passes|passed|passing|works|working|verified|succeeds|succeeded|successful|success|complete|completed|resolved|all green)\b", re.I)
EVID = re.compile(r"`[^`\n]{3,}`|\brc\s*=\s*\d|\bexit(ed)?( code)?\s*\d|\bPASS\b|\bFAIL\b|\b\d+ (passed|failed|tests?|checks?)\b|\S+\.\w+:\d+|evidence:\s*\S{6,}")
SUBAGENT = re.compile(r"\b(sub-?agent|worker|builder|the agent|agent)\b.{0,60}\b(reported|said|says|claims?|claimed|confirmed|returned)\b.{0,60}\b(success|done|fixed|passe[sd]|complete|works)", re.I)
DIFFCHK = re.compile(r"git diff|\bdiff\b|re-?ran|re-?run|checked against|checked myself|verified myself|ls -l|\bhash\b|sha\d*", re.I)
QUIET = re.compile(r"^\s*(NOT_CHECKED|PROBLEMS|NEEDS|NEEDS_ROMAN|SUGGESTED_NEXT|NEXT)\b", re.I)
FIX = {"EV1": "state the check and its result instead of a hedge word, or mark the item untested",
       "EV2": "paste the command and an exact output excerpt next to the claim, or mark it [untested]",
       "EV3": "compare the subagent's claim with the diff or re-run its check yourself, and say so"}


def analyse(text):
    lines = text.replace("\r\n", "\n").split("\n")
    fence = [False] * len(lines)
    inside = False
    for i, ln in enumerate(lines):
        if ln.strip().startswith("```"):
            inside = not inside
            fence[i] = True
        elif inside:
            fence[i] = True
    quiet = False
    findings = {"EV1": [], "EV2": [], "EV3": []}
    claims = 0
    for i, ln in enumerate(lines):
        if fence[i] or not ln.strip():
            continue
        if QUIET.match(ln):
            quiet = True
        elif re.match(r"^\s*[A-Z_]{4,}:", ln):
            quiet = False
        if quiet or re.search(r"\[untested\]|\buntested\b", ln, re.I):
            continue
        near = lines[i:i + 3]
        if HEDGE.search(ln) and (CLAIM.search(ln) or re.match(r"^\s*(DONE|VERIFIED|CRITERIA|RESULT|HEADLINE)\b", ln, re.I)):
            findings["EV1"].append((i + 1, ln.strip()[:100]))
        if (CLAIM.search(ln) and not re.match(r"^\s*(RESULT|HEADLINE)\b", ln, re.I)) or re.match(r"^\s*\[met\]", ln):
            claims += 1
            ok = any(EVID.search(x) for x in near) or any(fence[j] for j in range(i, min(i + 3, len(lines))))
            if not ok:
                findings["EV2"].append((i + 1, ln.strip()[:100]))
        if SUBAGENT.search(ln) and not any(DIFFCHK.search(x) for x in lines[max(0, i - 2):i + 3]):
            findings["EV3"].append((i + 1, ln.strip()[:100]))
    return findings, claims


def build(text, game=None, scorer="critic"):
    findings, claims = analyse(text)
    ev1 = max(0.0, round(10.0 - 2.0 * len(findings["EV1"]), 1))
    ev2 = 10.0 if not claims else round(10.0 * (claims - len(findings["EV2"])) / claims, 1)
    ev3 = max(0.0, round(10.0 - 3.0 * len(findings["EV3"]), 1))
    checks = {"EV1": ev1, "EV2": ev2, "EV3": ev3}
    failing = [dict(path="report:%d" % ln, check=cid, found=t, fix=FIX[cid]) for cid in ("EV2", "EV1", "EV3") for ln, t in findings[cid][:4]]
    reasons = ["%s %.1f: %d line(s)" % (cid, checks[cid], len(findings[cid])) for cid in checks if findings[cid]]
    return dict(kind="evidence-scan", scorer=scorer, game=game, severity="medium", pass_min=PASS_MIN, scripted=True,
                result="pass" if min(checks.values()) >= PASS_MIN else "fail", checks=checks, reasons=reasons, failing=failing[:12],
                counts=dict(claims=claims, hedges=len(findings["EV1"]), claims_without_evidence=len(findings["EV2"]), subagent_unchecked=len(findings["EV3"])),
                suggested_fix="add the command and output excerpt to each claim; drop hedges" if reasons else "none", time=time.strftime("%Y-%m-%dT%H:%M:%S"))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    opts, paths, i = {"game": None, "scorer": "critic", "write": None}, [], 0
    while i < len(argv):
        if argv[i] in ("--game", "--scorer", "--write"):
            opts[argv[i][2:]] = argv[i + 1]
            i += 2
            continue
        if argv[i] == "-" or not argv[i].startswith("--"):
            paths.append(argv[i])
        i += 1
    if not paths:
        print("give the report file (or - for stdin)", file=sys.stderr)
        return 2
    if paths[0] == "-":
        text = sys.stdin.read()
    elif os.path.isfile(paths[0]):
        text = open(paths[0], encoding="utf-8", errors="replace").read()
    else:
        print("no such report: %s" % paths[0], file=sys.stderr)
        return 2
    rec = build(text, opts["game"], opts["scorer"])
    if opts["write"]:
        d = os.path.join(opts["write"], "evidence-scan")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "gate.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(rec, fh, indent=1)
            fh.write("\n")
    print(json.dumps(rec, indent=1))
    return 1 if ("--strict" in argv and rec["result"] != "pass") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
