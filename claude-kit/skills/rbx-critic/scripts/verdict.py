#!/usr/bin/env python3
"""verdict.py - deterministic GOOD / NOT YET / BAD from critic scores (rules: rbx-workflow/references/stages.md section 4).

  python verdict.py <input.json> [--write <Games/slug>] [--report <body.md>]
input.json: {"stage": "playtest", "works": "pass"|"fail"|"fail-severe", "hard_rule_violation": false,
             "scores": {"F1": 7, "F2": 8, ...}, "game": "slug", "evidence_note": "optional",
             "visual_gate": "<path to the critic's gate-critic.json>" | {gate dict},
             "placement_gate": "<path to the critic's fresh placement scan, Games/<slug>/placement-qa/scan-critic.json>" | {scan dict},
             "lighting_gate": "<path to the critic's fresh lighting scan, Games/<slug>/lighting-qa/scan-critic.json>" | {scan dict}, "genre": "obby" (optional), "platform": "both" (optional),
             "code_gates": "<path to the critic's Games/<slug>/code-gates/run.json, written by code_gates.py --scorer critic --write>" | {run dict},
             "project": "<project folder, optional>"}
LOOKS (the visual gate, rbx-visual/scripts/visual_gate.py) is the third axis next to WORKS and GOOD: from stage prototype on, a verdict can only be
GOOD when the gate record passes; missing, skipped or failing = at most NOT YET and the status label "playable prototype, visuals not polished".
PLACEMENT (rbx-placement/scripts/placement_gate.py) is the fourth: every model in the map checked for pivot, size, grounding, upright, facing, overlap,
physics flags and connections. From stage prototype on GOOD needs `placement: pass` from a scan made by the CRITIC (scorer critic); missing, skipped or failing =
at most NOT YET and the label "playable prototype, placement not verified".
LIGHTING (rbx-lighting/scripts/lighting_gate.py) is the fifth: Lighting, Atmosphere, Sky and the post effects checked (L1-L12) for default Roblox look, sane
ranges, brightness, shadows, genre fog, interiors, mobile budget and conflicts. From stage prototype on GOOD needs `lighting: pass` from a scan made by the CRITIC; missing,
skipped or failing = at most NOT YET and the label "playable prototype, lighting not verified". The written verdict file carries `visual:`, `placement:` and `lighting:`
lines; `games.py advance` refuses anything but pass for all three (a verdict file without a `lighting:` line counts as missing: run a fresh critic pass).
CODE GATES (rbx-critic/scripts/code_gates.py: comment, scope/stubs, security, bug ledgers) are the sixth: GOOD needs proof that the CRITIC ran them (`codegates: ran`);
missing, builder-made, stale or incomplete = at most NOT YET and the label "playable prototype, code gates not run". Their findings are only SCORED (extra gates of
rbx-bench), a low score never changes the verdict. `games.py advance` needs `codegates: ran` (an older file without the line counts as missing).
HICCUPS (tools/hiccup.py check --scorer critic --write Games/<slug>, read from hiccup-qa/gate-critic.json or given as `hiccup_gate`) are the seventh, ADVISORY: the verdict file carries
`retro: ran|skipped|n/a` (ran = the critic compared the objective hiccup sources with the ledger AND the done-step retro ran); unreported hiccups are SCORED by rbx-bench and listed, never blocking (RETRO_REQUIRED).
UI DESIGN (rbx-ui-mockup, Games/<slug>/ui-design-qa/gate.json from ui_compare.py gate|skip) is the eighth, ADVISORY: the verdict file carries
`uidesign: done|skipped|n/a` (done = a design-first record with a mode auto|figma|manual); never changes the verdict (UIDESIGN_REQUIRED).
THUMBNAIL (rbx-thumbnail, Games/<slug>/thumb-score/gate.json from thumb_score.py score|skip) is the ninth, ADVISORY, asked only at stages launch, growth and live-ops: the verdict file carries
`thumbnail: scored S/M (variants N)|skipped: reason|n/a`; never changes the verdict (THUMBNAIL_REQUIRED).
Only factors present in "scores" count (unscored = N/A for this stage). Critical factors per stage count double and need their minimum.
--write DIR writes DIR/critic/<date>-<stage>.md with frontmatter (stage, verdict, date, score) + the body from --report. `games.py advance` reads that file.
"""
import datetime, json, os, subprocess, sys

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
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "rbx-visual", "scripts"))
        import visual_gate
    except Exception:
        return "skipped", "playable prototype, visuals not polished", ["visual gate script not found (install rbx-visual)"]
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
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "rbx-placement", "scripts"))
        import placement_gate
    except Exception:
        return "skipped", "playable prototype, placement not verified", ["placement gate script not found (install rbx-placement)"]
    base = "."
    if isinstance(pg, str):
        base = os.path.dirname(os.path.dirname(os.path.abspath(pg)))  # <Games/slug>/placement-qa/scan-critic.json -> <Games/slug>
        try:
            pg = json.load(open(pg, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped", placement_gate.NOT_VERIFIED, ["placement scan unreadable: %s" % e]
    if not pg:
        return "skipped", placement_gate.NOT_VERIFIED, ["placement scan not run: the critic cannot call this GOOD or done (run rbx-placement over the whole map)"]
    r = placement_gate.evaluate(pg, base, d.get("project"), "critic")
    return r["status"], r["label"], r["reasons"]


def lit(d, stage):
    """-> (status pass|fail|skipped|n/a, label, reasons). A missing scan, or one the critic did not make itself, is not a pass."""
    if stage not in VISUAL_STAGES:
        return "n/a", "", []
    lg = d.get("lighting_gate")
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "rbx-lighting", "scripts"))
        import lighting_gate
    except Exception:
        return "skipped", "playable prototype, lighting not verified", ["lighting gate script not found (install rbx-lighting)"]
    base = "."
    if isinstance(lg, str):
        base = os.path.dirname(os.path.dirname(os.path.abspath(lg)))  # <Games/slug>/lighting-qa/scan-critic.json -> <Games/slug>
        try:
            lg = json.load(open(lg, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped", lighting_gate.NOT_VERIFIED, ["lighting scan unreadable: %s" % e]
    if not lg:
        return "skipped", lighting_gate.NOT_VERIFIED, ["lighting scan not run: the critic cannot call this GOOD or done (run rbx-lighting: LightingKit.scan on the whole place)"]
    r = lighting_gate.evaluate(lg, base, d.get("project"), "critic", d.get("genre"), d.get("platform"))
    return r["status"], r["label"], r["reasons"] + ["%s %s: %s" % (f["check"], f["name"], "; ".join(f["issues"][:1])) for f in r["failing"][:6]]


RETRO_REQUIRED = False


def retro(d, stage, gd=None):
    """-> (status ran|skipped|n/a, reasons). Advisory while RETRO_REQUIRED is False: proof that the critic ran hiccup.py check and that the done-step retro ran."""
    if stage not in VISUAL_STAGES:
        return "n/a", []
    hg = d.get("hiccup_gate")
    if hg is None and gd and os.path.isfile(os.path.join(gd, "hiccup-qa", "gate-critic.json")):
        hg = os.path.join(gd, "hiccup-qa", "gate-critic.json")
    if isinstance(hg, str):
        try:
            hg = json.load(open(hg, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped", ["hiccup check record unreadable: %s" % e]
    if not isinstance(hg, dict):
        return "skipped", ["hiccup check not run by the critic (hiccup.py check --scorer critic --write Games/<slug>)"]
    if str(hg.get("scorer", "")).lower() != "critic":
        return "skipped", ["hiccup check run by %r, not by the critic" % hg.get("scorer")]
    rs = [str(x)[:160] for x in (hg.get("reasons") or [])][:3]
    if not hg.get("retro_ran"):
        return "skipped", ["retro not run in the done step (hiccup.py retro)"] + rs
    return "ran", rs


UIDESIGN_REQUIRED = False


def uidesign(d, stage, gd=None):
    """-> (line, reasons). Advisory while UIDESIGN_REQUIRED is False: `done (mode)` / `skipped: reason` / `n/a` from ui-design-qa/gate.json (ui_compare.py)."""
    if stage not in VISUAL_STAGES:
        return "n/a", []
    g = d.get("ui_design_gate")
    if g is None and gd and os.path.isfile(os.path.join(gd, "ui-design-qa", "gate.json")):
        g = os.path.join(gd, "ui-design-qa", "gate.json")
    if isinstance(g, str):
        try:
            g = json.load(open(g, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped", ["ui design record unreadable: %s" % e]
    if not isinstance(g, dict):
        return "skipped", ["no UI design record (rbx-ui-mockup: ui_compare.py gate or skip --write Games/<slug>)"]
    if g.get("done"):
        return "done (%s)" % g.get("mode", "auto"), []
    return "skipped", [str(g.get("reason", "no reason given"))[:160]]


THUMBNAIL_REQUIRED = False
THUMB_STAGES = ("launch", "growth", "live-ops")


def thumbnail(d, stage, gd=None):
    """-> (line, reasons). Advisory while THUMBNAIL_REQUIRED is False: `scored S/M (variants N)` / `skipped: reason` / `n/a` from thumb-score/gate.json (thumb_score.py)."""
    if stage not in THUMB_STAGES:
        return "n/a", []
    g = d.get("thumb_gate")
    if g is None and gd and os.path.isfile(os.path.join(gd, "thumb-score", "gate.json")):
        g = os.path.join(gd, "thumb-score", "gate.json")
    if isinstance(g, str):
        try:
            g = json.load(open(g, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped: thumbnail record unreadable", [str(e)[:160]]
    if not isinstance(g, dict):
        return "skipped: not run", ["no thumbnail score record (rbx-thumbnail: thumb_score.py score or skip --write Games/<slug>)"]
    if g.get("done"):
        return "scored %s/%s (variants %s)" % (g.get("score"), g.get("max"), g.get("variants")), [] if g.get("result") == "pass" else ["best variant did not pass: " + "; ".join(str(x)[:120] for x in (g.get("reasons") or [])[:2])]
    return "skipped: " + str(g.get("reason", "no reason given"))[:160], []


def readme_state(gd, project=None):
    """ok | stale | missing | n/a: the game README vs the newest design, decisions, systems, playtest, weekly note or Luau source. ADVISORY."""
    if not gd or not os.path.isdir(gd):
        return "n/a"
    rp = os.path.join(gd, "README.md")
    if not os.path.isfile(rp):
        return "missing"
    fs = [os.path.join(gd, n) for n in ("design.md", "decisions.md", "systems.md")] + [os.path.join(gd, s, f) for s in ("playtests", "weekly") if os.path.isdir(os.path.join(gd, s)) for f in os.listdir(os.path.join(gd, s)) if f.endswith(".md") and f.lower() != "readme.md"]
    pj = project if project and os.path.isdir(project) else os.path.join(gd, "project")
    return "stale" if max([os.path.getmtime(x) for x in fs if os.path.isfile(x)] + [newest_source(pj) if os.path.isdir(pj) else 0.0]) > os.path.getmtime(rp) + 2 else "ok"


def refresh_readme(gd):
    cfg = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    for g in (os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools", "games.py"), os.path.join(cfg, "claude-kit", "tools", "games.py")):
        if os.path.isfile(g) and os.path.isfile(os.path.join(gd, "GAME.md")):
            try:
                subprocess.run([sys.executable, "-I", g, "--games", os.path.dirname(os.path.abspath(gd)), "refresh", os.path.basename(os.path.abspath(gd))], capture_output=True, timeout=30)
            except (OSError, subprocess.SubprocessError):
                pass
            return


CODE_LABEL = "playable prototype, code gates not run"
CODE_REQUIRED = ("comment", "scope", "security")


def newest_source(project):
    best = 0.0
    for d, dn, fn in os.walk(project):
        dn[:] = [x for x in dn if x.lower() not in (".git", "packages", "node_modules", "vendor")]
        for f in fn:
            if f.endswith((".lua", ".luau")):
                best = max(best, os.path.getmtime(os.path.join(d, f)))
    return best


def coding(d, stage):
    """-> (status ran|skipped|n/a, label, reasons). Only proof that the critic ran the code gates counts; their scores never decide."""
    if stage not in VISUAL_STAGES:
        return "n/a", "", []
    cg, path = d.get("code_gates"), None
    if isinstance(cg, str):
        path = cg
        try:
            cg = json.load(open(cg, encoding="utf-8-sig"))
        except Exception as e:
            return "skipped", CODE_LABEL, ["code gates run record unreadable: %s" % e]
    if not cg or not isinstance(cg, dict):
        return "skipped", CODE_LABEL, ["code gates not run: the critic cannot call this GOOD or done (run rbx-critic/scripts/code_gates.py with --scorer critic --write Games/<slug>)"]
    if str(cg.get("scorer", "")).lower() != "critic":
        return "skipped", CODE_LABEL, ["code gates run by %r, not by the critic: the critic runs its own" % cg.get("scorer")]
    miss = [g for g in CODE_REQUIRED if g not in (cg.get("ran") or [])]
    if miss:
        return "skipped", CODE_LABEL, ["code gate record lacks: " + ", ".join(miss)]
    if path and d.get("project") and os.path.isdir(d["project"]) and os.path.getmtime(path) < newest_source(d["project"]) - 1:
        return "skipped", CODE_LABEL, ["stale code gate run: a Luau source is newer than the run (re-run code_gates.py)"]
    return "ran", "", []


def main():
    a = [x for x in sys.argv[1:]]
    if not a:
        sys.exit(__doc__)
    d = json.load(open(a[0], encoding="utf-8-sig"))
    stage = d.get("stage", "idea")
    if stage not in CRIT:
        sys.exit("unknown stage %r" % stage)
    try:
        sc = {k: float(v) for k, v in d.get("scores", {}).items() if v is not None}
    except (TypeError, ValueError):
        sys.exit("scores must be numbers from 0 to 10")
    if any(not 0 <= v <= 10 for v in sc.values()):
        sys.exit("scores must be numbers from 0 to 10 (got %s)" % ", ".join("%s=%g" % kv for kv in sc.items() if not 0 <= kv[1] <= 10))
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
    lstat, llabel, lreasons = lit(d, stage)
    cstat, clabel, creasons = coding(d, stage)
    wdir = a[a.index("--write") + 1] if "--write" in a and a.index("--write") + 1 < len(a) else None
    rstat, rreasons = retro(d, stage, wdir)
    ustat, ureasons = uidesign(d, stage, wdir)
    tstat, treasons = thumbnail(d, stage, wdir)
    dstat = readme_state(wdir, d.get("project"))
    if d.get("hard_rule_violation"):
        verdict = "BAD"; reasons.append("hard-rule violation (pay-to-win, paid randomness for kids, pressure timers, stranger contact or copied assets)")
    elif works == "fail-severe":
        verdict = "BAD"; reasons.append("WORKS fails severely (data loss / exposes players)")
    elif sc.get("F2", 10) <= 3:
        verdict = "BAD"; reasons.append("core loop F2 scored %s" % sc["F2"])
    elif mean < 4.5:
        verdict = "BAD"; reasons.append("mean %.2f is under 4.5" % mean)
    elif works != "pass" or below or missing or mean < 7.0 or vstat in ("fail", "skipped") or pstat in ("fail", "skipped") or lstat in ("fail", "skipped") or cstat == "skipped":
        verdict = "NOT YET"
        if cstat == "skipped": reasons.append("CODE GATES = skipped: %s" % "; ".join(creasons[:3]))
        if vstat in ("fail", "skipped"): reasons.append("LOOKS = %s: %s" % (vstat, "; ".join(vreasons[:9])))
        if pstat in ("fail", "skipped"): reasons.append("PLACEMENT = %s: %s" % (pstat, "; ".join(preasons[:9])))
        if lstat in ("fail", "skipped"): reasons.append("LIGHTING = %s: %s" % (lstat, "; ".join(lreasons[:9])))
        if works != "pass": reasons.append("WORKS = %s" % works)
        if below: reasons.append("critical below minimum: " + ", ".join("%s=%g (min %d)" % (k, v, crit[k]) for k, v in below.items()))
        if missing: reasons.append("critical factors not scored (score them or the verdict cannot be GOOD): " + ", ".join(missing))
        if mean < 7.0: reasons.append("mean %.2f is under 7.00" % mean)
    else:
        verdict = "GOOD"; reasons.append("WORKS pass, mean %.2f, all critical factors at minimum" % mean)
    print("VERDICT: %s | stage %s | mean %.2f | works %s | looks %s | placement %s | lighting %s | code gates %s | retro %s | ui design %s | thumbnail %s" % (verdict, stage, mean, works, vstat, pstat, lstat, cstat, rstat, ustat, tstat))
    if tstat.startswith("skipped") or treasons:
        print("THUMBNAIL: %s (advisory, never changes the verdict)" % ("; ".join(treasons[:2]) or tstat))
    if dstat in ("stale", "missing"):
        print("README: %s (advisory): update the hand-written sections of %s/README.md" % (dstat, wdir))
    if ustat.startswith("skipped"):
        print("UI DESIGN: %s (advisory, never changes the verdict)" % "; ".join(ureasons[:2]))
    if rstat == "skipped":
        print("RETRO: skipped (%s; advisory, scored by rbx-bench)" % "; ".join(rreasons[:2]))
    elif rstat == "ran" and rreasons:
        print("RETRO: ran; unreported hiccups are scored, not blocking: " + "; ".join(rreasons[:2]))
    if vstat in ("fail", "skipped"):
        print("STATUS: " + vlabel + " (never call this game done, complete or ready)")
    if pstat in ("fail", "skipped"):
        print("STATUS: " + plabel + " (never call this game done, complete or ready)")
    if lstat in ("fail", "skipped"):
        print("STATUS: " + llabel + " (never call this game done, complete or ready)")
    if cstat == "skipped":
        print("STATUS: " + clabel + " (never call this game done, complete or ready)")
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
        head = "---\ntype: critic-verdict\ngame: %s\nstage: %s\nverdict: %s\ndate: %s\nscore: %.2f\nworks: %s\nvisual: %s\nplacement: %s\nlighting: %s\ncodegates: %s\nretro: %s\nuidesign: %s\nthumbnail: %s\nreadme: %s\n---\n# Critic verdict: %s (%s, %s)\nBack to [[%s/GAME|GAME]] | [[%s/critic/README|all verdicts]]\n\n" % (slug, stage, verdict, date, mean, works, vstat, pstat, lstat, cstat, rstat, ustat, tstat, dstat, verdict, stage, date, slug, slug)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(head + "**Why:** " + "; ".join(reasons) + "\n\n" + body)
        print("WROTE " + p)
        refresh_readme(gd)


if __name__ == "__main__":
    main()
