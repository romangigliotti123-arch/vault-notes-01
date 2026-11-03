---
type: research-source
id: yt-o1JpFV-8dF4
title: "I Tested Destruction Effects In Blender With GPT-6 Astra"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=o1JpFV-8dF4"
published: "2026-09-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "other", "procedural-generation"]
---
# yt-o1JpFV-8dF4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video by Aidan Stanik tests GPT-6 Astra driving Blender via computer use (no plugins) on five physics scenes: wrecking ball collision, cloth wind (silk/cotton/canvas), baked water gate release, fireball/smoke chamber, concrete destruction with dust/fire, and jelly drop. Shows prompt-driven scene building and baking, not Roblox export. Relevance to Roblox pipeline is low.

## Claims
- c1: [1:08] Model drove Blender via computer use with no plugins or add-ons; wrecking-ball collision scene worked from a single prompt. *(demo, medium; claude-blender-mcp)*
- c2: [2:19] Cloth wind test with silk, cotton, canvas produced visibly different wrap behaviour around metal spheres at same wind speed; single prompt, no iteration. *(demo, medium; procedural-generation)*
- c3: [3:26] Water simulation was baked before final render; author says baking makes renders faster and viewport playback possible. *(demo, medium; creator-workflows)*
- c4: [5:52] Fireball/smoke test: explosion baked and rendered, but smoke dissipated too fast to show wrapping around the flow obstacle; author judged this a weak case. *(demo, medium; procedural-generation)*
- c5: [7:08] Concrete destruction output split concrete blocks into four separate sections, looking unnatural; author plans to iterate. *(demo, medium; creator-workflows)*
- c6: [8:30] Author says the explosion scene took two prompts and that human creative direction is still needed (opinion). *(opinion, low; creator-workflows)*
- c7: [8:35] Jelly drop test with soft/medium/firm blocks showed almost no visible difference in deformation; model missed intent. *(demo, medium; procedural-generation)*
- c8: [3:26] Author says a Fable 5.1 water test was very similar in quality to GPT-6 Astra output. *(opinion, low; other)*

## Numbers
- n1: **physics tests run**: 5 
- n2: **cloth materials compared**: 3 (silk, cotton, canvas) 
- n3: **water render resolution**: 720p 
- n4: **concrete block sections**: 4 
- n5: **prompts for explosion sim**: 2 

## Techniques
- t1: **Bake simulation before render**: Run fluid/fire/smoke sim in Blender, bake to static cache, then render; author says this speeds renders and enables viewport playback.
- t2: **Material preview instead of Rendered viewport**: Use Material Preview for checking cloth/water motion; Rendered viewport was glitchy and grainy for the author.

## Quotes (brief, for attribution)
> absolutely no plugins or additional knowledge, just using GPT-6 Astra and its computer use inside of Blender  (at 0:42, Aidan Stanik)
> it definitely did not pick up on like exactly what I was going for  (at 8:35, Aidan Stanik)

## Points to
- Fable 5.1 (prior video by author)
