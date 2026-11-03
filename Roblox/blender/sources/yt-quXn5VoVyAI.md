---
type: research-source
id: yt-quXn5VoVyAI
title: "Create a Simple Rig UI with Blender Python"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=quXn5VoVyAI"
published: "2024-07-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless"]
---
# yt-quXn5VoVyAI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tutorial (Blender 4.1, Victor Stepanoff) on writing a custom Rigify-style sidebar panel for an armature with Python. Covers a bpy.types.Panel with a rig-ID poll, bone-collection toggle and solo buttons, icon viewer lookup, and f-string IDs. Does not cover Roblox, Claude, blender-mcp, or export.

## Claims
- c1: [0:00] Rig UI panels in Blender 4.1 are bpy.types.Panel classes that show only when the active object has a custom property matching a rig ID; Rigify uses this to scope its layers panel. *(demo, high; bpy-scripting-headless)*
- c2: [10:43] Bone collection visibility can be toggled from the Python console by running the same command shown in the info log, editing True/False in the command history. *(demo, high; bpy-scripting-headless)*
- c3: [16:16] Icons for buttons are found via the Icon Viewer add-on (Develop category), which shows icon names such as the solo star, then passed as the icon= keyword with empty text. *(demo, high; bpy-scripting-headless)*
- c4: [19:03] Panel IDs should be built with an f-string including the rig ID so multiple rigs can each have their own panel without ID clashes. *(opinion, medium; bpy-scripting-headless)*
- c5: [23:35] Presenter says hand-copying one button block per bone collection becomes repetitive; a looped/compact version is offered only in an email-list extended video. *(opinion, low; bpy-scripting-headless)*

## Numbers
- n1: **Blender version**: 4.1 
- n2: **Video length**: 24:29 

## Techniques
- t1: **Poll-based panel scoping**: In poll(), check context.active_object custom property for rig ID inside try/except; return False on error so panel hides for other objects.
- t2: **Console command capture**: Copy the property-change command from the Info editor, run it in the Python console, edit True/False in history to test visibility toggles, then reuse in code.
- t3: **Toggle button via prop()**: Use row.prop(armature.collections[name], 'is_visible', text=...) with toggle=True to make a toggle button bound to a bone collection.

### Code: Panel skeleton scoped by rig ID, as described in the video (rig ID string is copied from Rigify's generated code).
```python
import bpy

class MY_PT_rig_ui(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_label = 'My Rig UI'
    bl_idname = 'VIEW3D_PT_my_rig_ui'

    @classmethod
    def poll(cls, context):
        try:
            return context.active_object.data['my_rig_ID']
        except (AttributeError, KeyError, TypeError):
            return False

    def draw(self, context):
        pass
```

## Quotes (brief, for attribution)
> creating your own basic rig UI with python is not that hard  (at 0:00, CG Python)

## Points to
- Rigify add-on
- Blender Icon Viewer add-on (Develop category)
