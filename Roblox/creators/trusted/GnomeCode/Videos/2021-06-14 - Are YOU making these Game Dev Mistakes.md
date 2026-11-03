---
title: "Are YOU making these Game Dev Mistakes?"
url: https://youtu.be/0rMO-VHSuGs
creator: GnomeCode
official: false
advice_density: high
date: 2021-06-14
views: 242815
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Are YOU making these Game Dev Mistakes?

[Watch](https://youtu.be/0rMO-VHSuGs) | GnomeCode | 242,815 views | 2021-06-14

## Summary
Roblox dev tutorial on common mistakes: dead buttons/coming-soon menus, teleport service delays and overuse, handling player death without kicking, resetting game state on respawn, team-based checkpoints, and avoiding long empty walking distances.

## Tips
- [0:00](https://youtu.be/0rMO-VHSuGs?t=0) **[[common-mistakes]]** Don't include vanity buttons (info, credits) that do nothing or settings windows with 'coming soon'. Add buttons only when their content exists.
- [0:41](https://youtu.be/0rMO-VHSuGs?t=41) **[[first-session-onboarding]]** Hide unfinished GUI from players using the Visible toggle instead of deleting it, so you can keep working on it without clutter in the live game.
- [2:25](https://youtu.be/0rMO-VHSuGs?t=145) **[[matchmaking-and-teleport]]** Avoid TeleportService for small or light places. Its load delay and Roblox loading screen break immersion; use it only for big builds or matchmaking into reserved servers.
- [4:14](https://youtu.be/0rMO-VHSuGs?t=254) **[[matchmaking-and-teleport]]** When teleporting, fire a RemoteEvent to show a teleport GUI immediately on touch, and use TeleportService's SetTeleportGui so the loading screen is skipped.
- [5:43](https://youtu.be/0rMO-VHSuGs?t=343) **[[matchmaking-and-teleport]]** For same-place travel, move the character's HumanoidRootPart CFrame to a destination part on touch instead of teleporting to another place.
- [9:11](https://youtu.be/0rMO-VHSuGs?t=551) **[[common-mistakes]]** Never kick players on death (e.g. 'please restart'). Kicking forces a full rejoin and hurts replayability; reset the player instead.
- [11:05](https://youtu.be/0rMO-VHSuGs?t=665) **[[development-process-and-speed]]** Set up game state in a per-character setup script on CharacterAdded: clone items and NPCs from templates to spawn points, so respawns restore everything.
- [14:31](https://youtu.be/0rMO-VHSuGs?t=871) **[[combat-and-gameplay-systems]]** Before spawning, destroy existing copies of spawned items/NPCs (check with FindFirstChild in workspace) to avoid duplicate monsters after respawn.
- [16:21](https://youtu.be/0rMO-VHSuGs?t=981) **[[core-loops-and-game-design]]** Add checkpoints using Team objects set to auto-assignable with unique team colors, and make spawn locations non-neutral with matching team color and Team Change On Touch.
- [20:52](https://youtu.be/0rMO-VHSuGs?t=1252) **[[core-loops-and-game-design]]** Keep distances between points of interest to about 10 seconds of walking. Long empty walks feel boring and make players quit.
- [22:14](https://youtu.be/0rMO-VHSuGs?t=1334) **[[building-and-level-design]]** If you must have long distances, add decoration like houses along the path, plus hidden side content such as chests, so the walk feels purposeful.
- [23:38](https://youtu.be/0rMO-VHSuGs?t=1418) **[[core-loops-and-game-design]]** Place NPCs along long routes to give quests and dialogue, so travel doubles as content rather than dead space.

## Numbers
- [10:33](https://youtu.be/0rMO-VHSuGs?t=633) Rejoin cost: **Kicked player must reload from website and redo menu and teleport** (Illustrates why kicks on death hurt replayability)
- [20:52](https://youtu.be/0rMO-VHSuGs?t=1252) Max walk distance: **~10 seconds** (Speaker's guideline for distance between points of interest)

## Tools
Roblox Studio, TeleportService, RemoteEvent, Team objects

## He points to
- Name Jam (game jam the speaker reviewed submissions from)

## Quotes
- [0:41](https://youtu.be/0rMO-VHSuGs?t=41) "never have a window that opens up with no content in it because all that's gonna do the first time people play your game they're gonna see the button"
- [9:53](https://youtu.be/0rMO-VHSuGs?t=593) "you don't want them to just leave and never come back to your game"

## Topics
[[building-and-level-design]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[first-session-onboarding]] [[matchmaking-and-teleport]]

Back to [[GnomeCode - How to make successful Roblox games]]
