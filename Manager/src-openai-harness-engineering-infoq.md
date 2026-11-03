---
tags: [manager-kb, source]
url: https://www.infoq.com/news/2026/02/openai-harness-engineering-codex
type: practitioner-blog
author: InfoQ news report on OpenAI's post (original https://openai.com/index/harness-engineering/ returned HTTP 403 to us; dated ~2026-02-11 by secondary sources)
published: 2026-02-21
accessed: 2026-11-01
reliability: med (secondary report of a primary; original unread)
---
# OpenAI "harness engineering" (as reported by InfoQ)
## Key claims
- Five-month internal experiment: a beta product of about 1 million lines with no manually written source; a small team of engineers steered Codex agents.
- Humans move from writing code to designing environments, specifying intent and giving structured feedback.
- Agents open PRs, run CI, reproduce bugs from logs/metrics/spans in isolated environments, propose and validate fixes, iterate until task criteria are met.
- A structured docs directory (maps, execution plans, design specs) is the single source of truth for agents; linters and CI mechanically check the cross-linked docs.
- Architecture is enforced mechanically: ordered layers (Types, Config, Repo, Service, Runtime, UI) with structural tests; agents must stay within them.
## Quotable
> (no verbatim OpenAI quote obtained; InfoQ paraphrase) humans design environments, specify intent and give structured feedback while agents write the code.
## Used by
[[topic-orchestration-patterns]], [[topic-managing-ai-agents-for-roblox-game-dev]]
