---
title: "How to Make Server-Synced Daily Shops"
url: https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-06-18
views: 548
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Make Server-Synced Daily Shops

[Open](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) | Roblox DevForum | 548 views | 2020-06-18

## Summary
Tutorial on building a server-synced daily rotating shop in Roblox. Uses Google HTTP time (SyncedTime module) so all servers agree on reset time, seeded Random for identical item sets, duplicate-free selection, weighted rarity via weight intervals, and a countdown timer. Includes offset calculation for custom reset times.

## Tips
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[scripting-and-performance]]** Avoid plain os.time() for cross-server sync; author reported servers drifting 3-5 minutes apart. Fetch time externally via the Google HTTP Date header.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[anti-exploit-and-security]]** Keep daily shop rotation logic on the server (ServerStorage/ServerScriptService) so it is not replicated to clients.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[scripting-and-performance]]** Seed Random.new() with the day number so every server generates the same shop items without communicating.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[scripting-and-performance]]** Floor the day value so the seed only changes when a full day boundary passes.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[core-loops-and-game-design]]** Set the reset time by computing an hour offset from 00:00 UTC in your local timezone.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[core-loops-and-game-design]]** Generate fewer shop items than the total item pool, otherwise duplicates cannot be avoided.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[testing-debugging-and-qa]]** Give every item a unique name; identical names make the duplicate-respin loop spin forever.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[core-loops-and-game-design]]** Implement rarity with ordered weight intervals (rarest first) and NextNumber for decimal-precise weights.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[core-loops-and-game-design]]** Prevent duplicates by respinning only from a copy of the rarity pool with already-chosen items removed.
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) **[[core-loops-and-game-design]]** Enable HTTP Requests in Game Settings > Options before using the Google time fetch module.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) Server clock drift reported with os.time(): **3-5 minutes** (Author's reported drift between servers before switching to external time)
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) Rarity weights example: **Common 100, Rare 25, Legendary 2** (Intervals on NextNumber(0,100): 0-2 Legendary, 2-25 Rare, 25-100 Common)
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) Shop size in example: **5 items from 9-item pool** (Sample tutorial configuration)
- [page](https://devforum.roblox.com/t/how-to-make-server-synced-daily-shops/632401) Seconds per day: **86400** (Used for day seed and countdown calculation)

## Games
- **Arsenal**: Cited as the reference example of a self-rotating daily shop synced across all servers.

## Tools
Roblox Studio, Random (Luau), HttpService, os.time, SyncedTime ModuleScript

## He points to
- @XAXA synced time module (Google-based time)
- @VitalWinter (helped with code)

## Topics
[[anti-exploit-and-security]] [[core-loops-and-game-design]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
