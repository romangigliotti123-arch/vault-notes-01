---
tags: [manager-kb, source]
url: https://cognition.com/blog/devin-sonnet-4-5-lessons-and-challenges
type: eng-blog
author: Cognition
published: 2025-09-29
accessed: 2026-10-29
reliability: med-high (production team observation, Sonnet 4.5 era; 5.x behaviour may differ)
---
# Rebuilding Devin for Claude Sonnet 4.5: Lessons and Challenges
## Key claims
- "context anxiety": "we found the model taking shortcuts or leaving tasks incomplete when it believed it was near the end of its window"; fix: "reminders both at the beginning and the end of the prompt to keep it from prematurely wrapping up".
- Workaround: "enabling the 1M token beta but cap usage at 200k... gave us a model that thinks it has plenty of runway and behaves normally". The model "consistently underestimates how many tokens it has left" and writes more summary tokens the shorter its window is.
- "The model treats the file system as its memory without prompting" (CHANGELOG.md, SUMMARY.md; not CLAUDE.md/AGENTS.md) but its own notes were often not thorough, paraphrased tasks and dropped details: "the model didn't know what it didn't know"; some agents spent more tokens on summaries than on the task.
- Reading for us: a tight window on a model that sees its remaining budget (Claude Code's `autoCompactWindow` is the compaction trigger, not the visible window size) is a documented risk; nothing here shows the same on Opus/Sonnet 5.5 (unverified).
## Quotable
> "enabling the 1M token beta but cap usage at 200k"

## Used by
[[topic-context-window-management]]
