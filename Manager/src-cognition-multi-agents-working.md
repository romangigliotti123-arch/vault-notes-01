---
tags: [manager-kb, source]
url: https://cognition.com/blog/multi-agents-working
type: eng-blog
author: Walden Yan (Cognition)
published: 2026-04-22
accessed: 2026-10-29
reliability: med (practitioner follow-up, one product)
---
# Multi-Agents: What's Actually Working (Cognition)
## Key claims
- Follow-up to the 2025 post: parallel "writer" swarms still see little adoption; what works keeps writes single-threaded and adds agents for intelligence, not for parallel edits.
- Working patterns: read-only helper/search subagents (mostly "tool calls" in spirit); review/verification loop (Devin + Devin Review); "smart friend" escalation to a stronger model; manager + child agents as "map-reduce-and-manage".
- Reviewer data point: catches about 2 bugs per PR, roughly 58% severe; works best when the reviewer starts with clean context (helps it reason from the diff, avoids context rot).
- Listed failure modes: conflicting implicit decisions from parallel writers; context rot; review loops that cycle, disobey user instructions or drift out of scope; weak primary models that do not know when to escalate; context loss in escalation (advisor guesses about files the primary never read); overly prescriptive managers lacking codebase context; false shared state ("Agents assume they share state with their children when they don't"); cost growth.
- Smart-friend escalation failed with a much weaker primary (SWE-1.5) but worked across frontier models (Claude, GPT).
## Quotable
> "Agents assume they share state with their children when they don't."
> "Devin Review catches an average of 2 bugs per PR, of which roughly 58% are severe" (vendor self-reported; verbatim re-checked)
## Note
WebFetch summary; quotes as returned by the summariser.

## Used by
[[topic-brief-prompt-engineering]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]], [[topic-report-formats-and-verification]]
