---
tags: [manager-kb, source]
url: https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/tips/claude-thariq-tips-17-mar-26.md (summary of Thariq Shihipar's X thread https://x.com/trq212/status/2033949937936085378)
type: practitioner-blog
author: Thariq Shihipar (Anthropic), summarised by shanraisshan
published: 2026-03-17
accessed: 2026-10-29
reliability: med-high (Anthropic staff lessons, but read SECOND-HAND via a community transcript; original X thread not opened)
---
# Thariq (Anthropic): "Lessons from Building Claude Code: How We Use Skills" (second-hand summary)
## Key claims
- "A common misconception is that skills are 'just markdown files', but the most interesting part is that they're folders that can include scripts, assets, data". Hundreds of skills in active use at Anthropic cluster into 9 types: library/API reference, product verification, data fetching/analysis, business-process automation, scaffolding, code quality/review, CI/CD, runbooks, infrastructure operations. "It can be worth having an engineer spend a week just making your verification skills excellent."
- Authoring tips: (1) don't state the obvious - push Claude out of its default behaviour; (2) "The highest-signal content in any skill is the Gotchas section", built from observed failure points and updated over time; (3) use the filesystem for progressive disclosure (`references/api.md`, scripts, examples); (4) avoid railroading - "Instead of prescriptive step-by-step instructions, give the goal and constraints"; (5) store setup in a `config.json` in the skill dir and ask via AskUserQuestion if missing; (6) "the description field is not a summary - it's a description of when to trigger this skill. Write it for the model."; (7) memory: append-only log or JSON/SQLite in the skill; skill-dir data may be deleted on upgrade so use `${CLAUDE_PLUGIN_DATA}`; (8) ship scripts/libraries so Claude composes instead of reconstructing boilerplate; (9) on-demand hooks inside skills (`/careful` blocks rm -rf, DROP TABLE, force-push, kubectl delete via a PreToolUse Bash matcher; `/freeze` blocks Edit/Write outside a directory) that live "for the duration of the session" once the skill is called.
- Business-process skills: "Saving previous results in log files can help the model stay consistent and reflect on previous executions of the workflow."
- Distribution: check into `.claude/skills` for small teams; plugin marketplace as it scales ("Every skill that is checked in also adds a little bit to the context of the model"); curation: sandbox folder first, PR into marketplace only after organic traction, "Curation before release is important to avoid redundant skills." Measure usage with a PreToolUse hook to find undertriggering skills (listed in the community tips index).
## Quotable
> "The description field is not a summary - it's a description of when to trigger this skill."
> "The highest-signal content in any skill is the Gotchas section."

## Used by
[[topic-claude-code-features]], [[topic-skill-library-retrieval]]
