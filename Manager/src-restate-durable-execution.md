---
tags: [manager-kb, source]
url: https://docs.restate.dev/concepts/durable_execution
type: official-doc
author: Restate
published: undated
accessed: 2026-10-29
reliability: high (vendor doc; fetch model summary with quotes)
---
# Restate: durable execution
## Key claims
- "Restate tracks every step of your code execution in a journal." After failure: "Restate replays the journal, skipping completed steps and resuming from exactly where it left off."
- External-call "run actions" are retried with exponential backoff, policy set in service config.
- Idempotency key in request headers => "Restate will automatically ensure that requests are deduplicated"; duplicates return the original result. Page says each invocation "runs exactly once regardless of failures" (effect-level claim; page does not discuss at-least-once delivery explicitly).

## Used by
[[topic-long-running-always-on-agents]]
