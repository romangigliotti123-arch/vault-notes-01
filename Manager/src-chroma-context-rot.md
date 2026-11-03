---
tags: [manager-kb, source]
url: https://www.trychroma.com/research/context-rot
type: practitioner-blog
author: Chroma research
published: 2025-07 (undated in fetch)
accessed: 2026-10-29
reliability: med-high (benchmarked 18 models; vendor of a vector DB has a retrieval interest)
---
# Context Rot: How Increasing Input Tokens Impacts LLM Performance
## Key claims
- 18 LLMs (GPT-4.1, Claude 4, Gemini 2.5, Qwen3 families): "their performance grows increasingly unreliable as input length grows" even on simple tasks; tested 8 input lengths x 11 needle positions.
- "Even a single distractor reduces performance relative to the baseline"; four distractors compound it.
- Lower needle-question semantic similarity degrades faster with length.
- Counter-intuitive: shuffled (incoherent) haystacks beat coherent ones across all 18 models ("structural coherence consistently hurts").
- LongMemEval: focused prompts (~300 tokens) far outperform full prompts (~113k tokens) across all models.
- Conclusion: "what matters more is how that information is presented" -> context engineering.
## Quotable
> "Even a single distractor reduces performance relative to the baseline"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-knowledge-management-rag]]
