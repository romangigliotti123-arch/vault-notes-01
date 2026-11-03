---
type: research-source
id: yt-P0RvjSfFyLg
title: "Building a Complete Animation Pipeline for a Feature Film with a Woolly Look — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=P0RvjSfFyLg"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0035
relevance: 1
density: medium
tags: ["research-source", "youtube", "mesh-texture-limits", "other"]
---
# yt-P0RvjSfFyLg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
BCON26 talk by Big Water Studios (Spain) on the Piculi feature-film look: fully procedural Blender/Cycles look dev, custom hair generator, two-collection hair collision system, Voronoi-based faceted normals, ray portal node painterly hair, 2D-card volumetric shadows, custom shader attributes for lighting overrides. Nothing on Roblox, blender-mcp, bpy-with-Claude, or the Roblox export pipeline.

## Claims
- c1: Studio renders on GPU farm with 16-32 GB memory per GPU; this constrains texture resolution and forces procedural detail. *(experience, medium; other)*
- c2: Props use a 2K baked texture for ~95% of the film and switch to full procedural resolution only for close-ups, because five characters per shot exceed memory for 4K textures. *(experience, medium; mesh-texture-limits)*
- c3: Studio's hair collision workaround uses two collections (self-collision and collision-only geometry) plus proximity deletion or raycast-based normal test to trim hair inside props, since no simulation was used. *(experience, medium; other)*
- c4: Voronoi trick: feed normal as coordinate into Voronoi, use position output to create faceted planes with random color; smooth F1 mode blends hard and soft areas. *(experience, medium; other)*
- c5: Ray Portal node with direction = original hair root minus current position gives flat, color-retaining painterly hair; it was a personal project not used in final film. *(experience, medium; other)*
- c6: Lighting overrides implemented via custom shader attributes at three levels (node default, scene, object), since Blender lacks dynamic overrides; author wants dynamic overrides and path-based light linking in Blender. *(opinion, medium; other)*
- c7: Blender sequence-level lighting and texture cache changes are opening doors for small teams that cannot afford $5,000 GPUs, per speaker. *(opinion, low; other)*

## Numbers
- n1: **render farm memory**: 16-32 GB GPU render farm memory limiting texture resolution
- n2: **texture resolution**: 2K baked default, procedural for close-ups props on ~95% of film at 2K
- n3: **shadow start distance**: 5 cm leaf shadow casting start threshold in custom shadow node

## Techniques
- t1: **Voronoi faceted normals**: Plug normal vector into Voronoi texture as coordinate; use position output for planes; add random color; distort with noise; use smooth F1 for blend.
- t2: **Two-collection hair collision**: Put self-characters in one collection for local tolerance; put collision props in second hidden collection; trim hair via proximity or raycast normal test.
- t3: **Ray Portal hair**: Use Ray Portal node with position/direction inputs; direction = hair root position minus shading position; add noise for broken edges.
- t4: **Custom attribute override layers**: Define default in shader node group; overwrite per scene via custom attribute; overwrite per object for finer control.

## Quotes (brief, for attribution)
> multi-pipeline studios because we are not stuck in one type of workflow standard industry pipeline  (at 0:00, Blender)
> we needed some custom solutions for example and yeah about proceduralism  (at 23:35, Blender)

## Points to
- Blender (Cycles, RenderMan add-on test)
- Ray Portal node
- Jack (hair node sharing)
