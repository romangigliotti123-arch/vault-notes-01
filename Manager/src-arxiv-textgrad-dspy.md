---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2406.07496 ; https://arxiv.org/abs/2310.03714
type: paper
author: Yuksekgonul et al. (TextGrad, Stanford); Khattab et al. (DSPy, Stanford)
published: 2024-06-11 (TextGrad); 2023-10-05 (DSPy)
accessed: 2026-10-29
reliability: med (abstracts only read via arXiv API; not full text)
---
# TextGrad and DSPy (abstract level)
## Key claims
- TextGrad: "backpropagates textual feedback provided by LLMs to improve individual components of a compound AI system"; PyTorch-like API; users supply only the objective function.
- DSPy: replaces hard-coded "prompt templates, i.e. lengthy strings discovered via trial and error" with declarative modules plus a compiler optimising a metric; "within minutes of compiling" pipelines outperform standard few-shot prompting "generally by over 25% and 65%" (GPT-3.5, llama2-13b).
- Common thread with OPRO/GEPA: treat the prompt as a parameter optimised against a measurable metric and textual error feedback; needs a metric and dev set, which a personal assistant manager does not have by default.
- Snippet/abstract only: no claim in this note depends on the full text.

## Used by
[[topic-brief-prompt-engineering]]
