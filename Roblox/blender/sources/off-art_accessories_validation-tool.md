---
type: research-source
id: off-art_accessories_validation-tool
title: "Roblox Creator Docs: art_accessories_validation-tool"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/accessories/validation-tool"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0031
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai"]
---
# off-art_accessories_validation-tool

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page for the Layered Accessory Validation Tool, a Blender 3.0 / Maya 2022 add-on that checks layered accessories before export to Studio. Explains installation, the Check Assets workflow, and eight checks with auto-fix behavior. Does not cover blender-mcp, bpy, Claude, or general FBX/glTF pipeline settings.

## Claims
- c1: Roblox's Layered Accessory Validation Tool is a supplemental add-on for Blender (designed for Blender 3.0) or Maya 2022 that checks common layered accessory issues before export. *(doc, high; blender-roblox-export-import)*
- c2: Blender install: download ValidationTool_Blender.zip, Edit > Preferences > Add-Ons > Install..., select zip, enable 'Validation Tool', then expand the viewport sidebar to use it. *(doc, high; blender-roblox-export-import)*
- c3: Usage: select the object, open the tool, click Check Assets. Failed checks turn red in Blender (yellow in Maya); some have an auto-fix button. *(doc, high; blender-roblox-export-import)*
- c4: Transforms check requires geometry location, rotation and scale frozen to 0,0,0; auto-fix freezes transforms but may change the rig. *(doc, high; blender-roblox-export-import)*
- c5: Validation tool checks: Layers, Transforms, Unused Material (orphan data), Keyframes, Attachment Points (naming and parenting), Intersection (inner/outer cage), Texture Format (resolution). *(doc, high; avatar-ugc-accessories)*
- c6: Intersection check in Blender switches to Edit Mode and highlights intersecting vertices; edges around sleeve, neck and torso holes are expected and can be ignored. *(doc, high; avatar-ugc-accessories)*
- c7: The tool does not comprehensively verify layered accessories; the model must still meet general mesh specs and layered accessory specs before importing into Studio. *(doc, high; automation-and-creator-workflows)*
- c8: Maya install requires Python 3.0+ with PATH enabled; run install.bat (Windows) or install.command (Mac, chmod 777 if needed), enter Maya version, then import ValidationTool in Script Editor. *(doc, medium; automation-and-creator-workflows)*
- c9: The source does not mention blender-mcp, bpy scripting, or Claude; it covers only the manual validation add-on. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Blender version target**: 3.0 
- n2: **Maya version target**: 2022 (Python 3.0+ required) 
- n3: **Transform values required**: 0,0,0 (location, rotation, scale frozen) 

## Techniques
- t1: **Run Validation Tool before export**: Install add-on, select accessory object, click Check Assets, fix red items via auto-fix or manually, then re-check before export.
- t2: **Intersection review in Edit Mode**: Click Intersection check to enter Edit Mode and inspect highlighted vertices; ignore sleeve, neck, torso hole edges.

## Points to
- https://www.blender.org/download/releases/3-0/
- https://www.autodesk.com/products/maya/overview
- https://www.python.org/downloads/
