---
type: research-source
id: gh-Roblox-roblox-blender-plugin-rel-v1.0.5
title: "Roblox/roblox-blender-plugin v1.0.5: Release v1.0.5"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/releases/tag/v1.0.5"
published: "2026-04-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 3
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai"]
---
# gh-Roblox-roblox-blender-plugin-rel-v1.0.5

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for Roblox Blender plugin v1.0.5 (2026-04-20). Main fix: dependency install and startup errors on Blender 5.x; plugin targets Blender 5.0 and 5.1 and may not work on Blender 4.x and earlier. Also sanitizes exported file names, fixes login error messages, and updates README for the 5.0 add-on UI. No triangle, UV, rig, or accessory specifics.

## Claims
- c1: v1.0.5 fixes dependency install and startup errors in Blender 5+ and is stated to work with Blender 5.0 and 5.1. *(doc, high; blender-roblox-export-import)*
- c2: v1.0.5 may not be compatible with Blender 4.x and earlier. *(doc, high; blender-roblox-export-import)*
- c3: Exported file names are sanitized to fix an export error (PR #76). *(doc, high; blender-roblox-export-import)*
- c4: Login errors now show the actual error message instead of a dictionary key (PR #106). *(doc, high; automation-and-creator-workflows)*
- c5: README updated with instructions for the new Blender 5.0 add-on UI (PR #111). *(doc, high; automation-and-creator-workflows)*
- c6: Repo adds recommended VS Code extensions.json (PR #72). *(doc, medium; automation-and-creator-workflows)*
- c7: Release notes do not mention blender-mcp, MCP, or bpy scripting; no Claude-specific workflow is covered. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Supported Blender versions**: 5.0 and 5.1; not 4.x or earlier 
- n2: **Version range in changelog**: v1.0.3 to v1.0.5 

## Quotes (brief, for attribution)
> The plugin should now work with 5.0 and 5.1.  (Roblox)
> this version of the plugin may not be compatible with blender v4.x and under  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/compare/v1.0.3...v1.0.5
- https://github.com/Roblox/roblox-blender-plugin/pull/110
- https://github.com/Roblox/roblox-blender-plugin/pull/111
