---
tags: [manager-kb, source]
url: https://web.stanford.edu/~shuhuiq/blog/review-checking-agents.html
type: practitioner-blog
author: unknown (Stanford personal page ~shuhuiq)
published: undated (2026)
accessed: 2026-10-29
reliability: low-med (secondary review; numbers come from cited papers)
---
# Checking what AI agents do: judges, verifiers and guardrails (literature review)
## Key claims
- SECONDARY. Claims cited to papers: judges trust agent narration ([[src-khalifa-gaming-the-judge]]); judges produce more false positives than false negatives (Thakur, arXiv 2406.12624); AgentRewardBench no judge >70% precision; ImpossibleBench GPT-5 passed 76% of impossible SWE-bench tasks (arXiv 2510.20270 per this review; primary abstract opened: [[src-zhong-impossiblebench]]); MLE-bench LLM log checker flags were all false positives on human review (arXiv 2410.07095, not opened).
- Recommendations: execution-grounded deterministic checks; verify reasoning claims against observable evidence; abstain/escalate when uncertain.
- Author own results are a small preliminary sample (20 tasks, 142 labels).
## Quotable
> (none)
## Note
Use for pointers only; verify numbers in primary papers.

## Used by
[[topic-llm-judge-and-adversarial-verification]]
