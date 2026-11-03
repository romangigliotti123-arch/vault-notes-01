---
title: "Docs: production / promotion / ads-manager"
url: https://create.roblox.com/docs/production/promotion/ads-manager.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / ads-manager

[Open](https://create.roblox.com/docs/production/promotion/ads-manager.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox Creator Hub docs for Ads Manager: creating ad accounts, funding via card or Robux ad credits, campaign goals (Plays, Earnings, Engagement), audiences, budgets, creatives, join options with launch data, asset library, reporting attribution windows, status meanings, and billing/fraud refund rules.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Expect Engagement campaigns to have higher CPP; use a dedicated budget rather than shifting spend from Plays campaigns.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Allow 3–5 days for campaign results; if no progress by then, improve onboarding and first-time user experience before continuing.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Ad campaigns for games that are not unique can result in no ad spend and no conversions; metadata and place files resembling existing games rank lower.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Use Plays objective for broad distribution, testing new ideas, or initial traffic that can help get Recommended For You consideration.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Use Earnings objective only if your game has a well-developed in-game economy; it targets high-value spenders.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Use launch data to tailor onboarding per ad audience, spawn players at the ad's map, or grant ad-only rewards; exclusive rewards help conversion.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Test the launch URL before publishing a campaign with launch data; GetJoinData must be wired into onPlayerAdded.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Running ads does not affect Recommended For You ranking, so ads and organic recommendations are independent.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[analytics-metrics]]** Compare performance using Recent Users or Resurrected Users views; All Users can look low for retention, plays, or Robux revenue.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[thumbnails-icons]]** Upload up to 10 creatives per campaign and compare per-creative performance in campaign details; disable underperforming thumbnails.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[thumbnails-icons]]** Thumbnails display at 16:9; non-matching images are auto-resized, so design at 16:9 to control the crop.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Use Recent Players or Lapsed Players audiences only if the game meets 10,000 recent or 20,000 lapsed player minimums.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[analytics-metrics]]** Read Earnings ROAS as USD earnings attributed divided by spend; wait for Estimated ROAS to finalize as attribution windows close.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Cancel a campaign up to 6 hours before scheduled start to get ad credits back and avoid card charges.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[business-and-payouts]]** Robux converted to ad credits is irreversible and can only be spent in Ads Manager; convert only what you will spend.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Set auto-reload carefully: it reloads one day's worth of ad credits and continues daily to keep the campaign running.
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) **[[ads-and-sponsored-experiences]]** Payment method cannot be changed after a campaign is published; choose it before publishing.

## Numbers
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Min ad credit purchase: **1 ad credit** (Minimum for buying ad credits and converting Robux)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Card hold for verification: **$1.00 USD, refunded within 7 business days** (Temporary hold when adding card (18+ only))
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Recent Players minimum: **10,000 recent players** (Required for Recent Players audience)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Lapsed Players minimum: **20,000 lapsed players** (Required for Lapsed Players audience)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Audience recency split: **New: never played or 180+ days; Recent: last 30 days; Lapsed: 30–180 days** (Audience definitions)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Creatives per campaign: **up to 10** (Evenly distributed across players)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Cancel deadline: **6 hours before scheduled start** (Campaign cancellation window)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Ad moderation time: **within 24 hours** (Campaign moderation target)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Asset library moderation time: **typically within 48 hours; up to 10 files per upload** (Pre-moderated reusable assets)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Engagement results check: **if no progress after 3–5 days** (Then improve onboarding before continuing)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Learning phase: **first 24 hours of active campaign** (System refines budget allocation during this time)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Attribution windows: **New users 30D; Recent <7D (session only); Resurrected 7D (7–29 days lapsed); Resurrected 30D (30+ days lapsed)** (Plays and earnings credit windows)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Reporting delay: **up to 48 hours; attribution events up to 30 days after ad served** (Impressions and clicks are real time)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Initial billing threshold: **$5 USD charged on first credit card campaign** (First-time credit card users; applied to first bill)
- [page](https://create.roblox.com/docs/production/promotion/ads-manager) Ad fraud refund timing: **analysis at 14 days after campaign end; invalid-traffic refunds at 16 days** (Post-campaign fraud review)

## Tools
Ads Manager, Creator Hub, Roblox Studio

## He points to
- Ads Manager permissions guide
- Advanced join options docs
- Roblox advertising terms

## Topics
[[ads-and-sponsored-experiences]] [[analytics-metrics]] [[business-and-payouts]] [[thumbnails-icons]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
