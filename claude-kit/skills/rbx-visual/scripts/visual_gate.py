#!/usr/bin/env python3
"""visual_gate.py: deterministic pass/fail of the visual gate (rubric V1-V7 in references/rubric.md). Nobody eyeballs the result.

  python visual_gate.py <gate.json> [--project DIR] [--write Games/<slug>] [--require-placement] [--require-lighting]

gate.json:
  {"game": "slug", "round": 1, "scorer": "builder" | "critic",
   "scores": {"V1": 8, ..., "V7": 7},                       # all seven, 1-10, each with evidence in the round notes
   "hard_fails": ["V2: banner hidden behind HUD at phone"],  # any entry = FAIL (list what is still broken; [] when none)
   "overlap": {"phone": 0, "tablet": 0, "desktop": 0},       # findings from scripts/ui_overlap.luau per viewport
   "screenshots": [{"path": "visual-qa/r1/desktop-spawn.png", "viewport": "desktop", "moment": "spawn"}, ...],
   "defects": ["V4 pufferfish is a flat sprite"]}            # optional, copied to the report and the polish backlog

PASS needs ALL of: every V1-V7 score >= 7; no hard_fails; overlap == 0 for phone, tablet and desktop; >= 6 distinct screenshot files that exist
(png/jpg, >= 10 KB), covering viewports desktop AND phone and moments spawn, action and effect; and, when --project is given and it has Luau
sources, no screenshot older than the newest source file (stale = the build changed after the picture). Paths are relative to --write's folder
or the gate file's folder. With --write (or --require-placement) `<Games/slug>/placement-qa/gate.json` must say result pass (rbx-placement runs
BEFORE the visual review). The lighting gate (rbx-lighting, checks L1-L12) is judged BEFORE the V-checks too: `<Games/slug>/lighting-qa/gate.json` is recorded
in the result as `lighting_gate` (pass / fail / missing) and printed as a note; with --require-lighting a missing or failing lighting gate fails the visual gate (the skills
call it that way; the critic's verdict needs `lighting: pass` in any case, see verdict.py).
Importable: evaluate(gate_dict, base_dir, project, require_placement=False, require_lighting=False) -> dict(status, reasons, lowest, label, lighting_gate).
"""
import hashlib
import json
import os
import sys

ITEMS = ["V1", "V2", "V3", "V4", "V5", "V6", "V7"]
NAMES = {"V1": "UI consistency", "V2": "Layout and overlap", "V3": "Readability and hierarchy", "V4": "Models and world",
         "V5": "Lighting and atmosphere", "V6": "Effects and juice", "V7": "First 30 seconds"}
PASS_MIN = 7
MIN_SHOTS = 6
MIN_BYTES = 10 * 1024
NOT_POLISHED = "playable prototype, visuals not polished"
POLISHED = "visuals polished (visual gate passed)"


def _newest_source(project):
    newest = 0.0
    for root, dirs, files in os.walk(project):
        dirs[:] = [d for d in dirs if d.lower() not in ("packages", "vendor", "node_modules", ".git", "build", "docs")]
        for f in files:
            if f.endswith((".luau", ".lua")):
                newest = max(newest, os.path.getmtime(os.path.join(root, f)))
    return newest


def _placement_reason(base_dir):
    """The placement gate (rbx-placement) must have passed before the visuals are judged: models that float, clip or face the wrong way
    are not a polish problem. -> reason text or None."""
    p = os.path.join(base_dir, "placement-qa", "gate.json")
    if not os.path.isfile(p):
        return "placement gate not recorded (%s): run rbx-placement over the whole map and pass it before the visual review" % p
    try:
        rec = json.load(open(p, encoding="utf-8-sig"))
    except Exception as e:
        return "placement gate record unreadable: %s" % e
    if rec.get("result") != "pass":
        return "placement gate is %s (placement-qa/gate.json): fix the placement failures first, then judge the visuals" % rec.get("result")
    return None


def _lighting_state(base_dir):
    """-> (pass|fail|missing, reason text or None) from <Games/slug>/lighting-qa/gate.json (rbx-lighting)."""
    p = os.path.join(base_dir, "lighting-qa", "gate.json")
    if not os.path.isfile(p):
        return "missing", "lighting gate not recorded (%s): run rbx-lighting (LightingKit.apply the genre preset, scan, lighting_gate.py) before the visual review" % p
    try:
        rec = json.load(open(p, encoding="utf-8-sig"))
    except Exception as e:
        return "missing", "lighting gate record unreadable: %s" % e
    if rec.get("result") != "pass":
        return "fail", "lighting gate is %s (lighting-qa/gate.json): fix the L-check failures first, then judge V5 lighting and atmosphere" % rec.get("result")
    return "pass", None


def evaluate(gate, base_dir=".", project=None, require_placement=False, require_lighting=False):
    reasons = []
    if not isinstance(gate, dict):
        return dict(status="skipped", reasons=["no visual gate record"], lowest=[], label=NOT_POLISHED, lighting_gate="missing")
    lstate, lwhy = _lighting_state(base_dir)
    if require_lighting and lwhy:
        reasons.append(lwhy)
    if require_placement:
        why = _placement_reason(base_dir)
        if why:
            reasons.append(why)
    scores = gate.get("scores") or {}
    miss = [k for k in ITEMS if scores.get(k) is None]
    if miss:
        reasons.append("rubric items not scored: " + ", ".join(miss))
    low = sorted(((k, float(scores[k])) for k in ITEMS if scores.get(k) is not None), key=lambda kv: kv[1])
    for k, v in low:
        if v < PASS_MIN:
            reasons.append("%s %s scored %g (needs %d)" % (k, NAMES[k], v, PASS_MIN))
    for h in gate.get("hard_fails") or []:
        reasons.append("hard fail still open: " + str(h))
    ov = gate.get("overlap") or {}
    for vp in ("phone", "tablet", "desktop"):
        if ov.get(vp) is None:
            reasons.append("layout check (ui_overlap) missing for %s" % vp)
        elif ov[vp] != 0:
            reasons.append("layout check found %s issue(s) at %s" % (ov[vp], vp))
    shots = gate.get("screenshots") or []
    seen, views, moments, mt = set(), set(), set(), []
    for s in shots:
        p = s.get("path", "") if isinstance(s, dict) else str(s)
        full = p if os.path.isabs(p) else os.path.join(base_dir, p)
        if not os.path.isfile(full):
            reasons.append("screenshot missing: " + p)
            continue
        if not full.lower().endswith((".png", ".jpg", ".jpeg")) or os.path.getsize(full) < MIN_BYTES:
            reasons.append("screenshot not a real image (png/jpg, >= 10 KB): " + p)
            continue
        h = hashlib.sha256(open(full, "rb").read()).hexdigest()
        if h in seen:
            reasons.append("duplicate screenshot file: " + p)
            continue
        seen.add(h)
        mt.append(os.path.getmtime(full))
        if isinstance(s, dict):
            views.add(s.get("viewport", ""))
            moments.add(s.get("moment", ""))
    if len(seen) < MIN_SHOTS:
        reasons.append("%d distinct screenshots (need %d)" % (len(seen), MIN_SHOTS))
    for v in ("desktop", "phone"):
        if v not in views:
            reasons.append("no screenshot at viewport " + v)
    for m in ("spawn", "action", "effect"):
        if m not in moments:
            reasons.append("no screenshot of moment " + m)
    if project and mt:
        src = _newest_source(project)
        if src and min(mt) < src - 1:
            reasons.append("stale screenshots: a Luau source changed after the oldest screenshot; re-capture")
    status = "pass" if not reasons else "fail"
    return dict(status=status, reasons=reasons, lowest=low[:3], label=POLISHED if status == "pass" else NOT_POLISHED, lighting_gate=lstate, lighting_note=lwhy)


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        sys.exit(__doc__)
    gate = json.load(open(a[0], encoding="utf-8-sig"))
    project = a[a.index("--project") + 1] if "--project" in a else None
    out_dir = a[a.index("--write") + 1] if "--write" in a else None
    gdir = os.path.dirname(os.path.abspath(a[0]))
    base = out_dir or (os.path.dirname(gdir) if os.path.basename(gdir) == "visual-qa" else gdir)
    r = evaluate(gate, base, project, require_placement=bool(out_dir) or "--require-placement" in a, require_lighting="--require-lighting" in a)
    rnd = gate.get("round", 1)
    print("VISUAL GATE: %s | round %s | scorer %s" % (r["status"].upper(), rnd, gate.get("scorer", "?")))
    print("STATUS LABEL: " + r["label"])
    if r.get("lighting_note") and "--require-lighting" not in a:
        print("  NOTE (lighting, not blocking here; the critic verdict needs lighting: pass): " + r["lighting_note"])
    for x in r["reasons"]:
        print("  - " + x)
    if r["lowest"]:
        print("  lowest: " + ", ".join("%s %s=%g" % (k, NAMES[k], v) for k, v in r["lowest"]))
    if r["status"] == "fail" and int(rnd) >= 3:
        print("  ROUND CAP REACHED: stop iterating. Report the status label above and write the polish backlog from the open items.")
    if out_dir:
        d = os.path.join(out_dir, "visual-qa")
        os.makedirs(d, exist_ok=True)
        rec = dict(gate, result=r["status"], label=r["label"], reasons=r["reasons"], lighting_gate=r.get("lighting_gate"))
        json.dump(rec, open(os.path.join(d, "gate.json"), "w", encoding="utf-8", newline="\n"), indent=1)
        print("WROTE " + os.path.join(d, "gate.json"))
    sys.exit(0 if r["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
