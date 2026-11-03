---
name: crafting-system-builder
description: "Build data-driven crafting with recipes, ingredients consumed at start, a timed queue based on absolute timestamps (offline-safe) and deliveries that never lose output when the inventory is full. Built on the pack Inventory. Use for crafting benches, furnaces, cooking and timers."
category: systems
tags: crafting, recipes, ingredients, queue, timer, furnace, offline, workbench, inventory, data driven
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-grow-a-garden.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/updates-live-ops.md
related: inventory-system-builder, currency-system-builder, quest-system-builder, boost-potion-builder, loot-drop-builder, remote-guard-builder
---

# crafting-system-builder

One job: recipes as data, a bounded queue of timed crafts, ingredients taken when the craft STARTS (so they cannot be traded or crafted twice) and output delivered on collect from absolute `os.time()` stamps, so crafts finish while the player is offline. `scripts/Crafting.luau` is pure logic over `Inventory.luau`.

## When to use
Crafting benches, cooking, smelting, timed production. Not for: instant item conversion without a queue (a one-line `inv:remove` + `inv:add`), farming plots with growth stages (use the timer pattern here but a separate state per plot).

## Inputs (max 2)
1. Recipes: inputs, output, seconds (default: 5 starter recipes, 0-120 s). 2. Queue length and whether time can be skipped with a product (default: 3 slots, no skip).

## Procedure
1. Write `Recipes.luau`. Vault: time-gated production creates return visits and fits scheduled-event pacing, so keep early crafts short (seconds) and make long timers an opt-in for returning players. Never let the output also be an input of the same recipe (the constructor asserts this).
2. Copy `Crafting.luau`; `Crafting.new({ inventory = inv, recipes = Recipes, queueLimit = 3, now = os.time })`.
3. Remotes (rate-limited): `StartCraft(recipeName)` -> `crafting:start(data, name)`; `Collect()` -> `crafting:collect(data)`; both server-only decisions. The client sends the recipe NAME, never ingredients or times.
4. `start` checks the recipe, the queue limit and every ingredient, then removes ingredients (with a refund if any removal fails) and appends `{ recipe, doneAt }`; later items queue behind earlier ones. `collect` delivers finished crafts in order and leaves a craft queued when the output does not fit.
5. Time skips (premium): implement as a developer product through the kit `Shop` whose `grant` moves `doneAt` earlier on the server; do not let the client claim a craft is done.
6. Offline: nothing runs while away; on join call `collect` once and show what finished. Use `os.time()` (wall clock), never `os.clock()`, for stamps that must survive rejoin.
7. Removed recipes: `collect` drops queue entries whose recipe no longer exists; decide whether to refund and write it in the design doc. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/crafting-system-builder/scripts/tests/Crafting.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Recipes.luau` and `Crafting.luau` -> `start_stop_play` -> `execute_luau` (Server) to start two crafts, advance a fake clock or wait, call `collect` and print inventory counts -> `get_console_output` to read the result. A bench UI and proximity prompt are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (bench prompts and UI, offline completion across a real rejoin) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/core-loops-and-game-design.md` (timers and restocks create return visits; cap resources and add sinks), `Roblox/roblox-kb/case-studies-grow-a-garden.md` (time-gated production and shared timers as a retention driver; indie observations), `Roblox/roblox-kb/anti-exploit-and-security.md` (server decides outcomes; validate arguments), `Roblox/roblox-kb/updates-live-ops.md`.

## Output
`Recipes.luau`, `Crafting.luau`, remotes, `design/crafting.md` (recipe table, queue rules, skip policy, removed-recipe policy).

## Acceptance checks
- [ ] Inputs are removed at start and a failed start changes nothing (Crafting tests 1-2).
- [ ] A craft is delivered only after its `doneAt` and only once (test 3).
- [ ] An output that does not fit stays queued (test 4).
- [ ] Bad recipes are rejected at construction (test 5).
- [ ] Crafting Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/crafting-system-builder/scripts/tests/Crafting.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Consuming ingredients at collect time (they can be traded away in between). Using `os.clock` for offline timers. A client-reported completion time. Unbounded queues. Recipes that create items from nothing (output cheaper than inputs by design is fine; output also an input is a loop).

## Related
`inventory-system-builder`, `currency-system-builder`, `quest-system-builder`, `boost-potion-builder`, `loot-drop-builder`.
