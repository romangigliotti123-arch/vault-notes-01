---
name: repro-step-writer
description: "Turn a vague bug ('the shop is broken sometimes') into exact reproduction steps by pinning the starting state, varying one factor at a time, and confirming the steps on a fresh join. Use before filing or fixing any bug you cannot yet make happen on demand."
category: qa
tags: reproduction, repro steps, minimal repro, bisect, bug, flaky, intermittent, test, isolate, steps
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/scripting-and-performance.md, Mentor/Combined-Brain.md
related: bug-report-template, output-error-triager, playtest-bot-writer, multiplayer-test-planner, join-leave-race-tester, crash-log-reader
---

# repro-step-writer

A bug you can make happen on demand is half fixed. This skill turns a fuzzy report into a numbered list of steps that starts from a known state, changes one factor at a time to find which ones matter, and ends with a confirmed run. The output goes straight into `bug-report-template` (its `bug-report-template/scripts/bug_report_lint.py` checks the steps section).

## When to use
A report with no steps, an "it happens sometimes" bug, a bug seen only on one device, or an automated check that failed once. Not for: reading logs (`output-error-triager`), races you can enumerate (`join-leave-race-tester`), or writing the fix.

## Inputs (max 2)
1. The report as received (text, screenshot, log lines). 2. Access (default: a test place and, if the bug may depend on it, the device or account type).

## Procedure
1. Extract the claim: what the reporter did, what they expected, what they saw, on what device and build. List what is unknown; ask the reporter at most three questions, the ones that change the steps (device? first time or after respawn? alone or with others?).
2. Pin the start: a fresh join of a test place, the same account type, default settings, no leftover state. Write it as step 1. If the bug needs data state (owns item X), create that state with a plugin or `execute_luau` and say so.
3. Try the reporter's path once as written. If it happens, go to step 5. If not, list the factors that differ (respawned first, slow network, other players present, specific item, low graphics, touch input, time since join) and vary ONE per attempt, recording each as happened / did not.
4. Use the tools that make rare things common: 0.5-1 s artificial replication lag for races, the Network Simulator for latency and loss (one setting at a time), a second client for multiplayer, `playtest-bot-writer` to repeat the sequence 20 times and count (a bot turns "sometimes" into "7 of 20"), and the Client/Server toggle with Output filters to see which side errors.
5. Minimise: remove every step that is not needed (try removing one at a time and re-running). Keep the shortest list that still triggers it, with exact names (button labels, item names, positions).
6. Confirm: a fresh join, only the written steps, by someone or something that did not discover them (the bot, or you after a reset). Record frequency (N of M).
7. Hand off: steps, frequency, factors that matter and factors that do not, Output lines, then lint with `bug-report-template`. If it never reproduced, file "not reproduced after M attempts" with what was tried, not a guess.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `character_navigation` / `user_keyboard_input` / `user_mouse_input` to follow the steps -> `execute_luau` (Server/Client) to set state and read values -> `get_console_output` and `screen_capture` after each attempt -> `start_stop_play` (stop). Repeat counts come from a Harness bot loop.

## Fallback
By hand in Studio Test mode with a written attempt table (attempt, factor changed, result). Whatever could not be reproduced on the reporter's real device is `untested`; say which device was missing.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: reproduce race conditions with 0.5-1 s artificial lag; use 50-150 ms baseline latency and packet loss; test on real low-end Android devices; use the Client/Server toggle and pause/step to debug ephemeral mechanisms; confirm events with a temporary print; reproduce, profile, fix, retest; fresh-eyes testers reproduce bugs step by step and keep a folder of repros; report expected vs actual. `Roblox/roblox-kb/playtesting-and-feedback.md` for structured tester notes.

## Output
```
REPRO <bug> <date>: reproduced yes/no, frequency N of M
Start state: <fresh join, account type, data state>
Steps: 1. .. 2. ..      Factors that matter: .. Do not matter: ..
Evidence: Output lines, screenshot      Not tried: <devices, accounts>
```

## Acceptance checks
- [ ] The steps start from a stated fresh state and each step is one action under 200 characters.
- [ ] A confirmation run used only the written steps; N of M is recorded.
- [ ] At least one factor was varied alone, and the result of each attempt is in the attempt table.
- [ ] `python bug-report-template/scripts/bug_report_lint.py report.md` exits 0 with the steps in it (quoted), or the bug is marked not reproduced.
- [ ] Unreproduced devices/accounts are named as untested.

## Pitfalls
Changing three things per attempt. Steps that rely on leftover state from earlier tests. Testing only on a dev account. Writing "click around the shop" (exact labels). Confirming with the same person who found the steps while the game still holds state. Stopping at one lucky reproduction.

## Related
`bug-report-template`, `output-error-triager`, `playtest-bot-writer`, `multiplayer-test-planner`, `join-leave-race-tester`.
