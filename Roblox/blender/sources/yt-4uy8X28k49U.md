---
type: research-source
id: yt-4uy8X28k49U
title: "How to Make Realistic 3D Character in Less Than a Day with AI"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=4uy8X28k49U"
published: "2026-09-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: low
tags: ["research-source", "youtube", "avatar-ugc-accessories", "mesh-texture-limits", "other"]
---
# yt-4uy8X28k49U

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video on making a realistic custom 3D character with AI meshes, Blender, and MetaHuman in Unreal Engine 5.8. It does not cover Roblox, blender-mcp, Claude, or bpy scripting. Useful only for general Blender techniques: Data Transfer weight copying for garments, moving UVs into one 0-1 tile for baking, and cage-based color baking.

## Claims
- c1: For garments and accessories, Data Transfer from the exported body mesh gives better weights than Blender automatic weight transfer, since the body already has professional weight distribution. *(demo, medium; avatar-ugc-accessories)*
- c2: MetaHuman DNA export uses UDIM UVs with head and body merged into one space; the author separated head UVs and shifted body UVs by -1 in U to fit one tile before baking. *(demo, medium; mesh-texture-limits)*
- c3: Author bakes diffuse color in Cycles with direct and indirect light contributions unchecked and cage set to 0.1, then wires the baked textures into MetaHuman materials. *(demo, medium; mesh-texture-limits)*
- c4: Imported normal maps from Blender may need the flip normal map green channel option in Unreal Engine; the author describes this as a known issue. *(experience, low; avatar-ugc-accessories)*
- c5: Source gives no Roblox-specific steps, no Roblox import settings, and no Claude or blender-mcp workflow; the 3D AI generator is named only as 'High 3D' with no version or specs. *(doc, high; other)*

## Numbers
- n1: **Bake cage distance**: 0.1 Cage setting used for diffuse bake in Cycles
- n2: **Mesh resolution**: 2K Generator described as producing ultra-detailed meshes in 2K resolution

## Techniques
- t1: **Data Transfer weight copy from body**: Add Data Transfer modifier to garment, set source to exported body mesh (placed before armature), enable vertex data and vertex groups, then apply to copy body weights.
- t2: **UV tile separation before bake**: Separate head and body UV islands from the merged UDIM layout, shift body UVs by -1 in U so they fill the full 0-1 square, then bake color to a new image texture.

## Points to
- MetaHuman (Unreal Engine 5.8)
- Fab marketplace
- High 3D agent
