---
title: "Docs: tutorials / curriculums / environmental-art / optimize-your-experience"
url: https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / environmental-art / optimize-your-experience

[Open](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official curriculum page on optimizing environment art: review physics/render parameters (e.g., disable CastShadow on distant foliage), remove duplicate textures/asset IDs, combine meshes to cut draw calls, simplify geometry, and limit layered transparency overdraw. Uses Microprofiler and Scene Analysis to find costs.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) **[[scripting-and-performance]]** Near the end of development, review all physics and rendering parameters and disable CastShadow on foliage away from gameplay areas to save performance.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) **[[building-art-and-assets]]** Reuse assets via packages so every instance shares one asset ID; separate imports of identical meshes count as unique assets and cost memory and performance.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) **[[optimization-and-streaming]]** Combine groups of meshes into a single asset to reduce GPU draw calls (example: 8 draw calls reduced to 1), but only late in development since it locks per-part editing.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) **[[building-art-and-assets]]** After simplifying geometry in third-party tools, update the existing package with the new import rather than creating a new asset ID, to avoid extra asset calls.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) **[[optimization-and-streaming]]** Avoid stacking many semi-transparent objects (foliage, glass) in layers across large screen areas; overlapping transparency causes costly overdraw.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) **[[optimization-and-streaming]]** Use the Microprofiler to find which frames and assets take the most render time, and Scene Analysis to check resource usage, before deciding what to cut.
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) **[[optimization-and-streaming]]** Cull nonessential content that doesn't affect gameplay: duplicate textures, high-vertex geometry, and redundant transparent layers.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) Draw calls in example: **8 draw calls reduced to 1 by combining tower parts into a single asset** (Laser tag sample environment tower outside the building)
- [page](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) Overdrawn pixels in planter example: **hundreds of thousands** (Layered transparent leaves in sample environment planter view)

## Tools
Microprofiler, Scene Analysis, Roblox Studio

## He points to
- Environmental Art Curriculum Q&A (Roblox DevForum)
- Environment Art - Optimizing .rbxl file

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
