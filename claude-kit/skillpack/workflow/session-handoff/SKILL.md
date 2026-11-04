---
name: session-handoff
description: "Write the handoff note that lets the next Claude session, worker or human resume a Roblox project cleanly: exact state, what is done with evidence, the next step with its command, open questions and how to run it. Use at the end of a session, before a context reset, or when passing the project to someone else."
category: workflow
tags: handoff, resume, session, context, progress, state, pause, continue
kb: Manager/topic-long-running-always-on-agents.md, Manager/topic-context-window-management.md, Manager/topic-context-engineering.md, Roblox/roblox-kb/development-process-and-speed.md, Mentor/Combined-Brain.md
related: project-kickoff, decision-log-writer, worker-verifier, rbx-workflow, ai-brief-writer, onboarding-new-dev
---

# session-handoff

`rbx-workflow` already resumes from `Games/<slug>/GAME.md` and the evidence stage. A handoff is the short human-and-AI-readable note for the gap that file does not cover: what exactly was half-finished, how to run it, what was tried and failed. It is not a status report to Roman (that is the worker report) and not a design doc.

## When to use
End of a working session, before `/compact` or a restart, when a worker stops PARTIAL, or when another person or agent takes over. Not for: the permanent record of why something was chosen (`decision-log-writer`), onboarding a new teammate (`onboarding-new-dev`).

## Inputs (max 2)
1. The project folder (default: current). 2. The current job id if a ledger exists (default: the last row in `jobs.md` that is not DONE).

## Procedure
1. Gather state from files, not memory: `git status --short`, `git log --oneline -5`, `docs/PROGRESS.md`, `jobs.md`. If git is absent, list the files changed today instead and say git is missing.
2. Write **State**: the branch, whether the tree is clean, whether the project builds (`rojo build -o build.rbxl` result line or `untested`).
3. Write **Done** with evidence per line: the command and one output excerpt, or a path. No evidence means it goes under Open, not Done.
4. Write **Next**: ONE next action, with the exact command or file to open first. Then at most three follow-ups.
5. Write **Open**: unanswered questions, blockers, things tried that failed (so the next session does not repeat them), and anything unverified.
6. Write **Run**: how to start (`rojo serve`, Studio connect, test command) in copyable lines; list env needs by name only, never values.
7. Save `docs/HANDOFF.md` (overwrite; the previous one is in git history), keep it under 80 lines, run the check, and append a pointer line to `docs/PROGRESS.md`.

## Studio MCP path
If tools exist: `list_roblox_studios` and `get_studio_state` to record which place is open and whether a playtest is running; `get_console_output` to quote the current Output state. Record "Studio MCP: yes/no".

## Fallback
Shell output of the git commands above pasted into the sections; Studio-only facts are `untested`.

## Evidence
`Manager/topic-long-running-always-on-agents.md` (each new session begins with no memory; state belongs in files; "hallucinated handoff" is a named failure, so verify against git state), `Manager/topic-context-window-management.md` (exact file and id state is what summaries lose first; put it on disk), `Manager/topic-context-engineering.md`, `Roblox/roblox-kb/development-process-and-speed.md` (keep backups and clear specs so work survives a person leaving).

## Output
`docs/HANDOFF.md` with headings State, Done, Next, Open questions, Run (under 80 lines).

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/HANDOFF.md --kind handoff` prints PASS (needs an evidence mark).
- [ ] Executed: `git status --short` was run in this session and its result is reflected in State.
- [ ] Next names one concrete first action a stranger could start in under a minute.
- [ ] No secret values, tokens or personal data in the file.

## Pitfalls
Writing Done from memory of intent instead of from output. Leaving the failed attempts out, which makes the next session retry them. A Next that says "continue the shop". Pasting the whole transcript; the note is a pointer set.

## Related
`project-kickoff`, `decision-log-writer`, `worker-verifier`, `ai-brief-writer`, `onboarding-new-dev`, `rbx-workflow`.
