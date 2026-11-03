---
type: research-source
id: yt-N3U2noAHgBo
title: "Creating a Mesh from Scratch with Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=N3U2noAHgBo"
published: "2023-09-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 2
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-N3U2noAHgBo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tutorial on building meshes procedurally in Blender with bpy/bmesh: creating mesh data and objects, adding verts and faces (pyramid example), ensure_lookup_table, list comprehensions, face-orientation checks, bmesh.ops.create_icosphere, and selecting verts in edit mode via from_edit_mesh. No Claude, blender-mcp, or Roblox content despite the title.

## Claims
- c1: [0:14] Object setup: bpy.data.meshes.new(name) creates mesh data, bpy.data.objects.new(name, mesh) creates the object, and scene collection objects link adds it to the scene. *(demo, high; claude-blender-ai)*
- c2: [1:53] Editable geometry is built with bmesh.new(); mesh is written back with bm.to_mesh(mesh), optionally mesh.update(), and bm.free() at the end. *(demo, high; claude-blender-ai)*
- c3: [3:14] bm.verts.new(coords) adds one vertex and returns a reference; bm.faces.new(list_of_verts) creates a face from vertex references. *(demo, high; claude-blender-ai)*
- c4: [5:58] Indexing bm.verts[i] fails until bm.verts.ensure_lookup_table() is called; this line must run before index-based access to verts, edges, or faces. *(demo, high; claude-blender-ai)*
- c5: [9:12] Face winding order matters: a face built with the wrong vertex order shows red in Face Orientation overlay (inward-facing). Check via overlays > face orientation. *(demo, high; claude-blender-ai)*
- c6: [7:50] List comprehensions can replace explicit for-loops that build vertex-reference lists, e.g. filtering bm.verts with an if clause for selected verts; the author notes this is more advanced and optional. *(demo, medium; claude-blender-ai)*
- c7: [10:31] bmesh.ops.create_icosphere creates a full icosphere in one call; the options list can be discovered in the interactive Python console via bmesh.ops. then Tab. *(demo, high; claude-blender-ai)*
- c8: [11:53] In edit mode, bmesh.from_edit_mesh(mesh) is used instead of new(); selected verts are read via vert.select and filtered into a list. *(demo, high; claude-blender-ai)*
- c9: [12:53] Creator says vertex colors and UV data are not covered in this video and are deferred to another video. *(opinion, low; other)*

## Numbers
- n1: **pyramid vertex count**: 4 base verts plus 1 apex vert 
- n2: **index base**: 0-based indices (0,1,2,3 for four base verts) 

## Techniques
- t1: **Mesh-from-code setup**: 1) bpy.data.meshes.new(name). 2) bpy.data.objects.new(name, mesh). 3) Link object into scene collection. 4) Run in Scripting workspace to see it in outliner.
- t2: **bmesh build cycle**: 1) bm=bmesh.new(). 2) bm.verts.new per vertex. 3) ensure_lookup_table. 4) bm.faces.new with vert refs. 5) bm.to_mesh(mesh); mesh.update(). 6) bm.free().
- t3: **Face orientation check**: Enable Face Orientation overlay in viewport; blue = correct outward side, red = flipped; reorder face vertex list to fix.
- t4: **Shortcut primitives**: Use bmesh.ops.create_icosphere instead of hand-coding verts and faces; discover options in Python console with tab completion.

### Code: Create mesh data and object, link to scene (API calls named in transcript)
```python
import bpy
object_name = "my object"
mesh = bpy.data.meshes.new(object_name + "_data")
obj = bpy.data.objects.new(object_name, mesh)
bpy.context.scene.collection.objects.link(obj)
```

### Code: bmesh vertex/face creation and lookup table (API calls named in transcript)
```python
import bmesh
bm = bmesh.new()
v1 = bm.verts.new((0, 0, 0))
bm.verts.ensure_lookup_table()
bm.faces.new([bm.verts[0], bm.verts[1], bm.verts[2], bm.verts[3]])
bm.to_mesh(mesh)
mesh.update()
bm.free()
```

### Code: Read selected verts in edit mode
```python
bm = bmesh.from_edit_mesh(mesh)
selected = [v.index for v in bm.verts if v.select]
print(selected)
```

## Quotes (brief, for attribution)
> we haven't covered where the vertex colors are stored or the UV data and I'll be going over that and more in this video  (at 12:53, CG Python)

## Contradictions flagged
- Title says the video covers using Claude with Blender (blender-mcp), and the Blender-to-Roblox asset pipeline. (vs Transcript covers only bpy/bmesh scripting in the Blender Python console; no Claude, blender-mcp, or Roblox/export content appears.)
