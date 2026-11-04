---
name: decision-log-writer
description: "Record a project decision in docs/decisions.md as options considered, the evidence for the pick (vault note, measurement or playtest), the cost of being wrong and a revisit trigger, so later sessions do not re-argue it. Use whenever a design, tooling or scope choice is made that a future worker could reverse by accident."
category: workflow
tags: decision, adr, log, evidence, options, revisit, rationale, record
kb: Manager/topic-knowledge-management-rag.md, Manager/topic-long-running-always-on-agents.md, Roblox/roblox-kb/development-process-and-speed.md, Roblox/roblox-kb/mindset-and-strategy.md, Mentor/Combined-Brain.md
related: session-handoff, scope-creep-guard, post-mortem-writer, kb-lookup-routine, project-kickoff, rbx-workflow
---

# decision-log-writer

`rbx-workflow` creates a `decisions.md` in the game folder and `scope-cutter` appends its cut list there. This skill defines the entry format and when to write one, so the log stays short enough to be read at the start of a session. It is a log of choices, not a diary (`session-handoff`) and not a failure review (`post-mortem-writer`).

## When to use
A choice was made between real alternatives and reversing it would cost more than an hour: data schema shape, Rojo vs Script Sync, a monetisation model, a scope cut, a library adopted. Not for: trivial choices (names, colours) or a task list.

## Inputs (max 2)
1. The decision in one sentence (default: the last choice made in the conversation). 2. The evidence source (default: ask `kb-lookup-routine` for a vault note, else a measurement or playtest file path).

## Procedure
1. Number the entry `D-YYYYMMDD-n`. One entry per decision; split bundled choices.
2. **Decision**: what was chosen, in one sentence, in present tense.
3. **Options**: at least two, including "do nothing", each with one line of cost and one of benefit. If only one option was ever considered, say so; do not invent a straw option.
4. **Evidence**: the source for the pick with its trust label (official, TRUSTED, indie, measurement, opinion). A claim with no source is written as `opinion`; never as fact. Link a vault path or a file in the repo.
5. **Cost of being wrong** and **Revisit** trigger: a measurable condition ("if D1 is under the benchmark after 200 plays", "if two contributors join"), or a date.
6. Mark any entry it replaces as `superseded by D-...` rather than deleting it; append, do not rewrite old entries.
7. Append to `docs/decisions.md` (newest at the bottom), keep each entry under 15 lines, run the check, and mention the entry id in the next handoff.

## Studio MCP path
None.

## Fallback
Markdown append only. Use `git log -p docs/decisions.md` to see the history.

## Evidence
`Manager/topic-knowledge-management-rag.md` (append small dated deltas; every note carries provenance and status; superseded facts are marked, not silently overwritten; Karpathy-style append-only log), `Manager/topic-long-running-always-on-agents.md` (a decisions file the next session re-reads), `Roblox/roblox-kb/development-process-and-speed.md` (avoid re-doing work; cut scope under deadline), `Roblox/roblox-kb/mindset-and-strategy.md`, `Mentor/Combined-Brain.md` (where sources disagree, record which side was taken and why).

## Output
One appended entry in `docs/decisions.md` with headings Decision, Options, Evidence, Revisit.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/decisions.md --kind decision` prints PASS (headings Decision, Options, Evidence, Revisit present).
- [ ] At least two options listed or the single-option statement present.
- [ ] Evidence line has a trust label or the word `opinion`.
- [ ] Revisit is a condition or date, not "later".

## Pitfalls
Logging after the fact with invented alternatives. Evidence that is only "Claude said so". Editing old entries so history disagrees with git. A log so long nobody reads it: archive entries older than the current milestone into `docs/decisions-archive.md`.

## Related
`session-handoff`, `scope-creep-guard`, `post-mortem-writer`, `kb-lookup-routine`, `project-kickoff`.
