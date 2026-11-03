---
title: "Building Connected Experiences with Roblox’s APIs | RDC 2025"
url: https://youtu.be/lUc3Xj8Ojd8
creator: Roblox
official: true
advice_density: medium
date: 2025-09-26
views: 15875
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Building Connected Experiences with Roblox’s APIs | RDC 2025

[Watch](https://youtu.be/lUc3Xj8Ojd8) | RobloxOfficial | 15,875 views | 2025-09-26

## Summary
RDC 2025 session on Roblox social APIs: text chat (TCS) performance and roadmap, voice chat APIs, Party API, Communities/Forums and join-community APIs, and Moments capture/publish/consume with Capture and Recommendations APIs. Mostly platform announcements with few creator tactics.

## Tips
- [2:44](https://youtu.be/lUc3Xj8Ojd8?t=164) **[[social-features-and-virality]]** Design for co-play: players who play with friends stay longer, return more often, and spend about twice as much, per the speaker.
- [6:32](https://youtu.be/lUc3Xj8Ojd8?t=392) **[[social-features-and-virality]]** Add voice using the new voice chat APIs; team voice can be set up in a few lines of code, and custom distance attenuation curves tune falloff.
- [9:36](https://youtu.be/lUc3Xj8Ojd8?t=576) **[[social-features-and-virality]]** Use the Party API to show where party members are, keep parties on the same team, and give shared rewards to bring groups back.
- [13:12](https://youtu.be/lUc3Xj8Ojd8?t=792) **[[community-and-discord]]** Use Open Cloud to sync in-game milestones (e.g. level 10) to community roles that unlock forum posting.
- [16:04](https://youtu.be/lUc3Xj8Ojd8?t=964) **[[social-features-and-virality]]** Trigger captures at key moments (challenge complete, rare item, race finish) via CaptureService, but a player must consent to save or share.
- [20:51](https://youtu.be/lUc3Xj8Ojd8?t=1251) **[[social-features-and-virality]]** Register captures as recommendation items with tags and attributes, then customize ranking weights (e.g. challenge-of-the-week tags) with the Recommendations API.
- [5:15](https://youtu.be/lUc3Xj8Ojd8?t=315) **[[scripting-and-performance]]** Chat frame time is now under 1 ms on all platforms, and it costs zero frame time when chat is turned off.

## Numbers
- [2:44](https://youtu.be/lUc3Xj8Ojd8?t=164) Daily co-experience hours on Roblox: **~79 million** (Speaker's platform-wide figure)
- [3:13](https://youtu.be/lUc3Xj8Ojd8?t=193) Daily chat conversations / users: **4B+ conversations, 80M+ users per day** (Experience text chat, platform-wide)
- [5:51](https://youtu.be/lUc3Xj8Ojd8?t=351) Daily active voice users: **12M+** (Voice in experiences)
- [5:51](https://youtu.be/lUc3Xj8Ojd8?t=351) Voice users still on platform ~6 weeks later: **58%+** (Speaker's figure for voice users)
- [5:51](https://youtu.be/lUc3Xj8Ojd8?t=351) Top 10,000 creators with voice enabled: **61%+** (Share of top creators)
- [5:15](https://youtu.be/lUc3Xj8Ojd8?t=315) Chat frame time: **under 1 ms on all platforms** (Including Android after optimisation)
- [11:48](https://youtu.be/lUc3Xj8Ojd8?t=708) Communities daily players: **~5 million** (Daily engagement with Communities)
- [16:04](https://youtu.be/lUc3Xj8Ojd8?t=964) Moments clip length: **up to 30 seconds** (Captured on supported devices, on by default)

## Games
- **Rivals** [11:00](https://youtu.be/lUc3Xj8Ojd8?t=660): Used Party API so joined groups are matchmade together and kept together across subplaces.

## Tools
Text Chat Service (TCS), Voice chat / Audio API, Party API (Studio support planned), Open Cloud API, Join Community API (coming), Forum API (coming), CaptureService

## He points to
- Roblox DevForum (API dates and details)

## Quotes
- [9:36](https://youtu.be/lUc3Xj8Ojd8?t=576) "Players who co-play stay longer, return more often, and drive higher DAU. They often end up spending almost twice as much in your experiences."
- [16:04](https://youtu.be/lUc3Xj8Ojd8?t=964) "On supported devices, players can record short clips up to 30 seconds long right from your experience, and it's on by default."

## On screen
Slides show voice chat code sample and config options, a ~5M/day Communities stat, Moments capture/publish/consume diagram, party-as-a-system UI mockups, and code for CaptureService and Recommendations API.

## Topics
[[community-and-discord]] [[scripting-and-performance]] [[social-features-and-virality]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
