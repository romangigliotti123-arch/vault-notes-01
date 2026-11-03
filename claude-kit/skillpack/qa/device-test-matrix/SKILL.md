---
name: device-test-matrix
description: "Choose which devices, inputs, graphics settings, network conditions and server modes to test, using an all-pairs matrix that covers every pair of settings in a handful of rows, and say how to test each (real device, emulator, Network Simulator, Controller Emulator). Use before a release or after UI, performance or input changes."
category: qa
tags: device testing, test matrix, pairwise, mobile, low-end android, gamepad, controller, network simulator, graphics, platform
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/all-numbers-and-benchmarks.md
related: mobile-ui-audit, gamepad-ui-navigator, safe-area-checker, multiplayer-test-planner, load-test-planner, game-optimizer, regression-checklist-builder
---

# device-test-matrix

You cannot test every combination, but you can test every PAIR of settings (phone with touch, phone with low graphics, touch with slow network...) in a few rows. `scripts/Pairwise.luau` generates a deterministic all-pairs matrix, drops combinations that cannot exist, and verifies coverage. This skill decides the parameters, the rows and how to run each row.

## When to use
Before a release, after UI/input/performance work, when a bug appears only on one device type. Not for: a single-device visual check (`mobile-ui-audit`), gamepad flow design (`gamepad-ui-navigator`), or load (`load-test-planner`).

## Inputs (max 2)
1. Your audience (default: young mobile players first, plus desktop and console if the game ships there; read analytics platform split if available). 2. Features at risk (default: HUD, shop UI, core loop controls, loading).

## Procedure
1. Pick parameters and values from real audience data (analytics platform/device split; live-check). Typical: Platform (phone, tablet, desktop, console), Input (touch, keyboard and mouse, gamepad), Graphics (low, auto, high), Network (good, slow, lossy), Server (solo, full), plus a game-specific parameter (language, safe-area device). Stop at 4-6 parameters of 2-4 values each.
2. Write the exclusions: impossible combinations such as console with touch (`exclude(row)` function). Impossible pairs are reported as `uncoverable`; list them as not applicable.
3. `Pairwise.generate(params, exclude)` then `Pairwise.coverage(params, rows)` must return covered == total; `Pairwise.format` prints the Markdown table of rows. Six parameters of 3-4 values typically need about 15-20 rows instead of hundreds.
4. Add must-have rows by hand: the lowest-end real phone you target, the most common device, a controller-only run, and the worst network row. A matrix is a minimum, not a ceiling.
5. For each row choose the method: real low-end Android/iOS device for memory and thermal behaviour (Studio and emulators miss them); device emulator for layout and safe areas only; Controller Emulator for gamepad and analog input; Network Simulator for latency, jitter and packet loss (change one thing at a time; the "ideal" preset still adds latency, so use an all-zero custom baseline); solo vs multi-client for sync (`multiplayer-test-planner`).
6. For every row run the same short script: join, first minute, core loop once, open shop, buy test item (Studio test purchase, no Robux), leave. Record PASS/FAIL, FPS or frame feel, memory (F9), and a screenshot for each failure.
7. Fix by severity, re-run only the failed rows plus one control row, and keep the matrix file for the next release (`regression-checklist-builder`).

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Client) to set `UserSettings` graphics or simulate a viewport size -> `screen_capture` per row -> `get_console_output` -> `start_stop_play` (stop). Real-device rows cannot be driven by MCP; the owner runs them from the table.

## Fallback
`lune run ../skillpack/qa/device-test-matrix/scripts/tests/Pairwise.test.luau` from `claude-kit/systems` proves the generator. Without devices the matrix is still the plan; every row not run is `untested`.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: test on real low-end Android devices, not only Studio or a dev PC (emulation misses memory pressure and thermal throttling); test gamepad and analog input with the Controller Emulator; simulate network conditions one at a time and use a zero-value baseline; use 50-150 ms latency and packet loss for prediction; do not judge performance from Studio or emulators; fix performance test conditions for comparable results. `Roblox/roblox-kb/playtesting-and-feedback.md`: fresh-eyes testers. Audience splits are live data: check analytics.

## Output
```
DEVICE MATRIX <game> <date>: params P, rows R, pair coverage C/C
| # | Platform | Input | Graphics | Network | Server | method |
Not applicable pairs: <list>   Results column: PASS/FAIL/untested
```

## Acceptance checks
- [ ] `lune run` of the Pairwise test prints "7 passed, 0 failed".
- [ ] `Pairwise.coverage` equals total pairs for the generated rows (quoted), uncoverable pairs listed.
- [ ] The lowest-end target real device is a row; untested real-device rows are named.
- [ ] Every row has a method and a recorded result or `untested`.
- [ ] Exclusions are real device limits, not convenience.

## Pitfalls
Choosing values from your own hardware. Treating pairwise as full coverage (3-way bugs exist). Emulator-only mobile testing. Changing several network settings at once. Testing graphics Auto only. Forgetting the shop and loading screens on the smallest screen.

## Related
`mobile-ui-audit`, `gamepad-ui-navigator`, `safe-area-checker`, `multiplayer-test-planner`, `game-optimizer`.
