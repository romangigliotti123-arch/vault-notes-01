---
title: "Docs: resources / battle-royale / installation-and-setup"
url: https://create.roblox.com/docs/resources/battle-royale/installation-and-setup.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / battle-royale / installation-and-setup

[Open](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Setup guide for the Roblox Battle Royale reference project: download Studio and reference .rbxl files, create a six-place experience (Lobby, Gameplay, four Queue places), copy place IDs into the MainConfiguration _places table, set Server Fill to Maximum, and publish each place.

## Tips
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) **[[development-process-and-speed]]** Structure a battle royale as one experience with six places: Lobby, Gameplay, and four Queue places (Default, Deathmatch, Team Deathmatch, Free Play).
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) **[[matchmaking-and-teleport]]** Cross-associate all places by copying each place ID via Asset Manager into the MainConfiguration _places table so players can teleport between lobby, queues and match.
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) **[[matchmaking-and-teleport]]** Keep the _places table identical in every place; paste the same table into Gameplay and Queue files before publishing so teleports resolve correctly.
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) **[[optimization-and-streaming]]** Set Server Fill to Maximum in Experience Settings for all six places so battle royale servers fill fully instead of Roblox's default social balancing.
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) **[[development-process-and-speed]]** Publish with File → Publish As… for the first place, then File → Publish (or Overwrite) for others; re-publish after every place ID change.

## Numbers
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) places per experience: **6** (Lobby, Gameplay, and four Queue places required)
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) Queue places: **4** (Default, Deathmatch, Team Deathmatch, Free Play)
- [page](https://create.roblox.com/docs/resources/battle-royale/installation-and-setup) Server Fill setting: **Maximum** (Set per place in Experience Settings > Places)

## Tools
Roblox Studio, Asset Manager, Explorer, Experience Settings

## He points to
- RobloxBattleRoyale.zip reference project

## Topics
[[development-process-and-speed]] [[matchmaking-and-teleport]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
