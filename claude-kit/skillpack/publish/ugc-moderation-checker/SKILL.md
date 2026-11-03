---
name: ugc-moderation-checker
description: "Trace every path where players create something others see (names, signs, build plots, drawings, uploaded images, avatar-item styling) and check each has filtering, reporting, rate limits, an undo or remove path for staff, and an honest maturity answer. Use when a game has free-form creation, plots, boards or image features."
category: publish
tags: user generated content, moderation, text filter, plots, images, reporting, free-form creation, safety, compliance
kb: Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/ugc-and-avatar-economy.md, Roblox/roblox-kb/social-features-and-virality.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: chat-compliance-checker, age-rating-prep, tos-compliance-checker, toxicity-response-playbook, remote-guard-builder, publish-readiness-gate
---

# ugc-moderation-checker

One job: make the "players create it, others see it" surface safe by construction. Free-form creation raises the age bracket the game can reach and puts moderation risk on the creator, so every path needs a filter, a report route and a staff removal path. `tos-compliance-checker/scripts/compliance_gap.py --focus ugc` finds user-created text/image paths and whether any filter call exists; the rest is a path-by-path trace. Age limits and wording of the rules are `live-check`: the Creator Docs pages change.

## When to use
Plots with names, signs and boards, drawing or image upload, custom pet/item names, player-made maps, emotes or outfits shown to others, and before publish. Not for: ordinary chat (`chat-compliance-checker`), asset licensing (`asset-license-checker`), UGC items sold on the Marketplace (`ugc-item-planner`).

## Inputs (max 2)
1. Project folder (default: current). 2. The list of creation features (default: the scan finds them).

## Procedure
1. Run `python -I ~/.claude/claude-kit/skillpack/publish/tos-compliance-checker/scripts/compliance_gap.py <project> --focus ugc` and note each lead.
2. Build the path table, one row per creation feature: input (what the player types/draws/places), storage (attribute, DataStore, instance), who sees it (self, friends, server), and where the filter runs. Every row must end in a server-side filter call before any other player can see the result (see `chat-compliance-checker` for text; images and builds need a policy: no player-uploaded images unless the platform tools provide moderated paths, `live-check`).
3. Rate limit creation per player on the server (cooldown + size caps) so spam cannot flood a server; clear per-player tables on leave.
4. Staff removal: provide a server command or admin path (kit `Admin` system) to clear any plot, name or sign by UserId, and log who removed what.
5. Reporting: confirm players can reach the platform report flow from the creation surface; for custom boards, show the author's display name so a report is possible.
6. Maturity: free-form creation and social hangouts have a minimum age on the maturity pages (`live-check`: the vault note for 2026-10-28 gives 13+ on one page and 16+ on another, so read both and use the live text); feed the feature into `age-rating-prep`.
7. Test hostile inputs by hand: slurs and personal data patterns (use harmless placeholders), very long strings, rapid repeats, emoji floods, script-looking text. Record what happened.
8. Write `release/ugc-moderation.md`: path table, filter evidence, removal path, hostile-input results, page dates.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `script_grep` (`SetAttribute`, `TextBox`, `FilterStringAsync`) -> `start_stop_play` -> `execute_luau` (Server) to call the creation remote with test strings from a harness -> `get_console_output`. Filter output depends on the live service and the test account; without a play session mark filter rows `untested`.

## Fallback
The scan and the hand-built path table need no Studio. Filter behaviour, reporting flow and age gating stay `untested` until played with real accounts.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs chat guidelines.md` (filter all user text; shared editable text rate-limited), `... Docs chat examples rate-limit-public-text-inputs.md`, `... Docs production promotion content-maturity.md` (free-form creation and social hangouts have minimum ages; assets still moderated regardless of label), `... Docs production promotion experience-guidelines.md` (guidelines do not cover items players bring in; only content you create). Pack: `Roblox/roblox-kb/age-ratings-moderation-and-tos.md`.

## Output
`release/ugc-moderation.md`.

## Acceptance checks
- [ ] The scan ran and each lead is a row in the path table.
- [ ] Every row names the server-side filter location or a "not allowed" decision.
- [ ] A staff removal path exists and was exercised (or `untested`).
- [ ] The creation feature appears in the `age-rating-prep` inventory.
- [ ] Hostile-input results are recorded.

## Pitfalls
Filtering the chat but not the plot name. Showing the raw string to the author and the filtered one to others (inconsistent state, then saving the raw one). No size cap so a 10 MB string reaches the DataStore. Forgetting that attributes and instance names replicate to everyone.

## Related
`chat-compliance-checker`, `age-rating-prep`, `tos-compliance-checker`, `toxicity-response-playbook`, `remote-guard-builder`.
