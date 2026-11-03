---
title: "Docs: players / teams"
url: https://create.roblox.com/docs/players/teams.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players / teams

[Open](https://create.roblox.com/docs/players/teams.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on setting up teams: adding Team objects under Teams service, name and TeamColor, auto-assign behaviour, manually assigning players via Player.Team, and locking SpawnLocations to team colors.

## Tips
- [page](https://create.roblox.com/docs/players/teams) **[[building-and-level-design]]** Keep Team TeamColor values unique per team; team name and color both appear in the player list and name colors.
- [page](https://create.roblox.com/docs/players/teams) **[[development-process-and-speed]]** Leave Team AutoAssignable checked for balanced joins; new players auto-join the team with the fewest members by default.
- [page](https://create.roblox.com/docs/players/teams) **[[building-and-level-design]]** Uncheck SpawnLocation Neutral and set its TeamColor to the matching team's TeamColor, or any player can spawn on it.
- [page](https://create.roblox.com/docs/players/teams) **[[common-mistakes]]** Do not confuse SpawnLocation.TeamColor with BrickColor or Color; the latter only change visual appearance and do nothing for team functionality.
- [page](https://create.roblox.com/docs/players/teams) **[[combat-and-gameplay-systems]]** To force players onto a specific team, uncheck AutoAssignable on that team and set Player.Team to Teams[TEAM_NAME].

## Tools
Roblox Studio Explorer, Properties window

## Topics
[[building-and-level-design]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[development-process-and-speed]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
