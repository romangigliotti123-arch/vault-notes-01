---
name: receipt-flow-tester
description: "Test a game's purchase flow end to end offline: run the failure scenarios every ProcessReceipt must survive (duplicate delivery, data not loaded, save failure, unknown product) against the real catalogue wired to the kit Shop, then give the owner a short live test script. Use after wiring or changing any product, pass or grant; building the catalogue is devproduct-handler."
category: money
tags: receipt, processreceipt, purchase test, idempotent, duplicate, save failure, scenarios, regression, shop
kb: Roblox/roblox-kb/monetisation-devproducts.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: devproduct-handler, gamepass-maker, pass-ownership-cache-builder, playtest-bot-writer, datastore-schema-builder, lune-unit-test-writer
---

# receipt-flow-tester

One job: prove purchases cannot be lost or doubled. The kit Shop system already implements the rule (grant and receipt record in the same data table, save, then confirm) with 13 Lune tests, but that proves the library, not YOUR catalogue and `grant` functions. `scripts/ReceiptScenarios.luau` runs five failure scenarios against your real wiring: first delivery grants once, the same `PurchaseId` again never grants twice, data not loaded answers NotYet, save failure answers NotYet and the retry grants once, unknown product answers NotYet.

## When to use
After wiring `Catalogue` to Shop, after editing any `grant`, before launch, and after any change to the player data schema. Not for: designing products (`devproduct-handler`), game-pass ownership caches (`pass-ownership-cache-builder`).

## Inputs (max 2)
1. The catalogue module and the data module (default: `Catalogue.luau`, the PlayerData template). 2. The observable each product changes, e.g. `data.coins` (default: read each grant).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-devproducts rules --max-chars 4000` and `systems/Shop/README.md` (receipt rule). Stop when you can state the five rules.
2. Write a Lune test beside your catalogue (pattern in `scripts/tests/ReceiptScenarios.test.luau`): a factory that builds a fresh `Shop.new({ products = <your products>, getData = ..., saveNow = ..., ownsPass = ..., now = ..., wait = ... })` with fakes whose `loaded` and `saveOk` switches the factory exposes as `setLoaded` and `setSaveOk`.
3. Run `ReceiptScenarios.run(factory)` once per product you sell: pass the product id, user id and the expected change to the observable. Print each `name`, `pass`, `detail`.
4. For each failing scenario find the cause: a `grant` that yields, mutates data then returns false, grants into a table that is not saved, or a second `ProcessReceipt` assignment somewhere else in the project (search for `ProcessReceipt`; there must be exactly one owner, Shop).
5. Add product-specific refusal cases (full inventory, level cap): the grant must return false BEFORE changing data (`Catalogue` supports `refuseWith` fixtures).
6. Live test script for the owner, on their own published test place only, with the cheapest product and a test account: buy; confirm the reward and `data.Receipts` entry; rejoin and confirm it did not grant again; buy while data is loading if reproducible. Marked `untested` until the owner runs it. You never spend Robux.
7. Add the test to the project's test run so it stays green.
8. Test the tester: `lune run ../skillpack/money/receipt-flow-tester/scripts/tests/ReceiptScenarios.test.luau` from `~/.claude/claude-kit/systems` (it must pass the kit Shop and must fail a deliberately naive handler).

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add the test file (Rojo owners edit files) -> `execute_luau` (Server) to call `Shop:ProcessReceipt` with a fake receipt table for a loaded test player, twice, and compare the reward -> `get_console_output`. Real purchase prompts need a published place and a test account: `untested`.

## Fallback
Lune scenarios (headless) plus the owner's live script. The live script stays `untested`.

## Evidence
`Roblox/roblox-kb/monetisation-devproducts.md` (ProcessReceipt must be idempotent and return the right status; grant once), `Roblox/roblox-kb/data-persistence.md` (save before confirming; session locking), `Roblox/roblox-kb/anti-exploit-and-security.md` (server-only grants), `Roblox/roblox-kb/testing-debugging-and-qa.md`, `systems/Shop/README.md` (the receipt rule). Scenario names are this skill's; the rule is the platform's, live-check the callback contract.

## Output
A test file in the project, the printed scenario table, a list of defects found and fixed, and the owner's live test script (five steps).

## Acceptance checks
- [ ] `ReceiptScenarios.run` returns `allPassed` for every product (quote the pass lines).
- [ ] `lune run` ReceiptScenarios tests pass (quote "3 passed, 0 failed") and luau-check is clean.
- [ ] Exactly one `ProcessReceipt` assignment exists in the project (quote the search result).
- [ ] Every `grant` that can refuse has a fixture proving it refuses without changing data.
- [ ] The live script is written and marked `untested`.
- [ ] The receipt test proves `PurchaseGranted` is returned only after the grant is saved and that `PromptProductPurchaseFinished` grants nothing (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, monetisation-devproducts).

## Pitfalls
Testing the library but not your grants. A grant that errors after changing data. Receipts stored outside the saved record. A second handler overwriting Shop's. Counting a Studio-only test as proof of live behaviour.

## Related
`devproduct-handler`, `gamepass-maker`, `pass-ownership-cache-builder`, `playtest-bot-writer`, `lune-unit-test-writer`.
