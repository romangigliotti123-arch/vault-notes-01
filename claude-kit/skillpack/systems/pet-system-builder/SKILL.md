---
name: pet-system-builder
description: "Plan and wire pets on the pack Inventory: equip slots, server-side power with boost multipliers, deterministic fusing into higher tiers and an equipped-lock for trading. No paid randomness (that is loot-drop-builder). Use for pet, companion or collectible games."
category: systems
tags: pets, companions, equip, fuse, evolve, power, rarity, collection, simulator, inventory
kb: Roblox/roblox-kb/case-studies-pet-simulator-99.md, Roblox/roblox-kb/case-studies-simulator-genre-notes.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/monetisation-other.md
related: inventory-system-builder, loot-drop-builder, trading-system-builder, boost-potion-builder, rebirth-system-builder, currency-system-builder
---

# pet-system-builder

One job: pets as unique inventory items with an equip limit, a power number the SERVER computes, and a deterministic fuse path to higher tiers. Acquisition (eggs, rolls, pity) is `loot-drop-builder`; this skill starts when the player owns a pet. `scripts/Pets.luau` sits on top of `Inventory.luau` and exposes `locked` for `Trade`.

## When to use
Pet simulators, companion systems, any collection where owned creatures boost earnings. Not for: hatching odds (`loot-drop-builder`), pet AI/following animation, pet marketplaces (`trading-system-builder`).

## Inputs (max 2)
1. Pet list: id, tier, power, next tier (default: 3 tiers, 3 pets per tier). 2. Equip slots and how they grow (default: 3, +1 by upgrade or pass).

## Procedure
1. Write `PetDefs.luau`: `{ Dog = { power = 10, next = "GoldDog" }, GoldDog = { power = 40 } }` and register every pet as a stack-1, tradable item in `Items.luau` so each owned pet has a uid.
2. Vault pattern: a simulator pet system is a progression ladder (more and rarer pets multiply earnings). Choose the power curve so a fused tier-2 pet beats three tier-1 pets by a visible margin but not so far that tier 1 is dead on arrival; write the curve in the design doc and mark it as a first guess to tune from playtest data.
3. Copy `Pets.luau`; `Pets.new({ inventory = inv, defs = PetDefs, equipLimit = 3, fuseCount = 3 })` asserts that every `next` exists and does not point to itself.
4. Remotes (rate-limited): `EquipPet(uid)`, `UnequipPet(uid)`, `FusePet(petId)`. The server calls `pets:equip(data, uid)` / `unequip` / `fuse`. Power for earnings is `pets:power(data, boosts:multiplier(data, "coins"))` computed on the server at the moment of earning; the client never sends power.
5. Wire the trade lock: `Trade.new({ ..., locked = function(data, uid) return pets:locked(data, uid) end })`. Unequip happens automatically when a pet leaves the inventory (`init` prunes missing uids on every call).
6. Inventory limits: a full pet inventory must refuse new pets BEFORE a paid hatch charges (see `loot-drop-builder` step on refusing early). Add a clear message and a sell/fuse path.
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/pet-system-builder/scripts/tests/Pets.test.luau` (quote the "N passed, 0 failed" line); check that fuse leaves equipped pets alone and never loses pets when the output cannot be added (test 3).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `PetDefs.luau`, `Pets.luau` and the three remotes -> `start_stop_play` -> `execute_luau` (Server) to grant three pets, equip two, fuse, and print `pets:power(data)` -> `get_console_output` to read the result. Following/animation of pet models is separate Studio work and `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (pet model following, UI, the earnings loop reading `power`) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/case-studies-pet-simulator-99.md` and `case-studies-simulator-genre-notes.md` (pet collection and multiplier loops in top simulators; indie numbers are indie), `Roblox/roblox-kb/core-loops-and-game-design.md` (cap inventories and add sinks so collections have somewhere to go), `Roblox/roblox-kb/monetisation-other.md` (random paid pet acquisition needs odds disclosure and pity; keep odds independent of spend).

## Output
`PetDefs.luau`, `Pets.luau` wired to remotes, `design/pets.md` (tiers, power curve, equip growth, fuse rule, what is tradable).

## Acceptance checks
- [ ] Equip never exceeds the slot limit and rejects uids the player does not own (test 1).
- [ ] Power is computed from server data only and scales with the server multiplier (test 2).
- [ ] Fuse consumes exactly `fuseCount` unequipped pets and is all-or-nothing (test 3).
- [ ] Equipped pets are locked for trading (test 5).
- [ ] Pets Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/pet-system-builder/scripts/tests/Pets.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Sending power or multiplier from the client. Fusing equipped pets. Random fusing that is really a paid gamble (disclosure rules apply). Pet defs removed in an update while players own them (migrate, do not delete). Exponential power with no sinks, which collapses the economy. Per-pet model instances with scripts: use one controller for all pets.

## Related
`inventory-system-builder`, `loot-drop-builder`, `trading-system-builder`, `boost-potion-builder`, `rebirth-system-builder`.
