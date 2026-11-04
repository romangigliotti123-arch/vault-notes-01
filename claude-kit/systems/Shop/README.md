---
name: Shop
type: system
what: Developer-product purchases with a correct, idempotent ProcessReceipt (receipt ids stored in the same data as the reward) plus game-pass ownership checks and a name-based, rate-limited prompt remote.
tags: shop, monetisation, game pass, developer product, processreceipt, robux, idempotent, purchases
tested: unit-tested headless (Lune) + analyzed + linted; NOT tested in live Studio
---
# Shop

**What:** `MarketplaceService.ProcessReceipt` done the way Roblox requires, and game-pass checks that cannot be spoofed by the client.
**Not tested in live Studio.** Test purchases in Studio use real Robux flow-through only for your own published place; try a cheap product on a private test place first.

## Receipt rule (the whole point)
1. Unknown product, player data not loaded, any error or refusal: answer `NotProcessedYet` (Roblox retries, also when the player rejoins).
2. Reward and receipt record (`data.Receipts[PurchaseId] = time`) are written to the **same table** in the same step, then the data is **saved**, and only then `PurchaseGranted`.
3. A `PurchaseId` already in `Receipts` is never granted again; it just makes sure the save happened and confirms.
4. A receipt delivered again while the first is still running is deferred (`NotProcessedYet`).
5. Receipts are pruned to the newest 300 per player (config `maxReceipts`).

## Files
`src/Shop.luau` (pure), `src/ShopService.luau` (Roblox glue), `tests/Shop.test.luau`.

## Setup
Needs a data table per player that includes `Receipts = {}` (see `PlayerData` template; any storage works if `getData`/`saveNow` are provided).
```lua
local ShopService = require(script.Parent.Systems.Shop.ShopService)
ShopService.Start({
	products = {
		[1234567] = { name = "Coins100", grant = function(userId, data) data.coins += 100 return true end },
	},
	passes = { [7654321] = { name = "VIP", onOwned = function(userId) end } },
	getData = function(userId) local p = Players:GetPlayerByUserId(userId) return p and PlayerDataService.Get(p) end,
	saveNow = function(userId) local p = Players:GetPlayerByUserId(userId) return p ~= nil and PlayerDataService.SaveNow(p) end,
})
```
Client UI: `ReplicatedStorage.ShopRequest:FireServer("product", "Coins100")` / `("pass", "VIP")`. Server code: `ShopService.HasPass(player, "VIP")`.

## Config / API
`products[id] = {name, grant(userId, data) -> boolean}`; `passes[id] = {name, onOwned?}`; `maxReceipts`; `passAttempts` (4, backoff 1,2,3 s). Core: `ProcessReceipt`, `RefreshPasses`, `OnPassPromptFinished`, `HasPass`, `ClearPlayer`, `ProductIdByName`, `PassIdByName`.

## Exploit-safety
- The client sends only a NAME; ids and prices come from the server config. Prompts are rate limited (1 per 2 s per player).
- `PromptGamePassPurchaseFinished`'s `wasPurchased` is never trusted; ownership is re-asked from Roblox (`UserOwnsGamePassAsync`, with retries).
- Rewards are granted only on the server, only inside `ProcessReceipt`.

## Pitfalls
- A game has exactly one `ProcessReceipt` callback; `ShopService.Start` owns it. Do not set it elsewhere.
- `grant` must be synchronous and fast (no yields that can fail half way); if it can fail, return false BEFORE changing data.
- Roblox keeps calling `ProcessReceipt` until it says granted: an unknown product id retries forever (the log tells you), so keep `products` in sync with the Creator Dashboard.
- Pass perks that live in the world (a door, a tool) should check `HasPass` on the server at use time, not a client flag.
- Do not use `data.Receipts` for anything else. Keep it in the saved record; a separate in-memory table would lose the idempotency across servers.
- Prices/ids belong to the Creator Dashboard; monetisation fairness rules are in the vault (`rbx-monetize`, `rbx-critic`).

## Tests (2026-11-01)
```
cd <claude-kit>/systems && python check.py Shop
  stylua ok | selene ok | analyze ok (0 errors, 0 warnings) | lune Shop.test.luau: 13 passed, 0 failed
```
Covers: single grant, duplicate PurchaseId, unloaded player, unknown product, grant error/refusal, save failure then retry (no double grant), missing Receipts table, pruning, re-entrancy, pass verification and spoof, ownership retries.

## Sources
Roblox docs: `MarketplaceService.ProcessReceipt`, `ProductPurchaseDecision`, `UserOwnsGamePassAsync`, `PromptGamePassPurchaseFinished` (create.roblox.com/docs/production/monetization/developer-products, /game-passes); KB: monetisation notes in the vault.
