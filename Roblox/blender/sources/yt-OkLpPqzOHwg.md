---
type: research-source
id: yt-OkLpPqzOHwg
title: "ChatGPT 4o: Now ANYONE can literally code a Roblox game for Free"
source_type: "youtube"
creator: "Bluesteel"
url: "https://www.youtube.com/watch?v=OkLpPqzOHwg"
published: "2024-05-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 0
density: low
tags: ["research-source", "youtube", "common-mistakes-fixes", "other"]
---
# yt-OkLpPqzOHwg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender. A creator tests free ChatGPT-4o to write Roblox Lua: a double-jump script, a raycast gun script, and a round system with intermission, teleports and leaderstats. No Blender, bpy, MCP, export or asset-pipeline content. Only tangential lessons: AI-written scripts worked first try for simple mechanics; the gun failed because it ran as a LocalScript, so effects were client-only; DataStore needed API services enabled.

## Claims
- c1: [0:00] ChatGPT-4o produced a working double-jump LocalScript in one prompt; jump power is an adjustable value in the script. *(demo, high; other)*
- c2: [3:29] AI-generated gun script placed in a LocalScript made kills and effects happen only on the shooting client, not the server; the fix was server-side logic. *(demo, medium; common-mistakes-fixes)*
- c3: [5:20] DataStore leaderstats failed until the creator enabled API services for the game; the creator suspected this was the cause. *(demo, low; common-mistakes-fixes)*
- c4: [2:47] A full round system (lobby/battle spawns, leaderstats, intermission) generated in one prompt needed several follow-up fixes before it worked. *(demo, medium; other)*

## Techniques
- t1: **Prompting for scripts in steps**: Ask the LLM for complex systems in stages (first one feature, then the next) to avoid confusion; the creator tried a single large prompt instead, with mixed results.
