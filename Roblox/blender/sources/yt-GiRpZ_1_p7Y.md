---
type: research-source
id: yt-GiRpZ_1_p7Y
title: "How to Make a UGC Headband Hat for Roblox - Beginners"
source_type: "youtube"
creator: "Bluesteel"
url: "https://www.youtube.com/watch?v=GiRpZ_1_p7Y"
published: "2024-03-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 2
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# yt-GiRpZ_1_p7Y

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner manual tutorial (no Claude, MCP or bpy scripting) for a Roblox UGC headband. Exports the Block Avatar rig from Studio as OBJ, imports it into Blender, models the headband with solidify, bevel, mirror and loop cuts, UV-projects from view, applies a colour palette, and re-imports the OBJ via Import 3D, fixing the pivot with Edit Pivot.

## Claims
- c1: [0:17] Studio route: Avatar > Rig Builder > Block Avatar, select rig in Explorer, right-click Export Selection, save as OBJ for Blender reference. *(demo, medium; roblox-export-settings)*
- c2: [1:40] Blender import of the Studio rig: File > Import > Wavefront OBJ; object may not spawn at origin, so set origin to 3D cursor then origin to geometry. *(demo, medium; roblox-import-pipeline)*
- c3: [2:27] Headband built from a circle mesh (about 24 vertices), moved on Z, then Solidify for thickness and Bevel for edge rounding. *(demo, medium; avatar-ugc-accessories)*
- c4: [5:12] Bevel on a non-uniformly scaled object looks wrong; apply scale (Ctrl+A) first, otherwise bevel is computed as if the object were a square. *(experience, high; common-mistakes-fixes)*
- c5: [5:53] Bevel amounts used: 0.1 for the buckle block and 0.15 for the strap; Ctrl+R loop cuts (about 3 then 2 more) add edge loops before solidify. *(demo, medium; common-mistakes-fixes)*
- c6: [7:56] Mirror modifier with mirror object set to the other half; apply modifiers before joining (Ctrl+J) so the mirror is not duplicated. *(demo, medium; avatar-ugc-accessories)*
- c7: [8:24] UVs done by selecting all parts, Front view, U > Project From View, then scaling UV island; base colour set via image texture from a colour palette image, not a painted texture. *(demo, medium; texturing-baking-uv)*
- c8: [9:47] Export as Wavefront OBJ with 'Limit to Selection Only' enabled so only the headband exports, not the rig. *(demo, high; roblox-export-settings)*
- c9: [10:02] In Studio, Model/Home > Import 3D to load the OBJ; if pivot is wrong, Model tab > Edit Pivot and move it to geometry centre. *(demo, high; roblox-import-pipeline)*
- c10: [3:08] Auto smooth shading is applied to the model in Blender before UV work (Shade Auto Smooth); no normals fix beyond that is shown. *(demo, low; common-mistakes-fixes)*

## Numbers
- n1: **video length**: 10:40 
- n2: **circle vertex count**: about 24 
- n3: **bevel amount (strap)**: 0.15 (buckle block used 0.1) 
- n4: **loop cuts added on strap**: 3 initially, then 2 more 
- n5: **rotation for strap piece**: 90 degrees 

## Techniques
- t1: **Solidify + bevel headband**: Add circle, move on Z, add Solidify for thickness, extrude, then Bevel modifier. Use proportional editing (O) to shape the band.
- t2: **Apply scale before bevel**: Scale the buckle cube non-uniformly, press Ctrl+A to apply scale, then add Bevel so it is computed on the real geometry.
- t3: **Mirror modifier then apply**: Add Mirror with a mirror object, apply modifiers, then Ctrl+J join all parts before UV work.
- t4: **Project from view UV + palette**: Front view, select all, U > Project From View; scale UV island with A and S; new material with image texture pointing at a colour palette image.
- t5: **Edit Pivot in Studio**: Import OBJ via Model > Import 3D; if pivot is off, Model > Edit Pivot, move to geometry centre.

## Quotes (brief, for attribution)
> we need to apply that we've scaled it in different ways or else the bevel will be applied as if it was a square  (at 5:12, Bluesteel)
> make sure to hit limit to selection only because we have our headband selected  (at 9:47, Bluesteel)

## Points to
- Roblox Studio
- Blender
- colour palette link in video description
