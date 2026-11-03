---
type: research-source
id: gh-ahujasid-mcp-for-blender-i142
title: "ahujasid/mcp-for-blender#142 # FastMCP.__init__() got unexpected keyword argument 'description' when running blender-mcp"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/142"
published: "2025-08-01"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0403
relevance: 2
density: low
tags: ["research-source", "github", "claude-blender-mcp"]
---
# gh-ahujasid-mcp-for-blender-i142

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue (2025-08-01) on blender-mcp: `uvx blender-mcp` crashes with a TypeError because newer FastMCP no longer accepts a `description` kwarg. Workaround is to delete that argument in server.py. The maintainer later replied "Fixed". Useful for troubleshooting a Claude-Blender MCP setup. Nothing about Roblox.

## Claims
- c1: `uvx blender-mcp` fails at startup with TypeError: FastMCP.__init__() got an unexpected keyword argument 'description'. The latest FastMCP, installed automatically by uvx, dropped that argument. *(data, high; claude-blender-mcp)*
- c2: Workaround: edit blender_mcp/server.py (path is in the traceback, under the uv cache). Delete or comment out the `description=...` line in the FastMCP(...) call and keep `lifespan=server_lifespan`. *(experience, high; claude-blender-mcp)*
- c3: Reported on macOS (Apple Silicon, Python 3.13 and 3.12.4) and Windows 10 (Python 3.12.9). Blender was 4.3.2 or 4.5.0 and uv was 0.6.14 to 0.8.4. The failure is not tied to one OS, Python, Blender or uv version. *(data, high; claude-blender-mcp)*
- c4: Maintainer ahujasid replied 'Fixed'. The issue gives no fixed version number. This suggests unpinned dependencies pulled in by uvx can break the server when upstream APIs change (my inference). *(experience, medium; claude-blender-mcp)*

## Numbers
- n1: **Blender versions in reports**: 4.3.2, 4.5.0 Versions of users hitting the error
- n2: **uv versions in reports**: 0.6.14 to 0.8.4 Versions of users hitting the error

## Techniques
- t1: **Patch blender-mcp server.py to bypass the FastMCP description error**: Open the server.py path shown in the traceback (uv cache, blender_mcp/server.py). Remove the description= line from mcp = FastMCP('BlenderMCP', ..., lifespan=server_lifespan). Save and rerun uvx blender-mcp. Or update to the fixed release.

### Code: Fixed FastMCP constructor call with the description kwarg removed
```python
mcp = FastMCP(
    "BlenderMCP",
    lifespan=server_lifespan
)
```

## Points to
- ahujasid/mcp-for-blender (blender-mcp on PyPI)
- FastMCP
- uv / uvx
