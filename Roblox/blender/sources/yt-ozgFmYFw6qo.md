---
type: research-source
id: yt-ozgFmYFw6qo
title: "GN-to-UV: Hacking Coordinates with Geometry Nodes — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=ozgFmYFw6qo"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 1
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-ozgFmYFw6qo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Conference 2026 talk on Geometry Nodes for procedural UVs. Case 1: side UVs for a cloth/foam solidify rim using ID reordering and ID-difference pattern (256 = vertex count per plane x planes). Case 2: procedural path UVs using curve-to-mesh attribute storage, cross/dot products for left/right side, and geometry proximity. No Claude, blender-mcp, bpy, Roblox export, or mesh limits content.

## Claims
- c1: Source covers Geometry Nodes UV generation only; no mention of Claude, blender-mcp, bpy scripting, Roblox Studio, FBX/glTF export, or Roblox limits. *(doc, high; other)*
- c2: [5:14] Speaker states self-collisions in cloth simulation are consistent and fast, so multiple cloth objects are kept as one object (opinion/experience). *(opinion, medium; other)*
- c3: [14:58] Index-difference pattern on solidify-generated side vertices equals 256, derived from 64 vertices per plane times 4 planes; total vertex count 512 is double that. *(demo, medium; other)*
- c4: [8:40] Attribute Statistic node used to get vertex count so the normalization works across different mesh sizes instead of hardcoding. *(demo, medium; other)*
- c5: [22:21] Path generator uses a single material for the whole path; displacement mixing is done procedurally, and the UV-following path material is mixed with a standard-UV material. *(demo, medium; other)*
- c6: [27:51] Curve attributes (tangent, spline length/factor) are lost on Curve to Mesh, so they must be stored as named attributes before conversion and resampled with Sample Nearest/Sample Index. *(demo, high; other)*
- c7: [25:06] Left/right side of a curve is detected with cross product (tangent x normal) and dot product sign against pointing vectors; dot product > 0 separates sides. *(demo, high; other)*
- c8: [32:37] Geometry Proximity output is mirrored on both sides of curve; multiplying one side by -1 and mixing yields a full 0-1 ramp for U. *(demo, high; other)*
- c9: [35:23] Shader editor preview glitch (puff appearing above snow) was fixed by reopening the file; not a geometry issue. *(experience, low; other)*

## Numbers
- n1: **index difference between paired vertices**: 256 64 vertices per plane x 4 planes; total vertices 512
- n2: **UV multiply value tried**: 100 stretch multiplier mentioned as a starting point, to be tuned per texture
- n3: **Blender version used**: 5.1 speaker switched from 4.3 to 5.1 for the demo

## Techniques
- t1: **ID-difference pattern counting for procedural side UVs**: Delete all but rim; read Index on side geometry; find constant index offset between paired verts; count verts with Accumulate Field; use that to split the two solidify layers and Sample Index back to original.
- t2: **Mesh to Curve then Curve to Mesh to reorder IDs**: Convert rim to curve and back so indices follow the loop order; then normalize by max index for a smooth gradient.
- t3: **Store curve attributes before Curve to Mesh**: Store length/tangent as named attributes on the curve, convert to mesh, then Sample Nearest and Sample Index to recover them.
- t4: **Side detection via cross and dot product**: Cross(tangent, surface normal) gives side direction; Dot with vector from vertex to closest curve point; positive/negative sign splits left and right.

## Quotes (brief, for attribution)
> I kind of want to break a stigma about geonodes being maybe overly complicated or that you need massive node networks  (at 0:45, Blender)
> all these pairs are actually apart from each other by a value of 256  (at 14:58, Blender)
