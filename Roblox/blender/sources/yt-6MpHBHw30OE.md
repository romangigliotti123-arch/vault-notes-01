---
type: research-source
id: yt-6MpHBHw30OE
title: "I Reverse Engineered Mario 64 to Make My Own Game"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=6MpHBHw30OE"
published: "2026-10-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-6MpHBHw30OE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender-to-Roblox work. Video shows a Claude-driven game prototype (Super Mario 64-style platformer) built in Godot via the Reverse Engineer Anything (RIA) approach, with Blender never opened. Gives some agent-cost and asset-count figures, but no Blender, bpy, FBX/glTF, or Roblox pipeline steps. Transcript is auto-generated and garbled in places.

## Claims
- c1: [20:51] Creator states the whole prototype was built without opening Blender at all, using only Claude plus feedback. *(demo, medium; claude-blender-ai)*
- c2: [4:45] Godot chosen over Unity because it allows multiple instances and is lighter on memory when running many parallel Claude agents. *(opinion, low; other)*
- c3: [19:30] Full build took a little over two days, with about five hours of upfront brief preparation. *(experience, medium; other)*
- c4: [20:11] Asset budget was about $100 via API; creator says more assets are needed for levels two and three. *(experience, low; other)*
- c5: [20:11] Asset breakdown stated as roughly 182 models and 168 image/reference generation jobs; transcript numbers are garbled. *(data, low; other)*
- c6: [19:30] Agent usage consumed one full weekly limit on Claude Max X20 plus 20–30% more, about 130% total. *(experience, low; other)*
- c7: [21:00] Opinion: MCP-style tool bridges may become unnecessary as Claude improves at figuring out tooling itself. *(opinion, medium; claude-blender-ai)*
- c8: [0:00] RIA is described as a library that reverse engineers software binaries using tools such as Ghidra, IDA, and Hopper to recreate behavior. *(doc, medium; other)*
- c9: [1:20] Creator says game mechanics (jump values, movement) can be extracted from a binary and reused, while art assets remain copyrighted and were not copied. *(opinion, medium; other)*

## Numbers
- n1: **build duration**: just over 2 days 
- n2: **prep time**: ~5 hours 
- n3: **asset budget**: $100 
- n4: **models generated**: 182 (garbled) 
- n5: **image/reference jobs**: 168 
- n6: **Claude Max X20 weekly limit used**: ~130% of one weekly limit 

## Techniques
- t1: **Binary-to-mechanics reverse engineering with RIA**: Point RIA at a game binary, let it extract movement values (jump, double jump, long jump), then reimplement those values in a new engine. Modify values as needed for the new game.
- t2: **Benchmark reference game**: Use a known game as the mechanical reference so the agent can match feel (jump heights, controls) against it.

## Points to
- RIA (Reverse Engineer Anything)
- Ghidra
- IDA
- Hopper
- Godot
- Tripo
- Nano Banana Pro
- Seedream 5 Pro
- GPT Image 2.5
- Claude Max X20
