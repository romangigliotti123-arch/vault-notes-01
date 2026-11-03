---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/hooks.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312, fetched raw .md, 282 KB)
accessed: 2026-10-29
reliability: high (official reference, raw markdown)
---
# Hooks reference (Claude Code docs)
## Key claims
- 5 handler types: `command`, `http`, `mcp_tool`, `prompt`, `agent` (agent hooks "experimental", up to 50 turns, default 60 s). ~30 events incl. SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolBatch, Notification, SubagentStart/Stop, TaskCreated/Completed, Stop, StopFailure, InstructionsLoaded, ConfigChange, CwdChanged, FileChanged, WorktreeCreate/Remove, PreCompact/PostCompact, PreModelSwitch/PostModelSwitch, SessionEnd, Elicitation. Prompt/agent hooks supported on PreToolUse, PostToolUse, Stop, SubagentStop, UserPromptSubmit, TaskCompleted etc.; NOT on SessionStart, SubagentStart, Notification, SessionEnd, PreCompact.
- Locations: `~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, managed, plugin `hooks/hooks.json`, skill frontmatter (active after invocation), subagent frontmatter. Entries merge across levels; identical handler in several files runs once. Max 24 prompt/agent hooks concurrently per session incl. subagents (2.1.312).
- Matcher: exact string / `A|B` list when only letters, digits, `_`, `-`, space, `,`, `|`; otherwise unanchored JS regex. Matchers are case-sensitive. `if` field (permission-rule syntax e.g. `Bash(git push *)`) narrows handlers on tool events; exactly one rule, "best-effort": "use the permission system rather than a hook to enforce a hard allow or deny."
- Exit codes: 0 = success (JSON on stdout applied), 2 = blocking error (stderr is the reason; fields cannot override block), other = non-blocking error (action proceeds). `onFailure: "block"` (2.1.295+) makes a crashed/timed-out hook block the action (fail closed). JSON must be the only stdout; profile echo in Git Bash breaks it.
- PreToolUse decisions in `hookSpecificOutput`: `permissionDecision` allow|deny|ask|defer (+`updatedInput`, `additionalContext`); precedence deny > defer > ask > allow. `defer` only works in `-p` mode with a single tool call. A hook "deny" blocks even in bypassPermissions / `--dangerously-skip-permissions` (hooks fire before any mode check) (hooks-guide.md). A hook "allow" never overrides deny/ask rules.
- `additionalContext` (SessionStart, SubagentStart, UserPromptSubmit, Pre/PostToolUse, Stop/SubagentStop) injected as system reminder; 10,000 char cap (overflow saved to file, 2,000-char preview). Write as facts, not imperatives: "Text framed as out-of-band system commands can trigger Claude's prompt-injection defenses". For static rules prefer CLAUDE.md.
- SessionStart: matchers startup|resume|clear|compact|fork; stdout becomes context; can return `sessionTitle`, `initialUserMessage` (-p), `watchPaths`, `reloadSkills`; on resume receives `seconds_since_last_response`, `context_tokens`, `prompt_cache_likely_expired`, `estimated_cache_write_usd` (2.1.251+) -> a hook can warn what a stale resume will cost. `CLAUDE_ENV_FILE` to persist env (bash only).
- Stop / SubagentStop: `decision:"block"` + `reason` (or exit 2) continues the turn; check `stop_hook_active`; 8-consecutive-block cap (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`). Input includes `last_assistant_message`, `background_tasks`, `session_crons` (distinguish "done" from "waiting on background work"). `hookSpecificOutput.additionalContext` gives non-error feedback and continues. `/goal` is a built-in session-scoped prompt Stop hook.
- Prompt hook: model returns `{ok, reason, impossible}`; `impossible:true` lets Stop end. On PreToolUse `ok:false` ends the turn unless `continueOnBlock:true`. Default model is the background (small) model; `model` field overridable. Best-practices page: prompt/agent hooks "ask another model to decide, so it isn't deterministic either. For real enforcement, use a command or http hook".
- Async: `async:true` (command only) cannot block; output delivered next turn; killed at `-p` teardown; `asyncRewake` wakes Claude on exit 2 even when idle.
- `terminalSequence` field emits OSC notifications only in interactive sessions. Notification matcher values include `permission_prompt`, `idle_prompt`, `agent_needs_input`, `agent_completed`, `quota_auto_resume_fired`.
- Windows: PowerShell hooks via `"shell":"powershell"` or exec form (`command: powershell.exe`, `args:[...]`); env var `CLAUDE_CODE_BRIDGE_SESSION_ID` set while Remote Control is connected (2.1.199+). Debug: `claude --debug-file`, `/debug`, Ctrl+O transcript.
## Quotable
> "Because the `if` filter is best-effort, use the permission system rather than a hook to enforce a hard allow or deny."
> "A hook that returns `permissionDecision: \"deny\"` blocks the tool even in `bypassPermissions` mode or with `--dangerously-skip-permissions`."
> "A `prompt` or `agent` hook asks *another model* to decide, so it isn't deterministic either." (from best-practices.md, see [[src-ccdocs-best-practices]])

## Used by
[[topic-agent-security]], [[topic-claude-code-features]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-multi-agent-failure-modes]], [[topic-observability]]
