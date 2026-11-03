---
title: "How to Prevent Speed Hacking"
url: https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733
creator: Roblox DevForum
official: false
advice_density: medium
date: 2018-12-12
views: 225
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to Prevent Speed Hacking

[Open](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) | Roblox DevForum | 225 views | 2018-12-12

## Summary
Tutorial on a basic server-side speed-hack detection system for Roblox: compares the player's HumanoidRootPart position every second on the X/Z plane against a max distance, and if exceeded, moves the player back to their last valid CFrame instead of kicking. Notes false-positive and teleport caveats.

## Tips
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[anti-exploit-and-security]]** Detect speed hacks by position, not by WalkSpeed or Velocity: hackers can alter any property, but server-side position deltas catch all methods, including FPS-based hacks.
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[anti-exploit-and-security]]** Don't kick on suspected speed hacks; reset the player to their last valid CFrame to avoid rage from false positives on slow connections.
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[anti-exploit-and-security]]** Set the max distance above default WalkSpeed (e.g. 22 vs 16 with checktime 1s) to avoid flagging slow players who appear faster to the server.
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[anti-exploit-and-security]]** Keep maxspeed and checktime proportional; checks that run too fast (e.g. 0.1s) record positions too quickly and fail to work correctly.
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[anti-exploit-and-security]]** Compare only X and Z axes so falling does not trigger a false positive.
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[anti-exploit-and-security]]** Round the distance with math.floor before comparing to avoid inaccurate readings from long decimals.
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[anti-exploit-and-security]]** Disable the check for a few seconds around legitimate teleports, since position-based detection flags teleportation.
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) **[[scripting-and-performance]]** Run the position check as a server Script in the character's StarterCharacterScripts loop with wait(checktime), storing the last CFrame each tick.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) Default WalkSpeed: **16 studs/s** (Baseline the speed threshold is set above)
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) Example maxspeed: **22 studs per checktime** (Max distance per check, with checktime = 1 second)
- [page](https://devforum.roblox.com/t/how-to-prevent-speed-hacking/210733) Example checktime: **1 second** (Interval between position comparisons; 0.1 is too fast)

## Tools
Roblox Studio, Luau

## Topics
[[anti-exploit-and-security]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
