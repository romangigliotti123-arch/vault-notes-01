#!/usr/bin/env python3
"""tune_check.py: ledger for rbx-tune runs and the gate that validates it (stdlib only).

  python tune_check.py init <run-dir> --metric NAME --direction up|down --evaluator FILE [--budget N] [--target X]
  python tune_check.py log <run-dir> --change TEXT --before X --after Y --status keep|discard|crash [--gates-pass true|false]
  python tune_check.py baseline <run-dir> --value X
  python tune_check.py check <game folder | run-dir> [--game ID] [--scorer critic|builder] [--write GAME_FOLDER] [--claims]

A run is <Games/slug>/tune/<run-id>/ with run.json (metric, direction, evaluator, evaluator_sha256, budget, target) and results.tsv
(n, change, metric_before, metric_after, status, gates_pass). Row 0 is the baseline. `check` scores every run: TN1 baseline row first, TN2 every keep improved the
metric in the declared direction (strictly) from the best value so far, TN3 evaluator file unchanged (sha256), TN4 experiment rows within budget (hard cap 25),
TN5 gates_pass true on every keep. With --claims, GAME.md / decisions.md / playtests that say balanced, tuned, optimised or improved without any run add TN6
(unmeasured claim). Writes <game>/tune/gate.json (kind tune-ledger), found by rbx-bench; scored, never blocking; exit 0 unless --strict.
"""
import glob
import hashlib
import json
import os
import re
import sys
import time

HARD_CAP = 25
COLS = ["n", "change", "metric_before", "metric_after", "status", "gates_pass"]
CLAIM = re.compile(r"\b(balanced|tuned|optimi[sz]ed|retuned|rebalanced)\b|\b(improved|reduced|faster)\b.{0,40}\b(by|to)\s+\d", re.I)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def read_rows(path):
    rows = []
    if not os.path.isfile(path):
        return rows
    for i, ln in enumerate(open(path, encoding="utf-8").read().split("\n")):
        if i == 0 or not ln.strip():
            continue
        c = ln.split("\t")
        c += [""] * (6 - len(c))
        rows.append(dict(zip(COLS, c[:6])))
    return rows


def append_row(run, row):
    p = os.path.join(run, "results.tsv")
    new = not os.path.isfile(p)
    with open(p, "a", encoding="utf-8", newline="\n") as f:
        if new:
            f.write("\t".join(COLS) + "\n")
        f.write("\t".join(str(row[c]) for c in COLS) + "\n")


def check_run(run):
    errs = {k: [] for k in ("TN1", "TN2", "TN3", "TN4", "TN5")}
    try:
        meta = json.load(open(os.path.join(run, "run.json"), encoding="utf-8"))
    except (OSError, ValueError):
        meta = {}
        errs["TN1"].append("run.json missing or unreadable")
    rows = read_rows(os.path.join(run, "results.tsv"))
    if not rows or rows[0]["status"] != "baseline" or rows[0]["n"] != "0" or num(rows[0]["metric_after"]) is None:
        errs["TN1"].append("row 0 must be the baseline run with a numeric metric")
    sign = 1.0 if meta.get("direction", "up") == "up" else -1.0
    best = num(rows[0]["metric_after"]) if rows else None
    for r in rows[1:]:
        before, after = num(r["metric_before"]), num(r["metric_after"])
        if r["status"] not in ("keep", "discard", "crash"):
            errs["TN2"].append("row %s: status %r is not keep, discard or crash" % (r["n"], r["status"]))
        if r["status"] == "keep":
            if after is None or best is None or sign * (after - best) <= 0:
                errs["TN2"].append("row %s: keep without a strict improvement over %s (after %s)" % (r["n"], best, r["metric_after"]))
            else:
                best = after
            if r["gates_pass"].strip().lower() != "true":
                errs["TN5"].append("row %s: keep while gates_pass is %r" % (r["n"], r["gates_pass"]))
    budget = int(meta.get("budget") or 10)
    if len(rows) - 1 > min(budget, HARD_CAP):
        errs["TN4"].append("%d experiments but the budget is %d (hard cap %d)" % (len(rows) - 1, budget, HARD_CAP))
    ev = meta.get("evaluator")
    if not ev:
        errs["TN3"].append("run.json has no evaluator")
    else:
        for cand in (ev, os.path.join(run, ev)):
            if os.path.isfile(cand):
                if sha(cand) != meta.get("evaluator_sha256"):
                    errs["TN3"].append("evaluator %s changed since the baseline (sha256 differs)" % ev)
                break
        else:
            errs["TN3"].append("evaluator %s not found" % ev)
    return errs, meta, rows


def check(folder, game=None, scorer="critic", claims=False):
    tune = os.path.join(folder, "tune")
    runs = [d for d in sorted(glob.glob(os.path.join(tune, "*"))) if os.path.isdir(d)] if os.path.isdir(tune) else (
        [folder] if os.path.isfile(os.path.join(folder, "run.json")) else [])
    tot = {k: [] for k in ("TN1", "TN2", "TN3", "TN4", "TN5")}
    summary = []
    for r in runs:
        errs, meta, rows = check_run(r)
        for k, v in errs.items():
            tot[k] += ["%s: %s" % (os.path.basename(r), x) for x in v]
        kept = sum(1 for x in rows[1:] if x["status"] == "keep")
        summary.append(dict(run=os.path.basename(r), metric=meta.get("metric"), experiments=max(0, len(rows) - 1), kept=kept,
                            baseline=rows[0]["metric_after"] if rows else None))
    checks = {k: (10.0 if not v else max(0.0, 6.0 - 2.0 * (len(v) - 1))) for k, v in tot.items()}
    reasons = [x for v in tot.values() for x in v][:12]
    if claims:
        hit = []
        for pat in ("GAME.md", "decisions.md", os.path.join("playtests", "*.md")):
            for p in glob.glob(os.path.join(folder, pat)):
                for i, ln in enumerate(open(p, encoding="utf-8", errors="replace").read().split("\n"), 1):
                    if CLAIM.search(ln):
                        hit.append("%s:%d" % (os.path.relpath(p, folder).replace(os.sep, "/"), i))
        if hit and not runs:
            checks["TN6"] = 5.0
            reasons.append("unmeasured claim (balanced/tuned/optimised/improved) with no tune ledger: " + ", ".join(hit[:4]))
        elif hit:
            checks["TN6"] = 10.0
    fl = [dict(path=x.split(":")[0], check=k, found=x, fix="repair the ledger or redo the run with rbx-tune") for k, v in tot.items() for x in v][:20]
    return dict(kind="tune-ledger", scorer=scorer, game=game, severity="medium", pass_min=7.0, scripted=True,
                result="pass" if min(checks.values()) >= 7.0 else "fail", checks=checks, reasons=reasons, failing=fl,
                counts=dict(runs=len(runs)), runs=summary, suggested_fix="none" if min(checks.values()) >= 7.0 else "repair the ledger or measure the claim with rbx-tune",
                time=time.strftime("%Y-%m-%dT%H:%M:%S")), bool(runs) or "TN6" in checks


def opt(argv, name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def main(argv):
    if len(argv) < 2 or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, run = argv[0], argv[1]
    if cmd == "init":
        ev = opt(argv, "--evaluator")
        if not ev or not os.path.isfile(ev):
            print("evaluator file not found", file=sys.stderr)
            return 2
        os.makedirs(run, exist_ok=True)
        meta = dict(metric=opt(argv, "--metric"), direction=opt(argv, "--direction", "up"), evaluator=os.path.abspath(ev), evaluator_sha256=sha(ev),
                    budget=min(int(opt(argv, "--budget", "10")), HARD_CAP), target=num(opt(argv, "--target")), created=time.strftime("%Y-%m-%dT%H:%M:%S"))
        json.dump(meta, open(os.path.join(run, "run.json"), "w", encoding="utf-8", newline="\n"), indent=1)
        print(json.dumps(meta))
        return 0
    if cmd == "baseline":
        append_row(run, dict(n=0, change="baseline", metric_before="", metric_after=opt(argv, "--value"), status="baseline", gates_pass="true"))
        return 0
    if cmd == "log":
        n = len(read_rows(os.path.join(run, "results.tsv")))
        append_row(run, dict(n=n, change=(opt(argv, "--change") or "").replace("\t", " ").replace("\n", " "), metric_before=opt(argv, "--before"),
                             metric_after=opt(argv, "--after"), status=opt(argv, "--status"), gates_pass=opt(argv, "--gates-pass", "true")))
        return 0
    if cmd == "check":
        rec, found = check(run, opt(argv, "--game"), opt(argv, "--scorer", "critic"), "--claims" in argv)
        w = opt(argv, "--write")
        if w and found:
            os.makedirs(os.path.join(w, "tune"), exist_ok=True)
            with open(os.path.join(w, "tune", "gate.json"), "w", encoding="utf-8", newline="\n") as fh:
                json.dump(rec, fh, indent=1)
                fh.write("\n")
        print(json.dumps(rec, indent=1))
        return 1 if ("--strict" in argv and rec["result"] == "fail") else 0
    print("unknown command", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
