---
tags: [manager-kb, source]
url: https://github.com/crewAIInc/crewAI
type: repo
author: CrewAI Inc
published: undated (created 2023-10-27; pushed 2026-10-28)
accessed: 2026-10-29
reliability: med (README read; marketing-heavy, no benchmarks)
---
# CrewAI (60,221 stars, MIT, 882 open issues)
## Key claims
- Two layers: **Crews** ("Teams of AI agents with true autonomy and agency ... role-based collaboration") and **Flows** ("production-ready, event-driven workflows" with conditional branching, `@start`/`@listen`/`@router` decorators, combinable with Crews). Process modes: sequential, and hierarchical ("automatically assigns a manager to the defined crew to properly coordinate the planning and execution of tasks through delegation and validation of results").
- Commercial layer: CrewAI AMP Suite (control plane, tracing, governance); claims "over 100,000 developers certified" via courses.
- Agents are defined by role / goal / backstory strings, the "role-play team" style.
- Critical read: README claims ("High Performance ... faster execution") give no numbers. The Flows layer being the "production" recommendation signals that free-form role-play crews were not reliable enough alone (consistent with MAST and Anthropic's "role-based decomposition causes telephone game").

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
