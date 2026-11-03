---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-modeling-workflo
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-modeling-workflow/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-modeling-workflow/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0041
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "common-mistakes-fixes", "creator-workflows", "other", "procedural-generation", "texturing-baking-uv"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-modeling-workflo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent-skill doc for scripted Blender modeling: Python script as durable source, headless Blender CLI runs, staged quality gates, reference-image matching, and fresh-import validation before export. Only loosely tied to Roblox: it mentions GLB export and game-ready assets but gives no Roblox-specific scale, mesh-limit, or import settings.

## Claims
- c1: Runs Blender headlessly with --background --factory-startup --python create_asset.py; the script is the durable source and Blender is only the execution runtime. *(doc, high; bpy-scripting-headless)*
- c2: Requires a clean Blender process rerun of the source script before a model counts as complete. *(doc, high; bpy-scripting-headless)*
- c3: Warns that procedural shaders, atmospheric volumes and Cycles lighting do not survive GLB export unchanged. *(doc, high; procedural-generation)*
- c4: Materials must be checked after export; final validation requires fresh-import checks of the requested export format. *(doc, medium; texturing-baking-uv)*
- c5: Radius-zero rings in revolved meshes must collapse to one shared pole vertex with triangle fans, otherwise zero-length edges appear even if the render looks smooth. *(doc, medium; common-mistakes-fixes)*
- c6: Modifier results must be evaluated before measuring exported geometry; a bevel or subdivision modifier is not assumed to equal polish. *(doc, medium; common-mistakes-fixes)*
- c7: Default target for game-ready assets is a polished smooth model with bevels and support geometry, not visibly low-poly, unless low-poly is explicitly requested. *(opinion, medium; creator-workflows)*
- c8: Suspected detached joints are checked with construction-derived contactPairs; close bounds only yield contact_unverified, not proof of contact. *(doc, medium; common-mistakes-fixes)*
- c9: Local repairs use a fast preview with two views, resolution 256, and a fixed camera before one final evidence run. *(doc, medium; creator-workflows)*
- c10: Reference-image matching: named reference camera, comparison at maxEdge 256 or 512, up to 32 landmarks, and at least three separated correspondences for camera framing fit; silhouette IoU alone does not establish 3D shape. *(doc, medium; other)*

## Numbers
- n1: **comparison image max edge**: 256 or 512 px blender_compare_reference maxEdge setting for reference vs silhouette overlay
- n2: **landmarks per reference**: up to 32 named correspondences supplied to blender_compare_reference
- n3: **correspondences for camera fit**: at least 3 separated needed by blender_fit_reference_camera; it fits framing only, not orientation or position
- n4: **fast preview resolution**: 256 px, views perspective + front local repair preview setting

## Techniques
- t1: **Headless Blender build from script**: Set BLENDER_EXECUTABLE, then run blender --background --factory-startup --python create_asset.py. Keep a deterministic entry script, explicit seeds, named parts and cameras.
- t2: **Pole-vertex lathe helper**: Use lathe_mesh.py for revolved parts: collapse radius-zero rings to one pole vertex with triangle fans, optional end caps; inspect evaluated prototype before replication.
- t3: **Reference camera matching**: Create named camera in bpy, match projection and framing first, compare silhouettes/overlay, fix largest mismatch, keep camera fixed while editing geometry.
- t4: **Local repair preview**: Preserve last good source, change smallest area, render two angles at 256 px with fixed presentation, retain only if visible result improves.

### Code: Run a Blender script headlessly on Windows
```powershell
$env:BLENDER_EXECUTABLE = "C:\path\to\Blender\blender.exe"
& $env:BLENDER_EXECUTABLE `
  --background --factory-startup --python .\create_asset.py
```

## Quotes (brief, for attribution)
> Treat the script as the durable source and Blender as the execution runtime.  (ifBars)
> Do not imply that procedural shaders, atmospheric volumes or Cycles lighting survive a GLB export unchanged.  (ifBars)

## Points to
- ifBars/blender-agent-studio plugin skills: blender-asset-validation, blender-rendering-workflow, blender-character-workflow, blender-animation-workflow, blender-signage-workflow
- lathe_mesh.py (bundled helper)
- blender_compare_reference / blender_fit_reference_camera / blender_quality_report (bundled MCP tools)
