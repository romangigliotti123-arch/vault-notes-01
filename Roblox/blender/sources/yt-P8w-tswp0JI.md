---
type: research-source
id: yt-P8w-tswp0JI
title: "Extending Blender Pie Menus with Custom Operators using Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=P8w-tswp0JI"
published: "2023-06-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-P8w-tswp0JI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python tutorial on extending a pie menu (Ctrl+Alt+A hotkey add-on) with built-in and custom bpy operators. Shows a custom Operator class that adds a Subdivision Surface modifier, registration/unregistration, debugging in VS Code, and F3 search. Not about Roblox, Claude, blender-mcp, or FBX/Roblox export.

## Claims
- c1: [1:18] Pie menu options can call built-in bpy operators by label and icon; icon names are found via Preferences > Interface > Developer Extras icon viewer. *(demo, high; claude-blender-ai)*
- c2: [4:45] Custom operator = bpy.types.Operator subclass with bl_idname, bl_label, bl_options (e.g. UNDO) and IntProperty fields; referenced in pie menu by its bl_idname. *(demo, high; claude-blender-ai)*
- c3: [11:31] Operator class must be registered in register() and unregistered in unregister(); otherwise Blender does not know it. *(demo, high; claude-blender-ai)*
- c4: [12:13] Custom operators only appear in F3 search when Developer Extras is enabled in preferences. *(demo, high; claude-blender-ai)*
- c5: [6:07] Operator helper should validate context.active_object exists and is type MESH, printing a warning and returning otherwise, since callers can pass a camera. *(demo, high; claude-blender-ai)*
- c6: [7:23] Debugging bpy add-ons: launch Blender from VS Code with breakpoints set, then step through the operator function to inspect active object type. *(demo, medium; claude-blender-ai)*
- c7: [13:01] Including UNDO in bl_options makes the operator's properties editable in the bottom-left Adjust Last Operation panel. *(demo, high; claude-blender-ai)*
- c8: [5:27] Example custom operator sets a Subdivision Surface modifier with viewport levels 3 and render levels 5 on the active mesh. *(demo, high; claude-blender-ai)*

## Numbers
- n1: **subsurf levels**: viewport 3, render 5 example Subdivision Surface modifier settings in custom operator

## Techniques
- t1: **Pie menu operator wiring**: Define operator class, register it, then reference it in pie menu column via its bl_idname and an icon-name label.
- t2: **Breakpoint debugging of bpy add-on**: Run Blender from VS Code, set breakpoint at function top, run script, step through to check object type.

## Points to
- Victor Stepanoff (CG Python channel)
