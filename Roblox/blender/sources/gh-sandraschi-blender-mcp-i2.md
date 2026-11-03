---
type: research-source
id: gh-sandraschi-blender-mcp-i2
title: "sandraschi/blender-mcp#2 Windows: script_execute always fails — shell=True + pre-quoted args corrupt the init functionality test command"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/issues/2"
published: "2026-06-10"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0276
relevance: 3
density: medium
tags: ["research-source", "github", "claude-blender-ai"]
---
# gh-sandraschi-blender-mcp-i2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on sandraschi/blender-mcp: on Windows, script_execute fails because the init functionality test uses shell=True with pre-quoted args (cmd.exe corrupts it), producing a misleading "Blender not found". Fix is list-form subprocess without shell and a 60s timeout. A comment adds a second bug: children inherit the MCP stdio pipe as stdin and hang, so stdin must be redirected.

## Claims
- c1: On Windows, sandraschi/blender-mcp script_execute fails after a ~2-minute stall with a misleading 'Blender not found' even when BLENDER_EXECUTABLE is correct; the cause is the init-time functionality test. *(data, high; claude-blender-ai)*
- c2: Root cause: _test_blender_functionality() pre-quotes the blender path and script path and runs the joined string with shell=True. cmd.exe quote-stripping mangles it, Blender spins (a stray headless process used 98s+ CPU), and the 30s timeout fires. *(data, high; claude-blender-ai)*
- c3: The same command run as an argument list without a shell exits in 1.9s with BLENDER_TEST_SUCCESS. _build_blender_command(), used for real script runs, was already correct (list form), so only the init gate was broken. *(data, high; claude-blender-ai)*
- c4: After the fix (list form on all platforms, no shell, timeout 60s), executor init plus a create-cube-and-export-FBX script completes in 3.7s end-to-end. *(data, medium; claude-blender-ai)*
- c5: Second defect, reported in a comment: neither the sync subprocess.run nor asyncio.create_subprocess_exec redirects stdin. Under a real stdio MCP server, Blender children inherit the MCP protocol pipe as stdin and hang until timeout. The fix passed from a console but failed under stdio. *(experience, medium; claude-blender-ai)*
- c6: The reporter suggests raising the Blender test timeout from 30s to 60s because a cold first launch building shader/font caches can exceed 30s on slower machines. *(opinion, medium; claude-blender-ai)*

## Numbers
- n1: **control run time with list args**: 1.9 s Blender --background test script, no shell
- n2: **end-to-end after fix**: 3.7 s init + create cube + export FBX
- n3: **test timeout**: 30 s -> 60 s proposed change
- n4: **Blender version**: 5.1.0 environment where bug was observed

## Techniques
- t1: **Run Blender headless via subprocess list form**: Build argv as [blender_path, '--background', '--factory-startup', '--python', script, '--'] and call subprocess.run(list) with no shell=True. CreateProcess handles Windows quoting for paths with spaces.
- t2: **Redirect child stdin under stdio MCP**: When the MCP server runs over stdio, give spawned Blender processes a stdin that is not the protocol pipe (e.g. DEVNULL) in both subprocess.run and asyncio.create_subprocess_exec. This is implied by the comment, which was truncated.

### Code: Proposed fix for the init test command
```python
blender_cmd = [
    str(self.blender_path),
]
...
    test_script_path,
...
# all platforms:
result = subprocess.run(blender_cmd, capture_output=True, text=True, timeout=60, check=False)
```

## Points to
- https://github.com/sandraschi/blender-mcp/issues/2
- FastMCP 3.2.4
- Claude Code (stdio transport)
