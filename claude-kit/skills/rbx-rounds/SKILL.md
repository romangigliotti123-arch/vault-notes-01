---
name: rbx-rounds
description: "Architecture for round-based Roblox games (lobby, intermission, round, results) with a server state machine, teams, spawning and cleanup. Use for minigames, battle, obby-race, social deduction (Among Us or Murder Mystery style) or party games with timed rounds."
---

# Round-based game loop

Code comments: none by default (see rbx-luau, Comments).

Server-authoritative state machine in one ModuleScript (`RoundService`), driven by a single loop, with state replicated through attributes or one RemoteEvent.

## States
`Lobby` (waiting for min players) -> `Intermission` (countdown, vote map/mode) -> `Starting` (teleport/spawn, freeze, load map) -> `InRound` (rules, timer) -> `Ending` (winner, rewards, results UI) -> cleanup -> `Lobby`.

## Rules
1. One source of truth: `RoundService.State` and `State.EndsAt = workspace:GetServerTimeNow() + seconds`. Clients render countdowns from `EndsAt`; they never run the timer.
2. Player set: snapshot participants at `Starting`. Handle `PlayerRemoving` mid-round (remove from team, re-check win condition), late joiners (spectate until next round), and everyone leaving (abort to Lobby).
3. Win check runs on every relevant event (death, flag, timer end) and is idempotent; end the round exactly once (guard with a state check).
4. Spawning: assign teams, set `Player.RespawnLocation` / `SpawnLocation.TeamColor`, `LoadCharacterAsync` or `player:LoadCharacter()` at start; freeze with `WalkSpeed = 0` for the countdown rather than anchoring parts.
5. Maps: clone from ServerStorage into Workspace, destroy at end, never leave scripts running from a destroyed map (disconnect and `Destroying` hooks). Vote system validated server side, one vote per player.
6. Rewards: grant at `Ending` only, server side, through the DataStore module; compute from server-tracked stats, not client reports.
7. Pacing: intermission 15-30 s, round 2-5 min depending on genre; min players default 2 with a solo/practice fallback so a new player is never stuck alone in a lobby.
8. Test: 1 player (Lobby fallback), 2 players, leave during each state, join during each state, timer expiry with no winner, server shutdown mid-round.

Output the module with a state table and the test results from a Local Server run.
