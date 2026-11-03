---
type: research-source
id: gh-elithril-blender-kiln-f-docs-plans-2026-04-02-kiln-batch-implementation.md
title: "elithril/blender-kiln/docs/plans/2026-04-02-kiln-batch-implementation.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/docs/plans/2026-04-02-kiln-batch-implementation.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0960
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "open-cloud-automation", "procedural-generation", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-f-docs-plans-2026-04-02-kiln-batch-implementation.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Implementation plan for a Claude skill (blender-kiln) adding /kiln:batch: a wizard writes a YAML manifest, and a runner drives Blender through the Blender MCP to produce many assets sequentially. It covers per-asset method heuristics, a clear-scene-between-assets rule, and failure handling. Targets glTF/Unity/Unreal/USDZ, not Roblox. Useful only as a pattern for Claude+Blender-MCP batch automation.

## Claims
- c1: Batch system is pure skill instructions (markdown SKILL.md) with no Python/TypeScript; Claude executes pipeline phases through Blender MCP, with a YAML manifest as the source of truth. *(doc, high; claude-blender-mcp)*
- c2: Runner pre-flight verifies Blender MCP is connected, validates manifest, and runs environment auto-detect before starting. *(doc, high; claude-blender-mcp)*
- c3: Scene is cleared between assets via execute_blender_code running bpy.ops.wm.read_homefile(use_empty=True), so no state carries over from one asset to the next. *(doc, high; bpy-scripting-headless)*
- c4: Viewport screenshot is captured per asset via get_viewport_screenshot() and saved next to the asset's log for verification. *(doc, high; claude-blender-mcp)*
- c5: Creation-method heuristics: simple geometric shapes (table, shelf, door) -> scripted; organic/complex forms and all characters -> hunyuan3d; repetitive patterns (cables, fences) -> geometry-nodes; standard objects (keyboard, monitor) -> marketplace. *(opinion, medium; procedural-generation)*
- c6: Runner never switches creation method on failure; it skips and logs the asset, prioritizing art-direction coherence over completion rate. It continues to the next asset with no retry. *(doc, high; creator-workflows)*
- c7: Manifest is rewritten after each asset (status pending/running/done/failed/redo plus result), so a crash leaves progress recorded and the batch can be resumed. *(doc, high; creator-workflows)*
- c8: Automated cleanup sequence: Merge by Distance, Recalculate Normals, Remove Loose, Degenerate Dissolve, Apply Transforms, Origin to base center; auto-decimate to tier midpoint if poly count is >50% above tier range. *(doc, high; common-mistakes-fixes)*
- c9: Import step verifies scale (1 unit = 1 m) and logs an alert on odd dimensions without blocking. *(doc, high; common-mistakes-fixes)*
- c10: Shared material palette across batch assets (PolyHaven PBR IDs or procedural Principled BSDF params) keeps visual coherence; materials are assigned to mesh zones by face normal/position clustering. *(doc, medium; texturing-baking-uv)*
- c11: Optimize presets use gltf-transform: resize 1024 -> webp -> draco, or resize 512 -> webp, or none. *(doc, high; texturing-baking-uv)*
- c12: Plan covers no Roblox upload or Open Cloud step. Export targets are glTF-web, Unity FBX, Unreal FBX, USDZ, or multi. *(doc, high; open-cloud-automation)*

## Numbers
- n1: **token estimate per asset: scripted**: ~30K Used for batch cost estimate
- n2: **token estimate per asset: marketplace**: ~20K Used for batch cost estimate
- n3: **token estimate per asset: hunyuan3d**: ~60K Used for batch cost estimate
- n4: **token estimate per asset: geometry-nodes**: ~40K Used for batch cost estimate
- n5: **estimate range multiplier**: 1.0x to 1.5x Low/high range; retries may double a single asset
- n6: **decimate trigger**: >50% above tier range Auto-decimate to tier midpoint

## Techniques
- t1: **Manifest-driven batch runner**: Wizard collects theme, style, target, tier, assets, palette; writes batch-manifest.yaml. Runner loops over assets with status pending/failed/redo: clear scene, run phases, screenshot, log, update manifest, append report.
- t2: **Per-asset isolation in Blender MCP**: Run read_homefile(use_empty=True) through execute_blender_code before each asset so state never leaks between assets.
- t3: **Resume/redo via status editing**: Edit manifest status done->redo, change method or brief, then rerun; flags --all and --asset <name> force reruns.

### Code: Clear Blender scene between batch assets (via execute_blender_code)
```python
bpy.ops.wm.read_homefile(use_empty=True)
```

## Points to
- blender-mcp (execute_blender_code, get_viewport_screenshot)
- Hunyuan3D-2.1 HF Space
- PolyHaven
- Sketchfab
- gltf-transform
- gltfpack
- Pollinations
