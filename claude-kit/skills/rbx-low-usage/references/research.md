# rbx-low-usage: research (2026-11-01)

Sources are the official Claude Code docs (read 2026-11-01 against Claude Code 2.1.314) plus community write-ups found by web search. Community numbers are the authors' own estimates, not measured here. YouTube was not reachable as text; GitHub issues were read only as search snippets.

## A. Making a mode last for the whole session, including after auto-compaction

Design: a marker file is the single switch; a `UserPromptSubmit` hook every turn is load-bearing, `SessionStart` (startup/resume/compact) restores the rules after compaction; hooks are inert when the marker is absent; the injected text is about 200 tokens per message at the end of the conversation (cache-safe). [cold:rbx-low-usage/research.md] read only to see the evidence behind the hook design or the usage-saving levers.

## B. What actually lowers usage

Levers: keep context small (`/clear`, `/compact`), Sonnet by default and no mid-session model switch, lower effort, at most one subagent, filtered tool output, few images, stable cache. [cold:rbx-low-usage/research.md] read only to see the evidence behind the hook design or the usage-saving levers.

## Sources

Official Claude Code docs (hooks, skills, output-styles, costs, prompt-caching, read 2026-11-01) plus community write-ups. [cold:rbx-low-usage/research.md] read only to see the evidence behind the hook design or the usage-saving levers.