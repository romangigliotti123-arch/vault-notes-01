---
type: research-source
id: yt-1j3SE0b-r2c
title: "Fable 5.1 FINALLY Fixed Water Simulation In Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=1j3SE0b-r2c"
published: "2026-09-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "other"]
---
# yt-1j3SE0b-r2c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator demo of driving Blender from Claude Code via the Blender Lab MCP server to build water-fluid simulation scenes from a text prompt. Covers setup, a reusable skill folder built from a YouTube tutorial, and a token/cost breakdown (~960k tokens, ~$20-35). No Roblox export or import content.

## Claims
- c1: [2:14] Setup needs a Claude subscription (Claude Code), Blender, and the official Blender Lab MCP server, installed by dragging a blue box into Blender twice. *(demo, medium; claude-blender-mcp)*
- c2: [3:10] Workflow: start with an empty Blender scene, then drop a project folder (readme, assets, references, scripts, SKILL.md) into the Claude Code session so it has context. *(demo, medium; claude-blender-mcp)*
- c3: [5:39] Author uses Fable 5.1 on high effort with bypass-permissions enabled, since Blender commands run constantly and per-command approval is impractical. *(experience, medium; claude-blender-mcp)*
- c4: [4:00] A skill can be built by giving Claude a YouTube tutorial link and asking it to pull transcript and screenshots, then rebuild the scene in Blender to verify understanding. *(demo, medium; bpy-scripting-headless)*
- c5: [4:41] Claude watching a long video frame by frame makes the skill-building run slow and token-heavy. *(opinion, low; other)*
- c6: [7:01] Run used a director agent (Fable 5.1) that spawned sub-agents for lighting, scripting, environment building and geometry nodes; total ~960,000 tokens. *(data, medium; creator-workflows)*
- c7: [7:41] Estimated cost of the first run on API tokens was about $20-35 (estimate ~$25); author was on a Max subscription. *(data, medium; creator-workflows)*
- c8: [8:22] Repeat runs get cheaper because the skill/context already exists; first run from an empty session costs more. *(opinion, low; creator-workflows)*
- c9: [0:58] Claude talks to Blender through the MCP connection and runs Python it writes into the open Blender viewport session, since Blender is Python-scriptable. *(demo, medium; claude-blender-mcp)*

## Numbers
- n1: **total tokens**: ~960,000 
- n2: **estimated API cost**: $20-35 (est. ~$25) 
- n3: **MCP install steps**: drag blue box into Blender 2x 
- n4: **community size**: ~3,000 members (creator claim) 

## Techniques
- t1: **Blender Lab MCP + Claude Code**: Install Claude Code and the official Blender Lab MCP server in Blender; run Claude in a project folder; prompt it to drive the open Blender session.
- t2: **Save-as-skill iteration**: After a scene looks right, save the working scripts into the project or as a section of SKILL.md so future runs reuse context.

## Points to
- Blender Lab MCP server (official Blender site)
- YouTube tutorial on quick Blender water simulation (source of skill)
