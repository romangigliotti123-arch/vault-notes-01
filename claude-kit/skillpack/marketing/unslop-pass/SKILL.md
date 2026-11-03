---
name: unslop-pass
description: "Rewrite AI-sounding text (store description, update post, devlog, Discord announcement, ad copy) so it reads like a person who made the game: scan for stock AI patterns, rewrite with concrete facts, self-audit. Use on any player-facing or community text written with AI help before it is posted."
category: marketing
tags: writing, slop, copy, store-text, devlog, announcement, voice, edit, ai-text
kb: Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/updates-live-ops.md, Manager/topic-brief-prompt-engineering.md, Mentor/Combined-Brain.md
related: update-announcement-writer, devlog-writer, title-generator, store-page-audit, game-icon-maker
---

# unslop-pass

Text drafted by a model has a recognisable shape: puffed adjectives, a closing offer to help, dashes everywhere, vague "showcasing growth" tails. Players and the store page notice. This skill is an edit pass, not a generator: it removes the pattern, keeps the meaning and puts in the specific fact only the developer knows. Method source: Theo's walkthrough of an "unslop" skill (MIXED, opinion and self-report; no measurement of effect). Treat the pattern list as a checklist, not proof that text is human.

## When to use
Any text a player, the store or a community will read that an AI drafted or touched. Not for: code comments, internal notes, or text that must be legal/policy wording (`tos-chat-checker`-type text stays as written).

## Inputs (max 2)
1. The text file. 2. Two or three real facts to use (a number, a player quote, what changed); default: ask for one. The pass cannot invent them.

## Procedure
1. Scan: `python unslop-pass/scripts/slopscan.py text.md` lists line, pattern, phrase.
2. For each hit, ask "what is the concrete thing?" and write that: replace "a pivotal update showcasing growth" with "v1.4: trading limit 20 items; 312 players hit the old cap last week".
3. Delete: openers and closers addressed to a chatbot reader, any sentence that could sit unchanged in another game's post, adjectives with no number or example behind them.
4. Add voice sparingly: first person ("we"), one opinion or admitted flaw, mixed sentence length. Do not add fake enthusiasm or invented quotes.
5. Keep what must stay: item names, prices as "SET IN CREATOR HUB" if unknown, dates, platform terms.
6. Self-audit: reread and ask "what here still looks machine-written?" then fix that. Re-run the scan; stop after two rounds.
7. Hand back the text plus a 3-line change note. Posting is the user's action.

## Studio MCP path
None.

## Fallback
Without the script, search the draft by hand for the six pattern groups in the script's header and the em dash character.

## Evidence
`Roblox/roblox-kb/titles-descriptions.md` and `Roblox/roblox-kb/updates-live-ops.md` (store text and updates drive conversion; live-check numbers), creator note `theo-t3gg` "So I tried Matt's skills" (MIXED: unslop skill steps are described, benefit is self-reported; AI-text detectors were inconclusive in his own test). No claim that scanning guarantees human tone.

## Output
Cleaned text plus the change note (hits before and after).

## Acceptance checks
- [ ] Executed: `python unslop-pass/scripts/slopscan.py --selftest` prints `selftest ok`.
- [ ] Executed: `python unslop-pass/scripts/slopscan.py text.md` prints PASS (at most 3 hits) on the final text.
- [ ] Every number or quote in the final text came from the user or a source file.
- [ ] Meaning unchanged: item names, prices placeholders and dates match the draft.

## Pitfalls
Over-correcting into forced slang. Replacing one stock phrase with another. Inventing a player quote to sound human. Treating a clean scan as quality: the text can pass and still say nothing. Using an AI-text detector as a judge (unreliable).

## Related
`update-announcement-writer`, `devlog-writer`, `title-generator`, `store-page-audit`.
