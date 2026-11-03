---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2307.03172
type: paper
author: Liu et al. (Stanford et al.)
published: 2023-07-06
accessed: 2026-10-29
reliability: high (abstract read via arXiv API; older models, effect partly mitigated in newer ones)
---
# Lost in the Middle: How Language Models Use Long Contexts
## Key claims
- Multi-document QA and key-value retrieval: "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models."
- Practical reading: put the standing rules at the start (CLAUDE.md, system prompt) and the live task/recitation at the end; the middle of a 100k+ transcript is the weakest part.
- Caveat: 2023-era models; newer Claude models are far better at recall, but Chroma/NoLiMa below show length-driven degradation persists.
## Quotable
> "performance is often highest when relevant information occurs at the beginning or end of the input context"

## Used by
[[topic-context-engineering]], [[topic-context-window-management]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
