---
name: progression-curve-designer
description: "Design level, XP and unlock curves with quick early wins and a visible long-term goal: pick the XP formula, compute time-per-level from expected income, flag grind walls and spikes with progcurve.py, and lay short, mid and long goals on the curve. Use after the core loop exists, before the economy is tuned."
category: design
tags: progression, xp, level curve, unlock, rebirth, prestige, pacing, grind wall, early game, goals
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/case-studies-pet-simulator-99.md, Roblox/roblox-kb/case-studies-rebirth-speed-run.md
related: core-loop-designer, reward-schedule-designer, difficulty-tuner, session-length-designer, economy-balancer, first-minute-designer, quest-chain-designer
---

# progression-curve-designer

Vault: front-load progression (early levels about a minute, something unlocks or a number jumps every few minutes), show the long-term goal early, layer goals by horizon, and do not fake depth with exponential numbers.

## When to use
After `core-loop-designer`. Not for: currency prices and sinks (`economy-balancer`), drop rates (`reward-schedule-designer`), enemy difficulty (`difficulty-tuner`).

## Inputs (max 3)
1. Income per minute at level 1 and expected growth (default: measured from a prototype; else 60 xp/min flat, marked `estimated`). 2. Target hours to the first long-term milestone (default: 10 hours of play for a session game). 3. Levels in the first area (default: 10).

## Procedure
1. Choose the curve shape. Default `xp(L) = base * growth^(L-1)` with base so L1 takes about 20 s and growth 1.2-1.4. With little content use flatter growth and add content per stage (ByteBlox, indie); do not use currency walls instead of natural gates.
2. Run `python progression-curve-designer/scripts/progcurve.py --levels 30 --base 20 --growth 1.35 --xp-per-min 60 [--xp-growth 1.1]`. Read the table. Fix every FLAG (early levels over 1.5 min, a grind wall before level 10, a level costing over 2.5x the last). These thresholds are the skill's defaults, not vault numbers.
3. Place unlocks on the curve: something new at least every 3-5 minutes in the first 30 minutes (a tool, zone, pet slot, colour, title). List them in a table with the level or minute.
4. Lay goals by horizon: short (this session), mid (days), long (weeks). Name one visible long-term goal shown in the first 5 minutes (a locked door, a rare silhouette, a huge number).
5. Rebirth or prestige, if used: first requirement low, later ones hard; it resets one thing and keeps another; it must change context (new area, new tools) rather than repeat the loop with bigger numbers.
6. Stagger gates so players do not grind one area; if playtesters rush content, add an unlock gate before launch (LovJak, indie).
7. Save `design/progression.md` with the script output pasted and the unlock table.

## Studio MCP path
Design first. For the measured income: `start_stop_play`, drive the loop with `execute_luau` (Server) for 5 minutes, read the earned XP from the `PlayerData` profile, then re-run the script with that value.

## Fallback
Run the script on estimates and mark every row `estimated` until a playtest gives real income.

## Evidence
`core-loops-and-game-design` (front-load progression; layer goals; rebirth meaningful; do not fake progression), `first-session-onboarding` and `retention-d1-d7` (D7 fix: visible short, mid and long goals), `case-studies-pet-simulator-99` and `case-studies-rebirth-speed-run` (rebirth and zone-gating patterns; creator/tracker claims).

## Output
`design/progression.md`: formula, progcurve table (first 30 levels), flags fixed, unlock table, goal ladder (session, days, weeks), rebirth rule if any.

## Acceptance checks
- [ ] Executed: `python progression-curve-designer/scripts/progcurve.py --selftest` prints `selftest ok`, and the design's own run ends with `OK`.
- [ ] L1-L3 each take about a minute or less; the first unlock lands within 5 minutes.
- [ ] A long-term goal is visible in the first 5 minutes.
- [ ] Income values are marked measured or `estimated`.

## Pitfalls
Exponential costs with linear income. A rebirth that resets everything for a small multiplier. All unlocks in one early cluster then nothing. Tuning with developer-speed play instead of a fresh player's.

## Related
`core-loop-designer`, `reward-schedule-designer`, `difficulty-tuner`, `session-length-designer`, `economy-balancer`.
