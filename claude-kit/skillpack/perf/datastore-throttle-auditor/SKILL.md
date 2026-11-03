---
name: datastore-throttle-auditor
description: "Find DataStore and MemoryStore request bursts that exhaust the per-minute budgets or queue limits: compute the documented budgets for your CCU, tally requests per call site, set a safe autosave interval, and remove join/leave/shutdown spikes. Use when logs show throttling warnings, data saves fail, or before scaling player count."
category: perf
tags: datastore, throttle, budget, request limit, autosave, memorystore, queue, bindtoclose, rate limit, saves
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/analytics-metrics.md
related: datastore-schema-builder, game-optimizer, server-tick-analyzer, lag-hunter, network-traffic-auditor
---

# datastore-throttle-auditor

Data requests are a budget like any other: a fixed number per minute that grows with concurrent players. Most throttling comes from a few bursty call sites (autosave on a timer for everyone, loops on join, shutdown storms), so the fix is to count them, size the interval from the formula, and spread the load.

## When to use
Output shows "request was throttled" or queue-full warnings, players lose progress during busy periods, a new feature reads or writes per player per action, or you plan a CCU jump. Not for: designing the data shape (`datastore-schema-builder`), session locking, or non-data network volume (`network-traffic-auditor`).

## Inputs (max 2)
1. Peak CCU and players per server (default: read MaxPlayers; use the dashboard for CCU). 2. Which stores are used (default: grep all `GetDataStore|GetOrderedDataStore|MemoryStoreService`).

## Procedure
1. Inventory call sites: `script_grep` for `GetAsync|SetAsync|UpdateAsync|IncrementAsync|RemoveAsync|GetSortedAsync|ListKeysAsync|MemoryStoreService`. For each, note the trigger (join, leave, timer, action, BindToClose), the per-player frequency, and the key.
2. Compute budgets with `scripts/DataStoreBudget.luau`: `experienceBudget(ccu)` gives the per-minute budgets (read 300 + CCU x 40, write 300 + CCU x 20, list 300 + CCU x 2, ordered write 300 + CCU x 20) and `serverBudget(players)` the per-server defaults (read/write 60 + players x 40, ordered write 30 + players x 5). Live-check these numbers in the Creator Docs: they change.
3. Estimate load: per-minute reads and writes = sum over call sites (players x frequency). `utilisation({reads=, writes=}, ccu)` then `worst()` names the metric nearest its limit and gives ok (<=60 percent, a heuristic that leaves headroom for bursts), warn or over. Stop here if every metric is ok and no throttling appears in logs.
4. Fix bursts, largest first:
   a. Autosave: one write per player per interval with `minSaveInterval(players)` as the floor (it keeps steady-state use to 50 percent of the server write budget); add random jitter per player so saves do not align; save on change flags only (dirty bit).
   b. Join/leave: cache the loaded data in memory, one read at join, one write at leave; never read per action. Do not poll DataStores to sync state across servers; use MessagingService/MemoryStore for transient data.
   c. Shutdown (`BindToClose`): save all players in parallel with `task.spawn`, but within the shutdown window; skip players saved in the last few seconds.
   d. Per-key limits: one key takes up to 4 MB/min of writes and 25 MB/min of reads, rounded up to the next KB per request; `maxWritesPerMinutePerKey(valueBytes)` tells you the cap; shard hot keys; keep values lean (limit 4,194,304 characters serialized).
   e. Wrap calls in pcall with retry and backoff; respect the queue limit (30 requests per queue type); stagger retries.
5. Verify: run a stress session (many bots or Studio multi-client), watch the console for throttle warnings, and compare the Data Stores observability charts per minute before and after.
6. Write the guard: the formula table with your CCU, the interval constants and the check to rerun when adding any data call.

## Studio MCP path
`script_grep` (call sites) -> `script_read` the saving modules -> `multi_edit` interval/jitter/dirty-flag changes -> `start_stop_play` -> `get_console_output` for throttle warnings. Real throttling needs live servers: the stress run in Studio uses mock or Studio data and does not prove production limits (`untested`).

## Fallback
Without Studio: do the paper audit and run `DataStoreBudget` under Lune with the numbers; use the Creator Hub Data Stores observability charts for live per-minute counts. Mark production behaviour `untested`.

## Evidence
Official (vault notes): `Roblox/docs/Videos/2026-10-28 - Docs cloud-services data-stores error-codes-and-limits.md` (budget formulas, per-key throughput 4 MB/min write and 25 MB/min read, value limit, queue limit 30), `Roblox/docs/Videos/2026-10-28 - Docs cloud-services data-stores best-practices.md`, `Roblox/docs/Videos/2026-10-28 - Docs cloud-services data-stores observability.md`, `Roblox/docs/Videos/2026-10-28 - Docs cloud-services memory-stores best-practices.md`. `Roblox/roblox-kb/optimization-and-streaming.md`: reduce requests, item sizes and expirations before adding capacity; shard; stagger and retry. `Roblox/roblox-kb/data-persistence.md` for safe patterns. The 60 percent warn line and 50 percent autosave share are heuristics.

## Output
```
DATASTORE AUDIT <game> <date>  CCU 2,000, 30 players/server
Budgets/min: read 80,300 | write 40,300 | per server rw 1,260
Load/min: reads 31,000 (39%) | writes 52,000 (129% OVER) <- autosave every 60 s, all servers aligned
Fix: interval 120 s + jitter, dirty flag -> writes 14,000 (35%). Per-key hot spot: Leaderboard key 3 KB x 120/min = ok
```

## Acceptance checks
- [ ] Every call site has a trigger and frequency; no store is unlisted.
- [ ] Budgets are computed from the stated CCU and marked live-check.
- [ ] The autosave interval is >= `minSaveInterval(players)` with jitter.
- [ ] BindToClose saves in parallel and skips recently saved players.
- [ ] Executed check: `DataStoreBudget.test.luau` passes under Lune; scripts pass luau-check.
- [ ] The alert and the action trigger at 70 percent of a DataStore or Memory Store quota, not at the critical overage (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, analytics-metrics).

## Pitfalls
Autosaving every player every 30 seconds by default. Reading on every action instead of caching. Using SetAsync where UpdateAsync is needed (data loss races). Ignoring the ordered-store budgets. Treating Studio as proof of production throttling. Forgetting that joins in a burst (events, front-page spikes) multiply reads.

## Related
`datastore-schema-builder`, `game-optimizer`, `server-tick-analyzer`, `lag-hunter`, `network-traffic-auditor`.
