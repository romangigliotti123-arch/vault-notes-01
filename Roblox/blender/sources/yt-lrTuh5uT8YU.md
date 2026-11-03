---
type: research-source
id: yt-lrTuh5uT8YU
title: "I Tested GPT-6 Astra In Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=lrTuh5uT8YU"
published: "2026-09-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "other", "procedural-generation", "rigging-animation"]
---
# yt-lrTuh5uT8YU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Promotional-style video testing a GPT-6 Astra model connected to a live Blender session. Covers a cathedral scene recreated from one reference image, a rigged character backflip prompt, and a facial-animation follow-up. No Roblox export, Claude, blender-mcp setup, or bpy code is shown. Low value for the Roblox pipeline.

## Claims
- c1: [1:28] A chat AI connected to the user's open Blender session recreated a cathedral from one reference image and a single prompt; creator says output has gaps and needs human fixing. *(demo, low; claude-blender-mcp)*
- c2: [2:49] Creator says the AI used geometry nodes for the chairs, which he says saves time long term. *(opinion, low; procedural-generation)*
- c3: [3:23] Given an existing fully rigged Blender Studio character with a one-line prompt, the model analysed the rig and produced a backflip landing in a Spider-Man pose in about 2 minutes. *(demo, low; rigging-animation)*
- c4: [4:20] Model animated the facial rig (blinks, eye movement, smile) after a follow-up prompt; the first wave pass had no face motion. *(demo, low; rigging-animation)*
- c5: [0:36] Creator claims the new model outperforms Fable 5.1 on benchmarks and is cheaper; these are vendor-chart claims he did not verify. *(opinion, low; other)*

## Numbers
- n1: **generation time**: about 2 minutes 
- n2: **video length**: 5:58 

## Techniques
- t1: **Single-prompt rig animation**: Upload a fully rigged character, prompt the AI in plain language (e.g. backflip and land in a Spider-Man pose), let it analyse the rig and keyframe the viewport, then refine by hand.
- t2: **Follow-up facial pass**: After a body-only wave, prompt the AI to animate the existing face rig; it then keyed blinks, eye movement and smile.

## Quotes (brief, for attribution)
> You're never going to get a perfect output with these AI models connected to 3D softwares, and that's where the human can come in.  (at 2:49, Aidan Stanik)

## Points to
- Blender Studio storm character (rigged sample)
- GPT-6 Astra promo page (OpenAI)
- Fable 5.1 (comparison model)

## Visual notes
Contact sheet shows a Blender cathedral scene with rows of chairs, a Blender viewport with a cartoon character in a backflip-like pose, and a text panel of rig notes. The OpenAI benchmark chart is shown top-left. No Roblox or export settings appear.
