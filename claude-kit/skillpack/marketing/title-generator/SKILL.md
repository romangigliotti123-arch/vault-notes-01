---
name: title-generator
description: "Generate 15-20 candidate Roblox game titles from the core fantasy, screen them with the executable title_screen.py check (literal, short, no repeats, emoji and money rules), and shortlist 3 with a name-check and test plan. Use when naming a game, renaming for search, or choosing between names; the page body is game-description-writer."
category: marketing
tags: title, name, naming, literal, verb noun, search, keyword, reading level, rename, name check
kb: Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: game-description-writer, keyword-researcher, tagline-writer, thumbnail-maker, ctr-ab-test-planner, one-sentence-pitch, experience-name-checker
---

# title-generator

The title gives the thumbnail its context; together they state the core fantasy (vault: titles-descriptions). This skill produces many candidates, throws most away with a script, and leaves three to test. It writes only the title; description and keywords are `game-description-writer`, search terms are `keyword-researcher`.

## When to use
A new game with no name, a name that tests badly, or a rename aimed at search. Not for: ad taglines (`tagline-writer`), the description, group names (`roblox-group-setup`).

## Inputs (max 3)
1. One-sentence pitch and genre (default: `GAME.md`). 2. Target age and audience (default: young, mobile-first). 3. Names already considered or rejected.

## Procedure
1. Pull the rules: `python -I .rbx/claude-kit/tools/kbq.py section titles-descriptions rules --max-chars 4000`. Live-check the current title length limit and naming rules on Creator Docs; write the limit and date down.
2. Write 15-20 candidates in four families (vault patterns, all indie or creator-reported unless marked): verb + noun naming the action ("Steal an Egg"), literal fantasy ("Grow a Garden"), fantasy with implied challenge or a number plus a setting ("99 Nights in the Forest"), genre-keyword names ("... Simulator", "... Tycoon") when true. Plain words beat clever wordplay.
3. Screen: put the candidates in `titles.txt` and run `python -I .rbx/claude-kit/skillpack/marketing/title-generator/scripts/title_screen.py --file titles.txt --max-chars <limit>`. Delete FAIL rows; read WARN rows. The script checks word count, repeats, caps, emoji count, symbols, reward-led titles and long words; it does not judge meaning.
4. Human screens on the survivors: half-second test (a stranger understands it), one-sentence test (they can guess the game), third-grade reading level and easy to type on a phone, true to the gameplay (a title that promises more than the game delivers raises bounce).
5. Search: ask `keyword-researcher` whether the genre keyword helps and whether the name is findable; the vault says players search by typed name and that renaming for a searched keyword helped one game.
6. Safety: not a look-alike of a famous game, no brand or character names, no real people; run the official name check before launch and again around big updates (vault: Roblox guidance late 2026). Keep the final name stable; frequent renaming hurts findability.
7. Shortlist 3 and write the test plan: name the one variable (title wording), pair with the same thumbnail, then `ctr-ab-test-planner`. One freshness tag such as [NEW] is a later, temporary option, not part of the name.

## Studio MCP path
Not needed. If a place is connected, `get_studio_state` can read the current experience name to avoid a clash; nothing is changed.

## Fallback
Same. The owner sets the name in Creator Hub.

## Evidence
`Roblox/roblox-kb/titles-descriptions.md` (literal and specific; verb + noun; clear fantasy with implied challenge; about third-grade reading; genre keywords; no bloat or repeated words; limit emoji (official advice moved from avoid to one or two); do not lead with money rewards; keep the name consistent; name checks protect against copycats), `Roblox/roblox-kb/thumbnails-icons.md` (title and thumbnail as a pair), `Roblox/roblox-kb/discovery-algorithm.md` (mismatched metadata raises first-play bounce), `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`. Limits and policy move: live-check.

## Output
`marketing/title-shortlist.md`: live limits with date; the 15-20 candidates with PASS/WARN/FAIL; the 3 finalists (reason, risk, keyword fit); the test plan. Raw `titles.txt` kept beside it.

## Acceptance checks
- [ ] `title_screen.py` was run and its output is quoted; every finalist is PASS.
- [ ] Each finalist passed the half-second and one-sentence tests, written yes/no.
- [ ] The length limit is cited with a source and date.
- [ ] No finalist contains a third-party brand, character or real name.
- [ ] A one-variable test plan exists.

## Pitfalls
Clever names that say nothing. Stuffing keywords or repeating words. Naming a reward in the title. Renaming repeatedly. Choosing in a vacuum: ask 3-5 players from the target age which name they would click.

## Related
`game-description-writer`, `keyword-researcher`, `tagline-writer`, `thumbnail-maker`, `ctr-ab-test-planner`.
