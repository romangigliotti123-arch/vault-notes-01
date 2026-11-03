---
name: inventory-system-builder
description: "Build a server-owned slot inventory (stacking, capacity, unique items with uids, atomic add/remove, save-time validation) on the kit's PlayerData, with a client view that only mirrors. Use for any game where players hold items; currency is currency-system-builder, trading is trading-system-builder."
category: systems
tags: inventory, items, slots, stack, capacity, uid, backpack, hotbar, server owned, validate
kb: Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/client-server-and-remotes.md
related: currency-system-builder, trading-system-builder, pet-system-builder, crafting-system-builder, loot-drop-builder, remote-guard-builder, datastore-schema-builder, inventory-ui-builder
---

# inventory-system-builder

One job: the player's items live in `data.Inventory` (inside the PlayerData session), only the server changes them, and every change is all-or-nothing. Stackable items merge up to a stack size; stack-1 items are unique and carry a `uid` so trading, pets and duplicate scans can tell two swords apart. `scripts/Inventory.luau` is pure logic with Lune tests; the client only receives a read-only copy to draw.

## When to use
Adding a backpack, hotbar, storage, equipment or any item list that must survive rejoin and resist duplication. Not for: currency (`currency-system-builder`), Roblox Tools in the character's Backpack (those are instances; this is the saved record behind them), UI layout (`inventory-ui-builder`).

## Inputs (max 2)
1. Item list with stack sizes and which are tradable (default: ask for 5-10 starter items). 2. Slot capacity and how it grows (default: 30, growth by gamepass or upgrade).

## Procedure
1. Write `Items.luau`: `{ Wood = { stack = 99 }, Sword = { stack = 1, tradable = true } }`. Stack 1 means unique with a uid. Decide `tradable` per item now; untradable is the safe default.
2. Install PlayerData if missing and add `Inventory.luau`; construct once: `Inventory.new({ capacity = 30, items = Items, newUid = function() return HttpService:GenerateGUID(false) end })`.
3. Give items only from server code through `inv:add(data, id, qty)`; it returns `ok, reason` and changes nothing when the stack or slot room is missing. Callers must handle `false` (full inventory is a normal answer: show a message, never drop the reward silently).
4. Take items only through `inv:remove(data, id, qty)` or `inv:removeUid(data, uid)`. Never trust a client-sent id, quantity or uid: look the uid up with `inv:findUid`, which only finds items this player owns.
5. Run `inv:validate(data)` on load and before save; any returned problem is logged with the player id and the offending slot is quarantined, not deleted (deleted items cannot be restored).
6. Client view: send a copy `{ slot -> {id, qty} }` over a rate-limited RemoteEvent (see `remote-guard-builder`) after each change; the client never writes. Equip/use actions are requests the server validates (owns it, cooldown, state).
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/inventory-system-builder/scripts/tests/Inventory.test.luau` (quote the "N passed, 0 failed" line) and `luau-check.sh scripts/Inventory.luau`. Add schema migrations through `datastore-schema-builder` when you change item ids later.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Inventory.luau` and `Items.luau` -> `start_stop_play` -> `execute_luau` (Server) to add, overfill and remove items for the test player and print `inv:validate(data)` -> `get_console_output` to read the result. Instance Tools in the Backpack are a separate display layer: untested until run in Studio.

## Fallback
Files + Lune tests only; the DataStore round trip is the kit PlayerData's test. Everything that needs a running Studio session (the Backpack/Tool display layer, a real save and rejoin) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/combat-and-gameplay-systems.md` (show stackable resources as a growing stack with a count; no vault benchmark for stack limits - pick yours and playtest), `Roblox/roblox-kb/anti-exploit-and-security.md` (server decides outcomes; reject quantities <= 0 and fractions; destroy a leaving player's data handles after saving so late remote events cannot mutate items - single creator source, treat as a tip), `Roblox/roblox-kb/data-persistence.md` (versioned, session-locked saves), `Roblox/roblox-kb/client-server-and-remotes.md`.

## Output
`Items.luau`, `Inventory.luau`, a short `design/items.md` (item table, stack sizes, tradable flags, capacity growth), and the client-view remote contract (one table shape).

## Acceptance checks
- [ ] An add that does not fit changes nothing (Inventory test 2).
- [ ] Quantities 0, negative, fractional, NaN and huge are refused (test 3).
- [ ] Unique items have distinct uids and removing one uid never removes another (test 5).
- [ ] `validate` flags unknown ids, overstacked slots and unique items without a uid (test 6).
- [ ] Inventory Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/inventory-system-builder/scripts/tests/Inventory.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Storing item names the client typed. Using the Backpack instances as the source of truth (clients can influence what is parented where). Removing the old id when renaming an item instead of migrating it. Letting a full inventory eat a purchase: for a paid grant, refuse BEFORE charging or hold the item in a claim queue. Giving every item a uid (data bloat): only unique items need one.

## Related
`currency-system-builder`, `trading-system-builder`, `pet-system-builder`, `crafting-system-builder`, `loot-drop-builder`, `datastore-schema-builder`, `remote-guard-builder`.
