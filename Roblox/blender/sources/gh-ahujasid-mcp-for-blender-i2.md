---
type: research-source
id: gh-ahujasid-mcp-for-blender-i2
title: "ahujasid/mcp-for-blender#2 Having connection issues even though both processes are running"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/2"
published: "2025-03-12"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0289
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-mcp"]
---
# gh-ahujasid-mcp-for-blender-i2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue thread on blender-mcp (ahujasid) connection failures between Claude Desktop and Blender addon. Maintainer advises: configure uvx in Claude Desktop config, don't run uvx in terminal (port conflict), install uv via brew on Mac, restart Blender/Claude, and Stop/Start addon server. Nothing on Roblox.

## Claims
- c1: Running `uvx blender-mcp` manually in a terminal is unnecessary; Claude Desktop launches it. The terminal instance may occupy the same port and block communication. *(experience, medium; claude-blender-mcp)*
- c2: Claude Desktop config: add mcpServers.blender with command uvx and args [blender-mcp] via Settings > Developer > Edit Config, then restart Claude and start the server in the Blender addon. *(doc, high; claude-blender-mcp)*
- c3: The addon server is 'finicky'; pressing Stop then Start in the addon may be needed. Connection reported inconsistent by users, working intermittently. *(experience, medium; claude-blender-mcp)*
- c4: On Mac, 'Claude failed to connect' was fixed by `brew install uv`; confirmed working by one user. *(experience, high; claude-blender-mcp)*
- c5: Troubleshooting checklist: uv installed; Blender addon installed and server running; uvx not running in terminal; restart Blender and Claude. *(doc, high; claude-blender-mcp)*
- c6: Failure symptom: tools visible in Claude (9 tools) but get_scene_info times out (MCP error -32001 Request timed out) while Blender addon shows a connected client on localhost:9876. *(data, medium; claude-blender-mcp)*

## Numbers
- n1: **Addon server port**: localhost:9876 BlenderMCP socket server address in Blender logs
- n2: **Tools exposed to Claude Desktop**: 9 tool count seen by reporter
- n3: **MCP timeout error code**: -32001 Request timed out on resources/list

## Techniques
- t1: **Claude Desktop blender-mcp setup**: Install uv (brew install uv on Mac). Edit Claude config to add blender server using uvx blender-mcp. Restart Claude. In Blender addon, start server. If failing, Stop/Start server and restart both apps.

### Code: Claude Desktop MCP config for blender-mcp
```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": [
                "blender-mcp"
            ]
        }
    }
}
```

## Points to
- https://github.com/ahujasid/blender-mcp/issues/5
- uv package manager
