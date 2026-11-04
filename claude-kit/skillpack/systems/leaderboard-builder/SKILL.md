---
name: leaderboard-builder
description: "Build global and per-server leaderboards around OrderedDataStore with a cached top-N read that survives outages, throttled score writes that only fire on improvement, score sanitising and rank lookup. Use for any ranked board; seasonal event design is event-planner."
category: systems
tags: leaderboard, ranking, top players, OrderedDataStore, cache, ttl, score, global, budget, throttle
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: rbx-leaderboard, event-planner, currency-system-builder, datastore-schema-builder, remote-guard-builder, analytics-event-planner
---

# leaderboard-builder

One job: show a ranked board without burning DataStore request budget or trusting the client. `scripts/Leaderboard.luau` is the pure part: a TTL cache that serves the stale page when a fetch fails, a per-user write gate (valid integer, improved, not more often than the gap) and rank lookup. The Roblox calls (`GetSortedAsync`, `SetAsync`) are injected, so they stay in a thin glue script wrapped in `pcall`.

## When to use
Top players by score, wealth, wins, time or any stat; weekly boards. Not for: deciding which events to run (`event-planner`), the installed `rbx-leaderboard` skill for the Roblox-API walkthrough (this skill is the tested logic), in-server scoreboards (a plain table and a UI).

## Inputs (max 2)
1. Stat to rank and its range (default: a single non-negative integer, higher is better). 2. Board scope (default: all-time global top 50, refreshed every 60 s; weekly = new store key per week).

## Procedure
1. Pick the store: one `OrderedDataStore` per board (`Board_<stat>_<period>`); weekly boards put the week number in the name so an old board simply stops being read. Values are integers only.
2. Copy `Leaderboard.luau`; build with `fetch = function(limit) local ok, pages = pcall(function() return store:GetSortedAsync(false, limit):GetCurrentPage() end) if not ok then return nil end return mapToEntries(pages) end`. Return nil on failure so the cache serves the stale page.
3. Reads: UI and in-world boards call `board:top(n)` only; `ttl` of 60 s or more keeps you far below the request budget (live-check current DataStore limits in the official docs). Bigger `n` than ever fetched triggers one refetch.
4. Writes: on the server, when the stat changes, `if board:shouldWrite(userId, score) then pcall(store.SetAsync, store, tostring(userId), board:clean(score)) end`. The gate refuses invalid, equal or lower scores and enforces the gap, so spamming the stat cannot flood the store. Call `board:forget(userId)` on leave.
5. The score comes from server state (the saved stat in PlayerData), never from a remote. Flag impossible jumps in the same place (`Analytics` event) rather than inside the board.
6. Display: names via `Players:GetNameFromUserIdAsync` cached by user id (it yields and can fail: pcall); numbers through `Leaderboard.short`. A player outside the page sees their own rank only if you fetch it separately; `Leaderboard.rank` returns nil for "not in the top N", which is a normal answer.
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/leaderboard-builder/scripts/tests/Leaderboard.test.luau` (quote the "N passed, 0 failed" line); the glue is `untested` until run on a published place with API access (DataStores need it in Studio).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Leaderboard.luau` and the glue script -> `start_stop_play` -> `execute_luau` (Server) to write three test scores through `shouldWrite` and read `board:top(3)` -> `get_console_output` to read the result. DataStore access in Studio needs API access enabled and a published place: `untested` until then.

## Fallback
Files + Lune tests with a fake fetch. Everything that needs a running Studio session (OrderedDataStore calls, display names, a real outage) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/data-persistence.md` (DataStore calls fail and are limited: pcall and retry, do not call per frame), `Roblox/roblox-kb/events-and-seasonal-content.md` (timed leaderboards drive event engagement), `Roblox/roblox-kb/social-features-and-virality.md`, `Roblox/roblox-kb/anti-exploit-and-security.md` (server decides scores). Exact request budgets change: live-check the Creator Docs.

## Output
`Leaderboard.luau`, a glue script, the board config (store name, ttl, gap, limit), `design/leaderboards.md`.

## Acceptance checks
- [ ] `top` fetches at most once per ttl (Leaderboard test 1) and serves a stale page on failure (test 3).
- [ ] Negative, NaN, infinite, huge and non-number scores are refused (test 4).
- [ ] A user is written only when the score improved and the gap has passed (test 5).
- [ ] No remote accepts a score from a client (grep the handlers).
- [ ] Leaderboard Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/leaderboard-builder/scripts/tests/Leaderboard.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Calling `GetSortedAsync` per player per join. Writing every stat change. Storing floats. Showing an all-time board that nobody new can ever enter (add weekly boards). Resolving names for 50 rows on the main thread every refresh. Trusting a client-sent score.

## Related
`event-planner`, `rbx-leaderboard`, `currency-system-builder`, `datastore-schema-builder`.
