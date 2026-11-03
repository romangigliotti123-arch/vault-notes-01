---
type: research-source
id: yt-t3YWMAJURIw
title: "Time Saving Blender Python Workflow"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=t3YWMAJURIw"
published: "2023-07-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 2
density: medium
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai"]
---
# yt-t3YWMAJURIw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video (9:19) shows a VS Code + Blender Development extension add-on that auto-runs a bpy script on save, avoiding command palette. Covers setup (__init__.py folder, script name/path, no-arg reload function), a scene-reset helper, and appending objects from a .blend file for iteration. No Roblox, MCP, or export content.

## Claims
- c1: [0:00] Creator wrote a Blender add-on that watches a script file and reloads/runs it in Blender on every save, avoiding the command palette. Targets VS Code Blender development extension workflow. *(demo, high; claude-blender-ai)*
- c2: [1:18] Add-on config has three settings: script name, script path (default: next to init.py), and optional function name to call on reload; function must take no arguments. *(demo, high; claude-blender-ai)*
- c3: [5:25] Scene-clean helper deletes current scene, creates new scene and world, and purges orphan data before each run, so iterations don't accumulate clutter. *(demo, high; claude-blender-ai)*
- c4: [6:41] Loading objects from an external .blend file via append (not link) lets the script modify imported objects; a separate linked-library removal helper is used first. *(demo, medium; automation-and-creator-workflows)*
- c5: [8:03] Script errors (e.g. missing import) do not crash Blender or the add-on; the error is shown and the next save re-runs the fixed script. *(demo, high; claude-blender-ai)*

## Numbers
- n1: **Iteration example**: Cube Z location set to 4, then 6 across saves 
- n2: **Scale example**: icosphere scale by 2 

## Techniques
- t1: **Save-triggered script reload**: Create package folder with __init__.py containing add-on code; place target script next to it; start Blender from VS Code extension; edit and save to auto-run.
- t2: **Clean scene per run**: Call scene-reset function (delete scene, new scene+world, purge orphans) before the iterated code.
- t3: **Iterate on existing .blend content**: Build path to .blend with pathlib, append objects from it (not linked), then modify them by name via bpy.data.objects.

### Code: Iterate on newly added cube by fetching active object and setting Z location
```python
obj = bpy.context.active_object
obj.location.z = 4
```

### Code: Scale an object from appended data by name
```python
ico_object = bpy.data.objects['Icosphere']
ico_object.scale = (2, 2, 2)
```

## Quotes (brief, for attribution)
> The add-on just watches my script and as soon as I save, it reloads it and runs it in Blender, removing any need for me to run from the command palette.  (at 0:00, CG Python)

## Points to
- Blender Development VS Code extension
- CG Python add-on (linked in video description)
