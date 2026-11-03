---
title: "Advanced Datastore Tutorial - Roblox Studio"
url: https://youtu.be/eMKYqdSvoMs
creator: B Ricey
official: false
advice_density: high
date: 2020-05-13
views: 15499
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Advanced Datastore Tutorial - Roblox Studio

[Watch](https://youtu.be/eMKYqdSvoMs) | BRicey | 15,499 views | 2020-05-13

## Summary
Tutorial on building an advanced DataStore save/load system for Roblox: a ModuleScript holding a session-data table keyed by UserId, default values on PlayerAdded, pcall-wrapped GetAsync/SetAsync, saving on PlayerRemoving, and a public ChangeValue function for other scripts.

## Tips
- [0:33](https://youtu.be/eMKYqdSvoMs?t=33) **[[data-persistence]]** Put all player data in one table keyed by UserId and store it under a single DataStore key; this keeps saves to one write per player.
- [5:36](https://youtu.be/eMKYqdSvoMs?t=336) **[[data-persistence]]** Use a single DataStore for most games; only add more when you need OrderedDataStore, since nested tables can hold very large data.
- [6:18](https://youtu.be/eMKYqdSvoMs?t=378) **[[data-persistence]]** Wrap DataStore GetAsync and SetAsync in pcall so a failed request does not error your scripts.
- [9:20](https://youtu.be/eMKYqdSvoMs?t=560) **[[data-persistence]]** On load, only overwrite session data if the pcall succeeded and data exists; otherwise fall back to defaults.
- [4:45](https://youtu.be/eMKYqdSvoMs?t=285) **[[data-persistence]]** Connect PlayerAdded and PlayerRemoving to functions without parentheses; calling them directly causes errors.
- [3:22](https://youtu.be/eMKYqdSvoMs?t=202) **[[data-persistence]]** Initialise each new player with a default data table (e.g. money = 0, inventory = {}) on PlayerAdded.
- [3:20](https://youtu.be/eMKYqdSvoMs?t=200) **[[code-architecture-and-frameworks]]** Expose a single ChangeValue(player, name, value) function from the data ModuleScript as the only interface other scripts use to modify data.
- [11:53](https://youtu.be/eMKYqdSvoMs?t=713) **[[data-persistence]]** Autosave is a trade-off: it protects progress but adds DataStore load; the speaker had mixed results, so test before relying on it.

## Tools
Roblox Studio, ModuleScript, DataStoreService, pcall

## He points to
- Roblox Developer Hub DataStore article (linked in description)
- Speaker's earlier DataStore videos

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]]

Back to [[BRicey - How to make successful Roblox games]]
