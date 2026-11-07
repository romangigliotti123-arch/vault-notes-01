---
name: feedback-synthesizer
description: "Cluster player feedback (Discord, comments, ratings, playtest notes) into ranked themes with counts and quotes, check each theme against metrics, and turn the top ones into candidate changes. Use before planning an update or when the community is loud and you need the signal."
category: liveops
tags: feedback, player feedback, themes, discord, comments, requests, prioritisation, community, playtest, voice of player
kb: Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/analytics-metrics.md
related: churn-reason-finder, retention-diagnoser, patch-notes-writer, update-cadence-planner, rbx-playtest, discord-server-setup, rbx-critic
---

# feedback-synthesizer

The vault: start updates from a problem and a KPI, combine community feedback (Discord, polls, ratings) with metrics and tests, and check requests against the data before building them. This skill does the first half: turn a pile of comments into counted themes with evidence. It uses keyword matching, so it counts, it does not understand; you read the samples.

## When to use
Before an update plan, after a rough release, or when Discord is on fire. Not for: structured playtest sessions (`rbx-playtest`), writing the announcement (`patch-notes-writer`), or diagnosing a metric (`retention-diagnoser`).

## Inputs (max 2)
1. The feedback as text, one comment per line, with the source noted (Discord channel, game comments, store reviews, playtest notes); a CSV with a `text` column also works. 2. Time range and what shipped in it.

## Procedure
1. Collect from one source at a time and remove duplicates and bot lines. Keep one line per player per topic if you can; the script counts mentions, not unique players.
2. Run `python -I .rbx/claude-kit/skillpack/liveops/feedback-synthesizer/scripts/feedback.py feedback.txt --top 8 --samples 2`. Default themes: lag/performance, bugs/crashes, grind/progression, price/monetisation, more content, controls/mobile, exploiters/cheaters, social/trading, balance. Replace them with your own via `--themes themes.json` (`{"theme": ["keyword", ...]}`) for a game with its own vocabulary.
3. Read the unmatched sample it prints; add keywords for any theme it missed and re-run. Stop condition: unmatched share under about 30 percent and no unnamed theme in the samples.
4. For each of the top themes, find the metric that would confirm it: lag -> crash rate, FPS percentiles on low-end devices; grind -> time to first upgrade, session length; price -> payer conversion, shop funnel; bugs -> error counts grouped by message; exploiters -> economy sources. A loud theme with no metric support may be a vocal minority; a quiet theme with metric support (a leak in the funnel) outranks it.
5. Segment: new players vs veterans, platform, spenders vs free. Veterans ask for content; newcomers hit onboarding walls (vault: balance new content against newcomer onboarding).
6. Rank candidate changes by severity, effort and players affected (vault rule for bugs), mark quick wins, and separate "fix" from "feature".
7. Close the loop: reply to the top themes publicly ("fixed", "planned", "not planned and why"), list fixed bugs in the notes, and re-run in a month to see whether the theme shrank.
8. Keep a feedback log so repeated requests accumulate evidence. Do not quote or store names; keep usernames out of shared files.

## Studio MCP path
Not needed. To check a bug theme: `get_console_output` after reproducing, `script_grep` for the named feature.

## Fallback
Python 3 on a text file; works with pasted comments. Ratings: judge the like ratio over a recent window after a fix, not lifetime totals (vault).

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: drive updates from data and feedback; blend community suggestions with your own roadmap; prioritise fixes by severity, effort and players affected; publish a changelog of fixed items. `playtesting-and-feedback.md` for how to gather and weigh qualitative input. `analytics-metrics.md`: pair telemetry with qualitative playtests; judge ratings on recent data after a fix. `community-and-discord.md` for channels.

## Output
```
FEEDBACK <source> <range>: N comments, unmatched M%
rank | theme | mentions | % | confirming metric | samples
Candidate changes (quick win / fix / feature) with severity, effort, players affected
Public reply plan, re-check date
```

## Acceptance checks
- [ ] `feedback.py --selftest` prints "selftest ok (6 checks)".
- [ ] Unmatched lines were read and the themes list updated.
- [ ] Each top theme names a confirming metric or is marked unconfirmed.
- [ ] Counts are described as mentions, not unique players.
- [ ] No usernames in the output.

## Pitfalls
Treating the loudest voice as the majority. Counting one player's ten messages as ten. Building requested features that the data shows no one uses. Ignoring newcomers who never post. Over-trusting keyword themes.

## Related
`churn-reason-finder`, `retention-diagnoser`, `patch-notes-writer`, `update-cadence-planner`, `rbx-playtest`.
