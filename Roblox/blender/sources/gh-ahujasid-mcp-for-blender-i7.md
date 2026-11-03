---
type: research-source
id: gh-ahujasid-mcp-for-blender-i7
title: "ahujasid/mcp-for-blender#7 running on cursor"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/7"
published: "2025-03-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i7

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #7 on ahujasid/mcp-for-blender (Mar 2025) about getting blender-mcp to show tools in Cursor. Maintainer's checklist: install uv, install and run the Blender addon server, set the Claude config file correctly, don't run uvx in a terminal, restart Blender and the client. Users report a Cursor "client closed" error fixed by restarting Cursor or running it as administrator. No Roblox content.

## Claims
- c1: blender-mcp tools not showing in Cursor MCP settings is most often caused by uv package manager missing; maintainer's first check. *(doc, medium; claude-blender-mcp)*
- c2: Cursor must be fully restarted after installing uv; one user confirmed tools appeared only after reopening Cursor. *(experience, medium; claude-blender-mcp)*
- c3: Blender addon must be installed and its server started inside Blender before the MCP client can connect. *(doc, medium; claude-blender-mcp)*
- c4: uvx command should not be run manually in a terminal; it is meant to be launched by the MCP client config (Claude Desktop). *(doc, medium; claude-blender-mcp)*
- c5: Cursor shows a 'client closed' MCP error; a user reported it resolved by running Cursor as administrator (Windows). Single anecdotal report. *(experience, low; common-mistakes-fixes)*
- c6: Install of uv on Windows was done via PowerShell per the readme; the blender-mcp package is then run with uvx from the config. *(experience, low; claude-blender-mcp)*
- c7: A user reported blender-mcp did not appear in Claude Desktop even after adding the script to the config file; no resolution recorded. *(experience, low; claude-blender-mcp)*

## Techniques
- t1: **MCP troubleshooting checklist**: 1) Confirm uv installed (uv --version). 2) Install Blender addon and start its server. 3) Verify MCP client config JSON points to uvx blender-mcp. 4) Don't run uvx in a terminal. 5) Restart Blender and the client.
- t2: **Run client as administrator (Windows)**: If Cursor shows 'client closed' for the MCP server, launch Cursor as administrator; reported to fix it, unverified by maintainer.

## Quotes (brief, for attribution)
> Do you have uv package manager installed on your device? If not, that is the problem.  (ahujasid)
> Ensure that uvx command isn't running in the terminal, only in Claude Desktop  (ahujasid)

## Points to
- https://forum.cursor.com/t/mcp-feature-client-closed-fix/54651/15
- https://github.com/ahujasid/mcp-for-blender
