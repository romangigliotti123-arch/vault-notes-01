---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-characters.md
title: "elithril/blender-kiln/plugin/references/characters.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/characters.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.1036
relevance: 2
density: high
tags: ["research-source", "github", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# gh-elithril-blender-kiln-f-plugin-references-characters.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender rigging/skinning/animation reference from a Kiln pipeline (bpy scripts, glTF/FBX export; not Roblox-specific). Covers T-pose conversion by arm weights, Rigify via Python, FK/IK trap, Blender 4.4+/5.0 layered action API (no action.fcurves), bone collections, weight limits, rig-density ratio, validation script, and export gotchas relevant to scripted Claude/bpy workflows.

## Claims
- c1: Pre-4.4 snippets using action.fcurves.new fail on current Blender with AttributeError and no hint about slots; use keyframe_insert and walk layers/strips/channelbag to reach F-curves. *(data, high; claude-blender-ai)*
- c2: A Rigify-generated rig ships with IK_FK=0.0 on limb parent bones, so rotating FK controls does nothing silently (0 of 370 vertices moved). Setting IK_FK=1.0 moved 221 of 370. *(data, high; rigging-animation)*
- c3: addon_utils.enable('rigify') is insufficient; generation fails with a misleading 'RigifyParameters has no attribute make_custom_pivot' error. Use bpy.ops.preferences.addon_enable(module='rigify'). *(experience, high; rigging-animation)*
- c4: Generated Rigify human rig: 706 bones, 160 deforming, 23 bone collections (Blender 5.0.1); metarig has 159 bones. *(data, high; rigging-animation)*
- c5: Rigify human on a 370-vertex stylised figure gave 2.3 verts per deform bone, 107 of 160 deform bones influencing nothing, head detached; a 13-bone rig gave 28.5 verts/bone and held volume. Auto weights need roughly 5+ verts per deform bone. *(data, high; rigging-animation)*
- c6: T-pose conversion: build a throwaway rig only for arm weights, rotate vertices about the shoulder scaled by arm weight, then discard the rig. Verify wingspan ≈ height afterward. *(experience, medium; rigging-animation)*
- c7: Failed T-pose approaches: geometric arm vertex selection (pivot landed on skull, -26.8 to -56.3 deg), Euler rotation on bones (roll unknown, wingspan 0.88 m to 0.55 m), and wrong rotation sign (arms to -79.7 deg). *(data, medium; rigging-animation)*
- c8: Free models are not in T-pose: Khronos RiggedFigure A-pose -26.8 deg, CesiumMan -28.2 deg, Blender Human Base Meshes (CC0) I-pose -70.8 deg. *(data, high; rigging-animation)*
- c9: Blender Human Base Meshes bundle (CC0, 48 MB): entries named realistic_body_male are cameras; geometry is under GEO-body_male_realistic. Appended dependencies may land in no collection and need linking to scene.collection.objects. *(experience, medium; other)*
- c10: Rig low-poly meshes welded, not split: split-edge cat (1,856 verts) tore up to 12.5 cm when posed; welding with normals kept (466 verts) gave 0 tear. glTF exporter re-splits where normals differ (466 to 1,875) without bringing back the tear. *(data, medium; rigging-animation)*
- c11: glTF exporter binds unweighted vertices to a synthetic 'neutral_bone' and the file still validates, hiding the defect; automatic weights skip disconnected parts (48 vertices on a villager). Validate weights before export. *(data, high; rigging-animation)*
- c12: glTF export exports all bones as joints by default; pass export_def_bones=True. Rigify human: 865 joints/255 kB became 319 joints/98 kB. *(data, high; rigging-animation)*
- c13: Exporter re-parents a deform bone under a control bone to its nearest deforming ancestor (verified on Blender 5.2.2), so do not re-parent manually. Hyphenated Rigify names (DEF-spine) survive glTF and FBX. *(data, high; rigging-animation)*
- c14: Mobile limits: ~75 bones per draw call, budget 50-65 bones mobile and 150+ desktop; max 4 influences per vertex on mobile, 8 on desktop. Count deform bones only. *(doc, medium; mesh-texture-limits)*
- c15: Blender does not export an explicit FBX bind pose; apply pose as rest pose before export with bpy.ops.pose.armature_apply(selected=False). *(doc, medium; blender-roblox-export-import)*
- c16: Avoid spaces/special characters in bone names and apply armature scale to 1 before rigging to avoid export issues and deformed animation. *(doc, medium; blender-roblox-export-import)*
- c17: Blender 4.0+ replaced bone layers with named Bone Collections (armature.collections.new, collection.assign(bone), is_visible); verified on Blender 5.0.1. *(data, high; rigging-animation)*
- c18: Name animation skeleton bones Mixamo-style (Hips, Spine, LeftUpLeg...) since motion models condition on names; UniMate read 24 of 26 names directly. *(experience, medium; rigging-animation)*
- c19: Joint glossary: Blender IK joint limits are not exported in glTF and only partly in FBX; recreate in target engine. *(doc, low; rigging-animation)*
- c20: Rigid parts (eyes, helmet) parented to bones are dropped by tools reading skin weights; join into the skin at rest pose with 100% weight to the bone. *(experience, medium; rigging-animation)*

## Numbers
- n1: **Rigify human rig bones**: 706 total, 160 deform, 23 collections Blender 5.0.1 generated rig
- n2: **Vertices per deform bone**: 2.3 (Rigify) vs 28.5 (sized rig) 370-vertex stylised figure
- n3: **Vertices moved by FK pose**: 0 vs 221 of 370 IK_FK 0.0 vs 1.0
- n4: **Mobile bone limit**: ~75 per draw call budget 50-65 mobile
- n5: **Max influences per vertex**: 4 mobile, 8 desktop weight limiting
- n6: **glTF joints with/without export_def_bones**: 319 joints/98 kB vs 865/255 kB Rigify human
- n7: **Widest tear**: 12.5 cm vs 0 split vs welded cat mesh, 1,856 vs 466 verts
- n8: **Measured poses**: -26.8, -28.2, -70.8 deg RiggedFigure, CesiumMan, Human Base Mesh

## Techniques
- t1: **T-pose conversion via arm weights**: Build temporary rig, auto-weight, then rotate each vertex about shoulder pivot by -sign*angle*arm_weight around Y; skip weights <0.01; delete rig. Check sign with atan2 arithmetic; verify wingspan ≈ height.
- t2: **Read F-curves in Blender 4.4+**: Insert keyframes with keyframe_insert, then iterate action.layers → layer.strips → action.slots → strip.channelbag(slot).fcurves; set keyframe interpolation LINEAR where sync matters.
- t3: **Rigify from Python**: bpy.ops.preferences.addon_enable(module='rigify'); bpy.ops.object.armature_human_metarig_add(); position metarig on mesh; bpy.ops.pose.rigify_generate(). Set IK_FK=1.0 on limb parent bones to pose FK.
- t4: **Rig density check**: ratio = vertices / count of deform bones; below ~5 use a smaller custom rig (12-20 bones) instead of Rigify human.
- t5: **Place joints on unmodelled mesh**: Take centroid of leg vertices in thin horizontal slices at bend heights (e.g. 22 cm, 9-10 cm, 3 cm on a cat).
- t6: **Pose test for tears**: Bend leg joints, spine, tail ~40°, then compute largest distance between posed vertices that coincide at rest using evaluated depsgraph; expect 0.
- t7: **Auto weights and cleanup**: Select mesh then armature (active), parent_set(type='ARMATURE_AUTO'); check zero-weight vertices, wrong bones, normalize all, limit influences.
- t8: **Pre-export rig validation**: Script checks armature scale, multiple deforming roots, deform bone count, special-character names, >4 influences, unweighted vertices, shape keys with unapplied modifiers.

### Code: Fix Rigify FK so poses apply
```python
for n in ("upper_arm_parent.L", "upper_arm_parent.R",
          "thigh_parent.L", "thigh_parent.R"):
    rig.pose.bones[n]["IK_FK"] = 1.0     # 0 = IK drives, 1 = FK drives
```

### Code: Generate Rigify human rig headlessly
```python
bpy.ops.preferences.addon_enable(module="rigify")
bpy.ops.object.armature_human_metarig_add()   # 159-bone metarig, editable
bpy.ops.pose.rigify_generate()                # -> full control rig
```

### Code: Get F-curves in Blender 4.4+ layered actions
```python
def fcurves(obj):
    action = obj.animation_data.action
    for layer in action.layers:
        for strip in layer.strips:
            for slot in action.slots:
                bag = strip.channelbag(slot)
                if bag:
                    yield from bag.fcurves
```

### Code: Bone collections API
```python
deform_col = armature.collections.new(name="DEF")
bpy.ops.object.mode_set(mode='EDIT')
for bone in armature.edit_bones:
    if bone.name.startswith("DEF_"):
        deform_col.assign(bone)
bpy.ops.object.mode_set(mode='OBJECT')
mech_col.is_visible = False
```

## Quotes (brief, for attribution)
> Every pre-4.4 snippet on the internet uses action.fcurves, and it fails on any current Blender.  (elithril)
> The exporter hides unweighted vertices. It binds them to a synthetic joint named neutral_bone and the file validates.  (elithril)

## Contradictions flagged
- Hyphens in bone names (Rigify DEF-spine) survive glTF and FBX export intact (verified). (vs Its own anti-pattern table advising CamelCase/snake_case to avoid export issues)
- Reference says Blender 4.4+ layered actions while its heading says 'Blender 5.x' for bone collections that date from 4.0. (vs Version labeling within the document)

## Points to
- Khronos glTF sample models RiggedFigure, CesiumMan
- Blender Human Base Meshes (download.blender.org/demo/asset-bundles/human-base-meshes/)
- Mixamo
- Rigify
- AccuRIG
- Auto-Rig Pro
- UniMate
- Quad Remesher
- Instant Meshes
