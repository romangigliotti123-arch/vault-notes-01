---
title: "How to Make Global Announcements in Roblox"
url: https://youtu.be/fIwzczfIu2U
creator: ArTheDev
official: false
advice_density: medium
date: 2026-09-26
views: 619
transcript: auto-captions
confidence: high
tags: [roblox, arthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.5
---

> [!note] Trust: TRUSTED (credibility audit score 8.5): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Make Global Announcements in Roblox

[Watch](https://youtu.be/fIwzczfIu2U) | ArTheDev | 619 views | 2026-09-26

## Summary
Tutorial on building a global announcement system in Roblox: a server Module script that builds a formatted TextChatService message from a table (color presets, thickness, stroke), a RemoteEvent to push it to each client's general channel, and MessagingService to broadcast across servers.

## Tips
- [4:07](https://youtu.be/fIwzczfIu2U?t=247) **[[code-architecture-and-frameworks]]** Put reusable modules in a 'util modules' folder (copy-pasteable across projects) and game-specific modules in a separate modules folder.
- [9:04](https://youtu.be/fIwzczfIu2U?t=544) **[[luau-language-and-types]]** Pass function arguments as a single info table instead of many positional params; avoids forced placeholder args and makes optional fields easy.
- [5:36](https://youtu.be/fIwzczfIu2U?t=336) **[[combat-and-gameplay-systems]]** Define announcement color presets in one table keyed by name (name color + message color) so new announcement types are one line each.
- [15:56](https://youtu.be/fIwzczfIu2U?t=956) **[[client-server-and-remotes]]** Fire the announcement from a server script only; the module must run on the server, and the client just displays the received message via a RemoteEvent.
- [17:00](https://youtu.be/fIwzczfIu2U?t=1020) **[[client-server-and-remotes]]** Use MessagingService:PublishAsync on a shared topic to broadcast announcements to every server, not just the current one.
- [9:45](https://youtu.be/fIwzczfIu2U?t=585) **[[scripting-and-performance]]** Validate required inputs (e.g. player) with an early-return guard if they are nil before using them.

## Numbers
- [6:17](https://youtu.be/fIwzczfIu2U?t=377) Message color presets: **3 starting (red, blue, pink) plus added green; name and message colors set per preset** (Preset table in module; name color fixed, message color changes)
- [15:56](https://youtu.be/fIwzczfIu2U?t=956) Random color pick range: **math.random(0.1,3) indexing 3 options** (Demo button picks a random color preset)
- [5:28](https://youtu.be/fIwzczfIu2U?t=328) Demo wait before announce: **2 seconds** (Task wait before firing test announcement)

## Games
- **Anime game based on Cookie Run Kingdom (unnamed, in development)** [3:26](https://youtu.be/fIwzczfIu2U?t=206): Creator mentions building it as a showcase; no specific design lesson given.

## Tools
Roblox Studio, Luau, TextChatService, RemoteEvent, MessagingService, ModuleScript

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[ArTheDev - How to make successful Roblox games]]
