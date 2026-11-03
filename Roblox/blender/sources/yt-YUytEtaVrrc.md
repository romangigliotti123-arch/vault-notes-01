---
type: research-source
id: yt-YUytEtaVrrc
title: "5 Steps to setup VSCode for Blender Python (on Windows)"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=YUytEtaVrrc"
published: "2023-04-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes"]
---
# yt-YUytEtaVrrc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Windows walkthrough for editing Blender Python in VS Code: install a standalone Python matching Blender's interpreter (3.10), add the Python extension, install fake-bpy-module for autocomplete, and connect with the Blender Development extension to run scripts and debug add-ons with breakpoints. Nothing on Roblox, MCP, or Claude.

## Claims
- c1: [1:23] Blender bundles its own Python interpreter but Windows does not; a standalone Python is needed for VS Code. Version checked via Blender's scripting interactive console showing 3.10. *(demo, high; bpy-scripting-headless)*
- c2: [2:06] Install a standalone Python at or above Blender's interpreter version (3.10 used in video); tick 'Add python executable to PATH' in installer. *(demo, high; bpy-scripting-headless)*
- c3: [5:58] fake-bpy-module (pip install) gives VS Code autocomplete and hints for the bpy API; restart VS Code after install. *(demo, medium; bpy-scripting-headless)*
- c4: [7:18] Blender Development extension (by Jacques Lucke) adds commands like 'Blender: Start' and 'Blender: Run Script' via Ctrl+Shift+P to launch Blender and run the active file. *(demo, high; bpy-scripting-headless)*
- c5: [8:43] If Blender exits immediately from VS Code, the debugger extension failed installing modules into Blender's python folder; fix by granting the User group Allow Write on that folder via Properties > Security > Edit. *(demo, medium; common-mistakes-fixes)*
- c6: [10:04] Breakpoints in a script pause execution in VS Code, letting variables be inspected and stepped line by line while Blender updates live. *(demo, high; bpy-scripting-headless)*
- c7: [11:27] Add-on debugging: place a breakpoint in a custom operator's code; pressing the button in Blender hits the breakpoint in VS Code. *(demo, high; bpy-scripting-headless)*

## Numbers
- n1: **Blender bundled Python version**: 3.10 
- n2: **video length**: 12:29 

## Techniques
- t1: **fake-bpy-module autocomplete**: pip install fake-bpy-module into the standalone Python used by VS Code; restart VS Code so bpy names autocomplete.
- t2: **VS Code breakpoint debugging of bpy scripts**: Start Blender from VS Code via command palette, run script with Run Script command, set breakpoint, inspect sidebar variables, step through.
- t3: **Add-on debugging**: Put __init__.py add-on in its own folder opened in VS Code; set breakpoint in operator; trigger from Blender UI button.

## Points to
- fake-bpy-module GitHub repository
- Blender Development extension by Jacques Lucke
- Python extension by Microsoft
- python.org Windows installer
