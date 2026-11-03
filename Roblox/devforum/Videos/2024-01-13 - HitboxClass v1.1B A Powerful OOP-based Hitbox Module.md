---
title: "HitboxClass | v1.1B | A Powerful OOP-based Hitbox Module"
url: https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-01-13
views: 339
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# HitboxClass | v1.1B | A Powerful OOP-based Hitbox Module

[Open](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) | Roblox DevForum | 339 views | 2024-01-13

## Summary
Documentation page for HitboxClass, an OOP Roblox hitbox module by VulkanAPI. Covers automatic client-side replication, magnitude/part hitboxes, debounces, velocity prediction via WeldTo, usage setup, and security caveats (remotes not secured, script injection into StarterPlayerScripts, Humanoid-only, Alive folder requirement).

## Tips
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[combat-and-gameplay-systems]]** Use a hitbox module that handles client-sided hit detection and networking so you don't write remote plumbing for every attack.
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[anti-exploit-and-security]]** Validate every client-reported hit on the server; the module does not secure remotes. Use sanity checks like magnitude between attacker and target.
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[anti-exploit-and-security]]** Ensure the server only accepts hit results listed in the signal documentation, and reject anything else.
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[combat-and-gameplay-systems]]** Set a DebounceTime per hitbox (e.g. 1 second) to stop the same character being hit repeatedly by one attack.
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[client-server-and-remotes]]** For server-sided hitboxes welded to a moving part, use WeldTo so velocity prediction estimates the part's position on the client.
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[combat-and-gameplay-systems]]** Keep hit targets in a single folder (e.g. Alive) and only search that folder; otherwise nothing gets detected.
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[combat-and-gameplay-systems]]** Check the connected return value from HitboxClass.new; it is always true for server hitboxes but may be false for client hitboxes.
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) **[[code-architecture-and-frameworks]]** Note the module injects a RemoteEvent and a LocalScript into StarterPlayerScripts on first require; account for this in project setup.

## Numbers
- [page](https://devforum.roblox.com/t/hitboxclass-v11b-a-powerful-oop-based-hitbox-module/2790395) Example DebounceTime: **1 second per character** (Sample hitbox config in docs: magnitude size 5, debounce 1s)

## Tools
HitboxClass module (VulkanAPI), GitHub release (.rbxm)

## He points to
- HitboxClass GitHub documentation
- beansinmybathroom (WeldTo velocity prediction method)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
