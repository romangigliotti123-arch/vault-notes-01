---
type: research-source
id: yt-ia8gUVJBYh0
title: "Claude MCP + Roblox Studio - Auto Upload Images and Use Them Instantly"
source_type: "youtube"
creator: "MrWonderHow"
url: "https://www.youtube.com/watch?v=ia8gUVJBYh0"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows"]
---
# yt-ia8gUVJBYh0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender. A Roblox Studio tutorial on connecting Claude desktop to Roblox Studio via MCP, creating an Open Cloud API key with Assets read/write, allowing apis.roblox.com in Claude's capabilities, and having Claude upload two ChatGPT-generated PNGs and apply them to a two-part head/body model. No Blender, bpy, blender-mcp, FBX/glTF, or mesh/texture spec details.

## Claims
- c1: [0:26] Roblox Open Cloud API key is created in Creator Dashboard; Assets API permission needs read and write; key is shown only once. *(doc, high; automation-and-creator-workflows)*
- c2: [4:02] Claude desktop blocks outbound domains by default; apis.roblox.com must be added under Claude capabilities allowed domains before uploads work. *(demo, medium; automation-and-creator-workflows)*
- c3: [1:46] Roblox place must be saved/published to Roblox first so uploaded assets have a valid place ID to be used in the project. *(demo, medium; automation-and-creator-workflows)*
- c4: [3:30] Workflow: drop a folder with head.png and body.png plus API info text file into Claude; Claude uploads images and builds a two-part model with textures on front/back faces. *(demo, medium; automation-and-creator-workflows)*

## Techniques
- t1: **Claude-driven Open Cloud asset upload**: Create Open Cloud key with Assets read/write; store key and user ID in local text file; add apis.roblox.com to Claude allowed domains; have Claude upload PNGs and apply them as surface textures to parts.

## Points to
- apis.roblox.com
- Roblox Creator Dashboard Open Cloud API keys
- Claude desktop app MCP
