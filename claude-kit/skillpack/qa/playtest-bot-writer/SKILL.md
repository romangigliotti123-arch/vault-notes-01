---
name: playtest-bot-writer
description: "Write a scripted bot that plays a game's core loop inside a Studio playtest and asserts the outcomes (first action, first reward, save fields, purchase grant, state transitions), using a small tested harness and the Studio MCP execute_luau and input tools. Use to turn 'it should work' into a repeatable check after every change."
category: qa
tags: playtest, bot, automated test, harness, assert, studio mcp, execute_luau, regression, simulate, core loop
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/first-session-onboarding.md
related: rbx-playtest, rbx-playtest-list, regression-checklist-builder, multiplayer-test-planner, first-minute-designer, purchase-flow-tester, save-load-tester, rbx-studio
---

# playtest-bot-writer

A bot cannot judge fun; it proves the loop still works. It catches "the first reward never arrives" and "the save field vanished" in 30 seconds. Human feel testing stays `rbx-playtest`. Connection modes and the write-run-read loop are defined in `rbx-studio`; this skill adds the bot pattern.

## When to use
After a gameplay change, before a release, or to time the first minute. Not for: UX/feel judgement, performance (`game-optimizer`), or exploit testing (`remote-fuzzer`).

## Inputs (max 3)
1. The loop to test (default: first action to first reward from `design/core-loop.md`). 2. Success conditions as measurable facts (default: reward count > 0, currency increased, no errors in Output). 3. Studio MCP connected? (default: detect).

## Procedure
1. Write the scenario as 3-8 checks, each observable on the SERVER datamodel: "player data loaded", "player has a character", "after calling `Collect(player)` coins increased", "pet equipped is saved", "output has no errors". Prefer calling the game's server functions directly over simulating inputs; use input simulation only for client-only behaviours (UI buttons, tools).
2. Copy `scripts/Harness.luau` (check, checkEq, waitFor with timeout, step with error capture, report). Write the bot as a script that `require`s it (or inline the module text for `execute_luau`). Skeleton:
   ```lua
   local h = Harness.new("core loop")
   local player = game.Players:GetPlayers()[1]
   h:waitFor("character spawned", function() return player and player.Character end, 10)
   local before = PlayerDataService.Get(player).coins
   h:step("collect", function() Collect(player) end)
   h:waitFor("coins increased", function() return PlayerDataService.Get(player).coins > before end, 5)
   print(h:report())
   ```
3. Run: Studio MCP: `start_stop_play`, wait for the player (`get_studio_state`), `execute_luau` with datamodel_type Server running the bot, then `get_console_output` for errors; `stop`. Quote the report lines.
4. Client-side behaviours: `execute_luau` with datamodel_type Client, `character_navigation` to a target, `user_keyboard_input` / `user_mouse_input` for buttons, `screen_capture` as evidence.
5. Make it repeatable: save the bot under `tests/bots/<name>.luau` (not in the shipped game); list the command to run in `tests/README.md`; run it before each release (`regression-checklist-builder`).
6. Report: PASS/FAIL per check with the time; a failing check gets the exact Output lines. Do not "fix" a bot by loosening its asserts.

## Studio MCP path
As in steps 3-4: `list_roblox_studios` -> `get_studio_state` -> `start_stop_play` -> `execute_luau` (Server/Client) -> `get_console_output` -> `screen_capture` -> `start_stop_play` (stop). One agent at a time uses the session; never publish or save over the user's place.

## Fallback
No Studio: unit-test pure logic with Lune using fakes (`~/.claude/claude-kit/systems/_check/harness.luau`; run `lune run <file>` from `systems/`), and give the owner the bot as a Script to paste into ServerScriptService of a test place. Mark results `untested`.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md` (playtest after every few small changes; test solo and multiplayer; client/server toggle; confirm events with prints), `Roblox/roblox-kb/playtesting-and-feedback.md` (bots do not replace watching new players), `Roblox/roblox-kb/first-session-onboarding.md` (the checks to time). Studio tools: `rbx-studio` skill.

## Output
`tests/bots/<name>.luau`, a PASS/FAIL report block, timings, and the Output excerpt; failures include the first error line.

## Acceptance checks
- [ ] Every check is a measurable fact; none is "looks fine".
- [ ] The bot ran and the report is quoted (or labelled untested).
- [ ] Output was read before and after; new errors are listed.
- [ ] Harness logic tests pass (`lune run ../skillpack/qa/playtest-bot-writer/scripts/tests/Harness.test.luau`: "4 passed, 0 failed").
- [ ] The bot lives in `tests/`, not the shipped place, and is re-runnable.

## Pitfalls
Racing the load (wait for the character and data, not a fixed `task.wait`). Passing because a check never ran. Bots that touch the live DataStore (use a test place, or mock). Asserting on timings that vary by machine. Treating a green bot as "good".

## Related
`rbx-playtest`, `rbx-playtest-list`, `regression-checklist-builder`, `multiplayer-test-planner`, `purchase-flow-tester`, `save-load-tester`.
