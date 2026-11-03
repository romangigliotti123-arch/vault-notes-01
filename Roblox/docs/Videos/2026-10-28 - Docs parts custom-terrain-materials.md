---
title: "Docs: parts / custom-terrain-materials"
url: https://create.roblox.com/docs/parts/custom-terrain-materials.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / custom-terrain-materials

[Open](https://create.roblox.com/docs/parts/custom-terrain-materials.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Custom terrain materials: up to 62 paintable terrain materials per place, enabling Expanded Terrain (per-place, requires reopen), creating materials via Terrain Editor material picker, managing them in Terrain Materials Manager, and known limitations.

## Tips
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[building-art-and-assets]]** Enable Expanded Terrain on Workspace before using custom terrain materials; it is off by default and requires reopening the place to take effect.
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[building-art-and-assets]]** Early Access terrain users must re-set Expanded Terrain to Enabled, or custom materials may appear as grass.
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[building-art-and-assets]]** Create several shades of a material (e.g., grass variants) as separate custom terrain materials instead of globally overriding one base material.
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[building-art-and-assets]]** Before deleting a terrain material, replace it; terrain still using a deleted material turns bright purple.
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[optimization-and-streaming]]** With streaming enabled and a small radius, terrain thinner than 16 voxels may vanish on clients; add thickness rather than thinning, since thinning saves little memory with Expanded Terrain.
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[version-control-and-tooling]]** In Team Create, editing terrain may cause meshing or visual bugs; after toggling Expanded Terrain, exit and wait about 15 seconds before reopening.
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[building-art-and-assets]]** Custom physical properties on MaterialVariant are not yet respected by custom terrain material slots; don't rely on them.
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) **[[building-art-and-assets]]** Heightmap/colormap imports may differ from before; colormap import is sensitive to material colors, so check results after importing.

## Numbers
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) Custom terrain materials per place: **up to 62**
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) Thin terrain disappearance threshold (streaming, small radius): **less than 16 voxels thick**
- [page](https://create.roblox.com/docs/parts/custom-terrain-materials) Team Create wait before reopening after Expanded Terrain change: **about 15 seconds**

## Tools
Terrain Editor, Terrain Materials Manager, Material Generator, MaterialVariant

## He points to
- Custom materials (Roblox docs)

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
