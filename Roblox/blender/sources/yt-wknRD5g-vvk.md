---
type: research-source
id: yt-wknRD5g-vvk
title: "NVIDIA Kimodo Now Runs Without a GPU - Free Local Workflow"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=wknRD5g-vvk"
published: "2026-08-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0058
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# yt-wknRD5g-vvk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Roblox: an Unreal Engine and Blender AI-asset workflow video. Its useful parts are Blender techniques: UV Packer before baking, Cycles diffuse and normal bakes to a single atlas, decimating a ~1M-poly rock to ~1k, Node Wrangler scale mapping, clone-brush cleanup and color matching. It never covers Kimodo, bpy, blender-mcp or Roblox export.

## Claims
- c1: [10:04] Blender native clone brush (Ctrl+click to sample, then paint) is used to remove small texture artifacts instead of a round trip to an AI texture tool. *(demo, medium; mesh-texture-limits)*
- c2: [12:47] UV Packer add-on, used in edit mode via unwrap then pack with margin, makes merged objects' UVs non-overlapping before baking. *(demo, medium; mesh-texture-limits)*
- c3: [13:28] Bake settings: Cycles, Diffuse, direct and indirect lights unchecked, Selected to Active, cage enabled, bake into a new image texture to produce one texture atlas for several objects. *(demo, medium; mesh-texture-limits)*
- c4: [15:29] A rock built from about 1,000,000 polygons was decimated to roughly 1,000 polygons (ratio around 0.1) to serve as a low-poly base. *(demo, medium; mesh-texture-limits)*
- c5: [17:30] Normal map baked from the high-poly rock to the low-poly version at 4K using Cycles Normal Map with selected-to-active; cage extrusion lowered because the shape does not match exactly. *(demo, medium; mesh-texture-limits)*
- c6: [18:51] Material scale is set with a mapping node added via Ctrl+T (requires Node Wrangler add-on enabled); the author settled on scale 4. *(demo, medium; mesh-texture-limits)*
- c7: [14:49] Roughness and metallic maps are created by setting Image Texture nodes to Non-Color and painting values with the Texture Paint fill brush. *(demo, medium; mesh-texture-limits)*
- c8: [11:26] Color mismatch between AI-generated textures is corrected with Blender color nodes (gamma, contrast, RGB curves) inserted before the material input, then baked into a new texture. *(demo, medium; mesh-texture-limits)*
- c9: [4:01] Hunyuan 3D free tier cited as 23 daily generations; Smart Topology in the same tool outputs low-poly meshes using the same credit pool, with triangle or quad options. *(doc, low; other)*
- c10: [6:40] One texture is used for four paper objects by creating one plane and splitting it into four parts so the objects share a material. *(demo, medium; mesh-texture-limits)*
- c11: [27:37] Creator's opinion: a Bezier-curve rope converted to mesh was about five times faster than generating a rope with AI. *(opinion, low; other)*
- c12: [28:17] Creator mentions using a Claude plus Blender setup and suggests asking it for the easiest or fastest method, but shows no Claude or MCP steps. *(opinion, low; claude-blender-ai)*
- c13: [31:00] Creator states Unreal Engine 5.9 is announced with native MCP; no details given. *(opinion, low; other)*

## Numbers
- n1: **rock poly count**: 1,000,000 -> ~1,000 polygons 
- n2: **Hunyuan free daily generations**: 23 
- n3: **texture mapping scale**: 4 
- n4: **normal map resolution**: 4K 
- n5: **rope speed vs AI (opinion)**: ~5x faster 

## Techniques
- t1: **Atlas bake via Cycles**: Duplicate objects, UV Packer pack non-overlapping, new material with image node, Cycles Diffuse bake with direct/indirect off, Selected to Active, cage on, bake to single image.
- t2: **High-to-low normal bake**: Decimate high-poly rock, add seams and unwrap, create 4K image, Cycles Normal Map bake selected-to-active, connect normal to shader.
- t3: **Clone brush cleanup**: Select object, enter Texture Paint, Ctrl+click source area, paint over artifacts, save the texture.
- t4: **Color matching nodes**: Insert gamma, contrast or RGB curves nodes between color texture and material input, tune, then bake to new texture.
- t5: **Texture scale via mapping node**: Select texture node, Ctrl+T to add mapping node (needs Node Wrangler), adjust scale; try generated or object coordinates if UV looks wrong.

## Quotes (brief, for attribution)
> we're going to create this amazing pirate cave  (at 1:14, Stefan 3D AI)
> There's an amazing free add-on called UV Packer.  (at 12:47, Stefan 3D AI)

## Contradictions flagged
- Title says Kimodo runs without a GPU. (vs Transcript never mentions Kimodo or GPU requirements; it covers Gemini, Hunyuan 3D and Blender only.)
- Video is framed as a Blender workflow for a game level. (vs Its final target is Unreal Engine, not Roblox Studio; no Roblox export settings are given.)

## Points to
- Motive (free AI texturing tool)
- Hunyuan 3D
- Gemini (Nano Banana)
- UV Packer Blender add-on
- Node Wrangler Blender add-on
- Ultra Dynamic Sky / Ultra Dynamic Weather (Unreal)
- NVIDIA Kimodo (title only)
