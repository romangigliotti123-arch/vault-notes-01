---
tags: [manager-kb, source]
url: https://www.braintrust.dev/docs/integrations/developer-tools/claude-code
type: official-doc
author: Braintrust
published: undated
accessed: 2026-10-29
reliability: low-med (SNIPPET ONLY via web search summary; page not opened)
---
# Braintrust: Claude Code tracing
## Key claims
- SNIPPET ONLY: plugin `trace-claude-code@braintrust-claude-plugin` records session, turn, model-call, tool and subagent spans; one Claude Code session = one trace; needs `jq`; config `~/.claude/braintrust.json`; transcripts on disk can be sent after the fact (past sessions); OTel route exists for no-plugin setups.
- Pattern shared with Langfuse/LangSmith/OpenObserve: Stop-hook reads transcript and ships it. All SaaS-first.

## Used by
[[topic-observability]]
