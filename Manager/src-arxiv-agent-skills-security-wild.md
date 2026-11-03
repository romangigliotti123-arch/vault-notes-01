---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2601.10338
type: paper
author: Liu et al.
published: 2026-01-15
accessed: 2026-10-29
reliability: med-high: large scale, tool precision 86.7%
---
# Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale
## Key claims
- 42,447 skills collected from two marketplaces, 31,132 analysed: 26.1% contain at least one vulnerability across 14 patterns; data exfiltration 13.3%, privilege escalation 11.8%; 5.2% show high-severity patterns suggesting malicious intent.
- Skills that bundle executable scripts are 2.12x more likely to be vulnerable than instruction-only skills.
- SkillScan (static analysis + LLM classifier): 86.7% precision, 82.5% recall. Authors call for capability-based permissions and mandatory vetting.
## Quotable
> "implicit trust and minimal vetting" (abstract wording)

## Used by
[[topic-agent-security]], [[topic-skill-library-retrieval]]
