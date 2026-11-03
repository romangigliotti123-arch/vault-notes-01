---
type: research-source
id: web-e85f27e0c7
title: "Roblox docs: art/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0651
relevance: 2
density: low
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-e85f27e0c7

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Index/landing page for Roblox 3D art docs. It has no technical detail itself, only links to the relevant pages: Blender and Maya FBX export settings, general mesh specs, texture and SurfaceAppearance PBR pages, the Studio Importer, rigging and skinning, avatar accessory specs, and downloadable add-ons and tools. It says nothing about Claude, blender-mcp or bpy.

## Claims
- c1: Roblox documents Blender and Maya .FBX export settings on a dedicated page (art/modeling/export-requirements.md), listed under technical specs. *(doc, high; blender-roblox-export-import)*
- c2: Mesh and texture limits are documented in modeling/specifications.md (general mesh), modeling/texture-specifications.md (texturing requirements) and modeling/surface-appearance.md (PBR textures). This page gives no values. *(doc, high; mesh-texture-limits)*
- c3: Rigging pages: modeling/rigging.md (overview), modeling/rig-a-simple-mesh.md, avatar character-bodies specifications#rigging (avatar rig requirements), and avatar/automatic-skinning-transfer.md. Animation export is covered only for Maya (export-avatar-animations-from-maya.md). *(doc, high; rigging-animation)*
- c4: Separate spec pages exist for rigid accessories, layered accessories and avatar character bodies. The Accessory Fitting Tool, Marketplace policy, publish-to-marketplace and fees pages are also linked. *(doc, high; avatar-ugc-accessories)*
- c5: Studio tools listed for artists: Importer, Accessory Fitting Tool, Animation Editor, Animation Capture, Avatar Setup, Material Generator, Terrain Editor, Texture Generator, Toolbox and Asset Manager. *(doc, high; automation-and-creator-workflows)*
- c6: modeling/project-files.md hosts downloadable example models, reference avatar items, and an 'add-ons and tools' section. The Blender-related add-ons are probably there, but this page does not name them. *(doc, medium; blender-roblox-export-import)*
- c7: A staff DevForum article describes using alpha masks in PBR color maps to tint base colors, saving time and improving performance. *(doc, medium; mesh-texture-limits)*

## Points to
- art/modeling/export-requirements.md (Blender and Maya FBX export settings)
- art/modeling/specifications.md
- art/modeling/texture-specifications.md
- art/modeling/surface-appearance.md
- art/modeling/rigging.md
- art/modeling/project-files.md#add-ons-and-tools
- studio/importer.md
- art/overview-dcc.md (third-party software overview)
- avatar/rigid-accessories/specifications.md and avatar/layered-accessories/specifications.md
- devforum.roblox.com/t/using-alpha-masks-in-color-maps-to-customizetint-base-colors/2883381
