---
type: research-source
id: web-e9e47272ba
title: "Blender Python API doc: info_quickstart"
source_type: "web"
creator: "docs.blender.org"
url: "https://raw.githubusercontent.com/blender/blender/main/doc/python_api/rst/info_quickstart.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: medium
tags: ["research-source", "web", "bpy-scripting-headless", "other"]
---
# web-e9e47272ba

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Official Blender Python API quickstart. Covers bpy.data access and collections, creating/removing datablocks, custom properties (basic types only, 1024 nesting limit), bpy.context read-only rules, bpy.ops operators and poll(), registering operators/panels, native/mathutils types, and keyframe insertion (simple and low-level action/slot/channelbag API). No Roblox-specific content.

## Claims
- c1: bpy.types datablocks cannot be created by calling the class; create via bpy.data.<collection>.new() and remove via collection.remove(). *(doc, high; bpy-scripting-headless)*
- c2: bpy.context is read-only; use bpy.context.view_layer.objects.active = obj instead of bpy.context.active_object = obj. *(doc, high; bpy-scripting-headless)*
- c3: Operators raise RuntimeError when poll() fails; call operator.poll() first to check context. *(doc, high; bpy-scripting-headless)*
- c4: Custom properties accept only int, float, string, arrays of int/float, and dicts with string keys and basic values; nesting limit 1024. *(doc, high; bpy-scripting-headless)*
- c5: The API is described as generally stable but some areas still being extended; creating new space types and custom properties on every type are listed as missing. *(doc, high; other)*

## Numbers
- n1: **custom property nesting depth limit**: 1024 levels 

## Techniques
- t1: **Low-level action keyframing**: Create action via bpy.data.actions.new; action.slots.new(obj.id_type, obj.name); action.layers.new().strips.new(type='KEYFRAME'); strip.channelbag(slot, ensure=True); fcurves.new(data_path,index); assign adt.action and adt.action_slot.
- t2: **Simple keyframe insert**: Set obj.location[2], then obj.keyframe_insert(data_path='location', frame=..., index=2).
- t3: **Headless-agnostic script running**: Paste script into Text Editor New block, click Run Script; output goes to terminal.

### Code: Store custom property and nested dict on datablocks
```python
bpy.context.object["MyOwnProperty"] = 42

if "SomeProp" in bpy.context.object:
    print("Property found")

value = bpy.data.scenes["Scene"].get("test_prop", "fallback value")

collection = bpy.data.collections.new("MyTestCollection")
collection["MySettings"] = {"foo": 10, "bar": "spam", "baz": {}}
```

### Code: Guard operator call with poll()
```python
if bpy.ops.view3d.render_border.poll():
    bpy.ops.view3d.render_border()
```

### Code: Insert keyframes via keyframe_insert
```python
obj = bpy.context.object
obj.location[2] = 0.0
obj.keyframe_insert(data_path="location", frame=10.0, index=2)
obj.location[2] = 1.0
obj.keyframe_insert(data_path="location", frame=20.0, index=2)
```

## Quotes (brief, for attribution)
> The Blender Python API can't create Blender data that exists outside the main Blender database (accessed through bpy.data)  (docs.blender.org)
> So bpy.context.active_object = obj will raise an error. But bpy.context.view_layer.objects.active = obj works as expected.  (docs.blender.org)

## Points to
- https://docs.blender.org/manual/en/latest/
- https://docs.blender.org/api/current/bpy.types.Operator.html
- https://docs.blender.org/api/current/bpy.types.Panel.html
