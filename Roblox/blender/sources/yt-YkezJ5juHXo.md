---
type: research-source
id: yt-YkezJ5juHXo
title: "Opus 5.5 + Blender Builds Surprisingly Good Horror Games"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=YkezJ5juHXo"
published: "2026-10-01"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "common-mistakes-fixes", "texturing-baking-uv"]
---
# yt-YkezJ5juHXo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator video showing a Backrooms horror game and a kart racer built with Claude Code (Opus 5.5), Blender connected via MCP, and Higgsfield for images/audio. Covers a /gamebuilder skill that sets up Blender and Higgsfield connectors, and Blender used to place textures and lights. Nothing about Roblox Studio, Roblox export, or mesh limits. Promotional in parts.

## Claims
- c1: [4:33] Blender is connected to Claude Code as a connector; the creator says it was built inside a Blender folder holding existing skills and knowledge. *(demo, medium; claude-blender-mcp)*
- c2: [6:15] Connectors panel in Claude Code showed Blender and Higgsfield connected; a /gamebuilder skill reportedly sets up both connections if missing. *(demo, medium; claude-blender-mcp)*
- c3: [1:54] Creator says Blender 5.2.2 is required and that assets are written as code to become 3D models. *(opinion, low; claude-blender-mcp)*
- c4: [0:53] Generated carpet and wallpaper images are placed on Blender geometry and distorted in Blender to simulate worn, textured surfaces with light reflection. *(demo, medium; texturing-baking-uv)*
- c5: [5:14] Creator runs Claude Code desktop with bypass permissions on, Opus 5.5 model and effort set to extra; claims Opus uses fewer tokens. *(opinion, low; claude-blender-mcp)*
- c6: [8:24] Initial one-prompt build had no flashlight; creator had to request it as an extra fix. *(demo, medium; common-mistakes-fixes)*

## Numbers
- n1: **Blender version**: 5.2.2 
- n2: **Build time claimed**: under 15 minutes, one iteration (Backrooms game) 

## Techniques
- t1: **Folder-scoped Claude Code session with Blender connector**: Open Claude Code desktop in a dedicated project folder holding Blender skills, enable Blender and Higgsfield connectors, then prompt for the game. Creator asserts this lets Claude reuse stored knowledge.
- t2: **Generated image as distorted surface texture**: Generate wallpaper/carpet images via image model, apply to Blender geometry, then distort/displace in Blender for a worn look. Method described, not shown in detail.

## Points to
- higgsfield.ai/mcp
- Claude Code desktop app
- Blender MCP connector
- /gamebuilder skill (free school community, linked in description)
