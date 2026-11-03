---
type: research-source
id: web-8c6c20aee2
title: "Roblox docs: art/modeling/rigging"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/rigging.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# web-8c6c20aee2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc defining rigging and skinning: connecting a mesh to an armature so it bends with bones. Explains bone influence is set in Blender/Maya and saved to MeshPart data, imported as Class.Bone instances, and that bones affect appearance but not collision. Classifies rigs as R1 (single mesh) and R15 (15-mesh humanoid). Links to Blender rig/skin tutorials.

## Claims
- c1: Rigging connects a mesh to an internal bone skeleton; skinning adds natural bend. Rigs can be made in Blender or Maya. *(doc, high; rigging-animation)*
- c2: Bone-to-mesh influence assignment (e.g., LowerLeftArm bone drives LowerLeftArm geometry) is set in the third-party app and saved to Class.MeshPart data on import. *(doc, high; rigging-animation)*
- c3: After import, Studio represents the rig as Class.Bone instances; bones are viewable via Show Constraint Details or the Animation Editor. *(doc, high; rigging-animation)*
- c4: Class.Bone animation changes visual appearance of parts but does not change physical shape used for collision detection. *(doc, high; rigging-animation)*
- c5: R-naming convention: R followed by number of meshes in the model (R1, R6, R15, R20, etc.). *(doc, high; rigging-animation)*
- c6: R1 is a single rigged mesh suited to trees or accessories; R1 NPC humanoids lack full R15 animation and humanoid options. *(doc, high; rigging-animation)*
- c7: R15 is the humanoid avatar standard, 15 meshes parented to one R15 rig; Roblox requires R15 technical specifications for all avatars. *(doc, high; avatar-ugc-accessories)*
- c8: Doc gives no FBX/glTF export settings, scale, or axis guidance; it defers to linked pages for Blender steps. *(doc, high; blender-roblox-export-import)*
- c9: Source does not mention blender-mcp, Claude, or bpy scripting. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **R15 mesh count**: 15 Meshes in an R15 humanoid model parented to one R15 rig
- n2: **Example bone count**: 15 Constraint visualization shows 15 bones over humanoid limbs

## Techniques
- t1: **Rig and skin in Blender**: Create armature in Blender, assign bone influence to mesh parts, then import to Studio; follow linked Rig a simple mesh and Skin a humanoid model guides.

## Quotes (brief, for attribution)
> When imported into Studio, Roblox saves this influence assignment data to the Class.MeshPart asset data.  (create.roblox.com)
> When Class.Bone objects are used in animation, they affect the appearance of the parts but don't change the physical shape  (create.roblox.com)

## Points to
- https://www.blender.org
- https://www.autodesk.com/products/maya/overview
- ../../parts/meshes.md#import-meshes
- ../../animation/editor.md
- ../../avatar/character-bodies/specifications.md
- ../../workspace/collisions.md
