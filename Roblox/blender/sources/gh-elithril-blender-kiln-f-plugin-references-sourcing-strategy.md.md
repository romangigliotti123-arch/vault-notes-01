---
type: research-source
id: gh-elithril-blender-kiln-f-plugin-references-sourcing-strategy.md
title: "elithril/blender-kiln/plugin/references/sourcing-strategy.md"
source_type: "github"
creator: "elithril"
url: "https://github.com/elithril/blender-kiln/blob/HEAD/plugin/references/sourcing-strategy.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0326
relevance: 2
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-elithril-blender-kiln-f-plugin-references-sourcing-strategy.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Reference doc from a Blender MCP plugin (blender-kiln) on sourcing existing assets via PolyHaven and Sketchfab through blender-mcp. Covers preflight status checks (integrations off by default), PolyHaven public API fallback with ToS, licensing handling, search/result flow, and post-import scale check and renaming. Not Roblox-specific.

## Claims
- c1: PolyHaven and Sketchfab integrations are OFF in a default blender-mcp addon install; when off, search_polyhaven_assets / search_sketchfab_models are not registered and calls return 'Unknown command type: <name>', which looks like a version mismatch. *(doc, high; claude-blender-ai)*
- c2: Preflight: call get_polyhaven_status() and get_sketchfab_status() first; if enabled is false, print the message verbatim, which names the BlenderMCP sidebar panel (N key) checkbox to tick, then offer the other marketplace or creation. *(doc, high; claude-blender-ai)*
- c3: On the official Blender Lab MCP, or with integration off, PolyHaven's public API can be used via curl from Bash without a key; assets are CC0. *(doc, medium; claude-blender-ai)*
- c4: PolyHaven live API use requires a unique User-Agent (ToS 2.4) and visible credit to Poly Haven (2.5), though CC0 assets need no attribution themselves. *(doc, medium; automation-and-creator-workflows)*
- c5: Download 1k textures by default for web/glTF targets; 2k only for close-ups or console/PC targets. *(doc, medium; mesh-texture-limits)*
- c6: Sketchfab licenses vary (CC0, CC-BY, CC-BY-SA, CC-BY-NC); always log license, alert on attribution-required licenses, never download CC-BY-NC for commercial projects without user confirmation. Relevant to Roblox marketplace use. *(doc, medium; avatar-ugc-accessories)*
- c7: After importing a PolyHaven/Sketchfab asset, verify scale with get_object_info world_bounding_box (1 unit = 1 m). PolyHaven search reports millimetres but the importer converts to metres; a raw 568-unit object means conversion failed. *(doc, medium; blender-roblox-export-import)*
- c8: Sketchfab downloads require a free-account API token; download_sketchfab_model accepts target_size to normalize dimensions. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Chair file size, 2K maps uncompressed**: 16.2 MB same 724-triangle PolyHaven chair
- n2: **Chair file size, 2K WebP**: 1.03 MB same 724-triangle chair
- n3: **Chair file size, 1K uncompressed**: 0.48 MB same 724-triangle chair
- n4: **Search result count presented**: ~10 Sketchfab search count=10, downloadable=true

## Techniques
- t1: **PolyHaven public API fallback**: curl with -A unique User-Agent to api.polyhaven.com/assets?type=models&categories=X, then /files/<id>; pick gltf → 1k → gltf, download the file plus every 'include' entry in the same relative layout, import the .gltf.
- t2: **Sketchfab search flow**: search_sketchfab_models with query, downloadable=true, count=10; filter to free; present name, poly count, link, license; download_sketchfab_model with target_size.
- t3: **Post-import normalization**: get_object_info(name) to check world_bounding_box scale, then rename to SM_PascalCase with SM_..._Mesh data-block before downstream steps.

### Code: Query PolyHaven public API with unique User-Agent
```bash
UA="blender-kiln"
curl -s -A "$UA" "https://api.polyhaven.com/assets?type=models&categories=furniture"
curl -s -A "$UA" "https://api.polyhaven.com/files/WoodenChair_01"
```

## Points to
- Poly-Haven/Public-API ToS.md
- https://api.polyhaven.com
- https://sketchfab.com/settings/password
- https://polyhaven.com
