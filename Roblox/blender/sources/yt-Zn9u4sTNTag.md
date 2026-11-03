---
type: research-source
id: yt-Zn9u4sTNTag
title: "Get a sneak peek at Bungie co-founder's new Roblox game"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=Zn9u4sTNTag"
published: "2026-09-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0034
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai"]
---
# yt-Zn9u4sTNTag

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creators interview with Alex (Bungie co-founder) about his Roblox extraction shooter Drifters. Almost no Blender content. Useful only as anecdotes: Studio has out-of-box MCP connectivity; an AI-driven asset script (audio processing, cloud upload, permissions) cut a 1-2 hour task to 15 seconds; Git asset sync for Studio content relies on custom scripts. No bpy, blender-mcp, FBX/glTF or Blender-to-Roblox pipeline details.

## Claims
- c1: [13:48] Roblox Studio supports MCP connectivity out of the box, which the speaker uses to automate Studio edits. *(experience, medium; automation-and-creator-workflows)*
- c2: [14:28] A scripted AI-assisted flow (process audio, upload to cloud, set permissions, return asset ID) reportedly takes 15 seconds versus 1-2 hours manually. *(experience, low; automation-and-creator-workflows)*
- c3: [10:27] A leaderboard feature was reportedly built in about an hour with AI coding help versus 4-5 days previously; speaker was new to Roblox leaderboards. *(experience, low; automation-and-creator-workflows)*
- c4: [16:30] Custom weapon systems (recoil, muzzle flash, tracers, casings) were stood up in about five weeks instead of a much longer custom-code effort; Roblox lacks a full weapon stack. *(experience, low; automation-and-creator-workflows)*
- c5: [18:22] Artist-created assets made in Studio's cloud place must be pulled out with custom scripts into GitHub; the team calls this fragile and wants engine-backed automatic sync. *(experience, medium; automation-and-creator-workflows)*
- c6: [19:03] Team of about 10-12 people on the project; code uses Git via a third-party plugin, while Studio asset sync needs manual scripts. *(experience, medium; automation-and-creator-workflows)*
- c7: [9:47] AI coding assistants (Claude, Codex) are used to read existing game code, add profile fields and wire up services; speaker says engineers no longer write code by hand. *(opinion, low; claude-blender-ai)*
- c8: [5:41] Using AI to batch-rename about 1,200 assets' attributes to a naming convention is cited as a clear use case for Claude. *(opinion, low; claude-blender-ai)*

## Numbers
- n1: **asset pipeline task time**: 1-2 hours manual vs 15 seconds scripted 
- n2: **leaderboard feature time**: 4-5 days before vs about 1 hour with AI 
- n3: **weapon system prototype time**: about 5 weeks (vs 18 months cited) 
- n4: **assets needing rename**: 1,200 
- n5: **project team size**: 10-12 people incl. contractors 

## Techniques
- t1: **Studio MCP scripted asset pipeline**: Connect Studio via MCP, script audio processing and cloud upload, set permissions, then wire returned asset ID back into the flow. Speaker reports 15-second turnaround.

## Quotes (brief, for attribution)
> studio does just out of the box now allow MCP connectivity  (at 13:48, Roblox Creators)
> it's just a lot of parts, a lot of steps, kind of fragile  (at 19:03, Roblox Creators)

## Points to
- Left 4 Dead GDC AI director white paper (mentioned as research reference)
- GitHub (source of truth for project assets)
