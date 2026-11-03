---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-batch-mode.md
title: "elithril/blender-kiln/plugin/references/batch-mode.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/batch-mode.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0645
relevance: 2
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-batch-mode.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Batch-mode reference for the "kiln" Claude plugin driving Blender via blender-mcp: a wizard writes a YAML manifest, then an unattended runner processes each asset. Useful for blender-mcp pitfalls (read_homefile resets addon integration flags, geometry-nodes export needs applied modifiers, addon status checks) and batch design. No Roblox-specific content; targets glTF/Unity/Unreal/USDZ.

## Claims
- c1: Clearing the scene with bpy.ops.wm.read_homefile(use_empty=True) breaks blender-mcp batches: the addon stores integration flags (blendermcp_use_polyhaven, _sketchfab, _hunyuan3d, _hyper3d) as scene properties, so a fresh scene resets them to False. *(experience, high; claude-blender-ai)*
- c2: A disabled integration doesn't raise an error; its command is unregistered and the next call returns 'Unknown command type'. Measured: asset 1 succeeds, then every later asset fails, silently across an overnight batch. *(experience, high; claude-blender-ai)*
- c3: Safe scene clear between assets: remove all objects, then remove datablocks (meshes, materials, images, node_groups, armatures) with zero users, via execute_blender_code. *(doc, high; claude-blender-ai)*
- c4: Geometry-nodes output is a modifier result; exporting with export_apply=False writes the base mesh. A 2,688-triangle scatter exported as 2 triangles with no error, so the modifier must be applied before export. *(experience, high; blender-roblox-export-import)*
- c5: Pre-flight should call get_addon_status(), an MCP-server-side aggregation over get_addon_info. It reports up_to_date:false even for addons too old to have that command. Fix: run `uvx blender-mcp install-addon` and re-enable the addon. *(doc, medium; claude-blender-ai)*
- c6: Validate integrations before the batch starts using get_polyhaven_status, get_sketchfab_status, get_hunyuan3d_status and get_hyper3d_status. If one is off, abort and print its message field, which names the checkbox and sidebar panel. Ticking the box takes effect immediately; no connection restart is needed (verified). *(experience, medium; claude-blender-ai)*
- c7: Runner design: a YAML manifest is the source of truth with per-asset status (pending/running/done/failed/redo). It is updated after every asset so a crash preserves progress. Failures are skipped with no retry or method fallback. *(doc, high; automation-and-creator-workflows)*
- c8: Per-asset duration should be measured with `date +%s` at running and done, not estimated. *(doc, medium; automation-and-creator-workflows)*
- c9: Auto-decimate to the tier's top poly budget when the count exceeds 2x the tier's top, logging before/after stats. Tiers are lightweight/balanced/detailed. *(doc, medium; mesh-texture-limits)*
- c10: Optimize presets use gltf-transform: resize 1024, then webp, then draco (resize-1k-webp-draco), or resize-512-webp. Custom strings follow the format resize-{size}-{compression}. *(doc, medium; mesh-texture-limits)*
- c11: Creation-method heuristics: simple geometry gets scripted bpy; organic forms and characters get AI generation (TRELLIS.2 via HF Space, Hunyuan3D only on request); repetitive patterns get geometry-nodes; standard objects get marketplace (PolyHaven/Sketchfab). *(opinion, medium; claude-blender-ai)*
- c12: Token estimates per asset: scripted ~30K, marketplace ~20K, ai ~60-80K, geometry-nodes ~40K. The range multiplies the total by 1.0 to 1.5. *(opinion, low; claude-blender-ai)*
- c13: Import step verifies scale of 1 unit = 1m and logs an alert on odd dimensions without blocking. *(doc, low; blender-roblox-export-import)*

## Numbers
- n1: **geometry-nodes scatter exported without applying modifier**: 2,688 tris became 2 tris export_apply=False wrote base mesh
- n2: **auto-decimate threshold**: 2x tier top decimate down to tier top in batch mode
- n3: **optimize preset texture size**: 1024 or 512 px gltf-transform resize presets
- n4: **wizard time**: ~5-10 min interactive manifest creation
- n5: **token cost per asset**: 20K-80K marketplace 20K, scripted 30K, geometry-nodes 40K, ai 60-80K

## Techniques
- t1: **Safe scene reset between MCP batch assets**: Via execute_blender_code, remove every object with bpy.data.objects.remove(o, do_unlink=True). Then remove zero-user datablocks in meshes, materials, images, node_groups and armatures. Never call read_homefile.
- t2: **Pre-flight addon and integration checks**: Call get_addon_status() and abort with an install-addon hint if up_to_date is false. For each integration the manifest needs, call the matching get_*_status() and abort with its message if disabled.
- t3: **Apply geometry-nodes modifiers before export**: Apply the modifier, or export with modifiers applied, so the evaluated mesh is written. Check triangle counts after export to catch silent loss.
- t4: **Manifest-driven unattended batch**: Wizard collects theme, style, target, tier, assets, and a shared material palette. It writes batch-manifest.yaml. The runner loops over assets that are not done, writes logs, screenshots (get_viewport_screenshot) and batch-report.md, and rewrites the manifest after each asset.
- t5: **Reference-image brief enrichment**: Analyze the reference image for details missing from the brief and log the enriched brief. The user's brief wins on any conflict. Afterward, compare the final screenshot with the reference and log a non-blocking verdict.

### Code: Clear Blender scene without resetting addon scene properties
```python
import bpy
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o, do_unlink=True)
for blk in (bpy.data.meshes, bpy.data.materials, bpy.data.images,
            bpy.data.node_groups, bpy.data.armatures):
    for d in list(blk):
        if d.users == 0:
            blk.remove(d)
```

## Quotes (brief, for attribution)
> NEVER `bpy.ops.wm.read_homefile(use_empty=True)`. It builds a fresh scene, and the addon stores every integration flag as a SCENE property.  (elithril)
> a 2,688-triangle scatter exported as 2 triangles — with no error, so the batch would record it as done.  (elithril)

## Contradictions flagged
- The addon's message says to restart the connection after enabling an integration, but the author verified this is not required. (vs blender-mcp addon status message)

## Points to
- blender-mcp (uvx blender-mcp install-addon)
- PolyHaven
- Sketchfab
- Hunyuan3D
- Hyper3D Rodin
- microsoft/TRELLIS.2 (HF Space)
- FLUX.1-schnell Space
- gltf-transform
- github.com/elithril/blender-kiln
