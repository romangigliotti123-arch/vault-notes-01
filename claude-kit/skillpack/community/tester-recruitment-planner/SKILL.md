---
name: tester-recruitment-planner
description: "Find, brief and keep a core group of 8-10 playtesters for a Roblox game: where to recruit, who to include so feedback is not biased, a safe consent-aware brief, test session rhythm and thanks. Checks the roster for platform, newcomer and source balance. Use before a first playtest, before launch, or when feedback feels like it only comes from friends."
category: community
tags: playtest, testers, recruitment, roster, brief, community, feedback, discord, safety
kb: Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: feedback-channel-planner, playtest-bot-writer, discord-server-setup, bug-intake-builder, feedback-synthesizer, first-minute-designer
---

# tester-recruitment-planner

Tizzy keeps 8-10 core playtesters in his Discord, plans updates with them and has them test before launch (vault). Roblox says to start small: invite friends and testers first, then grow slowly. This plans who to ask, how to brief them and how to avoid a roster that tells you only what you want to hear.

## When to use
Before the first outside playtest, before launch, or when only friends give feedback. Not for: automated bots (`playtest-bot-writer`), the first-minute design (`first-minute-designer`), or the channel for feedback (`feedback-channel-planner`).

## Inputs (max 2)
1. Game stage and target audience (default: pre-launch, mostly young players). 2. Where the developer already has reach (default: friends, a small Discord, the group).

## Procedure
1. Set the target mix: 8-10 core testers plus a rotating pool; include new players (design default: at least a third who have never seen the game), regulars and a few veterans; cover mobile, PC and console where the game supports them.
2. Choose sources: your Discord and group, other devs' showcase channels with permission, a tester sign-up post in your updates channel, and creators who match the genre. Avoid cold mass DMs and never DM minors; recruit in public posts and let people apply.
3. Safety first: the sign-up asks for a Roblox username only. No ages, real names, phone numbers or photos. Tell parents/guardians what the test is (a game test, no purchases required) in the post; sessions with younger players happen in public channels or in-game, with adult staff only.
4. Write the brief (under 120 words): what to test today, how long, how to report (the bug template), what not to do (share builds, leak content), and the thanks you offer (tester role, credit with consent, early access, never Robux-for-feedback promises that break platform rules; live-check).
5. Keep the roster as a CSV `testers/roster.csv` with columns `handle,platform,experience,source` and run `python scripts/roster_check.py testers/roster.csv`; fix FAILs, read WARNs (single-source bias, no mobile, no new players), rerun.
6. Run sessions on a rhythm: one focused test per week before launch, a 5-minute debrief poll, and report back what changed because of them.
7. Weight their feedback by source and hours played; one loud tester is one data point.
8. Thank them publicly (with consent) and rotate in fresh newcomers so the group does not drift into insiders.

## Studio MCP path
Not needed. Optional: `list_roblox_studios` -> `get_studio_state` to confirm the build testers get is the one under test, and `get_console_output` after a session for crashes.

## Fallback
Plain text and one CSV. Sending invites is the owner's action.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (build a core playtester group of 8-10; treat testers and mods as an extension of the team; grow from 10 to 50 to 100 before scaling marketing). `Roblox/roblox-kb/playtesting-and-feedback.md` (weight feedback by source). The vault itself notes it has no guidance on consent or age considerations when recruiting testers: the safety rules above are conservative defaults, live-check platform policy. `Roblox/roblox-kb/testing-debugging-and-qa.md`.

## Output
`testers/brief.md`, `testers/roster.csv`, a recruitment post draft, and a session calendar for four weeks. Under 80 lines.

## Acceptance checks
- [ ] `roster_check.py` exit 0 on the roster CSV; output quoted (size, platform, new-player share, source mix).
- [ ] The sign-up collects a username only.
- [ ] No step involves cold DMs to minors or promises of Robux for feedback.
- [ ] The brief fits in 120 words and links the bug template.
- [ ] A debrief and a "what changed because of you" post are scheduled.
- [ ] Testing starts as closed access through a Roblox group; a Beta-tagged open test only once the game is playable end to end on all target platforms; each playtest has one goal and about one minute per check; retention tests are time-boxed to a weekend or one week (official; Roblox/roblox-kb/_tools/DECISION-RULES.md, playtesting-and-feedback).

## Pitfalls
Only friends. Only veterans. Collecting ages and real names. Testers who share the build. Never reporting back, so they leave. Treating one tester's taste as the audience.

## Related
`feedback-channel-planner`, `playtest-bot-writer`, `bug-intake-builder`, `feedback-synthesizer`.
