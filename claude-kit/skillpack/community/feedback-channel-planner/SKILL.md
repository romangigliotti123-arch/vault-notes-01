---
name: feedback-channel-planner
description: "Pick and run the right player feedback channel for a Roblox game: Discord suggestions, group wall, native community-page polls, in-game feedback, Q and A sessions, playtests. Chooses one primary channel per feedback type, names the reader and cadence, and sets how feedback is tagged and answered. Use when feedback is scattered, ignored or dominated by a loud minority."
category: community
tags: feedback, channels, suggestions, discord, group, polls, triage, cadence, loop
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/social-features-and-virality.md
related: feedback-synthesizer, community-poll-writer, bug-intake-builder, tester-recruitment-planner, discord-server-setup, retention-diagnoser
---

# feedback-channel-planner

The vault says it plainly: use the right channel for each feedback type, choose the one channel that gives the most actionable input (ideally one you control), monitor it for patterns, and keep final design control. This chooses and sets up that system on paper.

## When to use
Feedback arrives in five places and none is read, or one loud group steers design. Not for: summarising existing feedback (`feedback-synthesizer`), writing a poll (`community-poll-writer`), or bug intake details (`bug-intake-builder`).

## Inputs (max 2)
1. Current channels and rough volume per week (default: Discord + group wall + comments). 2. Team size and who has time to read daily (default: solo dev, 15 minutes a day).

## Procedure
1. Sort feedback into five types: bugs, balance and feel, new ideas, praise and complaints about the experience, and support questions. Each type gets exactly one home channel.
2. Pick channels by fit: bugs go to a form or template channel; ideas go to a suggestions channel where reactions act as upvotes; balance and feel go to a short poll plus telemetry; broad news and polls go to the native community page or group; deep one-to-one talk goes to Discord threads. Stop at one primary channel per type and one reader per channel.
3. Name the reader and the cadence: a single named person reads daily (15 minutes), tags each item (bug, idea, balance, praise), and sends a weekly summary to the dev (`feedback-synthesizer`).
4. Add weighting: weigh feedback by source (a playtester who played ten hours vs a one-line drive-by) and note repeated asks. Players find problems better than solutions: for each idea record the underlying problem, ask why, and keep final design control.
5. Close the loop: a monthly "you said, we did" post; reply publicly to broken features only; thank contributors by role or handle with their consent.
6. Set up in-game feedback only where it is safe: a text box must go through server filtering, be rate limited, and never ask for personal info; link to `chat-filter-tester` for the check.
7. Define success: median time to first reply, share of items tagged, number of shipped changes credited back. Stop after a 4-week trial and review.

## Studio MCP path
Only for an in-game feedback form: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add the UI and a server handler using `TextService:FilterStringAsync`; `start_stop_play` and `get_console_output` to verify. The connection is optional.

## Fallback
All text and a channel table. Creating channels and forms is the owner's action.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (right channel per feedback type; filter feedback and keep final design control; probe the reasoning behind suggestions; Discord suggestion channels with upvotes, Q and As, in-game feedback and community-page polls all work). `Roblox/roblox-kb/playtesting-and-feedback.md` (weight feedback by source; players identify problems better than solutions). `Roblox/roblox-kb/social-features-and-virality.md`.

## Output
`community/feedback-plan.md`: type-to-channel table (channel, reader, cadence, tag set), weekly summary template, monthly post template, success measures. Under 80 lines.

## Acceptance checks
- [ ] Each of the five types maps to exactly one channel and each channel has one named reader role.
- [ ] A weekly summary and a monthly "you said, we did" post exist as templates.
- [ ] The plan states who decides (the developer) and what is never promised from votes.
- [ ] Any in-game text box is server-filtered and rate limited in the plan.
- [ ] `python welcome-message-writer/scripts/text_lint.py feedback-posts.txt` exits 0 on the weekly-summary, monthly-post and in-game form copy (output quoted).
- [ ] The plan is small enough for the stated team size (15 minutes a day for a solo dev).

## Pitfalls
Five channels, no reader. Treating upvotes as a design vote. Never replying. Promising a feature because a poll liked it. Collecting feedback from minors by DM. Ignoring accessibility reports as "skill issues".

## Related
`feedback-synthesizer`, `community-poll-writer`, `bug-intake-builder`, `tester-recruitment-planner`, `discord-server-setup`.
