---
type: research-source
id: gh-ahujasid-mcp-for-blender-i137
title: "ahujasid/mcp-for-blender#137 Blender + Claude MCP connection failing"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/137"
published: "2025-07-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i137

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #137 on ahujasid/mcp-for-blender: Windows and Mac users see "MCP blender: Server Disconnected" in Claude Desktop. Maintainer reports a fix, users say it works, then it recurs. A commenter proposes pinning uvx to Python 3.12. Thin on technical detail; no root cause given.

## Claims
- c1: Claude Desktop shows 'MCP blender: Server Disconnected' when the blender-mcp server fails to start; reported on Windows and Mac starting around 2025-07-24. *(experience, high; claude-blender-mcp)*
- c2: Maintainer ahujasid fixed the disconnect server-side; several users confirmed it worked. No root cause is stated in the thread. *(experience, medium; claude-blender-mcp)*
- c3: Issue recurred later for at least one user even with latest Blender and Claude; a separate new issue was filed. *(experience, medium; claude-blender-mcp)*
- c4: Community workaround: set the Claude config command to 'uvx' with args '--python 3.12 blender-mcp', swapping in the user's installed Python version. *(opinion, medium; common-mistakes-fixes)*
- c5: Claude Desktop was updated to 0.12.55 (d55c63) around the time the disconnects started; a reporter suggested it might be related. Unverified. *(opinion, low; claude-blender-mcp)*

## Numbers
- n1: **Claude Desktop version**: 0.12.55 (d55c63) Reported by a user as updated just before the Mac disconnects began
- n2: **Suggested Python version for uvx**: 3.12 Community workaround config pins --python 3.12

## Techniques
- t1: **Pin Python for uvx launch**: In claude_desktop_config.json, set mcpServers.blender.command to 'uvx' and args to ['--python','3.12','blender-mcp']. Replace 3.12 with the Python version installed locally. Restart Claude Desktop.

### Code: Community-suggested Claude Desktop MCP config for blender-mcp launched via uvx with a pinned Python
```json
"mcpServers": {
    "blender": {
      "command": "uvx",
      "args": [
        "--python",
        "3.12",
        "blender-mcp"
      ]
    }
  }
```

## Quotes (brief, for attribution)
> MCP blender: Server Disconnected. For troubleshooting guidance, please visit our debugging documentation  (ahujasid)
> Try with this config (switch the python version with the one that you have)  (ahujasid)

## Contradictions flagged
- Maintainer says the issue is fixed, but a user reports it returned on the latest versions. (vs ahujasid's 'should be working now' comment)

## Points to
- https://github.com/ahujasid/mcp-for-blender/issues/137
