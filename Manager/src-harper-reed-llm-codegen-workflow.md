---
tags: [manager-kb, source]
url: https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
type: practitioner-blog
author: Harper Reed
published: 2025-02-16
accessed: 2026-10-29
reliability: med (practitioner workflow, early-2025 model era; fetched in full)
---
# Harper Reed: "My LLM codegen workflow atm"
## Key claims
- Three discrete loops: (1) idea honing in a conversational model with the prompt "Ask me one question at a time so we can develop a thorough, step-by-step spec" -> `spec.md`; (2) planning with a reasoning model: blueprint -> small iterative chunks -> "go another round to break it into small steps" -> a series of codegen prompts, each ending "with wiring things together. There should be no hanging or orphaned code" -> `prompt_plan.md`; (3) a `todo.md` checklist the codegen tool ticks off, which "is good for keeping state across sessions".
- Execute each prompt step by step (test-driven variant of the planning prompt exists); when stuck, dump the repo with repomix to a model to debug. Whole planning phase "maybe 15 minutes".
- Brief hygiene implied: right-size steps ("small enough to be implemented safely with strong testing, but big enough to move the project forward"); plan files live in the repo as state (spec.md, prompt_plan.md, todo.md) so any later session/agent can continue.
- Disclaimer by author: "This is working well NOW, it will probably not work in 2 weeks, or it will work twice as well."
## Quotable
> "Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea."

## Used by
[[topic-claude-code-features]]
