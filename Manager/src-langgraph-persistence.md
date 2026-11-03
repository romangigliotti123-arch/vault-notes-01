---
tags: [manager-kb, source]
url: https://docs.langchain.com/oss/python/langgraph/persistence
type: official-doc
author: LangChain
published: undated
accessed: 2026-10-29
reliability: med (page was high level; mechanism details not on the page)
---
# LangGraph persistence / checkpointers
## Key claims
- Checkpointers "persist a thread's graph state as checkpoints"; scoped by `thread_id`; uses listed: conversation continuity, human-in-the-loop, time travel, fault tolerance.
- InMemorySaver loses all checkpoints on process restart; production uses PostgresSaver, local uses SqliteSaver.
- "Over long conversations, checkpoints accumulate": prune or set a retention policy (state growth is a real operational cost).
- Page does not describe determinism/idempotency/pending writes (those are in the linked checkpointers/durable-execution pages, not verified).

## Used by
[[topic-long-running-always-on-agents]]
