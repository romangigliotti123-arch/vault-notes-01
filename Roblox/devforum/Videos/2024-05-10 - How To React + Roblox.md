---
title: "How To: React + Roblox"
url: https://devforum.roblox.com/t/how-to-react-roblox/2964543
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-05-10
views: 836
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How To: React + Roblox

[Open](https://devforum.roblox.com/t/how-to-react-roblox/2964543) | Roblox DevForum | 836 views | 2024-05-10

## Summary
Official Roblox docs guide to react-lua (Roblox's Lua port of React) for building Roblox UIs in code. Covers installation via Wally/Rojo or .rbxm, createElement trees, props, events, useState, useEffect, useMemo, dependency arrays, useRef, custom hooks, and styling with UI child objects.

## Tips
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[ui-ux-design]]** Use built-in Roblox UI tools for simple static UIs; adopt React (react-lua) when UI complexity grows and needs structure.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[code-architecture-and-frameworks]]** Install react-lua via Wally with Rojo (recommended); it lands in ReplicatedStorage. Or import the .rbxm file.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[client-server-and-remotes]]** Mount React root once in a LocalScript under StarterPlayerScripts; pass game data via root:render props and re-call render to update.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[ui-ux-design]]** Always pass an explicit dependency array to useEffect; omitting it reruns the effect every render and can cause infinite loops.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[scripting-and-performance]]** Use useMemo to cache expensive computations, with the input values listed as dependencies so they recompute only on change.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[scripting-and-performance]]** Never mutate state tables in place; build a new table (or use join from Cryo/Dash) and pass it to the setter, since reference equality drives re-renders.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[ui-ux-design]]** Clean up connections (e.g. RunService.Heartbeat, UserInputService signals) by returning a cleanup function from useEffect that calls Disconnect.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[code-architecture-and-frameworks]]** Do not use forwardRef; pass refs as a normally named prop (e.g. setTextRef) instead of the reserved ref name.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[ui-ux-design]]** Style Roblox GUI by adding child objects like UIListLayout, UICorner, UIPadding and UIStroke inside the element's children table.
- [page](https://devforum.roblox.com/t/how-to-react-roblox/2964543) **[[ui-ux-design]]** Treat useRef access to underlying GUIObjects as a last resort; it breaks unidirectional data flow and makes code harder to reason about.

## Tools
react-lua, react-roblox, Wally, Rojo, Cryo, Dash

## He points to
- react-lua-tutorial GitHub repo
- react-lua docs
- Official React docs
- Kampfkarren (custom hook example)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
