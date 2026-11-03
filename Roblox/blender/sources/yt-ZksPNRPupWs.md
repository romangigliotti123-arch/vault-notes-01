---
type: research-source
id: yt-ZksPNRPupWs
title: "AI Can Now Create VFX Fro YouR Game & Characters"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=ZksPNRPupWs"
published: "2026-09-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "mesh-texture-limits", "other", "rigging-animation"]
---
# yt-ZksPNRPupWs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Game-dev VFX video (not Blender/Roblox-specific). Creator uses GPT/Claude for 2D VFX concepts, Tripo for mesh generation, Nano Banana Pro for leaf textures, manual paint for fixes, and GPT for rigging and animation. Tools like blender-mcp, bpy, FBX export, and Roblox import are not covered.

## Claims
- c1: [0:00] Video is about making game VFX and animated characters with GPT/Claude and Tripo; it does not use blender-mcp, bpy, or the Roblox Blender export pipeline. *(doc, high; other)*
- c2: [9:35] Creator says AI texturing can fail on important details, so manual painting in Mudbox-style paint tool (named Moondiff in transcript) was used for fixes. *(experience, low; mesh-texture-limits)*
- c3: [7:56] Tripo now generates four meshes at once; creator sets different poly counts per generation and picks the best result. *(experience, medium; other)*
- c4: [8:37] Creator unwraps with smart UV so AI can later do color correction on the color map; clear UV layout is said to matter for later edits. *(opinion, medium; mesh-texture-limits)*
- c5: [10:16] Leaves are kept as separate planar objects with transparency and separate material so they can be animated by wind and recolored, not joined to the body. *(experience, medium; mesh-texture-limits)*
- c6: [11:36] Humanoid top half rigged via Mixamo or AccuRig, or a simple skeleton with automatic weight transfer; bottom half skipped and rigged by GPT. *(experience, medium; rigging-animation)*
- c7: [12:35] Creator states that video AI tools (Kling, MiniMax) could not animate root movement, while GPT produced it better when given the rig as-is. *(experience, medium; rigging-animation)*
- c8: [14:39] AI-built small plugin lets creator click set pose at a timeframe to give precise feedback on custom animations. *(experience, low; rigging-animation)*
- c9: [4:41] Concept-first workflow: generate 2D interactive concepts before implementation, judged as saving time versus iterating in-game. *(opinion, medium; other)*
- c10: [5:00] Giving the agent a visual reference link plus a description of changes is recommended over copying references. *(opinion, low; other)*
- c11: [15:31] Final VFX concept sheets were 2D visuals with timing breakdowns, iterated two to three times before handing to GPT for implementation. *(experience, medium; automation-and-creator-workflows)*
- c12: [16:55] Creator says one and a half day total to build the character's VFX and abilities in the game. *(experience, low; other)*
- c13: [18:54] Skills and workspace setup are stored in a Git repo and reused daily as Claude/agent skills. *(experience, low; automation-and-creator-workflows)*

## Numbers
- n1: **Tripo mesh generations per run**: 4 
- n2: **Course student count (promo, creator claim)**: 100+ 
- n3: **Time to build character VFX and abilities**: ~1.5 days 
- n4: **Guard trigger threshold (in-game)**: 5+ surrounding units 

## Techniques
- t1: **Concept-first VFX**: Generate 2D interactive concepts with GPT/Claude, iterate timings and look, then give implementation to a second agent.
- t2: **Separate foliage planes**: Keep leaves as separate transparent planes with own material so they can be wind-animated and recolored.

## Quotes (brief, for attribution)
> Concepting first: before you implement it into the game, you need to actually understand what do you want.  (at 4:41, Stefan 3D AI)
> I found some nice casting animation from Mik Samo... and reuse part of them.  (at 12:35, Stefan 3D AI)

## Points to
- Stefan 3D AI channel (creator) workspace on Git
- Tripo (AI 3D mesh generation)
- Mixamo
- AccuRig
- Nano Banana Pro (texture generation)
- Kling
- MiniMax
- Jean Moreno cartoon effects (VFX reference library)
