---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/output-styles.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (current docs, matches Claude Code 2.1.312; fetched raw .md)
accessed: 2026-10-29
reliability: high (official, raw markdown)
---
# Output styles
## Key claims
- Output style = instructions added to the system prompt every request: "sets Claude's role, tone, and response format for every response in a session". Built-ins: Default, Proactive, Concise (2.1.237+; "first sentence ... states what happened or what the answer is", simple answers in 1-3 sentences, still full length for safety content), Explanatory, Learning. Proactive style tells Claude to check in the conversation before deleting data or changing shared/production systems (an instruction, not a permission prompt).
- Custom style = markdown file in `~/.claude/output-styles/` (or project/managed) with frontmatter `name`, `description`, `keep-coding-instructions` (default false = the built-in software-engineering instruction section is DROPPED), `force-for-plugin`. Value of `outputStyle` setting is case-sensitive. Files are read at startup (restart to pick up edits); switching mid-session costs a prompt-cache miss for the first message (see prompt-caching page).
- Subagents do NOT get the output style (own system prompt); forks do. `/output-style <built-in>` works from Remote Control (mobile/web can list/select only built-in styles; custom ones must be selected in the host session) and in `-p` (2.1.269+).
- The docs' own decision table: style = voice/length/role for every response; CLAUDE.md = project knowledge; skill = task-specific instructions; hook = must happen every time; subagent = separate context; `--append-system-prompt` = launch-time addition.
- env-vars.md: "Haiku 4.5, Sonnet 5, Opus 4.7, and earlier models in those families use the full prompt by default, and newer models use the shorter one" (`CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT`; 0 forces full). So on the 5.5 models the shorter prompt is the default and `keep-coding-instructions` has no effect there unless the variable is set to 0.
## Quotable
> "An output style gives Claude instructions to follow. It doesn't guarantee that something always happens or never happens."
> "An output style is a set of instructions that sets Claude's role, tone, and response format for every response in a session."

## Used by
[[topic-claude-code-features]]
