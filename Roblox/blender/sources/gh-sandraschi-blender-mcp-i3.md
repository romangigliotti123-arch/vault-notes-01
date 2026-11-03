---
type: research-source
id: gh-sandraschi-blender-mcp-i3
title: "sandraschi/blender-mcp#3 Windows: every Blender-launching tool times out — child process inherits the MCP server's stdio pipe (fix: stdin=DE"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/issues/3"
published: "2026-07-02"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0270
relevance: 3
density: high
tags: ["research-source", "github", "claude-blender-ai"]
---
# gh-sandraschi-blender-mcp-i3

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on sandraschi/blender-mcp: on Windows, tools launching `blender --background` as a subprocess hang until 60s timeout because the child inherits the MCP server's stdio stdin pipe. Adding stdin=DEVNULL fixes it. Fixed in v0.11.0 (commit 066a2be). Same bug reported in the official Blender MCP server's background helper.

## Claims
- c1: On Windows, blender-mcp tools that launch `blender --background` (e.g. script_execute) hang until the 60s timeout with MCP error -32001, because the child inherits the MCP server's live stdio stdin pipe and deadlocks. *(experience, high; claude-blender-ai)*
- c2: The same command run directly from a shell finishes in ~1.5s, so Blender itself was not the problem. *(data, high; claude-blender-ai)*
- c3: Fix: pass stdin=DEVNULL to asyncio.create_subprocess_exec and to subprocess.run in _test_blender_functionality. After it, script_execute returns within a few seconds on Blender 5.1 / Windows 11. *(experience, high; claude-blender-ai)*
- c4: The reporter says the official Blender MCP server (projects.blender.org/lab/blender_mcp) has the identical bug in its `blender --background` helper. The same one-line fix takes its CLI tools from a 120s timeout to a 4s success. *(experience, medium; claude-blender-ai)*
- c5: Other Windows issues in the same repo: `@asgi_app.route` in server.py crashes at import on FastMCP 3.4+ (route removed), and shell=True with pre-quoted args corrupts the command (issue #2). *(experience, medium; claude-blender-ai)*
- c6: The maintainer fixed it in commit 066a2be (v0.11.0), adding stdin=subprocess.DEVNULL at both call sites, and fixed issue #2 in the same release. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **timeout before fix (blender-mcp)**: 60s script_execute hangs until MCP request timeout
- n2: **direct shell run time**: ~1.5s blender --background --python-expr completes normally
- n3: **official Blender MCP CLI tools**: 120s timeout -> 4s before vs after the stdin=DEVNULL fix
- n4: **tested versions**: Blender 5.1.0, Windows 11 25H2, commit 8bf3376 reporter environment

## Techniques
- t1: **Prevent stdio deadlock when spawning headless Blender from an MCP server**: When an MCP server in stdio mode spawns `blender --background`, pass stdin=DEVNULL (asyncio.subprocess.DEVNULL or subprocess.DEVNULL) so the child does not inherit the JSON-RPC stdin pipe. Apply this to both async and sync subprocess calls.

### Code: Fix for Blender subprocess hang on Windows under MCP stdio transport
```python
process = await asyncio.create_subprocess_exec(
    *cmd,
    stdin=asyncio.subprocess.DEVNULL,
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE,
    cwd=self.temp_dir,
    env=os.environ.copy(),
)
```

## Points to
- https://github.com/sandraschi/blender-mcp
- projects.blender.org/lab/blender_mcp
- FastMCP
