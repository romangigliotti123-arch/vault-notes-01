---
tags: [manager-kb, source]
url: https://docs.openhands.dev/sdk/guides/agent-stuck-detector
type: official-doc
author: OpenHands (All Hands AI)
published: undated
accessed: 2026-10-29
reliability: high (official SDK doc)
---
# OpenHands SDK: Agent stuck detector
## Key claims
- Detects: same action -> same observation 4+ times; same action -> error 3+ times; 3+ consecutive agent messages with no user input; two action-observation pairs alternating 6+ cycles; repeated context-window errors. Compares by content not identity (tool name, action, thought; error message), only events after the last user message.
- On by default (`stuck_detection=True`); can halt execution. GitHub issue (OpenHands/software-agent-sdk #762, snippet only) notes thresholds are hardcoded and a legitimate polling task can trip them; PR #1240 (snippet only) notes multi-action LLM turns evade per-action counts.

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-multi-agent-failure-modes]]
