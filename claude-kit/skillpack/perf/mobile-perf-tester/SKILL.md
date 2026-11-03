---
name: mobile-perf-tester
description: "Run a 10-15 minute on-device session on a real low-end phone, log frame time and memory each second, and analyse average, p95, spikes, thermal decline and memory growth against a frame budget. Use before launch, after every big update, or when mobile players report lag, heat or crashes that Studio never shows."
category: perf
tags: mobile, android, low-end, thermal, frame time, memory, device testing, performance stats, crash, 30 fps
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/scripting-and-performance.md
related: game-optimizer, memory-budget-planner, cpu-vs-gpu-diagnoser, mobile-ui-audit, join-time-reducer, instance-leak-finder
---

# mobile-perf-tester

Studio and the device emulator miss memory pressure, thermal throttling and touch latency. This skill produces the one thing they cannot: a session log from a real phone, analysed for the failures that only appear after ten minutes.

## When to use
Pre-launch gate, after any update that adds content, mobile complaints, or a crash spike on low-memory devices. Not for: touch-target and layout review (`mobile-ui-audit`), picking budgets (`memory-budget-planner`) or deciding what is slow (`cpu-vs-gpu-diagnoser`).

## Inputs (max 2)
1. Which real device (default: a budget Android phone with 2-4 GB RAM; the docs say Android is about 65 percent of a typical game's players and most Android devices have 2-4 GB). 2. Frame goal: 30 FPS (33.33 ms, default for phones) or 60 FPS (16.67 ms).

## Procedure
1. Prepare: publish a private/test version; add `scripts/mobile_sampler.luau` as a LocalScript in StarterPlayerScripts (12-minute default, inside the docs' 10-15 minute thermal window). Enable Roblox's Performance Stats overlay on the device for a visual cross-check.
2. Play normally for the whole session, covering the worst scenario (busiest area, effects on, full server if possible). Do not stop to observe; the point is sustained load. Stop if the app is killed: that is a result (out-of-memory), record the elapsed time and last memory reading.
3. Collect the log: the sampler prints `[mobile] t,frameMs,memMB,worstFrameMs` per second to the client log (Developer Console F9 > Client Log, or the logs pulled from the device). Convert lines to `{t=, frameMs=, memMB=}` and run `MobileSession.analyze(samples, 33.33)` from `scripts/MobileSession.luau`.
4. Read the report: avg and p95 frame ms, worst frame, share over budget, spikes (frames over twice the budget), `thermalDeclinePct` (late third versus early third; flagged above 25 percent, a heuristic), memory start/end and growth per minute (flagged above 1 MB/min), and the flags list. A short session (under 10 minutes) cannot show thermal throttling: say so.
5. Act on the flags: thermal decline means sustained GPU/CPU load in hot paths (`render-cost-auditor`, `script-profiler`); memory growth means a leak (`instance-leak-finder`); high steady memory means budget work (`memory-budget-planner`); frame time high from the start means `cpu-vs-gpu-diagnoser`.
6. Repeat on the same device with the same route after fixes and compare the two reports. Keep the baseline device and route written down so releases stay comparable.

## Studio MCP path
Studio MCP cannot reach a phone. Use it only to add or remove the sampler (`execute_luau` Edit to create the LocalScript) and to validate the analysis code with sample data. The device session and log retrieval are the owner's; report them `untested` until a log is supplied.

## Fallback
No sampler: read the Performance Stats overlay every minute and note FPS, memory and ping by hand (coarse). Analysis can then be done with `MobileSession` using one sample per minute (flags that need per-second data will be weak; say so). Rojo: add the script as a file.

## Evidence
Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization test-on-hardware.md` (real devices over emulation; 10-15 minute session for thermal throttling; Android about 65 percent; RAM mix about 60 percent 2-4 GB; Performance Stats overlay; dashboard crash spike suggests a low-end memory regression). `Roblox/roblox-kb/optimization-and-streaming.md`: judge spikes and consistency, not the average; frame budgets 16.67 and 33.33 ms; a 133 ms mobile frame is easy to notice; do not trust Studio memory. `Roblox/roblox-kb/scripting-and-performance.md`: a 10 ms PC frame can be about 40 ms on a low-end phone (creator report). The 25 percent thermal flag and 2x spike rule are this skill's heuristics.

## Output
```
MOBILE SESSION <build> <device> <date> (12.0 min, 721 samples)
avg 27.4 ms | p95 41 ms | worst 210 ms | over 33 ms: 18% | spikes 9 | thermal +31% (flag)
memory 410 -> 690 MB (+23 MB/min, flag leak) | flags: thermal-decline, memory-growth
Next: instance-leak-finder on the shop scene; render-cost-auditor (sustained GPU)
```

## Acceptance checks
- [ ] The session ran at least 10 minutes on a named physical device, or the report states it is short.
- [ ] Raw samples are saved; the report quotes `MobileSession` output.
- [ ] Every flag has a named follow-up skill or a reason to ignore it.
- [ ] A repeat run after fixes uses the same device and route.
- [ ] Executed check: `MobileSession.test.luau` passes under Lune; `mobile_sampler.luau` passes luau-check.

## Pitfalls
Using the emulator or a flagship phone. Testing a quiet room instead of the worst scenario. Judging by average FPS alone. Leaving the sampler in the shipping game. Comparing sessions with different routes. Charging a device during the test (hides thermals).

## Related
`game-optimizer`, `memory-budget-planner`, `cpu-vs-gpu-diagnoser`, `mobile-ui-audit`, `instance-leak-finder`.
