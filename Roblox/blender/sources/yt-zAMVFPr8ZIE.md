---
type: research-source
id: yt-zAMVFPr8ZIE
title: "Exploring the Pie Menu Template in Blender with Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=zAMVFPr8ZIE"
published: "2023-05-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-zAMVFPr8ZIE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python tutorial on the built-in UI Pie Menu template (Blender 3.5). Covers a bpy.types.Menu subclass with layout.menu_pie(), register/unregister, a keymap hotkey (Ctrl+Alt+A) under the 3D View, and stepping through the add-on in VS Code with breakpoints. No Claude, MCP, or Roblox content.

## Claims
- c1: [1:24] Pie menu is a bpy.types.Menu subclass; draw() uses layout.menu_pie() and layout.operator('mesh.select_mode') to pick vert/edge/face mode. *(demo, high; claude-blender-ai)*
- c2: [4:09] Class is made visible to Blender only via bpy.utils.register_class/unregister_class in register()/unregister() functions; a script with only definitions does nothing until these are called. *(demo, high; claude-blender-ai)*
- c3: [6:53] Hotkey is added in register() via window_manager.keyconfigs.addon, keymap under the '3D View' space type, and kmi with PIE_MENU-style call to the menu's bl_idname; Ctrl+Alt+A chosen arbitrarily. *(demo, medium; claude-blender-ai)*
- c4: [8:56] Keymap items are stored in a global list and removed in unregister() so the hotkey can be disabled cleanly when the add-on is disabled. *(demo, high; claude-blender-ai)*
- c5: [8:14] Presenter says custom keymap names were not usable in his experience; only existing keymap names worked (opinion from one test). *(opinion, low; claude-blender-ai)*
- c6: [11:00] Add-on needs a bl_info dict; code placed in __init__.py in a folder, then run in Blender via VS Code Blender Development extension (Command Palette: start blender) with breakpoints. *(demo, medium; other)*
- c7: [12:24] Debugging run used Blender 3.5 on Windows; register() hit at startup and unregister() hit when add-on disabled in Preferences. *(demo, medium; other)*

## Numbers
- n1: **Blender version used**: 3.5 
- n2: **Hotkey**: Ctrl+Alt+A 

## Techniques
- t1: **Pie menu via bpy Menu subclass**: Subclass bpy.types.Menu with bl_idname and bl_label; in draw(), get layout.menu_pie() and add operators. Register class with bpy.utils.register_class.
- t2: **Add-on hotkey registration**: In register(), get window_manager, check keyconfigs.addon, add keymap under '3D View', add keymap item calling the menu; store in global list; remove items and clear list in unregister().
- t3: **Step-through debugging of add-on**: Use VS Code Blender Development extension to launch Blender, set breakpoints in register/unregister and draw, and step through add-on lifecycle.

### Code: Register/unregister pattern for a bpy class
```python
def register():
    bpy.utils.register_class(PieMenu)

def unregister():
    bpy.utils.unregister_class(PieMenu)
```
