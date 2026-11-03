---
type: research-source
id: yt-7LwNSxJdlz8
title: "How To Create Insanely Realistic Renders With Claude & Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=7LwNSxJdlz8"
published: "2026-08-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows"]
---
# yt-7LwNSxJdlz8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator video on getting realistic Blender renders via Claude: organizes per-project folders with CLAUDE.md and skill MD files, uses an "agent team" skill where a director model (named Fable 5) orchestrates Opus/Sonnet/Haiku sub-agents that never run Blender code directly, and trains Claude with reference image plus tutorial video transcript. No Roblox export, import, or mesh-limit content; relevance to Roblox pipeline is low.

## Claims
- c1: [0:34] Structuring Claude Code project folders per scene (separate subfolders with blend files, reference images, MD spec files) is presented as key to good Blender output. *(opinion, medium; claude-blender-mcp)*
- c2: [2:22] Creator recommends routing only multi-step scene work through sub-agents and using cheaper models for simple checks, citing credit cost of the top model as the reason. *(opinion, medium; creator-workflows)*
- c3: [1:40] A skill file instructs the director model never to execute Blender code itself; sub-agents (Opus, Sonnet, Haiku) do the bpy work by assigned role (e.g., Opus for lighting/atmosphere, Sonnet for geometry nodes). *(demo, medium; claude-blender-mcp)*
- c4: [3:42] Creator's training method: paste a reference screenshot and a tutorial video link into Claude so it can pull the transcript and build from it. *(experience, medium; creator-workflows)*
- c5: [4:23] Creator states Claude should be treated as an assistant for a beginner; user must know Blender fundamentals first, and output quality rises as context is added. *(opinion, medium; creator-workflows)*
- c6: [6:04] Stopping a session to ask progress showed the director at 40% with two sub-agents working in parallel on camera, lights, world, compositor, and architecture. *(demo, medium; claude-blender-mcp)*
- c7: [6:45] Known issue: tile geometry was hard for Claude; creator's fix is to iterate and explain the exact problem in the session. *(experience, low; claude-blender-mcp)*

## Numbers
- n1: **sub-agent models used**: Opus, Sonnet, Haiku under a director model 
- n2: **build progress at stop**: 40% 
- n3: **video length**: 7:23 

## Techniques
- t1: **Director/sub-agent split**: Director model plans via step-by-step spec MD; assigns Opus/Sonnet/Haiku sub-agents roles (lighting, geometry); sub-agents run Blender actions in parallel.
- t2: **Reference-driven prompting**: Paste reference screenshot and tutorial video URL; ask Claude to download and transcribe the video, then build the scene matching it.

## Quotes (brief, for attribution)
> Fable 5 will never execute any code inside of Blender. It'll utilize Opus, Sonnet, and Haiku as sub-agents.  (at 1:40, Aidan Stanik)

## Points to
- Creator's free school community (project template folder with two agent-team skills)
