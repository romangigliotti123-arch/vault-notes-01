---
tags: [manager-kb, source]
url: https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/
type: practitioner-blog
author: Simon Willison
published: 2025-10-22
accessed: 2026-10-29
reliability: high (practitioner; talk write-up)
---
# Living dangerously with Claude (YOLO mode talk)
## Key claims
- YOLO mode (`--dangerously-skip-permissions`) is very productive but its main risk is prompt injection: anyone who can get text into context can steer the next tool calls. Example: an agent tricked into sending GitHub tokens from env vars to an external server.
- AI-based injection detection is "not reliable enough to serve as a defense".
- Only credible mitigation: run the agent in a sandbox; prefer hosted sandboxes (e.g. Claude Code for the web) where the worst case is compromising someone else's machine. Restrict filesystem (easy) and network (hard but breaks the exfil step).
## Quotable
> (no verbatim quote captured; paraphrase only from the opened page)

## Used by
[[topic-agent-security]]
