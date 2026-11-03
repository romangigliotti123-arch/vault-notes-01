---
type: research-source
id: gh-ahujasid-mcp-for-blender-i279
title: "ahujasid/mcp-for-blender#279 \"Consistent ~5 minute delay / MCP timeout on every tools/call despite server listening and responding correctly"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/issues/279"
published: "2026-07-06"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes"]
---
# gh-ahujasid-mcp-for-blender-i279

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue #279 in ahujasid/mcp-for-blender (blender-mcp). Users report every tools/call takes about 4-5 minutes: client times out with MCP -32001 at 4 min, then the server returns a valid result about 1 min later. Maintainer pointed to commit 3ab8925; a commenter said the latest code still fails. A later comment cites PR #292 as targeting the root cause. No Roblox content.

## Claims
- c1: Reporter on Windows with addon.py v1.2 and latest blender-mcp via uvx sees every tools/call take ~5 min, even trivial scene-info reads; Blender executes the command correctly. *(experience, medium; claude-blender-mcp)*
- c2: Client cancels at exactly 4 minutes with MCP error -32001 'Request timed out'; server returns a valid result ~1 minute later. *(experience, medium; claude-blender-mcp)*
- c3: Reporter suspects persistent-connection recv logic in blender_mcp/server.py stalls until an internal timeout before reconnecting; this is a hypothesis, not confirmed. *(opinion, low; claude-blender-mcp)*
- c4: Maintainer said the issue should be fixed by commit 3ab8925; a commenter reported the downloaded code still failed, so the fix was not confirmed working. *(doc, medium; common-mistakes-fixes)*
- c5: Still reproduced in Aug 2026 by a user on Windows with Claude Desktop and uvx blender-mcp, on Blender 5.0.1 and 4.2 LTS, addon version 1.5 / protocol 4. *(experience, medium; claude-blender-mcp)*
- c6: Antivirus uninstalls, Windows Defender Firewall and Defender real-time protection were ruled out as the cause by one user. *(experience, medium; common-mistakes-fixes)*
- c7: Log symptom: 'Incomplete JSON response' appears on the bridge side during these long calls. *(experience, low; claude-blender-mcp)*

## Numbers
- n1: **tools/call latency**: ~5 min (4 min to client timeout, ~1 min to result) Reported on Windows, addon v1.2, trivial scene-info call
- n2: **addon version / protocol**: 1.5 / protocol 4 Reported by jakesong21, Blender 5.0.1 and 4.2 LTS

## Contradictions flagged
- Commit 3ab8925 fixes the issue. (vs Commenter Korkerumaviking reports the latest GitHub version still does not work after download.)

## Points to
- https://github.com/ahujasid/mcp-for-blender/issues/279
- https://github.com/ahujasid/blender-mcp/commit/3ab892510cc0e5435ba5e611c01fb1021fbde8de
- PR #292 (cited, no link given in text)
