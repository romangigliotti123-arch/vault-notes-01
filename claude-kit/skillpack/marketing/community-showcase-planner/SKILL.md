---
name: community-showcase-planner
description: "Plan how to show off what players make and do as marketing: build clip-friendly moments, collect player creations and clips with permission and credit, run a monthly showcase or contest, and turn the best into posts. Use when the game has an active group or Discord and you want player content to feed promotion."
category: marketing
tags: community, showcase, ugc, fan art, contest, clips, captures, player content, credit, workshop
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/trailers-and-video-marketing.md, Roblox/roblox-kb/events-and-seasonal-content.md
related: social-post-calendar, short-video-planner, codes-campaign-planner, discord-server-setup, roblox-group-setup, event-planner
---

# community-showcase-planner

Vault: allow fan games and characters instead of policing them, run contests and workshops for art, vehicles, weapons and characters (always ask permission and credit or pay), design clippable moments, and integrate the Captures API so players can share highlights. A showcase makes players feel seen and gives you honest promotional material. This skill plans it; the owner runs it.

## When to use
An active group or Discord exists and posts are thin; or before an event that needs player content. Not for: building the server (`discord-server-setup`), paid creator deals (`influencer-outreach-writer`).

## Inputs (max 3)
1. Where players gather (group, Discord, in-game). 2. What players can make or do: builds, outfits, screenshots, runs, clips. 3. Moderation capacity (default: one volunteer moderator).

## Procedure
1. Choose one category to start: screenshots and clips, builds or outfits, fan art, or speedruns. One category done well beats a weekly menu.
2. In-game support: a screenshot or clip prompt at highlight moments (the Captures API exists; live-check its limits), a photo mode or clean camera if cheap, a streamer or clean-HUD mode, and moments designed to be clipped (surprise, chaos, a big reveal).
3. Rules in five lines: all-ages, no real people or third-party brands, you may repost with credit, entrants keep ownership of their art, you will not use their work in paid ads without written consent. Mark "owner to confirm" for anything legal; do not invent terms.
4. Cadence: a monthly showcase post and a themed submission window; reward with recognition first (credit, a group role, a showcase badge, a spot in the loading screen) and small in-game items second. Rewards are one-time and not premium currency. Link to `codes-campaign-planner` for any code-based prize.
5. Moderate before posting: check the content is the entrant's own, safe and in rules; keep a log of permissions with date and link.
6. Publish: two to five winners, credited by their chosen name, with the Details Page URL; ask the community what to show next; thank everyone who entered. Use a Roblox community post with a poll where useful (vault: members are notified).
7. Learn: record submissions, reach of each showcase post, and any increase in group or Discord joins; keep what worked.
8. Never publish a player's work without the recorded permission; the owner posts.

## Studio MCP path
Only for the in-game prompt: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add a client prompt calling the platform's capture feature -> `start_stop_play` -> `get_console_output`. The platform feature itself needs a published place: `untested` until tried.

## Fallback
The plan, rules text and a submission log template; all in-game behaviour is `untested` without Studio.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (source content from the community via contests and workshops, always ask permission and credit or pay; let fans create and treat engaged members as a team extension; keep it positive with rules; perks and small rewards; groups and notifications), `Roblox/roblox-kb/social-features-and-virality.md` (design clippable chaotic moments; Captures and video APIs for sharing; the 361 million screenshot figure is Roblox's, relayed), `Roblox/roblox-kb/trailers-and-video-marketing.md` (design for clippable, creator-friendly moments; keep clips on the details page current), `Roblox/roblox-kb/events-and-seasonal-content.md` (skill-based giveaways keep players engaged 1-2 weeks). API limits and policy change: live-check.

## Output
`marketing/showcase-plan.md`: category, in-game support list, rules text (owner to confirm), cadence, reward ladder, moderation checklist, permission log template, learning table.

## Acceptance checks
- [ ] Every reward is recognition or a one-time non-premium item.
- [ ] Permission and credit rules are written before the first submission; executed: `grep -c -i -E "permission|credit" marketing/showcase-plan.md` is at least 2 (quote the count).
- [ ] A permission log template exists and is used for each post.
- [ ] Rules ban real people, third-party brands and unsafe content.
- [ ] No post or reward is sent by the skill.

## Pitfalls
Using fan art in ads without consent. Weekly contests nobody can moderate. Prizes in premium currency that invite farming. Favouring friends of the team. Letting negativity sit in submissions.

## Related
`social-post-calendar`, `short-video-planner`, `codes-campaign-planner`, `discord-server-setup`, `roblox-group-setup`.
