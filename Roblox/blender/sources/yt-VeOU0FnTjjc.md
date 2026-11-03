---
type: research-source
id: yt-VeOU0FnTjjc
title: "Creating 3D Character with AI in 1 Min vs 1 H vs 10 H"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=VeOU0FnTjjc"
published: "2026-09-19"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 1
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-VeOU0FnTjjc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Stylized character workflow video: generate in Tripo P2 (low-poly, quads), split into parts (~500-1000 polys each), assemble in Blender, UV unwrap, add PBR in Substance/Modi, auto-rig, then finish physics and materials in Unreal Engine. No Roblox, blender-mcp, or bpy content.

## Claims
- c1: [1:10] Tripo P2 one-minute generation took about 2-3 minutes; result had blurry spots (eyes); no time for rigging. *(demo, medium; other)*
- c2: [1:28] Generating the model in parts with separate settings per part works better; split parts to roughly 500-1000 polygons each. *(experience, medium; mesh-texture-limits)*
- c3: [2:09] Typically 1-2 retries with different polycount settings were enough to get the right wireframe in Tripo P2. *(experience, medium; mesh-texture-limits)*
- c4: [3:31] Assembly of parts in Blender took about 20 minutes using sculpt mode or proportional editing. *(experience, medium; avatar-ugc-accessories)*
- c5: [4:12] Rigid accessories are weighted 100% to one bone; deforming parts get a quick auto-rig; accessories can be rigged separately or excluded. *(experience, medium; rigging-animation)*
- c6: [4:53] Blender materials are not exported to Unreal; materials had to be re-set in the engine. *(experience, medium; rigging-animation)*
- c7: [5:43] Author argues Tripo P2 low-poly, especially quads, beats retopology from high poly, so he skips high-to-low baking for stylized characters (opinion). *(opinion, low; mesh-texture-limits)*
- c8: [7:45] P2 mesh is logical part-separated, so UV seams are easier to place; full unwrap took about 30 minutes. *(experience, medium; mesh-texture-limits)*
- c9: [8:11] Good UVs enable nicer baking, texture packing at lower resolution, and fewer artifacts than many small islands. *(opinion, medium; mesh-texture-limits)*
- c10: [9:32] Substance Painter is used for baking AO and normal maps and for applying material zones such as fur on top of color texture. *(experience, medium; mesh-texture-limits)*
- c11: [10:12] Eyes were rebuilt as spheres placed inside the eye socket, textured with a generated image, and connected in Blender. *(demo, medium; mesh-texture-limits)*
- c12: [11:34] Scarf and tail were left unrigged or given a few bones for physics applied in Unreal Engine. *(demo, medium; rigging-animation)*
- c13: [12:55] Setting physics colliders/bones in Unreal Engine is tedious; Unreal's newer clothing workflow allows reusing physics presets. *(opinion, low; rigging-animation)*
- c14: [13:27] Total time reported: about 5.5 hours of work before Unreal finishing, plus about 1 more hour in Unreal; the 10-hour plan was cut short. *(experience, medium; other)*

## Numbers
- n1: **1-minute version generation time**: 2-3 minutes 
- n2: **polygons per split part**: 500-1000 
- n3: **retries to get right polycount**: 1-2 
- n4: **time spent generating all parts**: 30+ minutes 
- n5: **Blender assembly time**: ~20 minutes 
- n6: **full UV unwrap time**: ~30 minutes 
- n7: **assembly and fixes time**: ~40 minutes 
- n8: **total time at rigging stage**: 5.5 hours 
- n9: **Tripo free credits for new users via link**: 500 credits 

## Techniques
- t1: **Part-by-part generation**: Split character into body, head, weapons, accessories. Generate each separately with its own polycount setting, aiming 500-1000 polys per part, then assemble in Blender.
- t2: **Rigid accessory weighting**: Rigid pieces such as waist accessories get 100% weight to a single bone. Deforming pieces get a quick auto-rig.
- t3: **Seam-based UV unwrap on part-split mesh**: Use part boundaries as seams to unwrap each separated part, then re-bake color into one larger texture atlas.
- t4: **Zone material assignment**: Select polygon groups per part and assign materials such as gold or fur, then connect them to textures in Blender.

## Quotes (brief, for attribution)
> Produces much better low poly especially with quads than any retopology.  (at 5:43, Stefan 3D AI)

## Points to
- Tripo (Tripo P2 generator, Tripo retopology)
- Hunyuan retopology
- Modi
- Substance Painter
- Unreal Engine
- Auto-Rig (Blender add-on)
