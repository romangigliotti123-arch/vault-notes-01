---
type: research-source
id: yt-9kejfKCb0S8
title: "I Built a Souls-Like Game in 3 Days - Every Asset Made by AI"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=9kejfKCb0S8"
published: "2026-08-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0037
relevance: 1
density: low
tags: ["research-source", "youtube", "common-mistakes-fixes", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# yt-9kejfKCb0S8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Stefan 3D AI video on building a souls-like game in 3 days with AI-generated assets, mainly Tripo (high-poly generation, retopo), Patina tiled textures, Blender baking, and Unreal Engine 5.8 with Claude Code and a UE MCP. Almost nothing on Roblox, blender-mcp, or bpy scripting. Only the Blender baking and high-poly-then-retopo steps are loosely relevant.

## Claims
- c1: [4:29] Creator generates high-poly textured models in Tripo, then decimates or retopologises, then bakes normal and AO maps (and colour) in Blender, controlling parameters. *(demo, medium; texturing-baking-uv)*
- c2: [8:51] Baking is done in Blender with Cycles; colour, ambient occlusion, normal and other maps baked from high-poly to low-poly. UV is produced via xatlas in Tripo or a Blender UV packing add-on. *(demo, medium; texturing-baking-uv)*
- c3: [8:10] For static assets creator skipped perfect wireframe and manual UV unwrapping to save time; Tripo smart low-poly gives cleaner topology but may need manual refinement. *(opinion, medium; texturing-baking-uv)*
- c4: [4:29] Tripo smart mesh is limited to about 20k triangles, so high-poly generation is used and then reduced. *(experience, low; procedural-generation)*
- c5: [5:10] Large surfaces use tiled seamless AI textures (Patina, via fold.ai) rather than one 8K texture, to avoid blurriness up close; AI also produced matching AO and normal maps from the same texture. *(demo, medium; texturing-baking-uv)*
- c6: [15:21] Blender material export to Unreal does not carry over settings well, so shaders are usually rebuilt in the engine. *(experience, medium; common-mistakes-fixes)*
- c7: [13:35] Humanoid rigging is quick with markers; weights usually still need review after export. *(experience, low; rigging-animation)*

## Numbers
- n1: **Tripo smart mesh triangle limit**: 20k triangles 
- n2: **Texture resolution note**: 8K insufficient for large arena surface; tiling used instead 
- n3: **Build time**: 72 hours total; about 1.5 days for assets 

## Techniques
- t1: **High-poly generate, retopo, bake**: Generate high-poly textured mesh in Tripo; decimate or retopologise in Blender or Tripo; bake normal, AO and colour from high to low poly in Blender Cycles; UV via xatlas or packing add-on.
- t2: **Tiled PBR surfaces**: Generate seamless tiled texture sets (Patina) from text or image prompt; apply to large surfaces via UV tiling instead of one high-res texture.

## Points to
- Tripo (Tripo3D) retopology and smart mesh
- Patina (fold.ai) tiled textures
- Unreal Engine 5.8 with Vibe UE MCP
- Claude Code
- Ultra Dynamic Sky / Weather
