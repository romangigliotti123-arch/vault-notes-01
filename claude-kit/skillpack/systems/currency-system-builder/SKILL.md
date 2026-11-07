---
name: currency-system-builder
description: "Design a game's currencies (sources, sinks, caps) and wire a server-authoritative multi-currency wallet into the kit's PlayerData and Shop, with idempotent grants for Robux packs and a sources-minus-sinks report. Use when adding coins, gems or any spendable number; item storage is inventory-system-builder."
category: systems
tags: currency, wallet, coins, gems, economy, sources, sinks, cap, balance, idempotent, server authority
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/monetisation-devproducts.md
related: inventory-system-builder, trading-system-builder, devproduct-handler, rebirth-system-builder, datastore-schema-builder, remote-guard-builder, rbx-datastore
---

# currency-system-builder

One job: every spendable number lives in one server-owned wallet inside the player's saved data, changes only through `add` and `spend`, and every change is an integer, bounded, named by its source or sink and optionally keyed so a retry cannot pay twice. Saving is the kit's `PlayerData`; Robux purchases are the kit's `Shop` (its `ProcessReceipt` records the receipt in the same data table before answering). This skill designs the economy and supplies `scripts/Wallet.luau`, which plugs into both.

## When to use
Adding the first currency, a second currency, a cap, a currency pack, or fixing an economy where numbers go negative, overflow or double-pay. Not for: item stacks and slots (`inventory-system-builder`), what to charge in Robux (`price-ladder-planner`), the purchase handler itself (`devproduct-handler`).

## Inputs (max 2)
1. Game loop and where the player earns and spends (default: `design/core-loop.md`). 2. Currencies wanted (default: one soft currency + one premium currency bought with Robux).

## Procedure
1. List every currency with its role: soft (earned constantly), premium (bought, scarce), event (expires). Vault rule: keep sources minus sinks near zero over the whole player base; add sinks when wallets grow or a resource goes unspent, and cap resources. Stop when each currency has at least two sources and two sinks written down.
2. Write the source and sink table (name, amount or formula, frequency, who triggers it). Source names become the `source` argument, sink names the `sink` argument, so the report in step 6 matches the design.
3. Copy `scripts/Wallet.luau` next to the PlayerData system (`python .rbx/claude-kit/tools/games.py system add PlayerData --project <project>` if missing) and create `Currencies.luau`: `Wallet.new({ currencies = { Coins = { max = 1e9 }, Gems = {} } })`. A cap is a design choice (storage-style sink); say why in the design doc.
4. Route every change through `wallet:add(data, name, amount, source, key)` and `wallet:spend(data, name, amount, sink, key)` where `data` is `session.Data`. Never write `data.Coins += n` anywhere else. Rewards that can be retried (quest claims, Robux packs) pass a key: for Shop products use the receipt `PurchaseId`, so `Shop` and the wallet are both idempotent.
5. Robux packs: in the Shop product `grant(userId, data)` call `wallet:add(data, "Gems", 100, "robux:Gems100", tostring(purchaseId))`. Shop already saves before answering `Granted`; do not add a second `ProcessReceipt`.
6. Spending flows (shop, upgrade, rebirth, trade) call `spend` on the server after checking the price from a server table; the client sends an item NAME only. Reject amounts that are not positive integers (the wallet does this for you).
7. In a test session print `wallet:report(data)` and compare sources and sinks to step 1; fix the design when one currency only goes up. `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/currency-system-builder/scripts/tests/Wallet.test.luau` (quote the "N passed, 0 failed" line).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Wallet.luau` and `Currencies.luau` under ServerScriptService -> `start_stop_play` -> `execute_luau` (Server) to join a test player, call `wallet:add`/`spend` with good and bad amounts through the real session data and print `wallet:report(data)` -> `get_console_output` to read the result. The Robux path needs a published place and a test purchase: `untested` until the owner buys once with a test account.

## Fallback
Files + Lune tests (headless): the suite includes a real `Shop` receipt retried twice that pays once. Everything that needs a running Studio session (a real purchase, DataStore round trip) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/core-loops-and-game-design.md` (keep sources minus sinks near zero; add sinks when wallets grow; cap resources; storage cap as gold sink - demo numbers are tunable), `Roblox/roblox-kb/anti-exploit-and-security.md` (reject amounts <= 0 and floor fractions on the server; never accept a price from the client; do not hand out hard currency freely - it floods secondary markets), `Roblox/roblox-kb/data-persistence.md`, `Roblox/roblox-kb/monetisation-devproducts.md`. Shop guarantees: `systems/Shop/README.md`.

## Output
`design/economy.md` (currency table, source/sink table, caps, why), code `Currencies.luau` + `Wallet.luau`, product grants calling the wallet, `tests/Wallet.test.luau` copy if the project has its own test folder.

## Acceptance checks
- [ ] No code outside the wallet writes a balance (grep for `.Coins`/`.Gems` assignments finds none).
- [ ] Negative, zero, fractional, NaN and oversized amounts are refused (Wallet test 2 covers it).
- [ ] A retried Robux grant with the same key pays once (Wallet test 8 runs the real Shop).
- [ ] Every currency has at least two sources and two sinks in the design doc.
- [ ] Wallet Lune tests pass: `cd .rbx/claude-kit/systems && lune run ../skillpack/systems/currency-system-builder/scripts/tests/Wallet.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Clamping silently on overflow without telling the player (the wallet returns `capped`; show it). Using floats for money. One shared key namespace: prefix keys with the system (`quest:`, `robux:`). Letting an admin or test command bypass the wallet. Premium currency that can also be earned freely in bulk (vault: freely handed hard currency floods markets). The key list is bounded (default 200): keys must be unique per grant, not reused across days.

## Related
`inventory-system-builder`, `trading-system-builder`, `rebirth-system-builder`, `upgrade-tree-builder`, `devproduct-handler`, `datastore-schema-builder`, `rbx-datastore`.
