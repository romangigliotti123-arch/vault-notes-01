---
type: research-source
id: gh-sandraschi-blender-mcp-i1
title: "sandraschi/blender-mcp#1 Installation instructions don't work"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/issues/1"
published: "2026-05-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 2
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# gh-sandraschi-blender-mcp-i1

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue reporting that blender-mcp install docs fail on Windows 11 with Blender 5.1.1. The uvx mcpb install command is not on PyPI. After pip install blender-mcp, the blender-mcp entry point is not on PATH. Maintainer says mcpb was removed from docs and recommends git clone plus pip install -e . Relevant only to the Claude-to-Blender MCP setup step; no Roblox content.

## Claims
- c1: 'uvx mcpb install sandraschi/blender-mcp' fails: mcpb is not in the package registry (PyPI); mcpb is an internal packaging tool per maintainer. *(doc, high; claude-blender-ai)*
- c2: After 'pip install blender-mcp' on Windows, the blender-mcp command is not recognized in PowerShell; the entry script lands in %APPDATA%\Python\Python3XX\Scripts which is often not on PATH. *(experience, medium; claude-blender-ai)*
- c3: Maintainer's fix: git clone the repo, cd into it, run 'pip install -e .', then use the module form instead of the bare blender-mcp command. *(doc, medium; claude-blender-ai)*
- c4: Reporter's setup: Windows 11 25H2, Blender 5.1.1, Blender MCP addon installed and enabled from blender.org/lab/mcp-server before running the server. *(experience, medium; claude-blender-ai)*
- c5: HTTP server mode command 'blender-mcp --http --host 0.0.0.0 --port 8001' fails with CommandNotFoundException on Windows when the script is not on PATH. *(experience, medium; claude-blender-ai)*
- c6: Old troubleshooting section only gave the Linux PATH fix ($HOME/.local/bin), which does not help on Windows; maintainer says it was updated. *(doc, medium; other)*
- c7: Claude Code's own attempt tried alternatives (mcp install, mcpm install) that were not verified; these are unconfirmed suggestions in the issue. *(experience, low; automation-and-creator-workflows)*

## Numbers
- n1: **Blender version tested**: 5.1.1 Reporter's Blender version on Windows 11 25H2
- n2: **HTTP server port**: 8001 Example command: blender-mcp --http --host 0.0.0.0 --port 8001

## Techniques
- t1: **Editable install from clone**: Clone sandraschi/blender-mcp, cd into the folder, run pip install -e ., then launch via module form (python -m) rather than the PATH script on Windows.

### Code: Maintainer-recommended install from repo (fix for missing blender-mcp command)
```powershell
git clone https://github.com/sandraschi/blender-mcp.git
cd blender-mcp
pip install -e .
```

## Quotes (brief, for attribution)
> mcpb is an internal packaging tool and is not published to PyPI, so uvx can't find it. That instruction should never have been in the docs.  (sandraschi)
> On Windows the entry-point script lands in %APPDATA%\Python\Python3XX\Scripts\ which is often not in PATH.  (sandraschi)

## Contradictions flagged
- Docs instruct 'uvx mcpb install sandraschi/blender-mcp' as a valid install step for Claude Desktop. (vs Maintainer comment says mcpb is internal and not on PyPI; instruction removed.)
- Old troubleshooting covers blender-mcp PATH fix via $HOME/.local/bin. (vs Maintainer says this Linux-only fix is useless on Windows.)

## Points to
- https://github.com/sandraschi/blender-mcp/issues/1
- https://github.com/sandraschi/blender-mcp/blob/main/docs/installation.md
- https://github.com/sandraschi/blender-mcp
- https://www.blender.org/lab/mcp-server/
