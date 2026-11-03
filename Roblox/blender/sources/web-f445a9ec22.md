---
type: research-source
id: web-f445a9ec22
title: "Blender manual: advanced/scripting/introduction"
source_type: "web"
creator: "docs.blender.org"
url: "https://projects.blender.org/blender/blender-manual/raw/branch/main/manual/advanced/scripting/introduction.rst"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 2
density: low
tags: ["research-source", "web", "bpy-scripting-headless", "other"]
---
# web-f445a9ec22

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender manual intro to Python scripting: Python is the scripting language, the bpy API covers most of Blender (animation, rendering, import/export, object creation). Lists API docs and quickstart links, script types (add-ons, modules, presets, startup, custom scripts), script folder locations, and add-on installation via Preferences. No Roblox, MCP or export-specific content.

## Claims
- c1: Blender Python API docs at docs.blender.org/api/current are the official reference for writing scripts; a quickstart page is provided. *(doc, high; bpy-scripting-headless)*
- c2: Most areas of Blender can be scripted, including animation, rendering, import and export, object creation and repetitive tasks. *(doc, high; bpy-scripting-headless)*
- c3: Custom scripts are typically intended for one-time execution via the Text Editor, unlike add-ons which are persistent extensions. *(doc, high; bpy-scripting-headless)*
- c4: Scripts are loaded from the 'scripts' folder in local, system and user paths; extra script search paths can be set in Preferences > File Paths. *(doc, high; bpy-scripting-headless)*
- c5: Add-ons are installed in Preferences via Install... by selecting a .zip file and enabled from Preferences. *(doc, high; bpy-scripting-headless)*
- c6: Blender Extensions platform (extensions.blender.org) hosts community add-ons that are not part of official releases and not guaranteed stable. *(doc, high; other)*

## Techniques
- t1: **Run one-off script in Text Editor**: Write Python in Blender's Text Editor and execute it once; use Python Console or Info Editor for interactive checks.
- t2: **Package script as add-on**: Bundle script as add-on, zip it, install through Preferences > Install, then enable it.

## Points to
- https://docs.blender.org/api/current/
- https://docs.blender.org/api/current/info_quickstart.html
- https://extensions.blender.org/
- https://developer.blender.org/docs/handbook/addons/guidelines/
- https://blenderartists.org/c/coding/python-support
