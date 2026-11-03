---
title: "Docs: production / monetization / passes"
url: https://create.roblox.com/docs/production/monetization/passes.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / passes

[Open](https://create.roblox.com/docs/production/monetization/passes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on Passes: creating a pass (icon specs, category), getting pass IDs, selling inside a game via MarketplaceService (GetProductInfo, PromptGamePassPurchase, PromptGamePassPurchaseFinished), selling outside via Listed status and Buy Robux promotion, granting privileges on PlayerAdded, and personalization APIs (RankProductsAsync, RecommendTopProductsAsync) plus pass analytics.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** Use a 512x512 max image in .jpg, .png or .bmp for pass icons; keep important content inside the circular boundary so it isn't cropped.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** Mark passes as Listed in Monetization > Shop so they appear outside your game (homepage, search, post-purchase page); add a custom icon since Roblox otherwise shows a default one.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** Check UserOwnsGamePassAsync in PlayerAdded so players who bought the pass outside the game get its privileges on join; pass privileges must be assigned manually.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** Create a unique pass specifically for the Buy Robux page for best promotion results.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** Ensure promoted on-sale passes are priced above 49 Robux and below 801 Robux; promoted passes cannot grant paid random items and need a thumbnail.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[scripting-and-performance]]** Call RankProductsAsync once at game join rather than repeatedly, because it has a strict rate limit.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[scripting-and-performance]]** Wrap RecommendTopProductsAsync and RankProductsAsync calls in task.spawn with pcall so slow ranking calls don't block the game.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** Run price optimization scripts on the client so users see personalized pass prices.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[business-and-payouts]]** Store your own per-user pass purchase history; Roblox does not record pass purchases by specific users, though sales data can be downloaded.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** Use a pass for permanent benefits and developer products for repeatable purchases like potions, temporary power-ups or currency.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[common-mistakes]]** Don't rely on cross-game pass sales: they are disabled starting May 30, 2026; integrate Robux transfers before then if your game depends on them.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[analytics-metrics]]** Use pass analytics to view top passes, sales and net revenue trends, and how many buyers came via the Buy Robux page and joined the game.
- [page](https://create.roblox.com/docs/production/monetization/passes) **[[monetisation-gamepasses]]** RecommendTopProductsAsync returns nothing unless the game has at least one item sale in the past 28 days; build a Top Picks tab on that basis.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/passes) Pass icon max size: **512x512 px** (Formats .jpg, .png, .bmp; keep key content inside circle)
- [page](https://create.roblox.com/docs/production/monetization/passes) Promoted on-sale pass Robux range: **50 to 800 Robux** (Must be greater than 49 and less than 801 Robux)
- [page](https://create.roblox.com/docs/production/monetization/passes) Promoted pass cost to user: **Free** (Promoted passes are given to users for free after Robux purchase)
- [page](https://create.roblox.com/docs/production/monetization/passes) RecommendTopProductsAsync max items: **50** (Returns items user most likely to purchase; excludes owned passes)
- [page](https://create.roblox.com/docs/production/monetization/passes) Analytics top-series limit: **8 items** (Time-series graph can showcase up to eight top-selling items)
- [page](https://create.roblox.com/docs/production/monetization/passes) Recommendation data window: **28 days** (Requires at least one item sale in last 28 days)
- [page](https://create.roblox.com/docs/production/monetization/passes) Cross-game pass sales disabled: **May 30, 2026** (Cross-game pass sales end on this date)

## Tools
Creator Hub, MarketplaceService, Roblox Studio

## He points to
- Developer products docs
- Randomized Virtual Item Policy
- Community Standards

## Topics
[[analytics-metrics]] [[business-and-payouts]] [[common-mistakes]] [[monetisation-gamepasses]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
