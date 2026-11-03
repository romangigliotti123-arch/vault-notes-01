---
type: research-source
id: yt-4jODU0Us8gk
title: "Headless Heads: Calibrated Digital Human Pipelines with Cycles — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=4jODU0Us8gk"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-4jODU0Us8gk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Roblox. An EA character artist's BCON26 talk on light-stage scanning, cross-polarized diffuse capture, color calibration, and a Cycles shader/compositor hack for polarization-dependent specular. Only tangential bpy relevance: headless Blender run in Docker via the bpy module inside a scan-processing pipeline. Nothing on Roblox export, MCP, rigging, or UGC.

## Claims
- c1: [6:50] Blender can run headlessly in Docker by installing the bpy Python module on a base image with Python; the speaker's pipeline imports bpy to script any Blender operation. *(demo, medium; claude-blender-ai)*
- c2: [21:52] Polarization-aware specular can be approximated in Cycles by writing a custom AOV multiplier from Fresnel curves and then multiplying glossy passes in the compositor; speaker calls it a hack, not exact. *(demo, medium; other)*
- c3: [13:56] Color calibration with a 3x3 matrix maps camera RGB to a target working space; cross-polarized images lack matching chart reference values, so the mixed-polarization matrix is reused as an approximation. *(opinion, low; other)*
- c4: [7:31] Built-in Blender deformers were used to wrap a lacrimal mesh to each scanned head shape and conform it to the eyeball and eyelid. *(demo, low; other)*

## Techniques
- t1: **Headless bpy in Docker**: Base image with OS and Python, add dependencies and env vars, pip install the Blender bpy module, then import bpy in pipeline code. Render preview images to inspect results during headless runs.
- t2: **Baked UV remapping for texture transfer**: Ray-cast in an ideal pose to bake a UV warp map; use it to remap normal or displacement data into the target UV space, avoiding baking artifacts across poses.
- t3: **Cycles specular polarization AOV**: Compute two Fresnel curves plus an average curve, mix by view vector and object normal, divide by average, write as AOV; multiply glossy pass by it in compositor, attenuated by roughness.

## Points to
- Mitsuba 3
