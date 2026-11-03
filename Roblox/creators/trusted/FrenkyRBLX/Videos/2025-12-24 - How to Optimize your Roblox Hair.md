---
title: "How to Optimize your Roblox Hair"
url: https://youtu.be/rtF3uoHrqU4
creator: FrenkyRBLX
official: false
advice_density: high
date: 2025-12-24
views: 7586
transcript: auto-captions
confidence: high
tags: [roblox, frenkyrblx, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Optimize your Roblox Hair

[Watch](https://youtu.be/rtF3uoHrqU4) | FrenkyRBLX | 7,586 views | 2025-12-24

## Summary
Tutorial on reducing triangle count of Roblox UGC hair meshes to get under the 4,000-triangle limit. Covers lowering strand curve resolution, converting curves to mesh and merging vertices, dissolving unnecessary edges, deleting hidden back faces, and merge-by-distance cleanup.

## Tips
- [0:57](https://youtu.be/rtF3uoHrqU4?t=57) **[[building-art-and-assets]]** Lower curve resolution on hair strands (Curve Properties, resolution ~12 down to ~6) to cut triangles roughly from 10,000 to 5,000.
- [1:38](https://youtu.be/rtF3uoHrqU4?t=98) **[[building-art-and-assets]]** Convert hair curves to mesh, join strands, and merge vertices by center so no gaps remain in the hair mesh.
- [2:20](https://youtu.be/rtF3uoHrqU4?t=140) **[[building-art-and-assets]]** Dissolve edges that cannot be merged (Alt-select edge, Ctrl+X) to reduce triangle count.
- [4:09](https://youtu.be/rtF3uoHrqU4?t=249) **[[building-art-and-assets]]** Dissolve edges on flat, straight surfaces that add no topology value; repeat across the mesh to drop under 4,000 triangles.
- [4:49](https://youtu.be/rtF3uoHrqU4?t=289) **[[building-art-and-assets]]** Use G-G to slide edges so strands look smoother and more natural after dissolving edges.
- [5:51](https://youtu.be/rtF3uoHrqU4?t=351) **[[building-art-and-assets]]** Delete back faces of hair parts that are hidden under the head and never visible in game to save triangles.
- [6:47](https://youtu.be/rtF3uoHrqU4?t=407) **[[building-art-and-assets]]** Select all, press M, Merge by Distance to remove hidden overlapping geometry; this removed about 80 triangles in the example.
- [7:31](https://youtu.be/rtF3uoHrqU4?t=451) **[[building-art-and-assets]]** Keep the UGC accessory under 4,000 triangles, the limit to upload to the Roblox marketplace.

## Numbers
- [0:57](https://youtu.be/rtF3uoHrqU4?t=57) triangles after lowering strand resolution: **~10,000 to ~5,000** (Hair curve resolution lowered from 12 to 6)
- [5:51](https://youtu.be/rtF3uoHrqU4?t=351) UGC triangle limit: **4,000** (Maximum triangles to upload hair to Roblox marketplace)
- [5:51](https://youtu.be/rtF3uoHrqU4?t=351) triangles before back-face deletion: **4,500** (Needed to drop below 4K)
- [6:47](https://youtu.be/rtF3uoHrqU4?t=407) hidden geometry removed by merge by distance: **~80** (Triangles removed; about 90 left to reduce)

## Tools
Blender

## Topics
[[building-art-and-assets]]

Back to [[FrenkyRBLX - How to make successful Roblox games]]
