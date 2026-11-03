---
title: "How to LOWER TRIS COUNT in Your Roblox UGC"
url: https://youtu.be/7__AKBlwYkk
creator: FrenkyRBLX
official: false
advice_density: medium
date: 2025-05-05
views: 8841
transcript: auto-captions
confidence: high
tags: [roblox, frenkyrblx, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to LOWER TRIS COUNT in Your Roblox UGC

[Watch](https://youtu.be/7__AKBlwYkk) | FrenkyRBLX | 8,841 views | 2025-05-05

## Summary
Shows four techniques to reduce triangle (tris) count of a Roblox UGC accessory model to get under the 4,000 limit: dissolving unnecessary edges, deleting hidden faces, using the Decimate modifier (not recommended), and merge by distance. Model went from 19k tris in the demo.

## Tips
- [0:00](https://youtu.be/7__AKBlwYkk?t=0) **[[building-art-and-assets]]** UGC items must stay under 4,000 tris; check the Statistics overlay in Studio/Blender to see the count.
- [1:33](https://youtu.be/7__AKBlwYkk?t=93) **[[building-art-and-assets]]** Dissolve edges lying on flat surfaces (Alt-click edge, X, Dissolve Edges) to reduce polycount without changing shape.
- [4:45](https://youtu.be/7__AKBlwYkk?t=285) **[[building-art-and-assets]]** Delete hidden faces that players never see, such as parts poking inside other geometry, using X-ray and face select.
- [7:17](https://youtu.be/7__AKBlwYkk?t=437) **[[building-art-and-assets]]** Avoid the Decimate modifier; it badly damages topology. Use only as last resort when tris must drop fast.
- [8:37](https://youtu.be/7__AKBlwYkk?t=517) **[[building-art-and-assets]]** Use Merge by Distance (vertex select, A, M) to clean up very close vertices; often removes many vertices unnoticed.

## Numbers
- [0:00](https://youtu.be/7__AKBlwYkk?t=0) UGC tris limit: **4,000** (Maximum triangle count for uploading UGC to marketplace)
- [0:25](https://youtu.be/7__AKBlwYkk?t=25) Demo model tris before optimisation: **19k** (Example model shown in statistics overlay)
- [8:37](https://youtu.be/7__AKBlwYkk?t=517) Vertices removed by merge by distance: **66** (Single merge-by-distance pass on demo mesh)

## Tools
Blender, Statistics overlay, Decimate modifier, Merge by Distance

## Topics
[[building-art-and-assets]]

Back to [[FrenkyRBLX - How to make successful Roblox games]]
