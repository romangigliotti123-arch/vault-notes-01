---
type: research-source
id: yt-raFIWnMnXRo
title: "Blender Python Tutorial : Add-on Creation - Insta-Mist [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=raFIWnMnXRo"
published: "2020-10-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-raFIWnMnXRo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial (Darkfall, 2020) building the "Insta-Mist" add-on: a UI panel button that toggles the mist pass and builds compositor nodes (Mix RGB, Color Ramp) via bpy. Not about Claude, blender-mcp, or Roblox export. Useful only as a bpy scripting pattern reference.

## Claims
- c1: [0:00] Enabling mist manually requires view layer pass, camera viewport display, and world mist settings, then compositor nodes. *(demo, high; other)*
- c2: [4:39] Operator code that reads bpy.context.object fails with an AttributeError when a non-camera object is selected; fixed by referencing the camera via bpy.data.cameras by name. *(demo, high; claude-blender-ai)*
- c3: [8:29] Panel props can be exposed with layout.prop(world, 'start') on scene.world.mist_settings, so the UI reads world mist settings directly. *(demo, medium; claude-blender-ai)*
- c4: [10:05] Operator guards compositing with 'if scene.use_nodes == False' before enabling nodes, so an already-enabled node tree is not reset. *(demo, medium; claude-blender-ai)*
- c5: [19:55] Disabling the mist pass alone leaves orphan nodes; the author removes nodes by name via tree.nodes.remove(tree.nodes.get(...)) on disable, since stale nodes would otherwise be duplicated on re-enable. *(demo, medium; claude-blender-ai)*
- c6: [22:53] Add-on packaging: start from the Blender add-on template, fill the bl_info dict, save as a .py file and install it from text. *(demo, medium; claude-blender-ai)*
- c7: [12:08] Node positions are set via node.location = (x, y); the author used Mix at x=500 and Color Ramp at x=100, Composite moved to x=700. *(demo, low; claude-blender-ai)*

## Numbers
- n1: **Color ramp element 0 color**: (0.2, 0.2, 0.2, 1) 
- n2: **Added color ramp element position**: 0.27 
- n3: **Composite node location**: x=700, y=0 
- n4: **Mix RGB node location**: x=500, y=0 
- n5: **Video length**: 24:25; 7490 views 

## Techniques
- t1: **Reference-by-name for robust bpy operators**: Create convenience variables (scene = context.scene, camera = bpy.data.cameras['Camera'], vl = scene.view_layers[0]) and reuse them so the operator works without a selected object.
- t2: **Idempotent toggle**: Check current state (use_pass_mist, use_nodes) with an if/elif before changing it so repeated button presses do not stack duplicate nodes or reset settings.
- t3: **Find node names via sidebar**: Select node, press N, read the Name field in the Item tab, and use that exact string in tree.nodes.get() or tree.nodes.new().
- t4: **Link nodes by index**: links = tree.links.new(); pass output socket as node.outputs[index] and input as node.inputs[index]; index 0 is the first socket.

### Code: Guard to enable compositor nodes only if not already on (from operator).
```python
if scene.use_nodes == False:
```

### Code: Pattern for referencing camera data by name in bpy (spoken walkthrough, name is the tutorial's example).
```python
camera = bpy.data.cameras['Camera']
```

## Quotes (brief, for attribution)
> the idea is to create a panel with an operator which when pressed it will activate this and also create the nodes in the compositor for us  (at 0:00, Darkfall)

## Points to
- Darkfall Blender Python tutorial series (video source)
- Blender add-on template (Text Editor > Templates > Python > Add-on: Add Object)
