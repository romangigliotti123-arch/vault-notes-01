---
title: "Docs: parts / terrain"
url: https://create.roblox.com/docs/parts/terrain.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / terrain

[Open](https://create.roblox.com/docs/parts/terrain.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on the Terrain Editor: voxels (4x4x4 studs), default terrain materials, water and grass appearance properties, custom material colors, procedural Generate tool, heightmap/colormap import, scripting terrain via Terrain fill methods, and large-scale and brush-based editing tools.

## Tips
- [page](https://create.roblox.com/docs/parts/terrain) **[[building-art-and-assets]]** Use the Generate tool with biome selection to rapidly create large base terrain, then fine-tune details with brush tools.
- [page](https://create.roblox.com/docs/parts/terrain) **[[building-and-level-design]]** Heightmaps can be at most 4096x4096 px (.jpg or .png); 1 pixel maps to 4 studs, so plan map size accordingly.
- [page](https://create.roblox.com/docs/parts/terrain) **[[building-art-and-assets]]** For colormaps, use hard-edged colors matching the RobloxColorMapIndex values exactly, since anti-aliasing can produce colors that map to the wrong material.
- [page](https://create.roblox.com/docs/parts/terrain) **[[building-art-and-assets]]** Enable Expanded Terrain to paint custom terrain materials, or apply custom materials as overrides.
- [page](https://create.roblox.com/docs/parts/terrain) **[[ui-ux-design]]** Set Editor Quality Level to the highest in Studio Settings to preview all water properties while editing; some are only visible in playtest.
- [page](https://create.roblox.com/docs/parts/terrain) **[[vfx-and-particles]]** Enable Terrain.Decoration and set GrassLength between 0.1 and 1 to animate grass; animated grass only renders on the Grass material.
- [page](https://create.roblox.com/docs/parts/terrain) **[[cross-platform-and-console]]** Animated grass speed is reduced when players enable Reduce Motion, so don't rely on grass motion alone for gameplay-critical cues.

## Numbers
- [page](https://create.roblox.com/docs/parts/terrain) Voxel size: **4x4x4 studs** (Terrain grid unit in Studio)
- [page](https://create.roblox.com/docs/parts/terrain) Heightmap pixel scale: **1 px = 4 studs** (Heightmap import conversion)
- [page](https://create.roblox.com/docs/parts/terrain) Max heightmap size: **4096x4096 px** (Supported .jpg or .png heightmap/colormap)
- [page](https://create.roblox.com/docs/parts/terrain) Brush base size: **1-64 studs** (Range for terrain brush tools)
- [page](https://create.roblox.com/docs/parts/terrain) Grass length range: **0.1 to 1** (GrassLength property value)
- [page](https://create.roblox.com/docs/parts/terrain) Heightmap height example: **height 128 gives +/-64 studs** (Pure white/black relative to Y size)

## Tools
Terrain Editor, Generate tool, Import tool, Select and Transform tools, Fill and Sea Level tools, Brush tools (Draw, Sculpt, Smooth, Flatten, Paint), Terrain class scripting (FillBlock etc.), RobloxColorMapIndex file

## He points to
- RobloxColorMapIndex file

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[cross-platform-and-console]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
