---
title: "[Full Release] The Future of Character Movement: Character Controller Library"
url: https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-04-08
views: 491
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Full Release] The Future of Character Movement: Character Controller Library

[Open](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) | Roblox DevForum | 491 views | 2026-04-08

## Summary
Official Roblox release notes and docs for the Character Controller Library (CCL), a Luau-based replacement for the Humanoid movement system. Covers opt-in via Avatar Settings, tunable controller parameters, legacy-feel toggles, known issues, touch UI shifts, roadmap (Crouch, Sprint, Strafe, custom abilities), and Server Authority compatibility.

## Tips
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[development-process-and-speed]]** Build new projects on the Character Controller Library now; enabling it later means refactoring character logic when Crouch and Sprint land.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[ui-ux-design]]** Keep custom UI out of roughly 60px from each screen side; default touch movement and jump buttons are moving into those zones.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[ui-ux-design]]** Check the new touch button placement in Studio Emulator or on a physical device for overlaps with custom UI after the April 30 update.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[testing-debugging-and-qa]]** Test thoroughly before switching an experience that relies heavily on slopes, ladders, swimming, or MoveTo to the new library, given listed known issues.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[core-loops-and-game-design]]** Use per-ability toggles in Avatar Settings to gate movement, e.g. disable climbing in certain levels or jumping until a player unlocks it.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[core-loops-and-game-design]]** Tune TurnSpeedFactor, RollSpeedFactor, AirController.MoveMaxForce and controller Balance at runtime via Luau to adjust turning, air control and knockdown difficulty.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[core-loops-and-game-design]]** To get legacy feel, disable MaintainLinearMomentum and MaintainAngularMomentum on AirController and set GroundController FrictionWeight 100, Friction 2.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[client-server-and-remotes]]** For Server Authority, enable the beta, enable the CCL, then set the AuthorityMode attribute on Workspace to Server; abilities sync across peers automatically.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[scripting-and-performance]]** Expect performance from equal to 2x faster than Humanoid on server and client depending on in-game circumstances; benchmark your own scene.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[common-mistakes]]** Do not rely on Humanoid:MoveTo, which the new system does not yet support; swimming also breaks with the Single-Collider avatar setting.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[common-mistakes]]** Updating HumanoidDescription can kill characters when the Dead ability has RequiresNeck checked; uncheck it if this matters for your game.
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) **[[roblox-platform-changes]]** Library is loaded dynamically from an asset and may update anytime; breaking changes follow a three-phase rollout, and a custom copy gets no Roblox maintenance.

## Numbers
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) CCL performance vs Humanoid: **same to 2x faster on server and devices** (Real-world measured, depends on in-game circumstances)
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) Touch UI safe margin: **~60px from each side of screen** (Avoid custom UI here to prevent overlap with new touch buttons)
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) Legacy-feel friction setting: **FrictionWeight 100, Friction 2** (GroundController settings for uniform sticky ground)
- [page](https://devforum.roblox.com/t/full-release-the-future-of-character-movement-character-controller-library/4565267) Template rollout: **Classic Obby defaulted ON; all Studio templates over several months** (Announced at official release)

## Tools
Character Controller Library, AvatarAbilities Library, ControllerManager, Avatar Settings, Roblox Studio Emulator, CCL Reference Place

## He points to
- Character Controller Library documentation and tuning guide
- Character Controller Library Studio Beta post
- CCL Reference Place (uncopylocked)

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[roblox-platform-changes]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
