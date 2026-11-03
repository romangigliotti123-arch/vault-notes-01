---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-retopology.md
title: "ahujasid/mcp-for-blender/src/blender_mcp/guides/retopology.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/src/blender_mcp/guides/retopology.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0034
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "procedural-generation", "roblox-mesh-limits", "texturing-baking-uv"]
---
# gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-retopology.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Guide from ahujasid/mcp-for-blender on retopology and mesh cleanup for Claude-driven Blender (bpy via MCP). Covers choosing an approach by target (render prop, game prop, deforming character, 3D print), bmesh cleanup, Decimate, voxel remesh, QuadriFlow, Shrinkwrap, UV unwrapping, and Cycles normal/colour baking back to a low-poly mesh. Not Roblox-specific; no Roblox export or limits detail beyond generic face budgets.

## Claims
- c1: Generated and scanned meshes are dense, triangulated, often non-manifold; approach depends on destination (render, game prop, deforming character, 3D print). *(doc, high; procedural-generation)*
- c2: Keep the original high mesh as bake source; work on a copy via low = src.copy(); low.data = src.data.copy(). *(doc, high; texturing-baking-uv)*
- c3: Voxel remesh gives watertight even mesh but loses UVs and sharp edges; suggested voxel size ~1/200 of largest dimension. *(doc, high; procedural-generation)*
- c4: QuadriFlow is slow on dense input and can fail on non-manifold meshes; recommended to voxel remesh first, then QuadriFlow. *(doc, high; procedural-generation)*
- c5: Suggested face budgets: hero game character 15-50k tris, prop 500-5k, background 50-500. *(doc, medium; roblox-mesh-limits)*
- c6: Bake cage extrusion suggested at about 1-2% of object size when baking selected-to-active in Cycles. *(doc, medium; texturing-baking-uv)*
- c7: Guide uses MCP tools get_scene_info(fields=['topology']) for diagnosis and look(mode='angles', shading='wireframe') for viewing edges. *(doc, high; claude-blender-mcp)*
- c8: Guide says to read the current render engine before switching to Cycles for baking and restore it after; points to get_guide('bpy'). *(doc, medium; bpy-scripting-headless)*
- c9: Decimate keeps shape and UVs but outputs triangles; planar (DISSOLVE) mode suited to hard-surface. *(doc, medium; common-mistakes-fixes)*
- c10: Characters need seams marked on hidden edges before bpy.ops.uv.unwrap(); props use smart_project(angle_limit=1.15, island_margin=0.02). *(doc, medium; texturing-baking-uv)*

## Numbers
- n1: **hero game character triangle budget**: 15-50k tris Suggested budget in guide
- n2: **prop triangle budget**: 500-5k tris Suggested budget in guide
- n3: **background triangle budget**: 50-500 tris Suggested budget in guide
- n4: **voxel remesh size**: ~1/200 of largest dimension Sane starting point for voxel size
- n5: **bake cage extrusion**: 1-2% of object size For selected-to-active Cycles bake
- n6: **QuadriFlow target faces example**: 4000 bpy.ops.object.quadriflow_remesh(target_faces=4000)
- n7: **bake image resolution example**: 2048x2048 Low_Normal image for normal bake

## Techniques
- t1: **Cleanup pass with bmesh**: Create bmesh from mesh, remove doubles at 0.0001, dissolve degenerate, delete loose verts, recalc face normals, write back and free.
- t2: **Voxel then QuadriFlow**: Voxel remesh dense or non-manifold input to watertight mesh first, then run QuadriFlow to get quads for deformation.
- t3: **Normal bake high to low**: Add image texture node with new image in low material, select high then make low active, enable selected-to-active, set cage extrusion, bake NORMAL, wire into Normal Map node.
- t4: **Shrinkwrap to recover silhouette**: After remeshing, add Shrinkwrap modifier on low mesh with target set to high mesh.

### Code: bmesh cleanup: merge doubles, dissolve degenerate, delete loose verts, recalc normals
```python
import bmesh
bm = bmesh.new(); bm.from_mesh(obj.data)
bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)
bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=0.0001)
loose = [v for v in bm.verts if not v.link_edges]
bmesh.ops.delete(bm, geom=loose, context="VERTS")
bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
bm.to_mesh(obj.data); bm.free()
```

### Code: Decimate modifier for static props
```python
m = obj.modifiers.new("Decimate", "DECIMATE"); m.ratio = 0.1
```

### Code: Voxel remesh for watertight mesh (active object needed)
```python
obj.data.remesh_voxel_size = 0.01; bpy.ops.object.voxel_remesh()
```

### Code: QuadriFlow quad remesh for deformation
```python
bpy.ops.object.quadriflow_remesh(target_faces=4000)
```

### Code: Create bake target image and bake normals high-to-low in Cycles
```python
bpy.data.images.new("Low_Normal", 2048, 2048, is_data=True)
scene.render.bake.use_selected_to_active = True
bpy.ops.object.bake(type="NORMAL")
```

## Quotes (brief, for attribution)
> Voxel remesh makes a watertight, even mesh but loses UVs and sharp edges  (ahujasid)
> It is slow on dense input and can fail on non-manifold meshes — voxel remesh first, then QuadriFlow the result.  (ahujasid)

## Points to
- https://github.com/ahujasid/mcp-for-blender
- get_guide("bpy")
