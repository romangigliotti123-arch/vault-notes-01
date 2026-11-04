---
name: retry-wrapper-builder
description: "Add a retry helper with exponential backoff, jitter, a waiting budget and a retryable-error test for calls that fail for outside reasons (DataStore, MarketplaceService, HTTP, MemoryStore), without retrying invalid requests or double-wrapping the kit's PlayerData. Use when a network call can throttle or time out and the code currently gives up or loops."
category: scripting
tags: retry, backoff, jitter, pcall, datastore, throttle, http, marketplaceservice, memorystore, transient error
kb: Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: rbx-datastore, datastore-schema-builder, error-logger-builder, lune-unit-test-writer, kit-system-integrator
---

# retry-wrapper-builder

Calls to services outside your server fail sometimes: throttling, timeouts, brief outages. Retrying with a growing delay recovers most of them; retrying blindly makes throttling worse and can overwrite newer data. `scripts/Retry.luau` is the small, tested helper.

## When to use
`MarketplaceService:GetProductInfoAsync`, `HttpService` calls, MemoryStore, extra DataStores, anything yielding that returns an error on failure. Not for: the kit PlayerData system's own loads and saves (it already retries, session-locks and protects the save; wrapping them multiplies attempts and delays shutdown), or errors caused by your own bad input.

## Inputs (max 2)
1. The call and what failure looks like. 2. How long the caller may wait in total (default: the player-visible budget, e.g. 10 s).

## Procedure
1. Decide if the call is safe to repeat. Reads are. Writes are only if repeating gives the same result (set a value, not add to it); otherwise use `UpdateAsync` with idempotent logic and a receipt/id, and treat a failed call as an unknown outcome until you re-read.
2. Call: `local ok, result, tries = Retry.run(function() return market:GetProductInfoAsync(id) end, { attempts = 5, base = 0.5, max = 8, budget = 10, onRetry = function(n, err, delay) end })`. On failure `result` is the last error text.
3. For DataStore calls start from `Retry.DATASTORE` (5 attempts, 2 s base, 32 s max: the vault's official sample, live-check) and merge your overrides.
4. Retry only what can recover: the default test treats throttle codes 301 to 306, `KeyThrottled`, `DatastoreThrottled`, 429, timeouts and 5xx as transient and 4xx, invalid and permission errors as permanent. Provide `retryable = function(err) ... end` when you know your errors better. Unknown messages are retried (classified `unknown`), so supply the test if a retry could cause harm.
5. Jitter spreads retries from many servers so they do not stampede together; keep the default 0.2 unless you have a reason. `budget` stops the loop once the total waiting would exceed the time the player can tolerate.
6. Waiting: the helper uses `task.wait`. Never retry on the main thread of a join path without a budget (a stuck join is worse than a clear error); if the player is present keep retrying only while they stay, then show an error rather than losing data.
7. Failure path: after the final failure, log with `error-logger-builder` (one entry, not one per attempt) and degrade: cached value, default, a clear message. Never grant on failure.
8. Test: `lune run ../skillpack/scripting/retry-wrapper-builder/scripts/tests/Retry.test.luau` from the kit `systems` folder (fake wait and random: delays, cap, jitter band, budget, permanent errors).

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `GetProductInfoAsync|GetAsync|UpdateAsync|RequestAsync` without surrounding pcall -> `multi_edit` -> `start_stop_play` -> `execute_luau` (Server) with a function that fails twice then succeeds -> `get_console_output` for the delays. Real throttling cannot be provoked safely here.

## Fallback
Lune tests with injected wait and random; real service errors and their exact wording are `untested`, which is why `retryable` is overridable.

## Evidence
`Roblox/roblox-kb/data-persistence.md`: wrap every DataStore call in pcall; retry with exponential backoff (official sample 5 attempts, 2 s base, 32 s max; throttle codes 301 to 306, KeyThrottled, DatastoreThrottled, HTTP 429 are retryable); do not retry invalid-request errors; retries process in order per key so an old retry can overwrite a newer write, so treat a failed call as unknown until re-read. `Roblox/roblox-kb/testing-debugging-and-qa.md`: retry 429 with backoff. `Roblox/roblox-kb/scripting-and-performance.md`: protect yields with pcall and timeouts.

## Output
`Retry.luau`, the wrapped call sites with their options, the failure-path behaviour, test line.

## Acceptance checks
- [ ] Executed: Lune test quoted (`8 passed, 0 failed`).
- [ ] Each wrapped call is safe to repeat (stated), or uses an idempotent write.
- [ ] Permanent errors do not retry; the total wait stays within the budget.
- [ ] Failure path degrades without granting or losing data.
- [ ] No PlayerData call is double-wrapped.

## Pitfalls
Retry storms after an outage (no jitter). Retrying a purchase grant. Unbounded `while not ok` loops. Treating `unknown` as retryable for a harmful write. Hiding failures: log the final one. Using fixed `wait(7)` style delays.

## Related
`rbx-datastore`, `datastore-schema-builder`, `error-logger-builder`, `lune-unit-test-writer`.
