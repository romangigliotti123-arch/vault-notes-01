---
name: welcome-message-writer
description: "Write the welcome flow for new community members (Discord welcome post, verification text, group welcome, first-visit in-game message): what the place is for, where the game link is, three channels to read, how to report a bug, the age rule. Lints the text for personal-data requests, DM invites and scam wording. Use when a server or group is about to open or onboarding is leaking members."
category: community
tags: welcome, onboarding, discord, verification, newcomers, message, tone, safety, age
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/social-features-and-virality.md
related: discord-server-setup, moderation-rules-writer, faq-writer, bug-intake-builder, support-macro-writer, community-event-planner
---

# welcome-message-writer

A new member decides in seconds whether a community is for them. The welcome flow must say what this place is, where the game is, what to read first and how to get help, in plain friendly words, and it must be safe for a young audience. This writes the text; the owner posts it.

## When to use
Opening a Discord or group, or when members join and never speak. Not for: the channel structure (`discord-server-setup`), the rules content (`moderation-rules-writer`), or recurring announcements (`update-announcement-writer`).

## Inputs (max 2)
1. Game name, link placeholder and genre vibe (default: friendly, short sentences). 2. Platform surfaces to cover (default: Discord welcome + verification + group description).

## Procedure
1. List the five jobs the message must do, in order: what this is, play now (link placeholder `GAME_LINK`), read these three channels, how to report a bug or get help, the one rule that matters most (be kind, plus the age requirement).
2. Draft the Discord `#welcome` post at 60-100 words, one emoji at most per line, no walls of text. Add a second line for people who want to help (testers role, feedback channel).
3. Draft the verification text: one sentence that they agree to the rules and the age requirement, then a button or reaction. Never ask for age, name or any personal detail to verify.
4. Draft the group description (3-4 lines) and a first-visit in-game message of under 20 words that points to the group or Discord only where Roblox policy allows (live-check the off-platform link rules; social links on game pages have their own limits in the vault).
5. Write staff greeting rules: greet in public channels, never DM newcomers, no mass-pings, answer the same questions from `faq-writer` text.
6. Lint every text: `python scripts/text_lint.py welcome.txt --require-age`. Fix every FAIL, read every WARN, rerun to exit 0.
7. Read it as a ten-year-old and as a skeptical parent: is anything confusing, pushy or unsafe? Stop when neither would object.

## Studio MCP path
Only for the in-game line: `list_roblox_studios` -> `get_studio_state` -> `script_grep` for the existing welcome or tips text, then `multi_edit` after the user approves the copy; verify with `start_stop_play` and `get_console_output`.

## Fallback
The texts are plain files the owner pastes. Posting is the owner's action.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (link the Discord in the game description; clear rules; be visibly active; plan Discord structure and admin). `Roblox/roblox-kb/social-features-and-virality.md` (friends found early retain better: onboarding should be social, not isolated). `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (age-appropriate communities; filter all user text). Discord's minimum age is general knowledge, not in the vault: live-check it.

## Output
`community/welcome.txt` with sections: Discord welcome, verification text, group description, in-game line, staff greeting rules, and the lint output. Under 60 lines.

## Acceptance checks
- [ ] `text_lint.py welcome.txt --require-age` exits 0; the output is quoted.
- [ ] The five jobs appear in order and the game link is a placeholder until the owner supplies it.
- [ ] No step collects personal information or invites private messages.
- [ ] The in-game line is under 20 words and does not promise rewards for joining off-platform.
- [ ] Nothing was posted by the skill.

## Pitfalls
A 400-word wall. Rules pasted whole into the welcome. Asking new members to introduce themselves with age or location. Pinging everyone. Staff DMing newcomers. A reward for joining the Discord that breaks platform policy.

## Related
`discord-server-setup`, `moderation-rules-writer`, `faq-writer`, `bug-intake-builder`, `support-macro-writer`.
