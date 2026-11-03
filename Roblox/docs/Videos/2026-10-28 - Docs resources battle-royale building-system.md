---
title: "Docs: resources / battle-royale / building-system"
url: https://create.roblox.com/docs/resources/battle-royale/building-system.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / battle-royale / building-system

[Open](https://create.roblox.com/docs/resources/battle-royale/building-system.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Battle Royale docs on its building system: tile assets in ReplicatedStorage with ObjectType and StartingRotation children, bitmask occupancy and connectivity per grid cell, and terrain heightmap alignment using 20x16x20 stud cells.

## Tips
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) **[[building-and-level-design]]** Make every building tile connect to an existing tile or the ground, and place tiles on a grid so they connect properly without overlapping.
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) **[[building-and-level-design]]** Define each new tile type's occupancy and connectivity bitmasks in ObjectTypeConfigurations so the system knows where tiles can go.
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) **[[building-and-level-design]]** Two building objects count as connected only if they share at least 2 connectivity points on a cell surface.
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) **[[building-and-level-design]]** Match terrain to the build grid: use heightmap import with one pixel per 4-stud voxel so a 5x5 pixel area equals one 20x20 stud cell.
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) **[[building-and-level-design]]** Make heightmap red/grey channel values divisible by the grid cell height so floor tiles sit flush on terrain.
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) **[[3d-modeling-rigging-and-animation]]** Structure tile assets as BaseParts in ReplicatedStorage/BuildingSystem/Assets, each with ObjectType StringValue and StartingRotation NumberValue children.
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) **[[building-and-level-design]]** Use a cell size of 20x16x20 studs with 20x16x1 walls and 20x1x20 floors so building tiles and terrain line up.

## Numbers
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) Grid cell size: **20x16x20 studs** (Roblox Battle Royale building grid cell dimensions)
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) Wall tile size: **20x16x1 studs** (Wall tile dimensions in Battle Royale building system)
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) Floor/ceiling tile size: **20x1x20 studs** (Floor tile dimensions in Battle Royale building system)
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) Terrain voxel size: **4x4x4 studs** (Each terrain voxel occupies a 4-stud cube)
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) Connection threshold: **2 shared connectivity points** (Minimum shared points for two tiles to count as connected)
- [page](https://create.roblox.com/docs/resources/battle-royale/building-system) Heightmap import size: **width x 4, 256, length x 4** (Terrain import Size X, Y, Z with position 0,0,0)

## Games
- **Roblox Battle Royale**: Building system lets players build tiles for higher ground or cover, using a grid-aligned tile system with bitmask occupancy and connectivity.

## Tools
Roblox Studio, Environmental Terrain heightmap import

## He points to
- Environmental Terrain (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-and-level-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
