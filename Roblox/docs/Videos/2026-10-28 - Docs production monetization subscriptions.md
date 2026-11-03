---
title: "Docs: production / monetization / subscriptions"
url: https://create.roblox.com/docs/production/monetization/subscriptions.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / subscriptions

[Open](https://create.roblox.com/docs/production/monetization/subscriptions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on subscriptions: creation, Robux vs local-currency pricing and eligibility, activation and editing rules, integration via MarketplaceService (status checks, prompting purchases, replacing passes), revenue splits and hold periods, refunds, payouts, and subscription analytics/webhooks.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[monetisation-other]]** Subscriptions must offer the same benefits across all platforms and devices; benefits must be honored for the full subscription term with no back-end revocation.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[monetisation-other]]** Do not gate paid subscription benefits behind extra tasks such as social media posts; this is prohibited (battle passes are exempt).
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[monetisation-other]]** Make subscription tiers distinct sets of benefits; mutually exclusive tiers like Bronze/Silver/Gold are not supported, and players can own all subscriptions simultaneously.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[pricing]]** Robux subscriptions must be at least 49 Robux; local-currency subscriptions must use one of $2.99, $4.99, $7.99, $9.99, or $14.99.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[monetisation-other]]** Before going live, check whether the subscription is in supported regions/platforms; unsupported users can see the offer but cannot complete purchase.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[monetisation-other]]** Replacing a pass with a subscription: keep awarding legacy pass holders, take the pass off sale, and still listen to PromptGamePassPurchaseFinished while it remains on sale.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[first-session-onboarding]]** Offer in-game subscription purchase prompts in addition to the store listing; hide the prompt once the player owns the subscription, checking after about 10 seconds.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[common-mistakes]]** Do not check subscription status from the client; GetUserSubscriptionStatusAsync must run on the server. Handle UserSubscriptionStatusChanged to catch mid-session changes.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[pricing]]** Robux subscription price can only change once every 60 days, and increases need 30 days' notice. Local-currency prices cannot be changed; delete and recreate instead.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[business-and-payouts]]** Deleting an active local-currency subscription requires full refunds to subscribers. Prefer taking it off sale and cancelling renewals, then waiting for the period to end.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[business-and-payouts]]** Local-currency subscriptions pay 70% in month one and 100% after; Robux subscriptions pay 70% every month. Earnings are on a 30-day hold (Robux subscriptions about 5 days).
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[common-mistakes]]** Robux subscription purchases are not refundable, and cancellations do not auto-refund; refunds are handled case by case.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[analytics-metrics]]** Track new, renewed, resurrected subscribers and cancellations in the Creator Dashboard Analytics tab; use webhooks for real-time cancelled, purchased, refunded and renewed events.
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) **[[monetisation-other]]** Subscriptions cannot be cross-sold by other games and are ineligible for affiliate fees.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Max subscriptions per game: **50 (active + inactive combined)**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Minimum Robux subscription price: **49 Robux**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Local-currency price tiers: **$2.99, $4.99, $7.99, $9.99, $14.99**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Local-currency payout, month 1 vs later: **70% first month, 100% subsequent months**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Robux subscription payout: **70% every month**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Hold period, local currency / Robux: **30 days / ~5 days**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Robux subscription price change frequency: **once every 60 days**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Notice required for price increases: **30 days**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Delay before re-checking purchase in-game (sample code): **10 seconds**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Example: USD $5 local subscription, month 1 Robux earned: **350 Robux (500 Robux base x 0.7)**
- [page](https://create.roblox.com/docs/production/monetization/subscriptions) Local-currency unavailable countries: **Argentina, China, Colombia, India, Indonesia, Japan, Russia, Taiwan, Türkiye, UAE, Ukraine, Vietnam**

## Tools
MarketplaceService:GetUserSubscriptionStatusAsync, MarketplaceService:PromptSubscriptionPurchase, MarketplaceService:GetSubscriptionProductInfoAsync, MarketplaceService:GetUserSubscriptionPaymentHistoryAsync, Players.UserSubscriptionStatusChanged, MarketplaceService.PromptSubscriptionPurchaseFinished, Cloud API webhooks

## He points to
- Earn with subscriptions
- Webhook notifications
- Roblox Terms of Use
- Roblox Community Standards

## Topics
[[analytics-metrics]] [[business-and-payouts]] [[common-mistakes]] [[first-session-onboarding]] [[monetisation-other]] [[pricing]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
