---
type: research-source
id: off-gh-roblox-blender-plugin-rel-v1.0.5
title: "Roblox Blender plugin release v1.0.5 (2026-04-20)"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/releases/tag/v1.0.5"
published: "2026-04-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 4
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai"]
---
# off-gh-roblox-blender-plugin-rel-v1.0.5

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Blender plugin v1.0.5 (released 2026-04-20). Main fix: dependency install and Blender 5.x API incompatibility; plugin should work with Blender 5.0 and 5.1. Explicitly may not be compatible with Blender 4.x and under. Changes include VS Code extensions.json, sanitized export filenames, login error message fix, Blender 5+ install/startup fixes, and README update for the 5.0 add-on UI. Release notes only; no pipeline or rig/mesh specs.

## Claims
- c1: v1.0.5 fixes dependency install and Blender 5.x API incompatibility; plugin should now work with Blender 5.0 and 5.1. *(doc, high; blender-roblox-export-import)*
- c2: v1.0.5 may not be compatible with Blender 4.x and earlier. *(doc, high; blender-roblox-export-import)*
- c3: Exported file names are sanitized to fix an export error (PR #76). *(doc, high; blender-roblox-export-import)*
- c4: Fixed install and startup errors in Blender 5+ (PR #110). *(doc, high; blender-roblox-export-import)*
- c5: Added recommended VS Code extensions.json (PR #72). *(doc, high; automation-and-creator-workflows)*
- c6: Login errors now show the actual error message instead of a dictionary key (PR #106). *(doc, high; automation-and-creator-workflows)*
- c7: README updated for the new Blender 5.0 add-on UI (PR #111). *(doc, high; automation-and-creator-workflows)*
- c8: Release notes do not mention blender-mcp, Claude, or bpy scripting; relevance to the Claude/MCP topic is indirect. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Supported Blender versions**: 5.0 and 5.1 Plugin v1.0.5 stated compatibility
- n2: **Release date**: 2026-04-20 v1.0.5 release date

## Techniques
- t1: **Upgrade to Blender 5.x for plugin**: Use Blender 5.0 or 5.1 with plugin v1.0.5. Blender 4.x and earlier may not work; install via the 5.0 add-on UI as described in the updated README.

## Quotes (brief, for attribution)
> The plugin should now work with 5.0 and 5.1.  (Roblox)
> this version of the plugin may not be compatible with blender v4.x and under  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/compare/v1.0.3...v1.0.5
- https://github.com/Roblox/roblox-blender-plugin/pull/72
- https://github.com/Roblox/roblox-blender-plugin/pull/76
- https://github.com/Roblox/roblox-blender-plugin/pull/106
- https://github.com/Roblox/roblox-blender-plugin/pull/110
- https://github.com/Roblox/roblox-blender-plugin/pull/111
