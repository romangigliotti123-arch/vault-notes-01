---
name: reward-schedule-designer
description: "Plan what drops when: fixed, variable and milestone rewards across time horizons (per action, per session, per day, per week) with a drop table, visible odds and pity checked by rewardsched.py, and no paid randomness aimed at young players. Use after the progression curve, before the shop or crates are built."
category: design
tags: rewards, drops, variable reward, pity, rng, rarity, milestone, daily, odds, schedule
kb: Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/case-studies-pet-simulator-x.md
related: core-loop-designer, progression-curve-designer, kit-system-integrator, session-length-designer, game-feel-polisher, tos-compliance-checker, economy-balancer
---

# reward-schedule-designer

Vault: same reward every time makes players quit; randomise size, rarity and timing but keep it transparent; a visible pity counter is trusted more than a hidden one; keep rare items scarce; keep skill in the loop.

## When to use
When deciding what the player earns at each time horizon. Not for: curve of levels (`progression-curve-designer`), daily login mechanics (the kit DailyRewards system via `kit-system-integrator`), prices (`economy-balancer`).

## Inputs (max 3)
1. The core loop's cycle time (default: from `design/core-loop.md`). 2. Rarity tiers and wanted odds (default: 70/25/4/1 percent). 3. Whether anything is sold as random (default: no).

## Procedure
1. Fill a four-row schedule: per action (every 5-30 s: small fixed reward plus juice), per few cycles (variable bigger drop), per session (milestone: a 5-15 minute goal completed), per day/week (streak, event, collection set). Each row needs a reward, a size and a time. Stop when any horizon is empty.
2. Write the drop table as percentages summing to 100. Show "1 in X" odds in the UI (vault: show the odds to keep trust; hiding rarity until reveal is a separate presentation choice).
3. Run `python reward-schedule-designer/scripts/rewardsched.py --table "common:70,rare:25,epic:4,legendary:1" --pity legendary:60`. Read mean and p99 opens with and without pity; if the p99 is more than 3x the average, add or lower the pity cap (default of the skill). Re-run until OK.
4. Add one visible progress marker toward the rare reward (pity counter, bar) and one non-random path (craft, earn, or time-gated unlock) so free players reach all core content.
5. Randomness policy: no paid random items for a young audience by default; if the design wants one, mark it `NEEDS_ROMAN` and run `tos-compliance-checker`, because rules are regional and change (live-check).
6. Skill in the loop: add at least one reward modifier from play (combo, direct hit, speed bonus) so auto-play is not optimal. Auto-roll let kids reach the endgame in about 3 hours and wrecked one economy (indie report in the vault).
7. Save `design/rewards.md` with the schedule, drop table and script output.

## Studio MCP path
Design only. To verify live odds: `execute_luau` (Server) rolling the real drop function 10,000 times and printing the tier counts with `print`; compare to the table within sampling error.

## Fallback
Run only the Python simulation; mark live odds `untested`.

## Evidence
`player-psychology-and-game-feel` (randomised reward size, rarity and timing; use with caution; visible pity counter; loss framing for daily rewards; badges and milestones), `core-loops-and-game-design` (rarity and weighted RNG; skill in the loop), `retention-d1-d7` (daily rewards and playtime rewards at about 10, 30, 60 minutes: an official suggestion), `age-ratings-moderation-and-tos` (policy: live-check), `case-studies-pet-simulator-x` (egg and rarity loop: pattern only).

## Output
`design/rewards.md`: four-horizon schedule table, drop table with odds, pity rule, rewardsched output, non-random path, skill modifiers.

## Acceptance checks
- [ ] Executed: `python reward-schedule-designer/scripts/rewardsched.py --selftest` prints `selftest ok`; the design's run ends `OK`.
- [ ] All four horizons have at least one reward.
- [ ] Odds sum to 100 and are shown in the UI spec.
- [ ] No paid randomness unless explicitly approved and policy-checked.

## Pitfalls
Rare tiers that every update makes common (killed one economy in the vault). Hidden odds. Variance so high it feels like gambling. Daily rewards that punish a missed day harshly.

## Related
`progression-curve-designer`, `core-loop-designer`, `session-length-designer`, `economy-balancer`, `tos-compliance-checker`.
