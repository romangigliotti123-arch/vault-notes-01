---
type: research-source
id: web-e5ba39a76e
title: "Roblox docs: avatar/character-bodies/import"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/character-bodies/import.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# web-e5ba39a76e

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc on importing rigged character bodies (.fbx/.gltf) via Studio Importer: Rig General settings (Custom Humanoid optional, Rig Scale = body scale, Constraint Type = Joint Upgrade), texture fallback via Asset Manager and SurfaceAppearance PBR mapping, Avatar Setup for splitting single mesh into 15 parts, and playtest via StarterCharacter. Does not cover Blender or Claude.

## Claims
- c1: Roblox Studio Importer (Home tab > Import) accepts character body .fbx or .gltf files and creates a Model object in the workspace. *(doc, high; blender-roblox-export-import)*
- c2: In the Importer's Rig General section: set Rig Type to Custom Humanoid only for advanced R15 rigs (optional), set Rig Scale to the character's Body Scale, and set Constraint Type to Joint Upgrade. *(doc, high; blender-roblox-export-import)*
- c3: If textures fail to load on import, they can be uploaded via Asset Manager and assigned manually; PBR needs a SurfaceAppearance child with ColorMap=_ALB, MetalnessMap=_MTL, NormalMap=_NOR, RoughnessMap=_RGH. *(doc, high; mesh-texture-limits)*
- c4: Single basic texture is applied via MeshPart.TextureID; PBR uses SurfaceAppearance. Asset Manager upload requires publishing the game first if Asset Manager is inaccessible. *(doc, high; mesh-texture-limits)*
- c5: A single-mesh FBX/glTF can be partitioned into the 15 body parts needed for an avatar character body using the Avatar Setup tool. *(doc, high; avatar-ugc-accessories)*
- c6: Advanced R15 rigs may need HumanoidRigDescription and/or DigitsRigDescription objects, and the Adaptive Animation plugin can remap joints and set a baseline T-pose. *(doc, medium; rigging-animation)*
- c7: To playtest the imported character, rename the Model to StarterCharacter and move it into StarterPlayer in Explorer. *(doc, high; automation-and-creator-workflows)*
- c8: Importer checks general 3D requirements, but the model must also meet character body specifications separately or errors appear later in the workflow. *(doc, high; avatar-ugc-accessories)*
- c9: Source does not mention Blender, blender-mcp, Claude, or bpy scripting; no workflow info on these topics. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **body parts**: 15 Avatar Setup partitions single mesh into 15 body parts
- n2: **Rig Type for advanced rig**: Custom Humanoid Optional, for advanced R15 rig
- n3: **Constraint Type**: Joint Upgrade Required setting in Rig General

## Techniques
- t1: **Importer rig setup**: Import FBX/glTF; set Rig Scale to body scale; set Constraint Type to Joint Upgrade; optionally Custom Humanoid for advanced R15; click Import.
- t2: **Manual PBR texture assignment**: Upload images in Asset Manager; select MeshPart; add SurfaceAppearance; assign ALB, MTL, NOR, RGH to ColorMap, MetalnessMap, NormalMap, RoughnessMap.
- t3: **Playtest as character**: Rename imported Model to StarterCharacter and move into StarterPlayer in Explorer.

## Quotes (brief, for attribution)
> Set Constraint Type to Joint Upgrade.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/avatar-setup/
- https://create.roblox.com/docs/characters/adaptive-animation
- https://create.roblox.com/docs/projects/assets/manager
- https://create.roblox.com/docs/avatar/character-bodies/test
