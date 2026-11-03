---
title: "Docs: production / analytics / economy-events"
url: https://create.roblox.com/docs/production/analytics/economy-events.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / economy-events

[Open](https://create.roblox.com/docs/production/analytics/economy-events.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Economy events in Analytics. Explains tracking sources and sinks server-side via AnalyticsService:LogEconomyEvent, transaction types, optional item SKUs and custom fields, and the five Economy dashboard charts used to balance the in-game economy and grow revenue.

## Tips
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[analytics-metrics]]** Log economy events only from the server; events sent from the client or Studio are not tracked. Games must be published.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[analytics-metrics]]** Always pass the cost/amount as a positive number; the dashboard renders sinks as negative automatically.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[analytics-metrics]]** Include an itemSKU on source and sink events; without it the sources and sinks table shows N/A.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[analytics-metrics]]** Track every place users gain (sources) and spend (sinks) a currency so the Economy dashboard reflects the real economy.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[analytics-metrics]]** Use custom fields (e.g. quest name, store location) to break down which segments earn or spend the most.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[core-loops-and-game-design]]** Keep total sources minus total sinks near zero; if net total keeps growing, add more sinks for that resource.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[core-loops-and-game-design]]** If average wallet balance grows, especially for payers, add new sinks to spend resources.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[monetisation-devproducts]]** If users aren't sourcing resources from IAP, consider reducing prices or offering new purchase options.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[core-loops-and-game-design]]** If users aren't spending a given resource enough, add new sinks for that resource.
- [page](https://create.roblox.com/docs/production/analytics/economy-events) **[[analytics-metrics]]** Use the default transaction types (IAP, TimedReward, Onboarding, Shop, Gameplay, ContextualPurchase) first; custom type names are optional.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/economy-events) Dashboard charts: **5 charts; up to 5 currencies; filters up to 3 custom fields** (Economy dashboard capacity limits stated in docs)
- [page](https://create.roblox.com/docs/production/analytics/economy-events) Default transaction types: **6** (IAP, TimedReward, Onboarding, Shop, Gameplay, ContextualPurchase)
- [page](https://create.roblox.com/docs/production/analytics/economy-events) Target net economy balance: **sources minus sinks close to zero** (Total sources and sinks by category chart guidance)

## Tools
AnalyticsService:LogEconomyEvent, Creator Hub Analytics Economy dashboard

## He points to
- Balance virtual economies (Roblox docs)
- Event tracking limitations (Roblox docs)
- Custom fields (Roblox docs)

## Topics
[[analytics-metrics]] [[core-loops-and-game-design]] [[monetisation-devproducts]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
