---
name: post-mortem-writer
description: "Write a blameless post-mortem for a failed release, a lost-work incident, a missed milestone or a worker run that went wrong: timeline from logs and git, root cause chain, what worked, and actions with owners and checks. Use within a few days of the event while the evidence still exists."
category: workflow
tags: post-mortem, retro, incident, blameless, root cause, lessons, failure, review
kb: Manager/src-anthropic-april-23-postmortem.md, Manager/topic-multi-agent-failure-modes.md, Manager/topic-observability.md, Roblox/roblox-kb/common-mistakes.md, Roblox/roblox-kb/development-process-and-speed.md, Mentor/Combined-Brain.md
related: decision-log-writer, tech-debt-lister, worker-verifier, session-handoff, milestone-reviewer, devlog-writer, version-history-keeper
---

# post-mortem-writer

For events that cost real time or data: a bad update that rolled back, work lost to an overwrite, a milestone that slipped two weeks, a worker that reported done on a broken build. The output is a short document of facts and checkable actions, not blame. Game-performance post-launch analysis is `retention-diagnoser` and `post-launch-monitor`; this is about the development process.

## When to use
An incident or miss happened and a repeat would cost again. Not for: ordinary bugs (use a bug report), or a feeling that "the week went badly" with no event.

## Inputs (max 2)
1. What happened, in one sentence, with date and impact (hours lost, players affected, data lost). 2. Where the evidence is (default: git log, `docs/PROGRESS.md`, `jobs.md`, worker reports, Output logs).

## Procedure
1. Collect evidence before writing: `git log --since=<date> --stat`, reports in `reports/`, the ledger, console logs. Paste excerpts; if evidence is gone, say "no record" rather than reconstruct from memory.
2. **Timeline**: dated lines of what happened and what was known at the time. Facts only; no adjectives about people.
3. **Cause**: walk the chain at least three "why" levels deep, ending at something the process can change (a missing check, an unclear brief, no restore point), not at a person. Mark each link `evidenced` or `inferred`. Check the usual suspects: unclear spec, no verification step, parallel writers on one file, unreviewed claim of done, missing backup.
4. **What worked**: the checks and habits that limited the damage (a restore point, a clean diff). Keep these.
5. **Actions**: each with an owner, a due date, and a check that shows it is done (a hook installed, a gate added to the release checklist, a brief template line). Prefer structural fixes (hooks, checks, permissions) over "be more careful".
6. Fold lessons back: one line to `docs/decisions.md` (`decision-log-writer`), and for worker incidents one line in `docs/worker-incidents.md` ("brief lacked X"), and update the brief template or checklist that failed.
7. Save `docs/postmortems/YYYY-MM-DD-title.md` (headings Timeline, Cause, What worked, Actions; under 110 lines; needs evidence marks) and check it. Schedule a 30-day look at whether the actions are in place.

## Studio MCP path
Optional: `get_console_output` or version information to capture the state of an affected place; nothing is changed.

## Fallback
Git and files only. Studio-side facts (which version was live, who published) come from Creator Hub history, which the user reads.

## Evidence
`Manager/src-anthropic-april-23-postmortem.md` (a primary postmortem: product-layer changes, not the model, caused the quality drop; found by examining each change and its dates), `Manager/topic-multi-agent-failure-modes.md` (failures are mostly specification and verification; keep an incident log as calibration data), `Manager/topic-observability.md`, `Roblox/roblox-kb/common-mistakes.md`, `Roblox/roblox-kb/development-process-and-speed.md` (duplicate or back up before destructive edits; one creator deleted the main game mid-build).

## Output
`docs/postmortems/<date>-<title>.md` and the folded-back lines.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/postmortems/<file>.md --kind postmortem` prints PASS (evidence marks required).
- [ ] The cause chain ends at a process change, not a person.
- [ ] Every action has owner, date and a verifying check.
- [ ] At least one lesson was folded into a template, checklist or hook.

## Pitfalls
Writing a story instead of a timeline. Stopping at "human error". Actions like "test more". Hiding that evidence is missing. Writing it weeks later from memory.

## Related
`decision-log-writer`, `tech-debt-lister`, `worker-verifier`, `session-handoff`, `milestone-reviewer`, `version-history-keeper`.
