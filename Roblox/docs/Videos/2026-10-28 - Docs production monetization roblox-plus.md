---
title: "Docs: production / monetization / roblox-plus"
url: https://create.roblox.com/docs/production/monetization/roblox-plus.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / roblox-plus

[Open](https://create.roblox.com/docs/production/monetization/roblox-plus.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on Roblox Plus monetization for creators: discount mechanics and Roblox subsidy, in-game Plus sign-up rewards via PromptRobloxSubscriptionPurchase, paid private server time payouts, and Robux transfer revenue share. Includes Luau examples for checking subscription status and handling the purchase flow.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[pricing]]** Don't hard-code prices; use GetProductInfoAsync and GetDeveloperProductsAsync so Plus subscribers see the discounted price, avoiding UI mismatch.
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[monetisation-other]]** Plus discounts are subsidized by Roblox, so creator earnings per purchase stay the same while lower prices may increase purchase frequency.
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[monetisation-other]]** Prompt Plus sign-ups in-game with PromptRobloxSubscriptionPurchase; only prompts triggered from your game earn the sign-up payout.
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[monetisation-other]]** Before granting Plus rewards, check HasRobloxSubscription, then confirm server-side via GetPropertyChangedSignal to verify the status actually changed.
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[monetisation-other]]** Plus subscribers can create free paid private servers; design the server so the subscriber owner spends 60+ minutes, since only the owner's time counts.
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[monetisation-other]]** Use PromptRobuxTransferAsync for transfers; transfer amounts must be 10–500 Robux per transaction and you receive 10% of the amount.
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[monetisation-other]]** Track Plus earnings in Creator Hub under Creations > Monetization > Roblox Plus.
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) **[[common-mistakes]]** Only the server owner's time counts for paid private server payouts; time spent by invited subscribers does not count toward your earnings.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) Plus discount to subscribers: **10% first two months, 20% from third month** (Roblox covers the discount; creator earnings unchanged)
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) Plus sign-up payout: **250 Robux/month for first 3 months, up to 750 Robux per new subscriber** (Only when subscribed via PromptRobloxSubscriptionPurchase in your game; 60-day holding period)
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) Paid private server payout: **Up to 100 Robux per subscriber** (Requires at least 60 cumulative minutes in 30 days; top five servers across Roblox)
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) Robux transfer share: **10% of transfer amount** (Eligible for DevEx; transfers 10–500 Robux each; no Roblox fee)
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) Items above price cap excluded from discount: **1,000,000 Robux** (Discounts do not apply above this price)
- [page](https://create.roblox.com/docs/production/monetization/roblox-plus) Creator effective revenue share example (100 Robux item): **70% non-subscriber, 78% at 10% discount, 88% at 20% discount** (Creator earns 70 Robux in all cases; Roblox subsidizes difference)

## Tools
MarketplaceService:PromptRobloxSubscriptionPurchase, MarketplaceService:PromptRobuxTransferAsync, MarketplaceService:GetProductInfoAsync, MarketplaceService:GetRobloxSubscriptionDetailsAsync, Player.HasRobloxSubscription

## He points to
- Sell a pass docs
- Sell a developer product docs
- Robux transfers docs

## Topics
[[common-mistakes]] [[monetisation-other]] [[pricing]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
