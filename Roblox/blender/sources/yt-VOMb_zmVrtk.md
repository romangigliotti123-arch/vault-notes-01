---
type: research-source
id: yt-VOMb_zmVrtk
title: "Package your Python Helper Script as a Blender Add-on"
source_type: "youtube"
creator: "CG Python"
url: "https://www.youtube.com/watch?v=VOMb_zmVrtk"
published: "2023-10-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-VOMb_zmVrtk

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tutorial on wrapping the single-file easy_bpy Python utility as a Blender add-on via an added __init__.py (bl_info, register/unregister, sys.path insert), zipped and installed through preferences. Mentions pip-packaged bpy_building_blocks alternative. Not about Roblox, blender-mcp, Claude, or FBX export; only tangentially relevant to bpy scripting.

## Claims
- c1: [0:00] Video covers packaging a single-file Python utility (Curtis Holt's easy_bpy) as a Blender add-on so others can install it instead of copying into scripts folder. *(demo, high; other)*
- c2: [1:23] Add-on wrapper __init__.py is under 40 lines; defines bl_info dict plus register/unregister; appends add-on folder to sys.path so scripts can import the module. *(demo, high; other)*
- c3: [2:03] Packaging method: put all repo files including __init__.py into a zip and install via Edit > Preferences > Add-ons > Install, then enable. *(demo, high; other)*
- c4: [2:43] Without the add-on enabled, running a script that imports easy_bpy fails with a missing module error. *(demo, high; other)*
- c5: [4:06] Author says the add-on-wrapper approach suits quick sharing among friends/colleagues but not shipping utility code inside a production add-on; opinion. *(opinion, medium; other)*
- c6: [3:24] Packages can be wrapped too: a multi-module bpy_building_blocks package is distributed via pip or as an add-on. *(demo, medium; other)*

## Numbers
- n1: **add-on init file length**: under 40 lines 

## Techniques
- t1: **Wrap Python module as Blender add-on**: Add __init__.py with bl_info; in register() append add-on dir to sys.path; zip folder; install and enable in preferences; scripts then import module directly.

## Points to
- github.com/Curtis-Holt easy_bpy repo (fork used)
