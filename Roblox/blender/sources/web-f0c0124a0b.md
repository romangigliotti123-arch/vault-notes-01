---
type: research-source
id: web-f0c0124a0b
title: "Blender manual: modeling/meshes/uv/unwrapping/seams"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/modeling/meshes/uv/unwrapping/seams.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 2
density: medium
tags: ["research-source", "web", "texturing-baking-uv"]
---
# web-f0c0124a0b

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual page on UV seams: how to mark seams (Ctrl-E in Edit Mode), check them with Select Linked in Face mode, unwrap, and adjust. Covers seaming along mirror axes and hairlines to limit unwrapped faces, plus Seams from Islands. Generic UV guidance; no Roblox-specific content.

## Claims
- c1: Mark seams by selecting edges in Edit Mode and pressing Ctrl-E (Mark Seam); Ctrl-E again clears them. *(doc, high; texturing-baking-uv)*
- c2: Use Select Linked in Face Select Mode to verify seams: selection stops at seams, so unexpected faces selected means the seam is not continuous. *(doc, high; texturing-baking-uv)*
- c3: Fewer seams means less UV stretching but more texture-seam work; the manual advises as few seams as possible while hiding them where unseen. *(doc, high; texturing-baking-uv)*
- c4: Seam bilateral meshes along the mirror axis so both halves overlay in the same texture space and share pixels. *(doc, high; texturing-baking-uv)*
- c5: Seam at the hairline to exclude the scalp from unwrapping when the head will be covered by hair. *(doc, high; texturing-baking-uv)*
- c6: Seams from Islands (UV menu, UV Editor View mode) adds seams at boundaries of existing UV islands, useful when editing already-unwrapped meshes. *(doc, high; texturing-baking-uv)*
- c7: Workflow: mark seams, unwrap, adjust seams and repeat, then manually adjust UVs. *(doc, high; texturing-baking-uv)*
- c8: Different UV approaches can be used in different areas of one mesh; one perfect unwrap is not required. *(opinion, medium; texturing-baking-uv)*
- c9: Projection (3D) painting handles seams more easily than 2D texturing, where matching edges across UV islands is difficult. *(opinion, medium; texturing-baking-uv)*

## Techniques
- t1: **Seam-then-unwrap loop**: Mark seams on edges (Ctrl-E), check with Select Linked in Face mode, run Unwrap, adjust seams, repeat, then hand-tweak UVs.
- t2: **Mirror-axis seam for symmetry**: Seam bilateral mesh along centre line in front view so both halves unwrap onto shared texture space.

## Quotes (brief, for attribution)
> It is a good idea to have as few seams as possible while having the least amount of stretching.  (docs.blender.org)

## Points to
- bpy.ops.uv.unwrap
- bpy.ops.uv.mark_seam
- bpy.ops.mesh.select_linked
