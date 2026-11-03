---
type: research-source
id: web-ad826ab7cf
title: "Roblox docs: art/characters/validation-tool"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/validation-tool.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# web-ad826ab7cf

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox's official doc for the Avatar Validation Tool, a Blender add-on that runs pre-export checks on character models against Roblox avatar specs. The doc marks the tool as no longer in active development and possibly out of date. It requires Blender 3.5.1+, lists 14 checks (layers, transforms, UV 0-1, joint positions, FACS, polygons, textures, etc.), and says it does not replace testing in Studio.

## Claims
- c1: Validation Tool add-on requires Blender 3.5.1+; earlier versions may behave unexpectedly. *(doc, high; blender-roblox-export-import)*
- c2: Tool is no longer in active development and may be out of date or incompatible with modern Roblox assets. *(doc, high; blender-roblox-export-import)*
- c3: Install via Edit > Preferences > Add-Ons > Install, select ValidationTool_Blender.zip without opening it, enable, then use sidebar in Viewport. *(doc, high; blender-roblox-export-import)*
- c4: Target Armature field is set via eyedropper by selecting the armature object (often named Joints or Armature); Run All Checks runs every check. *(doc, high; rigging-animation)*
- c5: Joint Positions check requires Root and HumanoidRootNode bones, Root at 0,0,0 world space, and correct Left/Right axes. *(doc, high; rigging-animation)*
- c6: FACS check requires Neutral Pose mapped, Head_Geo custom properties, corrective poses use existing base poses and no more than 3 base poses. *(doc, high; rigging-animation)*
- c7: Keyframes check flags non-face keyframes; auto-fix removes them but facial keyframes must be kept. *(doc, medium; rigging-animation)*
- c8: Attachment Points check requires parenting to armature and correct naming; auto-fix parents unexpected points. *(doc, high; avatar-ugc-accessories)*
- c9: Intersection check flags overlaps between character geometry and cage mesh, switching to Edit mode to highlight them. *(doc, high; avatar-ugc-accessories)*
- c10: Transforms check requires location, rotation, scale frozen (0,0,0); auto-fix may change the rig. *(doc, high; mesh-texture-limits)*
- c11: UV check requires body geometry UVs within 0-1 range; no auto-fix, must be fixed manually. *(doc, high; mesh-texture-limits)*
- c12: Polygon Data check covers watertight meshes, polycount budgets, no N-gons, non-manifold, and no vertex color data. *(doc, high; mesh-texture-limits)*
- c13: Texture Format check validates resolution against requirements and lets users select an external image file. *(doc, medium; mesh-texture-limits)*
- c14: Asset Size check verifies total character and per-part size bounds; must be resized manually. *(doc, high; mesh-texture-limits)*
- c15: Layers check removes extra scene layers via auto-fix; Unused Data check removes orphan data and unused materials. *(doc, medium; avatar-ugc-accessories)*
- c16: Cage UV Modifications check auto-fixes cage UV coordinates; if it fails, use a new template cage. *(doc, medium; avatar-ugc-accessories)*
- c17: Head Joint Names check flags duplicate head bone names including Blender .001/.002 suffixes. *(doc, high; rigging-animation)*
- c18: Tool is a manual-check add-on; the doc does not mention Claude, blender-mcp, or bpy scripting. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Minimum Blender version**: 3.5.1+ Earlier versions may behave unexpectedly
- n2: **Max base poses per corrective pose (FACS)**: 3 Corrective poses must not use more than 3 base poses
- n3: **UV range**: 0-1 Body geometry UVs
- n4: **Transform target**: 0,0,0 Location, rotation, scale frozen

## Techniques
- t1: **Pre-export validation run**: Install add-on, set Target Armature via eyedropper, click Run All Checks, fix red items, use auto-fix where offered, then verify manually and test in Studio.

## Quotes (brief, for attribution)
> This tool is no longer in active development. You are free to use the tool for any purpose.  (create.roblox.com)

## Points to
- https://github.com/Roblox/avatar/tree/main/Tools/ClothingValidationTool
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/avatar/character-bodies/test-studio
