---
type: research-source
id: yt-zP0s1i9EXeM
title: "5 Steps to setup VSCode for Blender Python (on Linux)"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=zP0s1i9EXeM"
published: "2023-05-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-zP0s1i9EXeM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Linux guide for editing Blender Python in VS Code. Covers matching Blender's bundled Python (3.10 in the video), building it from source with altinstall, installing the VS Code Python extension, a fake bpy module for autocomplete, and the Blender Development extension to run scripts and debug add-ons with breakpoints. Nothing on Roblox, Claude, or blender-mcp.

## Claims
- c1: [2:01] Blender's scripting workspace showed it uses Python 3.10; the matching or higher interpreter is needed outside Blender. *(demo, high; claude-blender-ai)*
- c2: [1:23] Distro system Python 3 often does not match Blender's bundled Python version, so a separate interpreter is needed. *(opinion, medium; claude-blender-ai)*
- c3: [6:52] Use 'make altinstall', not 'make install', so the system Python 3.9 on Rocky Linux is not replaced. *(experience, medium; other)*
- c4: [6:09] Build parallelism set from nproc result: 8 jobs (make -j8) on the test machine. *(demo, medium; other)*
- c5: [11:49] A pip-installed fake bpy module gives VS Code autocomplete and hints for bpy; the video does not show the full package name in the transcript. *(demo, medium; claude-blender-ai)*
- c6: [14:11] The Blender Development extension (by Jacques Lucke) adds commands via Ctrl+Shift+P to start Blender and run the current script inside Blender without opening its text editor. *(demo, high; claude-blender-ai)*
- c7: [14:52] On first Blender boot, the VS Code extension installs extra Python packages into Blender's Python so it can talk to VS Code. *(demo, high; claude-blender-ai)*
- c8: [18:15] Breakpoints set in an add-on operator's function fire when the Blender button is pressed, allowing inspection of passed parameters and step-through. *(demo, high; claude-blender-ai)*

## Numbers
- n1: **Blender bundled Python version**: 3.10 
- n2: **make -j build jobs from nproc**: 8 
- n3: **default system Python on Rocky Linux**: 3.9 

## Techniques
- t1: **Run Blender script from VS Code**: Install Blender Development extension; Ctrl+Shift+P, 'Blender: Start' and pick Blender executable; then 'Blender: Run Script' to execute the open file in the running Blender.
- t2: **Breakpoint debugging of bpy scripts and add-ons**: Set breakpoints in VS Code, start Blender via the extension, run the script or click the add-on button, then step over lines and inspect variables.

## Quotes (brief, for attribution)
> it's very important for you to run the alt install because it won't replace that 3.9 so the system python  (at 6:52, CG Python)

## Points to
- python.org (standalone Python download)
- Visual Studio Code website
- Blender Development VS Code extension by Jacques Lucke
- Fake bpy module pip package (link in video description, not named in transcript)
- Visual Effects Society technology committee (Rocky Linux recommendation)
