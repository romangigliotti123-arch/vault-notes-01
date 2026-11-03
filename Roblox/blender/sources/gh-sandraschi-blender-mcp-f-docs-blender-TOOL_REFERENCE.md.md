---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-TOOL_REFERENCE.md
title: "sandraschi/blender-mcp/docs/blender/TOOL_REFERENCE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/TOOL_REFERENCE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0873
relevance: 2
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-TOOL_REFERENCE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Tool reference for sandraschi's blender-mcp server: 41 "portmanteau" tools, each taking an `operation` parameter. Focus is VRChat/Resonite/Unity/VRM avatars, not Roblox. Covers rigging, animation, shape keys, material baking/atlasing, export presets and validation. Some tools (validation, atlasing, humanoid bone mapping, weight transfer, FBX export presets) are loosely transferable to a Roblox pipeline, but no Roblox presets exist.

## Claims
- c1: blender-mcp (sandraschi) exposes 41 portmanteau tools; each tool takes an `operation` string plus parameters, e.g. blender_rigging(operation='list_bones', ...). This differs from one-tool-per-action designs. *(doc, high; claude-blender-ai)*
- c2: Tool groups: animation, rigging, VR avatar (validation, splatting, material baking, VRM metadata, atlasing, shapekeys, export presets), scene, materials, mesh, transform, lighting, camera, physics, particles, modifiers, textures/UV, selection, render, import/export, furniture, VSE, utilities. *(doc, high; claude-blender-ai)*
- c3: The doc lists no generic execute-python/bpy tool. Capabilities are fixed operations, so unlisted tasks (e.g. Roblox-specific export) would need a new operation. *(opinion, low; claude-blender-ai)*
- c4: blender_export_presets offers VRCHAT (Unity scale 1.0, FBX, 256 bones max), RESONITE (GLTF, 512 bones), UNITY, and LEGACY_VRCHAT (0.01 scale for old workflows). No Roblox preset exists. *(doc, high; blender-roblox-export-import)*
- c5: Export flow: validate_export_preset on target objects, then export_with_preset with output_path, include_materials and apply_modifiers options. *(doc, high; blender-roblox-export-import)*
- c6: blender_import handles FBX, OBJ, glTF, STL, PLY and VRM through import_[format]. blender_export has only export_unity and export_vrchat. *(doc, medium; blender-roblox-export-import)*
- c7: blender_validation.validate_avatar checks polycount, bones, materials and transforms against platform limits: VRChat 70k tris/256 bones/8 materials; Resonite 100k tris/512 bones; Unity mobile 32k tris recommended. *(doc, high; mesh-texture-limits)*
- c8: Material tools: convert_vrm_shader_to_pbr and bake_toon_to_pbr (resolution param, e.g. 2048), consolidate_materials with max_atlas_size 2048, and create_material_atlas with atlas_size 2048. *(doc, high; mesh-texture-limits)*
- c9: optimize_draw_calls merges materials (example max_materials=4) for mobile VR. blender_uv offers unwrap, smart_project, cube_project, cylinder_project and reset_uvs. blender_modifiers has add_decimate to reduce polygons. *(doc, medium; mesh-texture-limits)*
- c10: blender_splatting.generate_collision_mesh builds walkable collision geometry from Gaussian splats (density_threshold=0.1). It targets Resonite, not Roblox. *(doc, medium; mesh-texture-limits)*
- c11: blender_rigging has 12 operations: create_armature, add_bone, create_bone_ik, create_basic_rig (simple biped), list_bones, pose_bone, set_bone_keyframe, reset_pose, transfer_weights, manage_vertex_groups, humanoid_mapping. *(doc, high; rigging-animation)*
- c12: transfer_weights copies vertex weights from a body mesh to a clothing mesh. This is useful for layered-clothing-style workflows, though the doc is about VRChat. *(doc, medium; rigging-animation)*
- c13: humanoid_mapping applies VRChat/Unity humanoid bone names with a preset (mapping_preset or humanoid_preset='VRCHAT'). No R15 preset is documented. The two parameter names are inconsistent between examples. *(doc, medium; rigging-animation)*
- c14: blender_animation has 21 operations: keyframes, shape keys, actions, push_to_nla, interpolation (CONSTANT, LINEAR, BEZIER, BOUNCE, ELASTIC), easing, constraints, bake_action and bake_all_actions (NLA to a single action). Baking before export is the workflow shown. *(doc, high; rigging-animation)*
- c15: VRM shape-key tools: create_viseme_shapekeys (A, I, U, E, O), create_blink_shapekey, set_viseme_weights, create_facial_expression, analyze_shapekeys (VRM compliance). Roblox facial animation is not addressed. *(doc, medium; avatar-ugc-accessories)*
- c16: blender_vrm_metadata sets first-person offset (example offset_z=0.15; doc says VRChat standard is 0.1-0.2m), blink/viseme mappings, spring bones (stiffness, gravity_power), look-at, and JSON metadata export. These are VRM-specific and not applicable to Roblox. *(doc, medium; avatar-ugc-accessories)*
- c17: The doc's full workflow is a 7-phase script: import and validate, material optimization, VRM metadata, facial setup, rigging/weights, animation and bake, then export validation and export. It could be a template for a Roblox pipeline: validate, then bake, then export FBX. *(doc, medium; automation-and-creator-workflows)*
- c18: Other tools: blender_vse (20 ops, renders H264 video), blender_download (asset download from URLs), blender_addons, blender_view_logs/blender_log_stats, and blender_status for health checks. *(doc, medium; automation-and-creator-workflows)*

## Numbers
- n1: **portmanteau tools**: 41 total tools in Blender-MCP server
- n2: **VRChat limits**: 70k tris, 256 bones, 8 materials validate_avatar platform limits
- n3: **Resonite limits**: 100k tris, 512 bones validate_avatar platform limits
- n4: **Unity mobile recommended tris**: 32k validate_avatar platform limits
- n5: **atlas/bake resolution in examples**: 2048 bake, consolidate and atlas examples
- n6: **LEGACY_VRCHAT export scale**: 0.01 old FBX workflows; VRCHAT preset uses 1.0
- n7: **blender_animation operations**: 21 keyframes, shape keys, NLA, baking
- n8: **blender_rigging operations**: 12 listed table shows 11 rows

## Techniques
- t1: **Validate then export with preset**: Run blender_export_presets validate_export_preset with target_objects and platform, then export_with_preset with output_path, include_materials=True and apply_modifiers=True. A Roblox preset would need to be added as a custom preset (create_custom_preset).
- t2: **Clothing weight transfer**: Call blender_rigging transfer_weights with source_mesh (Body), target_mesh (Clothing) and armature_name, so the clothing mesh inherits the body's skin weights.
- t3: **Bake before export**: Set frame range, pose bones with pose_bone and set_bone_keyframe, set interpolation to BEZIER, then bake_action over start_frame to end_frame so constraints become keyframes.
- t4: **Material reduction for draw calls**: Convert toon shaders with convert_vrm_shader_to_pbr (resolution 2048), consolidate_materials into an atlas (max_atlas_size 2048), then optimize_draw_calls with a max_materials limit.
- t5: **Create custom preset for a new target**: Use blender_export_presets create_custom_preset to define a platform configuration. The doc gives no parameters for it.

### Code: Validate then export an avatar with a platform preset
```python
blender_export_presets(operation="validate_export_preset", target_objects=["Avatar"], platform="VRCHAT")
blender_export_presets(
    operation="export_with_preset", target_objects=["Avatar"], platform="VRCHAT", output_path="//avatar_vrchat.fbx"
)
```

### Code: Transfer weights from body to clothing
```python
blender_rigging(operation="transfer_weights", source_mesh="Body", target_mesh="Clothing", armature_name="Armature")
```

### Code: Pre-flight platform validation
```python
blender_validation(operation="validate_avatar", target_platform="VRCHAT")
```

### Code: Bake animation for export
```python
blender_animation(operation="bake_action", object_name="Armature", start_frame=1, end_frame=120)
```

## Contradictions flagged
- The heading says 41 tools and blender_rigging says 12 operations, but its table lists 11 rows. blender_furniture says 9 operations but lists 8, so counts are approximate. (vs the document itself)

## Points to
- https://github.com/sandraschi/blender-mcp
- VRChat
- Resonite
- Unity
- VRM / MToon
- Gaussian Splatting (3DGS)
