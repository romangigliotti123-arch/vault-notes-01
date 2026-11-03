# low-usage-mode-rbxdev-vault: research (2026-11-01)

Sources are the official Claude Code docs (read 2026-11-01 against Claude Code 2.1.314) plus community write-ups found by web search. Community numbers are the authors' own estimates, not measured here. YouTube was not reachable as text; GitHub issues were read only as search snippets.

## A. Making a mode last for the whole session, including after auto-compaction

| Mechanism | What it does | Verdict |
|---|---|---|
| Skill alone | Rendered SKILL.md "enters the conversation as a single message and stays there"; Claude Code does not re-read it. After auto-compaction only the most recent invocation of each skill is re-attached, first 5,000 tokens each, 25,000 shared; older skills can be dropped. A new session starts without it. (code.claude.com/docs/en/skills) | Fades in long sessions; gone in the next session. Use only to flip the switch. |
| CLAUDE.md | Loaded at session start; edits mid-session do not apply until `/clear`, `/compact` or restart. (docs/en/prompt-caching, "Editing CLAUDE.md mid-session") | Always-on cost, cannot be toggled per command without editing a user file. Not used. |
| Output style | Style instructions go with every request, switch mid-session with `/output-style`, saved by default to the project's `.claude/settings.local.json`. Built-in `Concise` (v2.1.237+) shortens replies. The docs say a style "doesn't guarantee that something always happens" and send "something that has to happen every time" to a hook. (docs/en/output-styles) | Good complement for brevity (`/output-style concise`), wrong tool for a per-message prefix and a global toggle. |
| UserPromptSubmit hook | Plain stdout or `hookSpecificOutput.additionalContext` is added as context before Claude sees each prompt; fires every turn, so compaction cannot remove it. The text is saved in the transcript; matcher is ignored; default timeout 30 s. (docs/en/hooks) | Primary mechanism. |
| SessionStart hook, matchers `startup`, `resume`, `clear`, `compact`, `fork` | Runs again on resume and after compaction; `additionalContext` is wrapped in a system reminder at the start of the conversation. (docs/en/hooks) | Second layer: restores the rules right after a compaction and at session start, before any prompt. |
| Skill frontmatter `hooks:` | Registered when the skill is invoked and runs for the rest of that session. (docs/en/skills) | Zero-settings option, but not present in a new or resumed process. Not used; noted as a fallback idea. |
| Plugin bundling hooks | Plugin hooks and skills are appended without invalidating the prompt cache. (docs/en/prompt-caching) | Possible later packaging; the kit installs files, so a settings.json merge was used. |

Conflicting community reports: older GitHub issues (claudeissues.com 32026, 54536) say nothing fires after compaction and describe PreCompact-marker-plus-UserPromptSubmit workarounds. Tested here on 2.1.314: the transcript shows `compact_boundary`, then a `SessionStart` attachment, then the `UserPromptSubmit` attachment, and the reply after `/compact` still began with the prefix. Also: dev.to "injecting rules every turn instead of hoping AI remembers" reports the same per-turn pattern working.

Design consequence: marker file as the single switch, `UserPromptSubmit` every turn (load-bearing), `SessionStart` for startup/resume/compact (belt and braces), hooks inert when the marker is absent.

Cost of the mechanism: the injected text is about 840 characters (roughly 200 tokens) appended per message at the end of the conversation, so the cached prefix is untouched (hooks and skills are cache-safe per docs/en/prompt-caching) and it is billed as cache reads afterwards. Break-even: it pays for itself if it saves more than about 200 tokens of output or one avoided tool dump per message.

## B. What actually lowers usage

1. Context size is the multiplier: every request resends the whole conversation (cached rate); a one-line question in an all-day session still draws for the whole history. `/clear` between unrelated tasks (free), `/compact` at natural breaks (a compaction is itself a large request), custom compaction instructions. (docs/en/costs)
2. Model: Sonnet for most work, Opus only for hard reasoning, `model: haiku` for simple subagents. Each model has its own prompt cache, so switching models mid-session re-reads everything uncached: choose at the start. (docs/en/costs, docs/en/prompt-caching)
3. Effort and thinking: thinking is billed as output; on Opus 5.5 / Sonnet 5.5 / Haiku 5.5 it cannot be turned off, so lower `/effort` (the cache survives an effort change on these models). (docs/en/costs)
4. Subagents, workflows and agent teams each send their own requests on top of the main chat; teams use about 7x tokens in plan mode. Cap at one at a time, small model, small task. (docs/en/costs)
5. Tool output is context: filter before Claude reads (hooks/CLI `grep`, `head`), delegate verbose runs, prefer CLI tools (`gh`, `aws`) over MCP servers, disable unused MCP servers; MCP definitions are deferred by default now. Removing a tool mid-session can invalidate the cache when tool search is off. (docs/en/costs, docs/en/prompt-caching)
6. Images: many screenshots hit request limits and Claude Code drops batches of old ones, forcing a recompute. Avoid unless essential. (docs/en/prompt-caching)
7. Cache hygiene: first message after a break longer than the cache lifetime (5 min or 1 h) is a full uncached read; model, fast-mode and MCP-server changes also miss. (docs/en/prompt-caching)
8. Habits: specific prompts, plan mode before big edits, stop early with Esc / `/rewind`, give verification targets, keep CLAUDE.md under about 200 lines and move rare workflows into skills. (docs/en/costs)
9. Background drains: session recap, idle compaction (`idleCompaction: false`, v2.1.290+), prompt suggestions, scheduled `/loop` tasks, goal check-ins. (docs/en/costs)
10. Read your own numbers: `/usage` (plan breakdown with attribution to skills, subagents, plugins, MCP servers, plus recommendations and an `f` fix shortcut), `/context`, the `Prompt cache (main)` line, `/insights`. (docs/en/costs)
11. Community (r/ClaudeAI usage-limits megathread, dev.to and KDnuggets token-saving posts, found via search): default to Sonnet, Haiku for exploration subagents (one post sets `CLAUDE_CODE_SUBAGENT_MODEL=haiku`, not verified in the official docs), `/clear` and `/compact` habits, disconnect idle MCP servers. Their savings figures (about 60% for Sonnet vs Opus, about 80% for Haiku subagents) are unverified estimates.

## Sources
- https://code.claude.com/docs/en/hooks , /skills , /output-styles , /costs , /prompt-caching (all read 2026-11-01)
- https://dev.to/kanta13jp1/claude-code-hooks-injecting-rules-every-turn-instead-of-hoping-ai-remembers-4bfm
- https://claudeissues.com/issue/32026-feature-request-postcompact-hook-event and /54536-... (search snippets)
- https://dev.to/vishnub33527201/tips-for-token-optimisation-in-claude-code-1kn5 , https://kdnuggets.com/7-practical-ways-to-reduce-claude-code-token-usage , r/ClaudeAI usage-limits megathread (search snippets)
