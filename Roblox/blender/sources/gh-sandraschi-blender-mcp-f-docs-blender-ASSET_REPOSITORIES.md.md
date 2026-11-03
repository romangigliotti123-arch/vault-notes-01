---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-ASSET_REPOSITORIES.md
title: "sandraschi/blender-mcp/docs/blender/ASSET_REPOSITORIES.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/ASSET_REPOSITORIES.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0338
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "roblox-mesh-limits"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-ASSET_REPOSITORIES.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Docs for a third-party blender-mcp fork's asset-repository handler: downloads/imports free assets (Kenney, Quaternius, OpenGameArt, Poly Haven) into Blender via Python async functions. Covers import options, errors, licenses, headless vs GUI executor. No Roblox-specific content; only marginally relevant for sourcing CC0 assets before a Roblox export.

## Claims
- c1: This blender-mcp variant supports automatic download+import from Kenney, Quaternius, OpenGameArt and Poly Haven; BlenderKit and Sketchfab are not implemented (BlenderKit needs API key and official add-on; Sketchfab has a complex API). *(doc, high; claude-blender-mcp)*
- c2: For unsupported sources like Sketchfab, download manually and use the import_file tool. *(doc, high; claude-blender-mcp)*
- c3: The executor can run headless or with GUI (get_blender_executor(headless=False)) so the user can see imported assets in a Blender window. *(doc, medium; claude-blender-mcp)*
- c4: Downloads are cached in %TEMP%\blender_mcp_assets\ and cleaned on restart. *(doc, medium; claude-blender-mcp)*
- c5: Licenses: Kenney and Poly Haven are CC0; Quaternius free for personal/commercial use; OpenGameArt varies per asset. Doc advises verifying terms before commercial use (relevant to Roblox marketplace sale). *(doc, medium; creator-workflows)*
- c6: Import options expose scale, location, rotation, and for FBX/OBJ global_scale; GLTF import_pack_images and merge_vertices; blend append/link via directory, asset_name, link flag. *(doc, medium; bpy-scripting-headless)*
- c7: Common import errors: HTTP 404 (wrong asset name), unsupported file format, connection timeout, and import returning {'CANCELLED'} (check format/options). *(doc, medium; common-mistakes-fixes)*
- c8: Doc suggests scaling large environments down (scale 0.1) on import; no Roblox stud/unit guidance given. *(doc, low; roblox-mesh-limits)*

## Techniques
- t1: **Download and import repository asset**: Call async download_and_import_asset(repository, asset_name, import_options, repository_specific_params). Poly Haven uses type 'hdris' or 'textures'; Kenney type '3d'/'2d'; OpenGameArt needs a direct url.

### Code: Download and import a Kenney asset via the MCP handler
```python
result = await download_and_import_asset(
    repository=AssetRepository.KENNEY,
    asset_name="fantasy-town-kit",
    import_options={"scale": 1.0, "location": [0, 0, 0]},
)
if result["status"] == "SUCCESS":
    print(f"Imported {result['asset_name']}")
```

## Points to
- https://kenney.nl/assets
- https://quaternius.com/
- https://opengameart.org/
- https://polyhaven.com/
- https://github.com/sandraschi/blender-mcp
