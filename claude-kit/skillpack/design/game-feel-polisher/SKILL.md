---
name: game-feel-polisher
description: "List the juice pass for each core action: for every verb the player repeats, define the sound, visual, number or UI, camera and haptic beats with timings, so every action has an immediate visible and audible reaction. Use after the core loop exists and the first reward works, before art polish."
category: design
tags: game feel, juice, feedback, sound, vfx, tween, camera shake, haptics, polish, hit stop
kb: Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/vfx-and-particles.md, Roblox/roblox-kb/sound-and-music.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/combat-and-gameplay-systems.md
related: core-loop-designer, first-minute-designer, reward-schedule-designer, damage-number-builder, ui-animation-planner, sound-placement-planner, accessibility-checker
---

# game-feel-polisher

Vault (official): give every player action an immediate visible or audible reaction; test hit latency directly. Small juice takes a beginner 20-30 minutes: VFX, sound, particles, number pop-ups, orbs flying to the player, camera shake, bounce tweens and a roughly 0.1 s hit-stop.

## When to use
After the loop works but feels flat, or when a playtester says "I did not know it worked". Not for: building specific UI animations (`ui-animation-planner`), damage numbers (`damage-number-builder`), music (`sound-placement-planner`).

## Inputs (max 2)
1. The list of repeated actions (default: from `design/core-loop.md`). 2. Platform split (default: mobile 70-80 percent, so no feature that needs a keyboard and a performance budget for effects).

## Procedure
1. List the actions in order of repetition (the most repeated first): the core verb, pickup, hit, reward, level-up, purchase, error, unlock. Add the failure and the near-miss; a silent failure feels like lag.
2. For each action fill a row: Action, Sound (what and pitch rule: a rising pitch for combos), Visual (particle, flash, squash-and-stretch, 0.1-0.3 s tween), Number/UI (pop-up, counter tick, bar fill), Camera (shake amount, FOV nudge, hit-stop about 0.1 s), Haptic (mobile vibration on big moments, optional), Latency target (input to first visible reaction under about 100 ms, the skill's default).
3. Scale by importance: tiny for the 1000th pickup, big for a rare drop or level-up. If every action is loud, nothing is.
4. Budget: cap simultaneous effects and particles for low-end phones; reuse the genre-standard effects; defer anything that needs new art.
5. Accessibility: a sound-off pass (visuals still carry the meaning), a camera-shake slider, flashing limits, volume categories (`accessibility-checker`).
6. Order the build: sound and number pop first (cheapest, biggest effect), then tween and particles, then camera, then haptics.
7. Test: play with sound on and off; ask a fresh tester which actions "felt good"; if any action gets "I could not tell", add one more beat there.
8. Save `design/feel.md`; run the doc check.

## Studio MCP path
`start_stop_play`; `execute_luau` (Server) to fire each action and `screen_capture` the reaction frame; `get_console_output` for warnings; measure latency by timestamping the input and the effect start with `os.clock()` in a client script (needs a client run; may be `untested`).

## Fallback
A table is the deliverable. Mark latency `estimated` until measured.

## Evidence
`player-psychology-and-game-feel` (immediate reaction; combos and variety; fixes for flat games), `core-loops-and-game-design` (instant feedback and juice; movement feel; hit-stop), `vfx-and-particles`, `sound-and-music`, `combat-and-gameplay-systems` (readable anticipation, contact, recovery).

## Output
`design/feel.md`: action table with sound, visual, number/UI, camera, haptic and latency target; build order; accessibility notes.

## Acceptance checks
- [ ] Every repeated action plus the failure case has a row with at least a sound and a visual.
- [ ] Effects are scaled by importance and a particle cap is stated.
- [ ] A sound-off and a shake-slider path exist.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/feel.md --kind feel` prints PASS.

## Pitfalls
Polishing before the loop is fun. Same loud effect on every pickup. Camera shake with no off switch. Effects that hide the readable telegraph in combat.

## Related
`core-loop-designer`, `first-minute-designer`, `reward-schedule-designer`, `ui-animation-planner`, `accessibility-checker`.
