---
type: research-source
id: yt-jT2EbqMfKU8
title: "Blender Python Tip: How to Get the File Path to Your Script"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=jT2EbqMfKU8"
published: "2023-04-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: medium
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-jT2EbqMfKU8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short tutorial on locating a Blender script's own file path so it can open sibling files. __file__ returns unhelpful text inside Blender's Text Editor; bpy.context.space_data.text.filepath works there but errors from command line. Fix: branch on whether space_data is the text editor, else use __file__. Then pathlib Path(...).resolve().parent gives the folder. Nothing on Roblox, MCP, or export.

## Claims
- c1: [0:21] Inside Blender's Text Editor, __file__ does not return the script's path; it returns unhelpful text. *(demo, high; claude-blender-ai)*
- c2: [1:43] Running with blender -b and --python, __file__ returns the actual script path. *(demo, high; claude-blender-ai)*
- c3: [2:21] In the Text Editor, the script path is obtained from the text datablock's file path via space data text, not __file__. *(demo, high; claude-blender-ai)*
- c4: [3:03] Using space_data in background/command-line mode raises an error because no UI or text editor exists. *(demo, high; claude-blender-ai)*
- c5: [3:43] Portable approach: check that space_data exists and is the text editor; if so use the text file path, otherwise fall back to __file__. Works from editor, command line, and add-on. *(demo, high; claude-blender-ai)*
- c6: [4:42] Folder is obtained with pathlib: Path(script_path).resolve().parent; requires importing pathlib.Path. *(demo, high; claude-blender-ai)*
- c7: [5:26] Sibling file path is built by joining the script folder with a filename and converting to str for use in scripts. *(demo, medium; claude-blender-ai)*

## Numbers
- n1: **video length**: 6:16 

## Techniques
- t1: **Dual-path script location**: Check bpy.context.space_data is a Text Editor; if so read space_data.text.filepath. Else use __file__. Then Path(p).resolve().parent for the folder and join a filename.
- t2: **Command-line test**: Run blender -b with --python script.py to verify behavior outside the UI.

## Quotes (brief, for attribution)
> you actually need to go into the space data text and then file path to get this particular file path when you're running from a thin blender  (at 2:21, CG Python)
