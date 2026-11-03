---
name: faq-writer
description: "Build the game FAQ from real player questions: cluster the questions asked in Discord, comments and tickets, rank them by how often they come up, answer the top ones in players' words with links, and keep it fresh. Use when the same questions repeat, before a launch, or after a big update."
category: community
tags: faq, support, questions, clustering, help, discord, onboarding, content
kb: Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/social-features-and-virality.md
related: welcome-message-writer, support-macro-writer, feedback-synthesizer, bug-intake-builder, community-poll-writer, discord-server-setup
---

# faq-writer

A good FAQ answers what players actually ask, not what the developer thinks they will. The vault's advice is to talk to players, watch for patterns rather than single messages, and ask why behind a request. This turns a pile of real questions into a ranked FAQ.

## When to use
When the same question has been answered three times, ahead of a launch (use playtester questions), or after an update that changes how something works. Not for: bug reports (`bug-intake-builder`), reply scripts for support cases (`support-macro-writer`), or feature requests (`feedback-synthesizer`).

## Inputs (max 2)
1. A text file of questions, one per line, with names and handles removed (default: ask the owner to paste 30-100 from Discord, comments and playtest sessions). 2. Where the FAQ will live (default: Discord `#faq` plus the game description).

## Procedure
1. Clean the questions: delete handles, names and anything personal; keep the wording players used. Stop at 30 or more lines; fewer is a sample, say so.
2. Cluster and rank: `python scripts/faq_cluster.py questions.txt --top 15`. Read the clusters; merge or split any that the word-overlap got wrong.
3. For each top cluster, write the heading as a player would ask it, then a 1-3 sentence answer, then one link or step. Answer the need behind the question, not just the words ("where do I get pets" may really be "how do I progress").
4. Order by frequency, not by what is easiest to write. Cap the FAQ at about 12 entries; below that, link to a wiki or channel.
5. Mark anything time-sensitive (event codes, current prices) with a "last checked" date and an owner; do not hardcode numbers that change with each update.
6. Check each answer against the real game: open it, or ask the dev to confirm. Wrong help is worse than none.
7. Lint the FAQ text: `python welcome-message-writer/scripts/text_lint.py faq.txt`; fix every FAIL.
8. Set the refresh rule: re-cluster every update and monthly; promote any new cluster of 3 or more.

## Studio MCP path
Optional, to verify answers: `list_roblox_studios` -> `get_studio_state` -> `search_game_tree` or `script_grep` to confirm names, locations or values quoted in an answer. Do not invent values; read them.

## Fallback
Pure text. If no questions exist yet, run a short playtest and collect the questions players ask (`tester-recruitment-planner`); do not make up questions.

## Evidence
`Roblox/roblox-kb/community-and-discord.md` (talk to players directly; monitor channels for patterns, not single messages; probe the reasoning behind suggestions). `Roblox/roblox-kb/playtesting-and-feedback.md` (weight feedback by source). `Roblox/roblox-kb/social-features-and-virality.md` (onboarding should reduce confusion in the first days).

## Output
`community/faq.md`: up to 12 entries (question, answer, link, last-checked date), a "not answered yet" list of rare questions, and the cluster output that justified the order. Under 100 lines.

## Acceptance checks
- [ ] `faq_cluster.py` output is quoted and the FAQ order follows its counts.
- [ ] Every answer was verified against the game or marked unverified.
- [ ] Time-sensitive entries have a date and an owner.
- [ ] `text_lint.py` exits 0 on the FAQ text.
- [ ] No handles, names or personal details remain in the source questions or the FAQ.

## Pitfalls
Writing the FAQ from the developer's head. A FAQ that mirrors the patch notes. Answers that quote prices or odds that change. Leaving the FAQ untouched for months. Pasting player names next to their questions.

## Related
`welcome-message-writer`, `support-macro-writer`, `feedback-synthesizer`, `bug-intake-builder`.
