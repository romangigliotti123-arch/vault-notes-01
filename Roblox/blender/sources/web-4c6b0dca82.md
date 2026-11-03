---
type: research-source
id: web-4c6b0dca82
title: "Roblox docs: avatar/character-bodies/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/character-bodies/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# web-4c6b0dca82

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on avatar character bodies. Covers the four layers (body parts, rigging, face data, cage/attachments), the 15 body-part meshes, 16+ bone minimum rig, up to 37 extra advanced R15 joints, 19 attachment points, and the requirement to start cage meshes from Roblox's project files. Says to export all components in one .fbx or .gltf from Blender or Maya. Little on bpy or MCP.

## Claims
- c1: An avatar body is built from 15 separate MeshPart body-part meshes (head, upper/lower torso, arms, hands, legs, feet) nested under one Model. *(doc, high; avatar-ugc-accessories)*
- c2: Rigging armature needs at least 16 bones (one per body part plus a root); higher-fidelity rigs add up to 37 optional bones. *(doc, high; rigging-animation)*
- c3: Standard R15 rigs require 15 poseable joints; advanced R15 adds optional joints for hands, shoulders and spine. *(doc, high; rigging-animation)*
- c4: Each avatar must include 19 attachment points, which are imported as Attachment objects with standardized names. *(doc, high; avatar-ugc-accessories)*
- c5: Cage objects must exist for all 15 body parts; outer cages are WrapTarget instances. Adding or removing vertices from the standard cage can break clothing fit and import. *(doc, high; avatar-ugc-accessories)*
- c6: Caging a custom (non-template) body should start from Roblox's body cage project files to keep the standard cage mesh. *(doc, high; avatar-ugc-accessories)*
- c7: All avatar components should be exported together in a single .fbx or .gltf file for import into Studio, from Blender or Maya. *(doc, high; blender-roblox-export-import)*
- c8: Imported character bodies are processed with the Avatar Setup tool in Studio before they can be sold on the Marketplace. *(doc, high; avatar-ugc-accessories)*
- c9: Textures are applied either via a child SurfaceAppearance object or the MeshPart TextureID property; a modesty layer is required over sensitive regions. *(doc, high; mesh-texture-limits)*
- c10: Facial animation is held in a FaceControls instance; each face pose is a keyframe on the animation timeline mapped to a pose name in the Head_Geo custom properties. *(doc, medium; rigging-animation)*
- c11: The doc does not mention blender-mcp, Claude, bpy scripting, or any Blender automation; it only names Blender as a modeling tool. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **body part meshes**: 15 separate MeshPart body parts per avatar
- n2: **minimum bones**: 16 one per body part plus root
- n3: **extra optional bones (advanced R15)**: 37 for hands, shoulders, spine on higher-fidelity rigs
- n4: **attachment points**: 19 required per avatar character
- n5: **cage objects**: 15 one per body part

## Techniques
- t1: **Single-file avatar export**: Model all avatar components in Blender or Maya, then export together as one .fbx or .gltf and import into Studio. Use Roblox's R15 Rig and Attachments and body cage project files as the starting base.

## Quotes (brief, for attribution)
> When designing a character body in Blender or Maya, you must export all of the avatar components in a single .fbx or .gltf for import into Studio.  (create.roblox.com)
> Removing or adding vertices from this standard mesh can cause issues with clothing fit and import.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/avatar/resources
- https://create.roblox.com/docs/art/characters/creating
- https://www.blender.org/
