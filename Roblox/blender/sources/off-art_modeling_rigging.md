---
type: research-source
id: off-art_modeling_rigging
title: "Roblox Creator Docs: art_modeling_rigging"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/rigging"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# off-art_modeling_rigging

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs introduction to rigging and skinning: meshes get internal bone rigs with per-bone influence set in Blender/Maya, stored in MeshPart on import as Class.Bone instances. Covers R-naming convention (R1 single mesh, R15 humanoid avatars). Bones affect appearance, not collision. Links to Blender rig/skin tutorials. Thin on Blender-specific steps or the Claude/bpy workflow.

## Claims
- c1: Rigging connects a mesh to an internal skeleton; skinning sets bone influence weights so meshes bend naturally. Rig/skin data is saved to Class.MeshPart on import into Studio. *(doc, high; blender-roblox-export-import)*
- c2: Bone-to-mesh influence assignment (e.g., LowerLeftArm bone driving LowerLeftArm geometry) is set in third-party software like Blender or Maya, not in Studio. *(doc, high; blender-roblox-export-import)*
- c3: Imported rigs appear in Studio as Class.Bone instances; bones can be viewed via View > Show Constraint Details or the Animation Editor. *(doc, high; rigging-animation)*
- c4: Bone objects affect visual appearance only; they do not change physical shape used for collision detection. *(doc, high; rigging-animation)*
- c5: R1 = single rigged mesh (e.g., tree, accessory); NPC humanoids can be R1 but lose full humanoid/animation options available to R15. *(doc, high; rigging-animation)*
- c6: R15 = 15 specific meshes parented to one R15 rig, typically humanoid avatars; Roblox uses R15 for all avatars and requires its technical specifications. *(doc, high; avatar-ugc-accessories)*
- c7: Rig naming convention: 'R' followed by number of meshes in the model (R6, R15, R20, R200 examples). *(doc, medium; rigging-animation)*

## Numbers
- n1: **R15 mesh count**: 15 meshes parented to a single R15 rig
- n2: **Bones in example humanoid**: 15 pink bone objects shown over limbs in Animation Editor figure

## Techniques
- t1: **Rig then skin in Blender**: Create armature in Blender, rig mesh to bones, then skin (assign vertex weights) so bones drive corresponding geometry; import rigged model into Studio.
- t2: **Verify bones in Studio**: After import, enable View > Show Constraint Details or open Animation Editor to inspect Class.Bone instances.

## Quotes (brief, for attribution)
> The assignment of influence between meshes and bones, such as a LowerLeftArm bone driving the movement of the LowerLeftArm geometry, is set in a third-party application like Blender or Maya.  (create.roblox.com)
> When Class.Bone objects are used in animation, they affect the appearance of the parts but don't change the physical shape in cases such as collision detection.  (create.roblox.com)

## Points to
- https://www.blender.org
- https://www.autodesk.com/products/maya/overview
- ../../art/modeling/rig-a-simple-mesh.md
- ../../art/modeling/skin-a-simple-mesh.md
- ../../art/modeling/rig-a-humanoid-model.md
- ../../art/modeling/skin-a-humanoid-model.md
- ../../parts/meshes.md#import-meshes
- ../../animation/editor.md
- ../../avatar/character-bodies/specifications.md
