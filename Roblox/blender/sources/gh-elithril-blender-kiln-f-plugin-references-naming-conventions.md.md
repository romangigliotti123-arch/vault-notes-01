---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-naming-conventions.md
title: "elithril/blender-kiln/plugin/references/naming-conventions.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/naming-conventions.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0506
relevance: 2
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-naming-conventions.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Naming-convention reference from a Blender-to-glTF/FBX tooling repo (blender-kiln). Covers Blender prefixes, texture suffixes, power-of-2 rule, glTF export name mangling, and bpy snippets for renaming and checking names. Not Roblox-specific; uses Unreal-style prefixes.

## Claims
- c1: On glTF export, Blender names change: spaces become underscores and dots are removed (Sphere.003 -> Sphere003; 'RINGS S ' -> 'RINGS_S_'). Verify names in the exported GLB, not in Blender, when runtime code references meshes. *(doc, medium; blender-roblox-export-import)*
- c2: Textures should be power-of-2 sizes (256 to 4096). Non-color maps (Normal, Roughness, Metallic, AO) should use the Non-Color colorspace in Blender. *(doc, high; mesh-texture-limits)*
- c3: Object and mesh data-block names should match (SM_WoodenChair / SM_WoodenChair_Mesh). Use PascalCase, with no spaces, special characters or accents. *(doc, high; automation-and-creator-workflows)*
- c4: Texture suffixes: _D/_BaseColor, _N, _R, _M, _AO, _ORM (packed occlusion/roughness/metallic), _E, _H. This is Unreal-style naming, not Roblox SurfaceAppearance naming. *(doc, medium; mesh-texture-limits)*
- c5: Suggested per-asset output folder in kebab-case: _original, _clean, _textured, _optimized and _final .glb files, plus a .blend and a _log.md. *(doc, medium; automation-and-creator-workflows)*
- c6: Export file naming: glTF and USDZ use kebab-case; FBX for game engines uses PascalCase with a prefix (SM_WoodenChair.fbx). *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **allowed texture sizes**: 256, 512, 1024, 2048, 4096 power-of-2 rule

## Techniques
- t1: **Batch rename via bpy**: Set obj.name to Prefix_Name and obj.data.name to Prefix_Name_Mesh. Prefix material names with M_ if they don't already start with it.
- t2: **Predict glTF names**: Loop over bpy.data.objects, replace ' ' with '_' and remove '.', and print any object whose name would change. Confirm with gltf-transform inspect on the GLB.

### Code: Warn about names that change on glTF export
```python
import bpy
for obj in bpy.data.objects:
    gltf_name = obj.name.replace(" ", "_").replace(".", "")
    if gltf_name != obj.name:
        print(f"'{obj.name}' -> '{gltf_name}' in GLTF")
```

### Code: Apply naming convention to object, mesh data and materials
```python
def apply_naming(obj, asset_name, prefix="SM"):
    obj.name = f"{prefix}_{asset_name}"
    if obj.data:
        obj.data.name = f"{prefix}_{asset_name}_Mesh"
    for i, slot in enumerate(obj.material_slots):
        if slot.material and not slot.material.name.startswith("M_"):
            slot.material.name = f"M_{slot.material.name}"
```

## Points to
- gltf-transform inspect
