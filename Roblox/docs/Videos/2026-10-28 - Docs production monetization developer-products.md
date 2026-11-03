---
title: "Docs: production / monetization / developer-products"
url: https://create.roblox.com/docs/production/monetization/developer-products.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / developer-products

[Open](https://create.roblox.com/docs/production/monetization/developer-products.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on developer products: creating them (icon specs, price limits), getting product IDs, selling inside and outside games via MarketplaceService and ProcessReceipt, external sales eligibility, personalization APIs (RankProductsAsync, RecommendTopProductsAsync), and product analytics.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Use developer products for repeatable purchases (currency, ammo, potions); use game passes for one-time purchases.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Upload product icons at max 512x512, keep key details inside the circular boundary, and use .jpg, .png or .bmp format.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Implement ProcessReceipt correctly before listing products; do not rely on PromptProductPurchaseFinished to grant items.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** In ProcessReceipt, return PurchaseGranted only after the item is actually granted; otherwise return NotProcessedYet so it retries on next join.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Set the ProcessReceipt callback from a single server Script, since it can only be assigned once.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Mark products Listed in Shop and add a custom icon so players recognize them on external surfaces; otherwise Roblox shows a default icon.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Listed products that Roblox flags for ProcessReceipt issues drop out of external surfaces until fixed and marked as fixed in the report.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Call RankProductsAsync once at game join, not repeatedly, because it has a strict rate limit.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Wrap RecommendTopProductsAsync in task.spawn to avoid blocking; filter out products the user can no longer buy.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[monetisation-devproducts]]** Track per-user purchase history yourself; Roblox does not record it for developer products.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[pricing]]** Developer product prices must be between 1 and 1,000,000,000 Robux.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[common-mistakes]]** Do not process purchases with PromptProductPurchaseFinished; the event firing does not mean the purchase succeeded.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[common-mistakes]]** If your game relies on cross-game developer product sales, integrate Robux transfers before May 30, 2026; cross-game sales are disabled after that date.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[common-mistakes]]** If using price optimization, run the price-showing script on the client so users see personalized prices.
- [page](https://create.roblox.com/docs/production/monetization/developer-products) **[[business-and-payouts]]** External sales do not change standard earnings or purchase handling.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/developer-products) Developer product icon max size: **512x512 px**
- [page](https://create.roblox.com/docs/production/monetization/developer-products) Developer product price range: **1 to 1,000,000,000 Robux**
- [page](https://create.roblox.com/docs/production/monetization/developer-products) RecommendTopProductsAsync requirement: **at least one purchase in last 28 days, else empty list**
- [page](https://create.roblox.com/docs/production/monetization/developer-products) Product analytics time-series showcase: **up to 8 top-selling items**
- [page](https://create.roblox.com/docs/production/monetization/developer-products) RecommendTopProductsAsync max results: **up to 50 items**
- [page](https://create.roblox.com/docs/production/monetization/developer-products) Cross-game developer product sales cutoff: **May 30, 2026 (disabled)**

## Tools
Roblox Studio, Creator Hub, MarketplaceService, RankProductsAsync, RecommendTopProductsAsync, GetProductInfo, GetDeveloperProductsAsync, ProcessReceipt

## He points to
- MarketplaceService.ProcessReceipt docs page
- Randomized virtual item policy
- Passes documentation

## Quotes
- [page](https://create.roblox.com/docs/production/monetization/developer-products) "Do not use the PromptProductPurchaseFinished event to process purchases. You must use the ProcessReceipt callback instead."
- [page](https://create.roblox.com/docs/production/monetization/developer-products) "The functions for handling each product ID must return true for the transaction to be successful."

## Topics
[[business-and-payouts]] [[common-mistakes]] [[monetisation-devproducts]] [[pricing]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
