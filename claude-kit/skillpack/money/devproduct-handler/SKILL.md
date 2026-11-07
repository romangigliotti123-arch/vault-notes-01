---
name: devproduct-handler
description: "Define a game's developer-product catalogue (what each repeatable purchase grants, price tier, when it is offered), wire it into the kit's Shop system - which already owns an idempotent ProcessReceipt - and verify every grant offline with fixtures before real Robux touch it. Use when adding currency packs, boosts, revives or offers."
category: money
tags: developer product, processreceipt, purchase, receipt, robux, idempotent, currency pack, boost, shop, grant, catalogue
kb: Roblox/roblox-kb/monetisation-devproducts.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md, Roblox/roblox-kb/pricing.md
related: gamepass-maker, datastore-schema-builder, price-ladder-planner, starter-pack-designer, offer-timing-planner, receipt-flow-tester, purchase-flow-tester, kit-system-integrator
---

# devproduct-handler

The hard part of developer products, a correct `ProcessReceipt`, is already solved and unit-tested in the kit system `Shop` (`.rbx/claude-kit/systems/Shop`, 13 Lune tests; NOT live-tested in Studio): it grants once per `PurchaseId`, stores the id in the same data as the reward, saves before confirming, defers re-entrant receipts, prunes old ids. Do not write a second handler: a game has exactly one `ProcessReceipt`. This skill decides WHAT to sell, builds the catalogue Shop consumes and proves every grant function offline.

## When to use
Any repeatable purchase. Not for: one-time perks (`gamepass-maker`), subscriptions, UGC sales, or replacing the Shop system.

## Inputs (max 3)
1. The products: what each gives and its price tier (default: ask for the pain points in `design/core-loop.md`). 2. The save system (default: kit `PlayerData`; its template must include `Receipts = {}`). 3. Product ids if they exist (default: `0` = SET IN CREATOR HUB; entries with id 0 are skipped with a note).

## Procedure
1. Choose products from needs, not from a price list (vault: best sellers solve a pain players already feel: grinding, waiting, being stuck, missing out; offer the exact amount needed when a player cannot afford something; first purchase matters most; a cheap starter pack after the first milestone, about 20-60 minutes in, never in the first 30 seconds). Convert repeatable value into consumables. Price on a ladder (`price-ladder-planner`). Reject anything that is pay-to-win in competitive modes, paid randomness, or sold as a rescue from a loss the design caused.
2. Install the kit systems if missing: `python .rbx/claude-kit/tools/games.py system add PlayerData --project <project>` and `... system add Shop --project <project>`. Put `Receipts = {}` in the PlayerData template (`datastore-schema-builder`).
3. Write the catalogue: copy `scripts/Catalogue.luau` next to `ShopService` and create `Products.luau` returning a list of entries `{ name, id, grant, refuseWith? }`. Rules for `grant(userId, data)`: synchronous and fast (no yields that can fail halfway), mutate only the loaded `data` table, return `true` only when applied, return `false` BEFORE changing anything when it cannot apply (inventory full, cap reached; give `refuseWith` data to prove it).
4. Start the shop once on the server:
   ```lua
   local products, notes = Catalogue.build(require(script.Parent.Products))
   for _, n in notes do warn(n) end
   ShopService.Start({ products = products, getData = ..., saveNow = ... })
   ```
   The client sends only a NAME to the Shop prompt remote (`ShopRequest:FireServer("product", "Coins100")`); ids and prices stay on the server. Update UI from server state after the grant, not from the prompt-finished event.
5. Verify offline (this is the new value): write `tests/Products.test.luau` that calls `Catalogue.verify(entries, PlayerDataTemplate)` and asserts `{}` (flags a grant that throws, does not return true, changes nothing, leaves unsaveable values, or changes data and then refuses), plus one end-to-end case through the real `Shop.new(...)` with a duplicate `PurchaseId`. Pattern: `scripts/tests/Catalogue.test.luau`. Run from `.rbx/claude-kit/systems`: `lune run ../skillpack/money/devproduct-handler/scripts/tests/Catalogue.test.luau` and `lune run ../skillpack/<your test path>`; static checks with `bash .rbx/claude-kit/tools/roblox-project-template/luau-check.sh <files>`.
6. Decide and write down the edge cases: purchase while data is loading (Shop answers `NotProcessedYet`, Roblox retries), purchase right before leaving, refunds (not undone automatically: log), unknown product ids retry forever so keep the Creator Hub list in sync with `products`.
7. Write the Creator Hub checklist for the owner: create each product, set name/icon/price, check regional pricing, copy the id into `Products.luau`, test with a test account on a PUBLISHED test place. You never create, price or publish products.

## Studio MCP path
`list_roblox_studios` -> `multi_edit` to add `Catalogue.luau` and `Products.luau` -> `start_stop_play` -> `execute_luau` (Server) calling the pure grant functions on a copy of the live data (never fire real receipts) -> `get_console_output` for the id-0 notes. Real prompts and receipts need a published place and are `untested` until the owner runs them.

## Fallback
Rojo files + Lune tests (headless). The purchase flow is the owner's test.

## Evidence
`Roblox/roblox-kb/monetisation-devproducts.md` (products for repeatables; first purchase; starter pack timing; offers at the moment of need; many shop entry points), `Roblox/roblox-kb/scripting-and-performance.md` (ProcessReceipt on the server, idempotent), `Roblox/roblox-kb/data-persistence.md`, `Roblox/roblox-kb/_tools/CHECKLIST-monetization.md`, `Roblox/roblox-kb/pricing.md`. Shop's guarantees and tests: `systems/Shop/README.md`. Receipt API details: Creator Docs (`kbq.py docs "ProcessReceipt"`).

## Output
`src/server/Systems/Shop/Catalogue.luau`, `Products.luau`, `tests/Products.test.luau`, `design/products.md` (product, id placeholder, grant, tier, trigger moment, refuse case), test output quoted, the Creator Hub checklist.

## Acceptance checks
- [ ] Exactly one `ProcessReceipt` owner in the project (`grep -rn "ProcessReceipt" src` shows only Shop).
- [ ] `Catalogue.verify` returns `{}` for every product (output quoted); each capped grant has a `refuseWith` case.
- [ ] End-to-end duplicate-PurchaseId test through the real Shop passes.
- [ ] No client-sent prices or amounts are used anywhere.
- [ ] Ids are `0` placeholders unless the owner supplied them.
- [ ] luau-check clean; no pay-to-win or paid-randomness grants.
- [ ] One server-side `ProcessReceipt` returns `PurchaseGranted` only after the grant is saved; `PromptProductPurchaseFinished` never grants; prices are read from MarketplaceService, not hard-coded (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, monetisation-devproducts).

## Pitfalls
Writing a second ProcessReceipt. A grant that yields or can fail after changing data. Selling a rescue from a loss the design caused. Forgetting `Receipts = {}` in the template (Shop answers NotProcessedYet forever). Unknown ids retrying silently. Trusting the prompt-finished event as proof of purchase.

## Related
`gamepass-maker`, `datastore-schema-builder`, `price-ladder-planner`, `starter-pack-designer`, `offer-timing-planner`, `kit-system-integrator`.
