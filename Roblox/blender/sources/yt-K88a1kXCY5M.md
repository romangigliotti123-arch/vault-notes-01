---
type: research-source
id: yt-K88a1kXCY5M
title: "Blender Python Tutorial : Importing Modules [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=K88a1kXCY5M"
published: "2020-09-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless"]
---
# yt-K88a1kXCY5M

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender Python tutorial on importing modules inside bpy scripts. Shows `import bpy`, then `from bpy.types import Panel, Operator` and `from bpy.props import StringProperty, FloatProperty, EnumProperty, PointerProperty` so classes and property definitions can be written without the full bpy.types./bpy.props. prefix. Tests by running the script and opening the N-panel. No Roblox, Claude, MCP, or export content.

## Claims
- c1: [0:00] Every Blender add-on script starts with `import bpy`, which exposes operators, panels, menus and other UI types. *(demo, high; bpy-scripting-headless)*
- c2: [0:57] Multiple types can be imported in one line from bpy.types, separated by commas (e.g. Panel, Operator), so classes need no bpy.types prefix. *(demo, high; bpy-scripting-headless)*
- c3: [1:51] Built-in bpy submodules listed in the Python console include bpy.data, bpy.ops, bpy.props, bpy.types, bpy.context and bpy.utils. *(demo, high; bpy-scripting-headless)*
- c4: [3:39] Property types (StringProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty) can be imported from bpy.props to shorten property group definitions. *(demo, high; bpy-scripting-headless)*
- c5: [4:43] Running the script with imports produced no errors and the new panel appeared in the N sidebar tab; the test added a sphere object via the panel. *(demo, medium; bpy-scripting-headless)*
- c6: [4:43] Author's opinion: importing specific names speeds up workflow and keeps code tidy compared with full bpy.props.X paths. *(opinion, medium; bpy-scripting-headless)*

## Techniques
- t1: **Selective from-import of bpy submodules**: Write `from bpy.types import Panel, Operator` and `from bpy.props import StringProperty, EnumProperty` at top, then subclass Panel/Operator and assign properties with bare names.

## Points to
- Darkfall scripting playlist (referenced, not linked in transcript)
