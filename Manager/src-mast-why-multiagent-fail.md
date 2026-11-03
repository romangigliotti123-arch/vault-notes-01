---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2503.13657
type: paper
author: Cemri, Pan, Yang, Agrawal, Chopra, Tiwari, Keutzer, Parameswaran, Klein, Ramchandran, Zaharia, Gonzalez, Stoica (UC Berkeley)
published: 2025-03-17 (v3 2025-10-26)
accessed: 2026-10-29
reliability: high (peer-visible, full text read)
---
# Why Do Multi-Agent LLM Systems Fail? (MAST taxonomy)
## Key claims
- MAST-Data: 1642 annotated execution traces (v3 text) from 7 MAS frameworks (ChatDev, MetaGPT, HyperAgent, AppWorld, AG2/MathChat, Magentic-One, OpenManus); 150 traces used to build the taxonomy; Cohen kappa 0.88 inter-annotator; an LLM-as-judge annotator pipeline scales it.
- 14 failure modes in 3 categories. FC1 system design/specification: FM-1.1 disobey task spec 11.8%, FM-1.2 disobey role spec 1.5%, FM-1.3 step repetition 15.7%, FM-1.4 loss of conversation history 2.80%, FM-1.5 unaware of stopping conditions 12.4%.
- FC2 inter-agent misalignment: FM-2.1 conversation reset 2.20%, FM-2.2 fail to ask for clarification (proceeds on wrong assumptions) 6.80%, FM-2.3 task derailment 7.40%, FM-2.4 information withholding 0.85%, FM-2.5 ignored other agent input 1.90%, FM-2.6 reasoning-action mismatch 13.2%.
- FC3 task verification: FM-3.1 premature termination 6.20%, FM-3.2 no or incomplete verification 8.20%, FM-3.3 incorrect verification 9.10%.
- Insight 1: failure is not only the model; a better-designed MAS with the same LLM gains. Insight 2: context/protocol fixes are often insufficient for inter-agent misalignment (needs social reasoning). Insight 3: "Multi-Level Verification is Needed"; sole reliance on final-stage low-level checks is inadequate.
- Verifier presence is not a silver bullet: ChatDev chess program passed superficial checks (compiled) but had runtime bugs because it never validated against actual game rules.
- Interventions (Table 5): AG2 GSM-Plus GPT-4 84.75 -> 89.75 with improved prompt, 85.50 with new topology; ChatDev ProgramDev 25.0 -> 34.4 (prompt) -> 40.6 (new topology); HumanEval 89.6 -> 90.3 -> 91.5. Giving the CEO role the final say gave +9.4% task success. Authors: isolated fixes are not enough for robust reliability.
- Failure-mode correlations are moderate (max 0.63): similar surface symptoms (missing info) can have different root causes (withholding vs ignoring vs context loss), so an LLM annotator can conflate them.

## Appendix L/M prompt wording (read from the HTML text)
- The AG2/MathChat "structured prompt with verification section" added: "Verification Steps: Before presenting your final answer, please complete the following steps: ... Verify your solution step by step, documenting each part of the verification process in a designated VERIFICATION section. Once you are confident in your verification and certain of your answer, present your final result..." plus "Handling Missing Data: If a problem is deemed unsolvable due to missing data, return \boxed{'None'}" (an explicit honest-failure output). Accuracy 84.75 -> 89.75 (GPT-4).
- ChatDev modified prompts: the Software Test Engineer is told "Check the edge cases and special cases and instances for the task we are doing. Do not miss any cases. Do not suffice with generic and superficial cases."; the CEO role is given "authority to make final decisions and terminate conversations when appropriate" (the +9.4% change).
- Lesson used in [[topic-multi-agent-failure-modes]]: one role owns the stop decision; verification is a named output section, and an explicit "cannot be solved from the given data" output exists.
## Quotable
> "Multi-Level Verification is Needed" (Insight 3; "sole reliance on final-stage, low-level checks is inadequate")
## Note
PDF fetch via WebFetch failed (binary); numbers read from arxiv.org/html/2503.13657 text. Percentages are share of failed traces per mode as reported in the v3 HTML.

## Used by
[[topic-brief-prompt-engineering]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]], [[topic-report-formats-and-verification]]
