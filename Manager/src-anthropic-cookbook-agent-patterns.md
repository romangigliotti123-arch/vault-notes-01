---
tags: [manager-kb, source]
url: https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents
type: repo
author: Anthropic (claude-cookbooks)
published: undated (notebook uses claude-sonnet-5-5, so current)
accessed: 2026-10-29
reliability: med-high (official reference code, toy examples)
---
# claude-cookbooks patterns/agents
## Key claims
- Notebooks: basic_workflows (prompt chaining, routing, parallelization), orchestrator_workers, evaluator_optimizer, async_multi_agent_orchestration, latency_multi_agent. README is thin; guidance lives in notebooks.
- orchestrator_workers.ipynb (read via raw.githubusercontent.com): two phases. Orchestrator prompt returns `<analysis>` + `<tasks><task><type/><description/></task></tasks>` XML (2-3 approaches); each worker prompt receives the ORIGINAL task + its style/type + its guideline ("Task: {original_task} Style: {task_type} Guidelines: {task_description}") and returns `<response>`; empty worker outputs are validated/handled.
- When to use: tasks where subtasks can't be predicted; multiple perspectives. Don't use: simple single-output tasks, latency-critical, predictable subtasks (use plain parallelization).
- Design takeaway for managers: workers get full original context plus a specific brief; structured (XML) task list makes delegation parseable; validate worker output before synthesising.
## Quotable
> "Workers receive both the original task AND their specific instructions for better context"

## Used by
[[topic-anthropic-agent-guidance]]
