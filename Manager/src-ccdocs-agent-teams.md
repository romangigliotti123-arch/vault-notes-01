---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/agent-teams
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (page mentions v2.1.309)
accessed: 2026-11-01
reliability: high (official; full page read)
---
# Agent teams (experimental)
## Key claims
- Disabled unless `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. While enabled, a subagent that Claude NAMES (Agent tool `name`) launches as a teammate with no confirmation, so teams can form unasked; set the var to `0` to get plain subagents back. Not available in `claude -p` or Agent SDK sessions (a named subagent runs as an ordinary subagent).
- Teammates are full sessions with a shared task list (pending/in progress/completed, dependencies, file-lock claiming) and JSON mailboxes; the lead's conversation history does NOT carry over; no nested teams; one team per session; the lead is fixed; in-process teammates are not restored on resume.
- Use for parallel research or review, competing-hypothesis debugging, independently owned modules; NOT for sequential tasks or same-file edits. Start with 3-5 teammates and 5-6 tasks each; "Three focused teammates often outperform five scattered ones". Two teammates on one file overwrite each other: assign file ownership.
- Hooks as quality gates: TeammateIdle, TaskCreated, TaskCompleted (exit 2 blocks and sends feedback).
- Teammate model order: spawn prompt, definition `model`, `CLAUDE_CODE_SUBAGENT_MODEL`, lead's model; teammates inherit lead effort and permission mode (bypass propagates); a message from another agent never counts as user consent.
- Known failure modes: teammates stop early on errors; the lead may start implementing instead of waiting; task status lags and blocks dependents.
## Used by
[[topic-orchestration-patterns]], [[topic-claude-code-features]], [[topic-model-effort-routing-cost]]
