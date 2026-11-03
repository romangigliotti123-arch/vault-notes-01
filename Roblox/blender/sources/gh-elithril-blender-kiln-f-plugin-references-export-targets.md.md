---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-export-targets.md
title: "elithril/blender-kiln/plugin/references/export-targets.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/export-targets.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0428
relevance: 2
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-export-targets.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Export-settings reference from a Blender-to-web/engine pipeline plugin (blender-kiln). Covers glTF, FBX, USDZ export via bpy, headless CLI fallback when blender-mcp execute_blender_code times out, pre/post-export checklists. No Roblox content; useful only for generic bpy export scripting, MCP timeout fallback, and FBX/glTF settings.

## Claims
- c1: The MCP server can time out on GLTF exports (long-running). If export via execute_blender_code fails or times out, use headless CLI export instead. *(experience, medium; claude-blender-ai)*
- c2: Without --python-exit-code 1, Blender exits 0 when the script raises, so a failed export looks successful (measured on 5.0.1; explicit sys.exit(1) propagates, uncaught exception does not). Check exit code and that the file exists. *(data, high; claude-blender-ai)*
- c3: export_apply=True on glTF export bakes Array modifiers and balloons file size (1MB to 56MB); keep False. *(experience, medium; blender-roblox-export-import)*
- c4: Axis conventions: Blender forward -Y, up Z; glTF +Z/Y; FBX (Unreal) +X/Z. Blender's glTF exporter converts automatically; for FBX set Forward and Up manually. *(doc, medium; blender-roblox-export-import)*
- c5: FBX export settings suggested: apply_scale_options FBX_SCALE_ALL, apply_unit_scale, bake_space_transform True, add_leaf_bones False, use_armature_deform_only True, path_mode COPY with embed_textures. Targeted at Unity/Unreal, not Roblox. *(doc, medium; blender-roblox-export-import)*
- c6: Only Principled BSDF maps cleanly to glTF PBR; custom shader node setups are not exported and must be baked first. Non-color maps (Normal, Roughness, Metallic) need Non-Color colorspace. *(doc, medium; mesh-texture-limits)*
- c7: glTF ORM packing: R=Occlusion, G=Roughness, B=Metallic. *(doc, high; mesh-texture-limits)*
- c8: USDZ export with convert_world_material default True writes a DomeLight referencing an .exr, making the archive non-conforming (PNG/JPEG only); set False. *(demo, medium; blender-roblox-export-import)*
- c9: Pre-export checklist: apply transforms (loc 0, rot 0, scale 1), merge doubles, recalc normals, origin at base center, no missing textures or empty material slots, no unbaked procedural nodes. *(doc, medium; blender-roblox-export-import)*
- c10: Post-export validation: gltf-transform validate must exit 0; gltf-transform inspect for mesh/texture counts; re-encoding existing Draco corrupts meshes, so apply Draco last. Validator checks format, not mesh quality. *(experience, medium; automation-and-creator-workflows)*

## Numbers
- n1: **file size with export_apply=True and Array modifiers**: 1MB → 56MB 
- n2: **USDZ max texture size**: 4096x4096 (Apple recommends 2048) 
- n3: **KTX2/Basis texture size reduction**: 60-80% 
- n4: **GLB size thresholds**: raw <30 MB, optimized <5 MB for web 
- n5: **Blender version measured**: 5.0.1 

## Techniques
- t1: **Headless Blender export fallback**: Run blender --background scene.blend --python-exit-code 1 --python-expr "...bpy.ops.export_scene.gltf(...)"; makedirs for output, print file size, check exit code and file existence. Quote paths with spaces. Good for heavy scenes and batch exports.
- t2: **Native USDZ export**: bpy.ops.wm.usd_export with .usdz path, selected_objects_only=True, export_materials=True, export_textures_mode='NEW', relative_paths=True, convert_world_material=False.

### Code: Headless glTF export with failure-propagating exit code
```bash
blender \
  --background "/path/to/scene.blend" \
  --python-exit-code 1 \
  --python-expr "
import bpy, os
export_path = '/path/to/output.glb'
bpy.ops.export_scene.gltf(filepath=export_path, export_format='GLB', export_apply=False)
"
```

### Code: FBX export settings
```python
bpy.ops.export_scene.fbx(
    filepath=output_path,
    use_selection=True,
    apply_scale_options='FBX_SCALE_ALL',
    apply_unit_scale=True,
    bake_space_transform=True,
    add_leaf_bones=False,
    use_armature_deform_only=True,
    path_mode='COPY',
    embed_textures=True,
)
```

## Points to
- gltf-transform
- Khronos glTF validator
- Babylon.js Sandbox
- blender-mcp execute_blender_code
