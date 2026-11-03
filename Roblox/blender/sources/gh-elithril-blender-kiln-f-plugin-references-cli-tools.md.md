---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-cli-tools.md
title: "elithril/blender-kiln/plugin/references/cli-tools.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/cli-tools.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0328
relevance: 1
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-cli-tools.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
CLI reference from a Blender-export plugin (blender-kiln) for GLB optimization with gltf-transform, gltfpack and USDZ conversion. Covers texture resize/WebP/KTX2, Draco/meshopt compression, LOD generation, and a warning against gltf-transform optimize. Web/AR-oriented, not Roblox-specific; only loosely transferable to Roblox (LOD ideas, texture downscaling).

## Claims
- c1: Source warns never to run `gltf-transform optimize` because it includes simplify, which destroys mesh geometry; use individual steps instead (resize, webp, draco last). *(doc, medium; mesh-texture-limits)*
- c2: Downscaling textures from 4K to 1K gives about 16x GPU memory reduction; mobile GPUs benefit most. *(doc, medium; mesh-texture-limits)*
- c3: gltfpack -sa (aggressive simplification) can create artifacts on marked edges, so each LOD should be checked visually. *(doc, medium; mesh-texture-limits)*
- c4: After optimization, report before/after file size, face count, texture count/resolution, and keep the pre-optimization file as backup. *(doc, medium; automation-and-creator-workflows)*
- c5: Meshopt compression needs no WASM decoder client-side, whereas Draco needs a ~200KB WASM decoder. Neither is Roblox-specific; Roblox import support for compressed GLB is not stated. *(doc, low; blender-roblox-export-import)*

## Numbers
- n1: **Raw export size with 4K textures**: ~22 MB (GPU ~89 MB per texture) reference metrics baseline
- n2: **After 1K resize**: ~3.7 MB, ~5.6 MB GPU same asset
- n3: **After Draco**: ~1 MB final size after resize, WebP, Draco
- n4: **LOD face budget**: LOD0 100%, LOD1 50%, LOD2 25%, LOD3 10% distances 0-10m, 10-25m, 25-50m, 50-100m
- n5: **KTX2 texture size reduction**: 60-80% gltf-transform ktx2
- n6: **USDZ max texture**: 4096x4096 (Apple recommends 2048) USDZ constraints

## Techniques
- t1: **Safe GLB optimization order**: gltf-transform resize to 1024x1024, then webp --quality 90, then draco last (irreversible), then gltf-transform inspect the result.
- t2: **Manual LOD generation with gltfpack**: Keep the original as LOD0. Run gltfpack -si 0.5 for LOD1, -si 0.25 for LOD2, and -si 0.1 -sa for LOD3. Inspect each with gltf-transform inspect.
- t3: **Compression without geometry change**: gltfpack -i in.glb -o out.glb -cc applies meshopt compression with no geometry changes.

### Code: Safe texture+mesh optimization pipeline
```bash
gltf-transform resize input.glb resized.glb --width 1024 --height 1024
gltf-transform webp resized.glb webp.glb --quality 90
gltf-transform draco webp.glb final.glb
gltf-transform inspect final.glb
```

### Code: Simplify to 50% faces with gltfpack
```bash
gltfpack -i input.glb -o output.glb -si 0.5
```

## Points to
- https://gltf-transform.dev/cli
- https://meshoptimizer.org/gltf/
- https://github.com/zeux/meshoptimizer/releases
- https://github.com/elithril/blender-kiln
