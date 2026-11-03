---
type: research-source
id: yt-Kgqmu1NgdvY
title: "Blender Python Tutorial : Read an Error Message and how to Fix it [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=Kgqmu1NgdvY"
published: "2020-09-15"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes"]
---
# yt-Kgqmu1NgdvY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender 2.90 scripting tutorial on reading a Python traceback from an add-on (Shader Library). The error came from an icon enum renamed in 2.90 (FORCE_SMOKEFLOW not found). Fix: open the script at the traceback line (F3 > "Edit Source") and change the icon name. Not about Claude, MCP, Roblox, or export. Only tangential to bpy debugging.

## Claims
- c1: [1:06] Blender 2.9 Info window shows the add-on traceback with a red X; the traceback line number (line 167) points to the failing script line. *(demo, high; bpy-scripting-headless)*
- c2: [1:32] To open the script at the error line, press F3 (spacebar in the author's setup), search 'edit source', and run it. *(demo, high; bpy-scripting-headless)*
- c3: [1:50] TypeError 'UILayout.operator() error with keyword argument icon' means the icon enum value (FORCE_SMOKEFLOW) is not in Blender 2.9's icon list; the icon was renamed or removed between versions. *(demo, high; common-mistakes-fixes)*
- c4: [2:31] Fix was changing icon='FORCE_SMOKEFLOW' to a valid icon (QUESTION); the menu then rendered. Author advises checking all icon names in the add-on for similar errors after a version change. *(demo, high; common-mistakes-fixes)*
- c5: [2:31] Author's general advice: read the traceback from the bottom (exception type and message) and locate the line number; simple errors like this are fixed by a one-word change. *(opinion, medium; bpy-scripting-headless)*

## Numbers
- n1: **Video length**: 3:05 
- n2: **Traceback line number**: 167 
- n3: **Blender version**: 2.90 (video titled 2.9) 

## Techniques
- t1: **Jump from traceback to source**: Read the traceback in the Info editor, note the file and line number, press F3, search 'Edit Source' to open the add-on text in the Text Editor, go to that line.
- t2: **Fix renamed icon enum**: Read the TypeError: the keyword value not found in the enum list is named. Replace it with a valid icon identifier and rerun the script.

### Code: Failing line from the traceback (Blender 2.90 Shader Library add-on); the icon enum no longer exists
```python
row.operator('shader.cloud_operator', icon='FORCE_SMOKEFLOW', text="Clouds")
```

## Quotes (brief, for attribution)
> force underscore smoke flow is no longer being used so if we change this to say question  (at 2:03, Darkfall)
> By reading the error messages we can get a clear understanding of what the problem is  (at 2:31, Darkfall)

## Points to
- Shader Library add-on (free Blender add-on; author's blog linked in video description, no URL given)

## Visual notes
Contact sheet shows Blender 2.90 Scripting workspace, Info editor red-X traceback with 'Edit Source' text editor showing line 167 'row.operator('shader.cloud_operator', icon='FORCE_SMOKEFLOW', text="Clouds")' and a Stylized panel in the sidebar.
