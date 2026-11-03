---
type: research-source
id: web-fe779baf8a
title: "Roblox docs: avatar/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0597
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "rigging-animation"]
---
# web-fe779baf8a

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Overview page of Roblox avatar anatomy: body geometry (15 MeshParts), rigging armature (15 joints, up to 37 extra), animations, attachments/cages, and wearables (makeup, rigid, layered, classic). Points to Avatar Setup, Blender/Maya/FBX project files, and a Blender layered-clothing tutorial. No Claude/blender-mcp/bpy content and no export settings.

## Claims
- c1: Avatar body geometry is 15 separate mesh parts: head, upper/lower torso, and per side upper arm, lower arm, hand, upper leg, lower leg, foot. In Studio they are MeshParts under one Model. *(doc, high; avatar-ugc-accessories)*
- c2: Standard avatar rigs need 15 poseable joints. Advanced R15 rigs add up to 37 optional joints for hands, shoulders and spine. Joints must follow a specific hierarchy and naming convention. In Studio they are Bone objects connecting MeshParts. *(doc, high; rigging-animation)*
- c3: Avatar Setup automatically generates a Marketplace-ready rig, attachment points and cage meshes if the geometry lacks them. It also generates FACS poses, facial rigging, skinning and animation data for facial animation. *(doc, high; avatar-ugc-accessories)*
- c4: Downloadable Blender, Maya and .fbx project files provide standard attachment points and cage meshes for humanoid bodies. The page also lists base rigs, mannequins for sizing, and character templates. *(doc, high; avatar-ugc-accessories)*
- c5: Studio class mapping: cage meshes are WrapTarget, attachment points are Attachment, rigid accessories are Accessory, and layered accessories are Accessory with a child WrapLayer. Classic clothing uses Shirt, Pants and ShirtGraphic. Makeup is layered textures baked into a Decal. *(doc, high; avatar-ugc-accessories)*
- c6: Emotes are Animation objects whose AnimationId is the animation asset ID. FACS values map to a dynamic head's FaceControls. Tools: Animation Editor, Animation Capture, Face Animation Editor, Adaptive Animation. *(doc, high; rigging-animation)*
- c7: Roblox provides a step-by-step tutorial for creating a Studio-ready layered t-shirt in Blender. The Accessory Fitting Tool in Studio tests accessories on multiple bodies, animations and accessory combinations. *(doc, high; avatar-ugc-accessories)*
- c8: Classic clothing is the simplest item type to sell, needing only an image editor and browser. The linked video tutorial uses GIMP. *(doc, high; avatar-ugc-accessories)*

## Numbers
- n1: **body mesh parts**: 15 separate MeshParts making up avatar body
- n2: **standard rig joints**: 15 required poseable joints
- n3: **optional advanced R15 joints**: up to 37 hands, shoulders, spine

## Techniques
- t1: **Use Avatar Setup for missing components**: Run Avatar Setup on custom 3D geometry to auto-generate rig, attachments, cage meshes, and FACS/facial data for Marketplace-ready avatar assets.

## Points to
- Avatar Setup (avatar-setup/index.md)
- avatar/character-bodies/specifications.md
- avatar/resources.md (project files, mannequins, templates)
- art/accessories/creating/index.md (Blender layered t-shirt)
- art/accessories/rig-and-cage-existing-models.md
- Accessory Fitting Tool
- art/characters/creating/modeling-best-practices.md
- GIMP classic clothing video
