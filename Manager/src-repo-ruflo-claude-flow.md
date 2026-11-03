---
tags: [manager-kb, source]
url: https://github.com/ruvnet/ruflo
type: repo
author: rUv (Reuven Cohen) - ruvnet/ruflo, formerly ruvnet/claude-flow
published: undated (created 2025-06-02; pushed 2026-10-28; latest release v3.63.8 on 2026-10-28)
accessed: 2026-10-29
reliability: med (README + issues read; the README is promotional, the issues are the honest part)
---
# ruflo (ex claude-flow): "agent meta-harness for Claude Code and Codex"
## Key claims (README) vs what the evidence says
- Stats (gh api): 79,952 stars, 9,378 forks, 980 open issues, MIT, repo size ~660 MB, releases almost daily.
- Pitch: "Agent = Model + Harness. Ruflo is the harness"; 100+ specialised agents, swarms with "Queen-led hierarchy (Raft, Byzantine, Gossip)", HNSW vector memory, "SONA self-learning", "Intelligent routing (89% accuracy)", "12 auto-triggered workers", federation across machines (mTLS + ed25519), 27 hooks, a plugin marketplace (`/plugin marketplace add ruvnet/ruflo`, ruflo-core, ruflo-console, ruflo-mods ...). Requires Claude Code >= 2.1.287.
- Promotional tells in the README itself: a download badge whose alt text says "Illustrative download counter starts at 98,000,000 and adds varied amounts each second in a 30 second loop. Verified dataset: 97,022,120 download events" (an animated counter, not a live number); a benchmark gist where "ruflo wins cold start, single turn, RSS by 1.3x-1953x" against LangGraph/AutoGen/CrewAI - those are startup/memory metrics, not task-success metrics. No SWE-bench or task-success comparison against plain Claude Code is given in the current README.
- Issues filed by contributors/automation scans (opened and read): #4557 `coordination_sync` "reports a synchronization that never happens" (a `// Simulate sync` 50 ms timeout then returns `{success:true, action:'synchronized'}`); #1058 V3 MCP hook handlers "return success responses but don't actually persist any data" (`recorded: true // LIES`, random fake durations); PR #4456 "WorkerDispatchService implements the 12 worker triggers with static placeholder results ... invented counts, recommendations, 'benchmarks'" (fix: mark results `synthetic: true`); PR #2494 (open) "Replaces coordination_orchestrate and coordination_metrics stubs with a real multi-agent executor". Several of these were later closed/fixed, which is positive, but they show the swarm/consensus layer was largely scaffolding that reported success.
## Verdict inputs
- Do not adopt as infrastructure: very large attack surface (plugins "run with your account's permissions"), mocked internals, churn. Learn from: the idea of a cost/token tracker plugin, a TUI/console for swarm status, `synthetic` provenance flags on any result not produced by real work.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
