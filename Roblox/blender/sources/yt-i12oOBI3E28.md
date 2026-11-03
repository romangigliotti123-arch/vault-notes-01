---
type: research-source
id: yt-i12oOBI3E28
title: "Blender Python Tutorial : Class Naming Convention [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=i12oOBI3E28"
published: "2020-08-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-i12oOBI3E28

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender 2.8 scripting tutorial on naming Python UI classes: prefix with add-on name in caps, then type token (PT, OT, MT, HT, UL), then a lowercase descriptive name. Prevents class-name collisions between add-ons. Covers panel, operator, and menu examples; no Roblox, MCP, or Claude content.

## Claims
- c1: [0:00] Video uses Blender 2.8 and says future versions may differ; check your version before following naming steps. *(demo, high; claude-blender-ai)*
- c2: [1:16] Add-on class naming: ADDONNAME_PT_name for panels, ADDONNAME_OT_name for operators, ADDONNAME_MT_name for menues; the add-on prefix in capitals avoids class-name collisions across add-ons. *(demo, high; claude-blender-ai)*
- c3: [0:36] Template 'UI Panel Simple' script from Blender's Python templates uses a non-conforming class name; rename it and keep register/unregister in sync. *(demo, high; claude-blender-ai)*
- c4: [2:44] Menu classes subclass bpy.types.Menu; operators subclass bpy.types.Operator; panels subclass bpy.types.Panel. *(demo, medium; claude-blender-ai)*
- c5: [3:27] Type tokens listed: PT panel, MT menu, HT header, OT operator, UL for UI list; suffix name in lowercase with underscores or camel caps. *(demo, medium; claude-blender-ai)*
- c6: [0:36] Wrong class names still run in Blender without breaking for a single add-on; failure only occurs when multiple add-ons share the same class name. *(demo, medium; claude-blender-ai)*

## Numbers
- n1: **Blender version used**: 2.8 
- n2: **Video length**: 4:21 

## Techniques
- t1: **Add-on prefix class naming**: Start class name with uppercase add-on name, underscore, type token (PT/OT/MT), underscore, descriptive lowercase name. Use same string for bl_idname on panels.

### Code: Panel class naming pattern
```python
class TEXTTOOL_PT_main_panel(bpy.types.Panel):
    bl_label = "Main Panel"
    bl_idname = "TEXTTOOL_PT_main_panel"
```

### Code: Operator class naming pattern
```python
class TEXTTOOL_OT_add_cube(bpy.types.Operator):
    bl_idname = "texttool.add_cube"
    bl_label = "Add Cube"
```

### Code: Menu class naming pattern
```python
class TEXTTOOL_MT_main_menu(bpy.types.Menu):
    bl_label = "Main Menu"
```

## Quotes (brief, for attribution)
> then we can add an underscore since this is a panel type. We're going to type PT underscore  (at 1:16, Darkfall)
> Imagine you've got a whole bunch of different add-ons and they all had the same name as main panel things wouldn't work  (at 0:36, Darkfall)

## Points to
- Darkfall blog post (linked in video description, not named)
