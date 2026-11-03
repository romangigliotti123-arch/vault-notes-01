---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2406.18665
type: paper
author: Ong et al. (LMSYS / Berkeley)
published: 2024-06-26
accessed: 2026-10-29
reliability: high (abstract read via arXiv API; full text not opened)
---
# RouteLLM: Learning to Route LLMs with Preference Data
## Key claims
- Routers choose between a strong and a weak LLM per query, trained on human preference data with augmentation; "significantly reduces costs-by over 2 times in certain cases-without compromising the quality of responses".
- Routers transfer: performance holds "even when the strong and weak models are changed at test time".
- Limitation relevant to us (my reading): routers classify single-turn queries; a manager's job types are few and known, so a static preset table per job type captures most of the value.
## Quotable
> "reduces costs-by over 2 times in certain cases-without compromising the quality of responses"

## Used by
[[topic-model-effort-routing-cost]]
