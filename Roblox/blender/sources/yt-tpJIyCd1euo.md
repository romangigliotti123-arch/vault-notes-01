---
type: research-source
id: yt-tpJIyCd1euo
title: "Blender Python Tutorial : Enumerator / Drop down Menu [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=tpJIyCd1euo"
published: "2020-07-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0051
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless"]
---
# yt-tpJIyCd1euo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial (2020) on adding an EnumProperty drop-down to a custom operator panel. Shows declaring bpy.props.EnumProperty with items tuples, drawing it via layout.prop in draw(), and branching in execute() to add a cube or sphere. No Roblox, blender-mcp, or export content.

## Claims
- c1: [0:31] Template script is a sidebar panel (N key, template tab) containing a blank operator; run via Blender's Scripting workspace. *(demo, high; bpy-scripting-headless)*
- c2: [0:56] Enum is declared as a class annotation: name: bpy.props.EnumProperty(name=..., description=..., items=[...]). *(demo, high; bpy-scripting-headless)*
- c3: [2:21] Each enum item is a tuple (identifier, display name, tooltip); execute() compares against the identifier. *(demo, high; bpy-scripting-headless)*
- c4: [4:26] draw() uses layout.prop(self, 'preset_enum') to render the enum as a drop-down in the operator popup. *(demo, high; bpy-scripting-headless)*
- c5: [5:01] execute() branches: 'OP1' calls bpy.ops.mesh.primitive_cube_add(); 'OP2' calls primitive_uv_sphere_add(). *(demo, high; bpy-scripting-headless)*
- c6: [8:04] Multiple EnumProperty declarations can be added to one operator, each with its own draw line, giving two drop-downs. *(demo, high; bpy-scripting-headless)*

## Techniques
- t1: **EnumProperty drop-down on operator**: Declare name: bpy.props.EnumProperty(name, description, items=[(id,label,tooltip),...]); draw with layout.prop(self,'name'); branch on self.name in execute(); return FINISHED.

### Code: Enum property declaration with items on an operator
```python
preset_enum: bpy.props.EnumProperty(
    name='Preset',
    description='...',
    items=[
        ('OP1', 'Cube', 'Add a cube to the scene'),
        ('OP2', 'Sphere', 'Add a sphere to the scene'),
    ]
)
```

### Code: Draw enum as drop-down and branch on selection in execute
```python
def draw(self, context):
    layout = self.layout
    layout.prop(self, 'preset_enum')

def execute(self, context):
    if self.preset_enum == 'OP1':
        bpy.ops.mesh.primitive_cube_add()
    if self.preset_enum == 'OP2':
        bpy.ops.mesh.primitive_uv_sphere_add()
    return {'FINISHED'}
```

## Points to
- Blender Python API (bpy.props)
