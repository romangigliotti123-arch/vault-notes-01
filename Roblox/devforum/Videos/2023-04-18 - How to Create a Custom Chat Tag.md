---
title: "How to Create a Custom Chat Tag"
url: https://devforum.roblox.com/t/how-to-create-a-custom-chat-tag/2302562
creator: Roblox DevForum
official: false
advice_density: low
date: 2023-04-18
views: 129
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Create a Custom Chat Tag

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/how-to-create-a-custom-chat-tag/2302562) | Roblox DevForum | 129 views | 2023-04-18

## Summary
Web tutorial showing how to create a custom chat tag using a LocalScript that sets TextChatService.OnIncomingMessage and prepends a colored PrefixText tag to player messages. Explains the code line by line and notes how to get the player instance via GetNameFromUserIdAsync.

## Tips
- [page](https://devforum.roblox.com/t/how-to-create-a-custom-chat-tag/2302562) **[[ui-ux-design]]** Chat tags can be customised by editing the colored PrefixText string in the TextChatService.OnIncomingMessage callback; the script is meant to be modified.
- [page](https://devforum.roblox.com/t/how-to-create-a-custom-chat-tag/2302562) **[[client-server-and-remotes]]** Place the chat tag LocalScript in StarterPlayer > StarterPlayerScripts so it runs on each client.
- [page](https://devforum.roblox.com/t/how-to-create-a-custom-chat-tag/2302562) **[[scripting-and-performance]]** Check msg.TextSource before modifying the prefix so system messages without a source are not altered.
- [page](https://devforum.roblox.com/t/how-to-create-a-custom-chat-tag/2302562) **[[luau-language-and-types]]** Type the callback parameter as TextChatMessage to make the OnIncomingMessage handler's expected input explicit.

## Tools
TextChatService, TextChatMessageProperties, Players:GetNameFromUserIdAsync

## Topics
[[client-server-and-remotes]] [[luau-language-and-types]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
