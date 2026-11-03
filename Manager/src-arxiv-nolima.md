---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2502.05167
type: paper
author: Modarressi et al.
published: 2025-02-07
accessed: 2026-10-29
reliability: high (abstract read via arXiv API; 13 models of early 2025)
---
# NoLiMa: Long-Context Evaluation Beyond Literal Matching
## Key claims
- Needle questions share minimal lexical overlap with the needle, so retrieval needs latent association. 13 LLMs claiming >=128K context: "At 32K, for instance, 11 models drop below 50% of their strong short-length baselines." GPT-4o fell from 99.3% to 69.7%.
- Reasoning/CoT models also struggle at length. Cause hypothesised: attention has a harder time without literal matches.
- Reading for us: a manager transcript is full of paraphrased, non-literal references ("the thing we did for the Linux box"), exactly the hard case; do not trust a 1M window to be uniformly usable.
## Quotable
> "At 32K, for instance, 11 models drop below 50% of their strong short-length baselines."

## Used by
[[topic-context-window-management]]
