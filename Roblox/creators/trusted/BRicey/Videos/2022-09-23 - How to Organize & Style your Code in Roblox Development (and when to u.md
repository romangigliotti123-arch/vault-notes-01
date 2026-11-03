---
title: "How to Organize & Style your Code in Roblox Development (and when to use OOP)"
url: https://youtu.be/MyK4o2pIpQw
creator: B Ricey
official: false
advice_density: high
date: 2022-09-23
views: 96308
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Organize & Style your Code in Roblox Development (and when to use OOP)

[Watch](https://youtu.be/MyK4o2pIpQw) | BRicey | 96,308 views | 2022-09-23

## Summary
Covers where to put scripts (model vs full game), the "you aren't going to need it" principle with frequent refactoring, when to use OOP (only when state is needed), module-per-class structure, Pascal/camel naming and underscore-private fields, commenting why not what, and shipping over perfection. Mentions Knit and Matter ECS as frameworks.

## Tips
- [1:23](https://youtu.be/MyK4o2pIpQw?t=83) **[[code-architecture-and-frameworks]]** For full games, keep scripts in ServerScriptService and StarterPlayerScripts/StarterCharacterScripts; for standalone models, keep scripts inside the model.
- [2:03](https://youtu.be/MyK4o2pIpQw?t=123) **[[client-server-and-remotes]]** Use the Script's RunContext property to run client scripts anywhere, not only inside tools, StarterPlayerScripts or StarterCharacterScripts.
- [3:26](https://youtu.be/MyK4o2pIpQw?t=206) **[[development-process-and-speed]]** Only build what you need now (YAGNI); don't architect the full game upfront since ideas change during development.
- [4:06](https://youtu.be/MyK4o2pIpQw?t=246) **[[development-process-and-speed]]** Refactor freely; it costs less time than guessing a perfect structure up front. Fail fast like SpaceX rather than designing like NASA SLS.
- [5:28](https://youtu.be/MyK4o2pIpQw?t=328) **[[code-architecture-and-frameworks]]** Don't let scripts grow huge; a ~1000-line tool script with all tools in one file was a mistake. Split into multiple scripts.
- [7:10](https://youtu.be/MyK4o2pIpQw?t=430) **[[code-architecture-and-frameworks]]** Don't create a class for a single function; use plain functions and only introduce an object/class when you need saved state between calls (e.g. cooldowns).
- [9:34](https://youtu.be/MyK4o2pIpQw?t=574) **[[code-architecture-and-frameworks]]** Keep one class per ModuleScript, and keep related functions in their own modules to keep scripts small and organized.
- [10:55](https://youtu.be/MyK4o2pIpQw?t=655) **[[luau-language-and-types]]** Use Pascal case for fields and methods (e.g. self.CooldownTime); prefix private fields with an underscore and camelCase (e.g. self._isCoolingDown) to signal not to access externally.
- [12:38](https://youtu.be/MyK4o2pIpQw?t=758) **[[code-architecture-and-frameworks]]** Mark private members with underscores in any module others will use, since Luau is flexible and nothing enforces privacy.
- [14:29](https://youtu.be/MyK4o2pIpQw?t=869) **[[code-architecture-and-frameworks]]** Only split code into a separate function if it is reused; long init functions with commented sections are fine for single-use logic.
- [15:51](https://youtu.be/MyK4o2pIpQw?t=951) **[[luau-language-and-types]]** Don't copy conventions from other languages like Java just because they are standard there; write idiomatic Luau.
- [16:33](https://youtu.be/MyK4o2pIpQw?t=993) **[[common-mistakes]]** Comment why you are doing something, not what the code does; skip comments when a solo codebase is self-explanatory.
- [17:05](https://youtu.be/MyK4o2pIpQw?t=1025) **[[development-process-and-speed]]** Release a game that mostly works and players enjoy; a perfect codebase that never ships earns nothing.
- [17:58](https://youtu.be/MyK4o2pIpQw?t=1078) **[[code-architecture-and-frameworks]]** Consider Knit for service/controller organization (note it leans on singletons) or Matter ECS for component-based games; pick what is simplest for your project.
- [19:19](https://youtu.be/MyK4o2pIpQw?t=1159) **[[mindset-and-strategy]]** Over-complicating wastes time without improving productivity; find the simplest way to build the game and ship it.

## Numbers
- [5:28](https://youtu.be/MyK4o2pIpQw?t=328) script length: **~1000 lines** (single tool script in Chaos The Next Generation, cited as a mistake)

## Games
- **Chaos The Next Generation** [5:28](https://youtu.be/MyK4o2pIpQw?t=328): Early project where all tools lived in one ~1000-line script with a bloated parent class; a cautionary example.
- **Submarine warfare game** [6:09](https://youtu.be/MyK4o2pIpQw?t=369): Speaker refactored almost the whole codebase and found it more robust and easier to work with.

## Tools
Roblox Studio, Luau

## He points to
- Knit framework
- Matter ECS
- Video critiquing OOP (unnamed creator)

## Quotes
- [17:05](https://youtu.be/MyK4o2pIpQw?t=1025) "If you spend so much time trying to make your code perfect you're never going to release your game."
- [6:09](https://youtu.be/MyK4o2pIpQw?t=369) "You need your code to be like a SpaceX rocket; it needs to launch and it needs to fail fast."

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[development-process-and-speed]] [[luau-language-and-types]] [[mindset-and-strategy]]

Back to [[BRicey - How to make successful Roblox games]]
