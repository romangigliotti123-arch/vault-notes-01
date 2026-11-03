---
type: research-source
id: gh-ahujasid-mcp-for-blender-i52
title: "ahujasid/mcp-for-blender#52 The claude desktop cannot connect to blender_mcp in error: AttributeError: 'ProactorEventLoop' object has no att"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/52"
published: "2025-03-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 3
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i52

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #52 on ahujasid/mcp-for-blender: Claude Desktop shows blender-mcp disconnected on Windows 10 (Blender 4.3.2, uv-managed Python 3.10.16). Logs show socketpair ConnectionError in asyncio ProactorEventLoop. Thread discussion covers reinstalling, single-instance running, a thread-based addon.py fix (PR), and a direct-python workaround. Not Roblox-specific.

## Claims
- c1: Windows error: Claude Desktop reports blender-mcp disconnected; log shows ConnectionError 'Unexpected peer connection' in socket.socketpair, then AttributeError 'ProactorEventLoop' has no attribute '_ssock'. Reporter used Blender 4.3.2. *(data, high; claude-blender-mcp)*
- c2: Maintainer advice: blender-mcp must run in only one place (Cursor, Claude, or Terminal); running in several breaks it. Reboot the PC afterward. *(doc, medium; common-mistakes-fixes)*
- c3: On macOS, starting only Claude Desktop spawned four blender-mcp-related processes (uv tool uvx plus duplicate Python blender-mcp runs), matching the multiple-instance theory. *(data, medium; claude-blender-mcp)*
- c4: Commenter embogomolov attributes the failure to addon.py using bpy.app.timers for socket work; the timer silently unregisters, leaving a registered but unresponsive 'zombie' server. *(opinion, medium; claude-blender-mcp)*
- c5: Proposed fix: replace the BlenderMCPServer class in addon.py with a thread-based socket implementation. Maintainer later pushed the PR and asked users to re-download addon.py. *(experience, medium; claude-blender-mcp)*
- c6: Workaround reported by handsomeevil-78 on Windows 10: point Claude Desktop config at 'python' running blender_mcp server.py directly instead of the uvx launch. Reporter blamed uvx version; unverified. *(experience, low; common-mistakes-fixes)*
- c7: Suggested uv reinstall via PowerShell (Set-ExecutionPolicy RemoteSigned, then astral install script) did not fix the same reporter's error. *(experience, medium; common-mistakes-fixes)*
- c8: Maintainer could not reproduce on Blender 4.4 and asked whether the reporter used it; the Windows failure appeared on 4.3.2. *(experience, low; claude-blender-mcp)*
- c9: Deleting and reinstalling the MCP server in Claude plus downloading latest addon.py did not fix the reporter's error. *(experience, medium; claude-blender-mcp)*

## Numbers
- n1: **Blender version**: 4.3.2 (failing); 4.4 not reproduced by maintainer 
- n2: **Python runtime**: cpython 3.10.16 via uv on Windows 10 
- n3: **Log date**: 2025-03-17 
- n4: **Duplicate processes (macOS)**: 4 blender-mcp processes after starting Claude Desktop only 

## Techniques
- t1: **Single-instance check**: Ensure blender-mcp runs from only one client (Claude, Cursor, or terminal). Kill stray processes, then reboot and retry.
- t2: **Thread-based socket server in addon**: Replace BlenderMCPServer in addon.py: run socket listening in a threading.Thread rather than bpy.app.timers. Reported as stable by one user.
- t3: **Direct python launch**: Configure Claude Desktop to run python with the path to blender_mcp/server.py instead of uvx. Reported as working on Windows 10.

### Code: Workaround: Claude Desktop MCP config launching server.py directly with python (reported by handsomeevil-78)
```json
"blender": {
  "command": "python",
  "args": [
    "<YOUR PATH>\\blender-mcp-main\\src\\blender_mcp\\server.py"
  ]
}
```

### Code: Suggested uv install on Windows (viv3k19; did not work for one reporter)
```powershell
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Quotes (brief, for attribution)
> Is your MCP server running only in ONE place? If it runs on more than one (Cursor, Claude, Terminal) it won't work.  (ahujasid)
> The root cause was in how the network communication was handled - relying on Blender's timer system (bpy.app.timers.register) for socket operations.  (ahujasid)

## Contradictions flagged
- Running in multiple places breaks blender-mcp (maintainer theory) (vs Reporter's error persisted after deleting and reinstalling; a single-instance explanation did not cover that case)
- Reinstalling uv via the astral PowerShell script fixes Windows setup (vs handsomeevil-78 reports it did not work in their environment)
- Timer-based sockets are the root cause (embogomolov) (vs Maintainer could not reproduce the issue; no maintainer confirmation of root cause in thread)

## Points to
- https://github.com/ahujasid/mcp-for-blender/issues/52
- https://modelcontextprotocol.io/docs/tools/debugging
- https://astral.sh/uv/install.ps1
- bpy.app.timers (Blender API)
- embogomolov pull request to ahujasid/mcp-for-blender
