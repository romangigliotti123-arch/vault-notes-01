---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-topology-rules.md
title: "elithril/blender-kiln/plugin/references/topology-rules.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/topology-rules.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0035
relevance: 2
density: high
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# gh-elithril-blender-kiln-f-plugin-references-topology-rules.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Generic mesh topology and poly-budget reference for a Blender AI-mesh cleanup plugin (blender-kiln). Covers quads vs tris, edge flow, mesh cleanliness, platform and tier triangle budgets, decimation modes with a bpy snippet, LOD percentages with a gltfpack command, and a post-AI-generation cleanup order. Not Roblox-specific; no Roblox limits, FBX/glTF settings, or rigging rules.

## Claims
- c1: AI-generated meshes are dense triangulated, typically 100-300K faces, and always need retopo or decimation. *(doc, medium; mesh-texture-limits)*
- c2: blender-kiln soft triangle tiers: hero/character lightweight 3-8K, balanced 8-20K, detailed 20-80K; props 300-1.5K / 1.5-5K / 5-15K. *(doc, medium; mesh-texture-limits)*
- c3: Tier ranges are soft: up to 2x the top is allowed if triangles sit on visible round parts; past 2x, propose reduction. Never block. *(doc, medium; mesh-texture-limits)*
- c4: Platform budgets listed for Web/WebGL, Mobile, Console/PC, VR/AR, UE5 Nanite; none are Roblox-specific. *(doc, high; mesh-texture-limits)*
- c5: Decimation rules: show before/after poly count and screenshot, ask before applying, keep original backup, prefer multiple low-ratio passes over one aggressive pass. *(doc, medium; mesh-texture-limits)*
- c6: Decimate modes: Collapse for general use, Un-Subdivide for regular grids, Planar for flat surfaces. *(doc, medium; mesh-texture-limits)*
- c7: LOD ladder as percent of LOD0 with distance bands: LOD1 50% at 10-25m, LOD2 25% at 25-50m, LOD3 10-12% at 50-100m. *(doc, medium; mesh-texture-limits)*
- c8: LODs generated via gltfpack with simplification flag: gltfpack -i model.glb -o optimized.glb -si 0.5. *(doc, medium; automation-and-creator-workflows)*
- c9: Post-AI cleanup order: merge by distance, recalc normals, remove loose geometry, apply transforms, check tier, decimate if needed, center origin at base. *(doc, medium; mesh-texture-limits)*
- c10: Topology rules: quads for deforming meshes, triangles acceptable for static props, n-gons avoided, 5-edge poles preferred over 3-edge, poles kept out of deformation zones. *(doc, medium; mesh-texture-limits)*
- c11: Character edge loops should follow muscle/joint lines; critical loops at eyes, mouth, shoulders, elbows, knees. *(doc, medium; rigging-animation)*
- c12: Decimation is shown as a bpy modifier script: add DECIMATE modifier, set COLLAPSE, ratio = target/current faces, then apply. Ratio is approximate. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **AI mesh face count**: 100-300K faces typical raw AI-generated mesh before reduction
- n2: **Hero/character triangle tiers**: lightweight 3-8K; balanced 8-20K; detailed 20-80K blender-kiln soft ranges, not hard caps
- n3: **Prop triangle tiers**: lightweight 300-1.5K; balanced 1.5-5K; detailed 5-15K blender-kiln soft ranges
- n4: **Soft-cap overshoot allowed**: up to 2x top of tier if triangles on visible round parts; past 2x propose reduction
- n5: **LOD1/LOD2/LOD3 size**: 50% / 25% / 10-12% of LOD0 distance bands 10-25m, 25-50m, 50-100m

## Techniques
- t1: **Multi-pass low-ratio decimation**: Back up original, decimate in several small ratio passes rather than one aggressive pass, show before/after poly count and screenshot, apply only after user confirmation.
- t2: **AI mesh cleanup sequence**: Merge by distance, recalc normals, remove loose geometry, apply transforms, check tier, decimate if needed, center origin at base.

### Code: Blender bpy decimation via Decimate modifier (COLLAPSE) applied to active object
```python
import bpy

obj = bpy.context.active_object
mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
mod.decimate_type = 'COLLAPSE'
mod.ratio = target_faces / current_faces  # approximate
bpy.ops.object.modifier_apply(modifier="Decimate")
```

### Code: Generate a simplified LOD glb with gltfpack
```shell
gltfpack -i model.glb -o optimized.glb -si 0.5
```

## Quotes (brief, for attribution)
> AI-generated meshes are always dense triangulated → retopo or decimate needed  (elithril)
> Multiple passes at low ratios > one aggressive pass  (elithril)

## Points to
- gltfpack
