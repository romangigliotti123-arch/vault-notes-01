---
name: discord-server-setup
description: "Design a Discord community for a Roblox game: channel structure, roles, rules, welcome and verification, bots, a feedback loop that reaches the developer, an announcement rhythm tied to updates, and the first 30 days of activity. Use about a month before launch or when the game has players but no home for them."
category: community
tags: discord, community, channels, roles, rules, moderation, announcements, feedback, server, onboarding
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: moderation-rules-writer, welcome-message-writer, feedback-channel-planner, community-event-planner, bug-intake-builder, update-announcement-writer, event-planner, tester-recruitment-planner
---

# discord-server-setup

Roblox says initial users are very hard to attract without community support; creators funnel every game into one Discord so each release starts bigger. A Discord pays off only if people have a reason to stay and the developer reads it. This designs it; the owner creates it (you do not log in to or post as the user).

## When to use
About a month before launch (vault: start roughly a month before release, not much earlier), or when players ask "is there a Discord". Not for: moderation of an existing crisis (`toxicity-response-playbook`), or the Roblox group page (`roblox-group-setup`).

## Inputs (max 3)
1. Game name, genre, audience age (default: young; see safety below). 2. Who will run it (default: solo dev + 1-2 volunteer mods). 3. Launch date (default: unknown).

## Procedure
1. Safety first for young audiences: Discord has its own minimum age (13 in most regions; general knowledge, not in the vault: confirm Discord's current terms) and many Roblox players are younger; state the age rule in the rules, never request personal information, keep the in-game community link accurate, and prefer an in-game "Discord" button/code reward only where Roblox policies allow linking to off-platform sites (check `age-ratings-moderation-and-tos` and current Roblox rules live). Do not DM minors; moderation by adults only.
2. Channels (start small, add on demand): `#welcome` / `#rules`, `#announcements` (read-only), `#updates` (patch notes), `#general`, `#game-chat`, `#feedback`, `#suggestions`, `#bug-reports` (form or template), `#showcase` (clips and screenshots), `#trading` (only if the game has trading), `#support`, `#voice` (optional). 8-10 channels are enough for the first month.
3. Roles: Dev, Mod, Helper (trusted volunteers), Tester (playtest invites), Verified/Player (granted after accepting rules), and cosmetic roles for milestones (first 100 members, beta tester). Least privilege: only Dev/Mod can post in announcements and manage messages; bots get minimal permissions.
4. Rules (short, positive, enforced): respect, no hate or harassment, no leaking or selling accounts, no exploit sharing, English-only or per-language channels, no self-promo, an escalation ladder (warn, timeout, ban) and who decides (`moderation-rules-writer`). Be transparent about changes and money.
5. Onboarding: a welcome message that says what the server is for, where to find the game link, the three channels to read, how to report a bug. Verification via reaction/button; anti-raid defaults (verification level, slow mode in `#general`).
6. Bots (minimal): one moderation bot with logging and auto-mod filters, one for roles/reaction roles, optional ticket bot for support; release-note webhooks from your pipeline. Fewer is safer.
7. Feedback loop: `#feedback` is read daily by one named person; weekly summary to the dev (`feedback-synthesizer`); a monthly "you said, we did" post. Use polls to gauge wants but keep final design control. Triage bug reports with a template (what, steps, device, screenshot) into a tracker (`bug-intake-builder`).
8. Rhythm: tease updates early with images and hints, announce release time (a fixed time makes people arrive together), post-update Q&A, a regular themed event day, contests/workshops for art and ideas, be visibly present as the developer.
9. First 30 days: day 1 seed 10-20 real people (playtesters, friends of the game); week 1 daily dev posts; week 2 first event; week 4 first "you said, we did". Measure: joiners per day, active members, bug reports per week, share of players who join.
10. Hand the owner a checklist to create the server (you do not create it): settings, channel list, roles, rules text, welcome text, bot invites to approve, and the invite link to put on the game page and group.

## Studio MCP path
Not needed. Optional: `script_grep` to find where an in-game link or code reward would go.

## Fallback
Same; everything is text for the owner to apply. Discord actions are the owner's; nothing is posted as the user.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (community before launch about a month ahead; funnel to one Discord; pick one platform and do it well; right channel per feedback type; be visibly active; tease and announce; themed event day; contests; clear rules and trolls; transparency), `Roblox/roblox-kb/social-features-and-virality.md`, `Roblox/roblox-kb/playtesting-and-feedback.md` (weight feedback by source; keep control), `Roblox/roblox-kb/updates-live-ops.md`, `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`.

## Output
`community/discord-plan.md`: channel table (name, purpose, who can post), roles and permissions, rules text, welcome message text, bot list with permissions, feedback-loop owner and cadence, 30-day calendar, creation checklist, metrics.

## Acceptance checks
- [ ] Rules include age requirement, exploit/account-sale ban and an escalation ladder.
- [ ] Only staff can post in announcements; bot permissions are least-privilege.
- [ ] A named person owns feedback reading and a cadence exists.
- [ ] The invite is placed on approved surfaces only (no policy-breaking in-game links).
- [ ] No personal data collection or DM-minors steps anywhere in the plan.
- [ ] The plan is small enough to run (<= 10 channels at launch).

## Pitfalls
Fifty empty channels. No one reading feedback. Letting volunteers moderate alone with admin rights. Leaking update content early by accident. Linking off-platform in ways Roblox forbids. Treating the loudest members as the player base.

## Related
`moderation-rules-writer`, `welcome-message-writer`, `feedback-channel-planner`, `community-event-planner`, `update-announcement-writer`, `event-planner`.
