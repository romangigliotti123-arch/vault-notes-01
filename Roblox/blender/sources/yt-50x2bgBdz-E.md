---
type: research-source
id: yt-50x2bgBdz-E
title: "Intel Open Image Denoise 3: Fast Temporal Denoising & Supersampling in Cycles — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=50x2bgBdz-E"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-50x2bgBdz-E

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Conference talk on Intel Open Image Denoise (OIDN) 3.0 for Cycles: kernel-prediction network, temporal viewport denoising with 2.5D motion vectors, 1x-3x upscaling, composable AOVs, custom retraining. Contains no Roblox Studio, blender-mcp, bpy scripting, or Blender-to-Roblox export content. Relevance to the topic is minimal.

## Claims
- c1: Source does not cover Roblox Studio, blender-mcp, bpy scripting, or the Blender-to-Roblox asset pipeline; it is about a Cycles denoiser. *(doc, high; other)*
- c2: [17:03] OIDN 3.0 supports 1x to 3x upscaling; demos rendered at low internal resolution on an Intel Arc B390 iGPU laptop. *(demo, medium; other)*
- c3: [27:42] Planned OIDN release timeline: alpha Oct-Nov 2026, beta around Dec 2026, final 3.0 in Q1 2027, temporal final-frame filter in 3.1 in Q2 2027. *(doc, medium; other)*
- c4: [7:17] Kernel prediction lets one predicted filter kernel apply to color and other AOVs; feature extraction uses int8, filtering uses FP16. *(doc, medium; other)*
- c5: [14:11] OIDN is open source (Apache 2.0) with a PyTorch training toolkit; Blender collaboration added a script to export denoising AOVs in the training format. *(doc, medium; other)*

## Numbers
- n1: **upscaling factor**: 1x-3x OIDN 3.0 joint denoise+upscale; demos used 3x on Intel Arc B390 iGPU
- n2: **final release**: Q1 2027 OIDN 3.0 final; 3.1 with final-frame temporal filter in Q2 2027

## Points to
- Intel Open Image Denoise (OIDN), Apache 2.0
- Blender 5.2 Cycles denoiser integration
- Blender Studio Nishita sky demo
- Flavio Della Tomassa Helen flight scene
- Carlobir Gancini Lone Monk scene
