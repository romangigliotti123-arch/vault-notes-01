---
type: research-source
id: yt-sL1qvAKx8SE
title: "Blender Python Tutorial: The REDO Operator [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=sL1qvAKx8SE"
published: "2021-03-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai"]
---
# yt-sL1qvAKx8SE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender Python tutorial (Darkfall, 2021) showing how to add a redo (undo/REGISTER) option to a custom bpy operator so properties can be edited on the fly in the Adjust Last Operation panel. Covers bl_options = {'REGISTER', 'UNDO'}, a bpy.props.FloatVectorProperty named location, and using self.location in execute. Not about Roblox, MCP, or Claude; relevance to the stated topic is low.

## Claims
- c1: [0:05] Adding bl_options = {'REGISTER', 'UNDO'} to a custom bpy operator makes its properties editable in the redo (Adjust Last Operation) panel. *(demo, high; claude-blender-ai)*
- c2: [2:40] Operator properties are declared as bpy.props.FloatVectorProperty and read via self.location inside execute. *(demo, high; claude-blender-ai)*
- c3: [3:21] Pop-up dialog operators (invoke_props_dialog style) are a separate technique the author covers in another video; not shown here. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **default location value in demo**: (1, 1) 

## Techniques
- t1: **Enable redo panel on a bpy operator**: Set bl_options = {'REGISTER', 'UNDO'} on the operator class. Declare the input as a bpy.props.FloatVectorProperty. Read self.location in execute() and apply it to the created object. Changes appear in the redo panel after each run.

### Code: Enable redo panel and declare a vector property on a custom operator
```python
bl_options = {'REGISTER', 'UNDO'}

location: bpy.props.FloatVectorProperty(...)

# in execute:
self.location
```

## Quotes (brief, for attribution)
> we just need to go to this bl information and then type bl underscore options  (at 1:57, Darkfall)
