---
tags: [manager-kb, source]
url: https://dev.to/thebasedcapital/why-your-overnight-ai-agent-fails-and-how-episodic-execution-fixes-it-2g50
type: practitioner-blog
author: thebasedcapital
published: undated (page: "Feb 23", year not shown)
accessed: 2026-10-29
reliability: low-med (single practitioner design; no external validation)
---
# Why your overnight agent fails (episodic execution / Nightcrawler)
## Key claims
- Six failure modes: context cliff (30-60 min), hallucinated handoff (reports done, git shows not), budget inferno, infinite retry loop, silent crash (no record), drift spiral.
- Design: bounded episodes, each a fresh `claude -p`; reads mission + previous handoff, verifies handoff against git, does top incomplete task, writes structured handoff. Orchestrator checks 8 termination conditions between episodes (budget cap, error threshold, diminishing returns: <0.5 tasks/episode for 3 episodes). `tasks.json`: agent may flip incomplete->complete, not delete/edit tasks. launchd restarts with 30 s throttle and 12 h hard timeout. Defaults: 24 episodes, $50 total, $5/episode, 10 errors, 3,600 s episode timeout.
- "Sessions will end. Build around that." "The default behavior on any unexpected state is to stop, not to continue."

## Used by
[[topic-long-running-always-on-agents]]
