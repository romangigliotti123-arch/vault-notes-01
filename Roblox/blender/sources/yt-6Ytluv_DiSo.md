---
type: research-source
id: yt-6Ytluv_DiSo
title: "I Built a Whole Game Level Using Only FREE AI - My Full Workflow"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=6Ytluv_DiSo"
published: "2026-08-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0034
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# yt-6Ytluv_DiSo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Stefan 3D AI video on building a pirate cave level with free AI tools (Gemini/Nano Banana concepts, Hunyuan 3D, Blender texturing and assembly, Unreal Engine setup). Not about Roblox, blender-mcp, bpy, or the Roblox export pipeline. Only generic Blender steps (bake, decimate, UV pack, clone brush) are reusable, and no Roblox-specific limits, settings, or code are given.

## Claims
- c1: [27:41] Speaker mentions a Claude Code with Blender setup but gives no details; advises asking the assistant for the easiest or fastest method rather than only asking it to execute tasks. *(opinion, low; claude-blender-ai)*
- c2: [16:01] Decimate modifier reduced rock meshes from about 1 million polygons to roughly 1000 polygons for a low-poly proxy before normal-map baking. *(demo, medium; mesh-texture-limits)*
- c3: [18:01] Normal map baked at 4K resolution from high-poly rock to low-poly proxy using Cycles, cage extrusion lowered. *(demo, medium; mesh-texture-limits)*
- c4: [12:00] Multiple similar objects were joined, duplicated as high/low, unwrapped/packed with the UV Packer add-on with margin, and diffuse-baked into one shared atlas texture with direct/indirect lighting unchecked. *(demo, medium; mesh-texture-limits)*
- c5: [9:36] Blender Clone brush (Ctrl+click to source) in texture paint mode fixes small texture artifacts faster than an AI round trip. *(demo, medium; mesh-texture-limits)*
- c6: [10:38] AI-generated textures inconsistent in color were matched with color nodes (gamma, contrast, RGB curves) and then baked into a new texture, since node tweaks don't export. *(demo, medium; mesh-texture-limits)*
- c7: [18:42] Node Wrangler add-on is needed for Ctrl+T mapping node; scale set to 4 for the rock tile texture after trying 4 to 6. *(demo, low; mesh-texture-limits)*
- c8: [14:18] Roughness and metallic maps created by filling a texture-paint canvas with values, then painting variations; maps set to Non-Color. *(demo, medium; mesh-texture-limits)*
- c9: [3:24] Hunyuan 3D site cited as giving 23 free daily generations; high-poly output recommended for big details, with Smart Topology as low-poly option. *(opinion, low; other)*
- c10: [24:18] Cave built from big pre-placed chunks took about 25 minutes; the full level assembly took about one hour in Blender before Unreal setup taking about two hours. *(experience, low; other)*
- c11: [22:17] Hidden bottom faces of large rocks were removed with the knife tool to save polygons. *(demo, low; mesh-texture-limits)*
- c12: [27:01] Rope made from Bezier curve with depth, then converted to mesh; described as about five times faster than generating a rope with AI. *(experience, low; other)*

## Numbers
- n1: **polygon reduction**: about 1M to about 1000 polys per rock (Decimate) low-poly proxy for normal-map baking
- n2: **normal map resolution**: 4K chosen because the rock object is instanced many times
- n3: **texture scale**: 4 (chosen from 4 to 6 tested) seamless rock texture mapping scale
- n4: **free generations**: 23 daily Hunyuan 3D free tier per video
- n5: **cave build time**: about 25 minutes real time, time-lapse compressed

## Techniques
- t1: **Atlas merge via bake**: Join objects, duplicate to high/low, remove materials, unwrap/pack UVs with no overlap (UV Packer), add image texture, bake Diffuse (direct/indirect off) with select-to-active and cage to one shared texture.
- t2: **High-to-low normal bake for rocks**: Decimate a duplicate heavily, add manual seams, unwrap, create 4K normal map, bake Normal in Cycles select-to-active, reduce cage extrusion, connect to shader.
- t3: **Clone brush artifact fix**: Texture paint mode, Clone brush, Ctrl+click source area, paint over artifacts; save the image afterward.
- t4: **Roughness/metal map from paint fill**: Create image texture, set Non-Color, use texture paint fill brush with value, then paint black/white for variation.

## Quotes (brief, for attribution)
> Don't only ask it to do some stuff. But I really encourage you to try asking like what is the best easiest way or fastest way.  (at 27:41, Stefan 3D AI)

## Points to
- blender-mcp (mentioned only as a Claude+Blender setup, unnamed)
- Hunyuan 3D
- Tripo P2
- Moondiff
- UV Packer add-on
- Node Wrangler add-on
- Ultra Dynamic Sky / Weather (Unreal)
