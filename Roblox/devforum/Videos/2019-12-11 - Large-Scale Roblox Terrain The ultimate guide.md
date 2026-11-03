---
title: "Large-Scale Roblox Terrain: The ultimate guide"
url: https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-12-11
views: 774
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Large-Scale Roblox Terrain: The ultimate guide

[Open](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) | Roblox DevForum | 774 views | 2019-12-11

## Summary
Vexture's guide to making large-scale Roblox terrain: generate landscape in Quadspinner Gaea, export as .obj, convert mesh to parts with NexusAvenger's OBJ Importer, then script parts into voxel terrain with FillWedge and auto-paint materials by slope/altitude. Notes the heightmap route is faster now.

## Tips
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[building-art-and-assets]]** Use Gaea's free version for terrain generation; its 1k resolution export is enough for Roblox terrain without a watermark.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[building-art-and-assets]]** Import OBJ meshes as Part triangle type, not Terrain; Terrain import produces an awful result.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[building-art-and-assets]]** Use FillWedge in the conversion script for better results than the older method, and back up the Studio file first since crashing is possible.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[building-art-and-assets]]** Heightmap import into Roblox is faster and supports higher resolution than mesh conversion; use it unless you need overhangs or caves.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[building-art-and-assets]]** Keep Blender decimation optional: reducing to about 200,000 faces can create holes after conversion, so skip it if your PC can handle the full mesh.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[scripting-and-performance]]** Run the terrain conversion script in the Studio command bar, not in Test Mode, or the terrain may not save.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[optimization-and-streaming]]** Expect heavy RAM use: 16 GB recommended, 8 GB minimum; Gaea uses under 10% of a GTX 1080 Ti for slower tasks.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[building-and-level-design]]** Use Gaea's Scale slider on the primitive to add more features for large maps or fewer for enclosed areas.
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) **[[building-and-level-design]]** Set sea_level in the conversion script (0 to 1 normalized) and fill water with Roblox's sea level method rather than the script's unfinished water fill.

## Numbers
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) Gaea free-version resolution: **1k without watermark** (Quadspinner Gaea free tier export resolution)
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) Recommended RAM: **16 GB (8 GB minimum)** (Studio and Gaea import process memory use)
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) Blender decimate target face count: **~200,000 (min ratio 0.1 / ~50,000 faces)** (Poly reduction before OBJ import, if PC struggles)
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) Example scale used: **4,000 studs** (Map scale set in OBJ importer)
- [page](https://devforum.roblox.com/t/large-scale-roblox-terrain-the-ultimate-guide/405672) Gaea GPU load: **<10% of GTX 1080 Ti** (Load on slower tasks, per author)

## Tools
Quadspinner Gaea, Blender, NexusAvenger .OBJ Importer plugin, Roblox Studio command bar, Terrain:FillWedge()

## He points to
- Quadspinner Gaea
- NexusAvenger .OBJ Importer

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
