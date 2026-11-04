---
name: rbx-placement
description: "Mandatory placement gate: every model created, inserted or moved is measured and fixed (pivot, size, grounded, upright, facing, overlap, physics flags) before work continues; fixes floating, buried, clipping or tilted models; whole-map scan in Studio. Done only at PLACEMENT GATE: PASS; run before visual QA and the critic."
argument-hint: "[game slug or project folder]"
---

# rbx-placement

Code comments: none by default (see rbx-luau, Comments).

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Why: models were left floating, buried, crooked, mis-facing, overlapping or unanchored because nothing measured them; WORKS, GOOD and LOOKS all miss it. This gate measures the geometry every time, and `rbx-critic` re-runs it independently and refuses GOOD without it.

## The rule (every model, every time)
**After every model create, insert or move: run `Placement.place(model, intent)` (or `Placement.verify` when you only moved or resized it), read the report, fix what failed, re-verify. Do not place the next model, start the next job or report back while the last one is `fail`.** Placing without verifying is the defect this skill exists to remove. This applies to models built from parts, `insert_asset`, `generate_mesh`, `generate_procedural_model`, `Clone`, terrain-adjacent props, spawner output and every later nudge or rotation.

## Definition of done (placement)
- The words done, complete, finished, ready, shipped, "good to go" about a game, map, level or build are allowed only when `placement_gate.py` printed `PLACEMENT GATE: PASS` for the CURRENT build (scan newer than the last Luau source and the last placement) AND the visual gate passed.
- Otherwise the status line is exactly: `playable prototype, placement not verified`, followed by the failing models (path, check, fix).
- A builder never grades itself: its scan guides the fix loop; the critic's own fresh scan (`scorer: critic`) decides.

## Loop
1. **Prereq**: write the intent per object (`references/intent.md`): kind, the surface it rests on, what it faces, grid, expected size, connections. Unknown kind = `prop`: grounded, upright, on the grid, clear and anchored are still checked; size and facing are `unverified`.
2. **Place**: Studio MCP (`rbx-studio`): `execute_luau` (datamodel Edit) with `scripts/placement_run.luau`, `CONFIG.mode = "place"` and `CONFIG.build` returning `{ { model = m, intent = {...} } }`; or call `Placement.place` from your build code (`scripts/Placement.luau`, or `src/shared/Placement.luau` in Rojo). It parents, moves to `intent.at`, measures, auto-fixes (upright, face, snap yaw, snap to ground, nudge out of overlap, anchor, remove junk parts, set PrimaryPart) and re-measures up to 6 passes.
3. **Read the report**: `status`, `failed`, then per failed check `issues` and `fixes`. What auto-fix cannot do (wrong size, no surface below, wrong surface, bad connection, design conflict) you fix by hand, then `Placement.verify` again. Record every report: `python scripts/placement_gate.py log <console-output-file> --write Games/<slug>` (the gate refuses a game whose latest report for a model is a fail, or a model placed after the last scan).
4. **Full-map scan before done** (and before every visual QA round): `CONFIG.mode = "scan"`, `CONFIG.scorer = "builder"`, root Workspace, datamodel Edit (and again in a Server playtest if models spawn at runtime). Save the console output and run `python scripts/placement_gate.py ingest <file> --game <slug> --scorer builder --write Games/<slug>`. It writes `Games/<slug>/placement-qa/scan-builder.json` and `gate.json` and prints PASS or FAIL with every failing model, its issues and the first suggested fix. Fix, re-scan, repeat until PASS.
5. **Critic**: `rbx-critic` makes its own scan (`CONFIG.scorer = "critic"`, ideally `includeInputs = true`), ingests it as `--scorer critic` (`placement-qa/scan-critic.json`) and passes it to `verdict.py` as `placement_gate`. GOOD needs `placement: pass` there; `games.py advance` refuses any verdict file without `placement: pass`.
6. **Stop rule**: three scans in a row still failing, or a failure needing a user decision (wrong-scale asset, design conflict): stop, report `playable prototype, placement not verified` and the failing list. Do not widen tolerances and do not waive to get a PASS: a waiver (`intent.waive = {P4 = "reason"}`) is for a deliberate, explained exception, and more than 10% of the models waived fails the gate.
7. Update `GAME.md` (`## Placement gate`) and `decisions.md`.

## Rules
- Evidence only: a placement is verified when the report says so; reading the positioning script is not verification. No Studio (no way to run Luau) = the gate stays `skipped`, say so, never claim it passed.
- Checks and tolerances: `references/checks.md`; intent fields: `references/intent.md`; API, report format, limits: `references/api.md`. Findings are measurements: an issue you disagree with is fixed in the intent (declare the true kind, surface, facing) or waived with a reason, never ignored.
- Placeholder positions are not placement: `at` and targets come from the design or the map, not invented numbers. Free assets from `insert_asset` often arrive with the wrong pivot or scale: P1 catches that.
- This skill moves only models you were asked to place; it never edits scripts, UI or lighting, nor anything outside the PROJECT folder and `Games/<slug>/placement-qa/`.
- `scripts/Placement.luau` and `scripts/placement_run.luau` are GENERATED by `python scripts/build_inline.py` from `PlacementCore.luau`, `adapter.src`, `runner.src`; gate maths and CLI: `scripts/placement_gate.py`; file roles: `references/api.md`.
