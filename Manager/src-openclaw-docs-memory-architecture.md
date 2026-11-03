---
tags: [manager-kb, source]
url: https://docs.openclaw.ai/concepts/memory-architecture.md ; /concepts/standing-intents.md ; /concepts/user-model.md
type: official-doc
author: OpenClaw project
published: undated (fetched 2026-10-29)
accessed: 2026-10-29
reliability: med (project docs; claims about "production audits" not independently verified)
---
# OpenClaw memory architecture, standing intents, user model
## Key claims
- Design principles: (1) "No hidden state" - the model only remembers what is in workspace files, all inspectable/editable; (2) "Writing is the hard part": retrieval over notes is competitive, what degrades memory is unreliable write-time curation (cites LongMemEval arXiv:2410.10813), so curation moves off the reply path into a background "dreaming" pass; (3) "The write path is the security boundary" (provenance enforced at write time instead of scanning for poisoned facts later); (4) fixed code checks with model judgment inside them; (5) memory failures never block replies.
- Tiers: Instructions (AGENTS.md, human-written only, always injected) / Curated core (MEMORY.md, USER.md, written only by gated consolidation or direct user request) / Episodic (daily notes, transcripts; retrieved on demand, not injected) / Prospective (standing intents + cron jobs) / Review (DREAMS.md, never injected).
- Provenance classes owner / agent / untrusted / system; "production audits have found the overwhelming majority of auto-captured memories to be restatements of runtime instructions, heartbeat noise, and recall feedback loops". Fixes: session-kind gating (cron, heartbeat, sub-agent sessions never create durable memory candidates) and recall-loop prevention (recalled content never re-extracted).
- Tainting: after a tool result from the network, the rest of that turn is marked untrusted for memory classification.
- Standing intents (event-conditioned prospective memory): defaults cooldown 24h, max 3 fires, expiry 90 days, only owner-authenticated channel senders can create; three intention tiers: time-based -> scheduled task, event-based -> standing intent, aspiration -> markdown with a review date.
## Quotable
> Writing is the hard part. Retrieval over notes files is competitive with far heavier designs; what degrades memory systems is unreliable write-time curation.

## Used by
[[topic-knowledge-management-rag]], [[topic-personal-assistant-agents]], [[topic-skill-library-retrieval]]
