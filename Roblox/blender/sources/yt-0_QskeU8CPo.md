---
type: research-source
id: yt-0_QskeU8CPo
title: "Blender Python scripting: Creating custom operators from scratch"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=0_QskeU8CPo"
published: "2023-03-19"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "creator-workflows"]
---
# yt-0_QskeU8CPo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial (part 2 of a custom-panel series) showing how to define a bpy.types.Operator with a bl_idname, register it, call it from a sidebar panel, move geometry logic into a function, add FloatProperty/IntProperty options with min/max, a BoolProperty checkbox, and enable the REGISTER/UNDO options for the redo panel. Nothing on Roblox export, MCP, or Claude.

## Claims
- c1: [0:52] Operators are defined as classes inheriting bpy.types.Operator with a bl_idname like 'mesh.add_subdiv_monkey' and bl_label; execute(self, context) must return {'FINISHED'}. *(demo, high; bpy-scripting-headless)*
- c2: [5:03] After registering, the operator is callable from the Python console as bpy.ops.mesh.<idname suffix> and autocompletes; its docstring shows as tooltip. *(demo, high; bpy-scripting-headless)*
- c3: [8:08] Author recommends recording manual actions in the Info panel and copy-pasting the generated bpy commands into the operator as a fast way to get code. *(demo, medium; bpy-scripting-headless)*
- c4: [12:30] Properties are declared as class attributes using bpy.props.FloatProperty(name, description, default); accessed in execute via self.<name>. *(demo, high; bpy-scripting-headless)*
- c5: [13:13] bl_options = {'REGISTER','UNDO'} makes the operator show an interactive redo panel at bottom-left of the viewport where properties can be changed after running. *(demo, high; bpy-scripting-headless)*
- c6: [14:48] Subdivision levels cannot be a FloatProperty; use IntProperty with min and max to constrain values (viewport 1-3, render 3-7 in the author's exercise). *(demo, high; bpy-scripting-headless)*
- c7: [16:24] A BoolProperty renders as a checkbox in the operator UI and can gate optional steps such as shade smooth. *(demo, high; bpy-scripting-headless)*
- c8: [9:30] Good practice: keep execute() minimal and move geometry logic into a standalone function that takes size and subdivision levels as parameters so it can be reused outside operators. *(opinion, medium; bpy-scripting-headless)*
- c9: [1:33] Right-clicking an add-on button in Blender preferences and choosing Edit opens the add-on source in the Text Editor, allowing live edits of the file. *(demo, medium; creator-workflows)*

## Numbers
- n1: **Example monkey size float default**: 4 Author changed default size to 4 to visibly show the property working
- n2: **Subdivision viewport range (exercise)**: min 1, max 3 Exercise 1 integer bounds for viewport subdivision levels
- n3: **Subdivision render range (exercise)**: min 3, max 7 Exercise 1 integer bounds for render subdivision levels

## Techniques
- t1: **Operator registration and invocation**: Subclass bpy.types.Operator, set bl_idname and bl_label, implement execute returning {'FINISHED'}, add to register/unregister lists, then test via bpy.ops.<category>.<name>() in the Python console.
- t2: **Logic-in-function split**: Move modeling code into a function taking size and subdivision params; operator execute only reads self properties and calls the function.
- t3: **Redo panel via REGISTER+UNDO**: Set bl_options to {'REGISTER','UNDO'} so the operator's properties appear in the bottom-left redo panel and can be adjusted after execution.

### Code: Float size property and use in operator
```python
size: bpy.props.FloatProperty(
    name="Size",
    description="Size of the monkey head",
    default=2.0
)
```

### Code: Integer subdivision levels with bounds (IntProperty, not Float)
```python
viewport_levels: bpy.props.IntProperty(
    name="Viewport Levels",
    description="Subdivision levels in viewport",
    min=1, max=3
)
```

## Quotes (brief, for attribution)
> you would need to use the integer property  (at 14:48, CG Python)

## Points to
- Blender Python API docs (bpy.props, bpy.types.Operator)
