---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2512.04864
type: paper
author: Dadi Guo, Qingyu Liu et al. (Shanghai AI Lab, HKUST)
published: 2025-12-04
accessed: 2026-10-29
reliability: med (200-task benchmark, 11 LLMs, preprint)
---
# Are Your Agents Upward Deceivers?
## Key claims
- Agentic upward deception: an agent facing environmental constraints (broken tools, mismatched sources) conceals the failure and does unrequested actions without reporting. Behaviours: guessing results, unsupported simulations, substituting unavailable sources, fabricating local files.
- Benchmark of 200 tasks, 5 types, 8 scenarios, 11 LLMs. Prompt-based mitigation ("explicit constraints") gives only limited reduction. Strict output formats and multi-task workflows amplify the behaviour.
- Search-result summary (not verified in the paper text): a dedicated report-failure tool reduced non-failure-reporting sharply; one model hid a broken-tool failure in 97.5% of one task.
## Quotable
> "conceals its failure and performs actions that were not requested without reporting"

## Used by
[[topic-multi-agent-failure-modes]]
