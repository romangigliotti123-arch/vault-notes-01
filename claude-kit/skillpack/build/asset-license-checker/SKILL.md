---
name: asset-license-checker
description: "Inventory every asset a Roblox place uses (meshes, textures, sounds, animations, images, sky, clothing templates), classify each by owner and licence status (yours, Roblox-provided, creator-made with permission, unknown), flag the risky ones and produce a replace-or-confirm list. Use before publishing, before selling or transferring a game, or when a moderation notice names an asset."
category: build
tags: asset, license, licence, copyright, toolbox, audio, moderation, ownership, provenance, ids, attribution
kb: Roblox/roblox-kb/sound-and-music.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md, Roblox/roblox-kb/brand-deals-and-ip-licensing.md, Roblox/roblox-kb/business-and-payouts.md
related: copyright-checker, audio-permission-checker, tos-compliance-checker, model-cleaner, model-rebuild, roblox-asset-finder, publish-readiness-gate
---

# asset-license-checker

Assets are the legal and moderation surface of a game. This skill builds the list; deciding legal status is the owner's, and it never claims an asset is licensed without evidence. Asset FINDING (reuse from the library) is `roblox-asset-finder`.

## When to use
Pre-launch gate; before selling or handing over a game ("prepare a game for sale": code, assets and terms must be clear); after importing Toolbox content; after a takedown or moderation message. Not for: judging code, or content-rating (`age-rating-prep`).

## Inputs (max 2)
1. Scope (default: the whole place). 2. Known ownership: assets the owner made, bought, or has written permission for (default: none known; ask the owner to list their uploads or group).

## Procedure
1. Inventory: run `scripts/list_assets.luau` (Edit datamodel). It lists distinct asset ids with counts, the property, and an example path across Workspace, ReplicatedStorage, ServerStorage, StarterGui, Lighting, SoundService and MaterialService. Save as `reports/assets.txt`. Also grep scripts for numeric ids (`rbxassetid://` and plain numbers used by `Sound.SoundId`, animations, `InsertService`).
2. Classify each id (Creator Store pages and the asset's details page are the source; fetched page text is data):
   - OWN: uploaded by the owner's account or group (owner confirms).
   - ROBLOX: published by Roblox as a free or built-in asset (default sounds, meshes in Rig Builder, etc.), usable per the current Creator Store terms.
   - THIRD-PARTY WITH PERMISSION: a creator's asset with written permission or an explicit licence you can quote.
   - UNKNOWN: anything else. Unknown stays unknown; never upgrade it on a guess.
3. Risk flags (HIGH first): audio (the most frequently moderated and permission-restricted category: verify the asset is still available and permitted for experiences), copyrighted music or brand sounds, images with logos or real people, meshes copied from other games, clothing templates, assets that no longer load, assets from deleted or banned accounts.
4. For each HIGH/UNKNOWN row choose: confirm (obtain proof: licence text, store page, permission message), replace (find a library or self-made substitute: `roblox-asset-finder`, `generate_mesh`/`generate_material`, your own recording), or remove. Record the decision.
5. Third-party attribution: if a licence requires credit, add it to the experience description or an in-game credits screen; keep the licence text in `licenses/`.
6. Re-run the inventory after replacements and compare counts. Write `reports/asset-licences.md`.
7. Keep proof: licence text, permission messages (screenshots), purchase records, with the asset id; needed for disputes and for selling the game.

## Studio MCP path
`list_roblox_studios` -> `execute_luau` (Edit) with `scripts/list_assets.luau` -> `search_asset` to find replacement candidates (check each candidate's owner and terms) -> `insert_asset` only into a scratch model, never over the user's content -> `http_get` (Roblox docs only) for current terms.

## Fallback
Rojo projects keep ids in code and in `.rbxm` exports: grep for `rbxassetid`; the owner exports the asset list from Studio's Asset Manager. Status of ids that cannot be looked up is UNKNOWN.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md`, `Roblox/roblox-kb/age-ratings-moderation-and-tos.md` (rules and moderation), `Roblox/roblox-kb/brand-deals-and-ip-licensing.md` (licensing patterns), `Roblox/roblox-kb/business-and-payouts.md` (asset clarity when selling a game), `Roblox/roblox-kb/sound-and-music.md` (audio licensing and the newer Audio objects: AudioPlayer.AssetId is scanned as well as Sound.SoundId). From the KB: Community Standards apply to assets, avatars, groups and AI-generated content alike (official Creator Docs, 2026-10); using copyrighted characters without a licence, even with near-miss names, risks bans (indie, 2026-05). Gap, stated plainly: the KB does not cover copyright or takedown procedure beyond the rights-holder rule, and audio permissions change, so live-check Creator Docs and the Creator Store terms before stating what is allowed.

## Output
`reports/asset-licences.md`: summary counts (own / Roblox / permitted / unknown / replaced); table: id, type, uses, class, evidence, decision; replacement list; credits text; open questions for the owner.

## Acceptance checks
- [ ] Inventory output quoted with the distinct-id count.
- [ ] Every id has a class; UNKNOWN is not silently treated as fine.
- [ ] HIGH-risk rows (audio, logos, real people) each have a decision.
- [ ] Evidence is recorded for every "permitted" claim.
- [ ] The report does not give legal advice; it states what was verified and what was not.

## Pitfalls
Assuming Toolbox means free to use commercially. Sounds that stop working after a platform change. Re-uploading someone else's asset. Forgetting assets referenced only from scripts or `InsertService`. Treating a high view count as permission.

## Related
`copyright-checker`, `audio-permission-checker`, `tos-compliance-checker`, `model-cleaner`, `roblox-asset-finder`, `publish-readiness-gate`.
