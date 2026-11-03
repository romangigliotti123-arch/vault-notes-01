---
title: "How to Make a Roblox Simulator Game (Pets & Rebirths)"
url: https://youtu.be/Oj0nbY61qsY
creator: Generalist Programmer
official: false
advice_density: medium
date: 2026-07-07
views: 72
transcript: auto-captions
confidence: high
tags: [roblox, generalistprogrammer3233, youtube-learn]
creator_trust: MIXED
creator_score: 7.1
---

> [!note] Trust: MIXED (credibility audit score 7.1): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# How to Make a Roblox Simulator Game (Pets & Rebirths)

[Watch](https://youtu.be/Oj0nbY61qsY) | generalistprogrammer3233 | 72 views | 2026-07-07

## Summary
Builds a Roblox simulator from scratch in ~8 minutes: one core loop (click, earn coins, spend, rebirth for permanent multiplier), leaderstats display, server-side click earning, RemoteEvent-based rebirth, pet multiplier value, and DataStore saving. Mostly a scripting walkthrough with a product pitch.

## Tips
- [0:50](https://youtu.be/Oj0nbY61qsY?t=50) **[[core-loops-and-game-design]]** Build simulators around one loop: click to earn, spend on upgrades, rebirth for a permanent multiplier. Each lap should feel faster than the last.
- [1:32](https://youtu.be/Oj0nbY61qsY?t=92) **[[client-server-and-remotes]]** Keep all coin changes on the server. Client-controlled currency lets players give themselves unlimited coins.
- [1:51](https://youtu.be/Oj0nbY61qsY?t=111) **[[analytics-metrics]]** Store coins and rebirths in a leaderstats folder under the player; Roblox renders them on the leaderboard automatically.
- [2:42](https://youtu.be/Oj0nbY61qsY?t=162) **[[scripting-and-performance]]** In a server Script, ClickDetector.MouseClick already gives the player on the server, so earning doesn't need a RemoteEvent.
- [3:41](https://youtu.be/Oj0nbY61qsY?t=221) **[[client-server-and-remotes]]** Rebirth via RemoteEvent: client only fires the event; server checks the cost, zeroes coins, increments rebirths.
- [5:07](https://youtu.be/Oj0nbY61qsY?t=307) **[[core-loops-and-game-design]]** Use a separate pet multiplier value stacked on the rebirth multiplier: coins += base * rebirthMult * petMult.
- [6:03](https://youtu.be/Oj0nbY61qsY?t=363) **[[data-persistence]]** Save coins, rebirths and pets to a DataStore keyed by UserId on PlayerRemoving, wrapped in pcall, and load on join.

## Numbers
- [0:00](https://youtu.be/Oj0nbY61qsY?t=0) core code size: **~40 lines of Luau for the simulator loop** (Speaker's estimate for the full core loop)
- [4:24](https://youtu.be/Oj0nbY61qsY?t=264) rebirth cost example: **1000 coins** (Example cost check in the rebirth handler)
- [3:25](https://youtu.be/Oj0nbY61qsY?t=205) rebirth multiplier example: **5 rebirths = 6x per click** (Multiplier is 1 + rebirths)
- [0:24](https://youtu.be/Oj0nbY61qsY?t=24) kit price: **$24** (Speaker's own Roblox Pro Simulator kit, promotional)

## Tools
Roblox Studio, Luau, RemoteEvent, DataStore, leaderstats

## He points to
- Speaker's full written guide (linked in description)
- Speaker's data store guide (linked in description)
- Roblox Pro Simulator kit (promotional, $24)

## Quotes
- [1:32](https://youtu.be/Oj0nbY61qsY?t=92) "Every coin change runs on the server in a script, never in a local script. If the client controls the coins, players will simply give themselves a billion."
- [3:41](https://youtu.be/Oj0nbY61qsY?t=221) "You must never let the client reset its own coins or hand itself a rebirth. If you do, a cheater just fires it a thousand times and skips the game."

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[core-loops-and-game-design]] [[data-persistence]] [[scripting-and-performance]]

Back to [[generalistprogrammer3233 - How to make successful Roblox games]]
