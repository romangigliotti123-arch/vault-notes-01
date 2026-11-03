---
tags: [manager-kb, source]
url: https://developers.googleblog.com/en/developers-guide-to-multi-agent-patterns-in-adk/
type: eng-blog
author: Shubham Saboo (Google)
published: 2025-12-16 (just before the Jan-Oct 2026 window; KB has no ADK note)
accessed: 2026-11-01
reliability: med (vendor guide, pseudocode, no measurements)
---
# Developer's guide to multi-agent patterns in ADK
## Key claims
- Eight patterns: sequential pipeline, coordinator/dispatcher, parallel fan-out/gather, hierarchical decomposition (sub-agents as tools), generator-and-critic, iterative refinement, human-in-the-loop, composite. Start with a simple sequential chain before adding loops.
- Parallel agents share session state: give each a unique output key to avoid race conditions (same rule as one-writer-per-artifact).
- Generator-critic: the critic signals pass or returns error feedback; a loop agent exits on pass (a bounded quality gate).
- Code samples are pseudocode; "Reliability comes from decentralization and specialization" is a claim, not a result.
## Used by
[[topic-orchestration-patterns]], [[topic-multi-agent-frameworks]]
