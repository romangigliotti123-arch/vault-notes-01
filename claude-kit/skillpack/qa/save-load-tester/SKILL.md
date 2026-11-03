---
name: save-load-tester
description: "Test the real save and load round trip in a Studio test place: write a probe value, save, stop, start again and read it back; then test leave, rejoin, schema migration and shutdown paths. Use after changing player data code, the schema, or adding a new saved field, to prove it persists."
category: qa
tags: save, load, datastore, round trip, persistence, rejoin, migration, studio api access, player data, test place
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: data-loss-simulator, datastore-schema-builder, retry-wrapper-builder, join-leave-race-tester, playtest-bot-writer, purchase-flow-tester
---

# save-load-tester

`data-loss-simulator` proves the persistence logic survives failure with fakes; this skill proves the real thing works in the real engine: a value written in one session is there in the next. `scripts/save_roundtrip.luau` is a two-phase probe for the kit's `PlayerDataService` (`WaitFor`, `SaveNow`); the rest is a checklist of save, leave, rejoin, migrate and shutdown paths using Studio MCP. It runs in a TEST place only.

## When to use
After a new saved field, a schema/migration change, a data module swap, or a "my progress is gone" report. Not for: failure injection (`data-loss-simulator`), schema design (`datastore-schema-builder`), or purchases (`purchase-flow-tester`).

## Inputs (max 2)
1. The data module and the field to test (default: kit `PlayerDataService`, field `qaProbe`). 2. Whether the place is published with Studio API access on (default: ask; DataStore calls in Studio need both).

## Procedure
1. Preconditions: a published TEST place (not the live one), Game Settings > Security > "Enable Studio Access to API Services" on, and a test account. Publish first, then enable access (vault, 2026 guidance). Stop and report if you cannot confirm it.
2. Phase write: set `PHASE = "write"` in `scripts/save_roundtrip.luau` and run it with `execute_luau` (Server) during a playtest started with Test (not Run: Run inserts no avatar). Expect `PASS wrote qaProbe=probe-1 ...`. Stop the playtest.
3. Phase read: set `PHASE = "read"`, start a new playtest, run again. Expect `PASS qaProbe survived the round trip`. A FAIL means the value did not persist: check Output for DataStore errors and that the leave-save ran.
4. Leave path: change a value, stop the playtest through the normal leave (not a crash), start again, read it. This tests `PlayerRemoving` and `BindToClose` saves together.
5. New field and migration: add the field to the template, bump the version with a migration if the shape changed (`datastore-schema-builder`), load an OLD record (save one before the change) and confirm the field is added and old values are intact. Plugins that edit saved values let you create the old state quickly (vault).
6. Shutdown path: with 2+ test clients, stop the server and read both players' data next session; saving must finish within the shutdown window.
7. Clean up: reset the probe field, and never run this against the live game's DataStore. Record results with Output excerpts.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `start_stop_play` (Test) -> `execute_luau` (Server) with the probe (phase write) -> `get_console_output` -> `start_stop_play` (stop) -> repeat with phase read -> `get_console_output`.

## Fallback
No Studio or API access: run `lune run ../skillpack/qa/data-loss-simulator/scripts/tests/DataLoss.test.luau` from `claude-kit/systems` for the logic, and give the owner the two-phase procedure to run by hand. Round-trip and real shutdown behaviour are `untested`.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: test DataStores after publishing with Studio API access enabled; edit saved player values in a plugin to test persistence; use Test not Run when you need an avatar; verify on the published live page when behaviour differs (pickups, purchases). `Roblox/roblox-kb/data-persistence.md`: save on `PlayerRemoving` and `BindToClose`, periodic save loop, session locking; migrate schema versions in order. Launch gate: `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`.

## Output
```
SAVE/LOAD TEST <place> <date>: write PASS|FAIL, read PASS|FAIL, leave PASS|FAIL, migration PASS|FAIL, shutdown PASS|FAIL
Output excerpts per failure   Preconditions confirmed: published yes/no, API access yes/no
```

## Acceptance checks
- [ ] Phase write printed `PASS wrote ...` and phase read printed `PASS ... survived the round trip` (both quoted).
- [ ] The test ran in a test place with a test account, never the live game.
- [ ] An old-format record was loaded after a schema change, or the change is marked untested.
- [ ] The leave path (not just `SaveNow`) was exercised.
- [ ] The probe field was cleaned up.

## Pitfalls
Studio API access off (saves silently fail or error). Testing in an unpublished place. Using Run instead of Test. Reading the value in the same session (it proves nothing). Testing `SaveNow` only and never the leave path. Running against live data.

## Related
`data-loss-simulator`, `datastore-schema-builder`, `retry-wrapper-builder`, `join-leave-race-tester`, `playtest-bot-writer`.
