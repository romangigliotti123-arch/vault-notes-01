---
name: tutorial-designer
description: "Teach one mechanic at a time through contextual, skippable, show-dont-tell triggers: list the mechanics, order them by when the player first needs them, define the trigger, cue and success check for each, and keep text to a minimum. Use after first-minute-designer for everything beyond the opening."
category: design
tags: tutorial, onboarding, teach, contextual, hint, skip, ftue, mechanics, show dont tell
kb: Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-dungeon-quest.md
related: first-minute-designer, core-loop-designer, difficulty-tuner, tooltip-system-builder, menu-flow-mapper, accessibility-checker
---

# tutorial-designer

Vault: show, do not tell; keep tutorials short, interactive and practice-based; trigger them from play, not up front; teach only the core loop first, one mechanic at a time; make them skippable and re-readable; gate advanced UI behind progression.

## When to use
After `first-minute-designer` has covered the opening. For each later mechanic, shop, rebirth, trading. Not for: the first 5 minutes (`first-minute-designer`), tooltip code (`tooltip-system-builder`).

## Inputs (max 2)
1. The list of mechanics and systems (default: from `design/core-loop.md` and GDD). 2. Whether older players are a target (default: yes, so skippable).

## Procedure
1. List every mechanic and system a player must learn. Rank by the minute at which the player first needs it. Stop if more than one mechanic is needed in the first minute: simplify the game, not the tutorial.
2. For each mechanic write a row: Mechanic, Trigger (the play event that fires it), Cue (world marker, beam, arrow, glow, highlight, a single short line), Success check (the player did the thing; log it), Skip (how to dismiss), Retry (where to replay it). Triggers come from play: entering a zone, getting an item, being about two-thirds of the way to an unlock, taking too long on a task, first death.
3. Limit: one new mechanic per trigger, one line of text maximum per cue, and no cue blocks input for more than a few seconds. Prefer practice: a safe target or range where the mechanic is done once.
4. Gate advanced UI: hide shop, rebirth, trade buttons until the player is invested; delay starter packs and paid offers until after the first reward.
5. Opt-in for depth: one dismissable prompt at first join for a longer guide; objective tooltips with a toggle in settings; keep a help page for repeat reading (accessibility).
6. Funnel events: log tutorial_step_shown, tutorial_step_done, tutorial_skipped per mechanic so `funnel-analyzer` can find the step where players leave; a step that over 20 percent of players skip or fail is rewritten (the skill's default, not a vault number).
7. Save `design/tutorial.md`; run the doc check.

## Studio MCP path
Design only. After building: `start_stop_play`, then `execute_luau` (Server) to fire each trigger condition and read the step events from `get_console_output`; `screen_capture` each cue.

## Fallback
Walk through a fresh profile by hand and time every step; mark times `estimated`.

## Evidence
`first-session-onboarding` (show, do not tell; interactive practice; opt-in or skippable; contextual triggers at 1K cash and similar; teach only the core loop first; gate features and UI), `retention-d1-d7` (over-explaining with text loses players), `ui-ux-design`, `case-studies-dungeon-quest` (an onboarding change gave +40 percent D1 per the official talk summarised in the quality model).

## Output
`design/tutorial.md`: mechanic table (mechanic, trigger, cue, success check, skip, retry), gated UI list, funnel events.

## Acceptance checks
- [ ] Every row has trigger, cue, success check and skip.
- [ ] No row introduces two mechanics; no cue longer than one short line.
- [ ] Tutorial funnel events are named.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/tutorial.md --kind tutorial` prints PASS.
- [ ] Icons and visible consequences replace instruction text; any dialogue is capped at 3-4 taps (mixed; Roblox/roblox-kb/_tools/DECISION-RULES.md, first-session-onboarding).

## Pitfalls
Front-loaded text walls. Darkened screens with click-the-arrow. Mandatory tutorials that older players quit on. Teaching systems before the player has the currency to use them.

## Related
`first-minute-designer`, `core-loop-designer`, `difficulty-tuner`, `tooltip-system-builder`, `accessibility-checker`.
