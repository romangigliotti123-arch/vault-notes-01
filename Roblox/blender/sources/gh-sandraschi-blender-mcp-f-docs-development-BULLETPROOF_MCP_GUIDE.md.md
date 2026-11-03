---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-development-BULLETPROOF_MCP_GUIDE.md
title: "sandraschi/blender-mcp/docs/development/BULLETPROOF_MCP_GUIDE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/development/BULLETPROOF_MCP_GUIDE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0500
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-ai"]
---
# gh-sandraschi-blender-mcp-f-docs-development-BULLETPROOF_MCP_GUIDE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Doc in the sandraschi/blender-mcp repo about generic MCP-server hardening (sync health monitor, file validator, regex link parser) borrowed from advanced-memory-mcp note-sync problems. It contains nothing on Blender, bpy, Claude-with-Blender workflows or Roblox. Only marginally useful as general MCP robustness practice (timeouts, limits, non-greedy regex, no swallowed exceptions).

## Claims
- c1: The blender-mcp repo adds sync_health.py, file_validator.py and link_parser.py modules (about 600 lines each) with tests; they are note-sync features inherited from advanced-memory-mcp, not Blender scene tools. *(doc, medium; claude-blender-ai)*
- c2: The guide's general MCP practice: validate inputs first, set size/count/time limits, log errors instead of bare except/pass, degrade gracefully, and report progress during long loops. *(opinion, medium; claude-blender-ai)*
- c3: The guide says to avoid greedy regex like \[\[(.+)\]\] because of catastrophic backtracking, and to use bracket-excluding non-greedy patterns such as \[\[([^\[\]]+?)\]\]. *(doc, medium; claude-blender-ai)*
- c4: The author claims large speedups, such as 5,000 links going from a hang to 87ms. These are self-reported and not reproducible from the doc. The doc is dated Oct 2025 and is heavily self-congratulatory. *(doc, low; claude-blender-ai)*

## Numbers
- n1: **stall timeout**: 60s SyncHealthMonitor stall_timeout, check_interval 10s
- n2: **link parser limits**: 10,000 links, 5.0s parse time LinkParser defaults
- n3: **max file size**: 10 MB FileValidator rejection threshold
- n4: **tests**: 77+ 17 sync, 30 validator, 30 link parser

## Techniques
- t1: **Defensive MCP tool wrapper**: In an @mcp.tool() async function: validate input via a validator, parse with a timeout and item limit, fall back to saving without the failed feature, wrap persistence in try/except that logs and returns a clear error string.

### Code: Safe non-greedy wikilink regex instead of greedy pattern
```python
# BAD
r"\[\[(.+)\]\]"  # Catastrophic backtracking

# GOOD
r"\[\[([^\[\]]+?)\]\]"  # Non-greedy, safe
```

## Points to
- advanced-memory-mcp
- basic-memory-mcp
- FastMCP
