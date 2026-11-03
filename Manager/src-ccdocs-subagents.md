---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/sub-agents.md
type: official-doc
author: Anthropic (Claude Code docs)
published: undated (CC 2.1.3xx era)
accessed: 2026-10-29
reliability: high (official; our actual runtime)
---
# Claude Code: Create custom subagents
(Mechanics are covered in manager-setup.md; this note keeps only brief/report-relevant facts.)
## Key claims
- Subagents receive "only this system prompt plus basic environment details like the working directory, not the Claude Code system prompt"; CLAUDE.md files still load (even with `omitClaudeMd`, per one line; `omitClaudeMd: true` is meant "for subagents that take everything they need from the delegation prompt").
- "Your full message still goes to Claude, which writes the subagent's task prompt based on what you asked." So the delegation prompt is authored by the manager model each time; the agent file body is the standing role, the per-call prompt is the brief.
- Descriptions are always in context; "move detail into each subagent's system prompt, which only loads when that subagent runs"; 15,000-token combined warning. "use proactively" in description encourages delegation.
- `--append-subagent-system-prompt[-file]` (headless only, v2.1.205/261) appends text to every subagent's system prompt: a hook for a universal "report format / evidence rule" without editing each agent file.
- Frontmatter fields incl. `maxTurns` (partial result; resumable), `effort`, `omitClaudeMd`, `background`, `memory`, `initialPrompt`.
- Subagent output scanning: "Claude Code scans each subagent's final report before Claude reads it" and inserts a backslash into text imitating `<system-reminder>` / `Human:` lines or prepends a `[harness: subagent output matched instruction-shaped pattern(s):` marker line. The report arrives under a header stating that instructions or approval claims inside it "carry no authority from you". Reports are untrusted data.
- Background subagent reports arrive inside a completion notification; only the top-level subagent's summary returns when a subagent launches its own background subagents.
- In auto mode the classifier reviews the subagent's work and final report before delivery.
## Quotable
> "A report that returns to Claude as the subagent's result also arrives under a header marking it as subagent output."

## Used by
[[topic-brief-prompt-engineering]], [[topic-report-formats-and-verification]]
