---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/building-effective-agents
type: eng-blog
author: Erik S., Barry Zhang (Anthropic Engineering)
published: 2024-12-19
accessed: 2026-10-29
reliability: high (primary Anthropic; page notes tooling has changed since)
---
# Building effective agents
## Key claims
- Workflows = "LLMs and tools are orchestrated through predefined code paths"; agents = "LLMs dynamically direct their own processes and tool usage". "Agentic systems" is the umbrella.
- Advice: find the simplest solution, only add complexity when needed; a single LLM call + retrieval + examples is often enough. Agents trade latency/cost for performance.
- Five workflow patterns: (1) prompt chaining (sequential steps, programmatic gates between), (2) routing (classify input, send to specialised prompt/model; easy queries to a small model, hard ones to a big one), (3) parallelization (sectioning = independent subtasks; voting = same task many times), (4) orchestrator-workers (central LLM decomposes at runtime, delegates, synthesises; subtasks not predefined), (5) evaluator-optimizer (generate + critique loop; needs clear criteria).
- Agents: start from a human command/discussion, plan and act, get "ground truth" from the environment at each step, may pause at checkpoints, use stopping conditions (max iterations). Use for open-ended problems where steps cannot be hardcoded and the model is trusted; autonomy = higher cost + compounding errors; test in sandboxes with guardrails.
- Frameworks can hide prompts/responses; start with direct API calls; understand what a framework does.
- ACI (agent-computer interface): invest as much as in HCI. Formats close to natural text; avoid line-counting/escaping overhead; clear param names, examples, edge cases, boundaries vs other tools; test many inputs; poka-yoke (SWE-bench: requiring absolute paths fixed errors after cwd changes). The team spent more time optimizing tools than the overall prompt.
- Three principles: simplicity, transparency (show planning steps), carefully crafted ACI.
## Quotable
> "They are typically just LLMs using tools based on environmental feedback in a loop."
> "finding the simplest solution possible, and only increasing complexity when needed"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-llm-judge-and-adversarial-verification]], [[topic-multi-agent-failure-modes]], [[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]], [[topic-report-formats-and-verification]]
