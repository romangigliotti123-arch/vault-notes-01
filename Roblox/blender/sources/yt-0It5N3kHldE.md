---
type: research-source
id: yt-0It5N3kHldE
title: "How I Make Realistic AI Videos with Blender + Claude"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=0It5N3kHldE"
published: "2026-10-21"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows"]
---
# yt-0It5N3kHldE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video on using Claude (Claude Code and desktop) to drive Blender via an MCP add-on for realistic renders. Covers installing the Blender MCP add-on, connecting it through Claude Connectors, and a camera/tone/lighting/texture (CTLT) markdown context file. No Roblox export, import, or mesh content.

## Claims
- c1: [7:21] Blender MCP setup: drag the install box from the MCP docs into Blender twice; first drag installs the extension, second installs the MCP add-on. *(demo, high; claude-blender-mcp)*
- c2: [8:02] After installing, enable MCP in Blender Preferences, then in Claude desktop Customize > Connectors search Blender and click Connect to get Blender tools. *(demo, high; claude-blender-mcp)*
- c3: [7:21] Video says a Claude subscription is required; it mixes Claude Code and Claude desktop setup steps without clarifying which client is needed. *(demo, medium; claude-blender-mcp)*
- c4: [9:13] A CTLT framework markdown file is uploaded into the Claude session as context; Claude then prompts for camera, tone, lighting and texture choices before building the scene. *(demo, medium; claude-blender-mcp)*
- c5: [12:09] Two-pass build: first pass sets camera, lighting and main textures; second pass adds detail (rust, erosion, mountain detail). Author says fog still looked like water. *(demo, medium; creator-workflows)*
- c6: [10:49] Author's opinion: treat Claude like a junior 3D artist; without repeatable skill files and context it gives generic output. *(opinion, medium; creator-workflows)*
- c7: [9:55] Suggests adding a list of 34 AI-filmmaker camera shots as extra context so Claude picks from named shots. *(opinion, low; creator-workflows)*

## Numbers
- n1: **camera shot list size**: 34 shots 
- n2: **example lenses shown**: fish-eye, 135mm, CCTV, disposable cam 

## Techniques
- t1: **Blender MCP add-on install**: Drag MCP box into Blender twice (extension then MCP add-on). Enable in Preferences by searching MCP. Connect via Claude Connectors for Blender.
- t2: **CTLT context file**: Save framework .md file, upload into Claude session or give file path, ask Claude to walk through camera, tone, lighting, texture options before building.

## Quotes (brief, for attribution)
> You have to treat it like it just graduated from college and is just entering the industry and it doesn't have any of the industry standard experience or knowledge or context.  (at 10:49, Aidan Stanik)

## Contradictions flagged
- Setup described for Claude Code subscription, then steps given for Claude desktop Connectors. (vs Itself: which Claude client is required is unclear)

## Points to
- CTLT framework (credited to Dam Keift)
- Blender MCP docs install page (shown on screen)

## Visual notes
Contact sheet shows a Blender MCP docs page with sections Installation (requirements: Blender, add-on, LLM client, MCP server), Add-on drag-and-drop, LLM Client, and MCP Server. Other frames show Blender scenes and Claude desktop prompts for camera, tone, lighting, texture.
