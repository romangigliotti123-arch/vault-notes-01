---
title: "The First Person Element Of A First Person Shooter"
url: https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434
creator: Roblox DevForum
official: false
advice_density: medium
date: 2018-08-06
views: 1116
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# The First Person Element Of A First Person Shooter

[Open](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) | Roblox DevForum | 1,116 views | 2018-08-06

## Summary
EgoMoose's guide to building a filtering-enabled first-person view for a Roblox FPS: a client-side view model attached to the camera, weapon attached via Motor6D with C0/C1 offsets, aim-down-sights via lerped joint C1, arm posing via shoulder joints, and replicating look-up/down tilt to other players through server-side interpolation (tiltJoint or BodyPosition). Shooting logic is out of scope.

## Tips
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[building-art-and-assets]]** Build the first-person view model as a clone of the character with only arms, upper torso and head kept; set head and torso transparency to 1 and anchor the head so its CFrame can be set directly.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[client-server-and-remotes]]** Keep the view model local to the camera and do not parent it to the character; first-person BaseParts on the character are invisible to the player, so a separate model is needed.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[client-server-and-remotes]]** Replicate gun and look movements through the server-side character rather than the local view model, since the local player cannot see their own body; this hides network delay.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[client-server-and-remotes]]** Do not fire a RemoteEvent every render step for look angle; fire about every 0.1 s and interpolate on the server with a Motor6D tiltJoint or BodyPosition to save traffic.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[3d-modeling-rigging-and-animation]]** Use humanoid:LoadAnimation for hold and aim poses; animations replicate automatically and interpolate between each other, avoiding extra RemoteEvents for transitions.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[building-art-and-assets]]** Add invisible reference parts (Handle, Right, Left, Aim) with consistent front/up faces on weapon models so offsets and hand placement stay predictable across weapons.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[scripting-and-performance]]** Compute aim-down-sights offset as Handle.CFrame:inverse() * Aim.CFrame and set joint C1 by lerping, so the camera centres on the sight rather than the handle.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[scripting-and-performance]]** Update arm shoulder C1 values each frame in RenderStepped so arms stay attached to the weapon while aiming down sights.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[client-server-and-remotes]]** Consider network ownership before relying on server-side interpolated parts for tilt, as it affects how those parts behave.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[3d-modeling-rigging-and-animation]]** Do not rely on shared animation IDs from others; Roblox blocks sharing of animations, so re-export them to your own account and update the IDs.
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) **[[building-art-and-assets]]** Expect to tune Motor6D C0 per weapon (for example C0 = CFrame.new(1,-1.5,-2)) since weapon size and camera fit vary.

## Numbers
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) Remote fire interval for look angle: **0.1 s (wait(0.1) loop) with server interpolation** (Interpolated tilt update rate recommended by author)
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) Aim-down-sights lerp steps: **t from 0 to 101 in steps of 10, with RenderStepped waits** (Lerp of joint C1 toward aim offset in aimDownSights)
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) Tilt angle split: **Neck and waist receive theta*0.5; arms receive full theta** (Vertical look angle distribution across joints)
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) MaxVelocity for tiltJoint: **math.pi*2*0.01** (Motor6D MaxVelocity suggested in server tilt example)

## Games
- **Open-source FPS (author's place, roblox.com/games/2198837034)**: Author's reference place with weapon sway and extra polish; shows details beyond the base tutorial.

## Tools
Roblox Studio, Motor6D, BodyPosition, RunService RenderStepped/Heartbeat, UserInputService, Animation Editor

## He points to
- ScriptingHelpers original post
- github.com/EgoMoose/Articles (simpleFPS gifs and images)

## Quotes
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) "Since we can't see our actual character in first person mode we're going to use it to replicate all our gun movements."
- [page](https://devforum.roblox.com/t/the-first-person-element-of-a-first-person-shooter/160434) "Wouldn't sending server updates every render step end up using a decent amount of traffic on the server and on the client?"

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
