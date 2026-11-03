---
tags: [manager-kb, source]
url: https://github.com/openai/symphony
type: repo
author: OpenAI
published: 2026-04 (blog post on open-source Codex orchestration; repo page undated)
accessed: 2026-11-01
reliability: med (primary README via summariser; OpenAI blog 403; the "+500% landed PRs in 3 weeks" claim is from a search snippet only, unverified)
---
# OpenAI Symphony: a task board as control plane for coding agents
## Key claims
- Turns project work into "isolated, autonomous implementation runs": monitors a Linear board, spawns an agent per task; agents supply proof of work (CI status, PR review feedback, complexity analysis, walkthrough videos) and land a PR only after acceptance.
- Spec-driven: a SPEC.md lets teams implement it in any language; an experimental Elixir reference implementation exists.
- Works best in codebases that already adopted harness engineering; self-described "low-key engineering preview for testing in trusted environments".
- 27.9k GitHub stars at fetch time (popularity, not quality evidence).
## Used by
[[topic-orchestration-patterns]], [[topic-long-running-always-on-agents]]
