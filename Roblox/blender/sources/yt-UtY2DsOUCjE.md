---
type: research-source
id: yt-UtY2DsOUCjE
title: "You Can Now Build UE 5 Games with 0$ Budget"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=UtY2DsOUCjE"
published: "2026-10-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-UtY2DsOUCjE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video (Stefan 3D AI) builds a Fall Guys-style game in Unreal Engine 5 at $0 using free AI: Gemini for concepts, Hunyuan 3D Studio for models, and OpenCode with DeepSeek 4.1 Free for Blender rigging/animation via MCP. Not about Roblox export. Little on Blender-to-Roblox, bpy, or Claude-with-Blender specifics.

## Claims
- c1: Video is about building an Unreal Engine game (Fall Guys-style) for $0 using free AI tools; it does not cover Blender-to-Roblox pipeline, bpy, or blender-mcp for Roblox. *(doc, high; other)*
- c2: [4:46] Author used OpenCode with DeepSeek 4.1 Free; it auto-found MCP connectors for Blender and Unreal Engine, and produced usable character walk/animation cycles in Blender. *(experience, medium; claude-blender-ai)*
- c3: [5:26] Author says GPT-6 Luna and Gemini 3.8 Flash gave poor rigging/animation results; DeepSeek 4.1 gave decent cyclic animations for a simple character. Opinion-level, single test. *(experience, low; rigging-animation)*
- c4: [6:47] Author reports Claude-style CLI/MCP connections are hard to use from browser chats; he preferred a CLI workspace so MCP connections are available. *(opinion, low; claude-blender-ai)*
- c5: [8:20] Early walking attempt by the AI produced a floating/sliding animation with jump but no walk cycle; it needed several re-prompts to fix. *(experience, medium; rigging-animation)*
- c6: [9:41] AI-generated ragdoll on hit and stand-up animation were judged natural; implemented in Unreal Blueprints, not Roblox. *(experience, low; rigging-animation)*
- c7: [10:21] Creating multiple OpenCode accounts to multiply free limits failed; author says limits appear tied to IP, and free usage limits reset after roughly six hours. *(experience, medium; automation-and-creator-workflows)*
- c8: [1:57] Hunyuan 3D Studio free tier offered about 20 generations; low-poly mesh with unwrap and texturing was produced; complex objects recommended to be generated in parts. *(experience, medium; mesh-texture-limits)*
- c9: [14:17] Total project: 26 3D models, $0 spend, about 7 days elapsed, ~13 million tokens per DeepSeek usage stats; author estimates 4 days if started with DeepSeek directly. *(data, medium; automation-and-creator-workflows)*
- c10: [10:49] Author says frontier models were poor at building large level layouts; level composition was placed by hand (2h39m of work), with AI supplying props and small tasks. *(experience, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Hunyuan 3D free generations**: up to 20 
- n2: **3D models created / cost**: 26 models, $0 
- n3: **Tokens used (DeepSeek)**: 13 million 
- n4: **Level build time by hand**: 2h 39m 
- n5: **Project duration**: about 7 days 
- n6: **Intelligence index**: DeepSeek 4.1 Flash 45; GPT-6 Luna 38; closest GPT 53 

## Techniques
- t1: **MCP-connected agent for Blender animation**: Run agent via CLI/workspace with Blender MCP connector; prompt for animation; re-prompt to fix walk cycle. Free model via OpenCode.

## Quotes (brief, for attribution)
> it was immediately able to find MCP connector for Blender and for Unreal Engine as well.  (at 6:47, Stefan 3D AI)
> multiple accounts and open codes, but it doesn't really work because it tracks by IP or something like that.  (at 10:21, Stefan 3D AI)

## Points to
- blender-mcp
- OpenCode
- DeepSeek 4.1
- Hunyuan 3D Studio
- Gemini
- Unreal Engine 5
- Patreon report
