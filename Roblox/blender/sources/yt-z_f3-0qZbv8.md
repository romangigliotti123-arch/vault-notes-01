---
type: research-source
id: yt-z_f3-0qZbv8
title: "HOW TO RENDER FASTER WITH YOUR GRAPHICS CARD (Roblox GFX) (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=z_f3-0qZbv8"
published: "2023-05-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 1
density: low
tags: ["research-source", "youtube", "common-mistakes-fixes", "other"]
---
# yt-z_f3-0qZbv8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Roblox and Claude. A Blender Cycles tutorial on enabling GPU rendering: choosing compute devices by GPU vendor (CUDA, OptiX, HIP, oneAPI, Metal), switching Device to GPU Compute, and comparing denoisers. Nothing on blender-mcp, bpy scripting, Roblox export or import, or Roblox limits. Transcript has ASR errors (e.g. "Optics" = OptiX, "hip" = HIP).

## Claims
- c1: [4:37] Blender 2.79 GPU setup: File > User Preferences > System, set Cycles Compute Device to CUDA, then set render Device to GPU Compute. Older Cycles limited by CUDA support. *(demo, medium; other)*
- c2: [3:08] Cycles compute device choice by GPU vendor: CUDA for GTX, OptiX for RTX (uses ray-tracing cores), HIP for AMD, oneAPI for Intel. Mac shows only None and Metal. *(demo, medium; other)*
- c3: [6:25] Single-test render comparison: CPU took 1m18s; RTX 3050 laptop GPU with OptiX denoise took 9s, which the video calls an 87% speed increase. Single scene, no repeats. *(demo, low; other)*
- c4: [8:51] Open Image Denoise (Intel) keeps more detail but is slower; OptiX (Nvidia) is faster but loses detail. Opinion: choose by speed versus look. *(opinion, low; other)*
- c5: [9:31] Claims Blender 3.0 gave a 7x faster Cycles render engine and added OptiX denoising and Metal rendering. Advises using a recent Blender version. *(opinion, low; other)*
- c6: [1:27] Using the integrated GPU for rendering, or a GPU already driving the display, may cause instability and poor performance; use the dedicated GPU. Outdated drivers can cause buggy or failed rendering. *(opinion, medium; common-mistakes-fixes)*

## Numbers
- n1: **render time CPU vs GPU**: 1m18s vs 9s same scene; CPU with Open Image Denoise, GPU with OptiX denoise
- n2: **claimed speedup**: 87% stated by the video from the timings above
- n3: **claimed Cycles speedup in Blender 3.0**: 7x video's claim, unsourced

## Techniques
- t1: **Enable GPU Cycles rendering**: Preferences > System > Cycles Render Devices: tick the vendor backend (CUDA/OptiX/HIP/oneAPI/Metal) and the GPU, not the CPU. Then in Render Properties set Device to GPU Compute.
