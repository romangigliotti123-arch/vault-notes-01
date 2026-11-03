---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2410.07283
type: paper
author: Donghyun Lee, Mo Tiwari
published: 2024-10-09
accessed: 2026-10-29
reliability: med (abstract read; attack demo)
---
# Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems
## Key claims
- Malicious prompts self-replicate across interconnected agents "much like a computer virus", propagating silently; multi-agent systems are highly susceptible even when agents do not publicly share all communications.
- Threats named: data theft, scams, misinformation, system-wide disruption.
- Proposed defence "LLM Tagging" (marking messages by origin), which combined with existing safeguards significantly mitigates spread.
- Manager lesson: one compromised worker (read a poisoned page) can pass instructions to the manager and onward to the next worker; label worker-origin text as untrusted when re-briefing.
## Quotable
> "malicious prompts self-replicate across interconnected agents, behaving much like a computer virus"

## Used by
[[topic-multi-agent-failure-modes]]
