---
title: "Docs: production / monetization / regional-pricing"
url: https://create.roblox.com/docs/production/monetization/regional-pricing.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / regional-pricing

[Open](https://create.roblox.com/docs/production/monetization/regional-pricing.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on Managed Pricing regional pricing: how regional prices are set (default price as ceiling, max 70% discount), enabling it for passes, devproducts, subscriptions and Avatar items, detecting hard-coded prices with the Dynamic Price Check tool, displaying regional prices in UI, and using GetUsersPriceLevelsAsync to guard gifts and trades against arbitrage.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[monetisation-gamepasses]]** Passes have Managed Pricing enabled by default; disable it per pass via Monetization > Passes > Disable Managed Pricing if you don't want regional prices.
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[monetisation-devproducts]]** Before enabling Managed Pricing on developer products, make sure their prices are dynamically scripted via MarketplaceService, not hard-coded in UI.
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[pricing]]** Set your default global price carefully: regional prices never exceed it and never drop more than 70% below it (100 Robux default means a 30 Robux floor).
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[common-mistakes]]** Hard-coded prices in your UI won't update for regional pricing, so players see the wrong price while being charged the correct regional one. Fix by using MarketplaceService.
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[scripting-and-performance]]** Use GetProductInfoAsync or GetDeveloperProductsAsync at runtime to show the regional price in custom UI so it matches the purchase prompt.
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[scripting-and-performance]]** Call GetUsersPriceLevelsAsync at player join and do not cache results after the session, since user price levels can change.
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[monetisation-other]]** To stop gift/trade arbitrage, compare recipients' price levels with GetUsersPriceLevelsAsync and only allow gifting down or trading between equal levels.
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[analytics-metrics]]** Use the Sales page's Top Countries/Regions list to see adjusted regional prices per pass or product.
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) **[[monetisation-other]]** Subscriptions priced in Robux have Managed Pricing enabled by default and it cannot be turned off; local-currency subscriptions are not eligible.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) Maximum regional discount: **70% off default price** (Regional prices never drop more than 70% below default)
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) Price ceiling: **100% of default price** (Regional prices never exceed the default price set)
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) Example floor: **30 Robux for 100 Robux default** (Lowest regional price for a 100 Robux item)
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) GetUsersPriceLevelsAsync range: **1 to 1000** (1000 = full global price; lower = larger regional discount)
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) Example price level: **500 = pays 50% of base price** (Used to compare gifting/trading level differences)
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) Dynamic Price Check test accounts: **up to 5 users** (Accounts used to detect hard-coded prices)

## Tools
MarketplaceService, Dynamic Price Check tool, GetUsersPriceLevelsAsync, GetProductInfoAsync, GetDeveloperProductsAsync

## He points to
- Create subscriptions
- Check for dynamic pricing (Price optimization page)
- Sell a pass inside your game
- Sell a developer product inside your game
- Publish to Marketplace (Avatar item pricing)

## Quotes
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) "Economic location is not always the same as account location. To determine a user's economic location, Roblox looks at signals, including VPN usage, billing history, and account history."
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) "We recommend that you do not cache the results of your GetUsersPriceLevelsAsync API calls after a user session. User price levels can change."
- [page](https://create.roblox.com/docs/production/monetization/regional-pricing) "if you have hard-coded the price into your game's UI, that number does not update as it's not dynamic or accessible by Roblox."

## Topics
[[analytics-metrics]] [[common-mistakes]] [[monetisation-devproducts]] [[monetisation-gamepasses]] [[monetisation-other]] [[pricing]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
