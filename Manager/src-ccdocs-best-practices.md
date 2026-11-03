---
tags: [manager-kb, source]
url: https://code.claude.com/docs/en/best-practices
type: official-doc
author: Anthropic (Claude Code docs; successor of the 2025-04-18 engineering post "Claude Code: Best practices for agentic coding", which now 308-redirects here)
published: undated (current docs, mentions Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / Fable 5.1)
accessed: 2026-10-29
reliability: high (official, current-model era)
---
# Best practices for Claude Code (Claude 5-era rewrite)
## Key claims
- Deterministic vs non-deterministic instructions: prompt/CLAUDE.md/skills are advisory ("Claude is allowed to decide a guideline doesn't apply"); hooks, deny rules, sandbox, managed settings, Stop hooks, CI, branch protection are enforced by the harness. "If something has to happen every time, make it a hook, a deny rule, or a managed setting." If you keep adding emphasis to a CLAUDE.md line and Claude still misses it, it belongs in a hook. Keep the enforced set small (~40 hooks = mostly preferences).
- Tell Claude only what it cannot see: test "Could it find this by reading the code? Would it actually go and look? If both yes, leave it out." Specific prompts (name the file, symptom, definition of "fixed"). "be ambitious" still helps for scope. `think hard` etc. are ordinary text; effort level is the real control.
- CLAUDE.md short (<200 lines per memory guide); only commands to verify work, misleading places, off-repo decisions, things corrected twice. Use `/doctor`, `/doctor prompt-audit` (flags instructions written for older models, stale paths, contradictions). Path-scoped `.claude/rules/`. Team procedures in skills (lighter than CLAUDE.md); side-effect skills get `disable-model-invocation: true`.
- Give Claude a check to run (tests, build exit code, linter, diff vs fixture, screenshot). Levels: in prompt; `/goal` (separate model checks condition after each turn); `Stop` hook (exit 2 sends it back; capped at 8 consecutive blocks); fresh-subagent `/code-review`. Always ask for evidence (command + output), not "all tests pass". Reviewer prompt must say "skip style" because "A reviewer that's asked to find problems will always find something."
- Auto mode: classifier checks actions; deny rules and PreToolUse hooks run before it; 3 consecutive / 20 total blocks pauses it; "your 'never' rules belong in deny rules or hooks". `bypassPermissions` only makes sense in a disposable container.
- Effort: Opus 5.5 / Sonnet 5.5 / Haiku 5.5 default `medium`; `high`/`xhigh` for hard-to-verify edge cases, `low` for quick back-and-forth, `max` only for hard unattended problems (tends to overthink otherwise). Haiku for simple subagents.
- Subagent economics: they pay off for parallel work, keeping noisy output out of main context, and an independent reviewer; they cost tokens (own requests, same usage), a fresh subagent re-gathers context so can be slower; "by default it's the same model (or a smaller one) on the same task. You get parallelism or a fresh pair of eyes out of it, but not a smarter answer." Ask for short summaries back; restrict tools (`tools: Read, Grep, Glob` = enforced read-only reviewer). Check `/usage` per subagent type.
- Context cost: every request resends the whole conversation (cheap while cache warm); `/clear` between unrelated tasks; `/compact <focus>`; prompt cache ~1 hour on subscription, 5 minutes on API/usage credits; subagents get 5 min unless changed; a >200K idle session is compacted before cache expiry.
- Steer: watch the first minute, Esc early, after two failed corrections `/clear` and write a better prompt rather than a third correction.
- Unattended-run checklist (5 questions): does it know what done looks like; can it check its own work; what may it touch; what stops it (`--max-turns`, `--max-budget-usd`); where does the result go and who signs off. "Try it on three files first".
- `claude -p` flags for scripts: `--bare` (skips hooks/skills/plugins/MCP/CLAUDE.md; needs API key auth), `--allowedTools`, `--permission-mode dontAsk`, `--output-format json`, `--max-turns`.
- "What you can stop doing" table (old advice now unnecessary): aggressive context-window management (1M windows + auto compaction; `/clear` still worth it), IMPORTANT/ALL CAPS emphasis (causes over-application), subagents to protect context window (rarely the problem now), delegating to a subagent for a *better* answer, "think hard" phrases, "keep going / don't be lazy" lines (more likely to cause over-work than fix a stall), describing architecture in CLAUDE.md.
## Quotable
> "Claude said it was done and it wasn't quite, usually because it had no way to check its own work."
> "Handing the same task to a subagent doesn't make the answer any better. A fresh reviewer does help, because it hasn't seen your reasoning"
> "Before a run goes unattended, make sure it knows what done looks like, can check its own work, and can only touch what it should."

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-claude-code-features]], [[topic-context-engineering]], [[topic-context-window-management]], [[topic-llm-judge-and-adversarial-verification]], [[topic-model-effort-routing-cost]], [[topic-multi-agent-failure-modes]], [[topic-report-formats-and-verification]]
