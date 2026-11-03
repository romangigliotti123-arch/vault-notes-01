---
title: "Docs: production / monetization / immersive-ads"
url: https://create.roblox.com/docs/production/monetization/immersive-ads.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / immersive-ads

[Open](https://create.roblox.com/docs/production/monetization/immersive-ads.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on Immersive ads: billboard video/image ads and portal ads, how publishers earn per click-to-play view, autoplay/image impression, or teleport; eligibility requirements; ad unit sizing and validity; removing ads for ineligible users via PolicyService; and viewing ad metrics in the Creator Dashboard.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Only public games with a 13+ owner, ID verification, and 2FA are eligible; game needs 2,000 unique monthly visitors (bots excluded).
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Complete the Maturity and Compliance Questionnaire; resubmitting temporarily removes ads eligibility, so only resubmit when a game update changes prior answers.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Scale billboard ad blocks between 8x4.5 and 32x18 studs; out-of-range ad units are invalid and cannot serve ads.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Do not add a second AdGui or SurfaceGui on the same ad face; it invalidates the ad unit.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Portal ad BasePortal package: only scale, position, and rotation may change; other edits invalidate it and it stops serving.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Pair click-to-play video ads with a rewarded video mechanism to drive users to watch at least 15 seconds.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Ineligible users see a Roblox logo fallback by default; to comply with Advertising Standards, hide, replace, or block ads for them using PolicyService:GetPolicyInfoForPlayerAsync AreAdsAllowed.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[ads-and-sponsored-experiences]]** Destroying ad units for some users can change gameplay if other users still see them; account for this in design.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[analytics-metrics]]** Check Monetization > Ads metrics after 48 hours of ads running to see views, impressions, teleports, and per-ad-unit Robux earned.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[analytics-metrics]]** Name ad units distinctly in Studio; metrics graphs per ad unit use the Studio instance name.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[common-mistakes]]** Do not manipulate impressions or teleports; Roblox may deduct or reclaim Robux, and may suspend the game or account for fraud.
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) **[[business-and-payouts]]** Ad earnings pay out on the 25th of the following month; track them in My Transactions or Group Transactions.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Unique monthly visitors required for ad eligibility: **2,000**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Billboard minimum size: **8 x 4.5 studs**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Billboard maximum size: **32 x 18 studs**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Click-to-play video paid view: **15 seconds watched**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Autoplay video impression: **0.5s look, 1.5% viewport, within 55 degrees, 50% pixels visible**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Image impression: **1s look, 1.5% viewport, within 55 degrees, 50% pixels visible**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Maximum billboard video length: **30 seconds**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Questionnaire re-review response time: **within 24 hours**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Ad payout date: **25th of following month**
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) Delay before ad metrics appear: **48 hours**

## Tools
Roblox Studio, Creator Store (Ads portal and image packages), PolicyService, Creator Dashboard

## He points to
- Roblox Advertising Standards
- Billing (advertiser billing docs)
- Maturity and Compliance Questionnaire

## Quotes
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) "Eligibility does not guarantee Roblox will serve ads in your game, and nothing obligates Roblox to serve ads into your game."
- [page](https://create.roblox.com/docs/production/monetization/immersive-ads) "if you engage in malicious practices to inflate impressions or teleports, Roblox might deduct Robux from your expected payout or reclaim the Robux you earned"

## Topics
[[ads-and-sponsored-experiences]] [[analytics-metrics]] [[business-and-payouts]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
