---
title: "Docs: production / monetization / paid-random-items"
url: https://create.roblox.com/docs/production/monetization/paid-random-items.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / paid-random-items

[Open](https://create.roblox.com/docs/production/monetization/paid-random-items.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official policy doc on paid random items. Covers which mechanics count as paid random items, required odds disclosures (all outcomes, numerical percentages summing to 100%, clickable details for large lists, pre-purchase disclosure of indirect purchases and odds-modifying items), and per-user restrictions via PolicyService (ArePaidRandomItemsRestricted, IsPaidItemTradingAllowed) with compliant alternatives.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** Disclose all possible outcomes and their numerical odds before purchase for any paid random item bought with Robux or Robux-purchasable currency.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** Disclose odds for indirect purchases too (keys, re-roll tokens, spin tickets) before the user spends the in-game currency.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** Use a clickable Details/Info button with descriptive text when too many outcomes fit the 3D view; a bare (i) icon is not sufficient.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** Show odds as percentages summing to exactly 100%; if rounding, add the disclaimer that displayed probabilities may not total 100%.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** Explain numerically and update dynamically any luck boost or odds-modifying item before purchase and while active.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** If an outcome is one-time only, update remaining odds for that user after each award.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** Call PolicyService:GetPolicyInfoForPlayerAsync and check ArePaidRandomItemsRestricted per user; for restricted users, offer free earnable paths, fixed-order outcomes, direct purchase priced at expected value, or remove the random item.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[monetisation-other]]** For restricted users, block trading of paid random outcomes when IsPaidItemTradingAllowed is false.
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) **[[pricing]]** When offering direct purchase to restricted users, price the guaranteed item at its expected value; e.g. a 10 Robux box with 5% odds for a rare sword implies 200 Robux.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) Expected-value direct price example: **10 Robux box at 5% odds → 200 Robux guaranteed** (Doc example for pricing guaranteed sword for restricted users)
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) Odds total requirement: **100% exactly** (Sum of all final outcome probabilities must equal 100%)

## Tools
PolicyService:GetPolicyInfoForPlayerAsync

## He points to
- Roblox Terms of Use
- Roblox Community Standards

## Quotes
- [page](https://create.roblox.com/docs/production/monetization/paid-random-items) "if you offer paid random items that users can purchase with Robux or other in-game currency purchasable with Robux, you must indicate all possible outcomes and the actual numerical odds of what they may receive."

## Topics
[[monetisation-other]] [[pricing]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
