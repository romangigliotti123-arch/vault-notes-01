---
title: "Docs: production / promotion / rewarded-video-ads"
url: https://create.roblox.com/docs/production/promotion/rewarded-video-ads.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / rewarded-video-ads

[Open](https://create.roblox.com/docs/production/promotion/rewarded-video-ads.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on rewarded video ads: placement guidance, reward rules (developer products, 3-10 Robux equivalent, no randomized rewards), client/server implementation using AdService, placements, ad opportunities, eligibility requirements, analytics metrics, and reward-strategy best practices.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[first-session-onboarding]]** Place rewarded videos in lobbies or menus where traffic is highest, since users are most likely to engage at gameplay start.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[core-loops-and-game-design]]** Show rewarded video ads at natural breaks: level completion, before a challenge, or when out of lives or resources, to avoid disruption.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[thumbnails-icons]]** Use prompts that need only 1-2 clicks and a clear call-to-action such as 'Watch this ad for 2x the coins!'.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[monetisation-devproducts]]** Offer rewards worth roughly 3 to 10 Robux (boosters, currency, extra lives, temporary privileges). Rewards cannot be randomized items.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[common-mistakes]]** Do not reward with Robux; rewards must be developer products. Do not let ads hurt the character; pause damage or show ads only in safe zones.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[ads-and-sponsored-experiences]]** Call GetAdAvailabilityNowAsync as close as possible to showing the ad (e.g., when the shop opens), not earlier, to improve fill rate and CPM.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[ads-and-sponsored-experiences]]** After an ad finishes, only call GetAdAvailabilityNowAsync if you will offer another ad opportunity, to avoid filled requests that never produce impressions.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[ads-and-sponsored-experiences]]** Disclose clearly before each ad what the reward is and what the user must do, e.g., 'Watch the ad to earn 10 diamonds!' on the button.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[ads-and-sponsored-experiences]]** Grant the reward immediately after the ad finishes; never force ads as a progress gate or take over screen or avatar motion.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[ads-and-sponsored-experiences]]** Use placements (Monetization > Ads > Placements) and pass the Placement ID to track each ad position separately.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[ads-and-sponsored-experiences]]** Register ad buttons with RegisterAdOpportunityAsync and compare filled requests, opportunities, and impressions to decide whether to make ads easier to find or rewards more compelling.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[monetisation-devproducts]]** Make rewards relevant to core mechanics, scaled to stay valuable as players progress, and limited-time or rare to boost engagement.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[monetisation-devproducts]]** Offer rewards at strategic moments such as after losing a life or completing a hard level, at intervals that do not trivialize progression.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[monetisation-other]]** Enable 'Exclude likely purchasers' only if users can choose between ad and purchase; do not enable it for unique rewards unavailable for Robux.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[analytics-metrics]]** Estimate earnings with the Eligibility calculator: eligible users (7-day) x ads per user x projected EPM. Daily ad views per user is the main lever you control.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[analytics-metrics]]** Track Opt-In Rate, DUV/eDAU, Frequency, AEPDUV, and EPM under Monetization > Ads > Analytics to judge rewarded video performance.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[analytics-metrics]]** Use experiments to roll a new ad placement out to a percentage of users first and measure engagement and retention before full rollout.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[ads-and-sponsored-experiences]]** Meet eligibility: 13+, ID-verified, 2FA enabled, public unrestricted game with at least 2,000 average unique visitors per month, and approved maturity questionnaire.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[common-mistakes]]** Resubmitting the Maturity questionnaire removes ads eligibility during review; only resubmit when a game update changes prior answers.
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) **[[monetisation-other]]** Violations of eligibility rules can cause account suspension, revoked ad payouts, or loss of ad eligibility; never offer fraudulent rewards like free Robux.

## Numbers
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) Ad length: **6 to 30 seconds** (Rewarded video is full-screen and rewards after completion)
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) Recommended reward value: **3 to 10 Robux** (Equivalent value of video ad reward)
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) Average unique visitors per month: **2,000** (Minimum for rewarded video ad eligibility)
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) Earnings formula: **EPM x impressions / 1000** (Total earnings = EPM times impressions in thousands)
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) Questionnaire re-review response time: **24 hours** (Response window for re-review requests of pending status)
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) Publisher age requirement: **13+** (Publisher must be 13+ years old)

## Tools
AdService, MarketplaceService, Creator Hub / Creator Dashboard, GetAdAvailabilityNowAsync, CreateAdRewardFromDevProductId, ShowRewardedVideoAdAsync, RegisterAdOpportunityAsync, ProcessReceipt

## He points to
- Roblox Creator Docs: Rewarded video ads
- Roblox Creator Docs: Experiments

## Quotes
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) "Rewards for video ads cannot be randomized items."
- [page](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) "Issue the reward to the user immediately after the rewarded video ad has finished playing."

## Topics
[[ads-and-sponsored-experiences]] [[analytics-metrics]] [[common-mistakes]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[monetisation-devproducts]] [[monetisation-other]] [[thumbnails-icons]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
