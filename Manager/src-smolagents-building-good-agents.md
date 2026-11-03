---
tags: [manager-kb, source]
url: https://github.com/huggingface/smolagents/blob/main/docs/source/en/tutorials/building_good_agents.md
type: official-doc
author: Hugging Face (smolagents team)
published: undated (repo doc, opened from raw.githubusercontent.com main)
accessed: 2026-10-29
reliability: high (maintainer docs; short on quantitative evidence)
---
# smolagents: building good agents (+ intro + multi-agent example)
## Key claims
- "The best agentic systems are the simplest: simplify the workflow as much as you can." Giving an LLM agency "introduces some risk of errors".
- "The main guideline is: Reduce the number of LLM calls as much as you can." Group tools (one unified `return_spot_information` instead of two API tools) "This will reduce costs, latency, and error risk!". "Whenever possible, logic should be based on deterministic functions rather than agentic decisions."
- Information flow: the LLM is "an intelligent robot, trapped into a room with the only communication with the outside world being notes passed under a door" - it knows only what you put in the prompt.
- The intro lists agency levels as stars; multi-agent = "one agentic workflow can start another agentic workflow" (the highest level, `if llm_trigger(): execute_agent()`).
- The multi-agent example is a plain manager/managed-agent hierarchy: managed agents need `name` and `description` to be callable by the manager; the sub-agent is a browsing ToolCallingAgent because "Web browsing is a single-timeline task".
- Library claim: whole agent logic fits in ~1,000 lines (README); CodeAgent writes actions as code, runs in sandboxes (Blaxel, E2B etc).
## Quotable
> Reduce the number of LLM calls as much as you can.

## Used by
[[topic-multi-agent-frameworks]], [[topic-orchestration-patterns]]
