---
name: community-event-planner
description: "Plan cheap, repeatable community events around a Roblox game: a themed day, a build or art contest, a Q and A, a dev stream, a tester night. Picks the format for the team size, writes a dated run sheet (tease, reminders, go-live, recap, close-the-loop) and a moderation plan. Use when the community is quiet between updates or you want a regular reason for players to return."
category: community
tags: events, community, discord, themed-day, qa, contest, schedule, run-sheet, moderation, recurring
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/social-features-and-virality.md
related: event-planner, discord-server-setup, fan-art-contest-planner, update-announcement-writer, moderation-rules-writer, community-poll-writer
---

# community-event-planner

This is for events that live in the community (Discord, group, social posts, a tester night), not in-game seasonal events. The vault: run a regular themed event day, engage players daily early on, tie any rewards to participation without pay-to-win, and tease from about ten days out with the date and time. Small and repeatable beats rare and huge.

## When to use
Quiet stretches between updates, a Discord with members but no rhythm, or before launch to build anticipation. Not for: in-game live events and economy (`event-planner`, `seasonal-calendar-builder`), contests judged on entries (`fan-art-contest-planner`), or update posts (`update-announcement-writer`).

## Inputs (max 2)
1. Team size and hours per week for community (default: solo dev, 2 hours). 2. Audience age and size (default: mostly young, under 500 members).

## Procedure
1. Pick one format from the cheap menu: themed day (post prompts, screenshot day), Q and A with the dev, dev stream or devlog, tester night, community vote on a cosmetic, show-off thread. Choose the one the team can run every 2-4 weeks without burning out.
2. Fix the schedule: same weekday and hour so people arrive together; state the time zone and give a converter-friendly time. Run `python scripts/event_run.py --date YYYY-MM-DD --hour 18 --title "<name>"` to produce the dated beats (tease about ten days out, reminder, go-live, recap, close-the-loop) and paste the output.
3. Define the participation hook and a small reward that does not require payment and does not become pay-to-win (a cosmetic role, a credit post, an in-game cosmetic the owner approves). If a code is used, hand over to `codes-campaign-planner`.
4. Moderation plan (the part people skip): two staff online, slow mode on, a one-line rule reminder pinned, no voice or video with minors unless adult staff run it under the platform's rules (live-check Discord and Roblox rules), no personal info in submissions. Rules from `moderation-rules-writer`.
5. Write the three posts (tease, reminder, go-live) and a recap template; lint them with `python welcome-message-writer/scripts/text_lint.py event-posts.txt`.
6. Define success: attendance, new members, messages per attendee, bugs or ideas found, return rate to the game next day; not just raw CCU (Discord-event CCU is artificial for organic-growth judgments, per the vault).
7. After the event: publish the recap within a day, collect feedback with one poll, and decide repeat/change/drop; stop after three runs to review.

## Studio MCP path
Not needed for the community side. If an in-game hook is wanted (a follow button, a timed server message), use `list_roblox_studios` -> `get_studio_state` -> `multi_edit` and `start_stop_play`; the vault notes a touch-part prompt to follow the scheduled event.

## Fallback
Everything is text and a run sheet. Scheduling and posting are the owner's actions.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (regular themed event day; tie monetisation to events so non-payers participate; judge community by anticipation, not plays; Discord-event CCU is artificial for organic judgments). `Roblox/roblox-kb/events-and-seasonal-content.md` (tease early, give date and time, announce on every channel). `Roblox/roblox-kb/social-features-and-virality.md`.

## Output
`community/event-<name>.md`: format, schedule table from the script, posts, moderation plan, success measures, repeat decision. Under 80 lines.

## Acceptance checks
- [ ] `event_run.py` output pasted with real dates and a time zone label.
- [ ] A named host and two staff are on the run sheet; slow mode and rules reminder are on the checklist.
- [ ] Rewards need no payment and no personal information.
- [ ] `text_lint.py` exits 0 on the three posts.
- [ ] A recap and a review date after three runs are scheduled.

## Pitfalls
A huge one-off nobody can repeat. Surprise events with no moderators. Voice chats with minors. Rewards that become pay-to-win. Judging success by CCU during the event only. Forgetting the recap.

## Related
`event-planner`, `fan-art-contest-planner`, `update-announcement-writer`, `moderation-rules-writer`, `codes-campaign-planner`.
