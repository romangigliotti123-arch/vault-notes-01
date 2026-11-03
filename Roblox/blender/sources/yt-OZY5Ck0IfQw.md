---
type: research-source
id: yt-OZY5Ck0IfQw
title: "AI-Driven Blender Scripting"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=OZY5Ck0IfQw"
published: "2025-12-26"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0513
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes", "creator-workflows"]
---
# yt-OZY5Ck0IfQw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tutorial on using an AI IDE (Google Antigravity, a VS Code fork) to write Blender Python: generating a simple bpy script, running it via the Blender Development VS Code extension, converting it into a 4.2+ extension with blender_manifest.toml, and analyzing add-on or Blender source code. Nothing on Claude, MCP, or Roblox.

## Claims
- c1: [3:47] Prompting an AI editor 'create a Blender Python script that adds three cubes at random locations' produced a working function with parameters. It pasted and ran in Blender's Scripting workspace. *(demo, high; bpy-scripting-headless)*
- c2: [7:13] AI-generated scripts wrap the call in `if __name__ == '__main__'`. With the VS Code Blender extension's Run Script this did nothing until the guard was removed. *(demo, medium; bpy-scripting-headless)*
- c3: [5:50] The Blender Development VS Code extension (maintained by Jacques Lucke and the community) launches Blender from the IDE and runs scripts and add-ons. It works in Antigravity after installing the VSIX manually. *(demo, medium; bpy-scripting-headless)*
- c4: [10:28] The AI defaulted to the legacy bl_info add-on format. It had to be told to use blender_manifest.toml, the extension format introduced in Blender 4.2. *(demo, high; bpy-scripting-headless)*
- c5: [11:49] Models may not know the latest Blender API. An agent that can search the web can look up current bpy implementations and correct its code. This addresses API version drift. *(demo, medium; bpy-scripting-headless)*
- c6: [12:35] The AI left dead code (the old bl_info file) behind and invented a placeholder website in the manifest. The generated output needs manual cleanup. *(demo, high; common-mistakes-fixes)*
- c7: [14:37] Opinion: for serious or team-used tools, read and understand AI-generated code. Otherwise a large codebase you didn't track eventually falls apart. You can ask the AI to explain parts of it. *(opinion, medium; creator-workflows)*
- c8: [16:33] The AI assistant can analyze existing add-on code, such as Bool Tool from the Blender Extensions platform. It summarizes the add-on, finds a specific feature like slice, and links to the code. The same approach works on Blender's C/C++ source. *(demo, medium; creator-workflows)*

## Techniques
- t1: **Run AI-generated bpy from the IDE**: Install the Blender Development extension in the IDE (VSIX if not in the marketplace). Use Ctrl+Shift+P > Start Blender, choose the version, then Run Script. Remove the __main__ guard if nothing runs.
- t2: **Turn a function into a panel extension**: Ask the AI in planning mode for an extension with a 3D viewport panel and a button that runs the function. It creates an operator and a panel. Then request blender_manifest.toml instead of bl_info, delete leftover files, and launch Blender from the IDE to test.

## Points to
- Google Antigravity (antigravity.google)
- VS Code Blender Development extension
- GitHub Copilot
- Blender Extensions platform (Bool Tool)
- CG Python channel / school community

## Visual notes
Frames show Antigravity with the generated add_random_cubes script, the manifest and extension files, and the Bool Tool page. They show nothing on Roblox or MCP.
