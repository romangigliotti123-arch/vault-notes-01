---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2410.06992
type: paper
author: Aleithan, Xue, Mohajer, Nnorom, Uddin, Wang
published: 2024-10-09
accessed: 2026-10-29
reliability: med (manual audit of one agent, small-ish)
---
# SWE-Bench+: enhanced coding benchmark
## Key claims
- Manual audit of SWE-Agent+GPT-4 resolved instances: 32.67% of successful patches had solution leakage (answer in the issue or comments); 31.08% passed only because of weak tests.
- Filtering both dropped the resolution rate from 12.47% to 3.97%. Same issues in SWE-bench Lite and Verified; over 94% of issues predate model knowledge cutoffs.
- Takeaway for a manager: a green test run can come from leaked answers or tests too weak to verify the claim.
## Quotable
> "32.67% of the successful patches involve cheating as the solutions were directly provided in the issue report or the comments"

## Used by
[[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
