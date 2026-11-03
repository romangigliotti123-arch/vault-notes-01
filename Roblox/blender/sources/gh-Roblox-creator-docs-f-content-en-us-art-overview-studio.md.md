---
type: research-source
id: gh-Roblox-creator-docs-f-content-en-us-art-overview-studio.md
title: "Roblox/creator-docs/content/en-us/art/overview-studio.md"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/creator-docs/blob/HEAD/content/en-us/art/overview-studio.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: low
tags: ["research-source", "github", "avatar-ugc-accessories", "creator-workflows", "roblox-import-pipeline", "roblox-mesh-limits", "texturing-baking-uv"]
---
# gh-Roblox-creator-docs-f-content-en-us-art-overview-studio.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs overview of Studio 3D art tools: interface panels, assets vs packages, Creator Store, Marketplace, basic parts vs mesh parts, materials and textures, terrain and lighting. Only briefly touches Blender/Maya as external modeling tools. Contains no Blender MCP, bpy, export-setting, or UV/bake specifics.

## Claims
- c1: Custom meshes are created in third-party tools like Blender or Maya, then the model file is imported into Studio and represented as a MeshPart. *(doc, high; roblox-import-pipeline)*
- c2: Textures are 2D images applied to a surface; they can be imported as image files or baked into an imported custom 3D object; they never affect physical properties. *(doc, high; texturing-baking-uv)*
- c3: Roblox has two texture types: single-image basic textures and advanced PBR textures that react to lighting. *(doc, high; texturing-baking-uv)*
- c4: Loading many unique PBR texture sets at once can hurt performance; reuse one PBR set and vary tint via alpha channel masks multiplied with mesh base colours. *(doc, high; roblox-mesh-limits)*
- c5: Basic parts are native, performant, work with native physics, and are suited to greyboxing or prototyping; mixing parts with custom meshes is common. *(doc, medium; creator-workflows)*
- c6: Studio includes a Texture Generator (natural-language prompt, creates textures for a mesh) and a Material Generator (prompt-generated custom materials). *(doc, high; creator-workflows)*
- c7: Roblox recommends most developers work with packages (equivalent to Unity Prefabs) so changes propagate to all copies. *(doc, medium; creator-workflows)*
- c8: Selling avatar assets on the Marketplace requires following specific avatar specifications and policies; details are in the Avatar and Marketplace docs. *(doc, high; avatar-ugc-accessories)*

## Techniques
- t1: **Model in Blender/Maya, import as MeshPart**: Create mesh in third-party app, import model file into Studio; Studio exposes it as Class.MeshPart. Doc gives no export settings.

## Quotes (brief, for attribution)
> Loading many unique PBR textures at once can affect performance in your game.  (Roblox)

## Points to
- https://create.roblox.com/store/
- https://devforum.roblox.com/t/using-alpha-masks-in-color-maps-to-customizetint-base-colors
- ../art/modeling/index.md
- ../art/modeling/surface-appearance.md
- ../studio/texture-generator.md
