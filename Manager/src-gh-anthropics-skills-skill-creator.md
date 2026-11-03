---
tags: [manager-kb, source]
url: https://github.com/anthropics/skills (README.md, skills/skill-creator/SKILL.md, skills/discernment-nudge/SKILL.md)
type: repo
author: Anthropic
published: undated (main branch read 2026-10-29)
accessed: 2026-10-29
reliability: high (first-party skill used to author skills)
---
# anthropics/skills and the skill-creator skill (Anthropic's own skill-authoring playbook)
## Key claims
- Repo layout: `skills/` (19 skills: docx, pdf, pptx, xlsx, claude-api, skill-creator, mcp-builder, webapp-testing, doc-coauthoring, discernment-nudge, ...), `spec/` (Agent Skills spec), `template/`. Installable as a Claude Code marketplace: `/plugin marketplace add anthropics/skills`. Disclaimer: skills are "for demonstration and educational purposes".
- Frontmatter minimum = `name` + `description`; "description: ... This is the primary triggering mechanism - include both what the skill does AND specific contexts for when to use it. All 'when to use' info goes here, not in the body."
- Anti-undertriggering advice: "currently Claude has a tendency to 'undertrigger' skills ... make the skill descriptions a little bit 'pushy'", e.g. append "Make sure to use this skill whenever the user mentions dashboards, ... even if they don't explicitly ask". Also: "Claude only consults skills for tasks it can't easily handle on its own - simple, one-step queries ... may not trigger a skill even if the description matches perfectly" -> eval prompts must be substantive.
- Progressive disclosure, 3 levels: metadata (~100 words, always), SKILL.md body (<500 lines ideal), bundled resources (scripts executed without loading; references with a TOC if >300 lines; organise by variant: `references/aws.md`, `gcp.md`...).
- Writing style: imperative form; "explain to the model why things are important in lieu of heavy-handed musty MUSTs"; use theory of mind; keep general, not narrow to examples; draft then re-read "with fresh eyes". "Principle of Lack of Surprise": a skill's contents must not surprise the user given its description (security).
- Eval loop (all via subagents): 2-3 realistic test prompts saved to `evals/evals.json`; spawn with-skill AND baseline (no skill, or snapshot of the old skill) runs in the SAME turn; draft assertions while runs go; capture `total_tokens`/`duration_ms` from task notifications into `timing.json` immediately ("the only opportunity to capture this data"); grader subagent writes `grading.json` with fields `text`, `passed`, `evidence`; `aggregate_benchmark` makes `benchmark.json` (pass_rate, time, tokens, mean +- stddev, delta); blind A/B comparison between versions; a separate description-optimizer script that needs `claude -p`.
- Skip assertions for subjective skills (writing style, design) - judge qualitatively.
- `discernment-nudge` skill shows description-as-trigger-spec at its most explicit: the description lists when to invoke AND when to skip (trivial how-to, lookups, formatting, code the user will run, creative writing, already asked to double-check), plus a "at most once per conversation" rule.
## Quotable
> "All 'when to use' info goes here, not in the body."
> "Try to explain to the model why things are important in lieu of heavy-handed musty MUSTs."

## Used by
[[topic-claude-code-features]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
