---
type: research-source
id: yt-TgQ9ahMuDMw
title: "Blender Python Tutorial : How to Display Info Messages [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=TgQ9ahMuDMw"
published: "2020-12-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless"]
---
# yt-TgQ9ahMuDMw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Blender Python tutorial (2020) on showing messages to the user via self.report() inside a bpy.types.Operator, with info/warning/error levels, and displaying an int property via bpy.props.IntProperty in the report text. Does not cover Claude, blender-mcp, or Roblox export; relevance to the topic is low.

## Claims
- c1: [0:12] Operator messages shown in the status bar/info window via self.report({'INFO'}, message); 'WARNING' and 'ERROR' change the icon, ERROR pops up a message box. *(demo, high; bpy-scripting-headless)*
- c2: [3:04] IntProperty values can be interpolated into a report string with Python % formatting, e.g. message = "special number is %i" % self.int. *(demo, high; bpy-scripting-headless)*

## Numbers
- n1: **IntProperty default**: 10 Example int property default used in report message

## Techniques
- t1: **Operator self.report for user messages**: Inside an Operator's execute(), call self.report({'INFO'}, 'text'); swap INFO for WARNING or ERROR to change icon and display. Run script, then press panel button to see message in status bar/info log.
- t2: **Display property value in report**: Define int = bpy.props.IntProperty(default=10) on the operator, build string with % formatting, pass to self.report({'INFO'}, message).

### Code: Report a message from an operator (Blender 2.8+ style)
```python
self.report({'INFO'}, 'your message')
# or
self.report({'WARNING'}, 'your message')
self.report({'ERROR'}, 'your message')
```

### Code: Show an integer property in the report text
```python
int: bpy.props.IntProperty(default=10)
message = "the special number is %i" % self.int
self.report({'INFO'}, message)
```

## Quotes (brief, for attribution)
> this actually pops up so we hit this button we can see it pops up with this error message  (at 2:22, Darkfall)
