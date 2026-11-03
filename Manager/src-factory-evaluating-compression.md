---
tags: [manager-kb, source]
url: https://factory.com/news/evaluating-compression
type: practitioner-blog
author: Factory Research
published: 2025-12-16
accessed: 2026-10-29
reliability: med (self-run eval, GPT-5.2 as judge, not independently replicated)
---
# Evaluating Context Compression for AI Agents
## Key claims
- Probe-based eval (Recall, Artifact, Continuation, Decision) over 36,611 production messages; GPT-5.2 judge, six dimensions on 0-5. Overall: Factory 3.70, Anthropic 3.44, OpenAI 3.35.
- **Artifact trail (which files/IDs were touched) is the weakest dimension for every method: 2.19-2.45.** "OpenAI's compression discards file paths as low-entropy content." "Artifact tracking remains an unsolved problem" -> keep a separate artifact/file-state index.
- Factory's gain attributed to **anchored iterative summarisation**: "only the newly-truncated span is summarized and merged with the existing summary" with fixed sections (intent, file modifications, decisions, next steps); Anthropic "regenerates the full summary on each compression".
- "Compression ratio turned out to be the wrong metric entirely" (OpenAI 99.3%, Anthropic 98.7%, Factory 98.6%).
- Reading for us: after any compaction the manager forgets exact paths, job IDs, agent names; so those must live on disk (job ledger), not only in the transcript.
## Quotable
> "Artifact trail is the weakest dimension for all methods, ranging from 2.19 to 2.45."

## Used by
[[topic-context-window-management]]
