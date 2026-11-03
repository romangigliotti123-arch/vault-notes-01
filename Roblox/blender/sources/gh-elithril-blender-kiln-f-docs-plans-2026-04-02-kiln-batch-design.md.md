---
type: research-source
id: gh-elithril-blender-kiln-f-docs-plans-2026-04-02-kiln-batch-design.md
title: "elithril/blender-kiln/docs/plans/2026-04-02-kiln-batch-design.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/docs/plans/2026-04-02-kiln-batch-design.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0419
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-export-settings", "roblox-mesh-limits", "texturing-baking-uv"]
---
# gh-elithril-blender-kiln-f-docs-plans-2026-04-02-kiln-batch-design.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Design doc for blender-kiln's /kiln:batch: a wizard writes a YAML manifest, then an autonomous runner drives a local Blender MCP to produce multiple assets (scripted, Hunyuan3D, marketplace, geometry nodes) exported as glTF/FBX. It covers the manifest format, error handling and token estimates. Nothing Roblox-specific.

## Claims
- c1: Batch mode requires a local Blender MCP (machine on, Blender open). It is incompatible with Claude's remote/cloud schedule. *(doc, high; claude-blender-mcp)*
- c2: Design splits decisions (interactive wizard) from execution (autonomous runner) through an editable, git-versionable YAML manifest. This makes runs reproducible and lets you rerun single assets with status: redo. *(doc, high; creator-workflows)*
- c3: Method heuristics: simple geometric props use scripted bpy; organic/complex props and characters use Hunyuan3D; repetitive patterns use geometry nodes; standard items (keyboard, monitor, mouse) come from a marketplace. *(doc, medium; procedural-generation)*
- c4: The runner keeps 'iron rules' in every asset (merge doubles, recalc normals, scale check, material audit). Pipeline stages: BRIEF, CHOIX, IMPORT, CLEANUP, TEXTURING, OPTIMIZE, EXPORT. *(doc, high; common-mistakes-fixes)*
- c5: On error the runner logs the failure, marks the asset failed and moves on. It does no retry and no cross-method fallback, to keep art-direction consistency. *(doc, high; creator-workflows)*
- c6: A shared material palette (PolyHaven IDs or procedural PBR params) is used by all assets in a batch for visual consistency. *(doc, high; texturing-baking-uv)*
- c7: Auto decimation in batch runs triggers only when face count is more than 50% outside the tier's range. Tiers are lightweight, balanced and detailed. *(doc, medium; roblox-mesh-limits)*
- c8: Pragmatic guard: limit batches to about 5-10 assets, since there is no automatic token cutoff. *(opinion, medium; creator-workflows)*
- c9: Export targets are glTF-web, Unity FBX, Unreal FBX and USDZ AR. Roblox is not a target. The optimize preset example is resize-1k-webp-draco (1K textures, WebP, Draco). *(doc, high; roblox-export-settings)*

## Numbers
- n1: **tokens per scripted asset**: ~30K wizard estimate
- n2: **tokens per marketplace asset**: ~20K wizard estimate
- n3: **tokens per Hunyuan3D asset**: ~60-80K wizard estimate
- n4: **tokens per Geometry Nodes asset**: ~40K wizard estimate
- n5: **example 10-asset batch estimate**: 350K-550K tokens, ±50%; use x1.5 margin retries can double an asset
- n6: **example run**: 8/10 succeeded, ~25 min 2 failures, HF Space timeout type
- n7: **example desk result**: 2100 faces, 340KB, 180s balanced tier glb

## Techniques
- t1: **Manifest-driven batch generation**: A wizard collects scene, style, target, tier, asset list and palette. It writes batch-manifest.yaml. The runner loops over assets with status other than done: clear scene, run pipeline, save to a per-asset folder, screenshot, update status, log.
- t2: **Per-asset output structure**: Each asset gets its own folder with name_final.glb, name.blend, a screenshot and a log.md. A top-level batch-report.md summarises the run. Failed assets keep only a log with the error and failed step.
- t3: **Status-based reruns**: Statuses are pending, running, done, failed and redo. Use run <dir> to execute non-done assets, --all to force everything, and --asset <name> for one asset.

### Code: Manifest asset entry with method, materials and tier
```yaml
  - name: desk
    brief: "Bureau rectangulaire moderne, plateau bois clair, pieds métal tubulaire noir"
    method: scripted
    materials: [wood, metal]
    tier: balanced
    status: pending
```

## Points to
- elithril/blender-kiln
- Hunyuan3D
- Poly Haven
- Blender MCP
