---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/skills.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312; fetched raw .md, 118 KB)
accessed: 2026-10-29
reliability: high (official, raw markdown)
---
# Extend Claude with skills (Claude Code docs)
## Key claims
- All frontmatter optional, `description` recommended; unknown fields ignored silently; frontmatter only read if `---` is the file's first line; YAML parse failure -> skill still loads with NO metadata (so it can never auto-trigger). `claude plugin validate ~/.claude/skills` finds these (2.1.233+).
- Description rules: "Put the key use case first: the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing". Listing always contains every skill NAME; descriptions dropped (least-used first) beyond a budget of 1% of context window; raise via `skillListingBudgetFraction` or `SLASH_COMMAND_TOOL_CHAR_BUDGET`; shrink via `skillOverrides: "name-only"`. Angle brackets in descriptions render as `&lt;`.
- Keep SKILL.md under 500 lines; use supporting files (reference.md, examples.md, scripts/) referenced from SKILL.md so they load only when needed (progressive disclosure); scripts are executed, not loaded.
- Skill body lifecycle: rendered SKILL.md enters conversation as ONE message and stays; Claude Code does not re-read the file; after compaction the most recent invocation of each skill is re-attached, first 5,000 tokens each, 25,000 combined, newest first -> put the most important instructions at the top; write standing instructions ("Run the tests after every edit") not one-time steps.
- "Claude skipped a rule that must hold every time: move the rule into a hook" (or the skill's own `hooks` frontmatter, active from invocation to session end, `once:true` supported for skills).
- Invocation control: `disable-model-invocation: true` (manual only; also blocks subagent preload and scheduled-task use), `user-invocable: false`, `allowed-tools` (grant clears next user message), `disallowed-tools`, `model`/`effort` override for the turn, `paths` globs for auto-activation, `context: fork` + `agent:` runs the skill in a subagent (background default true; `background: false` to wait), `shell: powershell` for `` !`cmd` `` injection.
- Dynamic context injection: `` !`command` `` / ```! blocks run before the skill is sent; use for live state (e.g. PR diff).
- Skill evals: baseline comparison in a fresh session with and without the skill (`skillOverrides: "off"` for the second run); plugin skills use `claude plugin eval`; the `skill-creator` plugin (anthropics/claude-plugins-official) adds `evals/evals.json`, per-case subagent runs, `grading.json`, `benchmark.json`, blind A/B version comparison and description tuning (should-trigger / should-not-trigger prompts).
- `/skill-doctor` (2.1.252+) = cost vs usage per skill, flags never-invoked skills; NOT available over Remote Control ("Skill usage reports are not available on this connection") - run in the host terminal. `/doctor` reports listing cost and top contributors.
- Troubleshooting triggers: description must contain keywords users naturally say; "Skill triggers too often": make description more specific or `disable-model-invocation`.
- Skills synced from claude.ai load into Claude Code (`CLAUDE_CODE_SYNC_SKILLS`), see manager-setup.md for the plugin side.
## Quotable
> "Claude skipped a rule that must hold every time: move the rule into a hook."
> "Re-attached skills share a combined budget of 25,000 tokens."

## Used by
[[topic-claude-code-features]], [[topic-knowledge-management-rag]], [[topic-skill-library-retrieval]]
