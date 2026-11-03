---
title: "Rewarded Video ads are now available to all ads eligible creators"
url: https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-11-11
views: 195
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Rewarded Video ads are now available to all ads eligible creators

[Open](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) | Roblox DevForum | 195 views | 2025-11-11

## Summary
Announces Rewarded Video ads for all ads-eligible creators. Covers eligibility (2,000 monthly unique visitors, 13+, 2FA, maturity questionnaire), setup steps (enable in Game Settings > Monetization, reward via developer product, GetAdAvailabilityNowAsync), the Creator Hub earnings forecaster, reduce-ads-for-payers toggle, new reporting, and the Home Recommendations impact.

## Tips
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[ads-and-sponsored-experiences]]** Only show the rewarded-ad button when GetAdAvailabilityNowAsync confirms an ad is available, so players never see a dead option.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[ads-and-sponsored-experiences]]** Reward players with a developer product's in-game item or currency. Robux cannot be given as the reward.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[ads-and-sponsored-experiences]]** If earnings fall below forecast, the likely cause is too few ad views per user. Compute Impressions / Ads Eligible DAU (eDAU) in Analytics and raise it via placement.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[ads-and-sponsored-experiences]]** If earnings drop to zero, check API ad-availability responses and moderation/publisher eligibility status before anything else.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[monetisation-other]]** Enable the reduce-ads-to-likely-payers toggle to stop showing ads to payers, which protects Robux spend from cannibalization.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[analytics-metrics]]** Use the experimentation platform to test ad impact on ARPU, ARPPU and payer conversion. Those revenue metrics exclude ad revenue.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[analytics-metrics]]** Use the new reporting filters on R$ EPM and fill rate, plus per-placement breakdowns, to tune ad placement.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[trend-research-and-validation]]** Use the Creator Hub Monetization > Ads forecaster to estimate ad earnings before launch, based on desired ad views per user.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[discovery-algorithm]]** Well-implemented rewarded video can raise spend and playtime, which helps Home Recommendations. Suppress payers if Robux spend per user drops.
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) **[[common-mistakes]]** Do not add rewarded ads to experiences with free-form user creation or AI interaction. They are ineligible.

## Numbers
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) Minimum unique monthly visitors: **2,000** (Public, unrestricted experience required for Rewarded Video eligibility)
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) Minimum creator age: **13+ (previously 18+)** (Creator must also have 2FA and ID verification)
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) Ad-metric formula for earnings shortfall: **Impressions / eDAU** (Ads Eligible DAU from Analytics tab; compare with forecast)
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) Content maturity review turnaround: **~1 day** (Status update after requesting review in Ads Content Maturity Queue (Feb 2026 update))

## Tools
Roblox Studio (Experience Settings > Monetization), Creator Hub forecaster (Monetization > Ads), GetAdAvailabilityNowAsync API, Experimentation platform, Self-service ads reporting

## He points to
- Rewarded Video Documentation
- Previous DevForum post on Rewarded Video
- Rewarded Video webinar
- Ads eligibility page (linked in documentation)

## Quotes
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) "As long as the experience has no free-form user creation or AI interaction, any public, unrestricted experience with over 2,000 unique monthly visitors can integrate Rewarded Video."
- [page](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278) "Monetization from advertising is not currently factored into the Home Recommendations algorithm."

## Topics
[[ads-and-sponsored-experiences]] [[analytics-metrics]] [[common-mistakes]] [[discovery-algorithm]] [[monetisation-other]] [[trend-research-and-validation]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
