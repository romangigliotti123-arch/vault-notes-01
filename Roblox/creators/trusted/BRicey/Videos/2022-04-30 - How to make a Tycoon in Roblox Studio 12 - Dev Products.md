---
title: "How to make a Tycoon in Roblox Studio #12 - Dev Products"
url: https://youtu.be/5bI6l6SHBDU
creator: B Ricey
official: false
advice_density: medium
date: 2022-04-30
views: 14667
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Tycoon in Roblox Studio #12 - Dev Products

[Watch](https://youtu.be/5bI6l6SHBDU) | BRicey | 14,667 views | 2022-04-30

## Summary
Tutorial on adding Roblox developer products (repeatable purchases) to a tycoon: creating the product in Game Settings, wiring a UI button to PromptProductPurchase on the client, and granting currency server-side via MarketplaceService.ProcessReceipt with pcall and PurchaseGranted/NotProcessedYet return values.

## Tips
- [0:35](https://youtu.be/5bI6l6SHBDU?t=35) **[[monetisation-devproducts]]** Create developer products in Game Settings > Monetization > Developer Products; unlike game passes they can be bought repeatedly, so use them for consumables like currency.
- [5:45](https://youtu.be/5bI6l6SHBDU?t=345) **[[monetisation-devproducts]]** Grant the item by calling your existing player-manager setter rather than editing leaderstats directly, so all currency changes go through one function.
- [8:29](https://youtu.be/5bI6l6SHBDU?t=509) **[[monetisation-devproducts]]** In ProcessReceipt, return NotProcessedYet if the player is not in the server; Roblox will retry later, preventing players from paying without receiving the item.
- [9:51](https://youtu.be/5bI6l6SHBDU?t=591) **[[monetisation-devproducts]]** Wrap the product grant function in pcall; if it errors, return NotProcessedYet so the purchase is not charged without being granted.
- [10:32](https://youtu.be/5bI6l6SHBDU?t=632) **[[monetisation-devproducts]]** Only return PurchaseGranted after the grant succeeds; this is what tells Roblox the purchase completed.
- [3:30](https://youtu.be/5bI6l6SHBDU?t=210) **[[client-server-and-remotes]]** Keep client prompt code separate per purchase type (game pass vs dev product) even if duplicated, since the prompt function and handling differ.
- [4:22](https://youtu.be/5bI6l6SHBDU?t=262) **[[code-architecture-and-frameworks]]** A standalone script for an isolated dev product system is acceptable; only convert to a module when it is needed, avoiding over-complication.
- [4:11](https://youtu.be/5bI6l6SHBDU?t=251) **[[testing-debugging-and-qa]]** Studio test purchases do not charge Robux, so test the flow freely in Studio before release.

## Numbers
- [0:35](https://youtu.be/5bI6l6SHBDU?t=35) Example dev product price: **5 Robux** (Demo 'More Money' product priced at 5 Robux, grants 1000 coins)

## Tools
Roblox Studio, MarketplaceService, PromptProductPurchase, pcall

## He points to
- Roblox Developer Hub (MarketplaceService receipt info)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[monetisation-devproducts]] [[testing-debugging-and-qa]]

Back to [[BRicey - How to make successful Roblox games]]
