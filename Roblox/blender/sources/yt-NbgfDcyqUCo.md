---
type: research-source
id: yt-NbgfDcyqUCo
title: "I NEED THIS ROBLOX GAME TO MAKE MONEY"
source_type: "youtube"
creator: "SmartyRBX"
url: "https://www.youtube.com/watch?v=NbgfDcyqUCo"
published: "2026-09-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.1330
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# yt-NbgfDcyqUCo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Livestream of a Roblox dev building "Lift and Flex for Baddies" in Roblox Studio with AI coding agents (Claude, Codex, GPT-based models, Roblox's built-in assistant). Blender, bpy, FBX/glTF export, mesh import and blender-mcp are never discussed. Only tangential items: a Studio MCP tool that the speaker reports as unreliable, a ViewportFrame preview technique, and AI-agent cost and reliability opinions.

## Claims
- c1: [3:57] Speaker says the MCP tool used to drive Roblox Studio is failing ('MCP board'), and that agents may invent bugs or misreport fixes when asked to repair a tool. *(experience, low; claude-blender-ai)*
- c2: [5:54] Speaker cannot afford Substance Painter and suggests an MCP wrapper for it; claims AI can generate textures. Unverified, no workflow shown. *(opinion, low; mesh-texture-limits)*
- c3: [7:03] Technique: put a 3D model clone inside a ViewportFrame at the same position, then set the ViewportFrame CurrentCamera to the player's camera so the 3D object lines up with the world view. Shown in Studio, no code. *(demo, medium; other)*
- c4: [6:10] Roblox Studio's built-in assistant was reported as running GLM 5.2 (unconfirmed). Speaker judges it weaker than frontier models on single-property edits, though it made acceptable billboard UI in one test. *(experience, low; claude-blender-ai)*
- c5: [4:14] Speaker pays about $400/month for two $200/month AI subscriptions (OpenAI and Anthropic) for coding agents during development. *(experience, medium; automation-and-creator-workflows)*
- c6: [6:08] Opinion: AI models handle big multi-file code tasks well but fail at small, specific property changes (e.g. swapping an image icon), and repeatedly ignore parts of multi-step prompts. *(opinion, medium; claude-blender-ai)*

## Numbers
- n1: **AI subscription spend**: $400/month (2 x $200) 

## Techniques
- t1: **ViewportFrame 3D preview**: Clone the 3D object into a ViewportFrame at its world position. Set the ViewportFrame CurrentCamera to the player's camera. Set background transparency to show the model in UI.

## Quotes (brief, for attribution)
> AI agents can't always be trusted to fix a tool because they might just invent bugs and make it up.  (at 3:57, SmartyRBX)
> Astra shines in Substance Painter. Make an MCP for that.  (at 5:54, SmartyRBX)
