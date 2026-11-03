---
tags: [manager-kb, source]
url: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
type: eng-blog
author: Justin Young (Anthropic)
published: 2025-11-26
accessed: 2026-10-29
reliability: high (primary; scoped to full-stack web coding)
---
# Effective harnesses for long-running agents
## Key claims
- Each new session starts with no memory; compaction alone is not enough for multi-session projects. Failure modes: tries to do too much at once; declares the project done too early.
- Two-part solution: initializer agent (first session: init.sh, claude-progress.txt, initial git commit, feature list) + coding agent (every later session: one feature at a time, leave clean state, update progress file, commit). Same system prompt/tools, different initial user prompt.
- Feature list as JSON (200+ features, each with steps and a `passes` flag); agents may only flip `passes`; removing/editing tests is forbidden. JSON chosen because models alter it less than Markdown.
- Session-start routine: pwd, read git log + progress file, read feature list, run init.sh + a basic e2e check before new work.
- Agents marked features done after unit tests/curl only; browser automation (Puppeteer MCP) testing "dramatically improved performance".
- Open question: one general agent vs specialised testing/QA/cleanup agents.
## Quotable
> "each new session begins with no memory of what came before."
> "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-llm-judge-and-adversarial-verification]], [[topic-long-running-always-on-agents]], [[topic-multi-agent-failure-modes]], [[topic-report-formats-and-verification]]
