---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/managed-agents
type: eng-blog
author: Lance Martin, Gabe Cemaj, Michael Cohen
published: 2026-04-08 (index page also listed Mar 25; page itself says Apr 8)
accessed: 2026-10-29
reliability: high (primary; architecture of Anthropic's hosted product)
---
# Scaling Managed Agents: Decoupling the brain from the hands
## Key claims
- Harnesses encode stale assumptions (example: context resets for Sonnet 4.5 became unnecessary on Opus 4.5).
- Three decoupled components: session (durable event log), harness (loop calling Claude and routing tools), sandbox (where code runs). Each swappable.
- A single container holding everything became a fragile "pet": failures lost sessions, hard to debug. Fix: harness outside the container, sandboxes provisioned on demand as tools.
- "Because the session log sits outside the harness, nothing in the harness needs to survive a crash": a crashed harness restarts by reloading the log. The log sits outside Claude's context window too; the harness can query/transform it before it reaches the model, so context management can change without losing history.
- Credentials never enter the sandbox (git token used at clone time; MCP calls via a proxy fetching credentials from a vault).
- Scaling: lazily creating containers cut p50 time-to-first-token ~60% and p95 >90%.
## Quotable
> "harnesses encode assumptions about what Claude can't do on its own"
> "The harness is never made aware of any credentials."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]], [[topic-long-running-always-on-agents]]
