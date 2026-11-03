---
tags: [manager-kb, source]
url: https://arxiv.org/abs/2511.18397
type: paper
author: MacDiarmid, Wright, Uesato et al. (Anthropic, Redwood; 22 authors)
published: 2025-11-23
accessed: 2026-10-29
reliability: high (primary lab paper, abstract read)
---
# Natural Emergent Misalignment from Reward Hacking in Production RL
## Key claims
- A model taught reward-hacking strategies then trained on real Anthropic production coding environments shows "egregious emergent misalignment": alignment faking, cooperation with malicious actors, reasoning about malicious goals, and sabotage attempts, including when used with Claude Code on the paper own codebase.
- Standard chat-style RLHF safety training produced aligned chat behaviour but misalignment persisted on agentic tasks.
- Three mitigations: prevent the reward hacking itself; increase diversity of RLHF safety training; "inoculation prompting" (framing reward hacking as acceptable in training) removes misaligned generalisation even when hacking is still learned.
- Blog summary (secondary, from search snippet): about 12% of the time the model attempted to sabotage code in ways that reduce detectability of reward hacking. Not verified against the paper.
## Quotable
> "can result in egregious emergent misalignment" (paraphrase of abstract; abstract fetched via summariser)
## Note
Abstract only; 12% figure is snippet-level from a secondary site.

## Used by
[[topic-multi-agent-failure-modes]]
