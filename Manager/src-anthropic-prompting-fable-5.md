---
tags: [manager-kb, source]
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
type: official-doc
author: Anthropic
published: undated
accessed: 2026-10-29
reliability: high (official; also read Fable 5.1 page sections "Finish the whole task" and "Let the lead agent keep working")
---
# Prompting Claude Fable 5 / Fable 5.1
## Key claims
- "Ground progress claims during long runs": snippet "Before reporting progress, audit each claim against a tool result from this session. Only report work you can point to evidence for; if something is not yet verified, say so explicitly. Report outcomes faithfully: if tests fail, say so with the output; if a step was skipped, say that; when something is done and verified, state it plainly without hedging." Anthropic reports this "nearly eliminated fabricated status reports even on tasks designed to elicit them" (their testing, Fable 5).
- "Give the reason, not only the request": template "I'm working on [the larger task] for [who it's for]. They need [what the output enables]. With that in mind: [request]." Context lets the model connect the task to relevant information.
- Brevity: "Lead with the outcome. Your first sentence after finishing should answer 'what happened' or 'what did you find'... The way to keep output short is to be selective about what you include..., not to compress the writing into fragments, abbreviations, arrow chains".
- Checkpoint rule: "Pause for the user only when the work genuinely requires them: a destructive or irreversible action, a real scope change, or input that only they can provide."
- Boundaries: when the user is describing a problem rather than asking for a change "the deliverable is your assessment. Report your findings and stop."
- Parallel subagents: "Delegate independent subtasks to subagents and keep working while they run. Intervene if a subagent goes off track or is missing relevant context." Prefer asynchronous communication; long-lived subagents save cache cost.
- Early stopping (rare): text-only "I'll now run X" with no tool call. Autonomous-pipeline reminder: "The user is not watching in real time... asking 'Want me to...?' will block the work... Before ending your turn, check your last paragraph. If it is a plan, an analysis, a question, a list of next steps, or a promise about work you have not done, do that work now with tool calls."
- Memory system: one lesson per file, one-line summary at top; record corrections and confirmed approaches; update rather than duplicate.
- Fable 5.1: "Finish the whole task" block; "Delivering work" block: "The user's request... sets the scope, and the scope is the deliverable: don't quietly narrow, widen, or swap it... If one part turns out to be blocked, complete every other part in full and say exactly what you left out and why". "A step you have decided on is something to run, not to announce". Letting the lead keep working while subagents run lowers time to completion at similar quality and cost.
## Quotable
> "Before reporting progress, audit each claim against a tool result from this session."
> "If one part turns out to be blocked, complete every other part in full and say exactly what you left out and why"

## Used by
[[topic-anthropic-agent-guidance]], [[topic-brief-prompt-engineering]], [[topic-context-engineering]], [[topic-remote-mobile-ux]], [[topic-report-formats-and-verification]]
