---
name: experience-name-checker
description: "Check the experience name and description against the publishing rules and the vault's metadata advice: repeated words, decoration, emoji count, keyword stuffing, tags, first-sentence hook, length, social-hangout wording that changes classification, and rename risk. Use before the first publish and before any rename."
category: publish
tags: game name, title, description, metadata, keywords, emoji, rename, discovery, publish, content rules
kb: Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/thumbnails-icons.md
related: title-generator, game-description-writer, experience-settings-configurator, thumbnail-guideline-checker, age-rating-prep, keyword-researcher
---

# experience-name-checker

One job: screen the final name and description before they go live. It does not invent names (`title-generator`) or write the description (`game-description-writer`). It reuses `marketing/title-generator/scripts/title_screen.py` for the name (word count, repeats, caps, emoji, symbols, money lead) and adds the description checks as a short manual list from the live pages. Character limits and rules are `live-check`: the script has no built-in limit, you pass the one you verified.

## When to use
Before first publish, before renaming, before pushing a metadata update. Not for: choosing keywords (`keyword-researcher`), copy quality (`game-description-writer`), images (`thumbnail-guideline-checker`).

## Inputs (max 2)
1. Name and description text. 2. Whether the game is already live (a rename affects findability).

## Procedure
1. Open the live publishing and descriptions pages (Evidence); copy the current limits and metadata rules with the date.
2. Screen the name: `python -I ~/.claude/claude-kit/skillpack/marketing/title-generator/scripts/title_screen.py "<name>" --max-emoji 2 --max-chars <live limit>`. FAIL rows are fixed; WARN rows are decisions to write down.
3. Description checks by hand against the page: first sentence states the genre and content; the first ~160 characters work as a hook (the note says that is what search snippets and mobile show first); keywords appear naturally, no keyword lists; no tags or hashtags; controls taught in-game, not listed; FAQs short; update notes short; credits and changelog behind a link.
4. Length: count the description characters and compare with the live limit (the note says 1000); put the number in the settings sheet.
5. Classification wording: a title or description with social-hangout references makes the maturity system treat the game as a hangout; keep it accurate and align it with the questionnaire (`age-rating-prep`).
6. Honesty: nothing promises rewards the game does not give; no references to other brands you do not own (`copyright-checker`).
7. If renaming a live game: renaming often reduces findability under the old name, so rename rarely, never during a push.
8. Write `release/name.md`: final name, description, script output, checklist results, page date.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Server, Edit) to read `game.Name`; the Creator Hub name and description are web fields the owner edits. No MCP tool sets them.

## Fallback
Fully offline: the script plus the checklist. Moderation of the text happens after submission and is `untested` until then.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production publishing publish-games-and-places.md` (keep the name consistent; no repeated words like 'OBBY OBBY OBBY'; at most one or two emojis; genre in the first sentence; natural keywords; keyword lists and irrelevant terms may demote), `... Docs production publishing descriptions.md` (160-character hook; no hashtags; no control lists; 1000-character limit), `... Docs production promotion content-maturity.md` (hangout wording classifies a game). Pack: `Roblox/roblox-kb/titles-descriptions.md`, `Roblox/roblox-kb/discovery-algorithm.md`.

## Output
`release/name.md`.

## Acceptance checks
- [ ] `title_screen.py` ran on the final name (quote the PASS/WARN/FAIL summary).
- [ ] Every item in the description checklist is answered.
- [ ] The description length is a counted number against the live limit.
- [ ] The page date is recorded.
- [ ] `title_screen.py --selftest` prints `selftest ok`.

## Pitfalls
Stuffing the description with search terms. A name that promises free Robux. Treating the script's WARN as optional without writing why. Renaming the week before an event.

## Related
`title-generator`, `game-description-writer`, `experience-settings-configurator`, `thumbnail-guideline-checker`, `age-rating-prep`, `keyword-researcher`.
