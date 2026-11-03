---
title: "Docs: production / monetization / managed-pricing"
url: https://create.roblox.com/docs/production/monetization/managed-pricing.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / managed-pricing

[Open](https://create.roblox.com/docs/production/monetization/managed-pricing.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Managed Pricing in Creator Hub: a single opt-in combining price optimization (tests on pass/devproduct prices using game-specific demand, conversion, spend signals) and regional pricing (prices bounded 30%-100% of default). Covers enrollment steps, eligibility defaults, and the hard-coded price check.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/managed-pricing) **[[pricing]]** Before opting in, remove hard-coded prices from your game; managed pricing prompts you to fix them first.
- [page](https://create.roblox.com/docs/production/monetization/managed-pricing) **[[pricing]]** Regional prices are bounded between 30% and 100% of the default price; expect discounts up to 70% for lower-purchasing-power regions.
- [page](https://create.roblox.com/docs/production/monetization/managed-pricing) **[[monetisation-gamepasses]]** Protect in-game trades and gifts by using MarketplaceService:GetUsersPriceLevelsAsync when regional pricing is active.
- [page](https://create.roblox.com/docs/production/monetization/managed-pricing) **[[monetisation-other]]** Subscriptions are regionalized automatically and excluded from price optimization tests.
- [page](https://create.roblox.com/docs/production/monetization/managed-pricing) **[[pricing]]** Use the Managed Pricing tab's bulk enable/disable and per-item opt-out to control which passes and products are tested.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/managed-pricing) Regional price floor: **30% of default price** (Lower bound for regionally adjusted prices)
- [page](https://create.roblox.com/docs/production/monetization/managed-pricing) Regional price ceiling: **100% of default price** (Upper bound for regionally adjusted prices)

## Tools
Creator Hub Managed Pricing tab, Price optimization tests, Dynamic price check tool, MarketplaceService:GetUsersPriceLevelsAsync

## He points to
- Price optimization docs
- Regional pricing docs

## Topics
[[monetisation-gamepasses]] [[monetisation-other]] [[pricing]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
