---
name: data-loss-simulator
description: "Replay DataStore outages, throttling, server crashes, stale locks and shutdowns against your persistence layer with a fake store and fake clock, and report what data would be lost or corrupted. Use before launch and after any change to saving, loading, session locking or BindToClose."
category: qa
tags: datastore, data loss, outage, throttle, crash, shutdown, bindtoclose, session lock, simulation, persistence, test
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: save-load-tester, datastore-schema-builder, retry-wrapper-builder, join-leave-race-tester, roblox-datastore-safe-save, purchase-flow-tester
---

# data-loss-simulator

You cannot take down the real DataStore, but you can take down a fake one in milliseconds. `scripts/DataLoss.luau` provides a fake store with injectable failures (`failNext`, `failAll`), a fake clock, and eight scenarios that exercise any persistence layer with the kit `PlayerData` interface (`LoadAsync`, `SaveAsync`, `ReleaseAsync`, `ReleaseAll`, `AutosaveDue`). It is tested against the real kit `PlayerData` (all pass) and against a naive saver (it fails the lock and autosave scenarios), which proves the scenarios can fail.

## When to use
Before launch, after touching save/load code, migrating to the kit `PlayerData`, or after a "my progress reset" report. Not for: a live round trip in Studio (`save-load-tester`), schema design (`datastore-schema-builder`), or retry tuning (`retry-wrapper-builder`).

## Inputs (max 2)
1. The persistence module to test (default: the kit's `PlayerData`). 2. The autosave interval and lock timeout in use (default: 120 s and 600 s, the kit defaults).

## Procedure
1. Write a factory `(jobId, store, clock, lostLog) -> pd` that builds your module with `store` as its DataStore, `clock.t` as its `os.time` and `clock.wait` as its `task.wait`, with `spawn` running inline. If your module cannot take injected dependencies, that is finding number one: it cannot be tested or reasoned about; wrap or refactor it (`datastore-schema-builder`).
2. `local results = DataLoss.runAll(factory)` and print `DataLoss.report(results)`. The scenarios: transient load errors recover; a load outage never overwrites saved data; a save outage keeps data in memory and the next save lands; shutdown saves every session within 30 s; shutdown during an outage corrupts nothing and the lock expires; a crash without release lets the next server take over with the last save; an old server cannot overwrite after takeover; progress lost in a crash is bounded by the autosave interval.
3. Read every FAIL as a data-loss path: a failed load that returns template data (overwrites the real save on the next autosave), a save that drops the session on error, a missing lock, `BindToClose` that saves players one by one past 30 s, autosave interval too long.
4. Fix in the persistence layer (return failure and kick instead of continuing with fake data; keep the session after a failed save and retry; save in parallel on shutdown; autosave every 60-120 s), then re-run until all pass.
5. Add your own scenarios by adding the failure to `db` (for example `db.failNext = 30` for sustained throttling) and asserting on the stored row.
6. Throttle realism: the real store rejects over-budget calls; the fake throws the same "added to queue" message, so also confirm saving less often fixes it rather than retrying harder (see `retry-wrapper-builder`).
7. Record the worst-case loss in plain words ("up to 2 minutes of progress on a crash") for the owner.

## Studio MCP path
Not needed for the simulation. For real-engine confirmation: `list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) to call the module's save/release during play, then `get_console_output` for DataStore errors; the place must be published with Studio API access on for real DataStore calls.

## Fallback
`lune run ../skillpack/qa/data-loss-simulator/scripts/tests/DataLoss.test.luau` from `claude-kit/systems` runs the suite against the kit module; use that file as the template for your own factory. Real DataStore latency, budgets and Studio-vs-live differences are `untested`.

## Evidence
`Roblox/roblox-kb/data-persistence.md`: pcall/retry around every DataStore call, save on `PlayerRemoving` and in `BindToClose`, a periodic save loop (about 60 s in production) covers crashes where the leave-save never fires, session locking against two servers, "data store request was added to queue" means saving too often. `Roblox/roblox-kb/testing-debugging-and-qa.md`: test DataStores after publishing with Studio API access, edit saved values to test persistence, handle errors defensively. Fast-moving DataStore limits: live-check the docs.

## Output
```
DATA LOSS SIM <module> <date>: N/8 scenarios passed
  FAIL <scenario>: <detail>
Worst-case loss: <plain words>   Fixes: <list>   Re-run: 8/8
```

## Acceptance checks
- [ ] `lune run` of the DataLoss test prints "4 passed, 0 failed" (kit module 8/8, naive saver fails).
- [ ] The report for your module shows 8/8 or each failure has a fix and a re-run.
- [ ] No scenario passes because it never ran (each prints a detail line).
- [ ] The worst-case loss is stated for the owner.
- [ ] Real-engine behaviour is marked `untested` unless a published test place was used.

## Pitfalls
A factory that shares one store object by accident (hides locking bugs). Fake time that never advances past the lock timeout. Treating a passing simulation as proof against real throttling. Testing only the happy shutdown. Returning template data on load failure.

## Related
`save-load-tester`, `datastore-schema-builder`, `retry-wrapper-builder`, `join-leave-race-tester`, `purchase-flow-tester`.
