---
title: "Charm | Roblox Open Source Showcase #9"
url: https://youtu.be/gjUtuovH41w
creator: Possible Panda
official: false
advice_density: medium
date: 2026-09-20
views: 11472
transcript: auto-captions
confidence: high
tags: [roblox, possiblepanda, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.3
---

> [!note] Trust: TRUSTED (credibility audit score 8.3): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Charm | Roblox Open Source Showcase #9

[Watch](https://youtu.be/gjUtuovH41w) | PossiblePanda | 11,472 views | 2026-09-20

## Summary
Tutorial on Charm, a state management module for Roblox, using atoms, effects and computeds. Shows typed atoms for player points and items, updating state from client scripts, and bridging Charm into Fusion UI via a helper module. Mentions a replication library without covering it.

## Tips
- [1:05](https://youtu.be/gjUtuovH41w?t=65) **[[code-architecture-and-frameworks]]** Keep shared state in a separate module of atoms (e.g. player stats) so UI and logic can read and write it outside components.
- [1:47](https://youtu.be/gjUtuovH41w?t=107) **[[luau-language-and-types]]** Type-cast atom tables with an explicit type definition (item ID string, quantity number) so the editor gives proper type hints and safety.
- [3:12](https://youtu.be/gjUtuovH41w?t=192) **[[code-architecture-and-frameworks]]** Read an atom by calling it with no args; pass a function to update it. The function receives the current value and returns the new one.
- [5:11](https://youtu.be/gjUtuovH41w?t=311) **[[code-architecture-and-frameworks]]** Use charm.effect to run code automatically whenever the atoms it reads change, instead of polling or manually triggering updates.
- [7:13](https://youtu.be/gjUtuovH41w?t=433) **[[luau-language-and-types]]** Clone read-only atom tables with table.clone before modifying them, since the value passed into the update function is read-only.
- [9:02](https://youtu.be/gjUtuovH41w?t=542) **[[ui-ux-design]]** Use a computed to derive UI values from atoms; Charm's computed tracks dependencies automatically, similar to Fusion's computed.
- [10:24](https://youtu.be/gjUtuovH41w?t=624) **[[ui-ux-design]]** Bridge Charm atoms into Fusion with a small helper, letting UI bind to game state that lives outside components.
- [10:24](https://youtu.be/gjUtuovH41w?t=624) **[[client-server-and-remotes]]** Use server-side atoms and Charm's replication library to share state between server and client when data must live outside components.

## Numbers
- [3:12](https://youtu.be/gjUtuovH41w?t=192) Points increment in demo: **+150 per update; +1 per second timer** (Demonstration values in example code, not real game metrics)

## Tools
Charm, Fusion, Module loader, Charm replication library

## He points to
- Charm Roblox open source module
- Fusion UI framework video (creator's own)
- Module loader video (creator's own)
- Creator Discord

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[luau-language-and-types]] [[ui-ux-design]]

Back to [[PossiblePanda - How to make successful Roblox games]]
