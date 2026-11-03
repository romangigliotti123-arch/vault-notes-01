---
type: research-source
id: yt-FCaDpBvARyk
title: "Claude + Blender MCP: Photoreal Nature Scenes in 11 Minutes"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=FCaDpBvARyk"
published: "2026-08-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0030
relevance: 2
density: medium
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "procedural-generation", "texturing-baking-uv"]
---
# yt-FCaDpBvARyk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Aidan Stanik video showing Claude Code/desktop driving Blender via the official Blender MCP add-on to build a procedural jungle/nature scene with a 4-worker sub-agent skill file. No Roblox content: no export, import, mesh limits or UGC. Useful only as a general Claude-to-Blender MCP and sub-agent workflow reference.

## Claims
- c1: [0:58] Four prerequisites named: Claude subscription with Claude Code (desktop app or terminal), latest Blender, the Blender MCP add-on, and a skill.md project file. *(demo, high; claude-blender-mcp)*
- c2: [1:40] Install Blender MCP from the blender.org lab MCP server page: drag the add-on into Blender, then enable it under Preferences > Add-ons by searching MCP. *(demo, high; claude-blender-mcp)*
- c3: [2:20] In Claude desktop: Customize > Connectors > Add/Browse connectors, search Blender, enable and authorize. Install page on screen lists Blender 5.1 or newer. *(demo, medium; claude-blender-mcp)*
- c4: [2:50] Skill file uses sub-agents to cut credit and time cost; the author claims splitting work across agents gives less context spend and more accurate setup. *(opinion, low; claude-blender-mcp)*
- c5: [3:31] Director agent (strongest model, Fable 5 in video) never touches Blender; orchestrates Opus and Sonnet worker agents, one researching, one building, one scripting. *(demo, medium; claude-blender-mcp)*
- c6: [4:25] Workflow: enable bypass permissions, upload zip of skill and readme, prompt Claude to set up scene, answer questions on scene type, mood (misty dawn) and deliverable (single still). *(demo, high; creator-workflows)*
- c7: [5:49] Author advises against fly-through video: Claude moves the camera ridiculously fast; animate the camera manually and render a single still to verify. *(opinion, medium; claude-blender-mcp)*
- c8: [6:29] Reference image must be saved as a file, not pasted, so sub-agents can read it; copy path via Option + right-click 'Copy as path name' and paste into prompt. *(demo, high; claude-blender-mcp)*
- c9: [7:13] Four worker agents run in parallel: terrain, background jungle, understory and vines, lighting/camera/render; Fable 5 director verifies. Task panel shows token use and tool calls per worker. *(demo, high; claude-blender-mcp)*
- c10: [0:00] Whole scene generated in just under 5 minutes; generated script is editable and re-runnable with one click. *(demo, medium; claude-blender-mcp)*
- c11: [8:29] First render: trunk bark noticeably less detailed than reference; vines and leaves need more texturing; foreground and background judged acceptable. *(demo, high; texturing-baking-uv)*
- c12: [9:10] Suggested next step: add a dedicated texturing agent for leaves and trunk on top of the base build sub-agents. *(opinion, medium; creator-workflows)*
- c13: [9:21] Scene variation is controlled by random seeds in the script: terrain 111, understory 333, background 222, lighting 404; changing a seed regenerates only that element. *(demo, high; procedural-generation)*
- c14: [10:02] Re-running with seed 999 changes lighting; re-entering 404 restores the exact original lighting, showing seeds are deterministic. *(demo, high; procedural-generation)*
- c15: [10:17] Author offers a free project file (nature realism setup folder with readme.md, skill.md, references) via video description; not verified here. *(doc, low; creator-workflows)*

## Numbers
- n1: **scene build time**: under 5 minutes 
- n2: **minimum Blender version (on-screen install page)**: 5.1 
- n3: **parallel worker agents**: 4 workers + 1 director 
- n4: **random seeds used**: terrain 111, background 222, understory 333, lighting 404 
- n5: **lighting seed test**: 999 changed lighting; 404 restored it 
- n6: **video length**: 10:59, 7160 views, dated 2026-08-14 

## Techniques
- t1: **Blender MCP add-on install**: Open blender.org lab MCP server page, drag add-on into Blender, enable in Preferences > Add-ons, search MCP. Connect Claude via Connectors browse and authorize.
- t2: **Director plus worker sub-agents**: Skill.md spawns one director (top model) that writes a spec and dispatches parallel workers for terrain, background, understory, lighting/camera; director verifies output.
- t3: **Reference image by file path**: Save reference as PNG, Option+right-click Copy as path name, paste path into prompt so sub-agents can read it.
- t4: **Seed-driven remix**: Open script in Blender scripting tab, change random seed constant for terrain, understory, background or lighting, run; reuse seed to reproduce.

## Quotes (brief, for attribution)
> It just orchestrates Opus and Sonnet agents to build inside of Blender.  (at 3:31, Aidan Stanik)
> Claude likes to edit the camera ridiculously fast for some reason.  (at 5:49, Aidan Stanik)

## Points to
- blender.org lab MCP server page (Blender MCP official)
- Claude desktop Connectors browse (Blender)
- Fable 5 / Opus / Sonnet models named in video

## Visual notes
Contact sheet shows the blender.org MCP Server page with Requirements: Blender 5.1 or newer, Add-on, LLM Client, MCP Server; Blender preferences add-on list; Claude Code task panel with four worker tasks and token counts; a Blender scripting window with a jungle script.
