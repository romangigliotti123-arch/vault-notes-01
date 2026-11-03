---
type: research-source
id: web-f690baf738
title: "Roblox docs: parts/materials"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/parts/materials.md"
published: ""
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.1057
relevance: 1
density: low
tags: ["research-source", "web", "automation-and-creator-workflows", "mesh-texture-limits"]
---
# web-f690baf738

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs page on Parts materials: base materials, custom MaterialVariant in MaterialService, overrides, adaptive materials, physical properties, base material texture asset IDs. Only tangentially relevant to Blender export; it distinguishes MaterialVariant (tileable) from SurfaceAppearance (UV-mapped mesh PBR). No Blender, Claude, or import content.

## Claims
- c1: MaterialVariant and SurfaceAppearance both use PBR textures. MaterialVariant is for reusable tileable materials; SurfaceAppearance is for a specific UV-mapped mesh. Only MaterialVariant has physical properties. *(doc, high; mesh-texture-limits)*
- c2: For custom material texture maps (Color, Normal, etc.), square textures work best. Unspecified maps stay blank. Studs Per Tile and Pattern control tiling. *(doc, high; mesh-texture-limits)*
- c3: Renaming a MaterialVariant after applying it breaks the link on parts, because parts reference the variant by name. This enables adaptive materials: same-named variants in MaterialService restyle reused models. *(doc, high; automation-and-creator-workflows)*
- c4: When distributing a model with custom materials to the Creator Store, include the MaterialVariant instances. When inserting such a model, copy them to MaterialService. Packages using custom materials must be placed in MaterialService. *(doc, high; automation-and-creator-workflows)*
- c5: Physical property priority, highest to lowest: part CustomPhysicalProperties, part's custom material, material override of the part's material, default base material properties. *(doc, high; mesh-texture-limits)*
- c6: Base material shaders differ from the MaterialVariant shader, so custom materials can't look identical to base materials, though base textures can be reused via their asset IDs. *(doc, high; mesh-texture-limits)*
- c7: Glass refraction is not supported on mobile. ForceField, Neon, Plastic and SmoothPlastic textures are bundled with Studio and have no asset IDs. *(doc, high; mesh-texture-limits)*
- c8: Opinion/recommendation in docs: use PascalCase MaterialVariant names starting with the base material, e.g. GrassWet, GrassDry, GrassBurned. *(doc, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Default part material**: Plastic Default Enum.Material for new Part instances
- n2: **Asphalt ColorMap asset ID**: 9930003046 Current base material texture; example of listed IDs
- n3: **Default Plastic RGB**: [163,162,165] Default color for Plastic, Carpet, Neon, ForceField

## Techniques
- t1: **Create a custom material in Material Manager**: Pick a base material for physical properties, click Create Material Variant, rename it, paste asset IDs or import textures for each map, adjust Studs Per Tile and Pattern. The result is a MaterialVariant in MaterialService.
- t2: **Set a material override**: Select the custom material in Material Manager, enable Overrides > Set as Override. It then replaces textures and physics for all parts and terrain using that base material in the place. TerrainDetail can customize top, side and bottom faces.

## Points to
- Material Generator (create.roblox.com studio/material-generator)
- SurfaceAppearance docs (art/modeling/surface-appearance)
- Custom terrain materials
- Creator Store Materials category
- MaterialService
