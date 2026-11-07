---
name: upgrade-tree-builder
description: "Build a data-driven upgrade tree with prerequisites, per-level cost growth, max levels, cycle detection and a respec that refunds less than 100%, paid through the pack Wallet. Use for permanent upgrades; resetting progress is rebirth-system-builder."
category: systems
tags: upgrades, skill tree, prerequisites, levels, respec, refund, cost growth, progression, wallet
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-simulator-genre-notes.md, Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: currency-system-builder, rebirth-system-builder, pet-system-builder, core-loop-designer, price-ladder-planner
---

# upgrade-tree-builder

One job: permanent upgrades the player buys with a currency, with prerequisites and rising costs, validated on the server. `scripts/UpgradeTree.luau` rejects trees with unknown or unreachable prerequisites and cycles at construction, charges through the Wallet, and `respec` refunds a floored share (default 80%) so re-planning costs something and never creates currency.

## When to use
Upgrade menus, skill trees, tycoon upgrades. Not for: temporary effects (`boost-potion-builder`), prestige resets (`rebirth-system-builder`), Robux-priced unlocks (`gamepass-maker`/`devproduct-handler`).

## Inputs (max 2)
1. Nodes: id, base cost, growth, max level, prerequisites (default: 6-10 nodes in 2 branches). 2. Respec policy (default: free of Robux, 80% refund).

## Procedure
1. List each upgrade with the stat it changes and the SERVER formula that uses its level (`speed = 16 + 2 * level`). An upgrade nothing reads is dead content; cut it.
2. Set costs: `cost * growth^level`, with growth between 1.1 and 2 as a starting range (an assumption, not a vault number); check the total cost to max each branch against the expected earn rate and rebirth cadence.
3. Copy `UpgradeTree.luau`; `UpgradeTree.new({ wallet, currency, refund = 0.8, nodes })`. Construction asserts unknown prerequisites, prerequisite levels above the node's max, cycles, and a refund outside 0..1.
4. Remote `BuyUpgrade(id)` (rate-limited): `tree:buy(data, id)` returns `ok, reason` (`max level`, `requires speed`, `cannot afford`). The price comes from the server table, never the client.
5. Read levels where stats are computed: `tree:level(data, "speed")` on the server each time the stat is needed (or cache and invalidate on buy).
6. Respec: confirm in the UI, call `tree:respec(data)`; it returns the refund added through the wallet under the sink/source name `respec`. Floor refunds so repeated respecs cannot mint currency; test this with a loop.
7. Run `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/upgrade-tree-builder/scripts/tests/UpgradeTree.test.luau` (quote the "N passed, 0 failed" line); add a test that buying every node in dependency order reaches the expected total spend.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Nodes.luau` and `UpgradeTree.luau` -> `start_stop_play` -> `execute_luau` (Server) to buy a chain of upgrades with a funded test player and print levels and balance -> `get_console_output` to read the result. Tree UI is Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (UI, stat formulas in the real gameplay scripts) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/core-loops-and-game-design.md` (upgrades as currency sinks that keep collect-sell-upgrade loops going; scale costs; demo numbers are tunable), `Roblox/roblox-kb/case-studies-simulator-genre-notes.md`, `Roblox/roblox-kb/player-psychology-and-game-feel.md` (visible progress), `Roblox/roblox-kb/anti-exploit-and-security.md` (server prices).

## Output
`Nodes.luau`, `UpgradeTree.luau`, the buy and respec remotes, `design/upgrades.md` (node table, cost-to-max per branch, respec policy).

## Acceptance checks
- [ ] Prerequisites and max level are enforced (UpgradeTree test 2); cannot-afford changes nothing (test 3).
- [ ] Respec refunds a floored share and total currency never increases across buy/respec loops (test 4).
- [ ] Cycles, unknown and unreachable prerequisites fail at construction (test 5).
- [ ] Every node's level is read by a server formula (grep).
- [ ] UpgradeTree Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/upgrade-tree-builder/scripts/tests/UpgradeTree.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Costs read from the client. Respec at 100% (free rearranging removes commitment) or above (mints currency). Prerequisite chains so long that early players see a wall of locked nodes. Changing node ids after launch without migrating saved levels.

## Related
`currency-system-builder`, `rebirth-system-builder`, `pet-system-builder`, `core-loop-designer`, `price-ladder-planner`.
