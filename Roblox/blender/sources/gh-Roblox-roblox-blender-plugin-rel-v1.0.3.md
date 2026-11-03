---
type: research-source
id: gh-Roblox-roblox-blender-plugin-rel-v1.0.3
title: "Roblox/roblox-blender-plugin v1.0.3: Release v1.0.3"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/releases/tag/v1.0.3"
published: "2023-11-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 3
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# gh-Roblox-roblox-blender-plugin-rel-v1.0.3

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox roblox-blender-plugin v1.0.3 release notes (2023-11-29). Adds animation export settings (noting Open Cloud endpoint supports dynamic heads but not animations yet), fixes uploading in Blender 4.0, and adds export settings needed to import dynamic heads. Thin changelog; no bpy/MCP or triangle/texture specifics.

## Claims
- c1: v1.0.3 adds animation export settings to the Roblox Blender plugin (PR #31). *(doc, high; blender-roblox-export-import)*
- c2: As of v1.0.3, Open Cloud endpoint supports dynamic heads but not animations yet; plugin is ready once endpoint adds animation support. *(doc, high; automation-and-creator-workflows)*
- c3: v1.0.3 fixes uploading in Blender 4.0 (PR #37). *(doc, high; blender-roblox-export-import)*
- c4: v1.0.3 adds necessary export settings to import dynamic heads (PR #38). *(doc, high; avatar-ugc-accessories)*
- c5: Animation export settings were added in v1.0.3, but upload of animations depends on Open Cloud support that did not yet exist at release. *(doc, medium; rigging-animation)*

## Numbers
- n1: **Release date**: 2023-11-29 
- n2: **Changelog range**: v1.0.1 to v1.0.3 

## Techniques
- t1: **Dynamic head export**: Use the plugin's export settings added in v1.0.3 (PR #38) to produce a head mesh that Roblox can import as dynamic head; upload via Open Cloud.

## Quotes (brief, for attribution)
> The Open Cloud endpoint currently supports dynamic heads, but not animations yet. Once the Open Cloud endpoint supports animations, this plugin should now be ready to go.  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/releases/tag/v1.0.3
- https://github.com/Roblox/roblox-blender-plugin/pull/31
- https://github.com/Roblox/roblox-blender-plugin/pull/37
- https://github.com/Roblox/roblox-blender-plugin/pull/38
- https://github.com/Roblox/roblox-blender-plugin/compare/v1.0.1...v1.0.3
