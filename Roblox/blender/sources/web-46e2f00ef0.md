---
type: research-source
id: web-46e2f00ef0
title: "Roblox docs: art/characters/creating/texturing-eyes"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/texturing-eyes.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 2
density: medium
tags: ["research-source", "web", "mesh-texture-limits", "other"]
---
# web-46e2f00ef0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on texturing character eyes in Blender via Texture Paint. Covers raising texture resolution, joining eye meshes, painting black base, deep yellow outer eye, red inner eye and pupils with specified brush radii, then separating by loose parts and renaming. Does not cover blender-mcp, bpy scripting, or the Roblox export pipeline.

## Claims
- c1: Roblox official docs page on texturing eyes in Blender uses Texture Paint tab; it is a manual texturing guide, not about blender-mcp, bpy, or the Roblox Blender export plugin. *(doc, high; other)*
- c2: Before texturing eyes, increase texture image resolution per the texturing-setup page; eyes are textured as one joined object so both get painted in one pass. *(doc, high; mesh-texture-limits)*
- c3: Eye texturing workflow: hide Head_Geo, LowerTeeth_Geo, Tongue_Geo, UpperTeeth_Geo in Outliner; join LeftEye_Geo and RightEye_Geo with Ctrl+J. *(doc, high; other)*
- c4: Paint order: black base shadow (radius 50px, strength 1.0), outer eye deep yellow (radius 75px), inner eye red (radius 5px), pupils bright red (radius 5px). *(doc, high; other)*
- c5: After painting, switch to Edit mode, select both eye objects, press P, choose By Loose Parts to separate, then rename the remaining meshes back to LeftEye_Geo and RightEye_Geo. *(doc, high; other)*
- c6: X Symmetry toggle should be turned off when creating asymmetrical eye textures. *(doc, medium; other)*

## Numbers
- n1: **Black base brush radius**: 50px, strength 1.0 
- n2: **Outer eye color brush radius**: 75px, strength 1.0 
- n3: **Inner eye and pupil brush radius**: 5px (adjust with F key) 

## Techniques
- t1: **Join-paint-separate eye texturing**: Join both eye meshes (Ctrl+J), texture paint black base, yellow outer, red inner and pupils, then Edit mode P > By Loose Parts and rename.

## Quotes (brief, for attribution)
> join the two eye objects to texture them both at the same time. Then texture paint the entire eye, starting with the outer eye, moving to the inner eye, and finishing with the pupil.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/characters/creating/texturing-setup
- https://create.roblox.com/docs/art/characters/creating/texturing-face
