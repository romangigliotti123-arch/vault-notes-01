---
title: "Docs: production / promotion / deeplinks"
url: https://create.roblox.com/docs/production/promotion/deeplinks.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / promotion / deeplinks

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/production/promotion/deeplinks.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on deep links: URL formats (web list to app, direct to app, deferred via AppsFlyer), URL parameters (placeId, userId, accessCode, linkCode, gameInstanceId, launchData), encoding and size rules, and how to read launch data with Player:GetJoinData(). Notes the format is deprecated in favor of share links.

## Tips
- [page](https://create.roblox.com/docs/production/promotion/deeplinks) **[[titles-descriptions]]** Do not put confidential information in launchData; it is fully visible in the URL and users can modify it, so data may not be authentic.
- [page](https://create.roblox.com/docs/production/promotion/deeplinks) **[[social-features-and-virality]]** Use share links instead of deep links for creating public deep links, since this deep link process is deprecated.
- [page](https://create.roblox.com/docs/production/promotion/deeplinks) **[[ads-and-sponsored-experiences]]** Use deep links with launchData for traffic attribution and promotional codes so players land in a specific place with context.
- [page](https://create.roblox.com/docs/production/promotion/deeplinks) **[[social-features-and-virality]]** Use userId in a deep link to send players to a friend's current server; it fails with 'Followed user has left the game' if they are offline.

## Numbers
- [page](https://create.roblox.com/docs/production/promotion/deeplinks) launchData max size: **200 bytes decoded** (Decoded launch data cannot exceed this limit; use JSON string for complex data)

## Tools
Player:GetJoinData(), HttpService:JSONDecode(), AppsFlyer

## Topics
[[ads-and-sponsored-experiences]] [[social-features-and-virality]] [[titles-descriptions]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
