---
type: research-source
id: yt-aSkgwf0SX_k
title: "Blender Python: The most confusing part of BMesh"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=aSkgwf0SX_k"
published: "2023-10-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 1
density: high
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-aSkgwf0SX_k

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tutorial on bmesh loops in Blender bpy: loop structure, edge-loop selection via link_loop_next and link_loop_radial_next, UV editing with modulo indexing, and per-vert vertex colors via lookup dictionary. Covers none of blender-mcp, Claude, Roblox export, or Roblox limits.

## Claims
- c1: [0:00] Video is about bmesh loops and bpy scripting in Blender; does not cover blender-mcp, Claude, or the Roblox export pipeline. *(doc, high; claude-blender-ai)*
- c2: [0:42] A BMesh loop stores one edge, one vert, and a reference to a face; loops store per-vertex data and have direction. *(doc, high; other)*
- c3: [2:46] Extruding a single vert adds no loops; filling a face with F adds loops. Demo mesh went 4 loops to 7 after fill. *(demo, high; other)*
- c4: [4:21] Edge loop select algorithm: link_loop_next, then link_loop_radial_next to cross to neighbor face, repeat until back at starting edge. *(demo, high; other)*
- c5: [10:31] UV data accessed via bm.loops.layers.uv.active and loop[uv_layer].uv; UV coords are 2D vectors, Y=0 bottom, Y=1 top. *(demo, high; other)*
- c6: [16:27] Loop indices of a face are not fixed; hard-coding indices 20-23 fails on other faces. Use loop.index % 4 to map corner position per face. *(demo, high; other)*
- c7: [21:17] Per-face UV offset for six tiled squares: X = (face.index + corner offset) * 1/6, distributing one tile per face. *(demo, medium; other)*
- c8: [23:23] Vertex color layer created with bm.loops.layers.color.new('vert color'); setting per-loop colors gives visible seams when each face gets different random values. *(demo, high; other)*
- c9: [25:27] Uniform vertex color fix: store random red per vert index in a dictionary (color lookup) and reuse it for all loops sharing that vert. *(demo, high; other)*
- c10: [24:45] Blender UI: after running the script, the new color attribute appears under mesh data; vertex paint mode then needs that attribute selected. *(demo, medium; other)*

## Numbers
- n1: **loop count**: 4 then 7 after fill 
- n2: **UV tiles**: 6 squares, 1/6 each 

## Techniques
- t1: **Loop-walk edge loop select**: Start from selected edge's loop; repeat link_loop_next then link_loop_radial_next; select edges until returning to start edge.
- t2: **Modulo corner indexing**: Use loop.index % 4 to map corners independent of face loop index offsets.
- t3: **Shared vertex color via lookup**: Store random color per vert index in dict; reuse for all loops of that vert to avoid seams.

### Code: Edge loop walk using loop radial traversal (from transcript, spoken code)
```python
next_loop = loop.link_loop_next
edge = next_loop.edge
edge.select = True
neighbor_loop = next_loop.link_loop_radial_next
neighbor_next = neighbor_loop.link_loop_next
```

### Code: Modulo-based UV corner selection for any face (from transcript)
```python
if loop.index % 4 == 0:
    uv.uv.y = 0
elif loop.index % 4 == 1:
    uv.uv.y = 0
```

## Quotes (brief, for attribution)
> loops store per vertex data  (at 0:42, CG Python)

## Points to
- Blender BMesh documentation
- Victor's video on modulo (linked in description)
- Victor's Blender add-on deconstruction video
