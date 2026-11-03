---
type: research-source
id: gh-elithril-blender-kiln-f-docs-gallery.md
title: "elithril/blender-kiln/docs/gallery.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/docs/gallery.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0030
relevance: 2
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "roblox-export-settings", "roblox-mesh-limits"]
---
# gh-elithril-blender-kiln-f-docs-gallery.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Gallery doc from the blender-kiln repo measuring a 15-prop Blender-to-GLB optimisation pipeline: 21,879 tris, 1456.2 kB raw to 132.7 kB with Draco (91%). Covers Draco vs meshopt, Blender re-import behaviour, and audit of 20 "iron rules" in headless bpy scripts. It never mentions Roblox, so Roblox relevance is indirect.

## Claims
- c1: 15 assets total 21,879 tris; Draco output totals 132.7 kB vs 1456.2 kB raw GLB (91% smaller). Doc is not Roblox-specific. *(data, high; roblox-mesh-limits)*
- c2: Draco output is about 9% of raw size per asset (e.g. barrel 111.9 kB to 10.2 kB); meshopt output is roughly twice Draco size but decodes faster on the client. *(data, high; roblox-mesh-limits)*
- c3: gltfpack meshopt output (EXT_meshopt_compression) fails to re-import into Blender; Draco output re-imports fine. Doc calls the import error expected, not a broken file. *(data, high; common-mistakes-fixes)*
- c4: Weld step increases file size; it is only a preparation step for Draco and should not be shipped on its own. *(data, high; roblox-mesh-limits)*
- c5: Optimise steps must run separately (dedup, weld, draco, or gltfpack); never run gltf-transform optimize (iron rule 20). *(doc, high; roblox-mesh-limits)*
- c6: Pre-export cleanup order is apply transforms, merge doubles, recalc normals, then export; done by studio.cleanup() for every asset. *(doc, high; roblox-export-settings)*
- c7: GLTF export must set export_apply=False explicitly; a material audit (studio.material_audit()) scans for nodes GLTF drops before export. *(doc, high; bpy-scripting-headless)*
- c8: Scale rule: 1 Blender unit = 1 m, asserted per asset and written to the log. *(doc, high; roblox-export-settings)*
- c9: Triangle budget is tiered, not hard-capped: 9 lightweight, 5 balanced, 1 detailed tiers from topology-rules.md; alerts only above the top ceiling, never blocks. *(doc, high; roblox-mesh-limits)*
- c10: Iron rules 1/2/6 (scene info, screenshots, prompt before destroying) are not met by the headless scripts, since they need an interactive MCP session. *(doc, high; claude-blender-mcp)*
- c11: Principled BSDF inputs take linear values, not sRGB; hex-picked colours washed out (linear 0.31 is sRGB 0.58). Fix with a studio.srgb() conversion. *(doc, high; common-mistakes-fixes)*
- c12: Writing obj.location does not update obj.matrix_world in the same script; call view_layer.update() first or a ground-snap reads stale transform and leaves asset buried. *(doc, high; bpy-scripting-headless)*
- c13: Scripts need Blender 4.4+, measured on 5.0 and 5.2, plus gltf-transform, gltfpack and cwebp installed. *(doc, high; bpy-scripting-headless)*
- c14: Licence tracking: each asset log states all geometry is generated in-repo; no marketplace, generation service or money spent. *(doc, medium; creator-workflows)*
- c15: Each asset is built one per process by build.py; .blend is saved in <asset>/<asset>.blend; naming uses SM_PascalCase objects, M_Type_Variant materials, kebab-case files. *(doc, high; bpy-scripting-headless)*

## Numbers
- n1: **total triangles, 15 assets**: 21,879 
- n2: **raw GLB to Draco total**: 1456.2 kB to 132.7 kB (91% smaller) 
- n3: **Forge subtotal tris / Draco saving**: 7,044 tris, 91% 
- n4: **Sci-fi subtotal tris / Draco saving**: 11,472 tris, 92% 
- n5: **Nature subtotal tris / Draco saving**: 3,363 tris, 87% 
- n6: **largest asset: container tris, raw to Draco**: 5,076 tris, 350.1 kB to 20.4 kB (94%) 
- n7: **smallest asset: boulder tris, raw to Draco**: 320 tris, 34.0 kB to 4.3 kB (87%) 
- n8: **topology tiers**: 9 lightweight, 5 balanced, 1 detailed 
- n9: **minimum Blender version**: 4.4+ (measured on 5.0 and 5.2) 
- n10: **sRGB to linear example**: linear 0.31 = sRGB 0.58 
- n11: **unit scale**: 1 Blender unit = 1 m 

## Techniques
- t1: **Separate-step GLB compression**: Run dedup, then weld, then Draco as separate gltf-transform calls; never gltf-transform optimize. Ship the Draco output, not weld. Use gltfpack meshopt only for web viewers that decode it.
- t2: **Pre-export cleanup**: Apply transforms, merge doubles, recalc normals in that order, then run material audit and export GLB with export_apply=False.
- t3: **Stale matrix refresh**: After setting obj.location, call view_layer.update() before reading obj.matrix_world, e.g. for a Z=0 ground snap.
- t4: **Colour conversion for Principled BSDF**: Convert hex-picked sRGB to linear (studio.srgb()) before assigning Principled BSDF inputs, otherwise colours look washed out.
- t5: **Per-asset build process**: Build one asset per process via build.py, save <asset>/<asset>.blend, write a log with scale check, budget tier, material audit and licence note.

### Code: Reproduce gallery builds (all themes or selected)
```bash
cd examples/gallery
./run_gallery.sh                      # all three themes
THEMES="forge nature" ./run_gallery.sh
```

## Quotes (brief, for attribution)
> Draco wins on size; gltfpack's meshopt output is roughly twice as large but decodes faster on the client.  (elithril)
> EXT_meshopt_compression is a web runtime format: three.js and Babylon decode it, Blender's glTF importer does not.  (elithril)
> Feeding hex-picked values straight in washes everything out  (elithril)

## Points to
- README gallery section (../README.md#gallery)
- plugin/references/topology-rules.md
- references/ (iron rules)
- gltf-transform
- gltfpack
- cwebp
- three.js (meshopt decode)
- Babylon.js (meshopt decode)
