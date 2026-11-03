---
title: "Guide to Scripting Bots | Javascript Tutorial | FunCaptcha and New Host Info"
url: https://devforum.roblox.com/t/guide-to-scripting-bots-javascript-tutorial-funcaptcha-and-new-host-info/58201
creator: Roblox DevForum
official: false
advice_density: low
date: 2017-10-25
views: 571
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Guide to Scripting Bots | Javascript Tutorial | FunCaptcha and New Host Info

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/guide-to-scripting-bots-javascript-tutorial-funcaptcha-and-new-host-info/58201) | Roblox DevForum | 571 views | 2017-10-25

## Summary
Web guide (2017, unfinished) on building Discord bots with discord.js that interact with Roblox group ranks via roblox-js, plus a hosted server option on Heroku. Covers setup, commands, promote logic, and role checks. Notes login changes requiring cookies and recommends noblox.js.

## Tips
- [page](https://devforum.roblox.com/t/guide-to-scripting-bots-javascript-tutorial-funcaptcha-and-new-host-info/58201) **[[common-mistakes]]** Don't use roblox-js anymore; Roblox changed logins to require cookies. Use noblox.js, which the author says has better support for the new login.
- [page](https://devforum.roblox.com/t/guide-to-scripting-bots-javascript-tutorial-funcaptcha-and-new-host-info/58201) **[[scripting-and-performance]]** Use a unique password for the bot's Roblox account, separate from your main account.
- [page](https://devforum.roblox.com/t/guide-to-scripting-bots-javascript-tutorial-funcaptcha-and-new-host-info/58201) **[[anti-exploit-and-security]]** Set a maximum promotable rank so bot-driven promotions can't change protected ranks like officers.
- [page](https://devforum.roblox.com/t/guide-to-scripting-bots-javascript-tutorial-funcaptcha-and-new-host-info/58201) **[[community-and-discord]]** Use a Discord bot to manage group members (promote, demote, announce) so clans can run admin tasks from chat.

## Numbers
- [page](https://devforum.roblox.com/t/guide-to-scripting-bots-javascript-tutorial-funcaptcha-and-new-host-info/58201) Group rank thresholds: **Guest rank 0, owner rank 255** (Ranks used to decide promotability in group promote command)

## Tools
discord.js, roblox-js, noblox.js, nodemon

## Topics
[[anti-exploit-and-security]] [[common-mistakes]] [[community-and-discord]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
