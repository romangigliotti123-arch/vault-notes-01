---
title: "Docs: production / monetization / price-optimization"
url: https://create.roblox.com/docs/production/monetization/price-optimization.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / price-optimization

[Open](https://create.roblox.com/docs/production/monetization/price-optimization.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page on Price optimization within Managed Pricing. Explains how price tests split users into groups, measure conversion, apply optimized prices only with positive incremental revenue, and requires dynamically scripted prices (checked via Dynamic Price Check tool). Covers test steps, limitations, and reporting glossary.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Make sure product prices are scripted via MarketplaceService (not hard-coded) before price optimization; hard-coded prices can't be tested or changed.
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Run the Dynamic Price Check tool with test accounts to find which prices are hard-coded: if the price changes on the fake price, it's scripted; if not, it's hard-coded.
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Only run price optimization once the game has about 60,000 transactions over the previous 30 days, so the test produces significant data.
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Include all passes and developer products in the test for best results.
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Review the results after the test; optimized prices are applied only when they produce positive incremental total revenue.
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Use the price review period afterward to track long-term revenue impact of price changes.
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Stop a test anytime from Managed Pricing; products revert to original prices. Prices of tested products can't be edited while a test runs.
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) **[[pricing]]** Use GetProductInfo with Enum.InfoType.Product for developer products and Enum.InfoType.GamePasses for passes when scripting prices, since the default InfoType fetches assets.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) Transactions threshold: **60,000 over previous 30 days** (Recommended minimum for a successful price optimization test)
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) Test duration: **~3 weeks** (Approximate time until test-complete email notification)
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) Test frequency: **At least every 90 days** (Tests run automatically at least this often, or sooner if prices may be stale)
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) Control group share: **2% of users** (Users shown original prices during the four-week price review period)
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) Dynamic Price Check accounts: **Up to 5 users** (Test accounts that can be added to the dynamic price check tool)
- [page](https://create.roblox.com/docs/production/monetization/price-optimization) Price review period: **4 weeks** (Window in which revenue of tested products is measured after applying prices)

## Tools
Managed Pricing (Creator Hub), Price optimization, Dynamic Price Check tool, MarketplaceService

## He points to
- Pass analytics
- Developer Product analytics
- Sell a pass
- Sell a developer product

## Topics
[[pricing]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
