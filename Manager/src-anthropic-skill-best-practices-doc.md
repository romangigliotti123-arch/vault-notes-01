---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high: official doc
---
# Skill authoring best practices
## Key claims
- name: max 64 chars, lowercase letters, digits, hyphens; description: max 1,024 chars, third person, say WHAT and WHEN. "Claude uses it to choose the right Skill from potentially 100+ available Skills."
- Prefer gerund names (processing-pdfs); avoid vague names (helper, utils, tools) and inconsistent patterns inside a collection.
- SKILL.md body under 500 lines; references ONE level deep; table of contents for reference files over 100 lines.
- Evaluation-driven: identify gaps, build at least 3 scenarios, baseline without the skill, write minimal instructions, iterate; test with Haiku, Sonnet and Opus.
- "Claude A / Claude B" loop: one instance writes the skill, a fresh instance uses it on real tasks; observe navigation (ignored files, repeated reads).
- No time-sensitive info; legacy under an "old patterns" section; consistent terminology.
- "There is not currently a built-in way to run these evaluations" (build your own).
## Quotable
> "Create evaluations BEFORE writing extensive documentation."

## Used by
[[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
