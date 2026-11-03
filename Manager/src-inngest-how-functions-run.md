---
tags: [manager-kb, source]
url: https://www.inngest.com/docs/learn/how-functions-are-executed
type: official-doc
author: Inngest
published: undated
accessed: 2026-10-29
reliability: high (vendor doc)
---
# Inngest: how functions are executed
## Key claims
- "Inngest saves completed steps, retries failed work, and resumes after waits." Resume = replay handler and return saved step results; "Code outside a step can run again each time the handler replays" (side effects must be inside steps).
- Step ID is hashed into the state key; changing a function while runs are in flight needs versioning.
- Per-step retries; "Make refundOrder idempotent because a refund can succeed before Inngest saves the step result and retries the step" (the crash window between effect and checkpoint).
- Waits (delay / waitForEvent) consume no compute; `waitForEvent` returns null on timeout - a human-in-the-loop primitive.

## Used by
[[topic-long-running-always-on-agents]]
