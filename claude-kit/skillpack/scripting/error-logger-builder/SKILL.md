---
name: error-logger-builder
description: "Add one error logger that wraps handlers and risky calls in protected calls, records message plus stack trace, throttles repeats so a hot-loop bug cannot flood output or an analytics budget, keeps a ring buffer for admin commands, and can forward entries to the kit's Analytics. Use when errors vanish into Output or one bug spams thousands of lines."
category: scripting
tags: error, logging, pcall, xpcall, traceback, throttle, telemetry, crash, report, analytics, handler
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/analytics-metrics.md
related: retry-wrapper-builder, lune-unit-test-writer, remote-guard-builder, lag-hunter, roblox-datastore-safe-save, kit-system-integrator
---

# error-logger-builder

An unhandled error in an event handler prints once and that handler's run is lost; in a loop it can print thousands of times. A single logger gives errors a name, a trace and a rate limit, and a place to read them later. It reports; it does not fix, and it never swallows an error you needed to act on.

## When to use
Remote handlers, event callbacks and loops that must not die silently, or when live servers show errors you cannot reproduce. Not for: replacing validation (a handler should reject bad input, not catch the exception), or secrets handling (never log tokens or keys).

## Inputs (max 2)
1. Where errors should go (default: `warn` plus a ring buffer; optional sink to the kit Analytics system). 2. Throttle window (default 10 s per identical message).

## Procedure
1. Create the logger once per side: `local log = ErrorLog.new({ sink = function(entry) analytics:LogError(entry) end })` (omit `sink` to keep it local; `clock`, `window`, `capacity`, `print` are options).
2. Wrap handlers: `remote.OnServerEvent:Connect(log:Wrap("Buy", handler))`. For calls that return a value: `local ok, result = log:Try("LoadProfile", function() return store:GetAsync(key) end)`. Failures are reported with message and traceback and return `false, nil`; success returns `true, value`.
3. Report by hand where you catch something yourself: `log:Report("Name", message, trace)`.
4. Throttling is by name plus message inside the window: repeats are counted, not printed, and the next report after the window shows `(+N repeats)`. So a bug in a Heartbeat loop produces a handful of lines and a number.
5. A broken sink never breaks the game: sink errors are swallowed. Keep sinks cheap, do not make an HTTP request per entry, and keep within your analytics event budget (the kit Analytics system batches).
6. Messages carry error text and trace only. Do not put player data, tokens or keys into `error()` strings.
7. Expose `log:Recent()` and `log:Stats()` through an admin command (the kit Admin system) for live debugging; the buffer holds the last 50 entries by default.
8. Use it with retries: transient failures belong to `retry-wrapper-builder` (it returns the final error; log that one). Do not log every retry attempt.
9. Test: `lune run ../skillpack/scripting/error-logger-builder/scripts/tests/ErrorLog.test.luau` from the kit `systems` folder.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `OnServerEvent:Connect|task.spawn|pcall` -> `multi_edit` wrappers -> `start_stop_play` -> `execute_luau` (Server) throwing a test error in a wrapped handler 20 times -> `get_console_output` shows one line plus repeats count.

## Fallback
Files plus Lune tests; delivery to a real analytics backend and the trace format inside Studio versus live servers are `untested` here.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: handle errors defensively with guards and catch blocks; retry 429 with backoff; read the error text first (the vault notes it has no coverage of crash reporting or telemetry dashboards, so the sink design is this skill's own). `Roblox/roblox-kb/scripting-and-performance.md`: protect yields with pcall, xpcall and timeouts; fix leaks. `Roblox/roblox-kb/analytics-metrics.md`: event budgets for custom analytics (live-check the current limits).

## Output
`ErrorLog.luau`, the list of wrapped entry points, the sink choice, the test line.

## Acceptance checks
- [ ] Executed: Lune test quoted (`7 passed, 0 failed`).
- [ ] Twenty identical failures print once with a repeat count (play test, or marked untested).
- [ ] Entries contain message and trace, never secrets or player data.
- [ ] A throwing sink does not break reporting (tested).
- [ ] Every remote handler is wrapped or documented as exempt.

## Pitfalls
Wrapping so broadly that real bugs are hidden (log, then still fix). Catching an error and continuing with half-updated state (roll back or abort the operation). Using the logger as flow control. Logging inside the hot loop on every tick. Forgetting that `error(table)` has no message string.

## Related
`retry-wrapper-builder`, `lune-unit-test-writer`, `remote-guard-builder`, `lag-hunter`.
