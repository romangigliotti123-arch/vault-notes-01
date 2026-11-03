---
type: research-source
id: yt-_0srGXAzBZE
title: "5 Steps to setup VSCode for Blender Python (on macOS)"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=_0srGXAzBZE"
published: "2023-04-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-_0srGXAzBZE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Mac-only tutorial (2023) on setting up VS Code for Blender Python: install a standalone Python matching/exceeding Blender's version, install VS Code and Python extension, add fake-bpy-module for autocomplete, and use Blender Development extension to run scripts and debug add-ons with breakpoints. No content on Claude, blender-mcp, Roblox export, or mesh/rig limits.

## Claims
- c1: [1:22] Mac's built-in Python 3 is older than Blender's bundled Python; install standalone Python >= Blender's version (Blender showed 3.10; author installed 3.10.11 from python.org). *(demo, high; claude-blender-ai)*
- c2: [4:23] VS Code setup: install Microsoft Python extension, run-and-debug 'debug current active python file' to run scripts outside Blender. *(demo, high; automation-and-creator-workflows)*
- c3: [7:28] Install fake-bpy-module via pip (python3 -m pip install) to give VS Code autocomplete for bpy API; suggestions work with partial typing. *(demo, high; claude-blender-ai)*
- c4: [9:15] Blender Development extension (by Jacques Lucas) plus command palette 'Blender: Start' launches Blender and attaches debug client; 'Run Script' executes file inside running Blender. *(demo, high; claude-blender-ai)*
- c5: [10:37] Breakpoints work inside Blender-run scripts and add-on operators: pause, inspect variables, step line by line, then press play to continue. *(demo, high; automation-and-creator-workflows)*
- c6: [11:59] Add-on debugging: put code in __init__.py of a folder opened in VS Code, start Blender, press add-on button; breakpoint in operator is hit. *(demo, high; automation-and-creator-workflows)*
- c7: [2:03] Find Blender's bundled Python version by opening Scripting workspace and checking interactive Python console. *(demo, high; claude-blender-ai)*
- c8: [2:44] macOS installer may need Full Disk Access granted temporarily (Privacy & Security); author says revoke after install. *(demo, medium; other)*

## Numbers
- n1: **Blender bundled Python version**: 3.10 shown in Blender scripting console; installed Python 3.10.11 (3.11 latest then)
- n2: **Demo cube size**: 4 example bpy script sets cube size and moves on Z axis

## Techniques
- t1: **Blender Development extension run/debug**: Install extension; Ctrl+Shift+P > Blender: Start; select Blender executable; use Run Script to execute file in running Blender; attach debugger for breakpoints.
- t2: **fake-bpy-module autocomplete**: Run python3 -m pip install fake-bpy-module in VS Code terminal; restart VS Code; use Tab to accept bpy suggestions.

### Code: Install fake bpy module for VS Code hints
```shell
python3 -m pip install fake-bpy-module
```

## Quotes (brief, for attribution)
> look for the blender development extension created by Jacques Luca  (at 9:15, CG Python)
> think of it as running a script in slow motion  (at 10:37, CG Python)

## Points to
- python.org
- fake-bpy-module GitHub repo
- VS Code Blender Development extension (Jacques Lucas)
- CG Python tutorials
