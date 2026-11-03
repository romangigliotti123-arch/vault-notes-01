---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
type: official-doc
author: Anthropic (Claude Developer Platform docs)
published: undated (current; accounts created on/after 2026-08-31 enforce thinking-block binding)
accessed: 2026-10-29
reliability: high (official)
---
# Prompting Claude Fable 5.1 (autonomous-run guidance, compaction summary prompt)
## Key claims
- "Finish the whole task": on long async workloads the model sometimes describes next steps ("Next, I'll...") or asks permission for work already requested ("Shall I apply this?"). Two system prompt blocks: (1) "You are operating autonomously. The user is not watching in real time and cannot answer questions mid-task, so asking 'Want me to...?' or 'Shall I...?' will block the work. For reversible actions that follow from the original request, proceed without asking. Stop only for destructive actions or genuine scope changes the user must decide." + exception for questions/problem descriptions (report findings, don't fix) + "Before ending your turn, check your last paragraph. If it is a plan, an analysis, a question, a list of next steps, or a promise about work you have not done, do that work now with tool calls." + "Before running a command that changes system state... check that the evidence actually supports that specific action." (2) "Delivering work": the request or approved plan sets scope; don't quietly narrow/widen/swap; if one part is blocked, complete every other part and say exactly what was left out and why; a decided step is "something to run, not to announce"; extras are suggestions at the end. The opening "user is not watching" sentence "carries much of the effect".
- Compaction summary prompt (use when compacting client-side): preserve (1) problems and how resolved, (2) options tried/set aside and why, (3) asked/decided/ruled-out items stated exactly, (4) exactly where things stand, (5) open/promised/next items, (6) hard-to-reconstruct specifics (names, numbers, dates, exact wording, links) kept exactly; keep the user's voice close to their own words, condense the assistant's reasoning. Complete on these "even at the cost of length".
- Compaction timing: cache reads are cheaper, so "compacting early to save cost may no longer be the right cost-intelligence tradeoff... experiment with later compaction points."
- Keep conversation history append-only (edits invalidate thinking blocks and the prompt cache): per-turn reminders as turn-scoped system messages; let server-side compaction/context editing trim.
- Progress updates: fewer user-facing updates by default; ask for a before-start line and a standalone closing recap ("what you found, what you did, and what's next - so a reader who only sees the last message has the full picture").
- Scope: don't fix pre-existing bugs or extend behaviour unless required; report as follow-up; state assumptions in summary.
- Subagents: do not force the lead to block; subagent-start tool returns immediately, result delivered in a later user message, lead has a separate wait tool; "lowers average time to completion at similar quality, token usage, and cost".
- Parallel tool calls: nudge "First privately list what you need next; then request every item that doesn't depend on another's result in this one response."
## Quotable
> "A step you have decided on is something to run, not to announce"
> "If one part turns out to be blocked, complete every other part in full and say exactly what you left out and why"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-context-engineering]]
