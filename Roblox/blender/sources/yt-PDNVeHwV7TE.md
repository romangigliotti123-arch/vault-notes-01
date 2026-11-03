---
type: research-source
id: yt-PDNVeHwV7TE
title: "How To Improve Your UI In Roblox Studio"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=PDNVeHwV7TE"
published: "2025-06-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0563
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-PDNVeHwV7TE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Photoshop-based Roblox UI tutorial: building gradient/stroke/drop-shadow currency bars, popup and buttons as smart objects, exporting PNGs, and using ImageButton Image/HoverImage for a press effect without scripts. Nothing on Blender, Claude, bpy or 3D pipelines; only the 2D UI asset workflow is marginally relevant.

## Claims
- c1: [16:31] Clickable UI elements must be exported as separate images from the popup background, otherwise they can't be clicked individually. *(demo, high; automation-and-creator-workflows)*
- c2: [18:15] Press-button effect: export one button with drop shadow and one without (shifted down to cover shadow, no horizontal move). Set ImageButton Image to the shadow version and HoverImage to the no-shadow version; no script needed. *(demo, high; automation-and-creator-workflows)*
- c3: [18:57] Export UI as PNG, not JPEG, with the background layer hidden, so transparency works. Set ImageButton BackgroundTransparency to 1. *(demo, high; automation-and-creator-workflows)*
- c4: [8:06] Author UI canvases large (e.g. 2000x1000) and crop afterwards to avoid pixelated results in Studio. *(demo, medium; automation-and-creator-workflows)*
- c5: [5:25] Converting a layer to a smart object lets you add a final outer stroke that includes the drop shadow, while its effects stay editable. Duplicating it and recoloring makes variants (e.g. coins vs gems) in seconds. *(demo, medium; automation-and-creator-workflows)*
- c6: [11:45] Opinion: tint grays and blacks slightly blue for richer UI color; font choice and scale matter greatly (Clashbolt used instead of the popular Luckiest Guy). *(opinion, medium; other)*

## Numbers
- n1: **initial currency bar canvas**: 500x500 px 
- n2: **popup canvas**: 2000x1000 px 
- n3: **drop shadow settings for outline look**: spread 100%, size 0, opacity 100%, normal blend, distance ~10 
- n4: **title font size**: 300 

## Techniques
- t1: **ImageButton hover press effect**: Insert ScreenGui, add ImageButton. Set Image to the button PNG with drop shadow and HoverImage to the PNG without shadow, positioned lower. Set BackgroundTransparency to 1. Hovering looks like a press.
- t2: **Photoshop layered UI styling**: Draw a rounded rectangle, add gradient overlay, gradient stroke and a drop shadow, convert to smart object, then add an outside solid black stroke. Duplicate the smart object and recolor for variants, then export PNG.

## Points to
- Photoshop
- Pixlr
- Photopea
- Clashbolt font
- Luckiest Guy font
