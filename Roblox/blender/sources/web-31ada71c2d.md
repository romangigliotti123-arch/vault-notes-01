---
type: research-source
id: web-31ada71c2d
title: "DevForum thread 2522587"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/2522587"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "roblox-mesh-limits", "texturing-baking-uv"]
---
# web-31ada71c2d

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
DevForum thread (Aug 2023) where a creator reduced a UGC crown mesh from 15,248 to about 5k triangles in Blender using Merge by Distance and manual cleanup. A helper estimates under 2,000 tris is enough. No Claude, MCP or bpy scripting content. The video link has no transcript here.

## Claims
- c1: Poster believed the UGC triangle max was 6k based on older forum posts, unverified for 2023. *(opinion, low; roblox-mesh-limits)*
- c2: Imported Roblox Parts in Blender keep hidden inside faces that add triangles; select and delete them. *(opinion, medium; common-mistakes-fixes)*
- c3: Merge by Distance (select all vertices, Mesh > Clean up) joins coincident vertices and cut a 15k mesh to about 8k. *(experience, medium; common-mistakes-fixes)*
- c4: Helper estimates a crown like this should need no more than about 2,000 triangles; opinion, not a documented limit. *(opinion, low; roblox-mesh-limits)*
- c5: Blender Merge by Distance default is about 0.0001; helper uses about 0.003 so close vertices join. *(opinion, medium; common-mistakes-fixes)*
- c6: Over-subdivided smooth areas (e.g. a cylinder) carry excess triangles; merge vertices at the selected last vertex (M, Merge at Last) to reduce them. *(opinion, medium; common-mistakes-fixes)*
- c7: After merging, Normals > Reset Vectors in Face mode fixed dark/light triangle shading artifacts on a brown band. *(experience, medium; common-mistakes-fixes)*
- c8: Helper asked whether the crown uses four separately coloured meshes or one mesh with texture paint, which affects how colour is stored. *(opinion, low; texturing-baking-uv)*

## Numbers
- n1: **Original crown triangle count**: 15,248 Poster's initial Blender mesh count before cleanup
- n2: **Triangle count after cleanup steps**: 15k -> 8k -> 5k Poster's counts after merge and clean steps
- n3: **Triangle max cited by poster**: 6k From older forum posts; unverified for current rules
- n4: **Helper's triangle estimate for crown**: under 2000 Helper opinion on what the crown should need
- n5: **Merge by Distance default**: about 0.0001 Blender default per helper, not verified
- n6: **Merge distance used by helper**: about 0.003 Helper's usual setting to join close vertices

## Techniques
- t1: **Merge by Distance cleanup**: Edit mode, A to select all, Mesh tab > Clean up > Merge by Distance; raise threshold from default to about 0.003 to join near vertices.
- t2: **Delete hidden inside faces**: Select inside faces that are never visible (imported Roblox Parts keep them) and delete to cut triangles.
- t3: **Merge at last selection**: Select vertices, choose the target vertex last, press M then L (Merge at Last) to collapse over-dense regions.
- t4: **Reset Vectors normals fix**: After merging, Face mode, A for all, Mesh > Normals > Reset Vectors to clear shading artifacts.

## Quotes (brief, for attribution)
> I don't see that entire crown needing more than 2000 tris.  (devforum.roblox.com)
> Went from 15k -> 8k -> 5k. Is this enough condensing for a UGC hat?  (devforum.roblox.com)

## Contradictions flagged
- Crown needs no more than about 2,000 triangles. (vs Poster's belief in a 6k max from older posts; helper's figure is opinion, not a documented limit.)

## Points to
- https://www.youtube.com/watch?v=4d4N8d4ki2Y&t=1s
