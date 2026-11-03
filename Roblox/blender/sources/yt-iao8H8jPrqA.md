---
type: research-source
id: yt-iao8H8jPrqA
title: "PBRT 2: Creating and Working with Large Scenes — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=iao8H8jPrqA"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "mesh-texture-limits"]
---
# yt-iao8H8jPrqA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Talk on building large PBRT scenes in Blender via the Python API (bpy), not Roblox. Covers caching bpy operator results, collection-based instancing, deterministic hiding of instances to keep the viewport responsive, curve bundling, node-graph construction for materials, and VDB volume gotchas. No Roblox export, FBX/glTF, Studio, or Claude/MCP content.

## Claims
- c1: [10:50] Calling bpy operators is slow because they hook into undo/redo; use them sparingly, and cache results by exact parameters, copying the cached object on repeat requests. *(experience, medium; claude-blender-ai)*
- c2: [12:23] PBRT instance groups map well to Blender: one collection per group, shapes added to it, then an instance object set to collection instancing with a transform. *(experience, medium; claude-blender-ai)*
- c3: [13:05] Combining caching with instancing: repeated identical shapes with different transforms become instances, cutting a city scene to 66 meshes with over 600,000 instances. *(data, medium; claude-blender-ai)*
- c4: [15:59] Hiding a target ratio of instances uniformly uses an accumulator per group (add ratio per object, hide when total exceeds 1) instead of random numbers; hiding 90-95% raised landscape viewport to about 13 fps. *(data, medium; claude-blender-ai)*
- c5: [18:57] Curve objects with millions of single strands are bundled: curves grouped by shared type and meta parameters, each bundle added as many strands in one Blender curve object; curve U/V resolution reduces memory. *(experience, medium; claude-blender-ai)*
- c6: [27:38] VDB volumes created via OpenVDB cannot be imported in memory; must write a file and import it. Volume placement offset changed between Blender 4.5 and 5.1/5.2 (corner vs. middle of first voxel). *(experience, medium; claude-blender-ai)*
- c7: [06:00] A landscape scene with about 300 unique meshes and many instances reaches about 26 million triangles, which made the Blender viewport drop well below 1 FPS when opened as-is. *(data, medium; mesh-texture-limits)*

## Numbers
- n1: **triangles (instanced)**: ~26 million from ~300 unique meshes 
- n2: **curve objects in hair model**: over 3 million 
- n3: **city scene meshes vs instances**: 66 meshes, over 600,000 instances 
- n4: **viewport FPS after hiding 90-95% of instances (landscape)**: ~13 fps 
- n5: **5x5x5 OpenVDB grid result in Blender**: 8x8x8 grid 

## Techniques
- t1: **Object cache for bpy operator results**: Key by exact parameters; on hit, copy the cached object and rename; on miss, call the operator and store the result.
- t2: **Collection-based instancing**: Create one collection per instance group, add its shapes, then create an instance object with instance_type set to collection and the transform.
- t3: **Deterministic uniform hiding**: Per group keep a ratio accumulator; add target ratio per object; when it exceeds 1, hide the current object and subtract 1.
- t4: **Curve bundling**: Group curves by type and meta parameters, then add each bundle as multiple strands in one curve object.
- t5: **Recursive node-graph build from scene material description**: Create output node, link material to Surface socket, then for each parameter link the source node to the named socket, recursing for nested textures or mixed materials.

## Quotes (brief, for attribution)
> calling Blender operators in this fashion can be quite slow depending on them since they are often plumbed into various other things such as the undo and redo system  (at 10:50, Blender)
> I don't particularly like non-determinism. So, I use a slightly more complicated scheme  (at 15:59, Blender)

## Points to
- blender-mcp / Roblox pipeline: none referenced
- PBRT (physically based ray tracer) book and framework
- Codeberg repository (promised, not yet published)
- ASWF Digital Production Example Library (USD scenes)
- node_bpy extension (mentioned)
- Material Utils add-on
- Node Arrange add-on
