---
type: research-source
id: web-b2cc94fcdd
title: "Blender manual: modeling/meshes/editing/mesh/cleanup"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/modeling/meshes/editing/mesh/cleanup.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: medium
tags: ["research-source", "web", "common-mistakes-fixes", "other", "roblox-mesh-limits"]
---
# web-b2cc94fcdd

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page for Edit Mode mesh cleanup operators: Delete Loose, Decimate Geometry, Degenerate Dissolve, Limited Dissolve, Make Planar Faces, Split Non-Planar Faces, Split Concave Faces, Merge by Distance, Fill Holes. Describes parameters only. Nothing on Roblox, Claude, blender-mcp, bpy or export.

## Claims
- c1: Merge by Distance merges selected vertices closer than Merge Distance; Sharp Edges option adds edge marks so sharp edges stay sharp when smooth shading and custom split normals are used. *(doc, high; common-mistakes-fixes)*
- c2: Decimate Geometry Ratio is a target triangle-count ratio (e.g. 0.4 keeps 40% of original triangles); it collapses edges while minimizing shape change. *(doc, high; roblox-mesh-limits)*
- c3: Degenerate Dissolve collapses selected edges shorter than Merge Distance and removes small faces; it does not merge near vertices that are not connected by an edge. *(doc, high; common-mistakes-fixes)*
- c4: Fill Holes has a Sides limit; holes with more edges than Sides are skipped; Sides=0 fills all holes. *(doc, high; common-mistakes-fixes)*
- c5: Split Concave Faces and Split Non-Planar Faces (Max Angle) split faces so only convex, or less-bent, faces remain. *(doc, medium; common-mistakes-fixes)*
- c6: Delete Loose removes selected vertices, edges and optionally faces not connected to anything. *(doc, high; common-mistakes-fixes)*
- c7: Make Planar Faces Factor per iteration may not fully flatten faces at 1; increase Iterations. *(doc, medium; other)*

## Numbers
- n1: **Decimate ratio example**: 0.4 keeps collapsing edges until triangle count is 40% of original

## Techniques
- t1: **Merge by Distance**: Select vertices in Edit Mode, set Merge Distance, optionally allow Unselected, enable Sharp Edges if smooth shading with custom normals.

## Points to
- /modeling/modifiers/generate/decimate
- bpy.ops.mesh.dissolve_limited
- bpy.types.WeldModifier
