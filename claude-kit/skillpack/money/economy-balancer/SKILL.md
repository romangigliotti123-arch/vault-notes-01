---
name: economy-balancer
description: "Balance a game's soft currency by listing sources and sinks, simulating an average player's balance hour by hour, and tuning until it neither inflates nor starves; ties paid currency packs and boosts to the same model. Use when numbers feel wrong or before adding any currency source; mapping real data is sink-source-mapper."
category: money
tags: economy, currency, sources, sinks, inflation, balance, simulation, caps, soft currency, event currency
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/retention-d1-d7.md
related: sink-source-mapper, devproduct-handler, vip-pass-designer, limited-offer-designer, core-loop-designer, datastore-schema-builder
---

# economy-balancer

One job: find out, before shipping, whether your currency numbers hold together. The vault's rule is "keep sources minus sinks near zero": add sinks when wallets grow, cap resources and inventories, set a daily reward cap, scale conversion cost with level, use a separate event currency, and compute expected value per action. This skill turns that into a simulation (`scripts/Economy.luau`) fed by YOUR assumed rates; the output is a model, never a measurement. Real data goes through `sink-source-mapper`.

## When to use
Designing or changing currency amounts, adding a new source (quest, drop, daily), adding currency packs or boosts, or when players complain of boredom (too slow) or nothing to buy (too much). Not for: pricing Robux items (`price-ladder-planner`), reading logged data (`sink-source-mapper`).

## Inputs (max 3)
1. Every currency source and sink with a per-hour estimate for a typical active player (default: read the code and `design/core-loop.md`, then ask for gaps). 2. Session shape: hours per day for casual and committed players (default: 0.5 and 3). 3. The price points of the main goals (default: the shop's list).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section core-loops-and-game-design rules --max-chars 4000` (find "Balance the economy with sources, sinks and caps") and the event-currency rule in `monetisation-other`.
2. List sources and sinks in a table: name, per-hour amount at typical play, capped (yes/no), who is affected (all or payers). Flag any source with no cap and any sink only payers use.
3. Simulate: in a Lune script call `Economy.simulate({ sources = ..., sinks = ..., hours = 20, startBalance = 0 })` for casual and committed players. Read `verdict`: `inflating` (spent is below 60% of income, a default to tune), `starved` (more than 30% of demand unmet) or `balanced`.
4. Check goal timing: `Economy.hoursToEarn(price, incomePerHour)` for each major goal. Casual players should reach the first goal within the first sessions (see `first-minute-designer`); the last goal should take long enough to last a season.
5. Fix in this order: add or strengthen sinks that players WANT (cosmetic upgrades, storage, crafting), cap runaway sources, add a daily cap, then adjust prices. Do not fix inflation by selling currency faster or making paid boosters stack without limit (`vip-pass-designer`).
6. Re-run the simulation after each change and keep a table of before/after.
7. Paid currency: list every developer product that grants currency and run the same simulation with the pack bought once per day; if the pack grants more than a day of committed play, buyers skip the game and lifetime value drops.
8. Plan the real measurement: log every grant and spend with the Analytics system (`Analytics:Economy` with Source/Sink flows) so `sink-source-mapper` can compare the model with reality after launch.
9. Test: `lune run ../skillpack/money/economy-balancer/scripts/tests/Economy.test.luau` from `.rbx/claude-kit/systems`.

## Studio MCP path
Maths needs no Studio. To read real values from a place: `list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) to print reward constants from your config module -> `get_console_output`. Whether the numbers FEEL right is a play test: `untested`.

## Fallback
Lune script and a spreadsheet; the model is fully headless. Real player behaviour stays `untested` until data exists.

## Evidence
`Roblox/roblox-kb/core-loops-and-game-design.md` (sources, sinks, caps; storage cap as a paid sink, tunable numbers), `Roblox/roblox-kb/monetisation-other.md` (event currency so hoarders cannot buy out event content; keep an in-game currency), `Roblox/roblox-kb/pricing.md` (one creator reports LTV lifts of up to about 20% and 10% from sources/sinks and difficulty tuning, GameMakers 2022, self-reported), `Roblox/roblox-kb/analytics-metrics.md` (source/sink flow events). Thresholds 0.6 and 0.3 are this skill's defaults.

## Output
`design/economy.md`: sources and sinks table, simulation results for casual and committed players, goal timing table, changes with before/after, logging plan; code `Economy.luau` kept with the tests.

## Acceptance checks
- [ ] Every source and sink in the code appears in the table (search for balance-changing functions and tick them off).
- [ ] `Economy.simulate` verdict is `balanced` for both player types, or the design explains the intended exception.
- [ ] `lune run` Economy tests pass (quote "7 passed, 0 failed") and luau-check is clean.
- [ ] Every number is labelled "assumed" or "measured".
- [ ] A logging plan exists for validating the model with real data.

## Pitfalls
Treating the simulation as truth. Fixing inflation by nerfing rewards instead of adding wanted sinks. Letting paid packs outpace play. Forgetting offline or AFK sources. Many currencies that nobody tracks.

## Related
`sink-source-mapper`, `devproduct-handler`, `vip-pass-designer`, `limited-offer-designer`, `core-loop-designer`.
