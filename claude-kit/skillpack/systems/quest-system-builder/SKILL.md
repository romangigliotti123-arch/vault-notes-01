---
name: quest-system-builder
description: "Build a data-driven quest tracker: server code reports events, quests accumulate capped progress, prerequisites chain them, and rewards are claimed exactly once through the pack Wallet. Save-friendly state. Use for tutorials, daily or story objectives; chain pacing design is quest-chain-designer."
category: systems
tags: quests, objectives, missions, progress, events, claim, reward, chain, tutorial, tracker
kb: Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/updates-live-ops.md
related: quest-chain-designer, currency-system-builder, achievement-badge-builder, first-minute-designer, event-planner, daily-reward-builder
---

# quest-system-builder

One job: turn "the player did X" into quest progress without trusting the client, and pay each reward once. Gameplay code on the server reports events (`collect`, `kill`, `visit`); `scripts/Quests.luau` matches them to available quests, caps progress at the goal and refuses bad amounts. Claiming runs the reward function and sets the claimed flag in the same synchronous step, so a refused reward leaves the quest claimable and a double click pays once.

## When to use
Starter quests, daily or weekly objectives, story steps, tutorials that grant things. Not for: designing WHAT the chain teaches and its pacing (`quest-chain-designer`), badge awarding (`achievement-badge-builder`), the daily login streak (kit `DailyRewards`).

## Inputs (max 2)
1. Quest list: goal event, target, amount, reward, prerequisite (default: 3-5 starter quests that teach the core loop). 2. Reset rules (default: none; dailies are rebuilt each day by deleting their claimed flags).

## Procedure
1. Draft quests so each teaches one verb of the core loop in the order a new player meets it (vault onboarding: reward early actions fast). Write goal events as verbs the server already knows (`collect Wood`, `kill Zombie`).
2. Copy `Quests.luau`; `Quests.new({ defs = Defs })`. A `requires` chain is checked for unknown ids and loops at construction.
3. Report events from the SERVER code that performed the action: `quests:progress(data, "collect", "Wood", n)` right where the wood is granted. Never add a remote like `CompleteQuest`; there is nothing for a client to say.
4. Rewards: `reward = function(data) return wallet:add(data, "Coins", 50, "quest:wood", "quest:wood") end` (idempotent key = quest id) or `inv:add(...)`; return false to refuse (full inventory) and the quest stays claimable.
5. `ClaimQuest(id)` remote (rate-limited) -> `quests:claim(data, id)`; reply with the result string for the UI. `isAvailable` hides locked quests; `value` and goal amount drive the progress bar.
6. State is `data.Quests = { progress, claimed }`, small and serialisable; add the fields to the PlayerData template and a migration if you rename quest ids (`datastore-schema-builder`). For dailies, clear `claimed[id]` and `progress[id]` at the reset boundary on the server.
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/quest-system-builder/scripts/tests/Quests.test.luau` (quote the "N passed, 0 failed" line); add one test per reward that calls `claim` twice and checks the balance.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Defs.luau` and `Quests.luau` -> `start_stop_play` -> `execute_luau` (Server) to report events for the test player, claim, and print `data.Quests` -> `get_console_output` to read the result. Quest UI and world markers are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (UI, event hooks in the real gameplay scripts) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/first-session-onboarding.md` and `Roblox/roblox-kb/retention-d1-d7.md` (early guided rewards support first-session and D1 retention; thresholds are creator-reported), `Roblox/roblox-kb/core-loops-and-game-design.md`, `Roblox/roblox-kb/updates-live-ops.md` (recurring objectives as a live-ops tool).

## Output
`Defs.luau`, `Quests.luau`, the claim remote, `design/quests.md` (table of goal, reward, prerequisite, reset rule).

## Acceptance checks
- [ ] Only matching events advance a quest and progress caps at the goal (Quests test 1).
- [ ] Bad event amounts are ignored (test 2).
- [ ] A reward is paid once even if `claim` is called twice (test 3).
- [ ] A refused reward leaves the quest claimable (test 5).
- [ ] Chains with unknown or looping prerequisites fail at construction (test 6).
- [ ] Quests Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/quest-system-builder/scripts/tests/Quests.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Letting the client report progress. Marking claimed before the reward succeeds. Progress that counts events from before the quest was available (the module ignores unavailable quests on purpose). Reward values hard-coded in several places. Quest ids renamed without a migration.

## Related
`quest-chain-designer`, `currency-system-builder`, `achievement-badge-builder`, `first-minute-designer`, `event-planner`.
