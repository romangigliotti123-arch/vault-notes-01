---
name: localization-ready-checker
description: "Find UI text that will break in other languages (hardcoded strings, fixed-width labels, concatenated sentences, long-language overflow) and wire Roblox localisation: source language, automatic text capture, translated content on. Use before adding languages or when translated text clips."
category: ui
tags: ui, localization, translation, i18n, text overflow, automatic text capture, localizationservice, languages
kb: Roblox/roblox-kb/localization-and-international.md, Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md
related: mobile-ui-audit, ui-scale-fixer, font-and-color-picker, store-localization-writer, accessibility-checker
---

# localization-ready-checker

Translation breaks UI in two ways: strings that never reach the translator, and translated strings that no longer fit. This skill finds both. Expansion estimates (`scripts/TextFit.luau`, Lune-tested) are general i18n rules of thumb, labelled heuristics; replace them with real measurements once translations exist.

## When to use
Before enabling Automatic Translation or ordering translations; when German/Russian/Spanish text clips. Not for the store page copy (`store-localization-writer`).

## Inputs (max 2)
1. Target languages (default: the top ones by player geography from the analytics dashboard; if unknown, ask rather than guess). 2. Which screens (default: all).

## Procedure
1. Set up the pipeline (vault): set the source language and supported languages first, collect strings with Automatic Text Capture, add any text it misses by hand (runtime-built text), and exclude text that should not translate (names, codes). Turn on Use Translated Content after the table is filled.
2. Scan for hardcoded text: scripts that assign `.Text` from literals or concatenate sentence pieces (`"You have " .. n .. " coins"`). Replace with one translatable template with placeholders so word order can change. `TextFit.looksHardcoded` is a cheap first filter.
3. Estimate fit: for each label give `maxChars` from its width (`TextFit.capacity(widthPx, textSize, lines)`), then `TextFit.check(entries, langs)`; every issue is a label to make wider, allow to wrap, or shorten.
4. Make labels robust: `AutomaticSize` and wrapping for variable text, `TextScaled` only with `UITextSizeConstraint`, no fixed-width buttons around text (vault). Check fonts cover the scripts of the target languages (CJK, Cyrillic).
5. Quality: human translators beat machine output; use automatic translation only as a stopgap, audit it before and after shipping, and remember auto-translation never overrides manual entries (official docs).
6. Pseudo-localisation pass: temporarily show every string at 140% length with accents; screenshot every screen on a phone viewport.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `.Text =` with literals -> `search_game_tree` for fixed-width text objects -> `execute_luau` to list string lengths per label -> `TextFit.check` -> `multi_edit` fixes -> `start_stop_play` -> `screen_capture`. The localisation table UI is a Studio/Creator Hub action: the owner does it.

## Fallback
Static grep plus the estimate table; every fit claim is `untested` until real translations are viewed.

## Evidence
`Roblox/roblox-kb/localization-and-international.md` (set source/supported languages first; collect strings with Automatic Text Capture; add what it misses; exclude non-translatable text; enable Use Translated Content; prefer human translators; auto-translation is a stopgap and never overrides manual translations). `Roblox/roblox-kb/ui-ux-design.md` (AutomaticSize and wrapping for localised text). Expansion factors are heuristics, not vault data.

## Output
```
LOCALISATION CHECK <game>  langs: ...
hardcoded: N (paths)   overflow risks: key lang est/max
pipeline: source set / ATC run / translated content on  (owner steps listed)
```

## Acceptance checks
- [ ] Hardcoded strings listed with paths; sentence concatenations replaced by templates.
- [ ] `TextFit.check` run with real `maxChars`; every issue has a fix.
- [ ] Owner-only steps (source language, enabling translated content) are listed, not claimed.
- [ ] Lune test passes (`TextFit.test.luau`, 5 tests).

## Pitfalls
Building sentences from pieces. Fixed-width buttons. Trusting expansion factors over real text. Forgetting runtime text in scripts that ATC cannot see.

## Related
`mobile-ui-audit`, `ui-scale-fixer`, `font-and-color-picker`, `store-localization-writer`, `accessibility-checker`.
