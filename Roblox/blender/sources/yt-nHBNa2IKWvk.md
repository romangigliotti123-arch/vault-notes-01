---
type: research-source
id: yt-nHBNa2IKWvk
title: "You're Using GPT-6 Astra Wrong - This Setup Is Insane"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=nHBNa2IKWvk"
published: "2026-09-10"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other", "rigging-animation"]
---
# yt-nHBNa2IKWvk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GPT-6 (not Claude) setup video. Uses Codex CLI in YOLO mode, Unity MCP, a Blender MCP plus Hicksfield Blender add-on, and Godot/Unreal MCPs to build games. Blender content is brief: install the add-on via preferences, MCP drives Blender through tools. No Roblox, bpy scripting, or export pipeline coverage.

## Claims
- c1: [5:40] Blender Hicksfield add-on is installed via Edit > Preferences > Add-ons > Install from Disk using a zip, then activated; Blender native MCP must be kept running. *(demo, medium; claude-blender-ai)*
- c2: [6:20] Author says MCP tool calls to Blender are much faster and cheaper than computer-use screen control, which he calls slow and token-burning. Opinion, no measurements. *(opinion, low; claude-blender-ai)*
- c3: [9:02] Agent given a non-humanoid mesh (horse-like quadruped) via Blender plugin built a custom skeleton and a simple tail animation; author says weights were imperfect. *(demo, low; rigging-animation)*
- c4: [2:35] Codex CLI launched with dangerously-bypass-approvals flag runs without per-step confirmation; author reports no issues in his tests. *(experience, low; automation-and-creator-workflows)*
- c5: [2:35] Unity run took about 2.5 hours and 30M tokens, which the author estimates at $46 via API; it used 7% of his weekly plan limit. *(experience, low; other)*
- c6: [12:12] Agent produced a Blender file with a rigged Pickle Rick model and a separate asset-storage .blend; author notes the model was not accurate. *(demo, low; claude-blender-ai)*

## Numbers
- n1: **Unity project run duration and tokens**: 2h30m, 30M tokens 
- n2: **Trials game run duration and tokens**: 2h17m, 17M tokens 
- n3: **Weekly plan usage consumed**: 7% (Pro Max plan) 

## Techniques
- t1: **Blender add-on install from zip**: Blender > Edit > Preferences > Add-ons > Install from Disk, pick zip, enable add-on. Keep MCP server running; it can stop unexpectedly.
- t2: **Mid-run follow-up prompts**: In Codex CLI, send additional prompts while a long task is still running to steer it and check progress.

## Quotes (brief, for attribution)
> with MCP you're gonna do the same thing like so much faster and it's so much fun.  (at 6:20, Stefan 3D AI)

## Points to
- Codex CLI
- Unity MCP Server (Ankle Breaker Studio)
- Hicksfield Blender plugin / MCP
- Godot MCP (coding-solo)
- VibeUE (Unreal)
- Fal/fullAI MCP
