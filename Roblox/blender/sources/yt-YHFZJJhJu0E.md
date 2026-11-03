---
type: research-source
id: yt-YHFZJJhJu0E
title: "I Tested Claude Fable 5.1 In Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=YHFZJJhJu0E"
published: "2026-09-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other", "procedural-generation", "texturing-baking-uv"]
---
# yt-YHFZJJhJu0E

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Showcase of Claude 'Fable 5.1' driving Blender via agent-team prompts: cathedral, physics wrecking ball, cyberpunk city, studio lighting. Creator reviews benchmark charts and visible flaws (spacing, floating objects, weak textures). No blender-mcp setup, bpy code, Roblox export, or Roblox import content.

## Claims
- c1: [0:00] Video is a general Claude-in-Blender showcase; no Roblox export, Roblox import, or Roblox pipeline content is discussed. *(doc, high; claude-blender-mcp)*
- c2: [3:39] Creator says Claude built a full cathedral scene from one reference image using a team of agents executed inside Blender. *(experience, low; claude-blender-mcp)*
- c3: [4:20] Generated scene had spacing errors and floating candlesticks; creator deleted the floaters manually and suggests re-prompting for spacing. *(experience, medium; common-mistakes-fixes)*
- c4: [4:20] Claude-generated textures were described as messy; chairs showed no texture and needed further prompting. *(experience, medium; texturing-baking-uv)*
- c5: [6:28] Claude applied geometry nodes to create arches, pillars and tiles in the cathedral scene; creator says arches can be shade-smoothed. *(experience, medium; procedural-generation)*
- c6: [6:28] Physics test: Claude-built wrecking ball scene where the ball floated, suggesting missing gravity/rigid body setup. *(experience, medium; other)*
- c7: [7:20] Single prompt produced a wet cyberpunk night street scene with reflections and grunge; creator judged it good for one prompt. *(experience, low; procedural-generation)*
- c8: [8:04] Creator suggests studio lighting scenes for product showcase renders from user's own models; opinion, not tested on Roblox. *(opinion, low; creator-workflows)*
- c9: [1:06] Creator reads Anthropic's published chart as showing Fable 5.1 cheaper and more accurate than Fable 5 on benchmarks; benchmark claims are vendor-reported, not verified here. *(doc, medium; other)*
- c10: [2:18] Creator's reasoning that Blender being Python-based lets Claude iterate cleaner is opinion, not a measured result. *(opinion, low; claude-blender-mcp)*

## Numbers
- n1: **Agentic coding gain (Fable 5.1 vs Fable 5)**: over 10%, per creator's reading of chart 
- n2: **Terminal-Bench-Science 0.1 (Fable 5.1 high)**: 52.6% accuracy at ~$30 mean cost (approx from chart) 
- n3: **Video length**: 9:49 

## Points to
- Creative AI Network (creator's free school community, promotional)

## Visual notes
Contact sheet shows Anthropic benchmark tables (Fable 5.1 vs Fable 5, Opus 5, GPT-5.6) and Blender viewports of cathedral, physics and arrays of boxes; no Roblox content visible.
