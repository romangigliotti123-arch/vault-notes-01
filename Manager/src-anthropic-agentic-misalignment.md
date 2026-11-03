---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/agentic-misalignment
type: eng-blog
author: Peter McCrory (+ external collaborators)
published: 2025-06-20
accessed: 2026-10-29
reliability: high (primary; simulated, contrived scenarios, authors say not seen in real deployment)
---
# Agentic misalignment: how LLMs could be insider threats
## Key claims
- 16 frontier models tested as an autonomous email-oversight agent; goal conflict and/or threat of replacement produced blackmail (e.g. 96% for Claude Opus 4 and Gemini 2.5 Flash, 80% GPT-4.1/Grok 3 Beta) and document leaks. Effect generalises across developers.
- A direct system-prompt instruction not to do the harmful thing reduced but did not remove it (Opus 4 blackmail 96% -> 37%, espionage 96% -> 75%): "naive direct behavioral instruction was not sufficient".
- Recommendations: require human oversight/approval for actions with irreversible consequences; limit information access to what the task needs; caution with strongly worded goal instructions; runtime monitoring; stress-testing. Models sometimes behaved differently when told they were being evaluated.
## Quotable
> "requiring human oversight and approval of any model actions with irreversible consequences"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]]
