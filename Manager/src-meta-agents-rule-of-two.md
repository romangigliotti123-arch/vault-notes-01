---
tags: [manager-kb, source]
url: https://ai.meta.com/blog/practical-ai-agent-security/
type: eng-blog
author: Meta (no named authors on page)
published: 2025-10-31
accessed: 2026-10-29
reliability: high (vendor framework with explicit caveats)
---
# Agents Rule of Two (Meta)
## Key claims
- Prompt injection still unsolved. In a session an agent should have at most TWO of: [A] process untrustworthy inputs, [B] access sensitive systems or private data, [C] change state or communicate externally.
- If a task needs all three, do not run autonomously: require supervision (human approval) or a fresh context window.
- Examples: Travel assistant [AB] (outbound actions need human confirmation, trusted URLs only); Web research assistant [AC] (restrictive sandbox, no preloaded session data); Internal coder [BC] (filters untrusted data by author lineage, human review). An agent may switch configuration within a session (e.g. disable external comms before touching internal systems).
- Caveats: does not cover hallucination/excess privilege; not a finish line (users can blindly approve warnings); supplements defence in depth and least privilege; HITL is disruptive for background processes (open challenge).
- Inspired by Chromium's Rule of Two and Willison's trifecta.
## Quotable
> agents must satisfy no more than two of the following three properties within a session

## Used by
[[topic-agent-security]]
