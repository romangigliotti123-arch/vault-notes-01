---
name: devlog-writer
description: "Write a short, honest devlog entry from what was actually shipped this week: real numbers, a before/after, what went wrong and the next step, in a steady cadence before and after launch. Use weekly while building in public, or when preparing pre-launch posts; it never invents progress or metrics."
category: workflow
tags: devlog, dev log, build in public, weekly update, progress, content, pre-launch, cadence
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/development-process-and-speed.md, Mentor/Combined-Brain.md
related: changelog-writer, update-announcement-writer, short-video-planner, social-post-calendar, launch-teaser-planner, game-dev-weekly, post-mortem-writer
---

# devlog-writer

A devlog tells people what changed and why it matters; the changelog (`changelog-writer`) is the full developer list, the update post (`update-announcement-writer`) is for players of a live game, and `game-dev-weekly` analyses live numbers. This skill turns real project facts into a short post for a development audience. Posting is the user's action: this skill drafts, it does not publish.

## When to use
Weekly during development, or before a launch when a steady posting rhythm is planned. Not for: marketing copy for the game page, or posts about numbers you do not have.

## Inputs (max 2)
1. The period (default: since the last devlog date or 7 days). 2. The platform (default: Discord post; TikTok/YouTube scripts go to `short-video-planner`).

## Procedure
1. Gather facts, not feelings: the section from `changelog-writer`, `git log --since=<date> --oneline | wc -l`, the latest milestone verdict, any playtest evidence file. If a number is not in a file, it does not go in the post.
2. Pick ONE headline change a viewer can see (a screenshot or a 10-second clip), and at most two smaller ones. Include a before/after if the change is visual; capture is the user's step.
3. Write **Shipped**: what is new, in plain words, with the specific result ("shop now rejects spammed purchases", not "improved security").
4. Write **Numbers**: only measured values with the source and date (tester count, load time, session length from a playtest). An estimate is labelled `estimate`; a missing number is left out, not rounded up. If the game is live, use real analytics; never invent player counts.
5. Write **Went wrong**: one honest setback and what you changed; this builds trust and doubles as input for `post-mortem-writer`.
6. Write **Next**: one concrete next step and when the next entry is due. Do not promise dates you cannot keep.
7. Keep it under about 200 words; check it. Draft only; the user posts, and decides if details are public yet (unannounced systems, sponsor or collaborator names).

## Studio MCP path
None. Screenshots and clips are captured by the user; do not launch Studio or any GUI app.

## Fallback
Plain Markdown draft; no tools needed beyond git.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (post devlogs consistently, about two months before launch, on one chosen platform; one creator reports about 5,000 followers in that window, a single-creator example; conversions from reach are an illustration, not a benchmark; one creator advises keeping devlogs unpublished until release then batch-publishing, a disagreement to decide knowingly), `Roblox/roblox-kb/trailers-and-video-marketing.md`, `Roblox/roblox-kb/influencer-and-creator-marketing.md`, `Roblox/roblox-kb/development-process-and-speed.md` (one creator's devlog ran out of time before finishing the loop: plan the full loop first).

## Output
`docs/devlog/YYYY-MM-DD.md` draft, about 200 words, headings Shipped, Numbers, Went wrong, Next.

## Acceptance checks
- [ ] Executed: `python project-kickoff/scripts/wfdoc.py docs/devlog/<date>.md --kind devlog` prints PASS (needs Shipped, Numbers, Next).
- [ ] Every number in Numbers has a source file or is labelled `estimate`.
- [ ] No unannounced names, ids, keys or private info.
- [ ] Nothing was posted by the skill.

## Pitfalls
Inflated adjectives, invented progress, hiding a setback until it becomes a story. Posting when there is nothing new to show; skipping an entry is better than filler. Treating one creator's follower count as a plan.

## Related
`changelog-writer`, `update-announcement-writer`, `short-video-planner`, `social-post-calendar`, `launch-teaser-planner`, `post-mortem-writer`.
