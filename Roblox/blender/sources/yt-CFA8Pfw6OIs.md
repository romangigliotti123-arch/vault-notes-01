---
type: research-source
id: yt-CFA8Pfw6OIs
title: "You Can Now Create Modular 3D Character Without Blender"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=CFA8Pfw6OIs"
published: "2026-10-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0039
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "avatar-ugc-accessories", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# yt-CFA8Pfw6OIs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video demos Part Composer (AI modular character assembly via CLI/MCP, Tripo P2/3.1 parts, GPT-6 Astra) and says Blender cleanup is still needed. Targets Unity, not Roblox; no Roblox import, scale, or Studio steps. Mostly opinion and unverified claims.

## Claims
- c1: [0:00] Creator says AI-only modular character creation (no Blender) is now feasible via Part Composer tool with GPT-6 Astra; raw GPT-6 or Opus 5.5 'not even close' per his own test. *(opinion, low; claude-blender-ai)*
- c2: [1:30] Part Composer offers CLI and MCP, so the whole pipeline can be run from an agent like Claude Code, using one API key for image and 3D generation. *(doc, medium; automation-and-creator-workflows)*
- c3: [2:50] Part generation selects Tripo P2 (most recent) and a part count; generation can take up to 30 minutes; a simple character yielded body, head, top and bottom parts. *(demo, medium; automation-and-creator-workflows)*
- c4: [3:31] First assembly from Part Composer had visible artifacts; a second attempt with Tripo 3.1 gave better image adherence, while P2 had better wireframe. *(demo, medium; mesh-texture-limits)*
- c5: [4:52] Setup: tell agent to install the Part Composer CLI/MCP and store the API key in an environment variable so the agent can access it. *(demo, medium; automation-and-creator-workflows)*
- c6: [5:10] Prompt specified a per-part triangle limit of no more than 5000 faces for the simple character. *(demo, medium; mesh-texture-limits)*
- c7: [6:31] Pipeline outputs a report showing each iteration; the simple character still needed small Blender fixes. *(demo, medium; claude-blender-ai)*
- c8: [7:00] For modular sets such as armor, separate parts can be requested in the prompt to produce interchangeable pieces; complex characters were the hardest case. *(opinion, medium; avatar-ugc-accessories)*
- c9: [8:21] Creator recommends cutting always-hidden geometry (e.g. chest under top wear) in Blender for optimized mobile games; fixes take about five minutes in sculpting. *(experience, medium; mesh-texture-limits)*
- c10: [9:00] AI-assembled characters still need manual alignment and scaling in Blender; creator calls it not a complete replacement but a time saver. *(opinion, medium; claude-blender-ai)*
- c11: [10:21] Tripo P2 produces better UVs; creator asks GPT-6 or Opus 5.5 to process maps, then GPT-6 Astra for animations using video references. *(experience, low; rigging-animation)*
- c12: [11:20] Animations and VFX were produced by Claude from text descriptions and references; pose-at-frame feedback improves movement, per creator. *(experience, low; rigging-animation)*
- c13: [14:05] Modular parts can be color-tinted (enemy vs neutral) via marked color-able parts. *(demo, low; avatar-ugc-accessories)*

## Numbers
- n1: **per-part face limit**: <=5000 
- n2: **generation time**: up to 30 minutes 
- n3: **manual cleanup time**: about 5 minutes 

## Techniques
- t1: **Agent-driven Part Composer pipeline**: Install Part Composer CLI/MCP via agent, set API key in environment variable, prompt model, part count and face limit, then review preview and report in Blender.
- t2: **Hidden-geometry removal**: In Blender, delete parts of the mesh hidden under outer garments (e.g. chest under top) to cut triangles for mobile builds.

## Quotes (brief, for attribution)
> even this for complex characters will require some additional manual work to align parts together nicely before we actually put it into the game  (at 9:00, Stefan 3D AI)

## Contradictions flagged
- Blender can be dropped from the pipeline (vs Creator's own statements that AI assemblies still need Blender fixes for scale, artifacts, and alignment)

## Points to
- Part Composer
- Tripo
- Mr. Mark workspace
- Part Decomposer
