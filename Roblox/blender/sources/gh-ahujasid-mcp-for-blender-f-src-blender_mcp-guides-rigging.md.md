---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-rigging.md
title: "ahujasid/mcp-for-blender/src/blender_mcp/guides/rigging.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/src/blender_mcp/guides/rigging.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0317
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "rigging-animation"]
---
# gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-rigging.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Rigging guide bundled with a Blender MCP server: prep mesh (applied transforms, face -Y, merge doubles), Rigify for humanoids, hand-built armatures via bpy, rigid bone parenting for mechanical props, auto-weights with bone-heat failure fixes, and verification via MCP tools (get_scene_info weights, look). No Roblox-specific content.

## Claims
- c1: Before rigging: apply scale and rotation, place mesh at origin on ground, face -Y (Blender front); Rigify and auto-weights assume this. *(doc, high; rigging-animation)*
- c2: Merge duplicate vertices (bmesh.ops.remove_doubles) and remove loose parts; generated meshes often have many disconnected islands, which makes automatic weights fail. *(doc, high; rigging-animation)*
- c3: Characters rig best in A-pose or T-pose with slight bend at elbows and knees. *(doc, medium; rigging-animation)*
- c4: Rigify: generate with metarig active via bpy.ops.pose.rigify_generate(); skin to the generated rig (named 'rig' or 'RIG-<name>'), not the metarig. *(doc, high; rigging-animation)*
- c5: bpy.ops.object.armature_human_metarig_add() needs a 3D viewport context override, so it is awkward in background mode. *(doc, medium; bpy-scripting-headless)*
- c6: Mechanical objects (doors, wheels, robots) usually need no skinning; parent rigid parts to bones with parent_type BONE, which never deforms badly. *(doc, high; rigging-animation)*
- c7: Bone Heat Weighting failure fixes: merge by distance and remove interior faces; or skin a voxel-remeshed copy and transfer weights via Data Transfer modifier (vertex groups, nearest face interpolated); or scale up 10x, skin, scale back. *(doc, high; rigging-animation)*
- c8: The MCP exposes get_scene_info(fields=['weights'], query=...) reporting vertices no deform bone moves and deform bones without vertex groups; both should be zero for a skinned character. *(doc, high; claude-blender-mcp)*
- c9: The MCP look tool (mode='angles', shading='xray', views, target) lets the model visually check bone alignment and posed deformation at elbows, shoulders, knees, hips. *(doc, high; claude-blender-mcp)*
- c10: Verify by posing a bone (e.g. upper_arm_fk.L rotation_euler.x=1.2), inspect for collapsing/stretching, then reset all pose bones' matrix_basis to identity. *(doc, high; rigging-animation)*

## Numbers
- n1: **scale factor for heat-weighting workaround**: 10x scale up, skin, scale back for tiny-scale meshes

## Techniques
- t1: **Rigify humanoid rig**: Enable rigify via addon_utils, add human metarig, fit edit bones to mesh joints, check with xray front/right views, run rigify_generate, skin to generated rig.
- t2: **Auto-weights with fallback**: Select mesh, make armature active, parent_set(type='ARMATURE_AUTO'); on failure clean mesh, use voxel-remeshed proxy with Data Transfer, or scale 10x.
- t3: **Rigid bone parenting**: Set part.parent=rig, parent_type='BONE', parent_bone=name for mechanical props instead of skinning.
- t4: **Weight and pose verification via MCP**: Run get_scene_info weights query, pose a bone, view with look(mode='angles'), then reset pose.

### Code: Build simple armature in edit mode
```python
arm_data = bpy.data.armatures.new("Rig"); rig = bpy.data.objects.new("Rig", arm_data)
bpy.context.scene.collection.objects.link(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode="EDIT")
root = arm_data.edit_bones.new("root"); root.head = (0, 0, 0); root.tail = (0, 0.3, 0)
b = arm_data.edit_bones.new("arm"); b.head = (0, 0, 1); b.tail = (0, 0, 2); b.parent = root
bpy.ops.object.mode_set(mode="OBJECT")
```

### Code: Automatic weights skinning
```python
bpy.ops.object.parent_set(type="ARMATURE_AUTO")   # needs selection + active set
```

### Code: Enable Rigify and add human metarig
```python
import addon_utils
addon_utils.enable("rigify", default_set=True)
bpy.ops.object.armature_human_metarig_add()
metarig = bpy.context.active_object
```

## Points to
- Rigify (Blender bundled addon)
- ahujasid/blender-mcp
