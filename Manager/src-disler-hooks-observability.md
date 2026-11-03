---
tags: [manager-kb, source]
url: https://github.com/disler/claude-code-hooks-multi-agent-observability
type: repo
author: disler (IndyDevDan)
published: undated
accessed: 2026-10-29
reliability: med (community OSS; README via summariser)
---
# claude-code-hooks-multi-agent-observability
## Key claims
- Pipeline: Claude Agents -> hook scripts -> HTTP POST -> Bun server -> SQLite (WAL) -> WebSocket -> Vue dashboard (ports 4000/5173). 12 hook events forwarded (PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, Notification, UserPromptSubmit, Stop, SubagentStart, SubagentStop, PreCompact, SessionStart, SessionEnd) by one `send_event.py`; `agent_id`/`agent_type` forwarded.
- Needs uv + Bun; a `stop_hook_active` guard prevents infinite hook loops.
- Proves the hooks-as-event-bus idea; for us the SQLite + sender script is the useful half, the Vue dashboard is not (nobody watches a dashboard on a phone).

## Used by
[[topic-observability]]
