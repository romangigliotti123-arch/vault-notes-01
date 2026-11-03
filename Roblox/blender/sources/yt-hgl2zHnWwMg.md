---
type: research-source
id: yt-hgl2zHnWwMg
title: "I Tested Claude Fable 5 in Blender (5x Faster Than Opus 4.8)"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=hgl2zHnWwMg"
published: "2026-06-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 2
density: medium
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "procedural-generation", "rigging-animation"]
---
# yt-hgl2zHnWwMg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator connects the official Blender MCP to Claude Code (desktop app) and prompts Fable 5 to build studio, sci-fi alley, and animate a Blender Studio rig in Blender. Shows one-prompt scene builds, a Cycles iteration, and two-prompt walk/wave fixes. No Roblox export, bpy script, or pipeline content.

## Claims
- c1: [0:00] Official Blender MCP (from blender.org) connects Claude Code to a live Blender; verified via /mcp command listing and a prompt that returned a viewport render of the default cube. *(demo, high; claude-blender-mcp)*
- c2: [3:49] Video uses Claude desktop app Code tab with a project folder and bypass-permissions mode for Blender control; author says it is not invasive to the laptop (opinion). *(demo, medium; claude-blender-mcp)*
- c3: [6:21] Single prompt for studio still life (curved floor-wall backdrop, mug, 3-point light, gray world) produced a scene in about 30 seconds; author rates it basic, not perfect. *(demo, medium; claude-blender-mcp)*
- c4: [8:04] Alley first pass built from one prompt used plain cube facades and boxes; author judged walls and lights too basic and asked for iteration on detail. *(demo, medium; procedural-generation)*
- c5: [9:38] Iteration prompt asked Claude to switch render engine to Cycles, enable denoising, set sensible sample count, and add grime; output added beveled box corners and cardboard material (author's observation). *(demo, medium; claude-blender-mcp)*
- c6: [11:13] Used Blender Studio's Storm character blend file with full existing rig, so no rigging was needed; prompt asked Claude to list armatures and bone names first. *(demo, high; rigging-animation)*
- c7: [12:35] First Claude walk+wave animation had palm facing sideways and a stiff walk; a second prompt fixed hand orientation and locked camera, requiring two prompts total. *(demo, high; rigging-animation)*
- c8: [12:35] Author says animation prompts were about five times faster than Opus 4.8 with fewer errors (subjective, single test). *(experience, low; rigging-animation)*
- c9: [14:02] Cliff scene with forest backdrop and depth of field was added in a third prompt; author says output is low poly and would need rocks and more depth. *(demo, medium; creator-workflows)*
- c10: [2:28] Fable 5 usable via subscription (Pro, Max, or Teams) until June 22; afterward usage-based billing, per author. *(doc, medium; creator-workflows)*
- c11: [0:42] Author cites agentic coding benchmark 80.3% for Fable 5/Mythos 5 vs 69.2% for Opus 4.8 (vendor figure relayed by author). *(doc, low; claude-blender-mcp)*

## Numbers
- n1: **agentic coding score**: 69.2% (Opus 4.8) vs 80.3% (Fable 5/Mythos 5) 
- n2: **simple scene build time**: ~30 seconds 
- n3: **animation frame rate and length requested**: 24 FPS, 2 to 5 seconds 
- n4: **Fable 5 subscription cutoff before usage billing**: June 22 
- n5: **Blender Studio membership price**: $15/month 
- n6: **time for three prompts on cliff scene**: about 10 minutes 

## Techniques
- t1: **Scene inspection before building**: Prompt Claude to inspect current Blender scene first (objects, collections, rigs, bone names) to avoid clobbering existing work, then build.
- t2: **Two-stage iteration**: Build a base with plain primitives first, then prompt a second pass for materials, render engine, and detail on top of the existing scene.
- t3: **Cycles realism setup via prompt**: Ask Claude to switch to Cycles, enable denoising, pick sample count, and add PBR wet asphalt and concrete materials.
- t4: **Targeted correction prompt**: Describe the specific bad pose (palm direction) and the desired fix, and state constraints such as keep camera still, to re-run the edit.

## Quotes (brief, for attribution)
> Claude is connected. It sees what's inside of our viewport.  (at 4:33, Aidan Stanik)
> his is to the side, which this is what comes with the animation phase.  (at 12:35, Aidan Stanik)

## Points to
- claude.com/download
- blender.org official Blender MCP
- blenderstudio.org (Storm character)

## Visual notes
Frames show Claude Code terminal with /mcp listing, Blender default scene, Claude desktop chat with rendered alley, and Blender Layout workspace with outliner collections.
