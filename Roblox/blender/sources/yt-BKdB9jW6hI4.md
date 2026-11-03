---
type: research-source
id: yt-BKdB9jW6hI4
title: "I Tested GPT-6 Sol In Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=BKdB9jW6hI4"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other", "rigging-animation"]
---
# yt-BKdB9jW6hI4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator tests GPT-6 Soul (OpenAI) driving Blender via prompts across five scenes: radio, kitchen, marble-machine simulation, penguin rig, geometry-nodes forest. Gives self-rated quality and per-scene token/API cost. No Roblox export, Claude, blender-mcp, or bpy code shown. Little relevance to the Roblox pipeline.

## Claims
- c1: [2:22] GPT-6 Soul one-prompt radio model scored 4/10 by creator; missing speaker mesh, volume knobs, paint colors off; needed manual fixes. *(demo, medium; claude-blender-ai)*
- c2: [3:51] Kitchen scene from GPT-6 Soul rated 5-6/10; cabinets misplaced and a mat clipped into the marble tabletop. *(demo, medium; claude-blender-ai)*
- c3: [4:53] Marble machine keyframed rigid-body-style simulation built from prompt without asking for physics; floating objects; rated 6/10. *(demo, medium; claude-blender-ai)*
- c4: [6:11] Penguin: model produced only partial rig (limbs, core body) with no full armature in one prompt; creator says basic and not client-ready. *(demo, medium; rigging-animation)*
- c5: [7:10] Forest scene used geometry nodes for tree/rock/grass scattering with adjustable density, seed and trail; rated 7/10. *(demo, medium; claude-blender-ai)*
- c6: [8:01] Five-scene total: 19M tokens, $5.71 API cost (creator says subscription used, not API). *(data, low; claude-blender-ai)*
- c7: [8:41] Radio about 800k tokens for $0.33; kitchen 1.4M tokens for $0.53. *(data, medium; claude-blender-ai)*
- c8: [8:41] Marble machine 6M tokens for $1.86; penguin about 7M tokens for $1.96; forest about 3M tokens for $1.04. *(data, medium; claude-blender-ai)*
- c9: [0:41] Creator cites GPT-6 Soul API pricing of about $2 input and $10 output, roughly 50% cheaper than GPT-5.6 Soul. *(doc, low; claude-blender-ai)*
- c10: [8:01] Creator opinion: GPT-6 Soul is much cheaper than Opus 5.5 for Blender builds, though tests differed in intensity. *(opinion, low; claude-blender-ai)*
- c11: [2:02] Creator says Blender's Python backend lets the model use computer-use style control of the UI and scripts; claim is opinion, not tested here. *(opinion, low; claude-blender-ai)*
- c12: [9:12] Creator sells a Blender AI starter pack of skills/context files for Anthropic or GPT models, delivered via a paid community; promotional. *(opinion, low; other)*

## Numbers
- n1: **Radio tokens / cost**: ~800k / $0.33 single prompt build, creator subscription
- n2: **Kitchen tokens / cost**: ~1.4M / $0.53 scene build
- n3: **Marble machine tokens / cost**: ~6M / $1.86 simulation build
- n4: **Penguin tokens / cost**: ~7M / $1.96 includes small revision
- n5: **Forest tokens / cost**: ~3M / $1.04 includes small revision
- n6: **Total tokens / cost**: ~19M / $5.71 five scenes; per-scene tokens sum to ~18.2M
- n7: **API price**: ~$2 input / $10 output stated; about 50% cheaper than GPT-5.6 Soul
- n8: **Self-rated quality**: radio 4/10, kitchen 5-6/10, marble 6/10, forest 7/10 creator opinion

## Techniques
- t1: **Single-prompt scene generation with minimal iteration**: Send one structured prompt describing the Blender scene; review output; apply one small revision; track tokens and API cost per build.
- t2: **Geometry nodes scattering for environments**: Model applied geometry nodes to trees, rocks, grass and leaves; control density, random seed and trail width to adjust without deleting objects.
- t3: **Keyframed physics-like animation via prompt**: Prompt describes a mechanical sequence; model keyframes objects and a rigid-body-like roll; loop check by playback.

## Quotes (brief, for attribution)
> I didn't spend this money personally. I run everything on my subscription plan.  (at 8:41, Aidan Stanik)
> GPT-6 Soul was able to output this for us. So, I'd give this again maybe a seven out of 10  (at 7:50, Aidan Stanik)

## Contradictions flagged
- Total of about 19M tokens across five scenes (vs Per-scene token figures (0.8M+1.4M+6M+7M+3M) sum to about 18.2M)
- Creator reports API cost ($5.71) for the builds (vs Same creator says builds ran on a subscription plan, not API billing)

## Points to
- openai.com (GPT-6 Soul and Luna announcement)
- BlenderKit (asset library suggestion)
- Creative AI Network (creator community, Blender AI Starter Pack)
