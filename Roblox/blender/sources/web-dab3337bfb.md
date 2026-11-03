---
type: research-source
id: web-dab3337bfb
title: "Roblox docs: art/characters/facial-animation/create-basic-heads"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/facial-animation/create-basic-heads.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0897
relevance: 3
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# web-dab3337bfb

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox tutorial for building a basic dynamic (animatable) head in Blender 5.2 using the Cubie reference: add RootFaceJoint and eye/eyelid joints, skin, build controllers, pose FACS on timeline frames, map frames via custom properties, export FBX for Studio. No Claude/MCP/bpy content.

## Claims
- c1: Dynamic head needs a RootFaceJoint parented under the R15 head joint; it must parent all other face joints. Commonly named DynamicHead, but any name works if mapped in custom properties. *(doc, high; avatar-ugc-accessories)*
- c2: Head modeling requirements: distinct eyes, upper/lower teeth, tongue; separated lip vertices; mouth bag and eye bag for inner parts; no history or frozen transforms on Head_Geo children; outer cage for face and layered accessories. *(doc, high; avatar-ugc-accessories)*
- c3: Studio requires no specific hierarchy for face joints (unlike the body rig), but the rig must include RootFaceJoint. Use fewer than 50 face joints where possible; high vertex and joint counts hurt performance. *(doc, high; rigging-animation)*
- c4: Of 50 base FACS poses, only a specific 17 are required to sell a dynamic head on the Marketplace. *(doc, high; avatar-ugc-accessories)*
- c5: Frame 0 must be the neutral pose; FACS poses start at Frame 1, one pose per frame. Studio computes joint differences from neutral. Set timeline Start to 0 and End to the last pose frame. *(doc, high; rigging-animation)*
- c6: Import fails if poses are unmapped, any mapping string is empty, or multiple frames share one FACS pose name. *(doc, high; avatar-ugc-accessories)*
- c7: FACS pose names are relative to the character, not the camera: LeftEyeClosed closes the character's left eye, on the right of the camera view. *(doc, high; rigging-animation)*
- c8: Combination (corrective) poses combine 2-3 base FACS poses affecting the same region, e.g. LeftEyeClosed with LeftCheekRaiser, to avoid eyelid collision at 100%. Studio stores the corrective difference in FaceControls on import. *(doc, high; rigging-animation)*
- c9: Enable Auto Normalize when painting detailed or shared influences. Automatic Weights may leave pre-existing influences, so test them. *(doc, medium; rigging-animation)*
- c10: Reference Cubie-Eye-Poses-Mapped.blend must be imported with Animation Offset 0 so Frame 0 is included on the timeline. *(doc, medium; blender-roblox-export-import)*
- c11: Cubie head texture (Cubie_Head_ALB.png) is applied separately as the head part's TextureID after FBX import. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **base FACS poses**: 50 standard dynamic head base pose set
- n2: **required FACS poses for Marketplace**: 17 specific subset needed to sell a dynamic head
- n3: **recommended face joint cap**: <50 use fewer than 50 face joints where possible
- n4: **Cubie-Complete facial joints**: 30+ reference rig, over 50 poses mapped
- n5: **eyelid joints**: 8 4 duplicates of the 2 eye joints; inner/outer, upper/lower, left/right
- n6: **eye joint Tail Z offset**: 0.2 cm Tail Z set relative to Head Z; Tail Y copied from Head Y
- n7: **Blender version**: 5.2 version used in the tutorial

## Techniques
- t1: **Add RootFaceJoint**: Select armature, Edit mode, select Head bone, press E to extrude a child, rename to DynamicHead, then map it as the RootFaceJoint custom property on Head_Geo.
- t2: **Eye joints**: Add > Single Bone twice, name LeftEye/RightEye, enable X-Axis symmetry, center on irises, copy Head Y to Tail Y, set Tail Z offset 0.2 cm, then Parent > Make > With Offset to DynamicHead.
- t3: **Eyelid joints by duplication**: Select both eye bones, Shift+D four times for 8 new joints, position at eye corners with symmetry, and rename to {Left|Right}{Upper|Lower}{Outer|Inner}Eyelid.
- t4: **Weight paint skinning**: Select armature then Head_Geo, enter Weight Paint, enable Wireframe, Shift+Ctrl-click a bone, and paint so pupils are fully red. Test in Pose mode. Repeat per joint.
- t5: **Controller armature**: Duplicate armature as Controller, delete non-face bones, batch rename with suffix _Con (Edit > Batch Rename, Bones, Set Name, Suffix). On original bones add Copy Location and Copy Rotation targeting Controller/X_Con. For Copy Rotation, disable XYZ axes, enable Inverted XYZ, and set Mix to Offset (Legacy).
- t6: **Save FACS poses**: Set the frame (0 neutral, 1 EyesLookLeft, 2 EyesLookRight, 3 LeftEyeClosed, 4 RightEyeClosed), pose the controllers to maximum, press A in Pose mode, right-click > Insert Keyframe with Keying Set > Location and Rotation.
- t7: **Map poses with custom properties**: Select Head_Geo, Object Properties > Custom Properties > New, gear icon, Type String, name FrameN or RootFaceJoint. Value is the exact FACS name, or DynamicHead for the root. Combination poses join names with underscores, e.g. Funneler_JawDrop_Pucker. Maya uses Extra Attributes.
- t8: **Export FBX for Studio**: Select all objects, File > Export > FBX. Under Include: Limit To Selected Objects and Custom Properties on. Armature: Add Leaf Bones off. Animation on, with NLA Strips, All Actions and Force Start/End Keyframes off. Then import in Studio.

## Quotes (brief, for attribution)
> If you don't map your poses, leave any empty strings, or try to import the head into Studio with multiple frames per FACS pose name, the head will fail the import process.  (create.roblox.com)

## Points to
- https://www.blender.org/download/releases/5-2/
- avatar/dynamic-heads/facs-poses-reference
- avatar/dynamic-heads/specifications#facs-poses
- avatar/character-bodies/specifications
- avatar/dynamic-heads/test (Test heads in Studio)
- art/modeling/skin-a-simple-mesh (Auto Normalize)
- Cubie reference files (.blend, .fbx, .ma)
