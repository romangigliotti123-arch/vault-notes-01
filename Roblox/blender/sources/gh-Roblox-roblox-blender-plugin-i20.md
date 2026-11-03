---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i20
title: "Roblox/roblox-blender-plugin#20 Login button does nothing - No module named 'aiohttp'"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/20"
published: "2023-10-10"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "other"]
---
# gh-Roblox-roblox-blender-plugin-i20

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #20 on Roblox's blender-roblox-export plugin: login button does nothing because aiohttp is missing (dependencies not installed). Maintainers suggest reinstall, console checks, and deleting dependencies_public to force reinstall. Closed as duplicate of #42. Little on Claude, bpy, or asset export specs.

## Claims
- c1: Roblox Blender plugin login depends on aiohttp; login fails with ModuleNotFoundError 'No module named aiohttp' when dependencies not installed (Blender 3.6, Windows). *(doc, high; blender-roblox-export-import)*
- c2: Plugin shows Install Dependencies button after install; maintainer says login button should not show without successful dependency install, calling it a likely bug. *(doc, high; blender-roblox-export-import)*
- c3: Workaround: delete addon folder dependencies_public under Blender 4.0 scripts/addons/roblox-blender-plugin, then disable and re-enable plugin to trigger dependency reinstall, then restart Blender. *(experience, medium; blender-roblox-export-import)*
- c4: Reinstalling the plugin alone did not fix the missing aiohttp error for a user; system console output needed to diagnose install errors. *(experience, medium; blender-roblox-export-import)*
- c5: Debug tip: on Windows use Window > Toggle System Console; on macOS start Blender from a terminal to see install/login errors. *(doc, high; automation-and-creator-workflows)*
- c6: Issue was closed as duplicate of Roblox/roblox-blender-plugin#42, which tracks the root cause; #14 was a similar report. *(doc, high; automation-and-creator-workflows)*
- c7: Source does not mention Claude, blender-mcp, bpy scripting, or MeshPart/SurfaceAppearance; it is a narrow plugin install/login bug report with low topical relevance. *(doc, high; other)*

## Numbers
- n1: **Blender version in traceback**: 3.6 
- n2: **Blender version in workaround path**: 4.0 

## Techniques
- t1: **Reset plugin dependencies**: Delete the addon's dependencies_public folder, disable then re-enable the plugin, accept the Install Dependencies prompt, watch console for 'Installation complete', restart Blender.
- t2: **Capture Blender console**: Windows: Window > Toggle System Console. macOS: launch Blender from a terminal to read install and login tracebacks.

### Code: Workaround path for resetting plugin dependencies (Blender 4.0, Windows)
```text
%appdata%\Roaming\Blender Foundation\Blender\4.0\scripts\addons\roblox-blender-plugin\dependencies_public
```

## Quotes (brief, for attribution)
> Missing `aiohttp` module indicates the dependencies didn't get installed properly.  (Roblox)
> The login button shouldn't show without a successful dependency installation, so there may be a bug here.  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/14
- https://github.com/Roblox/roblox-blender-plugin/issues/42
