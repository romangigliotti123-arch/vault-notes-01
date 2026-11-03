---
type: research-source
id: web-f8432c1fc1
title: "Roblox docs: avatar/create"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/create.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: low
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# web-f8432c1fc1

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs overview of avatar asset creation. Lists third-party tools (Blender, Maya, GIMP) and Studio tools: Importer, Avatar Setup, Automatic Skinning Transfer, Accessory Fitting Tool, Animation Editor, Adaptive Animation, plus in-experience avatar creation and Photo-to-Avatar. Blender is named only as a free option; no Blender-specific workflow, settings, or limits.

## Claims
- c1: Blender is listed as a free, open-source 3D suite and an example third-party tool for creating avatar asset files that are imported into Studio. *(doc, high; blender-roblox-export-import)*
- c2: Studio's Importer supports meshes for avatar items with PBR textures, rigging, skinning, and animation data. *(doc, high; blender-roblox-export-import)*
- c3: Avatar Setup auto-generates missing components (geometry partitions, rig armatures, skinning weights, cages, facial animations, attachments) when a model lacks them for Marketplace publishing. *(doc, high; avatar-ugc-accessories)*
- c4: Automatic Skinning Transfer generates skinning for layered accessories and facial rigid accessories so creators need not skin the accessory itself. *(doc, high; rigging-animation)*
- c5: Accessory Fitting Tool tests custom models across body, animation and accessory combinations before generating the final Accessory object. *(doc, high; avatar-ugc-accessories)*
- c6: Adaptive Animation maps internal joints of custom characters for animation support across different body types, rigs and proportions. *(doc, high; rigging-animation)*
- c7: Animation Editor lets creators import, design and publish custom emotes for their rigging armatures. *(doc, high; automation-and-creator-workflows)*

## Points to
- https://www.blender.org/
- https://www.autodesk.com/products/maya/overview
- https://www.gimp.org/
- ../studio/importer.md
- ../avatar-setup/index.md
- ../avatar/automatic-skinning-transfer.md
- ../avatar/accessory-fitting-tool.md
- ../animation/editor.md
- ../characters/adaptive-animation.md
- ../avatar/in-experience-creation.md
