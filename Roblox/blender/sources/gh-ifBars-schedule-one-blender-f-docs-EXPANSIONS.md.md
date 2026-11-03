---
type: research-source
id: gh-ifBars-schedule-one-blender-f-docs-EXPANSIONS.md
title: "ifBars/schedule-one-blender/docs/EXPANSIONS.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/schedule-one-blender/blob/HEAD/docs/EXPANSIONS.md"
published: "2026-10-08"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0336
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other"]
---
# gh-ifBars-schedule-one-blender-f-docs-EXPANSIONS.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Doc for a Schedule I (Unity game) Blender modding workflow: generate a native-kit expansion scene via Python CLI, author placements in Blender with an add-on, export a JSON recipe, load in-game via MelonLoader. Mostly off-topic for Roblox; only marginally relevant as an example of headless Blender validation scripts and a Blender add-on placement pipeline.

## Claims
- c1: Workflow targets Windows, Blender 5.2.x and the Mono alternate-beta game; IL2CPP and multiplayer are not validated. It is Unity/MelonLoader based, not Roblox. *(doc, high; other)*
- c2: Axis mapping noted: Blender Y is Unity Z and Blender Z is Unity Y. Metre units and absolute grid snapping are enabled; bridge modules use 10 m spacing. *(doc, high; blender-roblox-export-import)*
- c3: The exporter rejects modifiers, mirrored transforms and shear, and checks geometry, UVs, material bindings and node settings. It warns against applying object transforms to native-reference meshes and against Shift-D, which copies placement IDs. *(doc, high; automation-and-creator-workflows)*
- c4: The recipe export is placement-only JSON (selectors, transforms, collision options) with no mesh or texture arrays, so no game assets are redistributed. Generated files stay local. *(doc, high; automation-and-creator-workflows)*
- c5: Validation runs in a fresh headless Blender process using --background, --python-exit-code 1 and --python script with args after '--'. A repo AGENTS.md covers agent handoff, and compile or import success is not treated as proof of gameplay. *(doc, high; claude-blender-ai)*
- c6: Existing 512px texture proxies are kept in the generated Blender file. Solid view is the default for fast startup, and Material Preview is available via Z. *(doc, medium; mesh-texture-limits)*
- c7: The Unity preview importer simplifies materials to color/albedo/smoothness. It does not reconstruct custom shader graphs, triplanar mapping, normal maps, wetness or post-processing. It is not an export-back authoring tool. *(doc, high; other)*

## Numbers
- n1: **bridge module spacing**: 10 m Fourteen 10 m spans on the tested map
- n2: **texture proxy size**: 512px Existing proxies in the generated Expansion.blend
- n3: **recommended RAM context**: 32 GB Close Blender and the game when generating another scene

## Techniques
- t1: **Headless Blender validation script**: Run blender.exe --background file.blend --python-exit-code 1 --python pipeline/validate_expansion.py -- --report out.json in a fresh process. Use it to check an authoring file after saving.
- t2: **Blender add-on for placement export**: Install pipeline/native_expansion.py via Preferences > Add-ons > Install from Disk. Use the sidebar (N) panel to duplicate a kit, move the pieces, then Export Native Placements to JSON.

### Code: Headless Blender validation of the saved authoring file
```powershell
& "D:\SteamLibrary\steamapps\common\Blender\blender.exe" `
  --background "D:\MyBridgeExpansion\Expansion.blend" --python-exit-code 1 `
  --python pipeline/validate_expansion.py -- --report "D:\MyBridgeExpansion\validation.local.json"
```

## Points to
- https://github.com/ifBars/schedule-one-blender
- MelonLoader 0.7.3
- docs/VALIDATION.md
- docs/BUILD.md
- AGENTS.md
