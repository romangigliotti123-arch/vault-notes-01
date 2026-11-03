---
type: research-source
id: gh-ahujasid-ableton-mcp-i117
title: "ahujasid/ableton-mcp#117 MCP SERVER CRASH / Not found MACBOOK 26.5.2 (25F84)"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/ableton-mcp/issues/117"
published: "2026-07-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 0
density: low
tags: ["research-source", "github", "claude-blender-mcp"]
---
# gh-ahujasid-ableton-mcp-i117

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic: a GitHub issue about the AbletonMCP (Ableton Live) server, not Blender or Roblox. It covers a broken mcp dependency (mcp.server.fastmcp missing) with a uvx pin workaround, then Live freezing on create_midi_track. Nothing on bpy, blender-mcp, or the Roblox pipeline.

## Claims
- c1: Ableton MCP server failed on newer mcp package (mcp.server.fastmcp missing); a workaround pins the client via uvx --with 'mcp[cli]<2'. Pattern may matter for MCP setups generally; not Blender-specific. *(experience, medium; claude-blender-mcp)*

### Code: Workaround pinning mcp[cli] below 2 for an MCP server launched via uvx (Ableton, not Blender)
```json
"mcpServers": {
    "AbletonMCP": {
        "command": "uvx",
        "args": ["--with", "mcp[cli]<2", "ableton-mcp"]
    }
}
```

## Quotes (brief, for attribution)
> Every attempt hits the same wall: mcp.server.fastmcp doesn't exist.  (ahujasid)

## Points to
- https://github.com/ahujasid/ableton-mcp/issues/117
- https://github.com/ahujasid/ableton-mcp/issues/118
