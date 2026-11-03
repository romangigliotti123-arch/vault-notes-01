---
name: copyright-checker
description: "Look for copied or restricted material in a game (names, descriptions, scripts, UI text, audio and image sources) with a lead scan for provenance cues and your own list of suspected terms, then route each lead to ownership proof, replacement or removal, and prepare the owner for takedown notices. Use before publish and after any notice."
category: publish
tags: copyright, trademark, IP, DMCA, takedown, provenance, licensing, fan game, brands, compliance
kb: Roblox/roblox-kb/brand-deals-and-ip-licensing.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/ugc-and-avatar-economy.md, Roblox/roblox-kb/building-art-and-assets.md
related: asset-license-checker, audio-permission-checker, tos-compliance-checker, thumbnail-guideline-checker, experience-name-checker, publish-readiness-gate
---

# copyright-checker

One job: find the places where material may belong to someone else, and make the owner decide with evidence. `scripts/ip_scan.py` scans text for two things: a terms file YOU provide (brands, characters, songs, shows you may echo) and built-in provenance cues ("ripped", "free model", "from the toolbox", copyright marks, "fan game"). It cannot know what is protected and never clears anything; legal status is the owner's (and, when serious, a lawyer's). The platform's IP guidelines and takedown steps are `live-check`: they change.

## When to use
Before publish, when a game is inspired by a known property, after buying or inheriting a project, and when a notice arrives. Not for: the per-asset licence inventory (`asset-license-checker`), audio permissions (`audio-permission-checker`), image rules (`thumbnail-guideline-checker`).

## Inputs (max 2)
1. Project folder (default: current). 2. Terms the owner worries about, one per line (default: none; the cue scan still runs).

## Procedure
1. Open the live IP guidelines page (Evidence); copy what counts as infringement and the notice process with the date.
2. Make `terms.txt` from the owner's list plus the game's own inspirations (titles, character names, famous phrases).
3. Run `python -I ~/.claude/claude-kit/skillpack/publish/copyright-checker/scripts/ip_scan.py <project> --terms terms.txt`. Read each lead in context.
4. Classify each lead: OWNED (proof: file, receipt, commit), LICENSED (proof: licence text or link, scope and credit terms), ORIGINAL (a generic word), or RISK. For RISK choose replace, remove or get written permission; do not rely on "no profit", "credit given" or "fair use", which the page says do not excuse infringement.
5. Run `asset-license-checker` for the asset side and `audio-permission-checker` for sound; attach their outputs.
6. Check the store page text and thumbnails by eye for lookalike characters, logos and copied art (`thumbnail-guideline-checker`).
7. Notices: keep a verified email linked to the account so notices arrive; know the counter-notice and appeal route from the live page and its deadline. Never file a knowingly false notice or counter-notice.
8. Write `release/ip-review.md`: lead table (lead, class, proof or action, owner), pages checked with date, open risks. Open RISK rows are `fail` in the readiness gate.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` for the terms -> `execute_luau` (Edit) to list `Name`s of Models/Sounds containing the terms -> `get_console_output`. Studio cannot tell who owns a Toolbox model; ownership proof comes from the Creator Store page of each asset.

## Fallback
Run the scan on the Rojo folder and review instance names by hand. Assets inside the `.rbxl` that are not text are not seen by the scan.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs production publishing ip-guidelines.md` (no excuse by non-monetization or credit; AI-modified copies still infringe; false notices illegal; verified email; counter-notice and appeals), `... Docs production publishing rights-manager.md`, `... Docs production publishing dsa-ip-reporting.md` (appeal window), `... Docs ip-licensing license-manager.md`. Pack: `Roblox/roblox-kb/brand-deals-and-ip-licensing.md`. This is a checklist, not legal advice.

## Output
`release/ip-review.md` and `terms.txt`.

## Acceptance checks
- [ ] `ip_scan.py` ran with a terms file (quote the lead counts).
- [ ] Every lead is classified with proof or an action.
- [ ] No RISK row is left open or waived without an owner.
- [ ] The live page date is recorded.
- [ ] `ip_scan.py --selftest` prints `selftest ok`.

## Pitfalls
Reading "no hits" as safe. Excusing a copy because it is a tribute. Trusting a Toolbox model's description as a licence. Forgetting names and text in the store page.

## Related
`asset-license-checker`, `audio-permission-checker`, `tos-compliance-checker`, `thumbnail-guideline-checker`, `experience-name-checker`.
