---
name: loot-drop-builder
description: "Build weighted loot, egg-hatch and crate rolls with a server-side roll, pity counter, luck that never touches the base rarity, an odds table computed from the same weights, a drop log and the paid-random disclosure checklist. Covers eggs and crates; pets after hatching are pet-system-builder."
category: systems
tags: loot, drops, egg, hatch, crate, gacha, weighted random, pity, odds, rarity, luck, paid random
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/combat-and-gameplay-systems.md
related: pet-system-builder, inventory-system-builder, boost-potion-builder, devproduct-handler, age-rating-prep, paid-random-compliance, currency-system-builder
---

# loot-drop-builder

One job: roll items on the server with odds the player can see, a pity guarantee and a log, for loot drops, eggs and crates alike (the planned egg-hatch skill is merged here: same roll, different presentation). `scripts/LootTable.luau` takes an injected random function, so tests use fixed sequences and one test checks 20000 seeded rolls against the stated odds. Luck multiplies non-base weights only and is capped.

## When to use
Enemy drops, chests, eggs, crates, spin wheels, any random reward. Not for: where the item goes afterwards (`inventory-system-builder`, `pet-system-builder`), deciding whether random paid items fit your audience and rules (`paid-random-compliance` and the checklist below), loot placement in the world.

## Inputs (max 2)
1. Table entries with weights and rarities (default: 3 rarities, odds like 70/25/5 as a starting point). 2. Is it free, earned with currency, or bought with Robux? (changes the compliance steps).

## Procedure
1. Write each table as data: `{ id, weight, rarity }`. Odds shown to players are `loot:odds()` from the SAME weights; never hand-write a second odds list. The constructor rejects empty tables, non-positive weights, duplicate ids and a pity rarity with no entry.
2. Roll on the server only: `loot:roll(data, luck)` with `rng = function() return Random.new():NextNumber() end` (one `Random` per server, not per call). The client sends 'open egg 3' at most; the result, animation target and the item all come from the server.
3. Pity: `pity = { rarity = "legendary", every = 50 }` forces the top rarity on the Nth miss and resets on any natural hit. Vault: add pity and fair rates; pity thresholds quoted by indie creators vary (30 in a demo, about 500 mentioned) and have no verified top-game numbers, so pick yours and playtest.
4. Luck: server-side boost value from `boost-potion-builder` or a pass, bounded 1..100 by the module; it multiplies every non-common entry equally. Do not make odds worse for loyal or high-spending players (vault: criticised as unfair).
5. Paid random (Robux or a currency bought with Robux): show all outcomes and numeric odds before spending, including indirect purchases such as keys, gate the feature by the player's region policy (PolicyService - live-check), keep odds independent of spend, and name each item's acquisition route (vault). Refuse the roll BEFORE charging when the inventory is full, and never silently swap duplicates.
6. Log every roll through the `log` callback (table, id, rarity, luck, pity-forced) to your analytics so you can compare real drop rates to stated odds weekly; investigate any gap.
7. Presentation (egg shake, reveal) is client-side AFTER the server result arrives; hide rarity until the reveal if you like, but the odds table stays visible. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/loot-drop-builder/scripts/tests/LootTable.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `LootTable.luau` and the table definitions -> `start_stop_play` -> `execute_luau` (Server) to roll 1000 times for a test player and print the counts next to `loot:odds()` -> `get_console_output` to read the result. Egg animations and the store-page odds panel are Studio/UI work: `untested` here.

## Fallback
Files + Lune tests, including the seeded 20000-roll frequency check. Everything that needs a running Studio session (animations, the in-game odds UI, regional policy gating) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` (random paid items: disclose odds, gate via PolicyService, treat as optional and risky; add pity and fair rates; never worsen odds for big spenders; state how each cosmetic is obtained; do not silently swap duplicates), `Roblox/roblox-kb/core-loops-and-game-design.md` (show '1 in X' odds, config in one module, luck modifiers and pity; verified top-game drop and pity numbers are missing, indie figures are unverified), `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (simulated gambling is banned; paid random generators remain allowed only if they follow the rules - live-check), `Roblox/roblox-kb/combat-and-gameplay-systems.md` (drop at the death position, despawn uncollected drops with a lifetime).

## Output
`LootTables.luau` (data), `LootTable.luau`, roll remote, odds panel data, `design/loot.md` (tables, odds, pity, luck sources, disclosure checklist ticked).

## Acceptance checks
- [ ] Odds sum to 100 and equal the weights used by the roll (LootTable test 1).
- [ ] Pity forces the top rarity exactly on the Nth roll and resets (tests 3-4).
- [ ] 20000 seeded rolls land near stated odds (test 8: quote it).
- [ ] Luck is bounded and leaves the base rarity alone (test 5); rng outside [0,1) fails (test 6).
- [ ] For paid rolls: the disclosure checklist in step 5 is ticked in the design doc.
- [ ] LootTable Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/loot-drop-builder/scripts/tests/LootTable.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
A client-supplied roll, luck or result. One `Random.new()` per call (repeated seeds). Showing different odds than the roll uses. Pity counters stored only in memory (lost on rejoin: it lives in `data.Loot`). Luck that scales the common item too, which makes it a no-op. Treating a pity threshold from a video as verified.

## Related
`pet-system-builder`, `inventory-system-builder`, `boost-potion-builder`, `devproduct-handler`, `age-rating-prep`, `paid-random-compliance`.
