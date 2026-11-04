#!/usr/bin/env python3
"""verdict.py - deterministic GOOD / NOT YET / BAD from critic scores (rules: game-dev-workflow/references/stages.md section 4).

  python verdict.py <input.json> [--write <Games/slug>] [--report <body.md>]
input.json: {"stage": "playtest", "works": "pass"|"fail"|"fail-severe", "hard_rule_violation": false,
             "scores": {"F1": 7, "F2": 8, ...}, "game": "slug", "evidence_note": "optional",
             "visual_gate": "<path to the critic's gate-critic.json>" | {gate dict},
             "placement_gate": "<path to the critic's fresh placement scan, Games/<slug>/placement-qa/scan-critic.json>" | {scan dict},
             "project": "<project folder, optional>"}
LOOKS (the visual gate, game-dev-visual-qa/scripts/visual_gate.py) is the third axis next to WORKS and GOOD: from stage prototype on, a verdict can only be
GOOD when the gate record passes; missing, skipped or failing = at most NOT YET and the status label "playable prototype, visuals not polished".
PLACEMENT (game-dev-placement-qa/scripts/placement_gate.py) is the fourth: every model in the map checked for pivot, size, grounding, upright, facing, overlap,
physics flags and connections. From stage prototype on GOOD needs `placement: pass` from a scan made by the CRITIC (scorer critic); missing, skipped or failing =
at most NOT YET and the label "playable prototype, placement not verified". The written verdict file carries `visual: <status>` and `placement: <status>`
lines; `games.py advance` refuses anything but pass for both.
Only factors present in "scores" count (unscored = N/A for this stage). Critical factors per stage count double and need their minimum.
--write DIR writes DIR/critic/<date>-<stage>.md with frontmatter (stage, verdict, date, score) + the body from --report. `games.py advance` reads that file.
"""
import datetime, json, os, sys

VISUAL_STAGES = ("prototype", "playtest", "launch", "growth", "live-ops")

CRIT = {  # stage -> {factor: minimum}
    "idea": {"F1": 6, "F2": 6, "F7": 6, "F10": 6},
    "prototype": {"F1": 6, "F2": 6},
    "playtest": {"F1": 6, "F2": 6, "F3": 6, "F4": 6, "F7": 6, "F9": 6},
    "launch": {"F8": 7},
    "growth": {},
    "live-ops": {},
}


def looks(d, stage):
    """-> (status pass|fail|skipped|n/a, label, reasons). Missing gate record = skipped = not a pass."""
    if stage not in VISUAL_STAGES:
        return "n/a", "", []
    vg = d.get("visual_gate")
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "game-dev-visual-qa", "scripts"))
        import visual_gate
    except Exception:
        return "skipped", "playable prototype, visuals not polished", ["visual gate script not found (install game-dev-visual-qa)"]
    base = "."
    if isinstance(vg, str):
        base = os.path.dirname(os.path.dirname(os.path.abspath(vg)))  # <Games/slug>/visual-qa/gate-critic.json -> <Games/slug>
        try:
            vg = json.load(open(vg, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped", visual_gate.NOT_POLISHED, ["visual gate file unreadable: %s" % e]
    if not vg:
        return "skipped", visual_gate.NOT_POLISHED, ["visual gate not run (no screenshots scored): the critic cannot call this GOOD or done"]
    r = visual_gate.evaluate(vg, base, d.get("project"))
    return r["status"], r["label"], r["reasons"]


def placing(d, stage):
    """-> (status pass|fail|skipped|n/a, label, reasons). A missing scan, or one the critic did not make itself, is not a pass."""
    if stage not in VISUAL_STAGES:
        return "n/a", "", []
    pg = d.get("placement_gate")
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "game-dev-placement-qa", "scripts"))
        import placement_gate
    except Exception:
        return "skipped", "playable prototype, placement not verified", ["placement gate script not found (install game-dev-placement-qa)"]
    base = "."
    if isinstance(pg, str):
        base = os.path.dirname(os.path.dirname(os.path.abspath(pg)))  # <Games/slug>/placement-qa/scan-critic.json -> <Games/slug>
        try:
            pg = json.load(open(pg, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped", placement_gate.NOT_VERIFIED, ["placement scan unreadable: %s" % e]
    if not pg:
        return "skipped", placement_gate.NOT_VERIFIED, ["placement scan not run: the critic cannot call this GOOD or done (run game-dev-placement-qa over the whole map)"]
    r = placement_gate.evaluate(pg, base, d.get("project"), "critic")
    return r["status"], r["label"], r["reasons"]


def main():
    a = [x for x in sys.argv[1:]]
    if not a:
        sys.exit(__doc__)
    d = json.load(open(a[0], encoding="utf-8-sig"))
    stage = d.get("stage", "idea")
    if stage not in CRIT:
        sys.exit("unknown stage %r" % stage)
    sc = {k: float(v) for k, v in d.get("scores", {}).items() if v is not None}
    if not sc:
        sys.exit("no scores given: a verdict needs at least one scored factor with evidence")
    crit = CRIT[stage]
    num = sum(v * (2 if k in crit else 1) for k, v in sc.items())
    den = sum(2 if k in crit else 1 for k in sc)
    mean = num / den
    below = {k: sc[k] for k, m in crit.items() if k in sc and sc[k] < m}
    missing = [k for k in crit if k not in sc]
    works = d.get("works", "pass")
    reasons = []
    vstat, vlabel, vreasons = looks(d, stage)
    pstat, plabel, preasons = placing(d, stage)
    if d.get("hard_rule_violation"):
        verdict = "BAD"; reasons.append("hard-rule violation (pay-to-win, paid randomness for kids, pressure timers, stranger contact or copied assets)")
    elif works == "fail-severe":
        verdict = "BAD"; reasons.append("WORKS fails severely (data loss / exposes players)")
    elif sc.get("F2", 10) <= 3:
        verdict = "BAD"; reasons.append("core loop F2 scored %s" % sc["F2"])
    elif mean < 4.5:
        verdict = "BAD"; reasons.append("mean %.2f is under 4.5" % mean)
    elif works != "pass" or below or missing or mean < 7.0 or vstat in ("fail", "skipped") or pstat in ("fail", "skipped"):
        verdict = "NOT YET"
        if vstat in ("fail", "skipped"): reasons.append("LOOKS = %s: %s" % (vstat, "; ".join(vreasons[:9])))
        if pstat in ("fail", "skipped"): reasons.append("PLACEMENT = %s: %s" % (pstat, "; ".join(preasons[:9])))
        if works != "pass": reasons.append("WORKS = %s" % works)
        if below: reasons.append("critical below minimum: " + ", ".join("%s=%g (min %d)" % (k, v, crit[k]) for k, v in below.items()))
        if missing: reasons.append("critical factors not scored (score them or the verdict cannot be GOOD): " + ", ".join(missing))
        if mean < 7.0: reasons.append("mean %.2f is under 7.00" % mean)
    else:
        verdict = "GOOD"; reasons.append("WORKS pass, mean %.2f, all critical factors at minimum" % mean)
    print("VERDICT: %s | stage %s | mean %.2f | works %s | looks %s | placement %s" % (verdict, stage, mean, works, vstat, pstat))
    if vstat in ("fail", "skipped"):
        print("STATUS: " + vlabel + " (never call this game done, complete or ready)")
    if pstat in ("fail", "skipped"):
        print("STATUS: " + plabel + " (never call this game done, complete or ready)")
    for r in reasons:
        print("  - " + r)
    lows = sorted(sc.items(), key=lambda kv: kv[1])[:3]
    print("  lowest factors (candidates for the top fixes): " + ", ".join("%s=%g" % kv for kv in lows))
    if "--write" in a:
        gd = a[a.index("--write") + 1]
        body = ""
        if "--report" in a:
            body = open(a[a.index("--report") + 1], encoding="utf-8").read()
        date = datetime.date.today().isoformat()
        os.makedirs(os.path.join(gd, "critic"), exist_ok=True)
        p = os.path.join(gd, "critic", "%s-%s.md" % (date, stage))
        slug = d.get("game") or os.path.basename(os.path.abspath(gd))
        head = "---\ntype: critic-verdict\ngame: %s\nstage: %s\nverdict: %s\ndate: %s\nscore: %.2f\nworks: %s\nvisual: %s\nplacement: %s\n---\n# Critic verdict: %s (%s, %s)\nBack to [[%s/GAME|GAME]] | [[%s/critic/README|all verdicts]]\n\n" % (slug, stage, verdict, date, mean, works, vstat, pstat, verdict, stage, date, slug, slug)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(head + "**Why:** " + "; ".join(reasons) + "\n\n" + body)
        print("WROTE " + p)


if __name__ == "__main__":
    main()
