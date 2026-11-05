# Placement API, output and how it runs

## Files (scripts/)
| file | what |
|---|---|
| `PlacementCore.luau` | the pure checks P1-P7 on plain tables (no Roblox API). Tested under Lune (`tests/Placement.test.luau`) |
| `placement_ref.py` | Python twin of the core: used by tests (65 fixtures, both implementations must agree) and by `placement_gate.py` to re-check reports that carry their inputs |
| `adapter.src` | the Roblox side: snapshots, ray casts, neighbour queries, fixes, `place`, `scan` |
| `Placement.luau` | GENERATED module = core + adapter. Copy to `src/shared/Placement.luau` (Rojo) or paste before your own code |
| `placement_run.luau` | GENERATED single file for `execute_luau`: edit `CONFIG` at the bottom, run. Rebuild with `python build_inline.py` (then stylua is applied by the script) |
| `placement_gate.py` | the gate: PASS/FAIL from a stored scan; `ingest` console output, `log` per-placement reports, `recheck` |

## Entry points
```lua
local Placement = require(path.to.Placement)
Placement.place(model, intent, opts)
Placement.verify(model, intent?, opts)
Placement.scan(root?, opts)
Placement.applyFixes(model, report)
Placement.Fix.snapToGround / rotateYaw / setUpright / moveBy / nudge / anchor / setCanCollide / removeParts / setPrimaryPart
Placement.setIntent(model, intent) / Placement.intentFor(model, opts) / Placement.snapshot(model) / Placement.collect(model, snap, intent) / Placement.objects(root, opts)
Placement.config
```
`place` parents the model, moves it to `intent.at`, then verify, auto-fix, re-verify (up to `opts.maxPasses`, 6) and returns the report. `verify` is read-only (intent from the argument, else the stored attribute, rules or name). `scan` checks every placed object under `root` (default Workspace) and prints one `PLACEMENT_MODEL` line each plus a `PLACEMENT_SCAN` summary. `applyFixes` is one correction pass from a report. `Placement.config` defaults: rayLift 4, rayLength 600, maxPasses 6, inferKind true, includeInputs false, groundNames, ignoreNames, core (tolerance and bounds overrides).
`opts` for `scan`: `game`, `scorer` ("builder" | "critic"), `intents`, `rules`, `defaultIntent`, `includeInputs` (store snapshot + environment in every report so `placement_gate.py` re-checks it offline), `compact` (default true for scans: passing checks shrink to their status), `emit = false` (no console lines).

Auto-fix order in one pass: non-geometric fixes together (remove junk, set PrimaryPart, anchor, collide flags), then ONE geometric fix in this order: setUpright, rotateYaw, moveBy, snapToGround, nudge (each changes the numbers of the next, so the model is re-measured between them). The loop stops on a pass, on no fix, on a repeated fix (not converging) or after `maxPasses`. A report whose `status` is `fail` after `place` means: do not move on; read `failed`, `checks.Pn.issues` and `fixes`, fix by hand or change the design, `verify` again.

## Report (per model)
```json
{"path": "Workspace.Map.House.Door", "class": "Model", "kind": "door", "status": "fail", "failed": ["P4"], "waived": [], "unverified": ["P5:map bounds"],
 "intent": {"kind": "door", "face": {"target": [10, 3.5, 20]}}, "intentSource": "argument", "datamodel": "Edit", "at": "2026-11-04T10:00:00Z",
 "fixesApplied": [{"action": "snapToGround", "dy": -0.3}], "passes": 2,
 "checks": {"P1": {"status": "pass", "measured": {"size": [4, 7, 0.5]}, "tolerance": {"originRadius": 0.5}, "issues": [], "fixes": []},
            "P4": {"status": "fail", "measured": {"facingOffDeg": 180, "yawDeg": 0}, "tolerance": {"faceTolDeg": 15}, "issues": ["front faces 180.0 deg away from the target (tolerance 15)"],
                   "fixes": [{"action": "rotateYaw", "deltaDeg": 180}]}}}
```
Scan: `{"kind": "placement-scan", "version": 1, "game", "scorer", "datamodel", "captured_at", "root", "models_total", "summary": {pass, fail, waived}, "skipped": [{path, reason}], "fingerprint", "models": [...]}`.

## Running it
- **Studio MCP** (`rbx-studio`): `execute_luau` with the text of `placement_run.luau` and `CONFIG.mode` = "scan" | "verify" | "place" (datamodel Edit for the built map; Server during a playtest for models spawned at runtime). The tool output contains the `PLACEMENT_*` lines. Save them to a file and run `python placement_gate.py ingest <file> --game <slug> --scorer builder --write Games/<slug>`; for a single placement `python placement_gate.py log <file> --write Games/<slug>`.
- **Rojo project**: copy `Placement.luau` into `src/shared/` and call it from a dev-only script or the command bar. Everything that needs the engine runs inside Studio; the files give no placement evidence by themselves.
- **No Studio and no way to run Luau**: the gate is `skipped` (it cannot pass). Say `playable prototype, placement not verified` and list which models were never measured.
- Models created at runtime by scripts (spawners, procedural maps, generated levels): run the scan in the Server datamodel after generation, or verify the generator by its output positions with `Placement.verify` on a sample.

## Limits (state them in the report)
Ray casts and `GetPartBoundsInBox` see collidable, queryable parts only; MeshParts use their bounding box; terrain is measured on the 4 stud voxel grid (`terrainFill`); CanQuery=false parts and decorative `CanCollide=false` parts do not count as ground or as obstacles; the checks cannot know design intent beyond the intent table (a door on the wrong wall that faces the right way passes). The logic of P1-P7 is tested without Studio (Lune + Python fixtures) and the Instance glue against a mock world; the engine calls are only exercised in live Studio.

## Runner CONFIG (placement_run.luau)
`mode` scan | verify | place; `game`; `scorer` builder | critic; `root` (scan, default Workspace); `paths` (verify); `build` (place, returns `{ { model, intent } }`); `opts` (includeInputs, core tolerance and bounds overrides, intents, rules, defaultIntent; see intent.md).
