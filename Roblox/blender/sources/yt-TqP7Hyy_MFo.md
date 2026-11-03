---
type: research-source
id: yt-TqP7Hyy_MFo
title: "Subject Extraction for Scene Reconstruction in VFX — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=TqP7Hyy_MFo"
published: "2026-09-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-TqP7Hyy_MFo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender-to-Roblox and Claude/blender-mcp. A BCON26 talk on RotoForge, a Blender extension for ML-assisted rotoscoping built on Segment Anything. It covers installing Python wheels in a Blender extension via a subprocess installer, and an RGBMatte-style alpha/foreground model (~2 GB VRAM). Nothing on Roblox, MeshPart, FBX/glTF, rigging, or Claude.

## Claims
- c1: [4:07] Installing Python packages into Blender by importing a custom dir into sys.path freezes the UI and breaks Extensions platform self-contained rules; wheels are the official route. *(opinion, medium; other)*
- c2: [6:34] RotoForge installer runs pip in a separate subprocess with --progress-bar raw and logs to a file, polled by a Blender timer to update UI. *(demo, medium; other)*

## Numbers
- n1: **VRAM**: under 2 GB in full precision; target ~6 GB 
- n2: **Training hardware**: laptop with 8 GB VRAM 
- n3: **Model size comparison**: Corridor Key ~11 GB; RotoForge model under 2 GB 

## Techniques
- t1: **Subprocess-based pip install with file-logged progress**: Run installer as separate process, pipe pip output to log file, poll with Blender timer, then rewrite blender_manifest.toml to use wheels and restart.

## Points to
- RotoForge (Blender extension)
- Segment Anything (Meta)
- Corridor Key
- DINOv2
