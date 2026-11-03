---
name: first-minute-designer
description: "Script the first 30 seconds, first 2 minutes and first 5 minutes of a Roblox game as a timed checklist - spawn view, first action, first reward, first guidance cue, first reason to stay or return - using the vault's onboarding rules, and test it by timing a real or scripted run. Use when D1 or play-through is weak or when designing a new game's opening."
category: design
tags: first minute, onboarding, tutorial, first session, first 30 seconds, ftue, spawn, beam, arrow, d1
kb: Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/_tools/BENCHMARKS.md
related: tutorial-designer, core-loop-designer, retention-diagnoser, funnel-analyzer, game-feel-polisher, mobile-ui-audit, playtest-bot-writer
---

# first-minute-designer

Free players who are not hooked in about five minutes are very unlikely to return (vault, official-sourced). The first 30 seconds decide whether they stay for those five. This skill writes the opening as a timed script and checks it.

## When to use
New game opening; low D1 or first-session drop-off; a tutorial that players skip or quit during. Not for: teaching a complex system over hours (`tutorial-designer`), pure analytics reading (`funnel-analyzer`).

## Inputs (max 3)
1. The core loop sentence (default: `design/core-loop.md`). 2. Current opening, if any (default: playtest it). 3. Platform mix (default: mobile first).

## Procedure
1. Measure the current opening if one exists: play it with a stopwatch (or Studio MCP below). Record seconds to: first control, first meaningful action, first reward, first goal shown, first menu opened. Anything over about 10 seconds to the first action is a stall (attention is roughly 8-10 s in creator reports).
2. Write the target script (times are goals):
   - 0-5 s: spawn into the fun place, not a menu; the hero view shows the thing the thumbnail promised; no text wall; character already free to move.
   - 5-15 s: first action is the core verb, one input, obvious target; world cues point to it (beam from player, arrow, bright path, landmark), not paragraphs.
   - 15-30 s: first reward with juice (sound + number pop + particle), and the goal for the next 2 minutes is visible.
   - 30 s-2 min: three to five cycles of the loop, each slightly bigger; first upgrade or unlock; teach exactly one new thing, triggered by play (contextual, skippable).
   - 2-5 min: first meaningful choice, first social touch (friend prompt, other players visible), and the first "next goal" that is 3-5 minutes away.
   - End of the opening: a moment of joy (reward animation) AND a reason to return tomorrow (daily reward, unfinished goal, timer).
3. Remove: mandatory tutorials longer than a minute, text-first explanations, forced menus, scattered mini-popups, prompts to buy before the first reward.
4. Mobile pass: all key actions reachable by thumb, text readable at phone size (`mobile-ui-audit`), no keyboard-only steps.
5. Instrument: define the funnel events (spawned, first_action, first_reward, goal_seen, 2min, 5min, returned_d1) so the drop-off point is visible (`funnel-analyzer`, kit system Analytics).
6. Verify by timing the new opening: target first action <= 10 s, first reward <= 30 s. Record the numbers.
7. Write `design/first-minute.md` and the fix list (cheapest first).

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `screen_capture` (0 s, 10 s, 30 s) -> `character_navigation` / `user_keyboard_input` / `user_mouse_input` to do what a new player would do -> `get_console_output`; or `execute_luau` (Server) with the bot pattern in `playtest-bot-writer` to time first action/reward. Stop play afterwards.

## Fallback
Ask the owner for a stopwatch time on a phone for the five checkpoints, or work from the script. Mark all timings `estimated` until measured.

## Evidence
`Roblox/roblox-kb/first-session-onboarding.md` (fun within seconds; show, don't tell; world cues; short interactive tutorials; opt-in/skippable; contextual teaching; one mechanic at a time), `Roblox/roblox-kb/retention-d1-d7.md` (first 5 minutes; fix onboarding by finding the drop-off; end with joy and a reason to return; friends), `Roblox/roblox-kb/ui-ux-design.md`, `Roblox/roblox-kb/_tools/BENCHMARKS.md` (D1 12-15 percent is "very good" in creator reports; official same-genre percentiles are in the sheet with their flags).

## Output
`design/first-minute.md`: measured vs target timeline table (checkpoint, now, target), the scripted opening step by step, removed items, funnel events, and the ordered fix list.

## Acceptance checks
- [ ] Five checkpoints have a time (measured or marked estimated).
- [ ] First action <= 10 s and first reward <= 30 s in the new script.
- [ ] No text-only teaching step; every cue is visible in the world or UI.
- [ ] The opening ends with a reward and a reason to return.
- [ ] No purchase prompt before the first reward.
- [ ] Funnel events defined.
- [ ] The first-action clock starts after the age-check/ID step (that is pre-play friction, not tutorial time; official 2026-01); starting currency is about 10 coins and the first purchase is reachable inside the first session (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, first-session-onboarding).

## Pitfalls
Long mandatory tutorial. Teaching three systems at once. A pretty intro that blocks control. Great desktop flow that fails with touch. Optimising the opening without the analytics to see whether it worked.

## Related
`tutorial-designer`, `core-loop-designer`, `retention-diagnoser`, `funnel-analyzer`, `game-feel-polisher`, `mobile-ui-audit`.
