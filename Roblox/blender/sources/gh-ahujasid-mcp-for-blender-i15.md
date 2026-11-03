---
type: research-source
id: gh-ahujasid-mcp-for-blender-i15
title: "ahujasid/mcp-for-blender#15 an issue connecting to Blender"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/15"
published: "2025-03-13"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i15

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #15 on ahujasid/mcp-for-blender (blender-mcp) about Claude failing to connect to Blender. Shows no Roblox content. Useful only for connection troubleshooting: the Blender addon's socket on port 9876 can stay bound or stale after a session, so Claude loses the link. Reported workarounds: kill the 9876 listener, restart Blender then Claude, start the Blender MCP server before Claude, and run only one MCP server instance.

## Claims
- c1: Blender MCP connection error 'Could not connect to Blender. Make sure the Blender addon is running' occurs; port 9876 stale connections are a reported cause. *(experience, medium; claude-blender-mcp)*
- c2: Workaround reported by users: kill all processes on port 9876, restart Blender, then restart Claude; it worked for one user. *(experience, medium; claude-blender-mcp)*
- c3: Maintainer advice: ensure only one MCP server instance runs, not also in a terminal, only in Claude or Cursor. *(opinion, medium; claude-blender-mcp)*
- c4: Reported order that works: open Claude first, then start Blender's MCP server from the addon. *(experience, low; claude-blender-mcp)*
- c5: Maintainer states the setup should work on Claude's free plan; some users reported it failing, others reported it working. *(opinion, low; claude-blender-mcp)*
- c6: Diagnose with netstat -ano | findstr :9876 on Windows to see listeners and ESTABLISHED client connections. *(experience, medium; common-mistakes-fixes)*

## Numbers
- n1: **port**: 9876 
- n2: **issue date**: 2025-03-13 

## Techniques
- t1: **Free the Blender MCP socket**: Find the process holding port 9876 (netstat -ano | findstr :9876), kill it, restart Blender and its addon server, then restart Claude; a second MCP instance (terminal plus Claude) can block the port.

## Quotes (brief, for attribution)
> Could not connect to Blender. Make sure the Blender addon is running.  (ahujasid)
> Make sure it's not running on terminal, just either on Claude or cursor  (ahujasid)

## Contradictions flagged
- Setup works on Claude free plan (vs A user reports it did not work on a paid plan, and the maintainer's free-plan claim is unverified)

## Points to
- https://github.com/ahujasid/mcp-for-blender
