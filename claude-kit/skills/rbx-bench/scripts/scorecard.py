#!/usr/bin/env python3
"""scorecard.py: one number and one card for "how good is this game, by every gate the vault has", comparable across vault versions. Stdlib only.

  python scorecard.py collect <game folder | directory of gate reports> [--game ID] [--spec obby|tycoon|tower-defense|<spec.json>] [--scores FILE]
                      [--bench-dir DIR] [--history FILE] [--no-history] [--label TXT] [--vault-version V] [--kit DIR] [--project DIR]
                      [--require-critic] [--date YYYY-MM-DD] [--json]
  python scorecard.py compare <A> <B> [--bench-dir DIR] [--history FILE] [--tolerance 5] [--strict]     A, B = scorecard.json | run id | baseline | last | prev
  python scorecard.py baseline set <scorecard.json> [--bench-dir DIR]      |   baseline show
  python scorecard.py history [--bench-dir DIR] [--history FILE] [--game ID]
  python scorecard.py verify <scorecard.json>                              re-hash the source gate files; changed or missing = tampering or a stale card
  python scorecard.py spec list | show <id> | write-md [--dir DIR] | check-md       the standard test games (benchmarks/standard/*.json)

WHAT IT READS (nothing is modified; discovery is generic, so a new gate shows up without a code change):
  * every file named gate.json, gate-*.json, *-gate.json under the folder (visual-qa/, placement-qa/, lighting-qa/, any future <name>-qa/): the gate is named after its
    folder (visual-qa -> visual). Status from result|status|verdict|passed; checks from `scores` (V1..V7, 1-10) or `checks` ({id: score | {status|score}}); reasons from
    `reasons`, `failing`, `hard_fails`. A critic-scored record (scorer critic, or gate-critic.json) wins over a builder-scored one.
  * placement-qa/scan-critic.json (else scan-builder.json): per-check pass rate P1..P7 over the models.
  * critic/<date>-<stage>.md verdict files (frontmatter verdict, score, works, visual, placement): the newest one.
  * optional benchmark-scores.json (features 0..1 + rubric 1..10 with evidence, from the independent critic) and benchmark-run.json (minutes, turns, tokens, model).
SCORING (all numbers 0-100, deterministic):
  gate score = mean of its check scores x 10 (pass/fail checks: pass 10, fail 0), or 100/0 for a pass/fail gate with no checks; a FAILED gate is capped at 69,
  a missing required gate scores 0. critic: GOOD = mean x 10, NOT YET capped 69, BAD capped 39.
  overall = weighted mean over the gates that apply. Weights: visual 25, placement 20, critic 25, lighting 15 (only when present), spec 20 (only with --spec),
  any other discovered gate 10. Required gates: visual, placement, critic (missing = 0 and a problem).
  grade: A >= 90, B >= 80, C >= 70, D >= 50, else F.   all_required_pass = every required gate is pass and the critic says GOOD.
"""
import argparse
import csv
import datetime
import glob
import hashlib
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
SPEC_DIR = os.path.join(SKILL, "benchmarks", "standard")
SCHEMA = 1
REQUIRED = ["visual", "placement", "critic"]
WEIGHTS = {"visual": 25, "placement": 20, "critic": 25, "lighting": 15, "spec": 20}
DEFAULT_WEIGHT = 10
FAIL_CAP = 69
SKIP_DIRS = {"benchmarks", "node_modules", ".git", "packages", "vendor", "build", "docs", "__pycache__", ".claude", "roblox-reference"}
GATE_FILE = re.compile(r"^(gate|.+-gate|gate-.+)\.json$", re.I)
PASS_WORDS = {"pass", "passed", "ok", "good", "true", "green", "success"}
FAIL_WORDS = {"fail", "failed", "bad", "not yet", "false", "red", "error"}
SKIP_WORDS = {"skip", "skipped", "n/a", "na", "none", "unknown", "pending", "not run"}

GATE_RUN = {
    "visual": "Run rbx-visual: capture the screenshots, score V1-V7, then visual_gate.py gate.json --write Games/<slug> (needs the placement gate first).",
    "placement": "Run rbx-placement: Placement.scan over the whole map, then placement_gate.py ingest <console output> --write Games/<slug> --scorer critic.",
    "critic": "Run rbx-critic: its own gate scans, then verdict.py <input.json> --write Games/<slug> so critic/<date>-<stage>.md exists.",
    "lighting": "Run rbx-lighting and keep its gate record in lighting-qa/.",
    "code-gates": "Run python <skills>/rbx-critic/scripts/code_gates.py <project> --scorer critic --write Games/<slug>: it writes comment-scan, scope-scan, security-scan, trigger-scan, bugfix and code-gates/run.json (add --report <final report> for evidence-scan).",
    "ui-design": "Run rbx-ui-mockup: ui_design.py all, build from the spec, then ui_compare.py gate (or skip --reason) --write Games/<slug>; advisory.",
    "thumb-score": "Run rbx-thumbnail step 4a: thumb_score.py score (or skip --reason) --write Games/<slug>; advisory.",
    "spec": "Fill benchmark-scores.json (features, rubric B1-B7 with evidence) from the standard test game card, then collect again with --spec.",
}
FIXES = {
    "V1": "Build one StyleKit component set (same corner radius, stroke, shadow, font, palette) and restyle every panel and button from it (rbx-art).",
    "V2": "Run ui_overlap at phone, tablet and desktop; anchor everything in Scale, queue popups one at a time, keep the thumbstick/jump zones and the top bar clear (rbx-visual).",
    "V3": "Make the key number large, raise contrast to 4.5:1, text >= 14 px on phone, one focal element per screen state, icon plus label.",
    "V4": "Replace bare primitives for hero objects with multi-part models (3+ materials, bevels, details, contact shadow); vary props in size, colour and angle.",
    "V5": "Apply a lighting preset: Atmosphere, Sky, ColorCorrection, Bloom, tuned Ambient/ClockTime and a lit focal object (rbx-art, rbx-lighting).",
    "V6": "Give every key event two of: particle burst, tween, sound, camera/UI reaction; fade effects out and capture one screenshot mid-effect.",
    "V7": "Fix the spawn view: goal visible, tidy HUD, lit styled world, no debug text or placeholder names, a clear first action and a first reward with feedback.",
    "P1": "Set pivot and size for the model's kind (Placement.verify prints measured vs expected); fix the wrong-scale asset or its PrimaryPart.",
    "P2": "Snap to the surface below (Fix.snapToGround) so nothing floats or sinks.",
    "P3": "Stand the model upright (Fix.upright) and re-verify.",
    "P4": "Turn the model to face its target and snap yaw to the grid (Fix.faceTarget / snapYaw).",
    "P5": "Nudge out of the overlap or z-fight and keep the model inside the map bounds and off the terrain.",
    "P6": "Anchor it, set CanCollide/CanTouch deliberately and delete junk parts.",
    "P7": "Align connected pieces, mirror pairs and clones to their neighbours.",
    "L": "Apply or tune the lighting preset for the art direction, then re-run the lighting gate (rbx-lighting).",
    "critic": "Raise the critic's lowest factors named in the verdict, fix every failing gate above, then run rbx-critic again with fresh scans.",
    "spec": "Implement the missing features/screenshots/scan points of the standard test game (see the spec card), then re-score.",
}


# ------------------------------------------------------------------ small helpers
def jload(p):
    with open(p, encoding="utf-8-sig") as f:
        return json.load(f)


def read_text(p):
    try:
        with open(p, encoding="utf-8-sig", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def num(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)) and not (isinstance(v, float) and (math.isnan(v) or math.isinf(v))):
        return float(v)
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


def norm_status(v):
    """-> 'pass' | 'fail' | 'skipped' | None"""
    if isinstance(v, bool):
        return "pass" if v else "fail"
    if v is None:
        return None
    s = str(v).strip().lower()
    if s in PASS_WORDS:
        return "pass"
    if s in FAIL_WORDS:
        return "fail"
    if s in SKIP_WORDS:
        return "skipped"
    return None


def grade(x):
    return "A" if x >= 90 else "B" if x >= 80 else "C" if x >= 70 else "D" if x >= 50 else "F"


def short(s, n=160):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return s if len(s) <= n else s[: n - 3] + "..."


# ------------------------------------------------------------------ discovery
def find_gate_files(root, maxdepth=5):
    out = []
    root = os.path.abspath(root)
    base_depth = root.rstrip(os.sep).count(os.sep)
    for d, dn, fn in os.walk(root):
        if d.count(os.sep) - base_depth >= maxdepth:
            dn[:] = []
        dn[:] = sorted(x for x in dn if x.lower() not in SKIP_DIRS)
        for f in sorted(fn):
            if GATE_FILE.match(f):
                out.append(os.path.join(d, f))
    return out


def gate_name(path, root):
    parent = os.path.basename(os.path.dirname(path))
    if os.path.abspath(os.path.dirname(path)) == os.path.abspath(root):
        stem = os.path.splitext(os.path.basename(path))[0]
        n = re.sub(r"(^gate[-_.]?|[-_.]?gate$)", "", stem, flags=re.I)
        n = re.sub(r"[-_.]critic$", "", n, flags=re.I)
        parent = n or "gate"
    n = parent.lower()
    for suf in ("-qa", "_qa", "-gate", "_gate"):
        if n.endswith(suf):
            n = n[: -len(suf)]
    return n or "gate"


def extract_checks(rec):
    """-> ({id: score 0..10 | None(skip)}, pass_min). Generic: scores / checks as dict or list."""
    pm = num(rec.get("pass_min")) or 7.0
    for key in ("scores", "checks"):
        v = rec.get(key)
        out = {}
        if isinstance(v, dict):
            for k, x in v.items():
                n = num(x)
                if n is not None:
                    out[str(k)] = max(0.0, min(10.0, n / 10.0 if n > 10 else n))
                elif isinstance(x, dict):
                    sc = num(x.get("score"))
                    st = norm_status(x.get("status"))
                    if sc is not None:
                        out[str(k)] = max(0.0, min(10.0, sc / 10.0 if sc > 10 else sc))
                    elif st == "pass":
                        out[str(k)] = 10.0
                    elif st == "fail":
                        out[str(k)] = 0.0
                    elif st == "skipped":
                        out[str(k)] = None
                else:
                    st = norm_status(x)
                    if st in ("pass", "fail"):
                        out[str(k)] = 10.0 if st == "pass" else 0.0
        elif isinstance(v, list):
            for i, x in enumerate(v):
                if isinstance(x, dict):
                    k = str(x.get("id") or x.get("name") or i)
                    sc = num(x.get("score"))
                    st = norm_status(x.get("status"))
                    if sc is not None:
                        out[k] = max(0.0, min(10.0, sc / 10.0 if sc > 10 else sc))
                    elif st in ("pass", "fail"):
                        out[k] = 10.0 if st == "pass" else 0.0
        if out:
            return out, pm
    return {}, pm


def reasons_of(rec):
    out = []
    for key in ("reasons", "problems"):
        v = rec.get(key)
        if isinstance(v, list):
            out += [short(x if isinstance(x, str) else json.dumps(x, ensure_ascii=False), 220) for x in v]
    for h in rec.get("hard_fails") or []:
        out.append("hard fail open: " + short(h, 200))
    return out


def placement_checks_from_scan(scan):
    """per-check pass rate over the models of a placement scan -> {P1: 0..10} (skips excluded)"""
    n, ok = {}, {}
    for m in scan.get("models") or []:
        for cid, c in (m.get("checks") or {}).items():
            st = (c or {}).get("status")
            if st in ("pass", "fail"):
                n[cid] = n.get(cid, 0) + 1
                if st == "pass" or (c or {}).get("waived"):
                    ok[cid] = ok.get(cid, 0) + 1
    return {cid: round(10.0 * ok.get(cid, 0) / n[cid], 2) for cid in sorted(n) if n[cid]}


def pick_best(cands):
    """candidates [(path, rec)] of one gate -> the critic-scored one, else the newest."""
    def key(c):
        p, r = c
        crit = 1 if (str(r.get("scorer", "")).lower() == "critic" or "critic" in os.path.basename(p).lower()) else 0
        return (crit, os.path.getmtime(p), p)
    return sorted(cands, key=key)[-1]


def build_gate(name, path, rec, root):
    status = None
    for k in ("result", "status", "verdict", "passed", "pass"):
        if k in rec:
            status = norm_status(rec[k])
            if status:
                break
    checks, pm = extract_checks(rec)
    scorer = str(rec.get("scorer") or ("critic" if "critic" in os.path.basename(path).lower() else "unknown")).lower()
    extra = {}
    scan, scan_path = None, None
    if not checks or name == "placement":
        # a scan record next to the gate record (written by the gate's own scan step): placement-scan -> per-check pass rate over the models;
        # any other scan with a stored report {"checks": {id: {status}}} -> that report's checks
        cands = [rec.get("scan")] if isinstance(rec.get("scan"), str) else []
        for fn in cands + ["scan-critic.json", "scan-builder.json"]:
            sp = os.path.join(os.path.dirname(path), fn)
            if fn and os.path.isfile(sp):
                try:
                    scan, scan_path = jload(sp), sp
                    break
                except Exception:
                    scan = None
    if scan_path and isinstance(scan, dict):
        extra["scan_file"] = scan_path
        if scan.get("kind") == "placement-scan" and not checks:
            checks = placement_checks_from_scan(scan)
        elif not checks and isinstance(scan.get("report"), dict):
            checks, _ = extract_checks({"checks": scan["report"].get("checks")})
    if not checks:
        # last resort: failing items that carry a check id (e.g. L3) plus counts.checks = N -> failing ids score 0, the others 10
        fl = [f for f in (rec.get("failing") or []) if isinstance(f, dict) and re.match(r"^[A-Za-z]+\d+$", str(f.get("check", "")))]
        cnt = rec.get("counts") if isinstance(rec.get("counts"), dict) else {}
        if fl and isinstance(cnt.get("checks"), int):
            pre = re.match(r"^[A-Za-z]+", str(fl[0]["check"])).group(0)
            bad_ids = {str(f["check"]) for f in fl}
            checks = {("%s%d" % (pre, i)): (0.0 if ("%s%d" % (pre, i)) in bad_ids else 10.0) for i in range(1, cnt["checks"] + 1)}
    vals = [v for v in checks.values() if v is not None]
    if vals:
        raw = 10.0 * sum(vals) / len(vals)
    elif status == "pass":
        raw = 100.0
    elif isinstance(rec.get("counts"), dict) and rec["counts"].get("models"):
        c = rec["counts"]
        raw = 100.0 * (c.get("pass_", 0) or 0) / max(1, c.get("models", 1))
    else:
        raw = 0.0
    if status is None:
        # no explicit status: derive from the checks vs pass_min
        if vals:
            status = "pass" if all(v >= pm for v in vals) else "fail"
        else:
            status = "skipped"
    score = raw
    if status == "fail":
        score = min(raw, FAIL_CAP)
    elif status == "skipped":
        score = 0.0
    failing = []
    if isinstance(rec.get("failing"), list):
        for f in rec["failing"][:50]:
            if isinstance(f, dict):
                failing.append(dict(path=f.get("path") or f.get("name"), failed=f.get("failed") or ([f["check"]] if f.get("check") else None), fix=short(f.get("fix", ""), 200)))
    g = dict(name=name, status=status, score=round(score, 1), raw_score=round(raw, 1), weight=WEIGHTS.get(name, DEFAULT_WEIGHT),
             required=name in REQUIRED, scripted=bool(rec.get("scripted")), checks={k: (None if v is None else round(v, 2)) for k, v in checks.items()}, pass_min=pm,
             reasons=reasons_of(rec), failing=failing, scorer=scorer, label=rec.get("label"), source=os.path.relpath(path, root).replace(os.sep, "/") if root else path,
             sha256=sha256_file(path), mtime=int(os.path.getmtime(path)))
    g.update({k: os.path.relpath(v, root).replace(os.sep, "/") if k == "scan_file" else v for k, v in extra.items()})
    return g


def parse_verdict_md(path):
    t = read_text(path).replace("\r\n", "\n")
    if not t.startswith("---\n"):
        return None
    end = t.find("\n---", 4)
    if end < 0:
        return None
    fm = {}
    for line in t[4:end].split("\n"):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    if "verdict" not in fm:
        return None
    why = re.search(r"\*\*Why:\*\*\s*(.+)", t)
    fm["why"] = why.group(1).strip() if why else ""
    return fm


def build_critic(root):
    files = []
    for d, dn, fn in os.walk(root):
        dn[:] = [x for x in sorted(dn) if x.lower() not in SKIP_DIRS]
        if os.path.basename(d).lower() == "critic":
            for f in sorted(fn):
                if f.endswith(".md"):
                    fm = parse_verdict_md(os.path.join(d, f))
                    if fm:
                        files.append((fm.get("date", ""), f, os.path.join(d, f), fm))
    if not files:
        return None
    files.sort(key=lambda x: (x[0], x[1]))
    date, f, p, fm = files[-1]
    v = fm.get("verdict", "").strip().upper()
    mean = num(fm.get("score"))
    base = 10.0 * mean if mean is not None else 0.0
    if v == "GOOD":
        status, score = "pass", base
    elif v == "NOT YET":
        status, score = "fail", min(base, FAIL_CAP)
    elif v == "BAD":
        status, score = "fail", min(base, 39.0)
    else:
        status, score = "skipped", 0.0
    reasons = [short(fm["why"], 300)] if fm.get("why") and status != "pass" else []
    return dict(name="critic", status=status, score=round(score, 1), raw_score=round(base, 1), weight=WEIGHTS["critic"], required=True, checks={}, pass_min=7.0,
                reasons=reasons, failing=[], scorer="critic", label="verdict " + v, source=os.path.relpath(p, root).replace(os.sep, "/"), sha256=sha256_file(p),
                mtime=int(os.path.getmtime(p)), verdict=v, stage=fm.get("stage"), works=fm.get("works"), claims=dict(visual=fm.get("visual"), placement=fm.get("placement"), lighting=fm.get("lighting"), codegates=fm.get("codegates"), readme=fm.get("readme")),
                verdict_date=date)


# ------------------------------------------------------------------ spec (standard test games)
def load_spec(arg):
    if not arg:
        return None
    p = arg if os.path.isfile(arg) else os.path.join(SPEC_DIR, arg + ".json")
    if not os.path.isfile(p):
        raise SystemExit("scorecard: spec %r not found (standard: %s)" % (arg, ", ".join(spec_ids())))
    return jload(p)


def spec_ids():
    return sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(SPEC_DIR, "*.json")))


def build_spec_gate(spec, root, gates, scores_file):
    """spec coverage gate from: the human/critic scores file (features, rubric), the screenshots of the visual gate, the placement scan model paths."""
    checks, reasons, notes = {}, [], []
    sp = scores_file or next((p for p in (os.path.join(root, "benchmark-scores.json"), os.path.join(root, "benchmark", "scores.json")) if os.path.isfile(p)), None)
    sc = {}
    if sp:
        try:
            sc = jload(sp)
        except Exception as e:
            reasons.append("benchmark-scores.json unreadable: %s" % e)
    feats = sc.get("features") or {}
    tw = sum(f.get("weight", 1) for f in spec["features"])
    got = 0.0
    for f in spec["features"]:
        v = num(feats.get(f["id"]))
        v = 0.0 if v is None else max(0.0, min(1.0, v))
        got += v * f.get("weight", 1)
        if v < 1.0:
            reasons.append("feature %s %s: %s" % (f["id"], "missing" if feats.get(f["id"]) is None else "partial (%.1f)" % v, f["text"]))
    checks["features"] = round(10.0 * got / tw, 2) if tw else 0.0
    rub = sc.get("rubric") or {}
    ev = sc.get("evidence") or {}
    rv = []
    for r in spec["rubric"]:
        v = num(rub.get(r["id"]))
        if v is None:
            rv.append(0.0)
            reasons.append("rubric %s %s not scored" % (r["id"], r["name"]))
        else:
            v = max(1.0, min(10.0, v))
            rv.append(v)
            if not str(ev.get(r["id"], "")).strip():
                notes.append("rubric %s scored %g without evidence text" % (r["id"], v))
            if v < 7:
                reasons.append("rubric %s %s scored %g (needs 7)" % (r["id"], r["name"], v))
    checks["rubric"] = round(sum(rv) / len(rv), 2) if rv else 0.0
    # screenshots
    shots = set()
    vis = gates.get("visual")
    if vis and vis.get("status") in ("pass", "fail"):
        try:
            rec = jload(os.path.join(root, vis["source"]))
            for s in rec.get("screenshots") or []:
                if isinstance(s, dict):
                    full = s.get("path", "")
                    full = full if os.path.isabs(full) else os.path.join(os.path.dirname(os.path.dirname(os.path.join(root, vis["source"]))), full)
                    if os.path.isfile(full):
                        shots.add((s.get("viewport", ""), s.get("moment", "")))
        except Exception:
            pass
    req = [(s["viewport"], s["moment"]) for s in spec["required_screenshots"]]
    have = [r for r in req if r in shots]
    checks["screenshots"] = round(10.0 * len(have) / len(req), 2) if req else 10.0
    for r in req:
        if r not in shots:
            reasons.append("required screenshot missing: %s-%s" % r)
    # scan points
    paths = []
    pl = gates.get("placement")
    scan_file = pl.get("scan_file") if pl else None
    if scan_file:
        try:
            paths = [m.get("path", "") for m in jload(os.path.join(root, scan_file)).get("models") or []]
        except Exception:
            pass
    ok = 0
    for pt in spec["scan_points"]:
        n = len([p for p in paths if re.search(pt["pattern"], p)])
        if n >= pt.get("min", 1):
            ok += 1
        else:
            reasons.append("scan point %s: %d of %d %s found in the placement scan" % (pt["id"], n, pt.get("min", 1), pt["text"]))
    checks["scan_points"] = round(10.0 * ok / len(spec["scan_points"]), 2) if spec["scan_points"] else 10.0
    raw = 10.0 * sum(checks.values()) / len(checks)
    status = "pass" if all(v >= 7 for v in checks.values()) and checks["features"] >= 9.99 else "fail"
    score = min(raw, FAIL_CAP) if status == "fail" else raw
    return dict(name="spec", status=status, score=round(score, 1), raw_score=round(raw, 1), weight=WEIGHTS["spec"], required=False, checks=checks, pass_min=7.0, reasons=reasons[:40],
                failing=[], scorer=str(sc.get("scorer", "unknown")).lower(), label="spec " + spec["id"], source=os.path.relpath(sp, root).replace(os.sep, "/") if sp else "(no benchmark-scores.json)",
                sha256=sha256_file(sp) if sp else "", mtime=int(os.path.getmtime(sp)) if sp else 0, notes=notes, spec=spec["id"])


# ------------------------------------------------------------------ collect
def newest_source(project):
    best = 0.0
    for d, dn, fn in os.walk(project):
        dn[:] = [x for x in dn if x.lower() not in ("packages", "vendor", "node_modules", ".git", "build", "docs")]
        for f in fn:
            if f.endswith((".luau", ".lua")):
                best = max(best, os.path.getmtime(os.path.join(d, f)))
    return best


def bench_dir_for(target, arg=None):
    if arg:
        return os.path.abspath(arg)
    if os.environ.get("BENCH_DIR"):
        return os.path.abspath(os.environ["BENCH_DIR"])
    t = os.path.abspath(target)
    par = os.path.dirname(t)
    if os.path.basename(par).lower() == "games":
        return os.path.join(par, "benchmarks")
    return os.path.join(t, "benchmarks")


def meta_hidden(root):
    for fn in ("benchmark-run.json", os.path.join("benchmark", "run.json")):
        p = os.path.join(root, fn)
        if os.path.isfile(p):
            try:
                return jload(p).get("benchmark_skill_hidden") is True
            except Exception:
                return False
    return False


def auto_version(kit=None):
    """vault version of the kit this script belongs to (or --kit): see vault_cost.vault_version."""
    try:
        sys.path.insert(0, HERE)
        import vault_cost
        base = os.path.dirname(os.path.dirname(SKILL))     # <kit>/skills/rbx-bench -> <kit>
        k = kit or (base if os.path.isdir(os.path.join(base, "mode")) else None)
        cfg = None
        if not k:
            parts = os.path.abspath(SKILL).split(os.sep)
            for i in range(len(parts) - 1, 0, -1):
                if parts[i] == ".claude":
                    cfg = os.sep.join(parts[: i + 1])
                    break
        return vault_cost.vault_version(k, cfg, None)
    except Exception:
        return "unknown"


CODE_STAGES = ("prototype", "playtest", "launch", "growth", "live-ops")
CODE_GATE_NAMES = ("comment-scan", "scope-scan", "security-scan")


def code_gates_integrity(gates, root, integrity):
    """a game with a prototype-or-later critic verdict must carry proof that the code gates ran; absent = an integrity note (the verdict itself is capped by verdict.py)."""
    crit = gates.get("critic")
    if not crit or crit.get("status") == "missing" or str(crit.get("stage") or "").lower() not in CODE_STAGES:
        return
    run_p = os.path.join(root, "code-gates", "run.json")
    run = None
    if os.path.isfile(run_p):
        try:
            run = jload(run_p)
        except Exception:
            run = None
    claim = str((crit.get("claims") or {}).get("codegates") or "").lower()
    if not isinstance(run, dict):
        integrity.append("code gates have no run record (code-gates/run.json): a prototype-or-later game must run code_gates.py" + ("; the critic verdict claims codegates: ran" if claim == "ran" else ""))
        return
    if str(run.get("scorer", "")).lower() != "critic":
        integrity.append("code gates were run by %r, not by the independent critic: advisory until the critic re-runs them" % run.get("scorer"))
    miss = [n for n in CODE_GATE_NAMES if n not in gates]
    if miss:
        integrity.append("code-gates/run.json exists but the gate record(s) %s are missing" % ", ".join(miss))
    if claim and claim != "ran":
        integrity.append("critic verdict file says codegates: %s but code-gates/run.json exists (stale verdict: run a fresh critic)" % claim)


def readme_integrity(gates, root, integrity):
    c = str(((gates.get("critic") or {}).get("claims") or {}).get("readme") or "")
    if os.path.isfile(os.path.join(root, "GAME.md")) and (c in ("stale", "missing") or not os.path.isfile(os.path.join(root, "README.md"))):
        integrity.append("game README.md is missing or older than the latest change (advisory)")


def collect(root, game=None, spec_arg=None, scores_file=None, require_critic=False, project=None, version=None, kit=None, label="", date=None, now=None):
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        raise SystemExit("scorecard: %s is not a folder" % root)
    now = now or datetime.datetime.now()
    game = game or os.path.basename(root.rstrip("\\/"))
    by_name = {}
    for p in find_gate_files(root):
        try:
            rec = jload(p)
        except Exception:
            continue
        if not isinstance(rec, dict):
            continue
        if rec.get("kind") == "placement-scan":
            continue
        by_name.setdefault(gate_name(p, root), []).append((p, rec))
    gates = {}
    for name, cands in by_name.items():
        p, rec = pick_best(cands)
        gates[name] = build_gate(name, p, rec, root)
    cg = build_critic(root)
    if cg:
        gates["critic"] = cg
    spec = load_spec(spec_arg)
    if spec:
        gates["spec"] = build_spec_gate(spec, root, gates, scores_file)
    integrity = []
    for r in REQUIRED:
        if r not in gates:
            gates[r] = dict(name=r, status="missing", score=0.0, raw_score=0.0, weight=WEIGHTS[r], required=True, checks={}, pass_min=7.0,
                            reasons=["no %s gate record found under %s" % (r, root)], failing=[], scorer="none", label=None, source="", sha256="", mtime=0)
    if require_critic:
        for n, g in gates.items():
            if n in ("critic", "spec") or g["status"] == "missing":
                continue
            if g["scorer"] != "critic":
                g["score"] = 0.0
                g["status"] = "fail" if g["status"] == "pass" else g["status"]
                g["reasons"].insert(0, "scored by %r, not by the critic (--require-critic): counted as 0" % g["scorer"])
    for n, g in sorted(gates.items()):
        if n not in ("critic", "spec") and g["status"] != "missing" and g["scorer"] != "critic":
            integrity.append("%s gate is scored by %r, not by the independent critic: advisory until the critic re-scores it" % (n, g["scorer"]))
        vals = [v for v in g["checks"].values() if v is not None]
        if len(vals) >= 5 and len(set(vals)) == 1 and vals[0] >= 9 and not g.get("scripted"):
            integrity.append("%s gate: all %d checks have the identical score %g (looks like a blanket score, ask for evidence per item)" % (n, len(vals), vals[0]))
    if "critic" in gates and gates["critic"]["status"] != "missing":
        cl = gates["critic"].get("claims") or {}
        for n in ("visual", "placement", "lighting"):
            claimed = norm_status(cl.get(n))
            actual = gates.get(n, {}).get("status")
            if claimed == "pass" and actual not in ("pass",):
                integrity.append("critic verdict file claims %s: pass but the %s gate record says %s" % (n, n, actual or "nothing (no record found)"))
    code_gates_integrity(gates, root, integrity)
    readme_integrity(gates, root, integrity)
    if project:
        src = newest_source(project)
        for n, g in gates.items():
            if g.get("mtime") and src and g["mtime"] < src - 1 and n not in ("critic",):
                integrity.append("%s gate record is older than the newest Luau source in %s (stale: re-run the gate on the current build)" % (n, project))
    if spec:
        for n in gates["spec"].get("notes", []):
            integrity.append(n)
    if project and os.path.isdir(os.path.join(project, ".claude", "skills", "rbx-bench")) and not meta_hidden(root):
        integrity.append("the builder's project still has .claude/skills/rbx-bench (the rubric and formula were readable during the build); hide it before a benchmark run and set \"benchmark_skill_hidden\": true in benchmark-run.json")
    # overall: gates that apply = discovered gates + required (missing counts as 0)
    used = {n: g for n, g in gates.items()}
    wsum = sum(g["weight"] for g in used.values())
    overall = sum(g["weight"] * g["score"] for g in used.values()) / wsum if wsum else 0.0
    all_req = all(gates[r]["status"] == "pass" for r in REQUIRED)
    problems = rank_problems(used, wsum)
    meta = {}
    for fn in ("benchmark-run.json", os.path.join("benchmark", "run.json")):
        if os.path.isfile(os.path.join(root, fn)):
            try:
                meta = jload(os.path.join(root, fn))
            except Exception:
                pass
    ver = version or auto_version(kit)
    run_id = "%s-%s-%s" % (now.strftime("%Y%m%d-%H%M%S"), re.sub(r"[^A-Za-z0-9_-]+", "_", game)[:30], re.sub(r"[^A-Za-z0-9._-]+", "_", str(ver))[:24])
    card = dict(kind="vault-scorecard", schema=SCHEMA, run_id=run_id, date=date or now.strftime("%Y-%m-%d"), time=now.strftime("%H:%M:%S"), vault_version=ver, game=game,
                spec=spec["id"] if spec else "", spec_version=spec.get("version") if spec else None, label=label, root=root, overall=round(overall, 1), grade=grade(overall),
                all_required_pass=all_req, gates={n: used[n] for n in sorted(used)}, problems=problems, integrity=integrity, run_meta=meta,
                weights={n: g["weight"] for n, g in sorted(used.items())}, method="see scorecard.py docstring: gate score = mean(check) x 10, fail cap 69, weighted mean")
    return card


def rank_problems(gates, wsum):
    """Top 3 problems by points lost. A gate's shortfall (weight share x (100 - score)) is split in two: the part explained by checks under their pass mark is shared among
    those checks by deficit (10 - score); the rest (cap for a failed gate, reasons, failing models, or a gate with no checks) is shared among its reasons.
    Critic problems are derived from the other gates, so they only rank high when nothing else is wrong."""
    cands = {}

    def add(gate, check, impact, text, fix):
        k = (gate, check or text[:60])
        if k in cands:
            cands[k]["impact"] += impact
            if text not in cands[k]["text"] and len(cands[k]["text"]) < 260:
                cands[k]["text"] += "; " + text
            return
        cands[k] = dict(gate=gate, check=check, impact=impact, text=text, fix=fix)
    others_bad = any(g["status"] != "pass" for n, g in gates.items() if n != "critic")
    for n, g in gates.items():
        wn = g["weight"] / wsum if wsum else 0
        if g["status"] in ("missing", "skipped"):
            add(n, "", wn * 100, "%s gate %s" % (n, "was not run (no record found)" if g["status"] == "missing" else "is skipped/unknown (counts as 0)"),
                GATE_RUN.get(n, "Run the %s gate on the current build and keep its gate.json in the game folder." % n))
            continue
        if g["status"] == "pass":
            continue        # a passing gate has no problem to fix; its weaker checks are visible in the table
        shortfall = wn * (100 - g["score"])
        checks = {k: v for k, v in g["checks"].items() if v is not None}
        below = {k: v for k, v in checks.items() if v < g["pass_min"]}
        raw_part = wn * (100 - g["raw_score"]) if checks else 0.0
        tot_def = sum(10 - v for v in below.values())
        pool = shortfall
        if below and tot_def > 0:
            pool = max(0.0, shortfall - raw_part)
            for k, v in below.items():
                fx = FIXES.get(k) or FIXES.get(re.sub(r"\d+$", "", k))
                if n == "spec":
                    fx = FIXES["spec"]
                add(n, k, raw_part * (10 - v) / tot_def, "%s %s scored %g (needs %g)" % (n, k, v, g["pass_min"]),
                    fx or "Fix the failing %s item %s named in %s, then re-run the gate." % (n, k, g["source"]))
        elif checks:
            pool = shortfall
        seen = set(below)
        items = []
        for f in g["failing"][:20]:
            ids = [x.split("(")[0] for x in (f.get("failed") or [])]
            hit = next((i for i in ids if (n, i) in cands), None)
            if hit:
                c = cands[(n, hit)]
                if f.get("path") and f["path"] not in c["text"] and len(c["text"]) < 200:
                    c["text"] += " (e.g. %s)" % f["path"]
                if f.get("fix"):
                    c["fix"] = f["fix"] + " Then " + c["fix"][0].lower() + c["fix"][1:]
                continue
            items.append((ids[0] if ids else "models", "%s: %s fails %s" % (n, f.get("path"), ", ".join(f.get("failed") or [])),
                          f.get("fix") or FIXES.get(ids[0] if ids else "", "Fix and re-verify.")))
        for r in g["reasons"]:
            m = re.match(r"^([A-Z]\d+)\b", r)
            if m and m.group(1) in seen:
                continue
            items.append(("", "%s: %s" % (n, short(r, 200)), FIXES.get(n) or "Fix the reason above and re-run the %s gate." % n))
        items = items[:8]
        if not items and (pool > 0.05 or g["status"] == "fail") and not below:
            items = [("", "%s gate failed with no reason recorded" % n, "Open %s and re-run the gate; a failing gate must name its reasons." % (g["source"] or n))]
        factor = 0.25 if (n == "critic" and others_bad) else 1.0
        for chk, text, fx in items:
            add(n, chk, pool / len(items) * factor, text, fx)
    ranked = sorted(cands.values(), key=lambda c: -c["impact"])[:3]
    for i, c in enumerate(ranked, 1):
        c["rank"] = i
        c["impact"] = round(c["impact"], 1)
    return ranked


# ------------------------------------------------------------------ output
HIST_COLS = ["date", "run_id", "vault_version", "game", "spec", "overall", "grade", "all_required_pass", "visual", "placement", "lighting", "critic", "spec_score",
             "other_gates", "missing", "failing", "minutes", "turns", "label", "scorecard"]


def history_row(card, path):
    g = card["gates"]
    known = ("visual", "placement", "lighting", "critic", "spec")
    return {"date": card["date"], "run_id": card["run_id"], "vault_version": card["vault_version"], "game": card["game"], "spec": card["spec"], "overall": card["overall"],
            "grade": card["grade"], "all_required_pass": "yes" if card["all_required_pass"] else "no",
            "visual": g.get("visual", {}).get("score", ""), "placement": g.get("placement", {}).get("score", ""), "lighting": g.get("lighting", {}).get("score", ""),
            "critic": g.get("critic", {}).get("score", ""), "spec_score": g.get("spec", {}).get("score", ""),
            "other_gates": ";".join("%s=%s" % (n, x["score"]) for n, x in sorted(g.items()) if n not in known),
            "missing": ";".join(n for n, x in sorted(g.items()) if x["status"] == "missing"), "failing": ";".join(n for n, x in sorted(g.items()) if x["status"] == "fail"),
            "minutes": card["run_meta"].get("minutes", ""), "turns": card["run_meta"].get("turns", ""), "label": card["label"], "scorecard": path}


def append_history(path, row):
    new = not os.path.isfile(path)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HIST_COLS, lineterminator="\n")
        if new:
            w.writeheader()
        w.writerow(row)


def read_history(path):
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def card_md(c):
    L = ["# Scorecard: %s%s" % (c["game"], " (spec %s)" % c["spec"] if c["spec"] else ""), "",
         "Run %s | %s | vault version %s%s" % (c["run_id"], c["date"], c["vault_version"], " | " + c["label"] if c["label"] else ""), "",
         "**Overall %.1f / 100, grade %s.** All required gates pass: %s." % (c["overall"], c["grade"], "yes" if c["all_required_pass"] else "NO"), "",
         "| gate | status | score | weight | scorer | checks |", "|---|---|---|---|---|---|"]
    for n, g in c["gates"].items():
        ck = " ".join("%s=%g" % (k, v) if v is not None else "%s=skip" % k for k, v in g["checks"].items()) or "-"
        L.append("| %s | %s | %.1f | %d | %s | %s |" % (n, g["status"].upper(), g["score"], g["weight"], g["scorer"], ck))
    L += ["", "## Top problems"]
    if c["problems"]:
        for p in c["problems"]:
            L.append("%d. [%s%s] %s (costs about %.1f points)\n   Fix: %s" % (p["rank"], p["gate"], "/" + p["check"] if p["check"] else "", p["text"], p["impact"], p["fix"]))
    else:
        L.append("None: every gate passes.")
    if c["integrity"]:
        L += ["", "## Integrity flags (the number above is advisory until these are cleared)"] + ["- " + x for x in c["integrity"]]
    m = c.get("run_meta") or {}
    if m:
        L += ["", "## Run effort", "- " + ", ".join("%s %s" % (k, v) for k, v in sorted(m.items()))]
    L += ["", "Sources (sha256 first 12): " + ", ".join("%s:%s" % (g["source"], g["sha256"][:12]) for g in c["gates"].values() if g.get("sha256"))]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ compare
RANK = {"pass": 3, "skipped": 1, "fail": 1, "missing": 0}


def resolve_card(ref, bench, history):
    if os.path.isfile(ref):
        return jload(ref), ref
    if ref == "baseline":
        p = os.path.join(bench, "baseline.json")
        if not os.path.isfile(p):
            raise SystemExit("scorecard: no baseline set (%s); run: scorecard.py baseline set <scorecard.json>" % p)
        return jload(p), p
    rows = read_history(history)
    if ref in ("last", "prev"):
        if not rows:
            raise SystemExit("scorecard: history %s is empty" % history)
        i = -1 if ref == "last" else -2
        if len(rows) < (1 if ref == "last" else 2):
            raise SystemExit("scorecard: history has too few rows for %r" % ref)
        row = rows[i]
    else:
        row = next((r for r in rows if r["run_id"] == ref), None)
        if not row:
            raise SystemExit("scorecard: %r is not a file, baseline, last/prev, or a run id in %s" % (ref, history))
    if not os.path.isfile(row["scorecard"]):
        raise SystemExit("scorecard: scorecard file of run %s is gone: %s" % (row["run_id"], row["scorecard"]))
    return jload(row["scorecard"]), row["scorecard"]


def compare_cards(a, b, tol=5.0, check_tol=1.0):
    """-> dict(overall, gates, regressions[], improvements[], warnings[]). b is the NEW run, a the old/baseline."""
    out = dict(a=a["run_id"], b=b["run_id"], a_version=a.get("vault_version"), b_version=b.get("vault_version"), overall=dict(a=a["overall"], b=b["overall"], delta=round(b["overall"] - a["overall"], 1)),
               gates={}, regressions=[], improvements=[], warnings=[])
    if a.get("game") != b.get("game"):
        out["warnings"].append("different games (%s vs %s): comparable only if both are the same standard spec" % (a.get("game"), b.get("game")))
    if (a.get("spec") or "") != (b.get("spec") or ""):
        out["warnings"].append("different specs (%r vs %r): the spec gate is not comparable" % (a.get("spec"), b.get("spec")))
    elif a.get("spec") and a.get("spec_version") != b.get("spec_version"):
        out["warnings"].append("spec version changed (%s -> %s)" % (a.get("spec_version"), b.get("spec_version")))
    if out["overall"]["delta"] < -tol:
        out["regressions"].append("overall dropped %.1f (%.1f -> %.1f)" % (-out["overall"]["delta"], a["overall"], b["overall"]))
    elif out["overall"]["delta"] > tol:
        out["improvements"].append("overall rose %.1f (%.1f -> %.1f)" % (out["overall"]["delta"], a["overall"], b["overall"]))
    names = sorted(set(a["gates"]) | set(b["gates"]))
    for n in names:
        ga, gb = a["gates"].get(n), b["gates"].get(n)
        if ga is None:
            out["gates"][n] = dict(status="new gate", b=gb["score"], status_b=gb["status"])
            out["improvements"].append("new gate %s (%s, %.1f)" % (n, gb["status"], gb["score"]))
            continue
        if gb is None:
            out["gates"][n] = dict(status="gate gone", a=ga["score"], status_a=ga["status"])
            out["regressions"].append("gate %s present before (%s) but absent now" % (n, ga["status"]))
            continue
        d = round(gb["score"] - ga["score"], 1)
        cd = {}
        for k in sorted(set(ga["checks"]) | set(gb["checks"])):
            va, vb = ga["checks"].get(k), gb["checks"].get(k)
            if va is not None and vb is not None:
                cd[k] = dict(a=va, b=vb, delta=round(vb - va, 2))
                if vb - va <= -check_tol:
                    out["regressions"].append("%s %s dropped %.1f (%g -> %g)" % (n, k, va - vb, va, vb))
                elif vb - va >= check_tol:
                    out["improvements"].append("%s %s rose %.1f (%g -> %g)" % (n, k, vb - va, va, vb))
        out["gates"][n] = dict(a=ga["score"], b=gb["score"], delta=d, status_a=ga["status"], status_b=gb["status"], checks=cd)
        if RANK.get(gb["status"], 0) < RANK.get(ga["status"], 0):
            out["regressions"].append("%s gate went %s -> %s" % (n, ga["status"], gb["status"]))
        elif RANK.get(gb["status"], 0) > RANK.get(ga["status"], 0):
            out["improvements"].append("%s gate went %s -> %s" % (n, ga["status"], gb["status"]))
        if d <= -tol:
            out["regressions"].append("%s score dropped %.1f (%.1f -> %.1f)" % (n, -d, ga["score"], gb["score"]))
        elif d >= tol:
            out["improvements"].append("%s score rose %.1f (%.1f -> %.1f)" % (n, d, ga["score"], gb["score"]))
    return out


def compare_md(c):
    L = ["# Compare %s -> %s" % (c["a"], c["b"]), "", "Vault version: %s -> %s" % (c["a_version"], c["b_version"]), "",
         "Overall: %.1f -> %.1f (%+.1f)" % (c["overall"]["a"], c["overall"]["b"], c["overall"]["delta"]), "", "| gate | before | after | delta | status |", "|---|---|---|---|---|"]
    for n, g in c["gates"].items():
        if "delta" in g:
            L.append("| %s | %.1f | %.1f | %+.1f | %s -> %s |" % (n, g["a"], g["b"], g["delta"], g["status_a"], g["status_b"]))
        else:
            L.append("| %s | %s | %s | | %s |" % (n, g.get("a", "-"), g.get("b", "-"), g["status"]))
    cks = [(n, k, v) for n, g in c["gates"].items() for k, v in (g.get("checks") or {}).items() if v["delta"] != 0]
    if cks:
        L += ["", "Per-check changes: " + ", ".join("%s/%s %+.1f" % (n, k, v["delta"]) for n, k, v in cks)]
    L += ["", "## Regressions (%d)" % len(c["regressions"])] + (["- " + x for x in c["regressions"]] or ["none"])
    L += ["", "## Improvements (%d)" % len(c["improvements"])] + (["- " + x for x in c["improvements"]] or ["none"])
    if c["warnings"]:
        L += ["", "## Warnings"] + ["- " + x for x in c["warnings"]]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ spec rendering
def spec_md(s):
    L = ["# %s" % s["title"], "", "Spec id `%s`, version %s, target stage `%s`. Suggested budget: %s minutes, %s turns (record the real numbers in benchmark-run.json)." % (
        s["id"], s["version"], s["stage_target"], s["budget"]["suggested_minutes"], s["budget"]["suggested_turns"]), "",
         "## Fixed prompt (give it verbatim, change nothing, in every version you compare)", "", "> " + s["prompt"], "", "## Target features (the critic scores each 0, 0.5 or 1 with evidence)", "",
         "| id | weight | feature |", "|---|---|---|"]
    for f in s["features"]:
        L.append("| %s | %d | %s |" % (f["id"], f.get("weight", 1), f["text"]))
    L += ["", "## Required screenshots (viewport-moment, as in rbx-visual; 6 base + extras)", "", ", ".join("%s-%s" % (x["viewport"], x["moment"]) for x in s["required_screenshots"]), "",
          "## Scan points (the placement scan must contain models whose path matches)", "", "| id | pattern | min | meaning |", "|---|---|---|---|"]
    for p in s["scan_points"]:
        L.append("| %s | `%s` | %d | %s |" % (p["id"], p["pattern"], p.get("min", 1), p["text"]))
    L += ["", "## Scoring rubric (independent critic, 1-10 per item, evidence text per item; 3 = clearly failing, 7 = pass, 9 = front-page quality)", ""]
    for r in s["rubric"]:
        L += ["**%s %s**" % (r["id"], r["name"]), "- 3: " + r["anchors"]["3"], "- 7: " + r["anchors"]["7"], "- 9: " + r["anchors"]["9"], ""]
    L += ["## benchmark-scores.json template", "", "```json", json.dumps({"spec": s["id"], "scorer": "critic", "features": {f["id"]: 0 for f in s["features"]},
          "rubric": {r["id"]: 0 for r in s["rubric"]}, "evidence": {r["id"]: "what you saw, with file names" for r in s["rubric"]}}, indent=1), "```", "",
          "Spec gate = mean of: features (weighted coverage x 10), rubric mean, screenshots found / required x 10, scan points met / total x 10. Pass needs every part >= 7 and all features at 1."]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ CLI
def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmds = ("collect", "compare", "baseline", "history", "verify", "spec")
    if argv[0] not in cmds and os.path.exists(argv[0]):
        argv.insert(0, "collect")
    ap = argparse.ArgumentParser(prog="scorecard.py")
    sp = ap.add_subparsers(dest="cmd")
    c = sp.add_parser("collect")
    c.add_argument("path"); c.add_argument("--game"); c.add_argument("--spec"); c.add_argument("--scores"); c.add_argument("--bench-dir"); c.add_argument("--history")
    c.add_argument("--no-history", action="store_true"); c.add_argument("--label", default=""); c.add_argument("--vault-version"); c.add_argument("--kit"); c.add_argument("--project")
    c.add_argument("--require-critic", action="store_true"); c.add_argument("--date"); c.add_argument("--json", action="store_true")
    m = sp.add_parser("compare")
    m.add_argument("a"); m.add_argument("b"); m.add_argument("--bench-dir"); m.add_argument("--history"); m.add_argument("--tolerance", type=float, default=5.0)
    m.add_argument("--check-tolerance", type=float, default=1.0); m.add_argument("--strict", action="store_true"); m.add_argument("--json", action="store_true")
    b = sp.add_parser("baseline")
    b.add_argument("action", choices=["set", "show"]); b.add_argument("card", nargs="?"); b.add_argument("--bench-dir")
    h = sp.add_parser("history")
    h.add_argument("--bench-dir"); h.add_argument("--history"); h.add_argument("--game")
    v = sp.add_parser("verify")
    v.add_argument("card")
    s = sp.add_parser("spec")
    s.add_argument("action", choices=["list", "show", "write-md", "check-md"]); s.add_argument("id", nargs="?"); s.add_argument("--dir")
    a = ap.parse_args(argv)
    if a.cmd == "collect":
        bench = bench_dir_for(a.path, a.bench_dir)
        card = collect(a.path, a.game, a.spec, a.scores, a.require_critic, a.project, a.vault_version, a.kit, a.label, a.date)
        rd = os.path.join(bench, "runs", card["run_id"])
        os.makedirs(rd, exist_ok=True)
        jp = os.path.join(rd, "scorecard.json")
        with open(jp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(card, f, indent=1)
            f.write("\n")
        md = card_md(card)
        with open(os.path.join(rd, "scorecard.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(md)
        if a.json:
            json.dump(card, sys.stdout, indent=1)
            print()
        else:
            sys.stdout.write(md)
        print("WROTE " + jp, file=sys.stderr)
        if not a.no_history:
            hp = a.history or os.path.join(bench, "history.csv")
            append_history(hp, history_row(card, jp))
            print("HISTORY " + hp, file=sys.stderr)
        return 0
    if a.cmd == "compare":
        bench = bench_dir_for(os.getcwd(), a.bench_dir)
        hist = a.history or os.path.join(bench, "history.csv")
        ca, pa = resolve_card(a.a, bench, hist)
        cb, pb = resolve_card(a.b, bench, hist)
        r = compare_cards(ca, cb, a.tolerance, a.check_tolerance)
        if a.json:
            json.dump(r, sys.stdout, indent=1)
            print()
        else:
            sys.stdout.write(compare_md(r))
        return 1 if (a.strict and r["regressions"]) else 0
    if a.cmd == "baseline":
        bench = bench_dir_for(os.getcwd(), a.bench_dir)
        bp = os.path.join(bench, "baseline.json")
        if a.action == "set":
            if not a.card or not os.path.isfile(a.card):
                raise SystemExit("scorecard: baseline set needs a scorecard.json")
            card = jload(a.card)
            if card.get("kind") != "vault-scorecard":
                raise SystemExit("scorecard: %s is not a vault-scorecard" % a.card)
            os.makedirs(bench, exist_ok=True)
            with open(bp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(card, f, indent=1)
                f.write("\n")
            print("baseline set: %s (overall %.1f, vault %s) -> %s" % (card["run_id"], card["overall"], card["vault_version"], bp))
        else:
            if not os.path.isfile(bp):
                print("no baseline (%s)" % bp)
                return 1
            card = jload(bp)
            print("baseline: %s | %s | overall %.1f | vault %s | game %s spec %s" % (card["run_id"], card["date"], card["overall"], card["vault_version"], card["game"], card["spec"]))
        return 0
    if a.cmd == "history":
        bench = bench_dir_for(os.getcwd(), a.bench_dir)
        rows = read_history(a.history or os.path.join(bench, "history.csv"))
        if a.game:
            rows = [r for r in rows if r["game"] == a.game]
        print("%-10s %-24s %-8s %-6s %-5s %-6s %-6s %s" % ("date", "vault_version", "overall", "grade", "req", "visual", "critic", "game/spec"))
        for r in rows:
            print("%-10s %-24s %-8s %-6s %-5s %-6s %-6s %s %s" % (r["date"], r["vault_version"][:24], r["overall"], r["grade"], r["all_required_pass"], r["visual"], r["critic"], r["game"], r["spec"]))
        return 0
    if a.cmd == "verify":
        card = jload(a.card)
        root = card.get("root", "")
        bad = 0
        for n, g in card["gates"].items():
            if not g.get("source") or not g.get("sha256"):
                continue
            p = os.path.join(root, g["source"])
            if not os.path.isfile(p):
                print("MISSING %s: %s" % (n, p))
                bad += 1
            elif sha256_file(p) != g["sha256"]:
                print("CHANGED %s: %s differs from the scored version" % (n, p))
                bad += 1
            else:
                print("ok      %s" % n)
        print("VERIFY: %s" % ("FAIL (%d)" % bad if bad else "ok"))
        return 1 if bad else 0
    if a.cmd == "spec":
        if a.action == "list":
            for i in spec_ids():
                s = jload(os.path.join(SPEC_DIR, i + ".json"))
                print("%-14s %s" % (i, s["title"]))
        elif a.action == "show":
            sys.stdout.write(spec_md(load_spec(a.id)))
        else:
            d = a.dir or SPEC_DIR
            bad = 0
            for i in spec_ids():
                t = spec_md(jload(os.path.join(SPEC_DIR, i + ".json")))
                p = os.path.join(d, i + ".md")
                if a.action == "write-md":
                    with open(p, "w", encoding="utf-8", newline="\n") as f:
                        f.write(t)
                    print("WROTE " + p)
                elif read_text(p).replace("\r\n", "\n") != t:
                    print("OUT OF DATE " + p)
                    bad += 1
            if a.action == "check-md":
                print("spec md check: %s" % ("FAIL" if bad else "ok"))
                return 1 if bad else 0
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
