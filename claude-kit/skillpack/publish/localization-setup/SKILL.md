---
name: localization-setup
description: "Set up localization for a game: source language, supported languages, automatic translation, the translation table, AutoLocalize opt-outs, translator collaborators, and a code scan for hard-coded strings and concatenation that break translation. Use when you want international players or before store-page translation."
category: publish
tags: localization, translation, languages, AutoLocalize, translation table, translators, automatic translation, international, settings
kb: Roblox/roblox-kb/localization-and-international.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/discovery-algorithm.md
related: localization-ready-checker, store-localization-writer, regional-availability-checker, accessibility-checker, experience-settings-configurator, publish-readiness-gate
---

# localization-setup

One job: the settings and code groundwork for translation, in the right order. Settings (source language, supported languages, automatic translation) are Creator Hub actions for the owner; the code side is checked by `scripts/loc_scan.py` (hard-coded text, concatenation, AutoLocalize opt-outs, existing translator calls). Translated strings are then checked with `marketing/store-localization-writer/scripts/loc_check.py` (placeholders, game name, length ratio). UI layout for longer text is `localization-ready-checker`. Feature names and options are `live-check`: the Creator Docs localization page changes.

## When to use
Before enabling languages, before commissioning translations, and when adding UI text late. Not for: store-page copy (`store-localization-writer`), layout expansion (`localization-ready-checker`), regional restrictions (`regional-availability-checker`).

## Inputs (max 2)
1. Target languages (default: let automatic translation show coverage first, then pick). 2. Project folder (default: current).

## Procedure
1. Open the live localization page (Evidence); copy the current steps with the date.
2. Set the source language first (one at a time; it defaults to the account language), then add supported languages. Enable automatic translation: it needs no setup beyond choosing languages and shows how much text is covered.
3. Run `python -I .rbx/claude-kit/skillpack/publish/localization-setup/scripts/loc_scan.py <project>`. HARD_TEXT and CONCAT leads are strings the table will not see or cannot reorder; move runtime text through a translator and a named-placeholder format string instead of `"Coins: " .. n`.
4. Set `AutoLocalize = false` only on text that must not change (NPC names, street signs, the game name); the AUTOLOCALIZE_OFF list should be short and each entry justified.
5. Remember the rule from the page: manual translations always display, automatic ones only fill missing strings, so review manual entries carefully, especially entries left empty on purpose.
6. Translators: add trusted Roblox users as translators to review or supply strings; download the monthly translation analytics to track coverage.
7. Check each delivered language file: `python -I .rbx/claude-kit/skillpack/marketing/store-localization-writer/scripts/loc_check.py strings.csv --lang <code> --name "<Game Name>"`. FAIL rows (missing, placeholder mismatch, name changed) go back to the translator.
8. Write `release/localization.md`: languages, scan output, opt-outs with reasons, translator list, loc_check outputs, page date. UI overflow checks are handed to `localization-ready-checker`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`.Text =`) -> `execute_luau` (Server, Edit) to list GuiBase2d with `AutoLocalize == false` -> `start_stop_play` -> `get_console_output`. Studio's localization tools (text capture, table editing) are UI features; the translation table lives in Creator Hub.

## Fallback
Run both scripts on the Rojo folder and a CSV. Text that exists only as instances in a `.rbxl` is not seen by the scan: capture it with Studio's localization tools. Live translation output is `untested` until viewed with a player set to that language.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production localization.md` (automatic translation on by default, source language first, AutoLocalize off for names and signs, manual beats automatic, translators, monthly analytics, translation table in code). Pack: `Roblox/roblox-kb/localization-and-international.md`, `Roblox/roblox-kb/ui-ux-design.md`.

## Output
`release/localization.md`.

## Acceptance checks
- [ ] `loc_scan.py` output attached; every HARD_TEXT/CONCAT lead is fixed or accepted with a reason.
- [ ] Every `AutoLocalize = false` has a written reason.
- [ ] `loc_check.py` ran on each delivered language (quote the summary line).
- [ ] The live page date is recorded.
- [ ] `loc_scan.py --selftest` prints `selftest ok`.

## Pitfalls
Concatenating text so word order cannot change. Translating the game name. Leaving empty manual entries that suppress automatic translation. Judging quality of an automatic translation without a native reader. Text drawn into images that no table can reach.

## Related
`localization-ready-checker`, `store-localization-writer`, `regional-availability-checker`, `accessibility-checker`, `experience-settings-configurator`.
