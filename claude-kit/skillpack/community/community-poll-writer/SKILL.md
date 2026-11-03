---
name: community-poll-writer
description: "Write polls that give usable answers: one neutral question, three to six distinct options, an escape option, wording that does not promise the result, and a plan for what the answer will change. Lints the poll file for leading questions and bad option counts. Use before any Discord, group or community-page poll."
category: community
tags: poll, survey, community, discord, feedback, questions, bias, community-page
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/social-features-and-virality.md
related: feedback-channel-planner, feedback-synthesizer, community-event-planner, update-announcement-writer, fan-art-contest-planner, welcome-message-writer
---

# community-poll-writer

Polls gauge wants; the developer decides (vault). A poll with a steering question or a pile of near-identical options produces noise you then wrongly treat as a mandate. This writes polls whose answers you can act on.

## When to use
Before a Discord poll, a community-page poll or a quick in-game vote. Not for: choosing the whole feedback system (`feedback-channel-planner`), analysing open comments (`feedback-synthesizer`), or judging entries (`fan-art-contest-planner`).

## Inputs (max 2)
1. The decision the poll informs (default: ask the owner to state it in one sentence; no decision, no poll). 2. The audience and the channel (default: Discord, mostly young players).

## Procedure
1. Write the decision first: "We will use this to choose X or Y by date Z". If nothing will change with the answer, do not poll.
2. One question, neutral wording, one topic. Split "do you want pets and maps?" into two polls. Avoid words that steer (obviously, amazing, best ever, don't you).
3. Options: 3-6, mutually distinct, in a randomised or alphabetical order, with a "not sure / other" escape when the poll asks what people want. Each option is real: only offer what you could ship.
4. Do not promise the outcome in the poll text; say "your vote helps us decide". Keep final design control (vault): weigh results by who voted (engaged members vs drive-by) and note the vocal-minority risk.
5. Safety: no polls asking for personal information, ages or locations; a poll about a purchase or a price shows no pressure and no urgency tricks; polls about moderation outcomes of named individuals are not run.
6. Put the poll in a file `community/polls.txt` (`Q: ...` then `- option` lines, blank line between polls) and run `python scripts/poll_lint.py community/polls.txt`; fix every FAIL and read every WARN; rerun to exit 0.
7. Choose the closing time and the follow-up: close after a fixed window, post the result with the decision it informed and what happens next (feeds the monthly "you said, we did").
8. Also lint the announcement text: `python welcome-message-writer/scripts/text_lint.py poll-post.txt`.

## Studio MCP path
Only for an in-game vote: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add a server-validated vote (one vote per UserId, results tallied on the server) and `start_stop_play` to test; a quick Discord or community-page poll needs no Studio.

## Fallback
Text file and script. Posting is the owner's action; the native community-page polls are created by the owner in Roblox.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (polls gauge wants but the developer decides; filter feedback and keep final design control; native community-page announcements with polls notify members instantly; probe the reasoning behind suggestions). `Roblox/roblox-kb/playtesting-and-feedback.md` (weight feedback by source; players identify problems better than solutions).

## Output
`community/polls.txt` (lint-clean polls), a poll post draft per poll, and a result-post template naming the decision. Under 50 lines.

## Acceptance checks
- [ ] `poll_lint.py` exit 0; output quoted (no FAIL on count, leading wording or duplicates).
- [ ] Each poll names the decision it informs and a closing date.
- [ ] No poll asks for personal data or promises the winner will ship.
- [ ] `text_lint.py` exits 0 on the post.
- [ ] A result post is scheduled.

## Pitfalls
Polls with no decision behind them. Leading wording. Ten options. Treating a vote as a binding promise. Polling too often. Running a poll about a specific player.

## Related
`feedback-channel-planner`, `feedback-synthesizer`, `community-event-planner`, `update-announcement-writer`.
