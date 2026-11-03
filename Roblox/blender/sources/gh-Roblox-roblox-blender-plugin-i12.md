---
type: research-source
id: gh-Roblox-roblox-blender-plugin-i12
title: "Roblox/roblox-blender-plugin#12 Login button does nothing - Port conflict"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin/issues/12"
published: "2023-08-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# gh-Roblox-roblox-blender-plugin-i12

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #12 on Roblox's blender plugin: Blender "Log in" button produced no browser window. Users' console showed aiohttp web_runner failing to start a local server, consistent with a port 8080 conflict. Maintainer said the plugin would move to a less common port and added error handling; v1.0.1 shipped the port change and the issue was closed. Mostly plugin auth troubleshooting, little on blender-mcp or bpy scripting.

## Claims
- c1: Roblox Blender plugin login starts a local aiohttp web server (OAuth callback) on port 8080; a conflict on that port makes login silently fail. *(doc, medium; blender-roblox-export-import)*
- c2: Port change away from 8080 shipped in roblox-blender-plugin v1.0.1; issue closed as resolved (date of fix not stated in thread). *(doc, high; blender-roblox-export-import)*
- c3: Login button only showed 'logging in' while hovered because hover triggers a panel redraw; state updated but UI not redrawn (maintainer's suspicion, not confirmed). *(opinion, low; blender-roblox-export-import)*
- c4: On Windows, Blender system console is opened via Window > Toggle System Console; on Mac, launch Blender from Terminal with `blender` to see logs. *(doc, high; automation-and-creator-workflows)*
- c5: Plugin was 3.6-era Blender with the plugin installed under scripts/addons/roblox-blender-plugin-main with bundled dependencies_public folder; a separate missing-module error 'pyjwt_key_fetcher' was reported in another issue (#14). *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **plugin port**: 8080 (old default, changed in v1.0.1) 
- n2: **plugin version with fix**: v1.0.1 
- n3: **Blender version in report**: 3.6 
- n4: **issue date**: 2023-08-28 

## Techniques
- t1: **Find port conflict on Windows**: Run netstat -ao in cmd, find PID bound to :8080, then tasklist /fi "pid eq PID" to identify process.
- t2: **Capture Blender console logs**: Windows: Window > Toggle System Console. Mac: start Blender from Terminal with `blender` and reproduce the error.

### Code: Identify the process holding port 8080 on Windows
```cmd
netstat -ao
tasklist /fi "pid eq 1234"
```

## Quotes (brief, for attribution)
> this is probably a port conflict with another application running on your computer. To avoid such conflicts, we plan to change the plugin's port  (Roblox)
> The port change is now live in v1.0.1. Closing this as resolved now.  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/issues/14
