---
name: streamer-kit-builder
description: "Make a game easy to stream and film: a streamer mode that hides other players' names, HUD-hide and clean-camera options, private-server stream-sniping protections, a creator press kit and a code or link, with StreamerAlias.luau (stable anonymous aliases, Lune-tested). Use before courting creators or when streamers ask for tools."
category: community
tags: streamer, creator, streaming, streamer-mode, alias, privacy, hud, clean-camera, press-kit, clips
kb: Roblox/roblox-kb/influencer-and-creator-marketing.md, Roblox/roblox-kb/community-and-discord.md, Roblox/roblox-kb/social-features-and-virality.md
related: creator-collab-planner, press-kit-builder, collab-pitch-writer, leaderboard-hooks-planner, codes-campaign-planner, accessibility-checker, settings-menu-builder
---

# streamer-kit-builder

The vault lists creator-friendly tooling as a driver of coverage: a streamer mode that anonymises names, server moderation (kick, whitelist), HUD hiding and camera rotation for clean footage, and private-server kickouts and presence settings against stream sniping. It also says to design for clippability. This ships the safe, small version of that, plus the kit creators need.

## When to use
Creators ask for tools, or you are about to pitch creators and want them to succeed. Not for: the creator programme and pitches (`creator-collab-planner`, `collab-pitch-writer`), the press kit alone (`press-kit-builder`), or general settings UI (`settings-menu-builder`).

## Inputs (max 2)
1. Where streaming hurts (default: names visible in chat/board, UI clutter, stream sniping on public servers). 2. Whether private servers exist (default: yes; the platform's private-server rules apply).

## Procedure
1. Streamer mode (client toggle, saved in the player's settings): replace OTHER players' displayed names with aliases in your own UI (nameplates, boards, kill feed, chat headers) using `scripts/StreamerAlias.luau`: `alias(userId, salt)` is stable per session and `uniqueAliases(userIds, salt)` resolves collisions. The salt is per-session so aliases cannot be correlated over days. Names inside platform chat remain the platform's; do not try to rewrite its filtering; this only changes labels you control.
2. Clean footage: a HUD hide toggle, optional free-camera or camera-rotate, hide of damage numbers and popups on demand, a "no music with copyright risk" option if you use licensed music (live-check audio rules), and a mute for the game's own loud events.
3. Anti-sniping: allow a private server for creators (platform's private-server system), a delay option for public-location info, and avoid showing the creator's server id or join link in their UI. Server moderation tools (kick, whitelist) stay behind creator-only checks on the server.
4. Never expose personal or account data: no real names, no friend lists, no location in the streamer overlay.
5. Creator kit (for `press-kit-builder`): logo and screenshots with usage rules, a trailer, key facts, a creator code via `codes-campaign-planner`, a Share Link, a contact route (business email), and a one-page "how to film this game" with the clip-worthy moments.
6. Test: Lune test the alias module; in Studio verify the toggle changes only labels, aliases are stable during the session, and the HUD hide restores cleanly. Settings are saved through the kit PlayerData profile.
7. Lint the kit copy: `python welcome-message-writer/scripts/text_lint.py streamer-kit.txt`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add `StreamerAlias.luau` (ModuleScript) and the toggle UI -> `start_stop_play` -> `execute_luau` (Client or Server as relevant) to print aliases for a few fake ids -> `get_console_output`. Real streaming, platform chat and private-server behaviour need a published place: `untested`.

## Fallback
`StreamerAlias.luau` and its Lune tests run without Studio (`cd systems && lune run ../skillpack/community/streamer-kit-builder/scripts/tests/StreamerAlias.test.luau`, 4 tests). UI wiring is hand steps.

## Evidence
`Roblox/roblox-kb/influencer-and-creator-marketing.md` (build creator-friendly tooling: streamer mode that anonymises names, server moderation, HUD hiding, camera rotation, private-server kickouts and presence settings against stream sniping; unique codes per creator). `Roblox/roblox-kb/community-and-discord.md` (design for clippability; influencer programme). `Roblox/roblox-kb/social-features-and-virality.md`.

## Output
`creators/streamer-kit.md` (toggle spec, anti-sniping list, creator kit contents), the module placed in the game, Lune output pasted.

## Acceptance checks
- [ ] The alias Lune test runs green; output quoted ("4 passed, 0 failed").
- [ ] Streamer mode changes labels only; real ids never appear in the overlay.
- [ ] Creator-only tools are checked on the server, not the client.
- [ ] A press-kit checklist exists with a creator code or link.
- [ ] `text_lint.py` exits 0 on the kit copy.

## Pitfalls
Pretending a hash alias is security. Exposing server ids. Client-side-only creator checks. HUD hide that does not restore. Forcing streamer mode on. Copyrighted music in clips.

## Related
`creator-collab-planner`, `press-kit-builder`, `collab-pitch-writer`, `leaderboard-hooks-planner`, `codes-campaign-planner`.
