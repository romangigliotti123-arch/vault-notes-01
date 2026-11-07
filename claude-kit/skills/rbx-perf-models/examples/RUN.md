# rbx-perf-models: a real run (synthetic fixture game)

What this is: the skill run end to end on `Fixture-Obby`, a synthetic game built inside Lune's Roblox DOM by `scripts/tests/fixture_run.luau` (34 parts: scenery, a hidden block, invisible leftovers, duplicates, a kill brick, a ladder, a vehicle seat, an NPC, a scripted door, a tagged gem, a welded wheel, a crate, 2 scripts). The Luau runner and the Python analyzer are the shipped files; only the engine is Lune instead of Studio. A run inside a real Studio place is the first thing to do on your own game.

## 1. Scan (read only)
`perf_run.luau` via `execute_luau` (or pasted in the command bar). Output saved to `Games/Fixture-Obby/perf-qa/scan-before.txt` (6 lines). Header line:
```
PERF_SCAN {"bulkTouch":false,"capped":false,"capturedAt":"2026-11-07T13:55:17Z","counts":{"beams":0,"decals":1,"distinctMeshIds":0,"emitterRate":0,"emitters":0,"fx":0,"lights":1,"lightsShadow":0,"mesh ...
PERF: scan done (42 nodes). Next: python perf_gate.py analyze <this output saved as a text file> --game <name>
```

## 2. Dry run
```
$ bash .rbx/claude-kit/tools/pyrun .rbx/claude-kit/skills/rbx-perf-models/scripts/perf_gate.py analyze Games/Fixture-Obby/perf-qa/scan-before.txt --game Fixture-Obby --write Games/Fixture-Obby
WROTE perf-qa/scan-before.json
WROTE perf-qa/plan.json
WROTE perf-qa/report.md
WROTE perf-qa/perf_apply.luau
WROTE perf-qa/perf_revert.luau
PERF ANALYSIS (dry run): 34 parts | SAFE: 30 changes/removals planned | REVIEW suggestions: 6 (approved: 0)
ESTIMATE physics cost units 50.0 -> 36.2 (28%), collision memory units 34.0 -> 30.0 (12%)
Undo in one step: press Ctrl+Z in Studio (Edit > Undo 'PerfPass: applied'), or run perf_revert.luau from the same folder.
```
The full report is `examples/report.md`. The plan behind it (SAFE tier only, nothing approved):
- S2 CanQuery True -> False: 9 parts (Core, Fern, LampGlow, Pebble)
- S3 CanTouch True -> False: 16 parts (Core, Edge, Fern, InvisibleWall, LampGlow, Pane)
- S4 CanCollide True -> False: 1 parts (Core)
- S5 Remove None -> None: 2 parts (Stray)
- S6 Remove None -> None: 2 parts (Plank)

Never touched at all: KillBrick, Lava, Waypoint (named in a script), RopeRail (ladder), Hood and Chassis (vehicle), Hand (NPC), Leaf (scripted door), Gem (tagged), Beacon (attribute), Axle and Disc (welded), Crate (movable). Collidable scenery (Wall, Slab, Edge, InvisibleWall, the two Panes) only loses CanTouch: its collision stays, InvisibleWall is invisible but collidable so it is not a leftover, the Panes are translucent so they are not opaque duplicates, and Edge touches the block surface so it is not hidden inside it.

## 3. User says yes: apply and check (Luau output of perf_apply.luau)
```
APPEARANCE Part PASS (28 checked, 0 differ)
APPEARANCE TrussPart PASS (1 checked, 0 differ)
APPEARANCE VehicleSeat PASS (1 checked, 0 differ)
APPEARANCE DIFF PASS: no rendering property of any surviving part changed
PERF_APPLY {"applied":30,"differ":0,"skipped":{},"status":"APPLIED"}
```
Independent check by the Python diff of the whole before/after state:
```
$ perf_gate.py verify perf-qa/scan-before.json perf-qa/apply-1.txt --plan perf-qa/plan.json --write Games/Fixture-Obby
APPEARANCE Part PASS (32 checked, 0 differ)
APPEARANCE TrussPart PASS (1 checked, 0 differ)
APPEARANCE VehicleSeat PASS (1 checked, 0 differ)
APPEARANCE DIFF: PASS
WROTE Games/Fixture-Obby/perf-qa/appearance-diff.json
WROTE Games/Fixture-Obby/perf-qa/scan-after.json
runner reported: {"applied": 30, "differ": 0, "skipped": {}, "status": "APPLIED"}
```
(the Luau count is lower than the Python one because the 4 removed parts are checked only in Python: invisible, or an identical twin remains.)

## 4. The same apply with a deliberately wrong change injected (a pebble tinted red after the edits)
```
APPEARANCE Part FAIL (28 checked, 1 differ)
APPEARANCE TrussPart PASS (1 checked, 0 differ)
APPEARANCE VehicleSeat PASS (1 checked, 0 differ)
APPEARANCE DIFF FAIL: 1 part(s) differ, everything was put back
PERF_APPLY {"applied":0,"differ":1,"skipped":{},"status":"REVERTED"}
```
```
$ perf_gate.py verify ... (exit code 1)
APPEARANCE Part FAIL (32 checked, 1 differ)
APPEARANCE TrussPart PASS (1 checked, 0 differ)
APPEARANCE VehicleSeat PASS (1 checked, 0 differ)
  FAIL part 21 (Pebble2): col '788C5A' -> 'FF0000'
  warn the runner reverted all of its edits (REVERTED): the planned changes are not in the game
APPEARANCE DIFF: FAIL
runner reported: {"applied": 0, "differ": 1, "skipped": {}, "status": "REVERTED"}
```
The runner put its own changes back (`applied: 0`, `REVERTED`); the verify step still names the tinted part because the injected change was not one of the runner's edits.

## 5. Undo
`Ctrl+Z` in Studio, or `perf-qa/perf_revert.luau` (restores the old flags and brings the removed parts back from ServerStorage.PerfPass_Removed). Run after the apply in the same fixture, then a fresh scan equals the original scan part for part:
```
PERF_REVERT {"restoredParts":4,"restoredValues":26,"skippedByGuard":0,"status":"OK"}
```
