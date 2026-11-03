---
name: moderation-rules-writer
description: "Write short, positive community rules and an enforcement ladder (warn, timeout, kick, ban) with who decides, what evidence is kept, how to appeal and what goes to the platform instead of being handled in-house; lint the ladder with a script. Use before a Discord opens, when a group wall gets noisy, or after the first real incident."
category: community
tags: moderation, rules, enforcement, ladder, discord, group, appeal, escalation, community-standards, age
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/social-features-and-virality.md
related: discord-server-setup, toxicity-response-playbook, welcome-message-writer, group-management-planner, ugc-moderation-checker, chat-filter-tester, support-macro-writer
---

# moderation-rules-writer

Creators who scale a community say the same thing: write the rules before you need them, separate game moderators from Discord moderators, define ban lengths, and keep the damaging permissions with the creator. This writes the rules text and the ladder behind it. It does not moderate anything, post as the owner or decide a real case.

## When to use
Before a Discord or group wall opens, when volunteers start making inconsistent calls, or right after a first ugly incident. Not for: the incident itself (`toxicity-response-playbook`), in-game chat filtering code (`chat-filter-tester`), or UGC upload review (`ugc-moderation-checker`).

## Inputs (max 2)
1. Where the rules apply (Discord, Roblox group wall, in-game, all) and who the audience is (default: mostly under 18, so the strictest sensible tone). 2. Who enforces (default: dev + 1-2 trusted mods + helpers who can only warn).

## Procedure
1. Start from the platform: the Roblox Community Standards and Terms of Use, and Discord's own rules and minimum age, always apply above yours. Tell the owner to live-check both before publishing (they change); the rules link to them rather than copy them.
2. Write 6-8 rules, positive wording first ("be kind to everyone"), each with one concrete example: respect and no harassment or hate; no sharing or selling accounts; no exploits or exploit tools; no personal information of anyone (including your own); no spam or self-promo; keep content age-appropriate; follow staff instructions; report, do not retaliate. State the age requirement. Stop when a new member can read them in under a minute.
3. Build the ladder as a CSV `moderation/ladder.csv` with columns `offence,first,repeat,decider,appeal,evidence,report_platform`. Ordinary offences start gentle (warn, then timeout, then ban). Severe ones (threats, doxxing, grooming or any sexual contact with a minor, account selling, hate) may skip steps and are reported to the platform's safety channel, never handled only in-house.
4. Decide authority: helpers warn only; mods time out, kick and ban with a logged reason; the dev handles appeals and permanent bans. Volunteers never get admin or owner rights.
5. Define evidence and appeals: screenshot or log link kept in a private staff channel; one appeal route (a form or ticket, not a DM with a minor), answered within a stated time, by someone other than the original moderator.
6. Run `python scripts/ladder_check.py moderation/ladder.csv`; fix every FAIL and rerun until exit 0 (quote the output).
7. Lint the player-facing rules with `python welcome-message-writer/scripts/text_lint.py moderation/rules.txt --require-age`.
8. Add a change rule: rule changes are announced with the reason (transparency was the creators' top trust tip) and take effect after the post.

## Studio MCP path
Only for in-game moderation hooks: `list_roblox_studios` -> `get_studio_state` -> `script_grep` for `Chat`, `Ban`, `Kick` to find where punishments live; recommend a DataStore blocklist so banned users cannot simply rejoin (vault). Edits go through the user's approval.

## Fallback
Everything is text and one CSV. Applying rules in Discord or on the group is the owner's action; nothing is posted or enforced by this skill.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (clear rules and trolls handled in advance; scale Discord moderation with written guidelines, separate game and Discord mods, defined ban lengths; keep damaging permissions with the creator). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (repeated violations get escalating enforcement; groups must be moderated actively; DataStore blocklist so banned users cannot rejoin). Platform policy details are not copied here: live-check them.

## Output
`moderation/rules.txt` (6-8 rules, age line, appeal line), `moderation/ladder.csv`, and a half-page staff guide (who decides what, evidence, appeal, escalation list). Under about 100 lines.

## Acceptance checks
- [ ] `ladder_check.py` exit 0 on the CSV, output quoted (no ordinary first-offence ban, helpers cannot ban, severe offences marked for platform reporting).
- [ ] Rules include the age requirement and the exploit and account-sale bans.
- [ ] `text_lint.py` exit 0 with `--require-age` on the rules text.
- [ ] An appeal route and an evidence habit exist and name a role, not a person's private account.
- [ ] No rule asks anyone for personal information or invites private contact with minors.

## Pitfalls
Thirty rules nobody reads. Permanent bans for first small offences. One moderator who is also the accused's friend deciding the appeal. Volunteers with admin. Handling threats or grooming reports quietly instead of reporting. Copying platform policy text that then goes stale.

## Related
`discord-server-setup`, `toxicity-response-playbook`, `welcome-message-writer`, `group-management-planner`, `chat-filter-tester`.
