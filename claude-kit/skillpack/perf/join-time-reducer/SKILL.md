---
name: join-time-reducer
description: "Time a cold join to first playable on a real device with milestone marks, find the long pole and any blocking third-party call, then cut it with streaming, deferral, preloading rules and a loading screen, comparing every run with the last. Use when players wait too long to start, after a content update, or before launch."
category: perf
tags: join time, load time, first playable, loading, preload, ContentProvider, ReplicatedFirst, streaming, deferral, analytics outage
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: game-optimizer, streaming-enabler, loading-screen-builder, first-minute-designer, mobile-perf-tester, replicated-loader-builder
---

# join-time-reducer

Join time decides whether the first-minute funnel even starts. This skill records milestone timestamps on a real device, names the single longest phase, and removes blocking work from the critical path, one change per run.

## When to use
"Loading takes forever", a join-time regression after an update, adding third-party services (analytics, ads, HTTP) to the join path, or a launch checklist. Not for: designing the loading screen's look (`loading-screen-builder`) or the first gameplay minute (`first-minute-designer`).

## Inputs (max 2)
1. The baseline device (default: low-end Android phone on average Wi-Fi). 2. A time budget in seconds you want to hold (the vault gives none: default to your own baseline run and require no regression above 10 percent, a heuristic).

## Procedure
1. Add `scripts/join_marks.luau` to StarterPlayerScripts for the test (remove it after). It prints a mark for client start, game loaded, character spawned, character root ready, PlayerGui ready and first ScreenGui, plus any `JoinMark` BindableEvent you add for your own steps (data loaded, HUD shown).
2. Cold-join three times on the device (leave and rejoin) and copy the printed list. Never use Studio as the only source: it runs client and server together and loads differently.
3. Analyse with `scripts/JoinTimeline.luau`: `local phases, total = JoinTimeline.phases(marks)`, `JoinTimeline.longPole(phases)`, `JoinTimeline.blocking(phases, {"analytics","datastore","http"}, 3)`. Use the median run. Stop if marks are missing around the long pole: add marks, rerun.
4. Attack the long pole in this order:
   a. Instance count and size: turn on or tune streaming (`streaming-enabler`); inspect free models for obfuscated scripts that spawn thousands of instances; keep client-unneeded assets out of ReplicatedStorage (clients load all of it) and in ServerStorage.
   b. Blocking calls: never block character loading on third-party calls (a creator reported an analytics outage causing 30 s waits at 15,000 CCU). Wrap in pcall with a timeout, run them after the character spawns, and give DataStore loads a retry budget with a default profile.
   c. Preloading: preload only what the first screen needs (`ContentProvider:PreloadAsync` with the minimum list); defer big art, audio and later areas; a loading screen in ReplicatedFirst shows progress, it does not shorten the wait (`loading-screen-builder`).
   d. Splitting a place into multiple places lowers the first join but adds a join on each teleport: weigh against streaming.
5. After each change rerun step 2-3 and compare with `JoinTimeline.verdict(total, budget, previousTotal)`: improved, ok, regressed or over-budget. Keep only improvements.
6. Record the final timeline and the guard: repeat the three cold joins before each release.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) to place `join_marks.luau` as a LocalScript in StarterPlayerScripts -> `start_stop_play` -> `get_console_output` for the marks (Studio-only, label it). Cold joins on a device cannot be driven by MCP: ask the owner for the printed lines or mark device numbers `untested`.

## Fallback
Rojo: add the script as a file; the owner joins on the device and pastes the console lines (Developer Console F9 > Client log). Or time with a stopwatch from tap to controllable, and say it is coarse.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (streaming cuts join time; keep client-unneeded content in ServerStorage; inspect obfuscated model scripts). `Roblox/roblox-kb/scripting-and-performance.md` (join time depends on instance and voxel count; analytics outage example, creator report; join queue exists). Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization identify.md` (measure load time before and after each change with a stopwatch or a ReplicatedFirst script; sudden increases often mean new ReplicatedStorage content or bigger assets), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization design.md` (splitting places), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization test-on-hardware.md` (time the full join-to-gameplay flow on the baseline device). The docs give no seconds target.

## Output
```
JOIN TIMELINE <build> <device> <date> (median of 3)
start 0.0 -> game loaded 4.1 -> character 5.0 -> PlayerGui 5.2 -> HUD 13.4   total 13.4 s
Long pole: PlayerGui -> HUD 8.2 s (61%): analytics init (blocking)
Change: moved analytics after character spawn -> total 6.0 s (improved 55%)
```

## Acceptance checks
- [ ] Three cold joins on the named device; the median is used.
- [ ] The long pole and any blocking third-party call are named with seconds.
- [ ] Each kept change shows a before/after total; regressions over 10 percent are reverted.
- [ ] The test script is removed from the shipping place.
- [ ] Executed check: `JoinTimeline.test.luau` passes under Lune; scripts pass luau-check.

## Pitfalls
Timing in Studio only. Averaging a warm rejoin with cold ones. Hiding a slow join behind a loading screen instead of fixing it. Preloading everything (it delays the start). Blocking join on analytics, ads or HTTP. Putting one huge model in ReplicatedStorage.

## Related
`game-optimizer`, `streaming-enabler`, `loading-screen-builder`, `first-minute-designer`, `replicated-loader-builder`.
