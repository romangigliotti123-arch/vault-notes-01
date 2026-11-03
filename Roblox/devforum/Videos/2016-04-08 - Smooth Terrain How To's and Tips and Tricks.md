---
title: "Smooth Terrain: How To's and Tips and Tricks"
url: https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017
creator: Roblox DevForum
official: false
advice_density: medium
date: 2016-04-08
views: 124
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Smooth Terrain: How To's and Tips and Tricks

[Open](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) | Roblox DevForum | 124 views | 2016-04-08

## Summary
Official-style DevForum guide by EndorsedModel covering Roblox Studio smooth terrain tools (Generate, Add, Subtract, Paint, Grow, Erode, Smooth, Regions), plus tips for smoothing ridges, blending terrain materials, and scripting terrain with FillBlock, FillBall, and FillRegion via the command bar.

## Tips
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[building-art-and-assets]]** Fix ridges left by the Smooth tool by running Grow or Erode at minimum strength over the affected area; this adds or removes a thin layer and looks cleaner.
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[building-art-and-assets]]** Blend two terrain materials by growing the opposite material at low strength on each side of the boundary to create a gradual transition.
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[building-art-and-assets]]** Use the Paint tool's plane lock to paint only along one plane, useful for layered material bands such as canyon strata.
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[building-art-and-assets]]** Use the Add tool's Snap to Grid and Ignore Water options to align chunks to the voxel grid and avoid overwriting water.
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[scripting-and-performance]]** Use Terrain:FillBlock(part.CFrame, part.Size, material) in the command bar to fill a part's volume with smooth terrain.
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[scripting-and-performance]]** Use Terrain:FillBall(position, radius, material) to create spherical terrain; the docs example uses part.Size.Y/2 as radius.
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[scripting-and-performance]]** Use Terrain:FillRegion(region:ExpandToGrid(4), 4, material) to fill a Region3; ExpandToGrid aligns it to the 4-stud voxel grid.
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) **[[building-and-level-design]]** Set Generate tool Biome Size smaller for many biomes close together, larger for sprawling maps; the default seed is the place ID.

## Numbers
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) Terrain voxel size: **about 4x4x4 studs** (Smooth terrain voxel size, used for Generate map size and grid snapping)
- [page](https://devforum.roblox.com/t/smooth-terrain-how-tos-and-tips-and-tricks/24017) Generate biome types: **9 (Water, Marsh, Plains, Hills, Dunes, Canyons, Mountains, Lavascape, Arctic)** (Selectable biomes in the Generate tool)

## Tools
Roblox Studio Terrain tools (Generate, Add, Subtract, Paint, Grow, Erode, Smooth, Regions), Command Bar

## He points to
- http://wiki.roblox.com/index.php?title=API:Class/Terrain/FillBlock
- http://wiki.roblox.com/index.php?title=API:Class/Terrain/FillBall
- http://wiki.roblox.com/index.php?title=API:Class/Terrain/FillRegion

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
