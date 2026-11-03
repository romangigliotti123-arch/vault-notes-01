---
title: "Docs: education / battle-royale-series / ending-matches"
url: https://create.roblox.com/docs/education/battle-royale-series/ending-matches.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / battle-royale-series / ending-matches

[Open](https://create.roblox.com/docs/education/battle-royale-series/ending-matches.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs lesson on ending matches in a battle-royale series: respawning defeated players in the lobby via a Died anonymous function, an endStates table, MatchEnd event firing for timer or single-winner conditions, checkPlayerCount/removeActivePlayer logic, and stopping the timer on match end.

## Tips
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[core-loops-and-game-design]]** Use a single MatchEnd event that passes an end-state value (TimerUp or FoundWinner) so any listening script can react to how the round ended.
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[client-server-and-remotes]]** Use colon syntax (matchEnd:Fire()) rather than dot syntax; check end-state strings match exactly wherever they are referenced.
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[scripting-and-performance]]** Connect a Died event with an anonymous function when you need the player reference inside the handler, since Died itself does not pass the player.
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[scripting-and-performance]]** Keep similarly named variables distinct (e.g. player vs whichPlayer) and declare functions above the code that calls them so they are in scope.
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[scripting-and-performance]]** Remove eliminated players from the active-player table and recheck the count after each removal so the win condition is accurate.
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[events-and-seasonal-content]]** Connect cleanup such as stopping the timer to the MatchEnd event so it runs for every end condition, not just one.
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[testing-debugging-and-qa]]** For faster tests, lower minimumPlayers to 2, lengthen matchDuration, or kill players via Command Bar with workspace.Player1.Humanoid.Health = 0.
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) **[[core-loops-and-game-design]]** Send defeated players back to a lobby with RespawnLocation set and LoadCharacter() instead of respawning them in the arena; LoadCharacter also removes their tools.

## Numbers
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) intermissionDuration: **5 seconds** (Default GameSettings wait before checking player count)
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) matchDuration: **10 seconds** (Example GameSettings value for testing)
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) minimumPlayers: **2** (Players needed to start a match in the example)
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) transitionTime: **5 seconds** (Delay between Get ready message and match start)
- [page](https://create.roblox.com/docs/education/battle-royale-series/ending-matches) Winning condition: **activePlayers count equals 1** (Single remaining player triggers FoundWinner)

## Tools
Roblox Studio, Output window, Command Bar

## He points to
- Roblox Creator Docs: education / battle-royale-series

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[events-and-seasonal-content]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
