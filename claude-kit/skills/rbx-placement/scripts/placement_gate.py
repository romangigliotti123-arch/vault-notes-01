#!/usr/bin/env python3
"""placement_gate.py: deterministic pass/fail of the placement gate (checks P1-P7 in references/checks.md). Nobody eyeballs the result.

  python placement_gate.py <scan.json> [--project DIR] [--write Games/<slug>] [--scorer critic]
  python placement_gate.py ingest <console-output.txt> --write Games/<slug> [--scorer builder|critic] [--game SLUG] [--name scan-builder]
  python placement_gate.py log <report.json | console-output.txt | -> --write Games/<slug>        store the per-placement report(s) of Placement.place/verify
  python placement_gate.py recheck <report-or-scan.json>                                          re-run P1-P7 from the stored inputs (placement_ref.py)

scan.json (written by Placement.scan, or built by `ingest` from the PLACEMENT_MODEL / PLACEMENT_SCAN console lines):
  {"kind": "placement-scan", "version": 1, "game": "slug", "scorer": "builder" | "critic", "datamodel": "Edit", "captured_at": "2026-11-04T10:00:00Z",
   "root": "Workspace", "models_total": 42, "models": [<report per placed model>], "skipped": [{"path": ..., "reason": ...}], "fingerprint": "ab12cd34"}
report (per model): {"path", "kind", "status", "failed": [..], "waived": [..], "checks": {"P1": {"status": pass|fail|skip, "issues": [..], "fixes": [..], "waived": "reason"?}, ... "P7"},
   "inputs": {snap, env, intent, opts}?  (when present the gate RE-RUNS the checks with the Python reference and compares)}

PASS needs ALL of: a scan of the whole map (models_total == len(models) > 0, or a stated reason `no_world`); every model's status recomputed from its checks (the
status field is never trusted) is pass; waived checks carry a reason of >= 10 characters and waivers/ignores stay under 10% of the models (min 2); no ignored
object without a reason; a scan not older than the newest Luau source (--project) and not older than the newest per-placement report; the latest per-placement
report of every path (placements/*.json under --write) is pass; reports that carry inputs re-check identically. --scorer critic additionally demands scorer == critic
(the critic's own fresh scan decides; a builder's scan is evidence only). Importable: evaluate(scan, base_dir, project, require_scorer) -> dict(status, reasons, failing, label, counts).
"""
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import placement_ref  # noqa: E402

CHECKS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
NOT_VERIFIED = "playable prototype, placement not verified"
VERIFIED = "placement verified (placement gate passed)"
MIN_WAIVER = 10
LINE = re.compile(r"(PLACEMENT_MODEL|PLACEMENT_SCAN)\s+(\{.*\})\s*$")


def _newest_source(project):
    newest = 0.0
    for root, dirs, files in os.walk(project):
        dirs[:] = [d for d in dirs if d.lower() not in ("packages", "vendor", "node_modules", ".git", "build", "docs")]
        for f in files:
            if f.endswith((".luau", ".lua")):
                newest = max(newest, os.path.getmtime(os.path.join(root, f)))
    return newest


def _ts(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc).timestamp()
    except Exception:
        return None


def model_status(rep):
    """Recompute from the checks. -> (status, failed, waived_without_reason)"""
    failed, bad_waiver = [], []
    checks = rep.get("checks") or {}
    for cid in CHECKS:
        c = checks.get(cid)
        if not isinstance(c, dict) or c.get("status") not in ("pass", "fail", "skip"):
            failed.append(cid + "(missing)")
            continue
        if c["status"] == "fail":
            w = c.get("waived")
            if w is None:
                failed.append(cid)
            elif len(str(w).strip()) < MIN_WAIVER:
                bad_waiver.append(cid)
                failed.append(cid)
    return ("fail" if failed else "pass"), failed, bad_waiver


def recheck(rep):
    """-> list of differences between the stored checks and a fresh run of the Python reference on rep['inputs'] (empty when equal or no inputs)."""
    inp = rep.get("inputs")
    if not isinstance(inp, dict) or "snap" not in inp:
        return None
    fresh = placement_ref.verify(inp["snap"], inp.get("intent") or {}, inp.get("env") or {}, inp.get("opts") or {})
    diffs = []
    for cid in CHECKS:
        a = (rep.get("checks") or {}).get(cid, {}).get("status")
        b = fresh["checks"][cid]["status"]
        if a != b:
            diffs.append("%s stored %s, re-check %s" % (cid, a, b))
    return diffs


def _first_fix(rep, cid):
    c = (rep.get("checks") or {}).get(cid) or {}
    fx = c.get("fixes") or []
    if isinstance(fx, list) and fx:
        f = fx[0]
        return "%s %s" % (f.get("action"), json.dumps({k: v for k, v in f.items() if k not in ("action", "note")}))
    return ""


def evaluate(scan, base_dir=".", project=None, require_scorer=None):
    reasons, failing = [], []
    counts = dict(models=0, pass_=0, fail=0, waived=0, rechecked=0, ignored=0, unverified=0)
    if not isinstance(scan, dict) or scan.get("kind") != "placement-scan":
        return dict(status="skipped", reasons=["no placement scan recorded (run rbx-placement: Placement.scan over the whole map)"], failing=[], label=NOT_VERIFIED, counts=counts)
    models = scan.get("models")
    if not isinstance(models, list):
        models = []
    total = scan.get("models_total")
    counts["models"] = len(models)
    if scan.get("version") != 1:
        reasons.append("unknown scan version %r" % scan.get("version"))
    if require_scorer and scan.get("scorer") != require_scorer:
        reasons.append("scan was made by %r, the verdict needs a fresh scan made by %r" % (scan.get("scorer"), require_scorer))
    if total != len(models):
        reasons.append("models_total %r does not match the %d model report(s) in the file (truncated or edited?)" % (total, len(models)))
    if not models:
        nw = scan.get("no_world")
        if not (isinstance(nw, str) and len(nw.strip()) >= MIN_WAIVER):
            reasons.append("the scan contains no placed models (wrong root? empty map?). A game with no world must say why in `no_world`")
    paths = set()
    for rep in models:
        if not isinstance(rep, dict) or not rep.get("path"):
            reasons.append("a model report has no path")
            continue
        p = rep["path"]
        if p in paths:
            reasons.append("duplicate report for " + p)
        paths.add(p)
        st, failed, bad_waiver = model_status(rep)
        if rep.get("status") != st:
            reasons.append("%s: stored status %r but its checks give %r" % (p, rep.get("status"), st))
        for cid in bad_waiver:
            reasons.append("%s: waiver of %s has no reason (>= %d characters)" % (p, cid, MIN_WAIVER))
        diffs = recheck(rep)
        if diffs is not None:
            counts["rechecked"] += 1
            if diffs:
                reasons.append("%s: re-check from the stored inputs differs: %s" % (p, "; ".join(diffs)))
                st = "fail"
        counts["waived"] += len([1 for c in (rep.get("checks") or {}).values() if isinstance(c, dict) and c.get("waived")])
        counts["unverified"] += 1 if rep.get("unverified") else 0
        if st == "pass":
            counts["pass_"] += 1
        else:
            counts["fail"] += 1
            items = []
            for cid in failed:
                base = cid.split("(")[0]
                c = (rep.get("checks") or {}).get(base) or {}
                iss = c.get("issues") or []
                items.append("%s %s" % (cid, (iss[0] if iss else "failed")))
            failing.append(dict(path=p, failed=failed, issues=items, fix=_first_fix(rep, failed[0].split("(")[0]) if failed else ""))
    allowed = max(2, int(0.1 * max(1, len(models))))
    waived_models = len([1 for r in models if isinstance(r, dict) and r.get("waived")])
    if waived_models > allowed:
        reasons.append("%d models carry waivers (limit %d = 10%% of the map, min 2): fix them instead" % (waived_models, allowed))
    ign = 0
    for s in scan.get("skipped") or []:
        why = str((s or {}).get("reason", ""))
        if "NO REASON GIVEN" in why:
            reasons.append("ignored without a reason: %s" % s.get("path"))
        if why.startswith("ignored"):
            ign += 1
    counts["ignored"] = ign
    if ign > allowed:
        reasons.append("%d objects are ignored (limit %d = 10%% of the map, min 2): scan them instead" % (ign, allowed))
    if failing:
        reasons.append("%d of %d model(s) fail their placement checks" % (len(failing), len(models)))
    # freshness
    cap = _ts(scan.get("captured_at") or "")
    if project:
        src = _newest_source(project)
        ref = cap if cap is not None else None
        if src and ref is not None and ref < src - 1:
            reasons.append("stale scan: a Luau source changed after the scan was captured; run the scan again")
    # per-placement reports (placements/*.json under base_dir/placement-qa)
    pdir = os.path.join(base_dir, "placement-qa", "placements")
    latest = {}
    for f in sorted(glob.glob(os.path.join(pdir, "*.json"))):
        try:
            r = json.load(open(f, encoding="utf-8-sig"))
        except Exception:
            continue
        if not isinstance(r, dict) or not r.get("path"):
            continue
        t = _ts(r.get("at") or "") or os.path.getmtime(f)
        if r["path"] not in latest or t >= latest[r["path"]][0]:
            latest[r["path"]] = (t, r)
    for p, (t, r) in sorted(latest.items()):
        st, failed, _ = model_status(r)
        if st != "pass":
            reasons.append("latest per-placement check of %s is FAIL (%s): fix it and verify again" % (p, ", ".join(failed)))
        if cap is not None and t > cap + 1:
            reasons.append("%s was placed/checked after the scan was captured: scan again" % p)
    status = "pass" if not reasons else "fail"
    return dict(status=status, reasons=reasons, failing=failing, label=VERIFIED if status == "pass" else NOT_VERIFIED, counts=counts)


# ------------------------------------------------------------------ console parsing
def parse_console(text):
    """-> (header or None, [model reports]) from PLACEMENT_SCAN / PLACEMENT_MODEL lines (timestamps or prefixes before the tag are ignored)."""
    header, models = None, []
    for ln in text.splitlines():
        m = LINE.search(ln)
        if not m:
            continue
        try:
            obj = json.loads(m.group(2))
        except ValueError:
            continue
        if m.group(1) == "PLACEMENT_SCAN":
            header = obj
        else:
            models.append(obj)
    return header, models


def build_scan(header, models, scorer=None, game=None):
    scan = dict(header or {})
    scan.setdefault("version", 1)
    scan["kind"] = "placement-scan"
    scan["models"] = models
    scan["models_total"] = len(models)
    if scorer:
        scan["scorer"] = scorer
    if game:
        scan["game"] = game
    scan.setdefault("scorer", "builder")
    scan.setdefault("captured_at", datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    return scan


def safe(name):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("_")[:80] or "model"


def print_result(r, scan):
    print("PLACEMENT GATE: %s | scorer %s | %d model(s), %d pass, %d fail" % (r["status"].upper(), scan.get("scorer", "?") if isinstance(scan, dict) else "?", r["counts"]["models"], r["counts"]["pass_"], r["counts"]["fail"]))
    print("STATUS LABEL: " + r["label"])
    for x in r["reasons"]:
        print("  - " + x)
    for f in r["failing"][:40]:
        print("  FAIL %s :: %s" % (f["path"], " | ".join(f["issues"])))
        if f["fix"]:
            print("       suggested fix: " + f["fix"])
    if len(r["failing"]) > 40:
        print("  ... %d more failing model(s)" % (len(r["failing"]) - 40))
    c = r["counts"]
    print("  waived checks: %d | ignored objects: %d | models with unverified items: %d | re-checked from inputs: %d" % (c["waived"], c["ignored"], c["unverified"], c["rechecked"]))


def write_gate(out_dir, scan, r, src):
    d = os.path.join(out_dir, "placement-qa")
    os.makedirs(d, exist_ok=True)
    rec = dict(result=r["status"], label=r["label"], reasons=r["reasons"], failing=r["failing"], counts=r["counts"], scorer=scan.get("scorer"),
               captured_at=scan.get("captured_at"), fingerprint=scan.get("fingerprint"), scan=os.path.basename(src) if src else None)
    p = os.path.join(d, "gate-critic.json" if scan.get("scorer") == "critic" else "gate.json")
    json.dump(rec, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
    print("WROTE " + p)


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        sys.exit(__doc__)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    def opt(name):
        return a[a.index(name) + 1] if name in a else None

    out_dir = opt("--write")
    if a[0] == "ingest":
        text = open(a[1], encoding="utf-8-sig", errors="replace").read() if a[1] != "-" else sys.stdin.read()
        header, models = parse_console(text)
        if not models:
            sys.exit("ingest: no PLACEMENT_MODEL lines found in " + a[1])
        scan = build_scan(header, models, opt("--scorer"), opt("--game"))
        if not out_dir:
            json.dump(scan, sys.stdout, indent=1)
            return
        d = os.path.join(out_dir, "placement-qa")
        os.makedirs(d, exist_ok=True)
        name = opt("--name") or ("scan-%s" % scan["scorer"])
        p = os.path.join(d, name + ".json")
        json.dump(scan, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
        print("WROTE " + p)
        r = evaluate(scan, out_dir, opt("--project"), "critic" if scan["scorer"] == "critic" else None)
        print_result(r, scan)
        write_gate(out_dir, scan, r, p)
        sys.exit(0 if r["status"] == "pass" else 1)
    if a[0] == "log":
        text = sys.stdin.read() if a[1] == "-" else open(a[1], encoding="utf-8-sig", errors="replace").read()
        reps = []
        try:
            obj = json.loads(text)
            reps = obj["models"] if isinstance(obj, dict) and "models" in obj else [obj]
        except ValueError:
            reps = parse_console(text)[1]
        if not reps:
            sys.exit("log: no report found")
        if not out_dir:
            sys.exit("log: --write Games/<slug> is required")
        d = os.path.join(out_dir, "placement-qa", "placements")
        os.makedirs(d, exist_ok=True)
        bad = 0
        for r in reps:
            st, failed, _ = model_status(r)
            stamp = (r.get("at") or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")).replace(":", "")
            p = os.path.join(d, "%s-%s.json" % (stamp, safe(r.get("path", "model"))))
            json.dump(r, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
            print("%s %s %s" % (st.upper(), r.get("path"), ("(" + ", ".join(failed) + ")") if failed else ""))
            bad += st != "pass"
        sys.exit(1 if bad else 0)
    if a[0] == "recheck":
        obj = json.load(open(a[1], encoding="utf-8-sig"))
        reps = obj["models"] if isinstance(obj, dict) and "models" in obj else [obj]
        bad = 0
        for r in reps:
            d = recheck(r)
            if d is None:
                print("NO INPUTS %s" % r.get("path"))
            elif d:
                bad += 1
                print("DIFF %s: %s" % (r.get("path"), "; ".join(d)))
            else:
                print("SAME %s" % r.get("path"))
        sys.exit(1 if bad else 0)
    scan = json.load(open(a[0], encoding="utf-8-sig"))
    gdir = os.path.dirname(os.path.abspath(a[0]))
    base = out_dir or (os.path.dirname(gdir) if os.path.basename(gdir) == "placement-qa" else gdir)
    r = evaluate(scan, base, opt("--project"), opt("--scorer"))
    print_result(r, scan)
    if out_dir:
        write_gate(out_dir, scan, r, a[0])
    sys.exit(0 if r["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
