---
type: research-source
id: yt-Qyy_6N3JV3k
title: "Create a Custom Blender Panel with less than 50 lines of Python code"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=Qyy_6N3JV3k"
published: "2023-02-27"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "other"]
---
# yt-Qyy_6N3JV3k

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial (Victor Stepanov, CG Python) on building a sidebar panel in the 3D Viewport with bpy: a Panel subclass, layout buttons, register/unregister, and packaging as an add-on. Nothing on Roblox, Claude, blender-mcp, or export. Only the generic bpy UI-scripting basics are relevant.

## Claims
- c1: [0:00] Video does not mention Roblox, Claude, blender-mcp, or any export pipeline; topic is only bpy UI panel scripting. *(doc, high; other)*
- c2: [1:27] Panel class naming convention is CATEGORY_PT_name (example: VIEW3D_PT_...), inheriting from bpy.types.Panel. *(demo, high; bpy-scripting-headless)*
- c3: [2:09] Panel placement uses bl_space_type = 'VIEW_3D' and bl_region_type = 'UI' to place it in the 3D Viewport sidebar. *(demo, high; bpy-scripting-headless)*
- c4: [3:32] A draw(self, context) method defines panel layout; without it the panel has no content. *(demo, high; bpy-scripting-headless)*
- c5: [3:53] Registration uses bpy.utils.register_class / unregister_class inside register() and unregister() functions, guarded by an if __name__ check when run from the text editor. *(demo, high; bpy-scripting-headless)*
- c6: [5:14] bl_category sets the sidebar tab name; default was 'Misc' until set. *(demo, high; bpy-scripting-headless)*
- c7: [6:34] Operator call names are copied from the Info editor after performing the action manually, e.g. mesh.primitive_cube_add, written without the bpy.ops prefix in layout.operator. *(demo, high; bpy-scripting-headless)*
- c8: [8:39] Exercise adds icosphere and shade-smooth buttons using the same Info-panel method; each button gets its own row. *(demo, medium; bpy-scripting-headless)*
- c9: [9:02] bl_info dict at top of script defines add-on name, author, blender version, location, description, category, shown in Preferences. *(demo, high; bpy-scripting-headless)*
- c10: [10:26] Script saved as a .py file (example my custom panel.py) via Text Editor save-as, then installed via Edit > Preferences > Install add-on, then enabled by checkbox. *(demo, high; bpy-scripting-headless)*
- c11: [11:07] Panel disappears after Blender restart until the add-on is re-enabled in Preferences; enabling restores the panel. *(demo, high; bpy-scripting-headless)*

## Numbers
- n1: **video length**: 12:02 
- n2: **views at capture (2023-02-27 upload)**: 28181 

## Techniques
- t1: **Minimal sidebar panel**: Subclass bpy.types.Panel; set bl_space_type='VIEW_3D', bl_region_type='UI', bl_category, bl_label; implement draw(self, context) with layout.row().operator(...).
- t2: **Get operator call from Info editor**: Perform the action via the menu, copy the logged command from the Info panel, paste into layout.operator without bpy.ops prefix.
- t3: **Package panel as add-on**: Add bl_info dict, save text as .py, install via Preferences > Add-ons > Install, enable checkbox.

## Points to
- Blender documentation for space/region type parameters (linked in description, not given)
- Victor Stepanov's separate videos on classes and Python dictionaries
