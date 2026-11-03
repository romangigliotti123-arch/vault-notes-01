---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-asset-validation
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/skills/blender-asset-validation/SKILL.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/skills/blender-asset-validation/SKILL.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 1
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "common-mistakes-fixes", "other"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-skills-blender-asset-validation

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Agent skill doc for validating Blender assets (.blend/.glb/.gltf/.fbx/.obj). Covers deterministic inspection via blender_inspect_asset or headless inspect_asset.py, topology diagnostics, scene description, quality reports with contact checks, motion inspection, multiview render evidence, and a fresh-import verification gate. Not Roblox-specific; no Roblox export or limit guidance.

## Claims
- c1: Headless inspection runs Blender with --background --factory-startup and --python inspect_asset.py, writing metrics.json. *(doc, high; bpy-scripting-headless)*
- c2: A clean export or low triangle count is not proof of visual or functional quality. *(doc, high; common-mistakes-fixes)*
- c3: Verification gate requires a fresh Blender process to import, inspect and render the exported file independently of the authored scene. *(doc, high; bpy-scripting-headless)*
- c4: Open boundaries alone are not defects; degenerate faces and zero-length edges trigger blender_diagnose_topology. *(doc, medium; other)*
- c5: Quality report returns review_required, which is explicitly not a pass; visual review still needed. *(doc, high; other)*

## Techniques
- t1: **Headless fresh-import verification**: Export artifact, start fresh Blender process, import/inspect/render the file independently, compare names, materials, dimensions, actions against authored scene.

### Code: Headless deterministic inspection of an asset
```powershell
$env:BLENDER_EXECUTABLE = "C:\path\to\Blender\blender.exe"
& $env:BLENDER_EXECUTABLE `
  --background --factory-startup `
  --python "<skill-root>\scripts\inspect_asset.py" -- `
  --input "<asset-path>" --output "<output-dir>\metrics.json"
```

## Quotes (brief, for attribution)
> A clean export or low triangle count is not proof of visual or functional quality.  (ifBars)

## Points to
- references/astra-workflow.md
- references/quality-gates.md
