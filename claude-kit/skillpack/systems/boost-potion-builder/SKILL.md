---
name: boost-potion-builder
description: "Build timed boosts (potions, 2x events) that persist across sessions with absolute expiry stamps, extend when re-granted, stack by an explicit per-group rule (add or best-of) with caps, and feed a HUD. Use for luck/xp/coin boosts; selling them is devproduct-handler."
category: systems
tags: boost, potion, buff, timer, multiplier, stacking, cap, expiry, hud, persistence
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/monetisation-devproducts.md, Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/updates-live-ops.md
related: devproduct-handler, loot-drop-builder, pet-system-builder, rebirth-system-builder, crafting-system-builder, event-planner
---

# boost-potion-builder

One job: temporary multipliers with a stated stacking rule, a cap and a lifetime that survives leaving the game. `scripts/Boosts.luau` stores `name -> expiry` (absolute `os.time()`), so time spent offline counts exactly as the design says; granting the same boost again extends it up to `maxSeconds`; boosts in one group combine by `add` (1 + sum of bonuses) or `max`; groups never combine with each other; the group cap bounds the total.

## When to use
Luck/XP/coin potions, event boosts, premium timed perks. Not for: permanent perks (`gamepass-maker`), the purchase handler (`devproduct-handler`; it calls `boosts:grant` in its `grant`), global server-wide events (`event-planner`).

## Inputs (max 2)
1. Boost list: group, multiplier, seconds, max stack time (default: luck/xp/coins groups, 10 min potions, 1 h max). 2. Stacking rule per group (default: `add` with a cap of 5x).

## Procedure
1. Write the stacking table first: for each group choose `add` or `max`, the cap, and what happens when the same boost is drunk twice (extend). Vault: single XP/coin boosters make poor gamepasses because they cap spend; as timed consumables they suit developer products.
2. Copy `Boosts.luau`; `Boosts.new({ now = os.time, defs, groups })`; it rejects multipliers <= 1, max time below base time and unknown groups.
3. Grant from server code only: potion item used (`inv:remove` then `boosts:grant(data, name)` - remove first, grant second, same synchronous step), Shop product `grant`, or an event script. Never from a remote that names the boost.
4. Apply where values are computed: `earn = base * boosts:multiplier(data, "coins") * rebirth:multiplier(data)`; write the cross-system combine rule (multiply across systems, add within a group) so nobody invents a new one per feature.
5. State is `data.Boosts = { [name] = expiresAt }`; `init` drops expired and unknown entries on every call, so removing a boost in an update is safe. Add `data.Boosts` to the PlayerData template.
6. HUD: send `boosts:active(data)` (name, seconds left, mult) after each change and every 30 s; the client counts down locally and the server stays the authority. Server-wide boosts: a separate table in a MemoryStore/Attribute, not per player.
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/boost-potion-builder/scripts/tests/Boosts.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Boosts.luau` and the potion handler -> `start_stop_play` -> `execute_luau` (Server) to grant two boosts to the test player, print `boosts:multiplier` and `boosts:active` -> `get_console_output` to read the result. HUD and potion tools are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (HUD, real offline expiry across a rejoin) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/monetisation-gamepasses.md` (avoid single XP/coin boosters as passes because they cap spend), `Roblox/roblox-kb/monetisation-devproducts.md` (repeatable consumables fit developer products), `Roblox/roblox-kb/core-loops-and-game-design.md` (timers and scheduled boosts create urgency; indie-labelled), `Roblox/roblox-kb/updates-live-ops.md`.

## Output
`Boosts.luau`, boost and group tables, grant paths, HUD payload shape, `design/boosts.md` (stacking table and cross-system combine rule).

## Acceptance checks
- [ ] Expiry removes the multiplier at the exact second (Boosts test 1).
- [ ] Re-granting extends up to the max and no further (test 2).
- [ ] `add` groups respect the cap and `max` groups take the best (test 3).
- [ ] Saved boosts expire correctly after offline time and unknown names are dropped (test 4).
- [ ] Boosts Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/boost-potion-builder/scripts/tests/Boosts.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Using `os.clock()` for stamps (resets per server). Granting before removing the potion item (duplicate on crash) or the reverse without a transaction (lost potion): do both in one synchronous step and save. Uncapped stacking multiplied across systems. Client-side countdown treated as truth.

## Related
`devproduct-handler`, `loot-drop-builder`, `pet-system-builder`, `rebirth-system-builder`, `event-planner`.
