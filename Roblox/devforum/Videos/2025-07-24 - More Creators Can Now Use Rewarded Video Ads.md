---
title: "More Creators Can Now Use Rewarded Video Ads"
url: https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-07-24
views: 375
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# More Creators Can Now Use Rewarded Video Ads

[Open](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) | Roblox DevForum | 375 views | 2025-07-24

## Summary
Roblox official update announcing Rewarded Video ads expansion to eligible creators (100K+ average DAU, minimal/mild maturity). Covers the AdService API implementation (client/server scripts with a dev product reward), earnings model (EPM x impressions), placement/reward optimization, eligibility rules, and expected revenue share of Rewarded Video (up to 3% initially).

## Tips
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[monetisation-other]]** Place rewarded ads at high-traffic points and raise reward value to increase the number of users who engage, which raises earnings.
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[monetisation-other]]** Expect Rewarded Video to make up to 3% of earnings in the first few months; Roblox targets 5-10% revenue growth from Roblox Ads products long term.
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[ads-and-sponsored-experiences]]** Only users 13+ see Rewarded Video; use GetAdAvailabilityNowAsync to show the button only when an ad is available so under-13 users never see the reward option.
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[scripting-and-performance]]** Create the reward dev product in the same universe as the place; the server calls CreateAdRewardFromDevProductId and ShowRewardedVideoAdAsync, then grants the reward in ProcessReceipt.
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[retention-d1-d7]]** Early tests showed users who watched rewarded ads also spent more Robux in-experience, so rewarded ads complement purchases rather than cannibalise them.
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[ads-and-sponsored-experiences]]** Expect higher EPMs with completion rates of 90%+ or Minimal content maturity; benchmark completion against the 85%+ industry expectation.
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[common-mistakes]]** Eligibility list refreshes every Monday; if still missing after a week, contact the Roblox team. Ads are not game-specific and sound settings are respected.
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) **[[ads-and-sponsored-experiences]]** Request a test universe via the form to run Rewarded Video in a non-monetised test experience before going live.

## Numbers
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) Eligibility threshold: **100K+ average DAU over past 28 days** (Initial self-service eligibility for Rewarded Video)
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) Ad length: **6-30 seconds, full-screen horizontal** (Rewarded Video placement format)
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) Expected completion rate: **85%+ industry; 90%+ earns higher EPM** (Advertiser benchmark for Rewarded Video)
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) Rewarded Video share of earnings: **Up to 3% in first few months** (Expected early contribution as platform scales)
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) Long-term revenue growth goal: **5-10% from Roblox Ads products** (Target for most creators in mid to long run)
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) User favourability: **87% favourable opinion** (Latitude study of surveyed users on Rewarded Video)
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) Minimum age: **13+** (Only users 13 and older see Rewarded Video ads)
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) Eligibility refresh: **Every Monday** (Refresh schedule for eligible experiences list)

## Tools
Roblox Studio, AdService API, Creator Hub

## He points to
- Creator Documentation
- Rewarded Video Newsroom Announcement
- Latitude brand lift study (Roblox Audience Impact, March 2024)

## Quotes
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) "Eligible creators earn Robux for every ad shown within their experience, and early tests have shown that users who view ads spend more Robux within experiences."
- [page](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678) "Creators own the implementation within their game, including reward prompt, frequency, reward value, and reward type."

## Topics
[[ads-and-sponsored-experiences]] [[common-mistakes]] [[monetisation-other]] [[retention-d1-d7]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
