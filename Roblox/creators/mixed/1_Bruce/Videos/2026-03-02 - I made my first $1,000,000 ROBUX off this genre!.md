---
title: "I made my first $1,000,000 ROBUX off this genre!"
url: https://youtu.be/9ZoyhYqBkcI
creator: 1_Bruce
official: false
advice_density: medium
date: 2026-03-02
views: 10064
transcript: auto-captions
confidence: medium
tags: [roblox, 1_bruce, youtube-learn]
creator_trust: MIXED
creator_score: 7.2
---

> [!note] Trust: MIXED (credibility audit score 7.2): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# I made my first $1,000,000 ROBUX off this genre!

[Watch](https://youtu.be/9ZoyhYqBkcI) | 1_Bruce | 10,064 views | 2026-03-02

## Summary
Promo-style walkthrough of a paid "button simulator" starter kit (~$5). Shows setup, adding stats via data template/formulas/stats module, buttons tagged 'button', runes with rarity chances, tokens, Big Num for large numbers, DataService and signal helpers, and component-based OOP. Mostly a product showcase, with a few reusable design notes.

## Tips
- [2:37](https://youtu.be/9ZoyhYqBkcI?t=157) **[[game-ideas-and-genres]]** Button/incremental simulators are easy to make, update and get popular; the speaker says they were the games that first got him big.
- [2:37](https://youtu.be/9ZoyhYqBkcI?t=157) **[[core-loops-and-game-design]]** Play several games in the genre before building one; you need to understand how incremental/stat-multiplier loops work first.
- [3:17](https://youtu.be/9ZoyhYqBkcI?t=197) **[[scripting-and-performance]]** Store large incremental values as strings and use a Big Num library to bypass Lua's number limit.
- [8:55](https://youtu.be/9ZoyhYqBkcI?t=535) **[[scripting-and-performance]]** Use math instead of for loops when opening many items at once so bulk opens don't crash or lag the server.
- [5:20](https://youtu.be/9ZoyhYqBkcI?t=320) **[[core-loops-and-game-design]]** Make each stat multiply the previous one (e.g. rebirth doubles multiplier), so upgrades compound visibly.
- [11:49](https://youtu.be/9ZoyhYqBkcI?t=709) **[[scripting-and-performance]]** Use a data service update helper that passes the current value into a function, simplifying stat increments.
- [12:33](https://youtu.be/9ZoyhYqBkcI?t=753) **[[scripting-and-performance]]** Tag objects (e.g. button, rune) and use a component system so game logic is modular and object-oriented.
- [7:39](https://youtu.be/9ZoyhYqBkcI?t=459) **[[core-loops-and-game-design]]** Use weighted rarity tables for random rewards (common to mythical) with configurable chances and luck modifiers.
- [10:26](https://youtu.be/9ZoyhYqBkcI?t=626) **[[core-loops-and-game-design]]** Add a secondary currency (tokens, 1-in-50 per button press) to gate purchases of higher-tier rooms.
- [6:18](https://youtu.be/9ZoyhYqBkcI?t=378) **[[core-loops-and-game-design]]** Consider tiered multipliers with stacking formulas, e.g. 2x per extra stat level, to keep scaling predictable.
- [8:15](https://youtu.be/9ZoyhYqBkcI?t=495) **[[monetisation-gamepasses]]** Place game-pass multipliers in the central formula script so they can be applied to any stat with one line.

## Numbers
- [0:41](https://youtu.be/9ZoyhYqBkcI?t=41) Kit price: **about $5** (Paid starter kit sold by the speaker)
- [7:39](https://youtu.be/9ZoyhYqBkcI?t=459) Rune boost example: **5 mythical rooms = money 5x, multiplier 2.5x, rebirth 0.5x** (Rarity-based room rewards example)
- [6:18](https://youtu.be/9ZoyhYqBkcI?t=378) Stat boost scaling example: **1 extreme = x2 ultra, 2 = x4, 3 = x6; money x5/x10/x15** (Stat multiplier scaling per level)
- [10:26](https://youtu.be/9ZoyhYqBkcI?t=626) Token drop chance: **1 in 50 per button press** (Secondary token currency rate)
- [9:38](https://youtu.be/9ZoyhYqBkcI?t=578) Bulk open demo: **~1000 rooms per second, 10 room clones, 1000 runes per open** (Rune luck 10x, room speed 0.01 in demo)

## Games
- **Button simulator (unnamed)** [0:00](https://youtu.be/9ZoyhYqBkcI?t=0): Speaker's own early hits; button/incremental sims are easy to build and update and got him big.

## Tools
Roblox Studio, Big Num library, Data Service (by Leaf)

## He points to
- Big Num library (packages folder in kit)
- Data Service by Leaf

## Quotes
- [12:08](https://youtu.be/9ZoyhYqBkcI?t=728) "these types of games were the games I started on and this is where this is the genre where I made my first million Robux from."
- [6:58](https://youtu.be/9ZoyhYqBkcI?t=418) "play literally any incremental game ever and you'll understand how these work"

## On screen
Contact sheet shows Roblox Studio with a grid of colored button tiles, a STATS board, and a large cube-like gift/rune object in the workspace. Code panels show the stat data template and formula scripts. No analytics or thumbnails are shown.

## Topics
[[core-loops-and-game-design]] [[game-ideas-and-genres]] [[monetisation-gamepasses]] [[scripting-and-performance]]

Back to [[1_Bruce - How to make successful Roblox games]]
