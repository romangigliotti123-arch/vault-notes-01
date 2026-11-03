---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/plugin-evals.md (+ plugins/measure.md, skills.md#evaluate-and-iterate-on-a-skill)
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (feature added v2.1.269, Sept 2026; fetched raw .md)
accessed: 2026-10-29
reliability: high (official, raw markdown)
---
# `claude plugin eval`, `claude plugin details`, skill eval loop
## Key claims
- `claude plugin eval <path>` runs each case N=3 times (default) in fresh isolated non-interactive sessions with only the plugin loaded, scores it with graders, and by default repeats with NO plugin (the "no-plugin baseline") to report WITH, W/OUT and delta. Needs Claude Code 2.1.269+, git 2.31+ if present; every run and judge call is a real model call on your plan. `claude plugin eval init` interviews you and drafts cases + graders. Runs also work from a "skills-directory plugin" (a folder of skills), not only a published plugin.
- Case layout: `evals/<case>/prompt.md` (+ frontmatter: run limits, tools, env), `case.yaml`, `graders/*.md`. Six grader types, no custom code graders: `regex` (over `last_message`, `trace`, `files`, a file path, or `mock_calls`), `tool_used` (`tool`, `input_match` regex, `min`/`max`; `min:0,max:0` asserts never called), `tool_order` (before/after), `file_exists`, `llm` (rubric judged by a model, PASS needs 2 of 3 votes), `baseline` (judge compares with a reference transcript). Free graders: regex, tool_used, tool_order, file_exists.
- Stable-signal advice: grade long output with `regex` over the file, keep `llm` rubrics to short outputs with concrete PASS/FAIL conditions; one grader on the result and one on the steps taken (`tool_used`/`tool_order`); if a `tool_used: Skill` grader passes but delta is negative, suspect the judge; re-run with `--judge-model sonnet`. `tool_used: Skill` graders are excluded from scoring (reported as indicators) in two-arm runs because they can never pass without the plugin; use `arm: both` for "must NOT invoke" checks.
- CI usage: `--trust-plugin --json results.json --threshold 0.8 --model <id> --judge-model <id> --max-cost-usd 20`; exit codes 0 pass, 1 below threshold/error, 2 partial (cost ceiling or rejected credential), 130 interrupted, 143 terminated; delta never changes the exit code. `--ablation none` halves cost. `--disallow-tools` (2.1.299) keeps e.g. Agent out of eval runs. Mocked MCP servers supported.
- Subagent delegation can be measured the same way: sub-agents.md says "If the subagent ships in a plugin, you can measure how reliably Claude delegates to it across realistic prompts ... `claude plugin eval` runs each prompt with and without the plugin" (so a `tool_used: Agent` grader with `input_match` on the subagent name tests routing).
- `claude plugin details <name>` prints component inventory and projected always-on token cost per component (hooks cost nothing; MCP tool schemas not counted; use `/context` for those). Skill-level alternative loop: fresh session with vs without (`skillOverrides: off`), or the `skill-creator` plugin.
- Early-access gating: error "plugin eval is currently in early access" means update; "currently unavailable" = switched off server-side by Anthropic.
## Quotable
> "If a case scores 1.0 both with and without the plugin, the plugin isn't what made it pass."
> "There are no custom-code graders."

## Used by
[[topic-claude-code-features]]
