---
name: live-balance-tuner
description: "Tune live values (prices, drop rates, health, rewards) from data without a publish: pick the signal, change one value in bounded steps with a cooldown, stage the rollout, watch guardrails and revert on a rule. Ships a tested TuneGuard module. Use for weekly balance passes on a running game."
category: liveops
tags: balance, live tuning, config, economy, difficulty, nerf, buff, rollout, guardrails, data driven, live ops
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/events-and-seasonal-content.md
related: feature-flag-config-builder, experiment-designer, economy-health-monitor, economy-balancer, patch-notes-writer, rollback-planner, ab-result-reader
---

# live-balance-tuner

Balance changes made in a hurry cause the next incident. The vault's rules are practical: make new content slightly too hard and ease it later; buff underused items instead of nerfing popular ones; act on economy-threatening features even if players object; and tune live with configs instead of republishing. This skill adds bounds, small steps and a revert rule. `feature-flag-config-builder` holds the values; this decides how to move them.

## When to use
A weekly balance pass, an item everyone picks or nobody does, a reward that skews the economy, a boss that is too easy or too hard. Not for: pre-launch modelling (`economy-balancer`), a large redesign (ship it as a major update), or testing a hypothesis with a control (`experiment-designer`).

## Inputs (max 3)
1. The value, its current setting and bounds. 2. The signal that says it is wrong (pick rates, completion rate, sink ratio from `economy-health-monitor`, win rates). 3. The guardrail metric to watch (D1, session time, revenue per user, complaints).

## Procedure
1. Name the signal and the target ("boss 1 clear rate between 40 and 60 percent for first-time attempts"). If you cannot name it, you are guessing; collect it first.
2. Prefer a buff to a nerf when the aim is to rebalance usage (vault). A nerf needs a number in the patch notes and a stronger reason. New content may start slightly harder; ease it later.
3. Define the guard: `{ min, max, maxStepPct, cooldown }` for the value. Defaults in `TuneGuard`: 25 percent maximum step and a one-hour cooldown (this skill's defaults; the vault says bold changes move metrics, so raise the step for an experiment but not for a live economy).
4. Check a proposed change with `TuneGuard.check(def, current, proposed, history, now)` (copy `scripts/TuneGuard.luau`). If refused, take the returned nearest allowed value or wait out the cooldown. `TuneGuard.stages(from, to, n)` gives the intermediate values; apply one stage per observation window.
5. Apply through the config source with a gradual rollout (the docs mention 15 minutes; live-check) after reading the draft back; record `{at, from, to, reason}` in the history and in `decisions.md`.
6. Watch the guardrail for the hold time you set (at least one full day for daily-cycle games). Compare to the same weekday last week, and slice by new vs returning players; a change that helps veterans and hurts newcomers is a retention cost.
7. Revert rule written in advance: if the guardrail falls past a threshold, restore `TuneGuard.revertValue(history)` immediately, then analyse. Do not stack a second change on an unread first one.
8. Announce balance changes with numbers (`patch-notes-writer`) and keep the public stats and drop-rate reference updated (vault). Do not change odds quietly, especially near an event end.
9. If the data is ambiguous after one change, escalate to a controlled test (`experiment-designer`).

## Studio MCP path
`script_read` the module holding the value -> `multi_edit` to read it from the flag layer -> `start_stop_play` -> `execute_luau` (Server) to run `TuneGuard.check` with the real definition and a proposed value and print the decision.

## Fallback
Rojo plus the Lune suite: `lune run ../skillpack/liveops/live-balance-tuner/scripts/tests/TuneGuard.test.luau` from `.rbx/claude-kit/systems` (8 tests) and luau-check. The live config write itself is manual and `untested` here.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: use live configs and experiments instead of republishing; balance and economy changes (slightly too hard then ease; buff underused items; act on economy-threatening features); publish a stats and drop-rate reference with each balance change; check key metrics after every update. `ab-testing-and-experiments.md`: gradual rollout for live gameplay values; reward-to-difficulty ratios per segment (indie, reported up to about 10 percent LTV lift). `events-and-seasonal-content.md`: do not secretly boost odds near the end of an event.

## Output
`liveops/tuning-log.md`: dated rows (value, from, to, signal, guard decision, hold time, result, revert rule), plus the TuneGuard definition per value.

## Acceptance checks
- [ ] Lune suite prints "8 passed, 0 failed"; luau-check exit 0.
- [ ] Each change has a signal, a target, bounds, a hold time and a revert rule.
- [ ] No step over the limit and no change inside a cooldown, or the exception is justified.
- [ ] The patch notes carry the number; no hidden odds change.
- [ ] Guardrails were read against the same weekday baseline and segmented.

## Pitfalls
Nerfing the popular item instead of buffing the rest. Stacking changes before reading the first. Changing prices and rewards on the same day. Tuning from a spike. Letting players discover nerfs.

## Related
`feature-flag-config-builder`, `experiment-designer`, `economy-health-monitor`, `patch-notes-writer`, `rollback-planner`.
