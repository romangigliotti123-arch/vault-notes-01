---
type: research-source
id: gh-ahujasid-ableton-mcp-i48
title: "ahujasid/ableton-mcp#48 Unable to connect to Ableton Live - \"Could not connect to Ableton. Make sure the Remote Script is running\""
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/ableton-mcp/issues/48"
published: "2025-10-10"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-ai", "other"]
---
# gh-ahujasid-ableton-mcp-i48

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue about ableton-mcp (an MCP server for Ableton Live, not Blender) failing with "Could not connect to Ableton." Reporter's setup used a Smithery npx config; a commenter fixed it by switching claude_desktop_config.json to a direct uvx ableton-mcp command. Off-topic for Blender/Roblox; only the generic MCP config pattern transfers.

## Claims
- c1: Source is about Ableton Live MCP, not blender-mcp; no Blender or bpy content present. *(doc, high; claude-blender-ai)*
- c2: Commenter reports the 'Remote Script not running' error was fixed by replacing the Smithery npx entry with a direct uvx ableton-mcp command in claude_desktop_config.json. *(experience, medium; claude-blender-ai)*
- c3: Reporter's MCP bridge used localhost port 9877 between the Remote Script and the MCP server; the error appears when the Remote Script is not listening. *(doc, medium; other)*
- c4: Reporter's setup used macOS IAC Driver Bus 1 as MIDI in/out, which the issue author states was verified but did not resolve the error. *(experience, low; other)*

## Numbers
- n1: **TCP port used by Remote Script**: 9877 (localhost) 
- n2: **Reporter versions**: Ableton Live 12.2.5 Trial; Claude Desktop 0.13.64; macOS 15.3.2 

## Techniques
- t1: **Direct uvx MCP config for ableton-mcp**: In claude_desktop_config.json, set the server key to AbletonMCP with command uvx and args [ableton-mcp]. Restart Claude Desktop. Reported by commenter as fixing the connection error versus the Smithery npx route.

### Code: Working Claude Desktop MCP entry for ableton-mcp (per commenter)
```json
{
  "mcpServers": {
      "AbletonMCP": {
          "command": "uvx",
          "args": [
              "ableton-mcp"
          ]
      }
  }
}
```

## Points to
- https://github.com/ahujasid/ableton-mcp
