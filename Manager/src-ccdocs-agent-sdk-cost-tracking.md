---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/agent-sdk/cost-tracking.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated
accessed: 2026-10-29
reliability: high (official; full page read)
---
# Track cost and usage (Agent SDK / claude -p result message)
## Key claims
- "The `total_cost_usd` and `costUSD` fields are client-side estimates, not authoritative billing data" (price table bundled at build time). For real billing use the Usage and Cost API / Console. On a subscription these USD numbers are API-equivalent, not what is charged.
- Parallel tool calls produce several assistant messages sharing one message id with identical usage: "deduplicate by ID to avoid double-counting". In the SDK stream per-step `output_tokens` is a placeholder (count from `message_start`); read output tokens from the result message. (Local check: usage in Claude Code TRANSCRIPT files carries realistic final output counts, identical across the blocks of one message id, so dedupe-by-id is the only fix needed there.)
- Whole-tree accounting: result `usage` excludes subagents; `total_cost_usd` and `modelUsage` include them. `modelUsage` gives per-model tokens and cost; `costBasis` says which price table priced it (v2.1.246+).
- A resumed session's result already includes the session's earlier spend (v2.1.277+): do not sum results of resumed calls. After a crash the final `error_during_execution` result may carry zeroed cost fields; recover from the previous result.
- Cache: track `cache_creation_input_tokens` and `cache_read_input_tokens` separately; on a subscription within included usage, own turns get the 1-hour TTL, dropping to 5 minutes once on usage credits.

## Used by
[[topic-observability]]
