---
name: audio-permission-checker
description: "Prove every sound and music asset in a game is owned, Roblox-provided, licensed or explicitly granted to the experience, with an audio manifest, a scan that finds audio ids used in code but missing from the manifest, and replacement steps for the rest. Use before publish, after buying or moving a game, and when audio stops playing."
category: publish
tags: audio, sound, music, permissions, licence, asset id, import, manifest, copyright, moderation
kb: Roblox/roblox-kb/sound-and-music.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/brand-deals-and-ip-licensing.md, Roblox/roblox-kb/age-ratings-moderation-and-tos.md
related: asset-license-checker, copyright-checker, tos-compliance-checker, sound-placement-planner, group-ownership-setup, publish-readiness-gate
---

# audio-permission-checker

One job: every audio id has a permission you can show. Audio is the asset type where games most often break or get flagged: imported audio is private until the owner grants specific experiences or friends, and music you do not own needs a licence. `scripts/audio_check.py` reads a manifest CSV, fails unknown or evidence-less permissions, and with `--scan` fails any `rbxassetid` used in Sound/AudioPlayer code that is not in the manifest. Limits (length, size, format) and permission mechanics are `live-check`: the Creator Docs audio pages change; the limits you verified are passed in, never built in.

## When to use
Before publish, after moving a game to a group or buying one, when audio plays for you but not for players, and when a notice names a sound. Not for: licensing models and textures (`asset-license-checker`), whether a tune copies a song (`copyright-checker`), building the music system (`sound-placement-planner`).

## Inputs (max 2)
1. Project folder (default: current). 2. Where the audio came from (default: unknown, the manifest will say).

## Procedure
1. Open the live audio assets page (Evidence); copy the current import limits and the permission steps with the date.
2. Inventory: in Studio run `build/asset-license-checker/scripts/list_assets.luau` (read-only) and keep the audio rows; also use Asset Manager for your own uploads.
3. Write `audio.csv` with columns `asset_id,title,owner,permission,length_s,size_mb,evidence`. permission is `owned`, `roblox`, `licensed`, `granted` or `unknown`. `licensed` and `granted` need evidence (a licence link or file path, a receipt id, a screenshot of the permission grant).
4. Run `python -I .rbx/claude-kit/skillpack/publish/audio-permission-checker/scripts/audio_check.py audio.csv --scan <project> --max-seconds <live limit> --max-mb <live limit>`. Every FAIL gets fixed: grant the experience access to your own uploads, replace the asset, or add evidence.
5. Test playback with a fresh account that is not a collaborator: audio that works for you can be silent for players if the permission is missing.
6. Replacement order: your own recording or creation, then Roblox-provided audio from the Creator Store, then a licensed track with the licence on file. Record every replacement in the manifest.
7. For transfers: grant the receiving group's games access before the move (`group-ownership-setup`).
8. Write `release/audio.md` with the manifest, the script output and the playback test. Re-run after any audio change.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) running `list_assets.luau` -> `start_stop_play` -> `get_console_output` to catch "Failed to load sound" warnings. The console warning shows a load failure but not why; ownership and grants are checked on the Creator Hub asset page.

## Fallback
Build the manifest by hand from Asset Manager. The scan covers code references only; Sounds stored as instances in a `.rbxl` appear through `list_assets.luau`, which needs Studio, so those rows are `untested` without it.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs audio assets.md` (only import audio you have rights to; imported audio private until permissions are granted to specific friends or experiences; import format/size/duration limits; song-listing requirements and Audio Terms), `... Docs production publishing account-verification.md` (verified accounts and audio length), `... Docs production publishing ip-guidelines.md`. Pack: `Roblox/roblox-kb/sound-and-music.md`, `Roblox/roblox-kb/brand-deals-and-ip-licensing.md`.

## Output
`audio.csv` and `release/audio.md`.

## Acceptance checks
- [ ] `audio_check.py audio.csv --scan <project>` exits 0 (quote the OK line).
- [ ] Every `licensed` or `granted` row has evidence.
- [ ] Playback was tested with a non-collaborator account, or the row says `untested`.
- [ ] The limits passed to the script came from the live page (date noted).
- [ ] `audio_check.py --selftest` prints `selftest ok`.

## Pitfalls
Using a friend's upload id without a grant. Pasting a popular song's id because it plays today. Testing audio only as the owner. Forgetting audio inside Studio-side instances that the code scan cannot see.

## Related
`asset-license-checker`, `copyright-checker`, `tos-compliance-checker`, `sound-placement-planner`, `group-ownership-setup`.
