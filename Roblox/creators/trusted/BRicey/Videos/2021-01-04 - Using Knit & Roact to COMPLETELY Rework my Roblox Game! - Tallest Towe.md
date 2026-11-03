---
title: "Using Knit & Roact to COMPLETELY Rework my Roblox Game! - Tallest Tower Devlog #5"
url: https://youtu.be/xwaCg7SWUhc
creator: B Ricey
official: false
advice_density: medium
date: 2021-01-04
views: 20306
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Using Knit & Roact to COMPLETELY Rework my Roblox Game! - Tallest Tower Devlog #5

[Watch](https://youtu.be/xwaCg7SWUhc) | BRicey | 20,306 views | 2021-01-04

## Summary
Devlog for Tallest Tower: the creator reworked the project using Knit (services/controllers/components, tag-based components via CollectionService) and Roact for UI, rebuilt the map with terrain height/color map imports, and tweaked gameplay (locked placed parts, anchor blocks, knockback throws).

## Tips
- [1:02](https://youtu.be/xwaCg7SWUhc?t=62) **[[building-and-level-design]]** Build terrain fast by importing grayscale height maps and color maps via the Terrain Editor Import tool; color map is a copy of height map recolored with terrain materials.
- [1:43](https://youtu.be/xwaCg7SWUhc?t=103) **[[building-and-level-design]]** Convert Parts to Terrain via the Terrain Editor Convert tool to turn blocky part builds into terrain.
- [3:28](https://youtu.be/xwaCg7SWUhc?t=208) **[[code-architecture-and-frameworks]]** Split project into game/client, game/server, and shared folders mapped to StarterPlayerScripts, ServerScriptService, and ReplicatedStorage for clear separation.
- [4:51](https://youtu.be/xwaCg7SWUhc?t=291) **[[code-architecture-and-frameworks]]** Use Knit framework (free, lightweight, open source by Sleitnick) to structure code into services and controllers with a single bootstrap script.
- [5:33](https://youtu.be/xwaCg7SWUhc?t=333) **[[code-architecture-and-frameworks]]** Expose shared modules via a global table (e.g. Knit.Modules) so you only change the module path in one place.
- [6:51](https://youtu.be/xwaCg7SWUhc?t=411) **[[scripting-and-performance]]** Use a Maid utility to collect event connections and instances, then call destroy once to clean them all up instead of manual connection tables.
- [8:21](https://youtu.be/xwaCg7SWUhc?t=501) **[[client-server-and-remotes]]** Use Knit services/controllers so remotes are generated for you rather than handling raw RemoteEvents/RemoteFunctions manually.
- [10:10](https://youtu.be/xwaCg7SWUhc?t=610) **[[code-architecture-and-frameworks]]** Use Knit components bound to CollectionService tags so temporary or per-object logic is created and destroyed automatically with the tagged instance.
- [12:14](https://youtu.be/xwaCg7SWUhc?t=734) **[[code-architecture-and-frameworks]]** Track players or objects with CollectionService tags instead of manual lists; tags auto-clear when a player leaves.
- [13:38](https://youtu.be/xwaCg7SWUhc?t=818) **[[code-architecture-and-frameworks]]** Put shared config in one module returning a table of game constants, accessible from both client and server.
- [14:02](https://youtu.be/xwaCg7SWUhc?t=842) **[[ui-ux-design]]** Use Roact (Roblox's React-style UI library) with reusable element templates so UI components can be reused without editing each one.
- [15:23](https://youtu.be/xwaCg7SWUhc?t=923) **[[ui-ux-design]]** In Roact, update UI by creating new element state rather than mutating instances; be aware the recreate cost can hurt performance on heavy UI.
- [16:10](https://youtu.be/xwaCg7SWUhc?t=970) **[[core-loops-and-game-design]]** Lock placed parts from being dragged so players cannot grab and topple others' towers, forcing skillful throws.
- [18:12](https://youtu.be/xwaCg7SWUhc?t=1092) **[[core-loops-and-game-design]]** Make thrown objects knock players over so players can defend their tower, adding dynamic interaction.
- [18:42](https://youtu.be/xwaCg7SWUhc?t=1122) **[[mindset-and-strategy]]** Consider that grinding out a big rework without progress clips may be less engaging for viewers; ask audience which they prefer.

## Numbers
- [14:42](https://youtu.be/xwaCg7SWUhc?t=882) UI approach: **Roact UI elements are instantiated from templates; UI rebuilt on state change** (Creator's Roact setup for text label component)
- [16:51](https://youtu.be/xwaCg7SWUhc?t=1011) Knockback: **Player falls over within 1 second of being hit by a thrown part** (Creator's test of thrown part hitting player)

## Games
- **Tallest Tower** [0:00](https://youtu.be/xwaCg7SWUhc?t=0): Creator's own game being reworked: locked placed parts, anchor blocks, knockback throws, new terrain and lobby.
- **Arsenal** [3:04](https://youtu.be/xwaCg7SWUhc?t=184): Lobby reference: a menu hub used mainly for buying items and pressing play again, so it needs little polish.

## Tools
Knit framework, Roact, Maid utility (from Knit), CollectionService, Tag Editor plugin, Terrain Editor (height/color map import, convert parts), Visual Studio Code

## He points to
- Knit framework by Sleitnick (Slate Nick)
- Roact (Roblox UI library, React-style)
- Creator's upcoming CollectionService tag tutorial
- Creator's previous OOP video

## Quotes
- [4:51](https://youtu.be/xwaCg7SWUhc?t=291) "Knit is an absolutely amazing framework... it's a super lightweight module, all you do is copy and paste the source folder."
- [18:42](https://youtu.be/xwaCg7SWUhc?t=1122) "I kind of grinded them out without updating like with a bunch of clips... the progress was kind of boring."
- [19:24](https://youtu.be/xwaCg7SWUhc?t=1164) "I'm kind of also losing motivation for this project; I just need to work on it."

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[core-loops-and-game-design]] [[mindset-and-strategy]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[BRicey - How to make successful Roblox games]]
