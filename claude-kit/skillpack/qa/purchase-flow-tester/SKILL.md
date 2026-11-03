---
name: purchase-flow-tester
description: "Test every purchase path (developer products, game passes, subscriptions) including failure and retry: duplicate receipts, failed saves, missing data, unknown products, refunds and rebuy after death or rejoin, with an automated rule suite against the kit Shop and a manual Studio and live checklist. Use after building or changing any monetisation code."
category: qa
tags: purchase, receipt, processreceipt, developer product, game pass, idempotent, refund, test, monetisation, shop, notyet
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md
related: devproduct-handler, gamepass-maker, receipt-flow-tester, pass-ownership-cache-builder, data-loss-simulator, dupe-exploit-hunter, join-leave-race-tester
---

# purchase-flow-tester

Purchases are the one place a bug costs real money and trust. The rules from the vault are few: one `ProcessReceipt` callback, grant only after the data is updated and saved, answer `NotYet` on anything uncertain so Roblox retries, never grant the same `PurchaseId` twice. `scripts/PurchaseScenarios.luau` encodes those as seven headless scenarios behind a small "rig" interface and is tested against the kit's real `Shop` module (all pass) and a naive handler (it fails four).

## When to use
After building a shop, adding a product or pass, changing save code, or before launching monetisation. Not for: choosing prices (`price-ladder-planner`), designing offers (`starter-pack-designer`), or receipt log reading in live (`receipt-flow-tester` covers the live-flow side if built).

## Inputs (max 2)
1. The products and passes with their grant effect (default: read them from the code; ids that are not yet created are `0` / `SET IN CREATOR HUB`). 2. The module that handles receipts (default: the kit `Shop`).

## Procedure
1. Inventory every purchase path: each product and pass, the single `ProcessReceipt` assignment (exactly one in the whole project: `script_grep` for `ProcessReceipt`), and where pass ownership is read. Stop if there are two receipt handlers: merge them first.
2. Build a rig for your module (see the test file: `process`, `coins`, `setSaveOk`, `setDataLoaded`, product ids) and run `PurchaseScenarios.runAll(make)` / `report`. The scenarios: normal purchase grants once; repeated PurchaseId never grants twice; failed save answers NotYet and the retry grants exactly once; data not loaded answers NotYet and grants nothing; unknown product answers NotYet; a throwing grant answers NotYet and changes nothing; two different purchases both grant.
3. Fix any FAIL in the receipt code, not the scenario. Typical: granting before checking data, recording the receipt after answering Granted, no per-PurchaseId in-flight guard, returning Granted when the save failed.
4. Studio manual run (test purchases do not charge Robux; vault): prompt each product and pass, buy, check the grant, rejoin and check persistence, buy again, die and respawn (passes must survive death and be re-verified on join, not assumed). Test with a one-player server and with 2 players.
5. Failure paths by hand: simulate a failed save (`SaveNow` returns false) and confirm the prompt does not show "bought" in your UI until the grant lands; simulate leaving mid-purchase and rejoining (the receipt must be retried).
6. Live checks the owner does: one real purchase on the published place by a test account with the cheapest product (the owner's action, may cost Robux), and verify it in the live game page rather than only in Studio. Refunds: policy and effects are live-checked; the grant must be reversible only if you chose to support it.
7. Record the result table and attach the receipts log lines (`PurchaseId` values).

## Studio MCP path
`list_roblox_studios` -> `script_grep` ProcessReceipt -> `start_stop_play` -> `execute_luau` (Server) calling your Shop module's `ProcessReceipt` with synthetic receipts (the `MarketplaceService.ProcessReceipt` callback itself cannot be read back) -> `get_console_output` -> `execute_luau` (Client) `MarketplaceService:PromptProductPurchase` for the real prompt flow -> `screen_capture`.

## Fallback
`lune run ../skillpack/qa/purchase-flow-tester/scripts/tests/PurchaseScenarios.test.luau` from `claude-kit/systems` (3 tests, kit Shop 7/7). The Roblox purchase prompt, real Robux and live receipts are `untested` without Studio and the owner.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: process purchases only in `ProcessReceipt`, idempotently. `Roblox/roblox-kb/anti-exploit-and-security.md`: define `ProcessReceipt` once in a single server script; verify receipt product and player before granting; do not grant rewards from purchase-finished events (deprecated); rebuy and pass checks. `Roblox/roblox-kb/testing-debugging-and-qa.md`: test monetisation in Studio or a one-player server; Studio test purchases do not charge Robux, and Studio grants passes for free and does not keep them after death, so verify re-buys in the live player. Checklist: `Roblox/roblox-kb/_tools/CHECKLIST-monetization.md`.

## Output
```
PURCHASE FLOW <game> <date>: scenarios N/7, paths tested M
| path | product/pass | result | evidence |
Manual: <checks and results>   Live: <owner action needed>   Unchecked: <refund policy, subscriptions>
```

## Acceptance checks
- [ ] `lune run` of the PurchaseScenarios test prints "3 passed, 0 failed".
- [ ] `PurchaseScenarios.report(...)` for your module shows 7/7 (quoted), or each fail is fixed and re-run.
- [ ] Exactly one `ProcessReceipt` assignment exists (grep output quoted).
- [ ] Persistence after rejoin and pass state after death were tested, or marked untested.
- [ ] No real purchase was made by the agent; live purchase is listed as the owner's action.

## Pitfalls
Granting from `PromptProductPurchaseFinished`. Returning Granted when the save failed. Trusting pass state cached from join without re-verifying. Studio-only testing (passes are free there). Two receipt handlers overwriting each other. Test ids copied from another game.

## Related
`devproduct-handler`, `gamepass-maker`, `pass-ownership-cache-builder`, `data-loss-simulator`, `dupe-exploit-hunter`, `join-leave-race-tester`.
