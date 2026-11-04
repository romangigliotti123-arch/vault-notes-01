#!/usr/bin/env python3
"""code_gates.py: the single runner of the code gates (stdlib only). One call, one line of result.

  python code_gates.py <project folder> [--game ID] [--scorer builder|critic] [--write GAME_FOLDER] [--strict]

Runs, in this order: comment_scan (CM1-CM3), scope_scan (SC1-SC5), static_scan --gate (SEC1-SEC5), the fix-loop ledger check (FL1: every
GAME_FOLDER/bugfix/<id>.md has a RED and a GREEN block) and tune_check (TN1-TN6, only when a tune/ folder or an unmeasured tuning claim exists).
Prints one line, for example
  CODE GATES: comment 9.2 pass | scope 8.1 pass | security 6.0 FAIL(2 S1) | fixes 10.0 pass | tune n/a
and the worst findings under it. With --write GAME_FOLDER each gate saves its gate.json (comment-scan/, scope-scan/, security-scan/, bugfix/, tune/) where
game-dev-benchmark finds it, plus GAME_FOLDER/code-gates/run.json, the proof that the gates ran (scorer, time, per-gate score). Policy: the findings are SCORED and
never block; "not run" is what verdict.py caps (at most NOT YET, `playable prototype, code gates not run`). The builder runs it with --scorer builder
before reporting; the critic runs its own with --scorer critic. Exit 0 unless --strict.
"""
import glob
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.dirname(os.path.dirname(HERE))
REQUIRED_RUN = ("comment", "scope", "security")


def load(mod, *parts):
    sys.path.insert(0, os.path.join(*parts))
    try:
        return __import__(mod)
    except Exception:
        return None
    finally:
        sys.path.pop(0)


def fix_gate(folder, game=None, scorer="critic"):
    d = os.path.join(folder, "bugfix")
    ledgers = [p for p in sorted(glob.glob(os.path.join(d, "*.md"))) if os.path.basename(p).lower() != "readme.md"]
    if not ledgers:
        return None
    bad, failing = 0, []
    for p in ledgers:
        t = open(p, encoding="utf-8", errors="replace").read()
        parts = re.split(r"^#{1,3}\s+", t, flags=re.M)
        miss = [name for name in ("RED", "GREEN")
                if not any(s.upper().startswith(name) and re.search(r"```[^\n]*\n\s*\S[^\n]*\n(?:[^\n]*\n)*?\s*```", s) for s in parts)]
        if miss:
            bad += 1
            failing.append(dict(path=os.path.relpath(p, folder).replace(os.sep, "/"), check="FL1", found="no %s block with command output" % "/".join(miss),
                                fix="reproduce first: record the failing command and output under ## RED, the passing one under ## GREEN"))
    score = round(10.0 * (len(ledgers) - bad) / len(ledgers), 1)
    return dict(kind="bugfix-ledger", scorer=scorer, game=game, severity="medium", pass_min=7.0, scripted=True, result="pass" if score >= 7.0 else "fail",
                checks={"FL1": score}, reasons=["FL1 %.1f: %d of %d bug ledgers lack a RED or GREEN block" % (score, bad, len(ledgers))] if bad else [],
                failing=failing, counts=dict(ledgers=len(ledgers), incomplete=bad), suggested_fix="complete the ledgers (game-dev-playtest, Fix loop)" if bad else "none",
                time=time.strftime("%Y-%m-%dT%H:%M:%S"))


def mean(rec):
    v = [x for x in rec["checks"].values() if x is not None]
    return round(sum(v) / len(v), 1) if v else 0.0


def put(folder, sub, rec):
    os.makedirs(os.path.join(folder, sub), exist_ok=True)
    with open(os.path.join(folder, sub, "gate.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rec, fh, indent=1)
        fh.write("\n")


def run(project, game=None, scorer="critic", folder=None):
    recs, missing = {}, []
    cs = load("comment_scan", HERE)
    if cs:
        recs["comment"] = ("comment-scan", cs.build([project], game, scorer, base=project if os.path.isdir(project) else None))
    else:
        missing.append("comment")
    sc = load("scope_scan", HERE)
    if sc:
        recs["scope"] = ("scope-scan", sc.build(project, game, scorer))
    else:
        missing.append("scope")
    ss = load("static_scan", SKILLS, "game-dev-playtest", "scripts")
    if ss:
        recs["security"] = ("security-scan", ss.gate(project, game, scorer))
    else:
        missing.append("security")
    if folder:
        fg = fix_gate(folder, game, scorer)
        if fg:
            recs["fixes"] = ("bugfix", fg)
        tc = load("tune_check", SKILLS, "game-dev-tune", "scripts")
        if tc:
            tg, found = tc.check(folder, game, scorer, True)
            if found:
                recs["tune"] = ("tune", tg)
    parts = []
    for name in ("comment", "scope", "security", "fixes", "tune"):
        if name not in recs:
            parts.append("%s %s" % (name, "NOT RUN" if name in missing else "n/a"))
            continue
        rec = recs[name][1]
        extra = ""
        if rec["result"] != "pass":
            s1 = rec.get("counts", {}).get("s1")
            extra = "(%d S1)" % s1 if s1 else ""
        parts.append("%s %.1f %s%s" % (name, mean(rec), "pass" if rec["result"] == "pass" else "FAIL", extra))
    line = "CODE GATES: " + " | ".join(parts)
    if folder:
        for _, (sub, rec) in recs.items():
            put(folder, sub, rec)
        os.makedirs(os.path.join(folder, "code-gates"), exist_ok=True)
        meta = dict(kind="code-gates", scorer=scorer, game=game, project=os.path.abspath(project), time=time.strftime("%Y-%m-%dT%H:%M:%S"), line=line,
                    ran=sorted(recs), missing_scripts=missing, gates={k: dict(score=mean(v[1]), result=v[1]["result"]) for k, v in recs.items()})
        with open(os.path.join(folder, "code-gates", "run.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(meta, fh, indent=1)
            fh.write("\n")
    return line, recs


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
        if not argv[i].startswith("--"):
            paths.append(argv[i])
        i += 1
    if not paths or not os.path.exists(paths[0]):
        print("give the project folder", file=sys.stderr)
        return 2
    line, recs = run(paths[0], opts["game"], opts["scorer"], opts["write"])
    print(line)
    worst = []
    for _, (_, rec) in recs.items():
        worst += [f for f in rec.get("failing", [])][:3]
    for f in worst[:8]:
        print("  %s %s: %s -> %s" % (f.get("check", ""), f.get("path", ""), str(f.get("found", ""))[:90], str(f.get("fix", ""))[:70]))
    return 1 if ("--strict" in argv and any(r["result"] != "pass" for _, (_, r) in recs.items())) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
