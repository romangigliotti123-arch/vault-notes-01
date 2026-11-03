---
tags: [manager-kb, source]
url: https://www.anthropic.com/research/prompt-injection-defenses
type: eng-blog
author: Anthropic Alignment team
published: 2025-11-24
accessed: 2026-10-29
reliability: high (primary; numbers from one internal attacker)
---
# Mitigating the risk of prompt injections in browser use (Anthropic)
## Key claims
- Best-of-N adaptive attacker, 100 attempts per environment, ~2,200-3,200 attempts per bar. Attack success: Opus 4.5 8.0% model-only / 7.6% old safeguards / 1.4% improved; Sonnet 4.5 13.8/10.8/1.9; Haiku 4.5 12.0/11.1/2.4.
- Defences: RL on simulated injected web content; classifiers scanning all untrusted content entering context (hidden text, manipulated images, deceptive UI); continuous red teaming.
- Anthropic's framing: "prompt injection is far from a solved problem, particularly as models take more real-world actions"; "A 1% attack success rate ... still represents meaningful risk"; "No browser agent is immune".
- Figures are one internal attacker, not a measure of real-world risk. Models in this table are not the manager's current models; read as direction only.
## Quotable
> But prompt injection is far from a solved problem, particularly as models take more real-world actions.

## Used by
[[topic-agent-security]]
