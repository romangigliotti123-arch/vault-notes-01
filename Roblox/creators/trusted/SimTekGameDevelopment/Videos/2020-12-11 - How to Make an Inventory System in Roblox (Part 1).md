---
title: "How to Make an Inventory System in Roblox (Part 1)"
url: https://youtu.be/8QUJ_Qc6JTs
creator: SimTek Game Development
official: false
advice_density: medium
date: 2020-12-11
views: 3982
transcript: auto-captions
confidence: medium
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Make an Inventory System in Roblox (Part 1)

[Watch](https://youtu.be/8QUJ_Qc6JTs) | SimTekGameDevelopment | 3,982 views | 2020-12-11

## Summary
Part 1 of a Roblox inventory tutorial: builds a tab-toggled bag GUI with a UIGridLayout and numbered slots, then server-side pickup logic using a ModuleScript (PickupManager), two RemoteEvents, a per-player item table initialized on PlayerAdded, and Touched-based item pickup. Bag UI update and dropping are deferred to Part 2.

## Tips
- [1:08](https://youtu.be/8QUJ_Qc6JTs?t=68) **[[ui-ux-design]]** Use a UIGridLayout with relative CellSize (e.g. scale 0.4 X) and centered alignment so inventory slots distribute evenly.
- [2:30](https://youtu.be/8QUJ_Qc6JTs?t=150) **[[ui-ux-design]]** Number inventory slot buttons so you can find the lowest empty slot in code when filling the bag.
- [3:13](https://youtu.be/8QUJ_Qc6JTs?t=193) **[[ui-ux-design]]** Anchor quantity labels at (1,1) in the bottom-right of each slot; set size in scale so they fit any slot size.
- [4:26](https://youtu.be/8QUJ_Qc6JTs?t=266) **[[client-server-and-remotes]]** Create separate RemoteEvents for each action (pickup and drop) in ReplicatedStorage so client and server communicate clearly.
- [5:00](https://youtu.be/8QUJ_Qc6JTs?t=300) **[[code-architecture-and-frameworks]]** Put inventory logic in a ModuleScript on the server and require it from item scripts, keeping item scripts short.
- [5:42](https://youtu.be/8QUJ_Qc6JTs?t=342) **[[client-server-and-remotes]]** Use WaitForChild with exact name strings for RemoteEvents; a mismatched name causes an infinite yield.
- [6:26](https://youtu.be/8QUJ_Qc6JTs?t=386) **[[scripting-and-performance]]** Check for a Humanoid and then GetPlayerFromCharacter before handling a touch, so NPCs/zombies with humanoids are ignored.
- [7:48](https://youtu.be/8QUJ_Qc6JTs?t=468) **[[core-loops-and-game-design]]** Store per-player item counts in a table keyed by player and item name, incrementing the old value on pickup.
- [8:30](https://youtu.be/8QUJ_Qc6JTs?t=510) **[[client-server-and-remotes]]** Fire the pickup RemoteEvent to the specific player with the item name and new quantity so the client UI can update.
- [9:54](https://youtu.be/8QUJ_Qc6JTs?t=594) **[[data-persistence]]** Initialize each player's table on PlayerAdded; this is where a DataStore load would go if you want saved inventory.
- [12:42](https://youtu.be/8QUJ_Qc6JTs?t=762) **[[client-server-and-remotes]]** Keep item Touched handlers on the item and route all inventory changes through the server module, not the client.

## Numbers
- [1:08](https://youtu.be/8QUJ_Qc6JTs?t=68) Bag frame size: **220 px wide, roughly 110 px scaled down in the tutorial** (Initial bag frame sizing, tuned by eye)
- [2:30](https://youtu.be/8QUJ_Qc6JTs?t=150) UIGridLayout CellSize: **Scale X 0.4, offset Y 0.2 (set via relative sizing)** (Slot grid sizing relative to parent frame)

## Tools
Roblox Studio, UIGridLayout, RemoteEvent, ModuleScript, Output window

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[core-loops-and-game-design]] [[data-persistence]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
