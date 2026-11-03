---
type: research-source
id: yt-oVjer9kRO4g
title: "HOW TO ADD BLURRY BACKGROUNDS IN ROBLOX GFX (Blender 3.0+)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=oVjer9kRO4g"
published: "2023-07-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 1
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-oVjer9kRO4g

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Cycles-style depth-of-field tutorial for render stills and animation. Covers camera DoF settings (F-stop, blades, ratio), focusing via a set distance, a picked object, or an Empty that can be keyframed. Not about Roblox, MCP, bpy, or asset export. Relevance to the topic is minimal.

## Claims
- c1: [1:57] Camera DoF: lowering F-stop increases blur; raising it reduces blur. Blades can create polygon bokeh shapes such as hexagons. *(demo, medium; other)*
- c2: [2:40] Ratio stretches the blur; author usually sets it to 2 (calls it 'vodka blur' and admits unsure of the name). Set to 1 is also acceptable. *(opinion, low; other)*
- c3: [3:21] Focus distance mode: set distance in meters to focus; author used F-stop 0.1 then raised distance until character sharp. *(demo, medium; other)*
- c4: [5:01] Focus object mode: pick target with eyedropper (author used character head); this overrides and disables the distance value. *(demo, medium; other)*
- c5: [6:28] For animation, author recommends an Empty (Cube, Plane, or Axes; Sphere also works) as the focus object, since it can be keyframed with auto-keying to shift focus to other objects. *(opinion, medium; other)*
- c6: [4:21] Depth of field increases render noise; author kept Optix denoising on and accepted the extra noise. *(experience, low; other)*
- c7: [7:52] DoF blur depends on object scale relative to the empty; HDRIs tend to get blurry easily with DoF. *(opinion, low; other)*

## Numbers
- n1: **F-stop used for focus test**: 0.1 
- n2: **Ratio setting**: 2 

## Techniques
- t1: **Empty-based keyframed focus**: Add Empty (Cube) in Shift+A Empty section, scale to match subject. Set Camera > Depth of Field > Focus Object to it. Enable auto-keying and move Empty to shift focus.

## Quotes (brief, for attribution)
> use the empty section and so in here you can add either a plane axes or a cube  (at 6:28, Comix Productions)
