---
type: research-source
id: yt-TFQMNcTj5Jw
title: "Blender Scripting Guide: Mastering Mesh Editing with Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=TFQMNcTj5Jw"
published: "2023-08-18"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 2
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless"]
---
# yt-TFQMNcTj5Jw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial on Blender's bmesh module from Python: create a bmesh from mesh data, edit it with bmesh.ops, write it back with to_mesh, then update and free. Covers bevelling verts and edges, and the edit-mode variant using from_edit_mesh and update_edit_mesh. No Roblox, MCP or Claude content.

## Claims
- c1: [1:37] bmesh is a separate module and must be imported alongside bpy. *(demo, high; bpy-scripting-headless)*
- c2: [2:59] bmesh.from_mesh(mesh_obj.data) initialises a bmesh from object mesh data in object mode. *(demo, high; bpy-scripting-headless)*
- c3: [5:23] Geometry edits made to a bmesh do not show in the viewport until bmesh.to_mesh() writes them back to mesh data. *(demo, high; bpy-scripting-headless)*
- c4: [6:43] After to_mesh, calling mesh_obj.data.update() makes the change visible immediately in the viewport. *(demo, high; bpy-scripting-headless)*
- c5: [7:12] Presenter advises calling bm.normal_update() after any operation that modifies the mesh. *(opinion, medium; bpy-scripting-headless)*
- c6: [8:33] bmesh.ops.bevel takes geom=edges for edge bevel with offset, segments and profile parameters; geom=verts for vertex bevel. *(demo, high; bpy-scripting-headless)*
- c7: [9:41] In edit mode, bm = bmesh.from_edit_mesh(mesh_obj.data) replaces from_mesh, and bmesh.update_edit_mesh(mesh_obj.data) replaces to_mesh plus update. *(demo, high; bpy-scripting-headless)*
- c8: [10:22] Edit-mode version of the script raises an error if the object is not in edit mode; user must press Tab first. *(demo, high; bpy-scripting-headless)*
- c9: [4:24] Presenter calls bm.free() at the end, though he says Blender would free it automatically; he recommends it because Blender developers advise it. *(opinion, medium; bpy-scripting-headless)*

## Numbers
- n1: **bevel offset (vertex bevel)**: 0.5 
- n2: **bevel parameters (edge bevel, edit-mode example)**: offset, segments=4, profile=0.5 (offset value shown differs in frames) 

## Techniques
- t1: **Object-mode bmesh round trip**: Get obj via bpy.context.active_object; bm = bmesh.new(); bm.from_mesh(obj.data); run bmesh.ops; bm.to_mesh(obj.data); obj.data.update(); bm.free().
- t2: **Edit-mode bmesh pattern**: Enter edit mode (Tab) first; bm = bmesh.from_edit_mesh(obj.data); run ops; bmesh.update_edit_mesh(obj.data). Works in edit mode only; one call replaces the object-mode pair.

### Code: Object-mode bmesh bevel of default cube, from the tutorial's flow
```python
import bpy
import bmesh
mesh_obj = bpy.context.active_object
bm = bmesh.new()
bm.from_mesh(mesh_obj.data)
bmesh.ops.bevel(bm, geom=bm.verts, offset=0.5)
bm.to_mesh(mesh_obj.data)
mesh_obj.data.update()
bm.free()
```

### Code: Edit-mode variant (object must be in edit mode)
```python
bm = bmesh.from_edit_mesh(mesh_obj.data)
bmesh.ops.bevel(
    bm,
    geom=bm.edges,
    offset=0.2,
    segments=4,
    affect='EDGES',
    profile=0.5
)
bmesh.update_edit_mesh(mesh_obj.data)
```

## Quotes (brief, for attribution)
> we need to apply that b mesh to the mesh data to actually make our mesh object update  (at 6:03, CG Python)
> make sure you are in edit mode before you run this  (at 10:22, CG Python)

## Contradictions flagged
- Presenter says bm.free() is unnecessary because Blender frees it automatically, yet still recommends calling it. (vs itself)

## Visual notes
Contact sheet shows Blender Scripting workspace: default cube and camera/light deleted, bmesh script in Text editor, bevelled cube result in viewport, and edit-mode version with from_edit_mesh and update_edit_mesh. No Roblox or MCP UI visible.
