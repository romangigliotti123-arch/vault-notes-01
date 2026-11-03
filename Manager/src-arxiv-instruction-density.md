---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2507.11538 ; https://arxiv.org/abs/2509.21051 ; https://arxiv.org/abs/2307.03172
type: paper
author: Jaroslawicz, Whiting, Shah, Maamari (IFScale); Harada, Yamazaki, Taniguchi, Marrese-Taylor (ManyIFEval); Liu, Lin, Hewitt, Paranjape et al. (Lost in the Middle)
published: 2025-07-15 (IFScale); 2025-09-25 (ManyIFEval); 2023-07-06 (Lost in the Middle)
accessed: 2026-10-29
reliability: med (abstracts read via arXiv API; models tested are not the 2026 Claude family)
---
# Instruction density and position effects (abstract level)
## Key claims
- IFScale: 500 keyword-inclusion instructions in a business-report task, 20 models, 7 providers: "even the best frontier models only achieve 68% accuracy at the max density of 500 instructions"; three degradation patterns, "bias towards earlier instructions", distinct error categories.
- ManyIFEval/StyleMBPP: "performance consistently degrades as the number of instructions increases" (up to 10 text / 6 code instructions, ten LLMs); a logistic regression on instruction COUNT predicts success with ~10% error.
- Lost in the Middle: performance "is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle".
- For briefs: each extra constraint costs adherence; put the goal and the hard constraints at the start, the report contract at the end, and keep the middle for reference material; prune rules that don't apply to this job rather than pasting all of CLAUDE.md. (Inference by the note's author; the papers measure older models and synthetic tasks.)

## Used by
[[topic-brief-prompt-engineering]]
