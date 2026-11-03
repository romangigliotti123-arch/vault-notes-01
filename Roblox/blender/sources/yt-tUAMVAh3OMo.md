---
type: research-source
id: yt-tUAMVAh3OMo
title: "Building Procedural Simulation Environments — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=tUAMVAh3OMo"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-tUAMVAh3OMo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Academic BCON26 talk on using Blender geometry nodes and Python to generate procedural radio-propagation scenes, export them to the Sionna RT solver (via Mitsuba XML), and visualize results back in Blender. Off-topic for Roblox, Claude/blender-mcp, and the Roblox asset pipeline. No Roblox export, rigging, or Claude workflow content.

## Claims
- c1: [1:00] Speaker argues Blender can host scene modeling, solver export, and visualization in one workflow instead of fragmented tools. Opinion, no Roblox relevance. *(opinion, high; other)*
- c2: [11:50] Speaker used Blender Mitsuba add-on version 3.6 to export scenes to Mitsuba XML for Sionna RT; said it worked for them, later versions unverified. *(experience, medium; other)*
- c3: [19:38] Speaker says 12 bounces was enough for one scene to stabilize results; sensitivity sweeps used to justify settings. *(demo, low; other)*

## Numbers
- n1: **Mitsuba add-on version**: 3.6 
- n2: **ray bounces stabilizing results**: 12 
- n3: **frequency sweep range**: 1 to 100 GHz 
- n4: **voxel size for 3D map**: 5 m 

## Points to
- Sionna RT (NVIDIA)
- Mitsuba
- Jupyter notebooks
- Blender OpenStreetMap add-on
- SUMO
