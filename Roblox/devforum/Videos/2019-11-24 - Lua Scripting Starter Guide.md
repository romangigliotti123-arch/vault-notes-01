---
title: "Lua Scripting Starter Guide"
url: https://devforum.roblox.com/t/lua-scripting-starter-guide/394618
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-11-24
views: 568
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Lua Scripting Starter Guide

[Open](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) | Roblox DevForum | 568 views | 2019-11-24

## Summary
Beginner Roblox Lua starter guide covering print, operators, concatenation, variables and naming rules, comments, properties, functions with parameters, local vs global scope, booleans, if statements, while/for/repeat loops, break, and arrays. Ends with a Q&A on learning resources, exploiters (FilteringEnabled), and practice-first advice.

## Tips
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[scripting-and-performance]]** Learn Luau fundamentals (print, variables, functions, loops, tables) before tackling advanced game systems; the guide says it provides the basics needed to follow advanced tutorials.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[common-mistakes]]** Define variables and functions before using them; Lua reads top to bottom, so using them earlier returns nil.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[common-mistakes]]** Keep print, function names and keywords lowercase and without spaces before parentheses; incorrect casing or spacing makes Lua fail to run the command.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[common-mistakes]]** Do not put quotes around variable names when you want their value; quotes turn the name into a literal string.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[common-mistakes]]** Remember order of operations: exponents, then multiply/divide, then add/subtract. print(1 + 5 * 2) gives 11, not 12.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[code-architecture-and-frameworks]]** Use local variables for limited scope inside code blocks; global variables stay accessible throughout the script, which can cause clutter.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[code-architecture-and-frameworks]]** Use indentation and comments to organise code; they make code blocks readable for you and reviewers.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[anti-exploit-and-security]]** Exploits mostly succeed against weak scripts; write solid server-side logic and rely on FilteringEnabled, which is applied to all games by default.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[community-and-discord]]** Before asking for help, check the Roblox Developer Hub, Stack Overflow, Lua.org and the DevForum for existing answers.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[mindset-and-strategy]]** Expect learning to take a lot of time and effort; patience and persistence separate strong developers from those who quit mid-project.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[mindset-and-strategy]]** Practise by building unique things yourself; repeated practice is the main path to becoming a better developer.
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) **[[client-server-and-remotes]]** Understand that LocalScripts affect only the individual client while server scripts affect everyone in the server.

## Tools
Roblox Studio, Output, Command Bar

## He points to
- Roblox Developer Hub
- Stack Overflow
- Lua.org
- AlvinBlox (YouTube)
- TheDevKing (YouTube)
- Roblox Scripting Playlist (YouTube)

## Quotes
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) "What sets poor and excellent students isn't necessarily intelligence, but their willingness to put in work and always seeking new ways to become better at what they do."
- [page](https://devforum.roblox.com/t/lua-scripting-starter-guide/394618) "When you can't figure it out, the first step should not be to ask for help. Go to the dev wiki, go to stackoverflow, go to the dev forums."

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[community-and-discord]] [[mindset-and-strategy]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
