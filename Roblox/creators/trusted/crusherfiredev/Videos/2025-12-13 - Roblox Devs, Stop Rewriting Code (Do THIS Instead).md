---
title: "Roblox Devs, Stop Rewriting Code (Do THIS Instead)"
url: https://youtu.be/6Q_p2ObUXSo
creator: Crusherfire
official: false
advice_density: high
date: 2025-12-13
views: 62657
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Devs, Stop Rewriting Code (Do THIS Instead)

[Watch](https://youtu.be/6Q_p2ObUXSo) | crusherfiredev | 62,657 views | 2025-12-13

## Summary
Shows how to build game-agnostic, drag-and-drop Roblox systems using a service model (shared, server, client modules plus network and types modules). Walks through a marketplace system with gifting via pseudo game passes and a tutorial system, plus a from-scratch template, server-only module relocation, and packaging systems.

## Tips
- [0:00](https://youtu.be/6Q_p2ObUXSo?t=0) **[[code-architecture-and-frameworks]]** Build systems with no game-specific dependencies so they can be packaged and dropped into any project. Write the infrastructure once, reuse it everywhere.
- [2:22](https://youtu.be/6Q_p2ObUXSo?t=142) **[[code-architecture-and-frameworks]]** Mirror Roblox's service model: a shared module, a server service, a client service, an optional network module for remotes, and a types module.
- [3:03](https://youtu.be/6Q_p2ObUXSo?t=183) **[[code-architecture-and-frameworks]]** Put shared utilities and cross-context signals in the shared module. Keep data, purchase processing and authority on the server; keep UI and client feedback on the client.
- [5:40](https://youtu.be/6Q_p2ObUXSo?t=340) **[[monetisation-devproducts]]** Roblox can't gift game passes directly. Sell a developer product, treat it as a pass, and record ownership in a DataStore. Purchases stack and can be gifted.
- [6:21](https://youtu.be/6Q_p2ObUXSo?t=381) **[[client-server-and-remotes]]** Before prompting a purchase, check the pseudo pass and recipient eligibility on the client. Then re-validate the gift on the server.
- [7:04](https://youtu.be/6Q_p2ObUXSo?t=424) **[[client-server-and-remotes]]** Store each player's owned passes and purchases in a configuration instance on the player. Server updates it; clients listen for attribute changes to react to others' purchases.
- [9:13](https://youtu.be/6Q_p2ObUXSo?t=553) **[[anti-exploit-and-security]]** Relocate server-only modules into ServerScriptService at server start, leaving a dummy module so require paths still work. Clients then can't read that code. The speaker's security claim is unverified and he invites challenges.
- [11:02](https://youtu.be/6Q_p2ObUXSo?t=662) **[[code-architecture-and-frameworks]]** Keep game-specific logic (product ID handlers, pass rewards, tutorial content) in a separate implementation folder that requires the core package. Keep the core free of game logic.
- [13:47](https://youtu.be/6Q_p2ObUXSo?t=827) **[[first-session-onboarding]]** Build tutorials as a generic system: register custom tutorial data, track step and state on the server, validate each step advance server-side, and replicate progress to clients.
- [17:14](https://youtu.be/6Q_p2ObUXSo?t=1034) **[[code-architecture-and-frameworks]]** Create client and server service modules even if unused at first. Have them inherit the shared module via metatable __index so the system can expand later.
- [18:36](https://youtu.be/6Q_p2ObUXSo?t=1116) **[[luau-language-and-types]]** Set the shared module's metatable __index to itself so child services can access shared fields. Store constants like tag names as capitalised fields in the shared module.
- [19:58](https://youtu.be/6Q_p2ObUXSo?t=1198) **[[luau-language-and-types]]** Require modules within a package by relative path (script.Parent) rather than the autocomplete absolute path, which locks the system to one folder hierarchy.
- [20:40](https://youtu.be/6Q_p2ObUXSo?t=1240) **[[luau-language-and-types]]** Return table.freeze(module) from service modules to prevent accidental mutation. Define the initialize function per service; it does not override the shared one.
- [22:03](https://youtu.be/6Q_p2ObUXSo?t=1323) **[[luau-language-and-types]]** Set Workspace > Scripting > Luau type check mode to strict so all scripts are type-checked without per-file comments.
- [24:06](https://youtu.be/6Q_p2ObUXSo?t=1446) **[[client-server-and-remotes]]** Wrap remotes in a network module with typed remote helpers, creating events and unreliable events or functions in one place. Require it wherever remotes are needed.
- [24:47](https://youtu.be/6Q_p2ObUXSo?t=1487) **[[code-architecture-and-frameworks]]** Tag modules with a load tag and set attributes (relocate to server script service, client only) so the module loader knows how to run them.
- [26:46](https://youtu.be/6Q_p2ObUXSo?t=1606) **[[code-architecture-and-frameworks]]** Default comms backbone: signals plus configuration instances for state, CollectionService tags and observers for wiring. Once built, right-click the folder to convert it into a package and publish it.
- [24:47](https://youtu.be/6Q_p2ObUXSo?t=1487) **[[code-architecture-and-frameworks]]** Expose tunable behaviour as attributes on the packaged system, read via script.Parent, so simple systems can be configured without editing or adding setup modules.

## Tools
Roblox Studio, Creator's module loader (tag-based loading, attribute-driven relocation), Typed remotes wrapper (from module util), CollectionService, Luau type check mode setting (Workspace > Scripting)

## He points to
- Top Bar Plus (open-source, game-agnostic drag-and-drop module)

## Quotes
- [25:29](https://youtu.be/6Q_p2ObUXSo?t=1529) "You can write the infrastructure once and then reuse it everywhere."

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[first-session-onboarding]] [[luau-language-and-types]] [[monetisation-devproducts]]

Back to [[crusherfiredev - How to make successful Roblox games]]
