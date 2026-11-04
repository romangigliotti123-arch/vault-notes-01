---
name: mvp-definer
description: "Define the smallest playable version of a game: the loop, one area, the first reward and one return hook, with pass/fail acceptance tests, a one-week build order and an out-of-scope list. Use right after core-loop-designer and scope-cutter, before the first task is assigned."
category: design
tags: mvp, minimum playable, prototype, acceptance test, build order, week one, vertical slice, playtest
kb: Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/case-studies-doors.md
related: core-loop-designer, scope-cutter, first-minute-designer, gdd-one-pager, playtest-bot-writer, rbx-workflow
---

# mvp-definer

Vault: ship a barebones MVP around one core loop and iterate; verify fun before adding content; solo-test the whole loop end to end before adding features (two indie developers reached that independently); build core systems first because dependent systems (shop, inventory) rely on them.

## When to use
The loop is chosen and the team needs a first playable target. Not for: cutting a long list (`scope-cutter`), the full document (`gdd-one-pager`).

## Inputs (max 2)
1. `design/core-loop.md` and `design/scope.md` (default: both if present, else the pitch). 2. Days available (default: 7 productive days).

## Procedure
1. State the MVP sentence: "A player can <verb> in <one area> and gets <first reward> in under 30 seconds, then <the next 2 minutes>, and sees <one reason to return>."
2. List the must-haves, nothing else: the loop's verb with input and feedback, one area (greybox is fine), one currency or reward, one upgrade, data save for that one thing, the spawn-to-first-reward path, one return hook (a goal on screen or a daily reward). Each must feed layer 1, 2 or 3.
3. Write acceptance tests, each pass/fail with a number: first control within 10 s, first reward within 30 s, reward #3 within 60 s, a full loop cycle completable by one player alone, a 10-minute session has no dead 3-minute stretch, no errors in the Output, data saves and loads on rejoin. These are the skill's defaults built from the vault's 30-second and 5-minute rules.
4. Out of scope list (explicit): shop, pets, trading, events, more areas, monetisation beyond a placeholder, polish beyond the juice on the core action. Anything on this list needs a written reason to enter.
5. Order the week: day 1 loop prototype with greybox; day 2 feedback and juice on the core action; day 3 save and one upgrade; day 4 first-minute script (`first-minute-designer`); day 5 playtest with five people, watching rather than helping; days 6-7 fix the top three problems and ship to a small audience. Core systems before the systems that depend on them.
6. Playtest protocol: five players, five minutes each, no instructions; log where each person hesitated or quit. Kill rule: if fewer than 3 of 5 want to keep playing after 5 minutes, fix the loop before adding anything.
7. Save `design/mvp.md`; run the doc check.

## Studio MCP path
Hand day-by-day tasks to the build skills. To verify acceptance tests in Studio: `start_stop_play`, bot via `character_navigation`, `execute_luau` (Server) to timestamp first control and first reward, `get_console_output` for errors.

## Fallback
Time with a stopwatch; mark results `estimated`.

## Evidence
`development-process-and-speed` (barebones MVP; many small games; verify fun before adding content; core systems first), `core-loops-and-game-design` (solo-test the full loop first), `playtesting-and-feedback` (watch players), `first-session-onboarding` (fun within 5 minutes), `case-studies-doors` (first test was a hallway and two monsters).

## Output
`design/mvp.md`: MVP sentence, must-have table, acceptance tests, out-of-scope, week plan, playtest protocol and kill rule.

## Acceptance checks
- [ ] Every acceptance test has a number or a clear pass/fail.
- [ ] Out-of-scope list is non-empty and the must-have list is under about 10 lines.
- [ ] Day 5 playtest exists in the plan.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/mvp.md --kind mvp` prints PASS.

## Pitfalls
An MVP that includes the shop. Polishing before the playtest. Helping testers (hides onboarding problems). Calling a tech demo an MVP with no reward.

## Related
`scope-cutter`, `core-loop-designer`, `first-minute-designer`, `gdd-one-pager`, `playtest-bot-writer`.
