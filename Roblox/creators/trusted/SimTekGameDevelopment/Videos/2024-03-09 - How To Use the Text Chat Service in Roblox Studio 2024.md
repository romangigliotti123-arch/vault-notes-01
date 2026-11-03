---
title: "How To Use the Text Chat Service in Roblox Studio 2024"
url: https://youtu.be/H7sk_T1zrD8
creator: SimTek Game Development
official: false
advice_density: medium
date: 2024-03-09
views: 8360
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How To Use the Text Chat Service in Roblox Studio 2024

[Watch](https://youtu.be/H7sk_T1zrD8) | SimTekGameDevelopment | 8,360 views | 2024-03-09

## Summary
Tutorial on Roblox's TextChatService (2024): switching from Legacy chat, using the Sending message event on the client, passing chat text to the server via RemoteEvent, intercepting incoming messages with a callback to recolor text with rich text markup, and displaying system messages. Builds a word-triggered explosion demo.

## Tips
- [0:00](https://youtu.be/H7sk_T1zrD8?t=0) **[[development-process-and-speed]]** Check TextChatService's ChatVersion property in Explorer; new projects default to TextChatService, switch to Legacy only for old code.
- [13:58](https://youtu.be/H7sk_T1zrD8?t=838) **[[scripting-and-performance]]** Lowercase the word list and the incoming message (string.lower) so capitalization doesn't cause missed matches.
- [16:03](https://youtu.be/H7sk_T1zrD8?t=963) **[[scripting-and-performance]]** Check string.match result with truthiness (nil means not found) rather than treating it as a boolean.
- [17:27](https://youtu.be/H7sk_T1zrD8?t=1047) **[[building-and-level-design]]** Place explosions at the target's HumanoidRootPart position in workspace, and play sounds on the root part for proper roll-off.
- [12:03](https://youtu.be/H7sk_T1zrD8?t=723) **[[ui-ux-design]]** Use TextChatMessageProperties with rich text markup in the Text property to recolor or restyle incoming chat messages.
- [18:50](https://youtu.be/H7sk_T1zrD8?t=1130) **[[scripting-and-performance]]** Validate chat keywords on the server and fire the result to all clients via RemoteEvent, keeping game logic server-authoritative.
- [21:33](https://youtu.be/H7sk_T1zrD8?t=1293) **[[ui-ux-design]]** Use TextChannel:DisplaySystemMessage on RBXGeneral to show server announcements in chat with custom formatting via string.format.

## Tools
Roblox Studio, TextChatService, RemoteEvent, Rich text markup

## He points to
- Roblox TextChatService documentation (linked in description)
- TextChatMessage documentation
- Roblox rich text markup reference

## Topics
[[building-and-level-design]] [[development-process-and-speed]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
