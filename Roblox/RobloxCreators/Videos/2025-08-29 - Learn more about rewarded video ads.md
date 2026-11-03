---
title: "Learn more about rewarded video ads"
url: https://youtu.be/7AtvvUxvCaU
creator: Roblox Creators
official: true
advice_density: high
date: 2025-08-29
views: 2779
transcript: auto-captions
confidence: high
tags: [roblox, robloxcreators, youtube-learn]
---

# Learn more about rewarded video ads

[Watch](https://youtu.be/7AtvvUxvCaU) | RobloxCreators | 2,779 views | 2025-08-29

## Summary
Roblox Rewarded Video Ads webinar (Nick McLaughlin, product marketing, and Patrick McInness, PM, Ads & Brands). Covers what rewarded video is, placement and frequency best practices, the Developer API (get ad availability, eligibility), earnings levers (EPM, opt-in rate, impressions, reward rate), reporting, eligibility (100K+ DAU, mild/minimal maturity) and the roadmap.

## Tips
- [6:53](https://youtu.be/7AtvvUxvCaU?t=413) **[[retention-d1-d7]]** Cap rewarded ads per user per day; high end seen is 5-10. Let players bank watches across sessions rather than forcing all in one session.
- [17:45](https://youtu.be/7AtvvUxvCaU?t=1065) **[[pricing]]** Set rewarded reward value around 3-10 Robux equivalent so players don't abandon mid-ad; experiment from there.
- [16:25](https://youtu.be/7AtvvUxvCaU?t=985) **[[core-loops-and-game-design]]** Place rewarded prompts in high-traffic areas (lobbies, menus) and at natural gameplay breaks, never mid-chase or mid-action.
- [17:05](https://youtu.be/7AtvvUxvCaU?t=1025) **[[first-session-onboarding]]** Make the ad prompt clear about the reward and that it is an ad; keep it reachable in a few clicks, not six menu levels deep.
- [24:40](https://youtu.be/7AtvvUxvCaU?t=1480) **[[scripting-and-performance]]** Call get ad availability before showing the watch button, and again after each watch; calling once per session yields only one ad.
- [25:21](https://youtu.be/7AtvvUxvCaU?t=1521) **[[scripting-and-performance]]** Call availability close to when the player can actually press the button; calling too early lowers impression rate and EPM.
- [27:09](https://youtu.be/7AtvvUxvCaU?t=1629) **[[scripting-and-performance]]** Never show ad prompts to ineligible (under-13) users; check the Eligibility API separately if not using availability checks.
- [17:45](https://youtu.be/7AtvvUxvCaU?t=1065) **[[common-mistakes]]** Rewards must be deterministic and clearly described; randomized rewards violate compliance (tickets for a later random draw are allowed).
- [18:26](https://youtu.be/7AtvvUxvCaU?t=1106) **[[common-mistakes]]** Test rewarded ad flows in Studio before release to catch compliance issues; moderation reacts to user reports and reviews new implementations.
- [12:03](https://youtu.be/7AtvvUxvCaU?t=723) **[[common-mistakes]]** Spamming ads makes players leave; if exposure is limited, you may have room to raise ad load and test the trade-off.
- [22:35](https://youtu.be/7AtvvUxvCaU?t=1355) **[[monetisation-devproducts]]** Estimate cannibalisation of payers conservatively: cap the value of a rewarded item at roughly 100x earnings per ad view; track earnings per ad view in Creator Hub.
- [23:18](https://youtu.be/7AtvvUxvCaU?t=1398) **[[monetisation-gamepasses]]** Offer time-limited trials of high-value game passes through rewarded ads, as Brook Haven did, instead of creating many small items.
- [40:27](https://youtu.be/7AtvvUxvCaU?t=2427) **[[core-loops-and-game-design]]** Make the reward something players value within the game loop (skins, abilities, area access); Basketball Zero saw 8x impressions from this.
- [39:04](https://youtu.be/7AtvvUxvCaU?t=2344) **[[ads-and-sponsored-experiences]]** Increase prominence of the rewarded prompt; Rivals got roughly 4x impressions almost overnight from a discoverability change alone.
- [37:16](https://youtu.be/7AtvvUxvCaU?t=2236) **[[analytics-metrics]]** Watch opt-in rate and impression rate: low opt-in means players can't find the ad or don't find the reward compelling.
- [38:24](https://youtu.be/7AtvvUxvCaU?t=2304) **[[analytics-metrics]]** Check downstream impact: engagement, playtime and retention in normal creator analytics alongside ad metrics; any negative effect is a warning sign.
- [45:20](https://youtu.be/7AtvvUxvCaU?t=2720) **[[roblox-platform-changes]]** Current eligibility: publisher eligibility plus 100K+ average DAU over 28 days and minimal/mild maturity label. Prepare implementations now for broader access.
- [8:15](https://youtu.be/7AtvvUxvCaU?t=495) **[[core-loops-and-game-design]]** Rewarded ads can be simple; reference code in docs. Fit the reward to the game's look and feel, but a heavy custom build is optional.
- [44:39](https://youtu.be/7AtvvUxvCaU?t=2679) **[[monetisation-other]]** Low-paying games with many users can gain significantly from a rewarded prompt, as Easy Glass Bridge did with a skip-ahead reward.
- [31:14](https://youtu.be/7AtvvUxvCaU?t=1874) **[[ads-and-sponsored-experiences]]** Prefer 6-15 second ad length; the platform accepts up to 30 seconds.
- [30:34](https://youtu.be/7AtvvUxvCaU?t=1834) **[[analytics-metrics]]** Treat unvalidated ad data as provisional; it is still being debotted for a couple of days after events.

## Numbers
- [3:53](https://youtu.be/7AtvvUxvCaU?t=233) Ad completion rate: **80-90%+ average for alpha campaigns** (Brand-side completion for rewarded video, per Roblox)
- [3:53](https://youtu.be/7AtvvUxvCaU?t=233) Player opinion: **87% favourable opinion of rewarded video** (Roblox user study)
- [3:53](https://youtu.be/7AtvvUxvCaU?t=233) Creators using rewarded video: **100+** (Creators already using it as a new earning way)
- [6:53](https://youtu.be/7AtvvUxvCaU?t=413) Ads per user per day: **Up to 5-10 high end** (Platform limits per user per day; experiment)
- [18:26](https://youtu.be/7AtvvUxvCaU?t=1106) Recommended reward value: **3-10 Robux** (Reward value to keep reward rate high)
- [22:35](https://youtu.be/7AtvvUxvCaU?t=1355) Max item value guideline: **~100x earnings per single ad view** (Rough cannibalisation first-pass heuristic)
- [40:27](https://youtu.be/7AtvvUxvCaU?t=2427) Basketball Zero impressions: **8x increase** (From making reward meaningful within game loop)
- [39:46](https://youtu.be/7AtvvUxvCaU?t=2386) Rivals impressions: **4x almost overnight** (From improving discoverability of rewarded prompt)
- [44:39](https://youtu.be/7AtvvUxvCaU?t=2679) Typical earnings uplift referenced: **3, 5, 10% on slide** (Earnings uplift, smaller creators seeing well above these)
- [45:20](https://youtu.be/7AtvvUxvCaU?t=2720) Eligibility threshold: **100K+ average DAU over 28 days, minimal or mild maturity** (Current access requirement; broader access coming)
- [31:14](https://youtu.be/7AtvvUxvCaU?t=1874) Ad length: **6-30 seconds; 6-15 recommended** (Full-screen horizontal video ads)
- [33:16](https://youtu.be/7AtvvUxvCaU?t=1996) Local demand share: **~96% of ads bought locally** (Speaker's past-life figure, relevant to direct sales)
- [11:22](https://youtu.be/7AtvvUxvCaU?t=682) Minimum user age: **13+** (Ads only served to users 13 and over)

## Games
- **Spongebob Tower Defense** [4:50](https://youtu.be/7AtvvUxvCaU?t=290): Visible rewarded option in shop, stacked multiple ad views for different rewards, used between-level downtime.
- **Easy Glass Bridge** [7:34](https://youtu.be/7AtvvUxvCaU?t=454): Ad offers skip-ahead bridge when players are stuck; low-monetising obby saw significant earnings lift.
- **Brook Haven** [9:18](https://youtu.be/7AtvvUxvCaU?t=558): Time-limited trials of premium game passes via ad let non-payers sample high-value items without economy changes.
- **Rivals** [39:04](https://youtu.be/7AtvvUxvCaU?t=2344): Improved discoverability of rewarded prompt for about 4x impressions in one update.
- **Basketball Zero** [40:27](https://youtu.be/7AtvvUxvCaU?t=2427): Rewards tied to in-game value (skins, abilities) drove about 8x impressions.

## Tools
Roblox Studio, Creator Hub (ads analytics), Rewarded Video Developer API (GetAdAvailability, Eligibility API)

## He points to
- Roblox Learn
- Roblox help center rewarded video documentation
- Roblox dev forum post on rewarded video

## Quotes
- [22:35](https://youtu.be/7AtvvUxvCaU?t=1355) "You certainly shouldn't think every single ad is stealing someone away who was going to buy it."
- [12:44](https://youtu.be/7AtvvUxvCaU?t=764) "If you spam users, they'll probably go out of the game and leave."
- [25:21](https://youtu.be/7AtvvUxvCaU?t=1521) "Calling it once at the beginning of the session doesn't mean that they can watch five or 10 ads."

## On screen
Contact sheet shows Easy Glass Bridge in-game 'SKIP TO END' ad prompt with a 50% progress bar and a bridge reward; Developer API settings toggle in Studio Game Settings > Monetization; Creator Hub reporting showing EPM and impressions graphs. Adds UI detail only; no extra numbers readable.

## Topics
[[ads-and-sponsored-experiences]] [[analytics-metrics]] [[common-mistakes]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[monetisation-devproducts]] [[monetisation-gamepasses]] [[monetisation-other]] [[pricing]] [[retention-d1-d7]] [[roblox-platform-changes]] [[scripting-and-performance]]

Back to [[RobloxCreators - How to make successful Roblox games]]
