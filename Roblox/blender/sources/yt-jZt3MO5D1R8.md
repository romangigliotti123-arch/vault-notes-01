---
type: research-source
id: yt-jZt3MO5D1R8
title: "Blender Python Tutorial : Create Property Group & Enumerator (Panel) [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=jZt3MO5D1R8"
published: "2020-08-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0036
relevance: 2
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless"]
---
# yt-jZt3MO5D1R8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial on building a bpy.types.PropertyGroup with string, float-vector and enum properties, registering it on bpy.types.Scene as a pointer property, drawing it in a N-panel, and using the values in an operator to add primitives, rename objects and set scale. Not Roblox-specific; no blender-mcp or Roblox export content.

## Claims
- c1: [1:35] Custom UI settings are built by subclassing bpy.types.PropertyGroup and declaring fields with bpy.props (string, float, enum) inside it. *(demo, high; bpy-scripting-headless)*
- c2: [7:44] The property group is attached to bpy.types.Scene via bpy.props.PointerProperty(type=...), and must be deleted in unregister with del bpy.types.Scene.my_tool. *(demo, high; bpy-scripting-headless)*
- c3: [4:18] Enum items are a list of (identifier, name, description) tuples; the identifier is what the code compares against. *(demo, high; bpy-scripting-headless)*
- c4: [8:25] Panel draw code gets scene via context.scene and reads the group with layout.prop(my_tool, 'property_name'). *(demo, high; bpy-scripting-headless)*
- c5: [12:06] Operator branches on the enum value and calls bpy.ops.mesh.primitive_cube_add, uv_sphere_add or monkey_add; the Shift+A tooltip shows the Python op name and can be copied. *(demo, high; bpy-scripting-headless)*
- c6: [16:22] A float vector property is indexed per axis (index 0,1,2) to set object.scale[0..2] from the panel values. *(demo, high; bpy-scripting-headless)*
- c7: [14:08] Object name can be set from a string property via bpy.context.object.name; the Properties editor tooltip reveals the data path to copy. *(demo, medium; bpy-scripting-headless)*

## Numbers
- n1: **vector axes indexed**: 3 (indices 0,1,2) 

## Techniques
- t1: **PropertyGroup plus PointerProperty on Scene**: Subclass bpy.types.PropertyGroup with bpy.props fields; register it; set bpy.types.Scene.my_tool = PointerProperty(type=group); read in panel via context.scene.my_tool; delete in unregister.
- t2: **Enum-driven operator branching**: In operator execute, compare my_tool.my_enum to identifier strings and call matching bpy.ops primitive add; copy op names from Shift+A tooltips.

### Code: Property group with string, float-vector and enum fields
```python
class my_properties(bpy.types.PropertyGroup):
    my_string: bpy.props.StringProperty(name="Enter text")
    my_float_vector: bpy.props.FloatVectorProperty(name="", soft_min=0, soft_max=100000)
    my_enum: bpy.props.EnumProperty(
        name="Enumerator",
        description="",
        items=[('OP1', 'Option 1', ''), ('OP2', 'Option 2', ''), ('OP3', 'Option 3', '')])
```

### Code: Attach and detach the group on Scene in register/unregister
```python
bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=my_properties)

# in unregister():
del bpy.types.Scene.my_tool
```

### Code: Operator branching on enum value to add primitives
```python
if my_tool.my_enum == 'OP1':
    bpy.ops.mesh.primitive_cube_add()
elif my_tool.my_enum == 'OP2':
    bpy.ops.mesh.primitive_uv_sphere_add()
```

### Code: Setting object scale per axis from a float vector property
```python
bpy.context.object.scale[0] = my_tool.my_float_vector[0]
bpy.context.object.scale[1] = my_tool.my_float_vector[1]
bpy.context.object.scale[2] = my_tool.my_float_vector[2]
```

## Quotes (brief, for attribution)
> we're going to create our own custom properties and then display them  (at 1:35, Darkfall)
> bpy dot types dot scene dot my underscore tool so now this is done we can use our property group  (at 7:44, Darkfall)

## Points to
- Darkfall blog template script (linked in description, not fetched)
- Darkfall earlier videos on enum in dialog box and custom properties (not fetched)
