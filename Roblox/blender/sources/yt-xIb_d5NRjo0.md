---
type: research-source
id: yt-xIb_d5NRjo0
title: "How To Create INSANE Scenes In Blender + Opus 5.5"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=xIb_d5NRjo0"
published: "2026-09-27"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "procedural-generation"]
---
# yt-xIb_d5NRjo0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video (9 min) showing Claude Opus 5.5 driving Blender via the official Blender MCP server plus BlenderKit (free asset library, ~140k models) to build interior/exterior scenes (modern living room previs, vintage car garage). Covers install steps and prompting. Nothing on Roblox export, import, or mesh limits; the Roblox angle in the title is absent from the transcript.

## Claims
- c1: [1:27] Official Blender MCP server is installed by dragging its box into an open Blender viewport twice; author says it is from the official Blender site, not GitHub. *(demo, medium; claude-blender-mcp)*
- c2: [2:22] BlenderKit is a free asset library (models, HDRIs, materials, scenes, brushes) reported at about 140,000 free assets, with a paid tier; Claude can search and import from it via MCP. *(demo, medium; claude-blender-mcp)*
- c3: [3:15] BlenderKit install: Edit > Preferences > Add-ons dropdown arrow > Install from Disk, select the BlenderKit zip. *(demo, high; claude-blender-mcp)*
- c4: [4:37] Author's opinion: using a pre-existing asset library lets the agent save tokens and cost versus generating geometry and textures itself; agent-generated chairs would look worse. *(opinion, low; creator-workflows)*
- c5: [5:30] Author verified connection by asking Claude to search BlenderKit and test-import a free model; he uses a downloadable 'Blender AI starter pack' skill zip that sets up MCP and skills. *(demo, medium; claude-blender-mcp)*
- c6: [6:49] A single natural-language prompt ('modern home previs, cozy living room') produced a furnished scene; author notes structured prompts would reduce back-and-forth iterations. *(demo, medium; procedural-generation)*
- c7: [8:08] Vintage car in garage prompt: agent searched BlenderKit for car and garage assets and assembled the scene; viewed in Material Preview. *(demo, medium; creator-workflows)*

## Numbers
- n1: **Blender version**: 5.2.2 (author's stated latest) 
- n2: **Claude subscription tiers**: $20, $100, $200 per month 
- n3: **BlenderKit free assets**: ~140,000 

## Techniques
- t1: **BlenderKit-backed agent building**: Install BlenderKit zip via Preferences > Install from Disk; let Claude search the BlenderKit library by keyword and place assets, instead of generating geometry from scratch.

## Quotes (brief, for attribution)
> the best library that is completely free, it does have a paid tier where you can get access to more  (at 2:22, Aidan Stanik)

## Points to
- Blender MCP server (official Blender)
- BlenderKit
- Claude Opus 5.5
- Creative AI Network classroom (Blender AI starter pack)
