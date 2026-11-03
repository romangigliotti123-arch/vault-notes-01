---
name: toxicity-response-playbook
description: "A calm step-by-step playbook for harassment, drama, pile-ons and toxic behaviour in a game community: triage by severity, what staff do in the first hour, what is reported to Roblox or Discord instead of handled in-house, how to talk to the community without naming and shaming, and how to protect young members and volunteers. Use when something ugly is happening or before you expect it."
category: community
tags: toxicity, harassment, drama, incident, moderation, safety, escalation, minors, community, response
kb: Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/social-features-and-virality.md
related: moderation-rules-writer, discord-server-setup, support-macro-writer, chat-filter-tester, ambassador-program-planner, ugc-moderation-checker, group-management-planner
---

# toxicity-response-playbook

Creators who run communities say: set clear rules beforehand, avoid drama, remove hateful negativity, ignore or block trolls with no actionable criticism, respond publicly only for broken features, and keep your own conduct professional. This turns that into steps staff can follow under stress. It is a playbook for the owner and staff; it does not contact anyone, ban anyone or post anything.

## When to use
A heated thread, a harassment report, a pile-on against a member or the dev, a raid, or before launch to prepare. Not for: writing the rules in the first place (`moderation-rules-writer`), the in-game chat filter checks (`chat-filter-tester`), or a content crisis from a bug (`hotfix-playbook`).

## Inputs (max 2)
1. The situation in two sentences with handles removed, or "no incident, preparing" (default). 2. Who is on staff and who is an adult (default: dev + mods).

## Procedure
1. Triage in five minutes. RED: threats, doxxing, self-harm talk, sexual content with or about a minor, grooming signs. These are never handled only in-house: preserve evidence (screenshots, message links), remove the content from view, report through the platform's safety channel (Roblox and Discord reporting; live-check the current routes, including emergency contacts for threats), and tell a trusted adult if the person at risk is a minor. AMBER: sustained harassment, hate, raids. GREEN: heated argument, trolling.
2. Contain: slow mode, lock the thread or channel, pause joins/raid mode if a raid, remove violating messages. Keep the first public message short and neutral ("we are looking into this; please report, do not engage").
3. Decide with the ladder from `moderation-rules-writer`: warn, timeout, kick or ban, by two staff for bans, with evidence logged in the private staff channel. Apply the rules equally to friends of staff and to popular members.
4. Do not name and shame: never post a player's handle with an accusation, never quote their message publicly, never call out a minor. Tell the target privately in a ticket or the thread that action was taken. Check every public post with `python welcome-message-writer/scripts/text_lint.py incident-post.txt` (it flags handle-plus-accusation patterns); fix FAILs.
5. Support: for the target, offer a mute/block and a named adult contact; for volunteers, rotate duty and allow a break; the developer does not argue in public.
6. After 24-48 hours: a short transparent note (what rule applied, what changed), a staff debrief (what was slow, which rule was unclear), and update the rules or filters. Look for repeats and escalate repeat offenders per the ladder.
7. Prepare in advance: an on-call list, a pre-written RED checklist, and a template set (`support-macro-writer`).

## Studio MCP path
Only for in-game aspects: `list_roblox_studios` -> `get_studio_state` -> `script_grep` for the report, mute and block code (use platform TextChannels and report features rather than custom chat); verify the filter with `chat-filter-tester`.

## Fallback
Pure process. Platform reports and bans are the owner's or staff's actions; the playbook acts on nothing.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (keep the community positive, set rules, handle trolls; remove hateful negativity; scale moderation with written guidelines, defined ban lengths and separate game and Discord mods; keep your own public conduct professional; respond publicly only for broken features). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (use TextChannels so messages stay reportable; escalating enforcement; groups must be moderated; DataStore blocklist for banned users). Platform policy specifics are live-check.

## Output
`community/incident-playbook.md`: the severity table, first-hour checklist, message templates, roles on call, debrief template. Under 90 lines.

## Acceptance checks
- [ ] RED cases route to platform safety reporting with evidence kept and are not handled only in-house.
- [ ] No template names a player or quotes their words in public; `text_lint.py` exits 0 on public posts.
- [ ] Bans need two staff and a logged reason.
- [ ] A support path exists for the target and for staff.
- [ ] A debrief and a rule/filter update step exist.

## Pitfalls
Arguing with trolls in public. Naming and shaming. Handling a threat quietly. Staff acting alone on a friend's case. A permanent ban without evidence. Letting volunteers burn out.

## Related
`moderation-rules-writer`, `support-macro-writer`, `chat-filter-tester`, `ambassador-program-planner`, `group-management-planner`.
