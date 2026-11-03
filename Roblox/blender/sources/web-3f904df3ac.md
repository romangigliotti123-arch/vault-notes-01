---
type: research-source
id: web-3f904df3ac
title: "Roblox docs: art/modeling/calisthenics-tool"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/calisthenics-tool.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# web-3f904df3ac

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for the Calisthenics Tool, a legacy Blender add-on (Blender 3.0+) that plays generic animation cycles on standard R15 rigs to check skinning, previews rigid test accessories, and exports FBX. Tool is no longer actively maintained. Source has no content on Claude, blender-mcp, or bpy scripting.

## Claims
- c1: Calisthenics Tool is a Blender add-on that runs test animation cycles (Walk, Run, Move, Idle) on a standard R15 armature to verify skinning; you can pause and fix weights with Weight Paint. *(doc, high; rigging-animation)*
- c2: Tool is designed for Blender 3.0+. Roblox marks it as no longer in active development and possibly out of date or incompatible with modern assets. *(doc, high; rigging-animation)*
- c3: Attach Test Accessory buttons add Normal Size or Slender Size rigid reference accessories to attachment points; Detach removes them. Misplaced accessories are fixed by repositioning the Attachment object in the armature. *(doc, high; avatar-ugc-accessories)*
- c4: Export Model button writes Character_Model_Export.fbx to a chosen folder, clearing test animations and accessories and applying Roblox export settings automatically. *(doc, high; blender-roblox-export-import)*
- c5: Manual FBX export requires detaching test accessories, pressing Stop Animation, returning the model to default pose, and matching Roblox Blender export settings. *(doc, high; blender-roblox-export-import)*
- c6: Tool does not verify all skinning issues; models must still meet Studio character body specs and layered accessory specs. Facial FACS data may conflict with reference animations on export. *(doc, high; rigging-animation)*
- c7: Source does not mention blender-mcp, Claude, or bpy scripting; coverage of the requested AI/MCP topic is absent. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Minimum Blender version**: 3.0+ Calisthenics Tool plugin design target

## Techniques
- t1: **Skinning test loop**: Import FBX, hide armature/cages/attachments, set Armature via Eyedropper in Outliner, play Walk/Run/Move/Idle, pause on bad frames, fix in Weight Paint, then export.

## Points to
- https://github.com/Roblox/avatar/tree/main/Tools/CalisthenicsTool
- Layered Accessory Validation Tool
- Skin a humanoid model
- Roblox Blender export settings (export-requirements.md)
- standard R15 character body specifications
