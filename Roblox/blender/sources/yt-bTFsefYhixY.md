---
type: research-source
id: yt-bTFsefYhixY
title: "HOW TO MAKE REALISTIC WATER FOR ROBLOX GFX (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=bTFsefYhixY"
published: "2023-03-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-bTFsefYhixY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender GUI tutorial for making a stylised water material for Roblox GFX renders. Uses a plane with a Musgrave texture into Bump and Principled BSDF, metallic 1 and roughness 0, a Mix Shader with Transparent BSDF for transparency, and keyframed mapping offsets for animation. It does not cover Claude, blender-mcp, bpy scripting, or Roblox export/import.

## Claims
- c1: [1:49] Setting Principled BSDF metallic to 1 and roughness to 0 gives a strongly reflective water look (GFX render, not a Roblox material export). *(demo, medium; other)*
- c2: [2:30] Transparency is done by feeding Principled BSDF and Transparent BSDF into a Mix Shader; the mix factor sets how see-through the water is (0 opaque, 1 fully transparent). *(demo, medium; other)*
- c3: [4:02] Water motion is faked by keyframing the Mapping node location of the Musgrave texture; Vector handle type removes ease-in/out. *(demo, medium; other)*
- c4: [3:11] Creator switches to rendered view with Cycles on GPU compute for faster preview of the transparent shader. *(demo, low; other)*

## Numbers
- n1: **Principled BSDF settings**: metallic 1, roughness 0 
- n2: **Musgrave detail**: 15 (more detailed, slower) 

## Techniques
- t1: **Musgrave-driven water normal bump**: Add Musgrave texture, connect Height to Bump Height, Bump Normal to Principled BSDF Normal. Add Texture Coordinate Generated into Mapping then into Musgrave Vector; Ctrl+T via Node Wrangler.
- t2: **Mix Shader transparency**: Mix Principled BSDF (slot 1) and Transparent BSDF (slot 2) into Material Output; tune Fac between 0 and 1.
- t3: **Keyframed mapping offset**: Right-click Mapping location values in the Shader editor and Insert Keyframes at two frames; set Graph/Dope Sheet handles to Vector.
