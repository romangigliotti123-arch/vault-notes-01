---
title: "Fixing 'X is not a valid member of Y' Error - Roblox Scripting Solutions #1"
url: https://youtu.be/lZrfA9Ogv2M
creator: Emancyphur
official: false
advice_density: medium
date: 2023-03-08
views: 13948
transcript: manual-subs
confidence: high
tags: [roblox, emancyphur, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.6
---

> [!note] Trust: TRUSTED (credibility audit score 7.6): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Fixing "X is not a valid member of Y" Error - Roblox Scripting Solutions #1

[Watch](https://youtu.be/lZrfA9Ogv2M) | Emancyphur | 13,948 views | 2023-03-08

## Summary
Beginner Roblox scripting tutorial on fixing the "X is not a valid member of Y" error. Covers reading the error and script location, typos and capitalization, finding correct names in Explorer/Properties, nested objects, FindFirstChild vs WaitForChild for timing issues, and LocalScript visibility limits on ServerStorage.

## Tips
- [0:56](https://youtu.be/lZrfA9Ogv2M?t=56) **[[scripting-and-performance]]** Read the error's Script path and line number first; the error names the missing child and the parent it was searched in.
- [2:18](https://youtu.be/lZrfA9Ogv2M?t=138) **[[scripting-and-performance]]** Check exact spelling and capitalization against Explorer or Properties; Roblox names and properties are case-sensitive (BrickColor, not Brickcolor).
- [3:43](https://youtu.be/lZrfA9Ogv2M?t=223) **[[scripting-and-performance]]** Use the full path through nested folders (e.g. Workspace.Furniture.Table); a search result showing an object elsewhere does not make a dot-path find it.
- [6:08](https://youtu.be/lZrfA9Ogv2M?t=368) **[[scripting-and-performance]]** Use :FindFirstChild() with a conditional when an object may not exist yet, so the script does not error immediately.
- [6:49](https://youtu.be/lZrfA9Ogv2M?t=409) **[[scripting-and-performance]]** Use :WaitForChild(name, seconds) when you are sure an object will appear; it yields the code below it, so put it in a separate script or reorder if needed.
- [7:49](https://youtu.be/lZrfA9Ogv2M?t=469) **[[client-server-and-remotes]]** LocalScripts cannot see ServerStorage or ServerScriptService; move shared objects to ReplicatedStorage or Workspace, or move the logic to a server Script.
- [9:14](https://youtu.be/lZrfA9Ogv2M?t=554) **[[client-server-and-remotes]]** Objects created by one player's LocalScript are visible only to that player; do not update them from server scripts or other clients.

## Numbers
- [6:49](https://youtu.be/lZrfA9Ogv2M?t=409) WaitForChild default timeout: **5 seconds** (Default wait before WaitForChild gives up; second argument changes it)

## Tools
Roblox Studio Explorer, Properties window, Output window, Autofill (Studio script editor)

## He points to
- Scripting Solutions playlist (creator's channel)

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Emancyphur - How to make successful Roblox games]]
