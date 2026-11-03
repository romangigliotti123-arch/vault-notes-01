---
type: research-source
id: yt-kfEahHL_grk
title: "Compositor Fast CACHE & NEW NODES 🎨 Blender Today LIVE #284 "
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=kfEahHL_grk"
published: "2026-06-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0050
relevance: 1
density: low
tags: ["research-source", "youtube", "blender-roblox-export-import", "other"]
---
# yt-kfEahHL_grk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live #284 (June 2026) covers Blender 5.2 LTS news: Vulkan default on Windows/Linux, compositor playback cache, file-handle limit raise, Grease Pencil and geometry nodes additions, Alembic/USD I/O changes. Nothing on Roblox, Claude, blender-mcp, bpy automation, or Roblox export. Relevance to the topic is minimal.

## Claims
- c1: [1:31] USD export of normals will follow Blender's internal data model (point/corner/face) instead of always converting to face-varying corners, aimed at game engines that store per-point normals. *(doc, medium; blender-roblox-export-import)*
- c2: [0:31] Vulkan becomes the default GPU backend on Windows (x86) and Linux, applied only to new setups or factory startup; existing preferences are unchanged. *(doc, medium; other)*
- c3: [0:31] Speaker says Blender 5.2 LTS release is 14 July (corrected from 17 July mid-stream); no Roblox-related content. *(opinion, low; other)*

## Numbers
- n1: **file handle limit**: 512 (Windows), 256 (macOS) raised to 8,192 on all platforms 
- n2: **paint update time**: 678 ms to 380 ms (~43% faster) on Suzanne 31k polys, 4K texture 
- n3: **GPU EXR playback**: 6.5 fps to 14.5 fps (PR figure) 

## Points to
- Blender Studio Vault announcement
- Blender 5.2 LTS demo files on blender.org
- Kando pie menu (Linux)
