---
name: fan-art-contest-planner
description: "Run a safe fan-art, build or idea contest for a Roblox game: clear rules (originality, credit, age-appropriate, no personal info), a fixed scoring rubric set before judging, anonymous scoring across judges with a script, prize and permission terms. Use when you want community content without legal, safety or fairness trouble."
category: community
tags: contest, fan-art, ugc, rubric, judging, prizes, permission, credit, community, safety
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/ugc-and-avatar-economy.md
related: community-event-planner, community-showcase-planner, social-proof-collector, ugc-moderation-checker, moderation-rules-writer, community-poll-writer, ugc-item-planner
---

# fan-art-contest-planner

Jailbreak sources many assets from its community; creators run contests and workshops for art, vehicles, weapons and characters, ask permission, credit or pay creators, and rebuild submissions in-house for a consistent style. The vault also says to score every entry on one fixed rubric. This sets up the contest so it is fun, fair and safe for young entrants.

## When to use
You want fan art, builds, ideas or names from the community. Not for: general events (`community-event-planner`), a showcase thread (`community-showcase-planner`), or selling UGC items (`ugc-item-planner`).

## Inputs (max 2)
1. Contest type and prize (default: fan art, a cosmetic or credit, no cash). 2. Judges (default: dev + 2 trusted staff; at least one adult not involved with any entrant).

## Procedure
1. Fix the rules in a single post: theme, dates, one entry per person (or a stated limit), original work only, no copyrighted characters or logos you do not own, nothing violating the platform's Community Standards, age-appropriate content, no personal information in the art or captions. Include the permission term: entrants keep their rights but grant permission to show the entry in the contest and the winners' work in announcements with credit; anything used in the game needs a separate written agreement (credit or payment).
2. Safety for young entrants: submissions via a public thread or ticket (not DMs); entries are reviewed by moderators before display; no real names, school or location; winners may be named by handle only with agreement; guardian involvement for anything involving payment.
3. Set the rubric before anyone submits: criteria and weights (e.g. creativity 3, theme 2, polish 1; design defaults, not vault values), a 0-5 scale, and the tie-break rule (publish it).
4. Judging: assign entries anonymous ids (E01...), each judge scores every criterion for every entry independently in `contest/scores.csv` (`entry,judge,criterion,score`). Run `python scripts/contest_score.py contest/scores.csv --weights creativity=3,theme=2,polish=1`; FAIL on missing or out-of-range scores; a WARN on judge disagreement means discuss before ranking; a tie WARN means apply the published tie-break.
5. Prizes: cosmetics or credit with no purchase needed; if any Robux or item prize is considered, the owner decides and checks the platform's rules on prizes and giveaways (live-check). No entry fee, no purchase to enter.
6. Announce winners with a short feedback note for runners-up, and offer a "highlights" showcase of all safe entries with the makers' permission.
7. Lint the rules and announcement posts: `python welcome-message-writer/scripts/text_lint.py contest-posts.txt`.

## Studio MCP path
Only if winning art goes into the game: `list_roblox_studios` -> `get_studio_state`, then follow `ugc-moderation-checker` and rebuild in-house in your own style (vault) rather than importing the upload directly; moderation of uploaded assets must be done before use.

## Fallback
Text plus the CSV scorer; all posting and prizing is the owner's action.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (source content via contests and workshops; always ask permission and credit or pay creators; rebuild in-house for style). `Roblox/roblox-kb/playtesting-and-feedback.md` (score every submission on a fixed rubric; contest cutoffs are self-reported examples from one contest, not standards). `Roblox/roblox-kb/ugc-and-avatar-economy.md`.

## Output
`contest/RULES.md`, `contest/scores.csv` template, the ranking output, announcement drafts. Under 80 lines.

## Acceptance checks
- [ ] `contest_score.py` exit 0 on the score CSV, ranking and WARNs quoted.
- [ ] Rules state originality, credit, permission, age-appropriate content, no personal info and no entry fee.
- [ ] Entries are scored anonymously on a rubric fixed before submissions opened.
- [ ] `text_lint.py` exits 0 on the posts.
- [ ] Any in-game use needs a separate agreement; nothing is imported unmoderated.

## Pitfalls
Rubric invented after seeing entries. Judging friends' entries. Cash or Robux prizes without checking rules. Using art in the game without agreement. Public shaming of low-scoring entries. DM submissions from minors.

## Related
`community-event-planner`, `community-showcase-planner`, `ugc-moderation-checker`, `social-proof-collector`.
