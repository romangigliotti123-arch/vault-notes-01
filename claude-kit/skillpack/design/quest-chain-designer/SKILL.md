---
name: quest-chain-designer
description: "Design a quest or objective chain that teaches systems in order and paces rewards: outcome-phrased steps, completable dailies, chain structure, tailored by level, with no gameplay gated behind notifications. Use after the progression curve, when players need a next goal or undiscovered features."
category: design
tags: quest, missions, objectives, daily, chain, tasks, guidance, onboarding, goals
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/case-studies-blox-fruits.md
related: progression-curve-designer, tutorial-designer, reward-schedule-designer, session-length-designer, kit-system-integrator, quest-system-builder
---

# quest-chain-designer

Vault: quests and missions must serve the loop and respect time: phrase on outcomes, avoid hard-currency tasks, keep dailies completable in a session, vary categories, chain quests, allow multi-progress, tailor by level, never gate gameplay behind notifications, and use quests to surface undiscovered features. A loop with no missions or pending goals fails the "is there anything to do" test.

## When to use
Designing starter quests, daily or weekly objectives, or a story-like chain. Not for: the code (`quest-system-builder`), login rewards (`kit-system-integrator`).

## Inputs (max 2)
1. The systems list and the unlock order (default: `design/progression.md`). 2. Chain type: starter chain, daily board or story (default: starter chain plus daily board).

## Procedure
1. Map systems to teach: list each system in the order a player first needs it (the order from `tutorial-designer`). Each quest step teaches or exercises exactly one.
2. Write each step as an outcome: "Hatch 3 eggs" not "Open the egg menu". Fix its size: starter steps take 30-120 seconds; a daily board's three tasks fit in one 10-15 minute session (the skill's default, vault: completable in a session).
3. Chain structure: step n unlocks step n+1 and rewards something used in n+1 (a currency, an item, a slot). Keep a visible "next quest" on the HUD. Include one step that shows a feature the player has not touched (a surfaced system).
4. Reward the chain: small fixed reward per step, a bigger milestone reward at chain end, and a pointer to what comes next. No hard-currency tasks, no required Robux, no luck-gated steps.
5. Variety and tailoring: vary categories (collect, defeat, explore, social) so the board does not repeat; scale targets with the player's level; allow multi-progress (one action advancing several quests).
6. Always something to do: after the chain ends, hand over to the daily board and the long-term goal; the player never faces an empty quest list.
7. Fail-safes: a stuck quest can be abandoned or rerolled; quests never block movement or gate core play; a skipped step can be completed later.
8. Table: Step, Teaches, Outcome text, Target number, Time estimate, Reward, Unlocks. Save `design/quests.md`; run the doc check.

## Studio MCP path
Design only. After building: `start_stop_play`, drive each step with `execute_luau` (Server) to grant progress, check reward grants in `PlayerData`, and `get_console_output` for errors.

## Fallback
Pure document; times `estimated`.

## Evidence
`core-loops-and-game-design` (quests serve the loop; outcome phrasing; no hard-currency tasks; always something to do, from MonarchDev, indie), `first-session-onboarding` (contextual guidance; one mechanic at a time), `retention-d1-d7` (daily quests as D1 hooks; daily challenge board of three tasks), `updates-live-ops`, `case-studies-blox-fruits` (quest-driven levelling: pattern only).

## Output
`design/quests.md`: chain table, daily board rules, reward ladder, surfaced-feature steps, fail-safes.

## Acceptance checks
- [ ] Each step teaches exactly one system and is phrased as an outcome.
- [ ] Daily board total time is at or under one session.
- [ ] No step needs paid currency, luck, or a notification to progress.
- [ ] Executed: `python gdd-one-pager/scripts/docheck.py design/quests.md --kind quest` prints PASS.

## Pitfalls
Chains that are fetch quests with no teaching. Dailies that take an hour. Rewards that arrive after the player stopped caring. Quest text walls.

## Related
`progression-curve-designer`, `tutorial-designer`, `reward-schedule-designer`, `session-length-designer`, `quest-system-builder`.
