---
title: "You NEED This Roblox Summoning System (Full Setup Guide)"
url: https://youtu.be/Iy9xuT1bpY4
creator: ArTheDev
official: false
advice_density: medium
date: 2026-04-18
views: 2958
transcript: auto-captions
confidence: high
tags: [roblox, arthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.5
---

> [!note] Trust: TRUSTED (credibility audit score 8.5): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# You NEED This Roblox Summoning System (Full Setup Guide)

[Watch](https://youtu.be/Iy9xuT1bpY4) | ArTheDev | 2,958 views | 2026-04-18

## Summary
Walkthrough of a modular Roblox summoning system: weighted rarity rolls driven by a rates config module, server-validated summon requests, DataStore-saved unit IDs, and a client GUI with viewport preview, blur tween, and click-to-advance reveal. Aimed at tower defense and simulator games.

## Tips
- [8:05](https://youtu.be/Iy9xuT1bpY4?t=485) **[[core-loops-and-game-design]]** Keep drop rates, pools and rarity weights in one config ModuleScript so tuning rarities means editing numbers, not rewriting logic.
- [8:46](https://youtu.be/Iy9xuT1bpY4?t=526) **[[scripting-and-performance]]** Validate summon amount on the server (reject values above 10 or below 1) and never trust client-sent prices; set the price server-side.
- [14:14](https://youtu.be/Iy9xuT1bpY4?t=854) **[[scripting-and-performance]]** Compute max affordable summons from the currency balance and cap the loop to it, so partial multis still work without errors.
- [14:56](https://youtu.be/Iy9xuT1bpY4?t=896) **[[scripting-and-performance]]** Set a summoning-in-progress flag on the server before rolling to block duplicate summon requests and double-spending.
- [12:11](https://youtu.be/Iy9xuT1bpY4?t=731) **[[core-loops-and-game-design]]** Use weighted random selection: sum all weights, roll math.random up to the total, and return the item where the running sum passes the roll.
- [18:21](https://youtu.be/Iy9xuT1bpY4?t=1101) **[[data-persistence]]** Give each summoned unit a unique generated ID and store units as a keyed table in player data so individual units can be found, equipped and removed later.
- [20:27](https://youtu.be/Iy9xuT1bpY4?t=1227) **[[data-persistence]]** Mirror summoned inventory to the client via a remote on join and on each new unit so the UI rebuilds from saved data after rejoin.
- [4:24](https://youtu.be/Iy9xuT1bpY4?t=264) **[[building-art-and-assets]]** Put unit models in a WorldModel inside the viewport template so idle animations play in the inventory preview.
- [23:45](https://youtu.be/Iy9xuT1bpY4?t=1425) **[[ui-ux-design]]** Debounce click-to-advance reveals (about 0.5s) so players cannot spam through the summon animation.
- [27:11](https://youtu.be/Iy9xuT1bpY4?t=1631) **[[ui-ux-design]]** Tween a background blur on summon start and reset it on finish to focus attention on the reveal.
- [16:57](https://youtu.be/Iy9xuT1bpY4?t=1017) **[[vfx-and-particles]]** Pace the reveal with short waits (about 2s for a single pull, 0.5s for multis) so the summon feels like an event; make these values adjustable.

## Numbers
- [0:52](https://youtu.be/Iy9xuT1bpY4?t=52) summon price: **50 gems per summon at price tier 1 (example from video)** (Demo player started with 600 gems; single summon costs 200 at default setting)
- [9:26](https://youtu.be/Iy9xuT1bpY4?t=566) multi-summon size: **10 max per request** (Server rejects amounts above 10 or below 1)
- [24:25](https://youtu.be/Iy9xuT1bpY4?t=1465) click debounce: **0.5 seconds** (Delay between reveal clicks, adjustable)
- [16:57](https://youtu.be/Iy9xuT1bpY4?t=1017) reveal wait: **2s single summon, 0.5s per multi summon** (Wait time between reveals, adjustable)
- [27:11](https://youtu.be/Iy9xuT1bpY4?t=1631) blur size: **24 during summon, 0 when finished** (Lighting blur tween on summon start and end)
- [12:11](https://youtu.be/Iy9xuT1bpY4?t=731) example rarity weight: **common = 100 in weight table** (Weights summed to total; higher weight means higher chance)

## Tools
Roblox Studio, Luau, DataStore, HttpService (GenerateGUID), TweenService, ReplicatedStorage remotes

## He points to
- Creator's previous inventory and DataStore tutorial (referenced, not named)

## Topics
[[building-art-and-assets]] [[core-loops-and-game-design]] [[data-persistence]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[ArTheDev - How to make successful Roblox games]]
