---
type: research-source
id: gh-ahujasid-mcp-for-blender-i144
title: "ahujasid/mcp-for-blender#144 Claude AI desktop no longer connecting to Blender MCP server?"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/144"
published: "2025-08-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i144

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #144 on ahujasid/mcp-for-blender: Claude Desktop stopped connecting to the Blender MCP server (2025-08-02). Thread blames a breaking change in the mcp Python SDK shipped in a patch version. Workaround: pin mcp==1.12.2 via requirements file and UV_CONSTRAINT. Nothing about Roblox export or import.

## Claims
- c1: Claude Desktop lost connection to the Blender MCP server while the Blender addon reported no errors; maintainer said it worked in local tests. *(experience, medium; claude-blender-mcp)*
- c2: A user attributes the failure to a breaking change in the mcp Python SDK shipped in a patch release, affecting blender-mcp installs from the prior week. *(opinion, low; claude-blender-mcp)*
- c3: FastMCP team suggested a temporary fix: pin mcp==1.12.2 in requirements.txt and pass it to uvx via --with-requirements, or set UV_CONSTRAINT in the env block. *(doc, medium; common-mistakes-fixes)*
- c4: One user reported Claude Desktop stuck in a running state for Blender MCP while the same server worked in Cursor. *(experience, low; claude-blender-mcp)*
- c5: A user reported a working fix by pointing the Claude config command at the installed blender-mcp binary in ~/.local/bin instead of running via uvx. *(experience, low; claude-blender-mcp)*

## Numbers
- n1: **Pinned mcp version workaround**: mcp==1.12.2 
- n2: **Local Blender MCP server URL in manual connection**: http://localhost:9876 
- n3: **Issue date**: 2025-08-02 

## Techniques
- t1: **Pin mcp SDK version for uvx launch**: Create requirements.txt containing mcp==1.12.2. Set UV_CONSTRAINT to that file in the Claude config env block, or pass --with-requirements to uvx. Restart Claude Desktop.

### Code: Claude Desktop config workaround: pin mcp via UV_CONSTRAINT for uvx-launched blender-mcp (FastMCP team suggestion)
```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": [
                "blender-mcp"
            ],
             "env": {
                    "UV_CONSTRAINT": "requirements.txt"
                  }
        }
    }
}
```

## Quotes (brief, for attribution)
> Someone merged a breaking change in a patch release, which makes me think it would be wise if blender-mcp was locked to a specific version of mcp.  (ahujasid)

## Contradictions flagged
- Blender MCP connection failures in Claude Desktop caused by mcp SDK breakage (vs Maintainer states the server works fine in local testing; root cause not confirmed in thread)

## Points to
- https://github.com/modelcontextprotocol/python-sdk/pull/1198
- https://github.com/ahujasid/blender-mcp/issues/144
- Cherry Studio (reported same failure)
- GitHub Copilot (reported working with blender-mcp)
