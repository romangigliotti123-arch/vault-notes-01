---
title: "Docs: resources / the-mystery-of-duvall-drive / supporting-systems"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / supporting-systems

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Developer docs describing the supporting systems of "The Mystery of Duvall Drive" (a Roblox game): UseManager for applying grabbed items to targets, highlight/item-indicator systems, lore and thought bubbles, door/drawer/seat managers, animation helpers, kill and respawn volumes, and shared config/utility scripts.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[code-architecture-and-frameworks]]** Wrap repeated interactions in a single shared API (e.g. UseManager.AddUse with tags and callbacks) so each mission reuses one system instead of custom scripts.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[code-architecture-and-frameworks]]** Drive behaviour from CollectionService tags rather than hardcoded instance names; one manager script handles every tagged object automatically.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[scripting-and-performance]]** Use a sphere-based Touched/TouchEnded detector around the player for highlights instead of scanning the whole map each frame.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[ui-ux-design]]** Show lore as a full-screen ScreenGui dismissed by click, and ambient dialogue as a BillboardGui above the object so it doesn't block the screen.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[ui-ux-design]]** Give the on-screen centre crosshair context icons (hand, eye, locked door) so players know which objects are interactable.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[client-server-and-remotes]]** Route client-side systems through a small bindable/invoke interface (e.g. HighlightItemsFunc GetType, EventManager Invoke) instead of letting modules reach into each other.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[data-persistence]]** For story-critical grabbable items, track their original transform and auto-restore them if left dropped for about five seconds so progress can't be lost.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[common-mistakes]]** Disable seating before teleporting players: a CFrame coordinate change while seated will not work correctly.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[optimization-and-streaming]]** Use cosmetic-only LocalScript rotation for distant or non-interactive props to avoid extra server simulation cost.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[development-process-and-speed]]** Keep a DemoGlobalSettings-style script that switches cheats and debug features by PlaceId so one codebase serves develop, playtest and release places.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) **[[physics-pathfinding-and-npc-ai]]** Use a 2D horizontal-distance check to pick the nearest respawn point when there is no checkpoint system.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) Grabbed-item restore timeout: **5 seconds** (RestorableManager resets dropped important objects after this delay)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/supporting-systems) Seat enable/disable window around teleport: **a few seconds before and after** (SeatManager toggles seating around room state teleports)

## Games
- **The Mystery of Duvall Drive**: Reusable tag-driven managers (doors, drawers, highlights, lore) let one codebase power a narrative mystery game with many interactive props.

## Tools
Roblox Studio, CollectionService, TweenService, PrismaticConstraint, ClickDetector, Highlight, ScreenGui, BillboardGui

## He points to
- Highlighting Objects
- Lore and Thought Bubbles
- Rotating Cloud Meshes

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[data-persistence]] [[development-process-and-speed]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
