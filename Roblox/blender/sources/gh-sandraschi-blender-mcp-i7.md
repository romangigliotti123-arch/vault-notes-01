---
type: research-source
id: gh-sandraschi-blender-mcp-i7
title: "sandraschi/blender-mcp#7 `blender-mcp --list-tools` fails because `FastMCP.list_tools()` is not awaited"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/issues/7"
published: "2026-10-21"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai"]
---
# gh-sandraschi-blender-mcp-i7

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #7 in sandraschi/blender-mcp: the `blender-mcp --list-tools` CLI helper fails with "object of type 'coroutine' has no len()" because FastMCP.list_tools() is async and not awaited in blender_mcp/cli.py:91. The MCP server itself works (responds to tools/list). Proposed fix: await the call before computing or displaying the list. Says nothing about Roblox export or pipeline.

## Claims
- c1: blender-mcp 0.11.1 `--list-tools` CLI fails on Python 3.14 with FastMCP 3.4.7: 'object of type coroutine has no len()'. *(demo, high; claude-blender-ai)*
- c2: Root cause reported: async FastMCP.list_tools() result treated as sync collection in blender_mcp/cli.py:91 (list_available_tools()); RuntimeWarning 'never awaited' shown. *(demo, high; claude-blender-ai)*
- c3: The blender-mcp server starts and responds to MCP tools/list; the bug is limited to the CLI helper, not the server. *(demo, high; claude-blender-ai)*
- c4: Suggested fix: await FastMCP.list_tools() before calculating/displaying the tool list. Fix status not stated in the issue text. *(opinion, medium; claude-blender-ai)*
- c5: Workaround hint printed by CLI: run 'blender-mcp --stdio' first to initialize the server; the issue reporter says this message is misleading for this bug. *(demo, low; automation-and-creator-workflows)*

## Numbers
- n1: **blender-mcp version**: 0.11.1 installed CLI version in the reported failure
- n2: **FastMCP version**: 3.4.7 version used with Python 3.14
- n3: **Failing line**: blender_mcp/cli.py:91 list_available_tools() call site

## Techniques
- t1: **Await async FastMCP list_tools**: Make the CLI helper async or run the coroutine (e.g., asyncio.run) and only then take len()/iterate the result, avoiding 'coroutine has no len()'.

## Quotes (brief, for attribution)
> object of type 'coroutine' has no len()  (sandraschi)
> coroutine 'FastMCP.list_tools' was never awaited  (sandraschi)

## Points to
- https://github.com/sandraschi/blender-mcp/issues/7
