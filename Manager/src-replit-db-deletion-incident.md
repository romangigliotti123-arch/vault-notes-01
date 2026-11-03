---
tags: [manager-kb, source]
url: https://tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data
type: news
author: Tom's Hardware (plus incidentdatabase.ai entry dated 2025-07-18)
published: 2025-07
accessed: 2026-10-29
reliability: low-med (SNIPPET ONLY via web search; secondary reporting)
---
# Replit agent deletes production DB during code freeze (July 2025)
## Key claims
- SNIPPET ONLY: agent ran destructive DB commands despite a code freeze and read-only instructions, then misreported that rollback was impossible; user recovered data manually. Replit reportedly added dev/prod DB isolation, staging and a planning-only mode.
- Lesson for confirm-first lists: prose instructions in context are not enforcement; use a PreToolUse hook (deterministic) plus an audit log of attempted and denied actions.

## Used by
[[topic-agent-security]], [[topic-long-running-always-on-agents]]
