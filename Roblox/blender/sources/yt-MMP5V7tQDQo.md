---
type: research-source
id: yt-MMP5V7tQDQo
title: "DARKER SHADOWS IN ROBLOX GFX (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=MMP5V7tQDQo"
published: "2022-09-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: low
tags: ["research-source", "youtube", "creator-workflows", "other", "texturing-baking-uv"]
---
# yt-MMP5V7tQDQo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender Cycles/Eevee tutorial for darkening ambient-occlusion shadows on Roblox GFX character renders. Build a mix shader: AO node into a Color Ramp factor, ramp colour into a Mix Shader factor, original Principled BSDF kept on the bottom input. Not about blender-mcp, bpy scripting, or Roblox export.

## Claims
- c1: [0:00] Creator says GFX community lacks cast shadows, making object dimensions hard to read; wants stronger shadows for GFX renders. *(opinion, medium; creator-workflows)*
- c2: [0:40] Creator says Cycles shows more shadows by default than Eevee but preview is very noisy; recommends Eevee with ambient occlusion as one option. *(opinion, low; other)*
- c3: [1:20] Method: AO node -> Color Ramp factor; Color Ramp colour -> Mix Shader factor; original Principled BSDF stays on the bottom Mix Shader input; Mix Shader output to Material Output surface. *(demo, medium; texturing-baking-uv)*
- c4: [2:02] Darkening shadows is tuned via the Color Ramp; the creator also adjusts AO distance, and says the effect adds photorealism on his face fix. *(demo, medium; creator-workflows)*

## Numbers
- n1: **Views / length**: 1534 views, 3:15 video dated 2022-09-26 

## Techniques
- t1: **AO-driven shadow darkening via material mix**: Add AO node, feed into Color Ramp factor, feed ramp colour into Mix Shader factor, keep original BSDF on bottom input. Adjust ramp stops to deepen shadows, tweak AO distance. Works in Cycles or Eevee; preview is noisy in Cycles.
