---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2403.14720
type: paper
author: Hines, Lopez, Hall, Zarfati, Zunger, Kiciman (Microsoft)
published: 2024-03-20
accessed: 2026-10-29
reliability: med-high (older, GPT-family models; abstract page only)
---
# Defending Against Indirect Prompt Injection Attacks With Spotlighting
## Key claims
- Family of prompt-engineering transformations that signal to the model where an input came from (so untrusted data is marked as data).
- Reported: attack success rate from over 50% to below 2% in GPT-family experiments with "minimal detrimental impact" on tasks. The abstract page did not name the techniques (delimiting / datamarking / encoding are from general knowledge, not verified here).
- Caveat: results are on 2024 models and non-adaptive attacks; Willison/NCSC argue probabilistic defences are not a boundary ([[src-willison-camel-post]], [[src-ncsc-prompt-injection-not-sqli]]).
## Quotable
> minimal detrimental impact to underlying NLP tasks

## Used by
[[topic-agent-security]]
