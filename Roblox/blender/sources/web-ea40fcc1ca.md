---
type: research-source
id: web-ea40fcc1ca
title: "Roblox docs: art/accessories/creating/trimming"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/trimming.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "procedural-generation"]
---
# web-ea40fcc1ca

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs page on the clothing-accessory modelling step: trimming a duplicated full-body mannequin mesh (LongSleeve) into a long-sleeve shirt shape in Blender, then subdividing, shade-smoothing, and scaling/positioning it over the mannequin. Manual GUI workflow only; no Claude, blender-mcp, bpy, or Roblox import/export settings covered.

## Claims
- c1: Clothing base shape is made by duplicating a full-body mannequin mesh (LongSleeve object) and deleting unwanted regions (legs, arms, head) in Edit mode with wireframe view on. *(doc, high; avatar-ugc-accessories)*
- c2: Deletion is done by box-selecting vertices then pressing X and choosing Vertices, repeated until the desired clothing shape remains. *(doc, high; avatar-ugc-accessories)*
- c3: Grid-like surface is removed by adding a Subdivision Surface modifier (default settings, then Apply) followed by Shade Smooth to remove creases, creating a flat canvas for later sculpting. *(doc, high; procedural-generation)*
- c4: Body mesh is set unselectable via the Selectable filter to avoid accidental edits while fitting the clothing; a cage mesh is unhidden for fitting. *(doc, medium; avatar-ugc-accessories)*
- c5: Scale with S and move with G in Object mode only slightly so the garment rests loosely over the mannequin; a perfect fit is not required at this stage. *(doc, medium; avatar-ugc-accessories)*

## Techniques
- t1: **Mannequin trim**: Duplicate body mesh, enter Edit mode in wireframe, box-select unwanted regions, X > Vertices, repeat until shirt silhouette is reached.
- t2: **Subdivide and smooth**: Object mode, Modifier Properties > Add Modifier > Subdivision Surface, Apply with defaults, right-click > Shade Smooth.
- t3: **Loose fit over mannequin**: Unhide cage mesh, set body Selectable off, press S for small scale, G to move so garment rests loosely on body.

## Points to
- https://create.roblox.com/docs/art/accessories/creating/modeling-setup
- https://create.roblox.com/docs/art/accessories/creating/sculpting
