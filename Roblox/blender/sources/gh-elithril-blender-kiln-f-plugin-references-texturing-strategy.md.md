---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-texturing-strategy.md
title: "elithril/blender-kiln/plugin/references/texturing-strategy.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/texturing-strategy.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0516
relevance: 3
density: high
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-texturing-strategy.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
A blender-mcp-based texturing playbook (glTF-oriented, not Roblox-specific): classify faces via execute_blender_code, label zones with viewport screenshots, apply PolyHaven textures through addon tools, procedural Principled BSDF recipes, glTF export compatibility of properties and maps, and a Cycles bake helper. Useful for Claude+Blender workflow patterns and PBR map loss; Roblox specifics are absent.

## Claims
- c1: For PolyHaven textures, use the addon's download_polyhaven_asset and set_texture tools rather than hand-building node graphs; hand-written ShaderNodeTexImage chains get colorspaces wrong more often than not. Fall back only if set_texture fails. *(experience, medium; claude-blender-ai)*
- c2: Workflow: color-coded material zones by face classification, get_viewport_screenshot so Claude names zones (seat, legs, cushion), propose materials, user validates, then search PolyHaven per zone (~5 options). *(doc, medium; claude-blender-ai)*
- c3: Measured on american_walnut_veneer: 7 PolyHaven maps downloaded, only 3 survived glTF export (diffuse, roughness, normal). Standalone AO is silently dropped; displacement has no glTF slot; ARM is unused by set_texture's graph. *(data, medium; mesh-texture-limits)*
- c4: Blender fills glTF occlusionTexture only from an ARM-packed arrangement. Displacement should be baked into the normal map or dropped deliberately. *(doc, medium; mesh-texture-limits)*
- c5: Exporter warning 'More than one shader node tex image used for a texture' means information was lost; the glTF sampler uses the first node. *(doc, medium; blender-roblox-export-import)*
- c6: Subsurface scattering and Shader-to-RGB toon materials do not export to glTF. Bake SSS to base color. Emission, sheen, clearcoat, IOR and transmission (partial) export via extensions. *(doc, medium; mesh-texture-limits)*
- c7: Audit material export at the map level (maps the material has vs slots the exported glTF filled), not by listing procedural node types, which misses AO and displacement losses. *(opinion, medium; mesh-texture-limits)*
- c8: Blender 4.x renamed Principled inputs: Transmission Weight, Subsurface Weight, Sheen Weight, Emission Color/Strength. Older scripts using 'Transmission' fail on 4.x. *(doc, high; claude-blender-ai)*
- c9: After set_texture, rename the material (default <texture_id>_material_<object>) to an M_Type_Variant convention, e.g. M_Wood_Walnut. *(opinion, low; automation-and-creator-workflows)*

## Numbers
- n1: **PolyHaven maps downloaded vs surviving glTF export**: 7 vs 3 american_walnut_veneer
- n2: **nodes built by set_texture**: 16 material graph with Non-Color colorspaces preset
- n3: **bake resolution / Cycles samples**: 1024 / 64 bake_channel helper defaults
- n4: **PolyHaven download**: 1k jpg example resolution and format
- n5: **smart_project params**: angle_limit=66, island_margin=0.02 auto UV when none exist before bake

## Techniques
- t1: **Geometric face classification via execute_blender_code**: Load mesh into bmesh, compute face z_ratio within bounding box and normal.z; horizontal (|nz|>0.7) vs vertical (<0.3) heuristics assign zones; set face.material_index; bm.to_mesh.
- t2: **Bake procedural materials to image textures**: Switch to Cycles, create image, add active ShaderNodeTexImage per material, ensure UVs, bpy.ops.object.bake(type=...), save PNG, remove temp node. Set Non-Color for ROUGHNESS/NORMAL. Then reconnect baked images and re-audit.
- t3: **Procedural Principled BSDF recipes**: Set Base Color, Roughness, Metallic values; glass uses Transmission Weight 1, IOR 1.45; neon uses Emission Color and Strength; fabric uses Sheen Weight 0.5. No image textures needed for stylized assets.

### Code: Rename material after set_texture
```python
obj.data.materials[0].name = "M_Wood_Walnut"
```

### Code: Bake a channel to image
```python
bpy.ops.object.bake(type=channel_type, save_mode='INTERNAL')
```

### Code: Auto UV unwrap
```python
bpy.ops.uv.smart_project(angle_limit=66, island_margin=0.02)
```

## Points to
- blender-kiln plugin (elithril)
- PolyHaven
- Hunyuan3D
- blender-mcp addon tools: download_polyhaven_asset, set_texture, search_polyhaven_assets, get_viewport_screenshot
- references/uv-materials.md
