---
type: research-source
id: gh-ahujasid-mcp-for-blender-i50
title: "ahujasid/mcp-for-blender#50 Error : MCP error -32001: Request Timed out"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/50"
published: "2025-03-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i50

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #50 in ahujasid/mcp-for-blender: user reports "MCP error -32001: Request Timed out" when asking Claude to build complex shapes from images/prompts in Blender. Timeouts left nothing in Blender; one build crashed Blender. Maintainer says running the MCP server in more than one place (Cursor, Claude, Terminal) breaks it; reboot, then an addon.py update fixed it per commenters. No Roblox content.

## Claims
- c1: Complex prompts (couch from renderings, building from sketch) produced MCP error -32001 'Request Timed out'; on timeout, Claude returned to the initial dialogue and no geometry was created in Blender. *(experience, high; claude-blender-mcp)*
- c2: One large building request did create 3D geometry but Blender then crashed. *(experience, high; claude-blender-mcp)*
- c3: Maintainer's first suspected cause: the MCP server running in more than one host (Cursor, Claude, Terminal) at once, so it fails; fix suggested is to run it in one place and reboot. *(opinion, medium; claude-blender-mcp)*
- c4: Maintainer pushed an updated addon.py to fix the issue; users reported it resolved after downloading the latest addon.py. *(doc, medium; claude-blender-mcp)*
- c5: Check for the hammer icon in Blender after the server loads to confirm the MCP server connected. *(doc, medium; common-mistakes-fixes)*
- c6: Multiple users on Windows reported the same timeout; the maintainer asked whether the problem was on Windows. *(data, low; claude-blender-mcp)*

## Numbers
- n1: **error code**: MCP error -32001 (Request Timed out) Error shown in Claude when a complex build request times out
- n2: **issue date**: 2025-03-16 Issue opened; fix pushed later in comments

## Techniques
- t1: **Single MCP host**: Run the blender-mcp server in only one client (Claude, Cursor, or terminal) at a time. Then reboot the PC. Maintainer's stated fix for conflicts.
- t2: **Update addon.py**: Download the latest addon.py from the repo, install it in Blender, and retry the request.

## Quotes (brief, for attribution)
> Is your MCP server running only in ONE place? If it runs on more than one (Cursor, Claude, Terminal) it won't work.  (ahujasid)
> an update was just pushed for this. Download the latest addon.py and try again?  (ahujasid)

## Points to
- https://github.com/ahujasid/mcp-for-blender/issues/50
