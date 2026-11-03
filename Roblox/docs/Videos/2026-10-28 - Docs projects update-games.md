---
title: "Docs: projects / update-games"
url: https://create.roblox.com/docs/projects/update-games.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / update-games

[Open](https://create.roblox.com/docs/projects/update-games.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on releasing game updates. Explains that old-version servers persist until they empty unless restarted, how to force-restart servers via Creator Hub with outdated-only and bleed-off delay options, what happens after restart, and the ServerRestartScheduled event for notifying players.

## Tips
- [page](https://create.roblox.com/docs/projects/update-games) **[[updates-live-ops]]** Without restarting servers, players migrate to the new version only as old servers empty; fine for non-disruptive updates but players may split across versions for a long time.
- [page](https://create.roblox.com/docs/projects/update-games) **[[updates-live-ops]]** If your player data format changes, restart outdated servers so all players run the same version.
- [page](https://create.roblox.com/docs/projects/update-games) **[[updates-live-ops]]** For time-sensitive updates, deploy early, hide new content behind a config, then flip the config value to release it.
- [page](https://create.roblox.com/docs/projects/update-games) **[[updates-live-ops]]** Always select 'Restart only servers with outdated versions' unless your update workflow is independent of place version, to avoid needlessly disconnecting players.
- [page](https://create.roblox.com/docs/projects/update-games) **[[updates-live-ops]]** Use 'Delay server restart' (1–60 minutes) so players can leave on their own instead of being disconnected; this is server bleed-off.
- [page](https://create.roblox.com/docs/projects/update-games) **[[updates-live-ops]]** Listen to DataModel.ServerRestartScheduled on the server to show a countdown, prompt players to save, or teleport them at a convenient time.
- [page](https://create.roblox.com/docs/projects/update-games) **[[matchmaking-and-teleport]]** After a restart, servers stop matchmaking; players still reach them via invites, teleports, or friend joins. Players are auto-teleported to matching new-version servers.
- [page](https://create.roblox.com/docs/projects/update-games) **[[matchmaking-and-teleport]]** To fully shut down a game and block reconnects after restarting servers, revoke public access to the game.

## Numbers
- [page](https://create.roblox.com/docs/projects/update-games) Server bleed-off delay range: **1 to 60 minutes** (Delay server restart option lets players leave on their own)

## Tools
Creator Hub (Configurations > Server management), ServerRestartScheduled event

## Topics
[[matchmaking-and-teleport]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
