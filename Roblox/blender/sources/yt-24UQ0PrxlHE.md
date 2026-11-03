---
type: research-source
id: yt-24UQ0PrxlHE
title: "Claude + Blender: Geometry Nodes for Beginners"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=24UQ0PrxlHE"
published: "2026-08-21"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "procedural-generation"]
---
# yt-24UQ0PrxlHE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video shows driving Blender geometry nodes from Claude Code using a downloadable geometry-nodes skill.md zip (with reference scripts and examples). Setup: run /init on the skill folder, enable Blender connector in Claude desktop, keep Blender running. A Fable 5 director delegates to Opus, Sonnet and Haiku sub-agents. Gumdrop scene generated in about 6 minutes; density tweaked via modifier. No Roblox content.

## Claims
- c1: [0:00] Creator says Claude generated a gumdrop-with-sugar-cubes geometry nodes scene, including camera and rendered image, in one session. *(demo, medium; procedural-generation)*
- c2: [1:15] Blind prompting Claude to build geometry nodes without a skill file is claimed to produce poor results; no comparison shown. *(opinion, low; claude-blender-mcp)*
- c3: [4:03] Claude desktop: enable Blender via Customize > Connectors, with Blender installed and running. *(demo, medium; claude-blender-mcp)*
- c4: [3:23] Skill is loaded by uploading zip into Claude session and running /init on the geometry nodes folder, which creates a reusable slash command. *(demo, medium; claude-blender-mcp)*
- c5: [5:50] Multi-model setup: Fable 5 acts only as director and never runs Blender code; Opus, Sonnet and Haiku execute, with Haiku used for render pass to save tokens. *(demo, medium; creator-workflows)*
- c6: [6:24] Initial scene build took about 6 minutes; sugar cube count was too low and was fixed by raising the density value in the geometry nodes modifier. *(demo, high; creator-workflows)*
- c7: [2:21] Skill zip contains a gumdrop reference, a gumdrop example MD file, a node-scripting reference, and skill.md with best-practice steps. *(doc, medium; procedural-generation)*
- c8: [2:50] Creator says skill was distilled from analysing hundreds of geometry nodes tutorial videos, mainly Blender Guru content. *(experience, low; procedural-generation)*
- c9: [0:42] Opinion: artist must remain director; Claude should not direct all modelling, animation and geometry nodes work. *(opinion, medium; creator-workflows)*
- c10: [7:46] Material colour can be changed afterwards in the Shading workspace, e.g. blue gumdrop to green. *(demo, medium; creator-workflows)*

## Numbers
- n1: **generation time**: ~6 minutes 
- n2: **sugar density value**: 250 then 300 
- n3: **video length**: 8:23 

## Techniques
- t1: **Skill-file loading**: Upload skill zip to Claude session, run /init on the folder so Claude analyses skill.md and saves it as a project slash command.
- t2: **Director-worker agent split**: Prompt top model as director that spawns sub-agents by role: scene objects, geometry nodes, materials, render pass on cheapest model.
- t3: **Density tuning via modifier**: Open geometry nodes modifier on the object and raise the sugar density input to add instances after generation.

## Quotes (brief, for attribution)
> If you're a 3D artist, you are still the director. Claude is just essentially a agent or an extra person on your team  (at 0:42, Aidan Stanik)

## Points to
- Blender Guru geometry nodes for beginners parts 1 and 2
- Nate Hurk multi-agent framework
- Excalidraw
- Creative AI Network (Skool community)
