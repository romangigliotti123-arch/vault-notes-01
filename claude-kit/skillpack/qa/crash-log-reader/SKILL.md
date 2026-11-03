---
name: crash-log-reader
description: "Read client and server crash evidence (Output and Developer Console logs, memory samples, disconnect and kick lines, Creator Hub error views) into a timeline with a suspect cause: memory pressure, script timeout, DataStore throttling, HTTP failures, kicks or plain disconnects. Use when players report crashes, disconnects or servers shutting down."
category: qa
tags: crash, disconnect, out of memory, server shutdown, developer console, log, memory leak, crash report, timeline, diagnosis
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/all-numbers-and-benchmarks.md
related: output-error-triager, lag-hunter, script-profiler, game-optimizer, data-loss-simulator, load-test-planner
---

# crash-log-reader

A crash report is a pile of lines. This skill turns them into a timeline and a suspect, using `scripts/CrashSignals.luau`: it classifies each line by message text (memory, script timeout, DataStore throttle or error, HTTP error, kick, disconnect, infinite yield, script error), picks the earliest meaningful signal before the disconnect, and checks memory samples for a steady climb. It matches wording, not Roblox error codes: treat the suspect as a lead to confirm on the real device.

## When to use
"The game crashes", "I got disconnected", a server that dies minutes after start, or a spike in the Creator Hub crash/error views. Not for: ranking ordinary script errors (`output-error-triager`), network lag (`lag-hunter`), or profiling a slow script (`script-profiler`).

## Inputs (max 2)
1. The evidence: pasted log lines (server and client separately), the device and session length, memory readings if any (default: ask for both sides' logs). 2. When it happens (join, after N minutes, during an event, on teleport).

## Procedure
1. Split the evidence by side. A client crash is judged from the CLIENT log and device memory; a server shutdown from the SERVER log. Stop if only one side is available and say so.
2. Run `CrashSignals.summarize(lines)`; read `timeline` (first occurrence per category with line number), `counts`, `suspect` and `why`. Signals after the first disconnect/kick are consequences, not causes.
3. Memory: if samples exist (`collectgarbage("count")`/Stats memory every 30-60 s, or F9 readings), `CrashSignals.memoryTrend(samples)` gives MB per minute and whether it is a steady climb. Short Studio tests miss growth that crashes live players, so test long sessions (vault). A leak shows as instance counts that never stabilise: print `#folder:GetChildren()` on spawn folders.
4. By suspect: `memory` -> real low-end device with F9 memory open, lower texture/mesh/instance counts, streaming, fix leaks (disconnected connections, uncleaned instances, caches); `script-timeout` -> find the loop without a yield (`script-profiler`); `datastore-throttle` -> save less often, batch, back off (`retry-wrapper-builder`); `http-error` -> allowed domains, status handling, back-off; `kicked` -> find the Kick call and what flagged them (`honeypot-remote-builder`); `disconnect` with no earlier cause -> look at the other side's log and time of day.
5. Reproduce: apply the described conditions on a device or in a long Studio session; one change at a time. Remove breakpoints before measuring.
6. Verify the fix by repeating the same session length and watching the same signal (memory slope, no throttle lines); report before/after.
7. If the log is empty of signals, say the evidence is insufficient and list what to collect (both logs, device model, time, session length, Developer Console screenshots).

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) sampling memory/instance counts on an interval -> `get_console_output` for the lines to feed `summarize` -> `screen_capture` of the Developer Console (F9) if needed -> `start_stop_play` (stop). Studio is not a phone: absolute memory needs a device.

## Fallback
Pasted text only: `lune run ../skillpack/qa/crash-log-reader/scripts/tests/CrashSignals.test.luau` from `claude-kit/systems` shows the classifier on samples; run it on the pasted lines in a scratch Lune file. Anything about specific devices is `untested`.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: most crashes are out-of-memory; warning thresholds rise near about 66 percent of device memory (roughly 1.3 GB on a 2 GB device, about 1.4 GB crash), check F9 on the real device, prefer memory over speed; a server that crashes within minutes of startup suggests a memory problem (indie-sourced numbers, live-check). `Roblox/roblox-kb/testing-debugging-and-qa.md`: open the Developer Console (F9), play longer sessions while watching memory, compare heap snapshots over time, count instances to catch leaks. `Roblox/roblox-kb/data-persistence.md`: "request was added to queue" means saving too often; throttle codes are back-off-and-retry.

## Output
```
CRASH READ <game> <date>: side server|client, lines N
suspect: <category>   why: <one line>   memory slope: X MB/min (leak: yes/no)
timeline: line | category | text
next step: <what to collect or change>
```

## Acceptance checks
- [ ] `lune run` of the CrashSignals test prints "6 passed, 0 failed".
- [ ] The suspect rests on a signal that appears BEFORE the disconnect line (line numbers quoted).
- [ ] Client and server logs were read separately, or the missing side is named.
- [ ] Memory conclusions come from at least 3 samples over time, not one reading.
- [ ] A fix claim is backed by a repeat of the same session (or marked untested).

## Pitfalls
Blaming the last error line. Treating a datastore warning as the crash cause when memory climbed first. One memory reading. Testing on a dev PC. Merging client and server logs. Assuming a kick is a crash.

## Related
`output-error-triager`, `lag-hunter`, `script-profiler`, `game-optimizer`, `data-loss-simulator`, `load-test-planner`.
