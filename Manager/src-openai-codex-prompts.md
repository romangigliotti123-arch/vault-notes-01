---
tags: [manager-kb, source]
url: https://github.com/openai/codex (codex-rs/core/gpt_5_2_prompt.md, templates/agents/orchestrator.md, templates/collab/experimental_prompt.md)
type: repo
author: OpenAI (open-source Codex CLI)
published: undated (files for GPT-5.2-era)
accessed: 2026-10-29
reliability: high (first-party open source prompts; written for GPT models, not Claude)
---
# OpenAI Codex prompts (raw files read)
## Key claims
- Persistence: "Persist until the task is fully handled end-to-end within the current turn whenever feasible: do not stop at analysis or partial fixes; carry changes through implementation, verification, and a clear explanation of outcomes unless the user explicitly pauses or redirects you."
- Validating: "start as specific as possible to the code you changed... then make your way to broader tests"; do not fix unrelated bugs, "You may mention them to the user in your final message though."
- Ambition vs precision: existing codebase -> "surgical precision"; new project -> ambitious.
- Final message: "should read naturally, like an update from a concise teammate"; "Brevity is very important as a default... no more than 10 lines" unless detail needed; do not paste file contents the user already has; group bullets 4-6 ordered by importance; headers only when they help.
- Orchestrator template ("User Updates Spec"): before starting give a quick plan "with goal, constraints, next steps"; call out discoveries; if the plan changes, "say so explicitly in the next update or the recap"; heads-down note with why/when it will report back.
- Multi-agent template: spawn only for large multi-scope tasks, reviews, debate from fresh context, or test/log-heavy runs to protect own context; when spawning several "you must tell them that they are not alone in the environment so they should not impact/revert the work of others"; tell a sub-agent "that it can't spawn another agent himself (to prevent infinite recursion)" and state whether sub-agents may spawn; close finished agents; scale `wait_agent` timeouts; "When you ask sub-agent to do the work for you, your only role becomes to coordinate them. Do not perform the actual work while they are working." and "wait for them before yielding".
- Git hygiene in prompt: unexpected changes you didn't make -> "STOP IMMEDIATELY and ask"; never destructive git commands unless asked.

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
