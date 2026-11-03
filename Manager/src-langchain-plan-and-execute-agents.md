---
tags: [manager-kb, source]
url: https://www.langchain.com/blog/planning-agents
type: eng-blog
author: LangChain team
published: 2024-02-13
accessed: 2026-10-29
reliability: med (vendor explainer; claims are qualitative, no benchmarks in the post)
---
# Plan-and-Execute Agents (plan-and-execute, ReWOO, LLMCompiler)
## Key claims
- Three promised wins over ReAct: speed (the big model is not consulted after each action), cost (sub-tasks can go to smaller/domain models; the big model only plans, re-plans and writes the final answer), quality (forcing the planner to "think through" all steps).
- Plan-and-execute: planner makes a multi-step plan, executors run each step with tools, then a re-plan prompt decides finish vs follow-up plan. Still serial and still one LLM call per task (no variable passing).
- ReWOO: planner writes steps with variables (`E1`, `#E2`), a worker fills variables in order without calling the planner again, a solver integrates. Each task sees only its inputs. Still sequential.
- LLMCompiler: planner streams a DAG of tasks with dependencies; a task-fetching unit schedules parallel execution; a joiner decides to finish or re-plan. Faster than ReWOO / parallel tool calls.
- ReAct drawbacks named: an LLM call per tool invocation, and only one sub-problem planned at a time.

## Used by
[[topic-orchestration-patterns]]
