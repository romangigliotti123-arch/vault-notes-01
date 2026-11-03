---
type: research-source
id: yt-wbEjHXSrG0Q
title: "What Every Roblox Dev Gets Wrong About AI"
source_type: "youtube"
creator: "SmartyRBX"
url: "https://www.youtube.com/watch?v=wbEjHXSrG0Q"
published: "2025-12-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai"]
---
# yt-wbEjHXSrG0Q

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video argues Roblox devs using AI should keep control: plan with AI, treat generated scripts as drafts, test each in Studio, and feed full code and dependency context. Nothing on Blender, blender-mcp, bpy, or the Blender-to-Roblox pipeline, so relevance is minimal.

## Claims
- c1: Source does not mention Blender, bpy, blender-mcp, or Claude-with-Blender workflows at all. *(doc, high; claude-blender-ai)*
- c2: Source does not cover FBX/glTF export, scale, axes, MeshPart import, or the Roblox Blender plugin. *(doc, high; blender-roblox-export-import)*
- c3: [2:14] Author's opinion: AI confidently breaks parts of a game when it lacks understanding of the whole codebase, so context matters more than clever prompts. *(opinion, medium; automation-and-creator-workflows)*
- c4: [1:43] Author says the biggest AI failure mode is incorrect logic or forgotten dependencies, not hallucinated Roblox APIs, which he says AI now knows well. *(opinion, medium; automation-and-creator-workflows)*
- c5: [2:37] Author pastes full scripts, reminds AI of dependencies, and describes explorer structure in each chat rather than relying on chat memory. *(experience, medium; automation-and-creator-workflows)*
- c6: [1:13] Author treats AI script output as a rough draft and tests every script in-game for iteration and correction. *(experience, medium; automation-and-creator-workflows)*
- c7: [3:36] Author says he tests all AI output unless it is very small and he understands it well enough to judge it. *(experience, medium; automation-and-creator-workflows)*

## Techniques
- t1: **Explicit context pasting**: Paste full current scripts into the AI chat, state cross-script dependencies, describe Explorer hierarchy and remote locations, and re-notify AI of manual changes.
- t2: **Iterative test loop**: Treat AI output as scaffolding; run each script in Studio, observe results, then correct and iterate.

## Quotes (brief, for attribution)
> AI output, it's like a rough draft of an essay.  (at 1:13, SmartyRBX)
> If AI doesn't understand your entire game and all of the important code in it, it will confidently break part of it.  (at 2:14, SmartyRBX)

## Points to
- SmartyRBX Scripting Secrets course (promotional, skipped)
