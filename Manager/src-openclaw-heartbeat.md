---
tags: [manager-kb, source]
url: https://docs.openclaw.ai/gateway/heartbeat.md
type: official-doc
author: OpenClaw
published: undated
accessed: 2026-10-29
reliability: low-med (page is a migration notice; rest from web-search snippets of third-party guides)
---
# OpenClaw heartbeat / automation jobs
## Key claims
- Heartbeat monitoring is now ordinary "automation jobs" with their own schedule, prompt and run history (`openclaw doctor --fix` converts old monitors). First-setup "Proactive check" every 30 minutes by default.
- Silent outcome token `NO_REPLY` ("Return NO_REPLY when a check has no visible update"); `record_result` logs without messaging; `activeHours` restricts to a timezone window; `idleOnly` gives foreground work priority; `skipIfScratchEmpty` skips model call if the checklist is empty.
- Search-snippet only (third-party guides, unverified): HEARTBEAT.md read each tick; empty/comment-only file => model call skipped (cost saver); cron jobs persisted in SQLite under ~/.openclaw and survive restarts but need the Gateway running.

## Used by
[[topic-long-running-always-on-agents]]
