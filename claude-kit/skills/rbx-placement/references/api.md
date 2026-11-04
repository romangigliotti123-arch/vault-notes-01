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

Per-model report: `path`, `kind`, `status`, `failed`, `waived`, `unverified`, `intent`, `fixesApplied`, `passes`, `checks.Pn` = `{status, measured, tolerance, issues, fixes}`. Scan file: `kind placement-scan`, `models_total`, `summary {pass, fail, waived}`, `skipped`, `fingerprint`, `models`. [cold:rbx-placement/report-shape.md] read only to see the full JSON shape of a per-model report or a scan file.

## Running it
- **Studio MCP** (`rbx-studio`): `execute_luau` with the text of `placement_run.luau` and `CONFIG.mode` = "scan" | "verify" | "place" (datamodel Edit for the built map; Server during a playtest for models spawned at runtime). The tool output contains the `PLACEMENT_*` lines. Save them to a file and run `python placement_gate.py ingest <file> --game <slug> --scorer builder --write Games/<slug>`; for a single placement `python placement_gate.py log <file> --write Games/<slug>`.
- **Rojo project**: copy `Placement.luau` into `src/shared/`, call it from a dev-only script or the command bar. Only a run inside Studio is placement evidence.
- **No Studio and no way to run Luau**: the gate is `skipped` (cannot pass). Say `playable prototype, placement not verified` and list the models never measured.
- Models created at runtime (spawners, procedural maps, generated levels): scan in the Server datamodel after generation, or `Placement.verify` a sample of the generator's output positions.

## Limits (state them in the report)
Ray casts and `GetPartBoundsInBox` see collidable, queryable parts only; MeshParts use their bounding box; terrain is measured on the 4 stud voxel grid (`terrainFill`); CanQuery=false and decorative `CanCollide=false` parts are not ground or obstacles; design intent beyond the intent table is unknown (a door on the wrong wall that faces the right way passes). P1-P7 logic is tested without Studio (Lune + Python fixtures), the Instance glue against a mock world; engine calls only in live Studio.

## Runner CONFIG (placement_run.luau)
`mode` scan | verify | place; `game`; `scorer` builder | critic; `root` (scan, default Workspace); `paths` (verify); `build` (place, returns `{ { model, intent } }`); `opts` (includeInputs, core tolerance and bounds overrides, intents, rules, defaultIntent; see intent.md).
