---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-code/issues/11455 ; https://propakistani.pk/2026/10/16/claude-reportedly-resets-your-cache-to-charge-you-more/ ; https://github.com/392fyc/claude-handoff
type: practitioner-blog
author: various community (GitHub issue, news aggregator, plugin repo)
published: 2026-10-16 (ProPakistani article); others undated
accessed: 2026-10-29
reliability: low (snippet/WebFetch-summary only; framing and claims unverified)
---
# Community reports: session handoff pattern and the "cache TTL" story
## Key claims
- Handoff pattern (WebSearch snippets only, not opened): before ending a session the agent writes a handoff file (HANDOFF.md / progress file), `/clear`, the new session reads it. One skill treats a handoff as "a hypothesis to verify against the live codebase and git history", not ground truth. Claimed resume cost drops from "entire conversation history" to "one small file". A built-in `.claude/handoff.md` + SessionEnd hook exists only as a feature request (issue 11455). Plugin `claude-handoff` auto-generates a handoff near the context limit and launches a fresh session (not evaluated).
- ProPakistani (2026-10-16, WebFetch summary): repackages the Claude Code prompt-caching doc as "Claude reportedly resets your cache to charge you more": TTL is 1 h for the main conversation within plan usage, drops to 5 min when billing falls to usage credits, subagents/workflows/compaction always 5 min, model switch = full re-read. Everything it states is in the official doc ([[src-ccdocs-prompt-caching]]); the "to charge you more" framing is the outlet's, with no Anthropic comment. Use the official doc, not this article.
- Aggregators (snippet only): unresolved whether cache reads count at full rate toward subscription limits; conflicting community telemetry. Treat as unknown ([[src-openclawdc-subagents-limits]]).

## Used by
[[topic-context-window-management]], [[topic-model-effort-routing-cost]]
