---
type: research-source
id: yt-eo7UjKFiagk
title: "Blender Python Tutorial : How to create and assign a Material Shader [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=eo7UjKFiagk"
published: "2020-08-10"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes", "creator-workflows"]
---
# yt-eo7UjKFiagk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender add-on tutorial (bpy, Blender 2.8+ era) showing how to build a 3D View sidebar panel and an operator that creates a new material with use_nodes, sets Principled BSDF inputs by index, adds and links an RGB node, and shows a dialog with a colour picker. No Roblox, Claude, MCP or export content.

## Claims
- c1: [1:10] Add-on UI panel uses bl_space_type VIEW_3D, bl_region_type UI and bl_category set to a new tab name; panel and operator class names follow addon_name + pt_/ot_ naming convention. *(demo, high; bpy-scripting-headless)*
- c2: [8:12] New materials created via bpy.data.materials.new are shown without nodes until material.use_nodes = True is set; otherwise the Principled BSDF is missing. *(demo, high; bpy-scripting-headless)*
- c3: [9:45] Principled BSDF is fetched with node_tree.nodes.get('Principled BSDF'); inputs[0] is Base Color and inputs[7] is Roughness (index counted from top of node). *(demo, high; bpy-scripting-headless)*
- c4: [11:09] Colour default_value needs a 4-tuple (R,G,B,A); a 3-value float_vector property raises ValueError expecting four values, so size=4 is required. *(demo, high; bpy-scripting-headless)*
- c5: [13:16] Nodes added via node_tree.nodes.new('ShaderNodeRGB'), positioned with .location=(x,y) and connected with node_tree.links.new(output, input) using outputs[0] and inputs[0]. *(demo, high; bpy-scripting-headless)*
- c6: [17:48] Operator becomes a dialog by defining invoke() returning context.window_manager.invoke_props_dialog(self); bpy.props.FloatVectorProperty with subtype COLOR_GAMMA and default tuple gives a colour picker. *(demo, high; bpy-scripting-headless)*
- c7: [16:05] Using a full stop instead of a comma between node location arguments caused a syntax error; a missing comma between property arguments also raised errors. *(demo, medium; common-mistakes-fixes)*
- c8: [4:44] Panel that uses row undefined disappears and throws a NameError in the console; replacing row with layout fixes it. *(demo, medium; common-mistakes-fixes)*
- c9: [22:43] Author notes the script can be extended to animated stylized shaders with start/end frame properties; presented as a template, no performance or quality claims. *(demo, low; creator-workflows)*

## Numbers
- n1: **Principled BSDF roughness input index**: 7 
- n2: **Colour property size (RGBA)**: 4 
- n3: **Base Color input index**: 0 

## Techniques
- t1: **Set Principled BSDF input by index**: Get node via nodes.get('Principled BSDF'), then set inputs[index].default_value; roughness is index 7, base colour is 0. Verify index by hovering the tooltip in the UI.
- t2: **Add and link shader node**: nodes.new('ShaderNodeRGB'), set .location, then links.new(rgb.outputs[0], principled.inputs[0]) to feed colour into Base Color.
- t3: **Operator with colour dialog**: Define execute() for the logic, invoke() returning window_manager.invoke_props_dialog(self), and a FloatVectorProperty(size=4, subtype='COLOR_GAMMA', default=...) on the class.

### Code: Create material, enable nodes, and set Principled BSDF base colour by input index
```python
material_basic = bpy.data.materials.new(name="Basic")
material_basic.use_nodes = True
principled_node = material_basic.node_tree.nodes.get('Principled BSDF')
principled_node.inputs[0].default_value = (1, 0, 0, 1)
principled_node.inputs[7].default_value = 0.08
bpy.context.object.active_material = material_basic
```

### Code: Operator that opens a dialog with a colour picker
```python
def invoke(self, context, event):
    return context.window_manager.invoke_props_dialog(self)

col = bpy.props.FloatVectorProperty(name="color", size=4, subtype='COLOR_GAMMA', default=(1.0, 0.0, 0.0, 1.0))
```

## Quotes (brief, for attribution)
> we actually need to define that. So let's close this back up... material_basic.use_nodes equals true  (at 8:12, Darkfall)
> sequences of dimension should contain four not three  (at 19:55, Darkfall)

## Points to
- Darkfall Blender add-on shader library (free, linked in description)
- Darkfall pastebin panel/registration snippet
