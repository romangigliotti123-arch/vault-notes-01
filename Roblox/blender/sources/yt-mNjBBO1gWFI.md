---
type: research-source
id: yt-mNjBBO1gWFI
title: "Building My Game I've Dreamed of for 15 Years with AI - From Absolute Zero"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=mNjBBO1gWFI"
published: "2026-09-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# yt-mNjBBO1gWFI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Solo dev video building an old-school RTS in Unity 6 (URP) with Claude, a custom.use MCP for generating textures and 3D parts, and Blender MCP for assembling modular castles. Nothing about Roblox Studio, FBX/glTF export, MeshPart, or Roblox limits. Only the Blender-via-agent castle assembly step touches the topic.

## Claims
- c1: [23:52] Agent used Blender MCP to drop generated castle parts into Blender; author then assembled parts into one castle in about 2 hours, with manual fixes in Blender. *(demo, medium; claude-blender-ai)*
- c2: [26:36] Author says the agent semi-automated assembly of skeleton mount variants in Blender; author did manual UV unwrap and texturing afterward. *(experience, medium; claude-blender-ai)*
- c3: [23:11] Castle parts were split by request (e.g., separate flags) so flags can change by ownership: enemy, neutral, or conquered. *(experience, medium; claude-blender-ai)*
- c4: [27:16] Author retextures meshes with Tripo (via custom.use) or Meshy, then fine-tunes in Substance-style tool Motif when more detail is needed; opinion that Motif is best AI texturing so far. *(opinion, low; mesh-texture-limits)*
- c5: [22:31] Author's project targets Unity 6 with URP, not Unreal or Roblox; the Unity MCP was chosen because agents work faster with Unity than Unreal. *(opinion, medium; other)*
- c6: [15:16] Unity URP terrain breaks with more than 8 layers (black artifacts); MicroSplat plugin adds 32-layer support, with a paid URP Unity 6 extension costing about $20. *(experience, high; other)*

## Numbers
- n1: **terrain layers**: 8 default vs 32 with MicroSplat Unity URP default terrain artifacts beyond 8 layers
- n2: **terrain textures**: 23 textures needed for first level
- n3: **castle assembly time**: about 2 hours Blender assembly of one modular castle, agent-assisted
- n4: **playtests**: 200 author says played game 200 times during balancing

## Techniques
- t1: **Agent-driven Blender assembly via Blender MCP**: Generate separate parts with an agent, send them into Blender through Blender MCP, combine into one castle, then fix textures and do manual UVs in Blender.
- t2: **Iterative regeneration with feedback**: Generate asset, review in preview canvas, tell agent what to keep or change, regenerate; keep project context in repo so the agent remembers.

## Quotes (brief, for attribution)
> My agent dropped it all in Blender because I also have Blender MCP.  (at 23:52, Stefan 3D AI)

## Contradictions flagged
- Video title and description imply a Roblox Studio pipeline, but the transcript is entirely about Unity and never mentions Roblox. (vs the source's stated topic (Blender to Roblox pipeline))

## Points to
- custom.use (MCP, Tripo, Meshy, Motif, Nano Banana Pro)
- blender MCP
- Unity MCP (Ankleshaker/ankle breaker studio)
- MicroSplat (Unity terrain plugin)
- Git for version control
