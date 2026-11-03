---
type: research-source
id: web-e2eda34103
title: "Blender Python API doc: info_gotchas_internal_data_and_python_objects"
source_type: "web"
creator: "docs.blender.org"
url: "https://raw.githubusercontent.com/blender/blender/main/doc/python_api/rst/info_gotchas_internal_data_and_python_objects.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: medium
tags: ["research-source", "web", "bpy-scripting-headless"]
---
# web-e2eda34103

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python API gotchas for bpy scripting: wrapped Python objects have short lifetimes, so don't persist them. Data names may differ from requested names, so keep references in your own dict. Linked-library name collisions need the (name, library) lookup. Changes to matrix_world need view_layer.update(). UI context changes are deferred. Scripts block redraw, so use modal operators.

## Claims
- c1: Newly created data may not get the requested name if the name is too long, already used, or empty; store the returned datablock instead of looking it up by name. *(doc, high; bpy-scripting-headless)*
- c2: Keep a own dict mapping imported asset IDs to created datablocks so lookups never hit existing bpy.data content in the blend file. *(doc, high; bpy-scripting-headless)*
- c3: bpy.data.objects[name, None] excludes linked library data; bpy.data.objects[name, lib_path] selects a library object. *(doc, high; bpy-scripting-headless)*
- c4: After changing location in script, matrix_world is stale until bpy.context.view_layer.update() is called, since evaluation is deferred. *(doc, high; bpy-scripting-headless)*
- c5: Setting Window.workspace, Window.screen, Window.scene, Area.type or Area.ui_type does not take effect immediately; defer via modal operator, app.handlers, or app.timers. *(doc, high; bpy-scripting-headless)*
- c6: A running script blocks Blender redraw and input; long tasks should use a modal operator. bpy.ops.wm.redraw_timer forced redraw is unsupported and not guaranteed across releases. *(doc, high; bpy-scripting-headless)*
- c7: Python wrappers of Blender data are created on demand and may be invalidated when Blender frees data; storing them persistently can cause invalid memory access. *(doc, high; bpy-scripting-headless)*

## Techniques
- t1: **Name-independent references**: Store the datablock returned by bpy.data.meshes.new() in a dict keyed by your own ID; avoid re-looking up by name in bpy.data.
- t2: **Forced dependency update**: After setting object properties, call bpy.context.view_layer.update() before reading matrix_world or other evaluated values.

### Code: Map imported asset IDs to created mesh datablocks without bpy.data name lookup
```python
mesh_name_mapping = {}

mesh = bpy.data.meshes.new(name=meshid)
mesh_name_mapping[meshid] = mesh

# Use own dictionary rather than `bpy.data`.
mesh = mesh_name_mapping[meshid]
```

### Code: Force dependency graph evaluation after a transform change
```python
bpy.context.object.location = 1, 2, 3
bpy.context.view_layer.update()
```

## Points to
- https://docs.blender.org/api/current/bpy.types.ViewLayer.html
- https://docs.blender.org/api/current/bpy.app.handlers.html
- https://docs.blender.org/api/current/bpy.app.timers.html
