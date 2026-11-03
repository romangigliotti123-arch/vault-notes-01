---
title: "Roblox Developer Conference 2018 - Building Games for Reach"
url: https://youtu.be/a2DaoXERzhE
creator: Roblox
official: true
advice_density: medium
date: 2018-07-24
views: 3729
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Roblox Developer Conference 2018 - Building Games for Reach

[Watch](https://youtu.be/a2DaoXERzhE) | RobloxOfficial | 3,729 views | 2018-07-24

## Summary
Roblox DevConf 2018 talk by Klaus Moberg (senior engineering director) on building for reach: total addressable market (TAM) as the growth ceiling. Covers platform (PC, mobile, Xbox, tablets), country, and age trends, plus advice on cross-platform UI, not forking control scripts, string tables/localization, and form-factor APIs.

## Tips
- [4:40](https://youtu.be/a2DaoXERzhE?t=280) **[[building-art-and-assets]]** Use string tables and Roblox localization infrastructure from the start; missing them caps your addressable market (e.g. Spanish-speaking audience) for good.
- [3:59](https://youtu.be/a2DaoXERzhE?t=239) **[[common-mistakes]]** Avoid forking control scripts per platform unless intentional; a PC-only fork cuts off console/tablet/mobile players from day one.
- [17:55](https://youtu.be/a2DaoXERzhE?t=1075) **[[building-art-and-assets]]** Use UI layouts and dynamic constraints instead of hard-coded pixel sizes so UI scales across devices.
- [21:28](https://youtu.be/a2DaoXERzhE?t=1288) **[[playtesting-and-feedback]]** Test on real low-end Android devices if possible; otherwise use Studio's emulator across multiple screen sizes to catch UI bugs.
- [20:41](https://youtu.be/a2DaoXERzhE?t=1241) **[[building-art-and-assets]]** Abstract how players interact with game systems so your game keeps working on future platforms without rework.
- [12:20](https://youtu.be/a2DaoXERzhE?t=740) **[[game-ideas-and-genres]]** Choose an age demographic deliberately; content for under-9s rarely appeals to 17-year-olds, but owning one segment can beat a diluted broad audience.
- [13:01](https://youtu.be/a2DaoXERzhE?t=781) **[[monetisation-other]]** Estimate revenue potential as players times spend per player per age group, since spending power differs sharply by demographic.
- [5:20](https://youtu.be/a2DaoXERzhE?t=320) **[[mindset-and-strategy]]** Make platform, language and age-targeting decisions intentionally with data, since each choice sets your long-term market ceiling.
- [9:02](https://youtu.be/a2DaoXERzhE?t=542) **[[roblox-platform-changes]]** Xbox player count on Roblox grew steadily after release, unlike typical console titles that spike then decline; Roblox monetises better per player on that platform.
- [10:24](https://youtu.be/a2DaoXERzhE?t=624) **[[trend-research-and-validation]]** Watch international growth: Spanish-speaking countries rose after Spanish localization tools shipped; expect East Asian language support to matter next.

## Numbers
- [3:17](https://youtu.be/a2DaoXERzhE?t=197) Monthly active users: **62 million MAU on Roblox (2018)**
- [3:59](https://youtu.be/a2DaoXERzhE?t=239) Platform audience lost by PC-only controls: **About 4 million MAU on other platforms (speaker's approximate, unverified)**
- [4:40](https://youtu.be/a2DaoXERzhE?t=280) Hypothetical TAM without Spanish localization: **Speaker illustrates ~30 million vs 62 million (illustrative)**
- [7:39](https://youtu.be/a2DaoXERzhE?t=459) Platform mix shift: **July 2016 PC dominated; by 2018 iOS + Android combined nearly equal to PC and soon larger**
- [11:38](https://youtu.be/a2DaoXERzhE?t=698) Age mix: **Under-9 segment growing fast, approaching the core 9-13 segment; 12-13+ also growing**

## Tools
Studio emulator (device/screen-size testing), Internal Roblox tool showing live player locations (not public), String tables / Roblox localization infrastructure

## He points to
- Chris Miziners keynote (internationalization)
- Deepak Circus talk on upcoming age rating system

## Quotes
- [3:59](https://youtu.be/a2DaoXERzhE?t=239) "If you fork the player scripts to do that, there is now an Xbox-shaped hole in your total addressable market."
- [18:35](https://youtu.be/a2DaoXERzhE?t=1115) "We can't forecast what Nintendo is going to come out with three years after this, so we won't add an API for form factor."

## On screen
Contact sheet shows the weekly average player count charts by platform (PC, Xbox, iOS, Android, OSX, UWP), by country (top 10 non-US, incl. Spanish-speaking countries), and user-by-age-group stacked area chart. Axes unlabeled with numbers, so no absolute values are visible. Also a Nintendo Switch slide at 19:14 with "What form factor is this thing?" and an internal global player-map slide was described verbally only.

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[game-ideas-and-genres]] [[mindset-and-strategy]] [[monetisation-other]] [[playtesting-and-feedback]] [[roblox-platform-changes]] [[trend-research-and-validation]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
