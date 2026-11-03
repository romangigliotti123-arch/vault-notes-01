---
type: research-source
id: web-2d60c92a3b
title: "Roblox docs: art/accessories/creating-rigid/texturing"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating-rigid/texturing.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: medium
tags: ["research-source", "web", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "roblox-export-settings", "texturing-baking-uv"]
---
# web-2d60c92a3b

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs page on texture painting for rigid accessories in Blender. Covers Smart UV Project unwrap (Island Margin 0.02), adding a new material with an Image Texture base colour, marking 3D areas in Texture Paint mode, painting the 2D atlas with hard-edge falloff, and saving the image. Does not cover Claude, blender-mcp, bpy scripting, or PBR maps in depth.

## Claims
- c1: Use Blender Smart UV Project in Edit mode with Island Margin set to 0.02 to unwrap an accessory before painting. *(doc, high; texturing-baking-uv)*
- c2: Roblox docs state PBR textures are not required for rigid accessories; the tutorial uses simple painted colour instead. *(doc, high; texturing-baking-uv)*
- c3: Painting workflow: mark the 3D areas to paint in Texture Paint mode first, then paint the 2D atlas with Falloff set to the flattest icon for sharp edges. *(doc, high; texturing-baking-uv)*
- c4: Texture is assigned by adding a new material, setting Base Color to Image Texture, and creating a new blank image; an _TXT suffix is suggested for file naming. *(doc, medium; roblox-export-settings)*
- c5: Ctrl+Z (Cmd+Z on Mac) undoes accidental brushes on metal borders; hold F and drag to resize brush. *(doc, medium; common-mistakes-fixes)*
- c6: Tutorial recommends a metallic colour for metal borders to save time. *(opinion, low; creator-workflows)*
- c7: The source does not mention Claude, blender-mcp, or bpy scripting at all. *(doc, high; claude-blender-mcp)*

## Numbers
- n1: **Island Margin**: 0.02 Smart UV Project setting before painting

## Techniques
- t1: **Smart UV Project unwrap**: Edit mode, select all with A, UV menu > Smart UV Project, set Island Margin 0.02.
- t2: **Mark-then-paint atlas**: Texture Paint mode: mark 3D regions first, then paint each 2D island with hard-edge brush (flattest falloff); save via Image > Save.

## Quotes (brief, for attribution)
> While PBR textures are not required for accessories and is not covered in this tutorial  (create.roblox.com)

## Points to
- https://docs.blender.org/manual/en/2.79/editors/uv_image/uv/editing/unwrapping/mapping_types.html
- ../../modeling/surface-appearance.md
