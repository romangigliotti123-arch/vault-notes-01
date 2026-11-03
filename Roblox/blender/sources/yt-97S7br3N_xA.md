---
type: research-source
id: yt-97S7br3N_xA
title: "I applied 1000 color palettes in 10 minutes with Blender Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=97S7br3N_xA"
published: "2024-01-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-97S7br3N_xA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender-to-Roblox and Claude/MCP. Shows a bpy script that randomizes Principal BSDF base colors and color ramp elements from a JSON palette list, renders EEVEE previews per palette, then re-runs one chosen palette/seed in Cycles. Uses the Info panel to copy UI-generated bpy code. No Roblox, MCP, or Claude content.

## Claims
- c1: [2:43] Workflow: keep a Blender Python script in the Text Editor, open the Info panel, and copy the auto-generated bpy code after each UI change to reuse it in the script. *(demo, high; claude-blender-ai)*
- c2: [8:52] Excluding already-used colors with a retry loop hangs Blender if the palette has too few colors; the speaker says to keep enough colors in the palette. *(experience, high; claude-blender-ai)*
- c3: [13:08] Batch generation freezes the Blender UI; progress is only visible by watching the output folder for images. *(demo, high; claude-blender-ai)*
- c4: [13:50] A chosen variation is reproduced by setting palette index and seed in main(), then rendering that single variation in Cycles to match the EEVEE preview. *(demo, medium; claude-blender-ai)*
- c5: [5:13] Principal BSDF base color is set via node.inputs['Base Color'].default_value; the script stores the node in a variable for reuse. *(demo, medium; claude-blender-ai)*
- c6: [11:48] Color ramp colors are set per element by index (elements 0 to 3 for a four-element ramp), each chosen by random selection. *(demo, medium; claude-blender-ai)*
- c7: [2:02] Example scene is a donut built from Blender Guru's donut tutorial; separate versions are offered for Blender 3 LTS and Blender 4. *(doc, medium; other)*
- c8: [14:34] Palettes come from the ColourLovers web API (about 1000 most popular palettes at download time); a 1000-variation batch is generated from them. *(doc, medium; other)*

## Numbers
- n1: **palettes**: 1000 variations generated from ColourLovers palettes 
- n2: **color ramp elements**: 4 
- n3: **Blender versions of example scene**: 2 (Blender 3 LTS and Blender 4) 
- n4: **video length**: 14:58 

## Techniques
- t1: **Info-panel code capture**: Make a UI change (color picker), copy the bpy line shown in the Info panel, paste into the Text Editor script, then replace hardcoded values with variables for readability.
- t2: **Exclusion-list random pick**: Pick a random palette color; if it equals an excluded color (e.g., backdrop), re-pick until different. Keep palette larger than exclusion list to avoid infinite loop.
- t3: **Debug break on first palette**: Add a break in the palette loop to render only the first palette while testing; remove or comment it out for the full batch.
- t4: **Seed and index replay**: Note palette index and seed from the chosen preview filename; set them in main() and run once in Cycles to reproduce the look for final render.

## Quotes (brief, for attribution)
> When you start running the script, Blender will freeze up so the UI won't be responsive.  (at 13:08, CG Python)
> your script will actually hang and it's just going to be looping over and over until you decide to exit Blender  (at 9:34, CG Python)

## Points to
- ColourLovers (colorlovers.com) web API
- Blender Guru donut tutorial
- Gumroad (example scene and palette JSON)
