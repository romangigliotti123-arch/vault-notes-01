---
title: "How to make a simple global leaderboard"
url: https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-03-23
views: 961
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to make a simple global leaderboard

[Open](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) | Roblox DevForum | 961 views | 2019-03-23

## Summary
Tutorial for building a global leaderboard in Roblox using an OrderedDataStore, a Surface GUI with a ScrollingFrame, and a looping script that updates and fetches the top 100 every 2 minutes. Covers daily/monthly/yearly resets via date-based keys. Notes PointsService deprecation (June 30, 2023 removal) and how to swap in leaderstats.

## Tips
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) **[[data-persistence]]** Use GetOrderedDataStore for leaderboards so Roblox sorts entries server-side instead of you sorting thousands of records.
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) **[[data-persistence]]** Wrap DataStore UpdateAsync calls in pcall so a Roblox outage does not error and break the loop.
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) **[[analytics-metrics]]** Change the OrderedDataStore key to create separate leaderboards or reset data; use date-based keys (day/month/year) for periodic resets.
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) **[[ui-ux-design]]** Give leaderboard rows gold/silver/bronze colours for places 1-3 and a header bar to make the board look appealing.
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) **[[common-mistakes]]** Do not rely on PointsService; Roblox announced its removal on June 30 (2023), so reroute the value to leaderstats or your own data.
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) **[[ui-ux-design]]** If a part blocks scrolling on a Surface GUI leaderboard, move the Surface GUI part forward so the ScrollingFrame sits above it.
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) **[[scripting-and-performance]]** Refresh leaderboard fetches on a long interval (tutorial uses 120 seconds) to limit DataStore and thumbnail request load.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) Leaderboard refresh interval: **120 seconds** (wait(120) loop in tutorial script)
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) Entries fetched: **100** (numberToShow in GetSortedAsync, max 100 per page)
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) ScrollBarThickness: **20** (Recommended scrollBarThickness for ScrollingFrame)
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) Headshot thumbnail size: **150x150** (GetUserThumbnailAsync HeadShot Size150x150)
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) Physical leaderboard part size: **6x9x1** (Example part used for Surface GUI leaderboard)

## Games
- **The Tower Tycoon**: Author's game where this leaderboard was used; shows players competing for a visible rank and name.

## Tools
Roblox Studio, DataStoreService (OrderedDataStore), Surface GUI, ScrollingFrame, UIListLayout, PointsService (deprecated), Players:GetNameFromUserIdAsync, Players:GetUserThumbnailAsync

## He points to
- ThatTimothy DevForum tutorial (original post)
- Leaderboard With Script Working DEMO.rbxl (downloadable)
- Global Leaderboard With Script.rbxm (downloadable model)

## Quotes
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) "Roblox has recently announced their plan to remove support for PointsService on June 30th."
- [page](https://devforum.roblox.com/t/how-to-make-a-simple-global-leaderboard/256754) "Players want to become the best of them all, and will work hard to compete to become the best."

## Topics
[[analytics-metrics]] [[common-mistakes]] [[data-persistence]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
