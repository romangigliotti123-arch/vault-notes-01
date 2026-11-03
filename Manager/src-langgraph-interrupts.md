---
tags: [manager-kb, source]
url: https://docs.langchain.com/oss/python/langgraph/interrupts
type: official-doc
author: LangChain
published: undated
accessed: 2026-10-29
reliability: high (vendor doc)
---
# LangGraph interrupts (human-in-the-loop)
## Key claims
- `interrupt()` pauses; the checkpointer writes state so execution can resume later; "Graph waits indefinitely until you resume execution with a response"; resume needs the same thread id.
- On resume "the runtime restarts the entire node from the beginning", so side effects before the interrupt "should (ideally) be idempotent"; put side effects after the interrupt or in a separate node. Do not wrap interrupt() in a broad try/except.
- Lesson: an approval request is a persisted ledger state (`awaiting_approval`) with a timeout policy, not a blocking in-context question.

## Used by
[[topic-long-running-always-on-agents]]
