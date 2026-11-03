---
title: "How to make a Voting System"
url: https://youtu.be/SUZPuQrKJuU
creator: GnomeCode
official: false
advice_density: medium
date: 2024-09-20
views: 24729
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Voting System

[Watch](https://youtu.be/SUZPuQrKJuU) | GnomeCode | 24,729 views | 2024-09-20

## Summary
Tutorial on adding a voting system to a round-based Roblox game: image-button UI named after maps, a RemoteEvent sending votes to the server, a vote tally broadcast to all clients, map selection from the winning vote, and a health refill on teleport.

## Tips
- [0:00](https://youtu.be/SUZPuQrKJuU?t=0) **[[development-process-and-speed]]** Name UI image buttons exactly as the map models in ReplicatedStorage.Maps; a spelling mismatch silently breaks the vote lookup.
- [4:09](https://youtu.be/SUZPuQrKJuU?t=249) **[[client-server-and-remotes]]** Send only the chosen map name from client to server via a RemoteEvent; the server validates and tallies, so clients cannot dictate results.
- [6:49](https://youtu.be/SUZPuQrKJuU?t=409) **[[core-loops-and-game-design]]** Add a dedicated voting stage between intermission and gameplay with its own countdown (example: 5 seconds).
- [7:30](https://youtu.be/SUZPuQrKJuU?t=450) **[[client-server-and-remotes]]** Store votes as votes[mapName][userId] = true so each player is one key; before recording a new vote, clear that user's previous entries to prevent multi-voting.
- [10:19](https://youtu.be/SUZPuQrKJuU?t=619) **[[scripting-and-performance]]** Handle no-vote and invalid-name cases by falling back to a random map; a winner of nil must not be cloned from ReplicatedStorage.
- [14:18](https://youtu.be/SUZPuQrKJuU?t=858) **[[testing-debugging-and-qa]]** Make sure the map-selection function actually returns its value; a missing return caused 'attempt to index nil' when spawning players.
- [16:18](https://youtu.be/SUZPuQrKJuU?t=978) **[[client-server-and-remotes]]** Broadcast the updated tally to all clients with FireAllClients after every vote so vote counters update live rather than only at the end.
- [19:07](https://youtu.be/SUZPuQrKJuU?t=1147) **[[core-loops-and-game-design]]** Reset player health to max when teleporting between rounds so damage does not carry over into the next map, especially for fighting games.
- [20:05](https://youtu.be/SUZPuQrKJuU?t=1205) **[[first-session-onboarding]]** Show a status message such as 'Loading <mapname>...' during the transition so players know which map is coming.

## Numbers
- [0:00](https://youtu.be/SUZPuQrKJuU?t=0) Vote stage countdown: **5 seconds** (Voting phase length set in the server script)
- [0:00](https://youtu.be/SUZPuQrKJuU?t=0) Map choices in demo: **3 maps** (Image buttons for desert, garden, and exosap maps)

## Tools
Roblox Studio, Luau, RemoteEvent, UIListLayout, ImageButton

## He points to
- Discord server (linked by creator)
- g.co website (creator's guides)

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[first-session-onboarding]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[GnomeCode - How to make successful Roblox games]]
