---
tags: [manager-kb, source]
url: https://github.com/google/adk-python
type: repo
author: Google
published: undated (created 2025-04-01; README says ADK 2.0; pushed 2026-10-28)
accessed: 2026-10-29
reliability: high (README + adk-docs a2a/intro.md read raw)
---
# Google Agent Development Kit (ADK) 2.0 (22,034 stars, Apache-2.0)
## Key claims
- "Code-first Python framework for building, evaluating, and deploying" agents; model-agnostic though optimised for Gemini. ADK 2.0 features: **Workflow Runtime** (graph engine with routing, fan-out/fan-in, loops, retry, state, human-in-the-loop, nested workflows), **Task API** (structured agent-to-agent delegation, multi-turn or single-turn controlled output), modular multi-agent hierarchies, MCP tools.
- ADK's A2A intro doc gives the clearest "when to use a protocol" rule: use A2A when the agent is a separate standalone service, maintained by another team/organisation, in a different language/framework, or needs a strong formal contract; do NOT use it for internal code organisation, performance-critical internal operations, or sub-agents needing shared memory/context ("A2A's network overhead and serialization/deserialization would be counterproductive") - prefer local sub-agents.

## Used by
[[topic-multi-agent-frameworks]]
