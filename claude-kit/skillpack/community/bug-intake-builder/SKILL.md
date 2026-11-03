---
name: bug-intake-builder
description: "Set up how community bug reports reach the developer: an intake form or Discord template, required fields, a duplicate-merging and priority routine run by a script, and a reply habit that closes the loop. Use when bug reports arrive scattered, incomplete or duplicated, or before opening a public beta."
category: community
tags: bugs, intake, triage, form, template, discord, duplicates, priority, support, playtest
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/playtesting-and-feedback.md
related: bug-report-template, feedback-synthesizer, crash-log-reader, regression-checklist-builder, tester-recruitment-planner, support-macro-writer, faq-writer
---

# bug-intake-builder

`bug-report-template` defines what a good report looks like. This builds the pipe around it: where reports go, how they are deduplicated and ranked, and how players hear back. The vault: set up a community that helps find bugs and crashes, cross-check Error Report findings against player reports (device and region), and escalate platform-level crashes to Roblox.

## When to use
Reports come from Discord, comments and DMs in different shapes; the same bug is reported ten times; a beta is coming. Not for: the report wording (`bug-report-template`), reading crash logs (`crash-log-reader`), or ranking feature ideas (`feedback-synthesizer`).

## Inputs (max 2)
1. Where reports arrive now (default: Discord + game comments). 2. Who triages and how often (default: one person, daily).

## Procedure
1. Choose one front door: a form, or a Discord channel with a pinned template and a bot-free fallback (copy the template). Fields: what happened, what you expected, steps (numbered), device and platform, game version or time, and a screenshot or clip. No personal information is requested; reports never include passwords or account details.
2. Define severity 1-4 (1 cosmetic, 2 annoying, 3 breaks a feature, 4 blocker, data loss or crash) and the reply promise per level (acknowledge within a day for 3-4).
3. Log every report in `bugs/reports.csv` with columns `title,steps,device,severity,reporter` (reporter as a handle or id only).
4. Triage weekly or daily with `python scripts/intake_triage.py bugs/reports.csv`: it merges near-duplicate titles, ranks by severity times the square root of report count, and lists INCOMPLETE reporters. Read the ranking; override it for security and data-loss reports, which jump the queue.
5. For incomplete reports, ask once, publicly or in the ticket, for the missing steps or device; never by private message to a minor.
6. Cross-check the top items against the Studio and Creator Hub error and crash reports (device, platform, version) to decide whether the bug is yours or the platform's; platform-level crashes go to Roblox via the bug channel, not to a fix attempt.
7. Close the loop: tag status (new, confirmed, fixing, fixed in version X, cannot reproduce) and post fixed items in the patch notes with thanks.
8. Security-flavoured reports (dupes, exploits) go to staff only, never to a public channel; follow `exploit-audit` handling.

## Studio MCP path
To reproduce: `list_roblox_studios` -> `get_studio_state` -> `start_stop_play` -> `get_console_output` -> `execute_luau` for a setup; fixes go through `multi_edit`. Reproduction in Studio is optional and varies by device: mobile and console bugs stay `untested` in Studio.

## Fallback
The CSV, the template and the script work without Studio.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md` and `Roblox/roblox-kb/community-and-discord.md` (set up a user community that helps find bugs and crashes; cross-check Error Report findings with player reports noting devices and regions; escalate platform-level crashes to Roblox). `Roblox/roblox-kb/playtesting-and-feedback.md`.

## Output
`bugs/INTAKE.md` (front door, fields, severity table, reply promises), the CSV schema, and the triage output of the latest run. Under 70 lines.

## Acceptance checks
- [ ] `intake_triage.py bugs/reports.csv` run and its ranking quoted (or `--selftest` quoted if no reports exist yet).
- [ ] Every field is justified; none collects personal data.
- [ ] Severity 4 and exploit reports have a fast path.
- [ ] A status vocabulary and a "fixed in version" post step exist.
- [ ] No step asks a minor to move to a private message.

## Pitfalls
Three front doors. Treating the loudest report as the top one. Ranking by report count alone (the script uses severity times the square root of count for a reason). Public exploit details. Never telling reporters the fix shipped.

## Related
`bug-report-template`, `feedback-synthesizer`, `crash-log-reader`, `regression-checklist-builder`, `support-macro-writer`.
