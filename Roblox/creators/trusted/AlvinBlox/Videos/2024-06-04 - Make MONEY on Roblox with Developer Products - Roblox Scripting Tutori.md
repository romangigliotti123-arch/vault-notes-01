---
title: "Make MONEY on Roblox with Developer Products - Roblox Scripting Tutorial"
url: https://youtu.be/5YNFRCD0pd0
creator: AlvinBlox
official: false
advice_density: medium
date: 2024-06-04
views: 11700
transcript: auto-captions
confidence: high
tags: [roblox, alvinblox, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Make MONEY on Roblox with Developer Products - Roblox Scripting Tutorial

[Watch](https://youtu.be/5YNFRCD0pd0) | AlvinBlox | 11,700 views | 2024-06-04

## Summary
Tutorial on creating Roblox developer products: create product in Creator Dashboard/game settings, prompt purchase from client with MarketplaceService:PromptProductPurchase, handle MarketplaceService.ProcessReceipt on server, validate player presence, use a table of product-ID handler functions, award currency and temporary walkspeed boost.

## Tips
- [0:36](https://youtu.be/5YNFRCD0pd0?t=36) **[[monetisation-devproducts]]** Create the developer product in game settings Monetization or create.roblox.com, then copy its product ID for scripting; the game must be published first.
- [1:12](https://youtu.be/5YNFRCD0pd0?t=72) **[[monetisation-devproducts]]** Prompt purchases from a LocalScript using MarketplaceService:PromptProductPurchase with the local player and product ID, e.g. on a button click.
- [2:32](https://youtu.be/5YNFRCD0pd0?t=152) **[[scripting-and-performance]]** Process purchases on the server in MarketplaceService.ProcessReceipt because server handling is authoritative and cannot be exploited by clients.
- [4:31](https://youtu.be/5YNFRCD0pd0?t=271) **[[scripting-and-performance]]** Return Enum.ProductPurchaseDecision.PurchaseGranted only after delivering goods; return NotProcessedYet if the player is missing so the purchase is retried next join.
- [7:17](https://youtu.be/5YNFRCD0pd0?t=437) **[[scripting-and-performance]]** Check the player exists with Players:GetPlayerByUserId before granting items, since they may have left mid-purchase.
- [8:36](https://youtu.be/5YNFRCD0pd0?t=516) **[[scripting-and-performance]]** Store one handler function per product ID in a table and dispatch by ID, so adding products means adding a table entry instead of more if/elseif branches.
- [12:03](https://youtu.be/5YNFRCD0pd0?t=723) **[[monetisation-devproducts]]** Developer products are consumable and can be bought repeatedly, unlike gamepasses; use them for currency or temporary boosts.
- [12:34](https://youtu.be/5YNFRCD0pd0?t=754) **[[core-loops-and-game-design]]** Use task.delay to revert temporary effects like walkspeed after a set duration without yielding the purchase function.

## Numbers
- [0:36](https://youtu.be/5YNFRCD0pd0?t=36) Example developer product price: **100 Robux (test product)**
- [11:22](https://youtu.be/5YNFRCD0pd0?t=682) Example currency grant per purchase: **100 cash per purchase**
- [13:16](https://youtu.be/5YNFRCD0pd0?t=796) Example temporary walkspeed boost: **speed 50 for 5 seconds, then reset to 16 (script shows 20s delay, narrator says 5s)**

## Tools
Roblox Studio, Creator Dashboard (create.roblox.com), MarketplaceService, Players:GetPlayerByUserId, task.delay

## He points to
- Roblox developer documentation (MarketplaceService ProcessReceipt pattern)

## Quotes
- [0:00](https://youtu.be/5YNFRCD0pd0?t=0) "a developer product can be purchased over and over again unlike a Game Pass which can only be purchased once"
- [2:32](https://youtu.be/5YNFRCD0pd0?t=152) "it's always good to handle this stuff on the server because it's authoritative... can't be touched by exploiters"

## On screen
Contact sheet shows Studio Game Settings > Monetization panel with Developer Products section, a Buy Item prompt dialog in-game, leaderstats being added, and a walkspeed test with a Roblox spiked-platform baseplate. No analytics numbers shown.

## Topics
[[core-loops-and-game-design]] [[monetisation-devproducts]] [[scripting-and-performance]]

Back to [[AlvinBlox - How to make successful Roblox games]]
