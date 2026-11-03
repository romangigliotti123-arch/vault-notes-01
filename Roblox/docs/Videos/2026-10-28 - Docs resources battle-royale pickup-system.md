---
title: "Docs: resources / battle-royale / pickup-system"
url: https://create.roblox.com/docs/resources/battle-royale/pickup-system.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / battle-royale / pickup-system

[Open](https://create.roblox.com/docs/resources/battle-royale/pickup-system.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Battle Royale docs page on the pickup system: how weapon pickups are structured (PickupSpawners, Assets/Weapons Tools, Assets/Pickups visual models), how to add new pickups via matching names and tags, and how rarity is configured in RarityConfiguration.

## Tips
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[building-and-level-design]]** Spawners are found by the PickupSpawner tag, not folder location, so tag parts wherever they sit in the map.
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[common-mistakes]]** Pickup models must be visual only; do not put functional weapon Tools in ReplicatedStorage/Assets/Pickups.
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[building-and-level-design]]** Give the pickup Model the exact same name as its Tool in Assets/Weapons, since the system matches them by name.
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[genre-mechanics]]** Tag pickup models with Action, Pickup, WeaponPickup, WeaponSystemIgnore and one rarity tag so the system recognises them.
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[core-loops-and-game-design]]** Rarity has no formula; define rarity tiers in RarityConfiguration to visually signal item value (Common to Special by default).
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[ui-ux-design]]** Pickup prompts show the weapon name and description on proximity; rarity name plus Item appears as the description, so set rarity names clearly.
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[combat-and-gameplay-systems]]** Weapons Kit is the base for Battle Royale weapons; consult its docs for customisation before writing custom pickup logic.
- [page](https://create.roblox.com/docs/resources/battle-royale/pickup-system) **[[combat-and-gameplay-systems]]** Pickup spawners pick weapons randomly from Assets/Weapons, so adding a Tool there adds it to the random loot pool.

## Tools
Roblox Battle Royale Weapons Kit, RarityConfiguration script

## He points to
- Roblox Battle Royale Weapons Kit documentation

## Topics
[[building-and-level-design]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[core-loops-and-game-design]] [[genre-mechanics]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
