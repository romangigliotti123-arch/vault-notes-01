---
name: rbx-placement
description: "Mandatory placement gate: every model created, inserted or moved is measured and fixed (pivot, size, grounded, upright, facing, overlap, physics flags) before work continues; fixes floating, buried, clipping or tilted models; whole-map scan in Studio. Done only at PLACEMENT GATE: PASS; run before visual QA and the critic."
argument-hint: "[game slug or project folder]"
---

# rbx-placement

Code comments: none by default (see rbx-luau, Comments).

Precedence: When a kit skill and another installed skill cover the same job, use the kit skill.

Why this exists: models were repeatedly created or inserted and left floating, buried, crooked, facing the wrong way, overlapping the wall next to them or unanchored, because nothing measured them. WORKS (no errors), GOOD (fun) and LOOKS (screenshots) all miss it. This gate measures the geometry itself, every time, and `rbx-critic` re-runs it independently and refuses GOOD without it.

## The rule (every model, every time)
**After every model create, insert or move: run `Placement.place(model, intent)` (or `Placement.verify` when you only moved or resized it), read the report, fix what failed, re-verify. Do not place the next model, start the next job or report back while the last one is `fail`.** This applies to models you build from parts, `insert_asset`, `generate_mesh`, `generate_procedural_model`, `Clone`, terrain-adjacent props, spawner output and every later nudge or rotation. Placing without verifying is the defect this skill exists to remove.

## Definition of done (placement)
- The words done, complete, finished, ready, shipped, "good to go" about a game, map, level or build are allowed only when `placement_gate.py` printed `PLACEMENT GATE: PASS` for the CURRENT build (scan newer than the last Luau source and the last placement) AND the visual gate passed.
- Otherwise the status line is exactly: `playable prototype, placement not verified`, followed by the failing models (path, check, fix).
- A builder never grades itself: its scan guides the fix loop; the critic's own fresh scan (`scorer: critic`) decides.

## Loop
1. **Prereq**: know what each object is for. Write the intent (`references/intent.md`): kind, the surface it rests on, what it faces, grid, expected size, connections. Unknown kind = `prop`: grounded, upright, on the grid, clear and anchored are still checked; size and facing are reported `unverified`.
2. **Place**: Studio MCP (`rbx-studio`): `execute_luau` (datamodel Edit) with `scripts/placement_run.luau`, `CONFIG.mode = "place"` and `CONFIG.build` returning `{ { model = m, intent = {...} } }`; or call `Placement.place` from your own build code (module `scripts/Placement.luau`, or `src/shared/Placement.luau` in a Rojo project). It parents, moves to `intent.at`, measures, auto-fixes (stand upright, turn to face, snap yaw, snap to ground, nudge out of overlap, anchor, remove junk parts, set PrimaryPart) and re-measures up to 6 passes.
3. **Read the report**: `status`, `failed`, then for each failed check `issues` and `fixes`. Something the auto-fix cannot do (wrong size, no surface below, wrong surface, bad connection, design conflict) you fix by hand, then `Placement.verify` again. Record every report: `python scripts/placement_gate.py log <console-output-file> --write Games/<slug>` (the gate refuses a game whose latest report for a model is a fail, or a model placed after the last scan).
4. **Full-map scan before done** (and before every visual QA round): `CONFIG.mode = "scan"`, `CONFIG.scorer = "builder"`, root Workspace, datamodel Edit (and again in a Server playtest if models spawn at runtime). Save the console output and run `python scripts/placement_gate.py ingest <file> --game <slug> --scorer builder --write Games/<slug>`. It writes `Games/<slug>/placement-qa/scan-builder.json` and `gate.json` and prints PASS or FAIL with every failing model, its issues and the first suggested fix. Fix, re-scan, repeat until PASS.
5. **Critic**: `rbx-critic` makes its own scan (`CONFIG.scorer = "critic"`, ideally `includeInputs = true`), ingests it as `--scorer critic` (file `placement-qa/scan-critic.json`) and passes it to `verdict.py` as `placement_gate`. GOOD needs `placement: pass` there; `games.py advance` refuses any verdict file without `placement: pass`.
6. **Stop rule**: three scans in a row that still fail, or a failure that needs a decision only the user can make (a wrong-scale asset, a design conflict): stop, report `playable prototype, placement not verified` and the failing list. Do not widen tolerances and do not waive to get a PASS: a waiver (`intent.waive = {P4 = "reason"}`) is for a deliberate, explained exception and more than 10% of the models fails the gate.
7. Update `GAME.md` (`## Placement gate`) and `decisions.md`.

## Rules
- Evidence only: a placement is verified when the report says so; reading the script that positioned it is not verification. No Studio (no way to run Luau) = the gate stays `skipped`, say so, never claim it passed.
- The checks and tolerances are in `references/checks.md`; the intent fields in `references/intent.md`; API, report format and limits in `references/api.md`. Findings are measurements: an issue you disagree with is fixed in the intent (declare the true kind, surface, facing) or waived with a reason, never ignored.
- Placeholder positions are not placement: `at` and targets come from the design or the map, not from invented numbers. Free assets from `insert_asset` often arrive with the wrong pivot or scale: P1 exists to catch that.
- This skill moves only models you were asked to place; it never edits scripts, UI or lighting. Do not edit anything outside the PROJECT folder and `Games/<slug>/placement-qa/`.
- Scripts: `scripts/PlacementCore.luau` (pure, tested under Lune), `scripts/placement_ref.py` (Python twin used by the tests and by the gate to re-check stored inputs), `scripts/adapter.src` + `runner.src` (Roblox side), `scripts/Placement.luau` and `scripts/placement_run.luau` (GENERATED by `python scripts/build_inline.py`), `scripts/placement_gate.py` (gate maths and CLI). Tests: `tests/Placement.test.luau`, `tests/Adapter.test.luau`, `tests/fixtures.json` (`tests/make_fixtures.py`).

## Learn

