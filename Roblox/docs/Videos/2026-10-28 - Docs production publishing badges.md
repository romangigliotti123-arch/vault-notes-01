---
title: "Docs: production / publishing / badges"
url: https://create.roblox.com/docs/production/publishing/badges.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / publishing / badges

[Open](https://create.roblox.com/docs/production/publishing/badges.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on badges: creating badges (free quota of 5 per 24h GMT per game, extra cost 100 Robux each, 512x512 icon with circular crop), reordering (up to 50 at once), and scripting with BadgeService to award, check, and fetch badge info.

## Tips
- [page](https://create.roblox.com/docs/production/publishing/badges) **[[first-session-onboarding]]** Badges display in the player's inventory Badges category once earned; enable badges to show them on the game's main page.
- [page](https://create.roblox.com/docs/production/publishing/badges) **[[development-process-and-speed]]** Only 5 badges per game are free per 24-hour GMT period; each extra badge in that window costs 100 Robux, so plan badge creation in batches.
- [page](https://create.roblox.com/docs/production/publishing/badges) **[[thumbnails-icons]]** Use a 512x512 template for badge icons and keep key content inside the circle, since upload trims and crops the image into a circle; text outside gets cut off.
- [page](https://create.roblox.com/docs/production/publishing/badges) **[[common-mistakes]]** Disabled badges are hidden from the game page and cannot be earned, so check Badge is Enabled before players are expected to earn it.
- [page](https://create.roblox.com/docs/production/publishing/badges) **[[scripting-and-performance]]** Award badges only from server-side Scripts, and call GetBadgeInfoAsync first to confirm IsEnabled before AwardBadgeAsync, wrapping both in pcall.
- [page](https://create.roblox.com/docs/production/publishing/badges) **[[scripting-and-performance]]** Use UserHasBadgeAsync in PlayerAdded to check ownership, or GetUserBadgesAsync to check many badges in batches.
- [page](https://create.roblox.com/docs/production/publishing/badges) **[[development-process-and-speed]]** Reorder up to 50 badges at once via drag-and-drop on the Reorder page; new badges appear at the end of the list by default.

## Numbers
- [page](https://create.roblox.com/docs/production/publishing/badges) Free badge creations: **5 per game per 24-hour period (GMT)**
- [page](https://create.roblox.com/docs/production/publishing/badges) Extra badge cost: **100 Robux each beyond free quota**
- [page](https://create.roblox.com/docs/production/publishing/badges) Badge icon size: **512x512 pixels**
- [page](https://create.roblox.com/docs/production/publishing/badges) Reorder limit: **50 badges at once**

## Tools
Creator Dashboard, BadgeService (AwardBadgeAsync, GetBadgeInfoAsync, UserHasBadgeAsync, GetUserBadgesAsync)

## He points to
- Roblox Creator Docs: Badges

## Topics
[[common-mistakes]] [[development-process-and-speed]] [[first-session-onboarding]] [[scripting-and-performance]] [[thumbnails-icons]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
