---
name: regression-checklist-builder
description: "Build the checklist to re-run after each change: derive rows from the systems the change touched plus a fixed core set, give each row an id, a runnable action and an observable expected result, and lint it. Use before every release or risky merge so 'did we break anything' is a list, not a feeling."
category: qa
tags: regression, checklist, release, smoke test, qa, test plan, change, checks, launch gate, re-run
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: playtest-bot-writer, publish-readiness-gate, bug-report-template, device-test-matrix, purchase-flow-tester, save-load-tester, multiplayer-test-planner
---

# regression-checklist-builder

A regression checklist is the list of things that used to work and must still work. It stays small, is grouped by system, and every row can be run by someone who did not write it. `scripts/checklist_lint.py` (self-tested) rejects rows that cannot be run: no id, a vague "works" as the expected result, duplicates, or a list too short to matter. Rows that can be automated point to a bot (`playtest-bot-writer`) or a scenario suite; the rest are done by hand.

## When to use
Before a release, after a refactor, when a bug returns, when onboarding a tester. Not for: the pre-launch gate across everything (`publish-readiness-gate`), writing the bot itself (`playtest-bot-writer`), or one-off exploration testing.

## Inputs (max 2)
1. What changed (default: the git diff or the last session summary; list the systems it touched). 2. The game's core loop and money paths (default: `design/core-loop.md` and the kit systems in use: PlayerData, Shop, DailyRewards, Analytics, Admin).

## Procedure
1. Start from the core set that every release re-runs: join and spawn; first action and first reward; save and rejoin; the shop opens and a test purchase grants once; one multiplayer interaction; UI on the smallest target phone; Output has no new errors; load time within your target. Stop at 8-12 core rows.
2. Add rows for each system the change touched, using the failure that system is known for: PlayerData -> `save-load-tester` and `data-loss-simulator`; Shop -> `purchase-flow-tester`; remotes -> `remote-fuzzer` / `input-validation-auditor`; movement -> `speed-teleport-detector` tests; UI -> `device-test-matrix`; economy -> `balance-sim-runner`. Prefer a row that runs a command or bot over a row that says "check".
3. Add one row per bug fixed since the last release (the bug's repro as the action, the corrected behaviour as the expected result). This is how regressions stay fixed.
4. Write every row as `id | area | check | expected`: id like R-001; check is a command, menu path or bot name; expected is observable (a number, a log line such as `PURCHASE FLOW: 7/7 scenarios passed`, a visible state). Ban "works", "looks fine", "as expected".
5. Run `python scripts/checklist_lint.py checklist.md`; fix every FAIL line. Exit 0 and at least 5 rows is the minimum.
6. Run the list in a test place: record PASS/FAIL, who, build/place version, and the Output excerpt for each FAIL. A FAIL becomes a bug report (`bug-report-template`). Do not release with an unexplained FAIL.
7. Keep the file at `tests/regression.md`; after the release, move rows that never fail in six releases to a monthly list and add rows for new bugs.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `start_stop_play` -> for bot rows `execute_luau` (Server/Client) with the bot and `get_console_output` -> for UI rows `screen_capture` per device profile -> `start_stop_play` (stop). Manual rows are done by a person and ticked in the file.

## Fallback
No Studio: the list is still the deliverable; every row not run is `untested`. `python scripts/checklist_lint.py --selftest` shows the lint's good and bad examples.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: playtest after every few small changes, not after a big batch; test solo and multiplayer; stress-test loops, duplicates and persistence after each change; keep a folder of repros; use a fresh-eyes tester and a bug pass. `Roblox/roblox-kb/_tools/CHECKLIST-launch.md` and `CHECKLIST-monetization.md`: the vault's launch and monetisation gates to seed rows. `Roblox/roblox-kb/playtesting-and-feedback.md`: bots do not replace watching new players.

## Output
`tests/regression.md` with the table (`id | area | check | expected | last result`), the lint output, and a run record (build, date, tester, PASS/FAIL counts, links to bug reports).

## Acceptance checks
- [ ] `python scripts/checklist_lint.py --selftest` prints "checklist_lint selftest: ok ...".
- [ ] `python scripts/checklist_lint.py tests/regression.md` exits 0 with "ready" and 5 or more rows (quoted).
- [ ] Every row has an observable expected result; no row says only "works".
- [ ] Every fixed bug since the last release has a row.
- [ ] The run record lists each row as PASS, FAIL or untested.

## Pitfalls
A list that grows until nobody runs it. Rows that test the implementation instead of the player-visible result. Skipping the money and save rows because "nothing changed there". Letting one tester do the whole list on one device. Fixing the checklist to match a regression instead of the code.

## Related
`playtest-bot-writer`, `publish-readiness-gate`, `bug-report-template`, `device-test-matrix`, `purchase-flow-tester`, `save-load-tester`.
