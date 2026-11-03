---
type: research-source
id: web-a25777bf0b
title: "how to make the backrooms in blender"
source_type: "web"
creator: "www.blenderguru.com"
url: "https://www.blenderguru.com/posts/2026/10/14/how-to-make-the-backrooms-in-blender"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 1
density: low
tags: ["research-source", "web", "procedural-generation", "texturing-baking-uv"]
---
# web-a25777bf0b

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Andrew Price's Blender Guru tutorial on building a procedural Backrooms level with Geometry Nodes, covering adaptive wall segments, exposed fields, box-projected textures, material segmenting in Geometry Nodes, Cycles lighting and compositing. No Claude, MCP, bpy, or Roblox content.

## Claims
- c1: Tutorial builds a procedural Backrooms level entirely in Geometry Nodes, with exposed fields for ease of use. *(doc, high; procedural-generation)*
- c2: [23:44] Materials are assigned inside Geometry Nodes, with texturing done via box projection instead of UV unwrapping. *(doc, high; texturing-baking-uv)*
- c3: [29:10] Material segmenting is handled in Geometry Nodes; emission maps are imported separately. *(doc, medium; texturing-baking-uv)*
- c4: [59:22] A shader value is linked back into Geometry Nodes to drive randomness. *(doc, medium; procedural-generation)*

## Techniques
- t1: **Adaptive wall segments**: Geometry Nodes generate wall segments that adapt to path length; outer shell created after walls. Node labelling used for organisation.

## Points to
- https://www.poliigon.com/backrooms
- http://www.blenderguru.com/academy
