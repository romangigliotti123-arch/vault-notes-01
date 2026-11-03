---
title: "Docs: projects / assets / packages"
url: https://create.roblox.com/docs/projects/assets/packages.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / assets / packages

[Open](https://create.roblox.com/docs/projects/assets/packages.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox Creator Docs page on packages (Studio asset system): converting objects to packages, PackageLink, inserting from Toolbox, editing and publishing versions, auto-update, mass updates, sharing permissions, reverting, and comparing versions.

## Tips
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[building-art-and-assets]]** Put a single object inside a Model before converting it to a package so child objects can be added, removed, or scaled later without breaking the package.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[building-art-and-assets]]** Use packages for greybox workflows: placeholder shapes can be published first, then copies auto-update as detailed versions are published.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[team-and-budget]]** Set package Ownership to the group you have permission to edit; ownership transfers are not supported by the asset system, so choose the owner carefully.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[common-mistakes]]** Never delete or move a PackageLink object; doing so converts that copy back to a normal object and loses package capabilities like self-updating.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[scripting-and-performance]]** Inspect scripts in packages you didn't create before running them, since unfamiliar assets can contain malicious scripts; save the place first so you can revert.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[development-process-and-speed]]** Enable AutoUpdate on PackageLink so copies pull new versions on place open; note that modifying a copy disables auto-update for it.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[development-process-and-speed]]** Publish nested packages before publishing their parent package; the parent cannot be published while a nested package has unpublished changes.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[version-control-and-tooling]]** Close other Studio instances of the game's places before a mass update to prevent an unsaved instance from overwriting your updates.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[player-psychology-and-game-feel]]** Add scripts that read package attributes at runtime to implement configurations; attribute values set per copy survive updates, other attributes take new defaults.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[development-process-and-speed]]** Add a version description via Package Details > Versions so changes are traceable and restorable; restoring a version does not reset configuration defaults.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[ugc-and-avatar-economy]]** Grant Use & View permission to collaborators rather than Edit when they only need to consume a package; revoking Use & View does not remove copies already inserted.
- [page](https://create.roblox.com/docs/projects/assets/packages) **[[ugc-and-avatar-economy]]** Grant game access to packages by adding the game's universe ID under Permissions > Experiences, since restricted assets only work in permitted games.

## Tools
Roblox Studio, Toolbox, Asset Manager, Creator Dashboard, PackageLink, Diff viewer (Compare Package Versions)

## He points to
- Roblox Creator Docs: Asset privacy

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[development-process-and-speed]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[team-and-budget]] [[ugc-and-avatar-economy]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
