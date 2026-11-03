---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-FREE_ASSETS_GUIDE.md
title: "sandraschi/blender-mcp/docs/blender/FREE_ASSETS_GUIDE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/FREE_ASSETS_GUIDE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0365
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "texturing-baking-uv"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-FREE_ASSETS_GUIDE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
A generic free-asset sourcing guide for the sandraschi blender-mcp project's blender_download tool (katana-themed examples). Lists CC0 sites (Poly Haven, AmbientCG), format advice and license basics. Nothing on Roblox, export settings, bpy scripting, or Claude workflows beyond illustrative blender_download calls; several example URLs look invented.

## Claims
- c1: blender-mcp (sandraschi) exposes an async blender_download(url, timeout=...) tool for fetching HDRIs, textures and models; the guide suggests timeout=120 for large files. *(doc, medium; claude-blender-mcp)*
- c2: The guide claims blender-mcp supports importing .obj, .fbx, .dae, .gltf and .blend; it calls .blend the best compatibility. *(doc, low; claude-blender-mcp)*
- c3: Poly Haven and AmbientCG are listed as CC0 sources of PBR textures (albedo, normal, roughness, displacement) up to 8K at AmbientCG; usable commercially, relevant for sourcing maps for SurfaceAppearance. *(doc, medium; texturing-baking-uv)*
- c4: Check licenses before commercial use: CC0 and public domain are unrestricted, CC-BY needs attribution, CC-BY-SA needs attribution plus ShareAlike. Avoid all-rights-reserved assets. *(doc, high; creator-workflows)*
- c5: Search tips: add 'low poly' or 'game ready' to queries to find real-time-optimised models, and check polygon count and texture resolution before use. *(doc, medium; creator-workflows)*
- c6: Download troubleshooting: dead URLs, extension/format mismatch, corrupted files and timeouts. Fixes are to try alternate sources or formats and lengthen the timeout. *(doc, medium; common-mistakes-fixes)*
- c7: Some example URLs in the guide (e.g. polyhaven.com/model/katana, ambientcg.com/metal_sword) look like placeholders and probably don't resolve. The doc has no verification. *(opinion, medium; creator-workflows)*

## Numbers
- n1: **suggested download timeout for large files**: 120 blender_download(url, timeout=120)
- n2: **AmbientCG max texture resolution**: 8K PBR materials, CC0

## Techniques
- t1: **Download asset into Blender via MCP**: Call blender_download with a direct file URL (e.g. Poly Haven 4k HDR or AmbientCG zip), then import into the scene. Loop over a URL list for batch downloads.

### Code: blender-mcp download tool usage with timeout
```python
await blender_download(url, timeout=120)
```

### Code: Download a Poly Haven HDRI
```python
await blender_download("https://dl.polyhaven.org/file/ph_assets/HDRIs/hdr/4k/studio_small_09_4k.hdr")
```

## Contradictions flagged
- The guide lists Quixel Megascans as a free library with no account, at megascans.se, under CC0. (vs Megascans licensing and access are not CC0 and need an account (my knowledge, not stated in the source).)

## Points to
- polyhaven.com
- ambientcg.com
- sketchfab.com
- opengameart.org
- blendswap.com
- BlenderKit
- Kenney Assets
