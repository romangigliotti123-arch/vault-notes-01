---
title: "Justice, the awesome NPC system"
url: https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-02-05
views: 508
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Justice, the awesome NPC system

[Open](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) | Roblox DevForum | 508 views | 2021-02-05

## Summary
Release page for Justice, a hackable open-source-style NPC script for Roblox that auto-generates NPCs and wanders them across tagged pathfindable areas. Tested to 1000 NPCs locally with a performance hit. Includes setup notes on discriminators and asset configuration.

## Tips
- [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) **[[ai-and-tools]]** Treat Justice as a starting point: it is pre-release and designed to be heavily modified before use in a full game.
- [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) **[[physics-pathfinding-and-npc-ai]]** Tag walkable areas with Justice:Pathfindable so NPCs wander there automatically; use Justice:Deadzone labels in a PathfindingModifier to exclude areas.
- [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) **[[physics-pathfinding-and-npc-ai]]** Limit NPC counts in live games; the author says running 500 NPCs causes visible issues, though 1000 ran locally with only a performance hit.
- [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) **[[building-art-and-assets]]** Use discriminators (e.g. gender) to restrict which assets apply to which NPCs, and the 'all' discriminator to share assets across every NPC type without duplication.
- [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) **[[building-art-and-assets]]** Set an accessory or hair slot to -1 to skip it, giving NPCs variety without forcing an item.

## Numbers
- [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) NPC capacity tested: **1000 NPCs locally with no issues beyond performance hit** (Author's local machine test in Studio)
- [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927) NPC count causing issues: **500 NPCs** (Author says this count causes issues in demo; not recommended)

## Tools
Justice.rbxm, Configuration instance, PathfindingModifier

## He points to
- Helltaker by vanripper (source of the Justice character and art)

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
