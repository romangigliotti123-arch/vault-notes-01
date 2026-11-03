---
tags: [manager-kb, source]
url: https://www.humanlayer.dev/blog/writing-a-good-claude-md ; https://www.hlyr.dev/blog/stop-claude-from-ignoring-your-claude-md
type: practitioner-blog
author: Kyle (HumanLayer) 2025-11-25; Dex Horthy (HumanLayer) 2026-03-17
published: 2025-11-25 and 2026-03-17
accessed: 2026-10-29
reliability: med (practitioner, partly speculative about harness internals; wrapper claim may be stale)
---
# HumanLayer: Writing a good CLAUDE.md; Getting Claude to actually read it
## Key claims
- "Claude often ignores CLAUDE.md": the authors observed (via a logging proxy on `ANTHROPIC_BASE_URL`) that Claude Code injects CLAUDE.md in the user message wrapped in a system-reminder saying the context "may or may not be relevant to your tasks. You should not respond to this context unless it is highly relevant". Hence "the more information you have in the file that's not universally applicable ..., the more likely it is that Claude will ignore your instructions". CAVEAT for us: the CLAUDE.md wrapper text our own session receives (the harness preamble) says the opposite ("Be sure to adhere to these instructions ... OVERRIDE any default behavior"), so this finding is version-dependent (Nov 2025) and not safe to assume today; the principle (irrelevant content dilutes adherence) still holds per official docs.
- "Frontier thinking LLMs can follow ~150-200 instructions with reasonable consistency"; smaller models decay exponentially, larger ones linearly (attributed research, not measured by the authors); Claude Code's own system prompt has ~50 instructions (their count). Therefore "less (instructions) is more"; root CLAUDE.md under 60 lines at HumanLayer; general consensus "< 300 lines".
- WHAT/WHY/HOW structure (map of the codebase, purpose, how to verify). Progressive disclosure: put task-specific docs in separate files (`agent_docs/*.md`) and list them with one-line descriptions in CLAUDE.md; "Prefer pointers to copies" (file:line refs, not snippets).
- "Claude is (not) an expensive linter": never put style rules in CLAUDE.md; use formatters + a Stop hook that feeds errors back. "Don't use /init or auto-generate your CLAUDE.md" (affects every phase, so hand-craft).
- Dex (2026-03-17): wrap sections that only matter sometimes in `<important if="you are writing or modifying tests">...</important>` blocks; "Don't wrap everything"; conditions must be specific; no rigorous explanation, "noticeably better adherence" anecdotally. Provides a skill `humanlayer/skills improve-claude-md`.
## Quotable
> "Never send an LLM to do a linter's job."
> "Prefer pointers to copies."
> "Don't wrap everything. Project identity, directory structure, and tech stack are relevant to basically every task."

## Used by
[[topic-claude-code-features]]
