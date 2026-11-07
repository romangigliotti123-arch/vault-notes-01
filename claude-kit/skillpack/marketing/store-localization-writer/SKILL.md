---
name: store-localization-writer
description: "Prepare a Roblox game's store text for other languages: pick languages from where players actually are, produce a clean source-string table, brief for translators (context, length, tone), localise name/description/thumbnail text, and verify the returned CSV with loc_check.py. Use when expanding to new markets or when auto-translation reads badly."
category: marketing
tags: localization, localisation, translation, store page, languages, csv, auto-translate, thumbnail text, international
kb: Roblox/roblox-kb/localization-and-international.md, Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/analytics-metrics.md
related: game-description-writer, store-page-audit, title-generator, rbx-kb, thumbnail-maker, discovery-signal-reader
---

# store-localization-writer

Vault: the US is under 5% of the world population and English is spoken by under 20%, so non-English markets matter, but bad translations hurt reputation and players leave. Translate the countries your players come from first, prefer human translators, treat auto-translation as a stopgap you audit, and keep the game name unchanged. This skill is the store-page layer; in-game text localisation is the platform's localization tooling.

## When to use
Adding languages to the page, or fixing machine-translated store text. Not for: translating the whole game UI (use the localization tables plus `ui` category skills), ad copy.

## Inputs (max 3)
1. Top player countries from analytics (default: ask the owner to read Creator Hub demographics). 2. Source text: name, description, thumbnail text, pass and product names. 3. Translator route (default: a bilingual human; auto-translation only as a labelled stopgap).

## Procedure
1. Choose languages by player geography first, not by size of language (vault); add 1-3 at a time. Test a new country with paid user acquisition before always-on creator campaigns if the market is new to you (vault, single indie source).
2. Live-check the current localization features and limits on Creator Docs: number of localised thumbnails per language, how manual entries interact with auto-translation, supported languages, CSV limits. Record them with the date. The vault lists examples from 2026-10 (10 localised thumbnails per language, CSV limits of 10,000 entries and 2 MB), which must be re-confirmed.
3. Source table: write `loc/source.csv` with columns `key,source,context` (context says where the string appears, which disambiguates identical words). Keep placeholders such as `{Player_Name}` exactly as written. Do not bake text into images where avoidable; text on thumbnails is localised as separate images.
4. Brief for translators: audience age, tone (friendly, short), terms that must stay in English (game name, brand terms), genre words that have no equivalent (agree a workaround), length limits (Spanish is about 30% longer, German more; design with room).
5. Translate (human) or stopgap with auto-translation, then audit: mistranslations, untranslated leaks, bloated tables. Auto-translation fills only blanks and manual entries win (official docs per the vault), but a 2026 report says it can override; verify in game.
6. Verify the returned file: `python -I .rbx/claude-kit/skillpack/marketing/store-localization-writer/scripts/loc_check.py loc/source_es.csv --lang es --name "<Game Name>" --limit title=<live limit> --limit description=<live limit>`. Fix every FAIL; read each WARN with the translator.
7. Locale test: set the play language in Studio's player emulator or the client and look at the real page text and the first screen.
8. Measure per region later (conversion and ARPU differ a lot by market, vault anecdote); hand to `discovery-signal-reader` after two weeks.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state`; for in-game strings `execute_luau` (Edit) can read an existing localization table; the store page itself is edited by the owner in Creator Hub.

## Fallback
CSV files and the translator brief; locale tests are `untested` without a client.

## Evidence
`Roblox/roblox-kb/localization-and-international.md` (prioritise by player geography; human over machine; audit auto-translation; manual entries win per docs, conflicting 2026 report; keep game name unchanged and localise descriptions and thumbnail text; up to 10 localised thumbnails per language; Spanish about 30% longer; placeholders identical across locales; per-region conversion varies), `Roblox/roblox-kb/titles-descriptions.md` (localise metadata), `Roblox/roblox-kb/thumbnails-icons.md`, `Roblox/roblox-kb/analytics-metrics.md`. Limits, languages and tool behaviour change: live-check.

## Output
`loc/source.csv`, `loc/brief.md`, one `loc/source_<lang>.csv` per language, and `loc/report.md` with the loc_check output.

## Acceptance checks
- [ ] `loc_check.py` exited 0 for every language (last line quoted).
- [ ] The game name is unchanged in every language (the `name` check passes).
- [ ] Limits and features cite a source and date from this run.
- [ ] A human or named reviewer saw each language, or the language is marked `machine only`.
- [ ] Languages chosen from analytics, not guesses.

## Pitfalls
Translating the game name. Literal translation of genre terms. Text locked inside images. Trusting auto-translation without a second check. Forgetting the extra length in tight buttons.

## Related
`game-description-writer`, `store-page-audit`, `title-generator`, `thumbnail-maker`, `discovery-signal-reader`.
