---
title: "Docs: education / battle-royale-series / cleanup-and-reset"
url: https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / battle-royale-series / cleanup-and-reset

[Open](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox DevHub education tutorial (battle-royale series, final part) on finishing the game loop: showing end status via DisplayManager, winner lookup with fallback, cleaning up weapons between matches, and resetting players to lobby and clearing activePlayers so the while-true loop can run indefinitely.

## Tips
- [page](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset) **[[development-process-and-speed]]** Check that a winner still exists before reading it (activePlayers[1] may be nil if the player left) and return a fallback string instead of erroring.
- [page](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset) **[[ui-ux-design]]** Send the end-state message to the status GUI before any wait; put task.wait(transitionTime) after updateStatus or players never see the message.
- [page](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset) **[[core-loops-and-game-design]]** Structure the match as a game loop: intermission, prepare, match, end status, cleanup, reset, then repeat, so the game runs indefinitely.
- [page](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset) **[[matchmaking-and-teleport]]** Send players back to the lobby spawn and clear the active players table between matches so each round starts from a clean state.
- [page](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset) **[[combat-and-gameplay-systems]]** Remove equipped and backpack copies of weapons at match end so tools do not carry over into the next round.
- [page](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset) **[[common-mistakes]]** Map each end state (winner found, timer up, unknown) to its own message branch with an else fallback, so an unhandled state shows an error rather than failing silently.
- [page](https://create.roblox.com/docs/education/battle-royale-series/cleanup-and-reset) **[[testing-debugging-and-qa]]** Test with a test server and run at least two full game loops to confirm the reset works without errors.

## Tools
Roblox Studio, Luau

## Topics
[[combat-and-gameplay-systems]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[matchmaking-and-teleport]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
