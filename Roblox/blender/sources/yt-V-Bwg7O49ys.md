---
type: research-source
id: yt-V-Bwg7O49ys
title: "Blender Python Tutorial : Property Subtypes and Password Protection [learn python for beginners]"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=V-Bwg7O49ys"
published: "2020-08-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: medium
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-V-Bwg7O49ys

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Python tutorial (2020) on bpy.props subtypes. Shows how a subtype argument changes a float vector's UI (COLOR_GAMMA, TRANSLATION, VELOCITY) and a string's UI (PASSWORD hides text). Demonstrates a password-gated operator that adds a cube. Does not cover Claude, blender-mcp, Roblox, or export pipelines.

## Claims
- c1: [0:35] Subtype argument on bpy.props float vector changes its UI, e.g. subtype='COLOR_GAMMA' gives a color input; 'TRANSLATION' shows X/Y/Z labels; 'VELOCITY' shows meters per second. *(demo, high; claude-blender-ai)*
- c2: [4:48] String property subtypes listed: FILE_PATH, DIR_PATH, FILE_NAME, BYTE_STRING, PASSWORD. PASSWORD hides entered text in the panel. *(demo, high; claude-blender-ai)*
- c3: [3:04] Finding subtypes: type bpy.props.float_vector_property in Python console and use Ctrl+Space autocomplete to read argument docs. *(demo, medium; claude-blender-ai)*
- c4: [6:11] Password gate pattern: operator uses an if-check on the stored string property and only runs bpy.ops.mesh.primitive_cube_add when it matches. *(demo, medium; claude-blender-ai)*
- c5: [6:52] Tutorial states the password logic is basic and hardcoded in the operator; it is not real security. *(opinion, medium; other)*

## Numbers
- n1: **float vector subtype examples**: COLOR_GAMMA, TRANSLATION, VELOCITY, DIRECTION, ACCELERATION 

## Techniques
- t1: **Subtype switching for property UI**: Pass subtype='COLOR_GAMMA' (or other) to bpy.props.FloatVectorProperty; re-run script; panel shows the new widget.
- t2: **Password field**: Add subtype='PASSWORD' to StringProperty; entered text is masked. Compare value in operator execute() with if-statement before acting.

### Code: Password-gated operator pattern from tutorial
```python
if my_tool.my_string == "awesome password":
    bpy.ops.mesh.primitive_cube_add()
```

## Quotes (brief, for attribution)
> now to add another we just want to go to the end just hit comma and then give it a subtype subtype equals password  (at 5:31, Darkfall)
