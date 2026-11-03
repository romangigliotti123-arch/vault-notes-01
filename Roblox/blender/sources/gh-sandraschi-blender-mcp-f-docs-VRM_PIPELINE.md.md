---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-VRM_PIPELINE.md
title: "sandraschi/blender-mcp/docs/VRM_PIPELINE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/VRM_PIPELINE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# gh-sandraschi-blender-mcp-f-docs-VRM_PIPELINE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Fleet-internal doc on blender-mcp's VRM pipeline: avatar-mcp to blender-mcp validate/re-export, MMD PMX to VRM steps, and Godot GLB and Unity/VRChat side paths. It has no Roblox Studio, Roblox export settings, bpy-for-Roblox, or Roblox asset pipeline content, so it is largely off-topic.

## Claims
- c1: blender-mcp is described as the 3D post-processor for VRM: import, inspect, metadata, re-export, and conversion hub, including MMD PMX sources. *(doc, high; claude-blender-ai)*
- c2: avatar-mcp calls blender-mcp via BLENDER_MCP_URL, default http://127.0.0.1:10849. *(doc, high; claude-blender-ai)*
- c3: Validation and re-export run via blender_validate and reexport tools using headless script_execute. *(doc, medium; claude-blender-ai)*
- c4: Doc points to docs/blender/TOOL_REFERENCE.md for VRM addon operations, blender_vrm_metadata, shape keys, rigging, and glTF/VRM/FBX export. *(doc, medium; claude-blender-ai)*
- c5: Source has no Roblox-specific content; Roblox Studio import/export steps are absent. Its export targets are VRM, Godot (GLB), and Unity/VRChat. *(doc, high; blender-roblox-export-import)*
- c6: For Godot, export GLB from Blender with the same rig, then import via godot-mcp godot_import_glb; godot-mcp does not import VRM directly. *(doc, high; blender-roblox-export-import)*
- c7: MMD path: import PMX via MMD tools addon, fix scale/materials/bone names, export VRM via VRM addon, then stage with avatar-mcp hub_stage_file. *(doc, high; avatar-ugc-accessories)*
- c8: VMD motions are not native to avatar-mcp; must be retargeted/baked in Blender. apple-test plays Resources/Animations/*.json humanoid quaternions; VRMA path deferred to VRMMetalKit. *(doc, medium; rigging-animation)*
- c9: Unity/VRChat path uses unity3d-mcp plus VRChat SDK after blender-mcp validation, separate from Godot path. *(doc, medium; automation-and-creator-workflows)*

## Numbers
- n1: **BLENDER_MCP_URL default port**: http://127.0.0.1:10849 

## Techniques
- t1: **MMD PMX to VRM conversion**: Import PMX with MMD tools addon; fix scale, materials, bone names; export VRM with VRM addon; stage via avatar-mcp hub_stage_file.
- t2: **Headless validate/re-export**: Run blender_validate and reexport through headless script_execute in blender-mcp, returning cleaned .vrm to avatar-mcp output.

## Quotes (brief, for attribution)
> blender-mcp is the 3D post-processor for VRM in the fleet: import, inspect, metadata, re-export, and conversion hub (including MMD PMX sources).  (sandraschi)

## Points to
- github.com/sandraschi/blender-mcp
- docs/blender/TOOL_REFERENCE.md
- godot-mcp/docs/AVATARS_AND_VRM.md
- mcp-central-docs/docs/avatars/MMD_EXPLAINER.md
- mcp-central-docs/docs/avatars/FLEET_VRM_PIPELINE.md
- unity3d-mcp
- VRChat SDK
- VRMMetalKit
