---
type: research-source
id: yt-2M1TEH6JPKc
title: "Claude Opus 5.5 Is the New KING of 3D Design & Blender"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=2M1TEH6JPKc"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "other", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# yt-2M1TEH6JPKc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Opinion-driven comparison of Claude Opus 5.5 vs GPT-6 Astra generating Blender scenes via an MCP plugin: DeLorean scene, Notre Dame, galleon, VFX, UV unwrapping, creature and Lego animation, castle, and a playable HTML game. No Roblox export or bpy scripting details. Both models were run with the same prompts, and the times and costs were self-reported.

## Claims
- c1: [0:00] Creator gave Claude and GPT Blender access and all APIs; Opus 5.5 built the DeLorean scene without side APIs, mostly procedurally, with only some images from Nano Banana Pro. *(demo, medium; claude-blender-mcp)*
- c2: [0:40] DeLorean scene runs took about 1.5 hours each and cost about $25 each. *(data, medium; creator-workflows)*
- c3: [2:13] Notre Dame: GPT-6 took 42 min vs Opus 5.5 at 96 min; creator found the outputs roughly equal in quality. *(demo, medium; procedural-generation)*
- c4: [5:28] Pirate galleon, fully procedural: both took about one hour; GPT-6 cost about half as much; GPT-6 judged more impressive. *(demo, medium; procedural-generation)*
- c5: [6:21] VFX test (magic circle, leaves, ice shards, shaders): both took about 30 min with low token use; Opus preferred for the intro/magic circle, GPT-6 for fireballs. *(opinion, low; other)*
- c6: [8:24] UV unwrap test on cape, boots, bag: GPT-6 failed (poor islands, unused UV space); Opus 5.5 kept objects split and was somewhat better but still left many small islands and wasted space. Took about 20 min and $10 each. *(demo, medium; texturing-baking-uv)*
- c7: [8:24] Creator says the 3D models were generated through the Blender MCP plugin, which exposes MCP tools to the agent and is free to use. *(doc, low; texturing-baking-uv)*
- c8: [10:31] Creature animation: GPT-6 walk ok, jump failed; Opus 5.5 walk in place (a bit harsh), jump in place better, attack better. Times: Opus 46 min, GPT-6 63 min. *(demo, medium; rigging-animation)*
- c9: [12:33] Lego humanoid walk and attack from a reference model: Opus slightly better; neither was especially funny. *(opinion, low; rigging-animation)*
- c10: [13:15] Procedural castle with channel name shown on screen: GPT-6 judged the more dynamic render with fireworks; Opus had more detailed time-lapse per creator. *(opinion, low; procedural-generation)*
- c11: [14:15] Single-file playable HTML 3D game from one prompt: Opus output was more fun and playable; GPT-6 output felt boring and stuttery. Opus took about 3x time and cost. *(demo, medium; creator-workflows)*

## Numbers
- n1: **DeLorean scene run cost**: ~$25 each, ~1.5 h 
- n2: **Notre Dame build time**: GPT-6 42 min vs Opus 5.5 96 min 
- n3: **Galleon build time**: ~1 h each; GPT-6 cost ~2x less 
- n4: **UV unwrap test cost/time**: ~20 min, ~$10 each 
- n5: **Creature animation time**: Opus 46 min, GPT-6 63 min 
- n6: **Playable game cost/time**: Opus ~3x time and ~3x cost vs GPT-6 

## Techniques
- t1: **Agent drives Blender via MCP with full Blender access**: Give the model Blender access plus APIs, prompt for a scene, let it build procedurally with minimal image generation. Creator reports this as the approach he prefers.
- t2: **UV unwrap check by visual review**: Generate models, ask the agent to unwrap, then inspect islands in the UV editor for split objects, small islands and unused space. Creator reports both models failed packing.

## Contradictions flagged
- Creator says Opus 5.5 is 'the new KING of 3D design' and wins on artistic work. (vs Creator's own tests show GPT-6 winning the galleon, castle, and UV tests on quality or cost; results mixed.)
- Creator says Claude lacks vision strength compared with GPT. (vs Opus 5.5 handled the UV-split test better than GPT-6 in the same video; creator's claim is opinion only.)

## Points to
- Blender MCP plugin (name garbled in transcript)
- Nano Banana Pro (image generation used in DeLorean scene)
- Claude Opus 5.5
- GPT-6 Astra
