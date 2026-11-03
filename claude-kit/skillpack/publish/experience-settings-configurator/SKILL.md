---
name: experience-settings-configurator
description: "Plan and check the Creator Hub experience settings sheet for launch (name, description, genre, audience, access, devices, max players, thumbnails, icon, place size, early testers, private servers, questionnaire) and catch conflicts and limit breaches before the owner enters them. Use as the settings step of a release."
category: publish
tags: experience settings, creator hub, genre, audience, access, devices, thumbnails, icon, place size, early testers, publish
kb: Roblox/roblox-kb/titles-descriptions.md, Roblox/roblox-kb/thumbnails-icons.md, Roblox/roblox-kb/studio-business-funding-and-publishing.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: publish-readiness-gate, experience-name-checker, thumbnail-guideline-checker, device-support-setter, private-server-settings-setter, age-rating-prep
---

# experience-settings-configurator

One job: one settings sheet, checked, before anyone clicks in Creator Hub. `scripts/settings_check.py` takes the sheet as JSON and reports conflicts (private servers on a non-public game, paid access with paid private servers, no questionnaire) and numeric limit breaches (place size, early testers, active thumbnails, icon size, description length, genre change interval). The numbers are the Creator Docs values at the vault snapshot (2026-10-28); every one is `live-check` because limits change, and the sheet can override them under `limits`. The owner enters the settings; this skill never changes a live place.

## When to use
Before the first release, before opening the game to a new audience, and when a release changes access, devices or monetization. Not for: wording of the name and description (`experience-name-checker`), image files (`thumbnail-guideline-checker`), the questionnaire answers (`age-rating-prep`).

## Inputs (max 2)
1. Current settings or intended ones (default: ask the owner to read them off Creator Hub / Studio Game Settings). 2. Target audience (default: 13+ first, widen later).

## Procedure
1. Open the live publishing pages (Evidence) and write down the current limits and release requirements with the date. They apply to every release, Publish As and audience change, not only the first.
2. Make the sheet: `python -I ~/.claude/claude-kit/skillpack/publish/experience-settings-configurator/scripts/settings_check.py --template > release/settings.json` and fill it from the project and Creator Hub. Missing fields stay `null` and print as WARN "undecided".
3. Put the live limits into `"limits"` where they differ from the defaults (place bytes, early testers, thumbnails, icon px, description chars, genre change days).
4. Run `python -I .../settings_check.py release/settings.json`. Exit 1 means at least one FAIL; fix the sheet or the project, not the script.
5. Decide each WARN: devices without a phone, an audience that needs a fee or subscription plan, thumbnails outside the advised count. Write the decision next to the field.
6. Get the real place size from the exported file (`backup_check.py make` in `place-backup-planner` records bytes) instead of a guess.
7. Genre: only choose once sure; changes are interval-limited, so record the date of the last change in `genre_changed_days_ago`.
8. Save the final JSON as `release/settings.json`, hand the owner an ordered click list (Creator Hub tab, field, value). Anything about the real dashboard stays `untested`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Server, Edit) to read `game.Name`, `game.MaxPlayers`-style properties that are readable in the open place (Game Settings) -> `get_console_output`. Many settings (genre, audience, access) are web-only and cannot be read from Studio.

## Fallback
The owner pastes the settings from the dashboard. The script needs no Studio. Dashboard-only facts stay `untested` until read live.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production publishing publish-games-and-places.md` (place size limit, early testers, release requirements, fees), `... Docs production publishing experience-genres.md` (genre change interval), `... Docs production publishing thumbnails.md`, `... Docs production publishing experience-icons.md`, `... Docs production publishing descriptions.md`, `... Docs projects configure-games.md`, `... Docs production monetization private-servers.md`. Pack: `Roblox/roblox-kb/titles-descriptions.md`, `Roblox/roblox-kb/thumbnails-icons.md`, `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`.

## Output
`release/settings.json` and the ordered click list.

## Acceptance checks
- [ ] `settings_check.py release/settings.json` exits 0 (quote the OK line).
- [ ] Every limit in the sheet came from the live page (the date is in the file).
- [ ] Each WARN has a written decision.
- [ ] The place size is a measured number.
- [ ] `settings_check.py --selftest` prints `selftest ok`.

## Pitfalls
Using remembered limits. Choosing a genre early and being stuck with it. Enabling private servers on a game that is still private. Overwriting the start place with Publish instead of Publish As. Leaving the default auto-generated icon.

## Related
`publish-readiness-gate`, `experience-name-checker`, `thumbnail-guideline-checker`, `device-support-setter`, `private-server-settings-setter`, `age-rating-prep`.
