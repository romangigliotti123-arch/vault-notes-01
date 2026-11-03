---
title: "Maid, Trove, Janitor - Cleanup Modules you never knew you needed in Roblox Development"
url: https://youtu.be/2Msrw5w5cTs
creator: B Ricey
official: false
advice_density: medium
date: 2022-08-21
views: 37233
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Maid, Trove, Janitor - Cleanup Modules you never knew you needed in Roblox Development

[Watch](https://youtu.be/2Msrw5w5cTs) | BRicey | 37,233 views | 2022-08-21

## Summary
Explains why Roblox developers need cleanup modules (Trove, Maid, Janitor) to avoid memory leaks from unreleased connections, parts, and events. Demonstrates refactoring a class to use Trove's add, connect, and destroy methods, then testing that everything is cleaned up.

## Tips
- [2:08](https://youtu.be/2Msrw5w5cTs?t=128) **[[scripting-and-performance]]** Forgotten connections and parts keep running after an object is done, causing leaks; clean up every connection, event and part when the object is destroyed.
- [5:11](https://youtu.be/2Msrw5w5cTs?t=311) **[[code-architecture-and-frameworks]]** Store a Trove per object (self._trove = Trove.new()) and call self._trove:Destroy() as the only line in your destroy method.
- [6:16](https://youtu.be/2Msrw5w5cTs?t=376) **[[code-architecture-and-frameworks]]** Use trove:Add(Instance.new(...)) so creation and registration for cleanup happen on one line.
- [8:24](https://youtu.be/2Msrw5w5cTs?t=504) **[[client-server-and-remotes]]** Use trove:Connect(event, fn) instead of storing connections manually; Trove disconnects them on destroy.
- [12:35](https://youtu.be/2Msrw5w5cTs?t=755) **[[code-architecture-and-frameworks]]** Trove can also hold functions; add a cleanup function to run custom teardown such as RenderStepped unbinding.
- [5:11](https://youtu.be/2Msrw5w5cTs?t=311) **[[code-architecture-and-frameworks]]** Install cleanup modules via a package manager like Wally when using Rojo rather than copy-pasting source.
- [12:35](https://youtu.be/2Msrw5w5cTs?t=755) **[[code-architecture-and-frameworks]]** Janitor is the most feature-complete cleanup module; Trove is simpler and works well with Knit.

## Numbers
- [2:08](https://youtu.be/2Msrw5w5cTs?t=128) Part move interval in demo: **every 10 seconds, 2 studs** (Example script used in the object cleanup demonstration)
- [3:44](https://youtu.be/2Msrw5w5cTs?t=224) Demo cleanup delay: **3 seconds** (Object lifetime before destroy is called in the final test)

## Tools
Trove, Maid, Janitor, Dumpster, Wally, Rojo, Knit, RunService

## He points to
- Promise module (covered in another video by the speaker)

## Quotes
- [4:26](https://youtu.be/2Msrw5w5cTs?t=266) "Cleanup modules let you program in a more fluid, step-by-step fashion without jumping back and forth to remember what to destroy."
- [9:27](https://youtu.be/2Msrw5w5cTs?t=567) "When I first started, I consciously tried to remember what to destroy later, and it led to a whole host of bugs I had no clue how to fix."

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
