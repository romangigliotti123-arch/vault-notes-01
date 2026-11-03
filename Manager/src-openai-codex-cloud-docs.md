---
tags: [manager-kb, source]
url: https://developers.openai.com/codex/cloud.md
type: official-doc
author: OpenAI
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: high (vendor docs, short page)
---
# OpenAI Codex Cloud
## Key claims
- Delegation surface: start tasks from web, mobile, desktop app, Slack or CLI; "Each task has its own workspace and can keep working while your computer is asleep"; review changed files and test results, request follow-up changes, then commit or open a PR. CLI can "list recent cloud chats and check their status".
- Environment = published, reusable setup (repos, tools, saved state) separate from the task's working state; credentials via "network secrets for allowed HTTPS services" and limited network destinations (per-environment secrets, not per-prompt).
- Codex "asks you for missing details or access" when preparing a project (clarification as a first-class step).
## Quotable
> Each task has its own workspace and can keep working while your computer is asleep.

## Used by
[[topic-cross-device-agent-control]], [[topic-personal-assistant-agents]]
