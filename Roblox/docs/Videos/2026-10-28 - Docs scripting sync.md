---
title: "Docs: scripting / sync"
url: https://create.roblox.com/docs/scripting/sync.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / sync

[Open](https://create.roblox.com/docs/scripting/sync.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for Script Sync, a feature that syncs Studio scripts and folders to local text files so they can be edited in external editors (VS Code, etc.) and used with version control. Covers setup, limits, conflict resolution, sync rules by filename, LSP recommendations, and settings.

## Tips
- [page](https://create.roblox.com/docs/scripting/sync) **[[development-process-and-speed]]** Sync whole folders rather than individual scripts; child scripts and folders then sync automatically, so creating, deleting, and renaming scripts needs no extra setup.
- [page](https://create.roblox.com/docs/scripting/sync) **[[version-control-and-tooling]]** Use Script Sync for code in version control while keeping the rest of the place in Studio; use Rojo if the whole project should live on disk as source of truth.
- [page](https://create.roblox.com/docs/scripting/sync) **[[version-control-and-tooling]]** Install both the Roblox Luau LSP VS Code extension and the Luau Language Server Companion Studio plugin so language features work correctly with Script Sync.
- [page](https://create.roblox.com/docs/scripting/sync) **[[scripting-and-performance]]** Avoid syncing folders that contain scripts alongside other instance types; Script Sync ignores non-script instances in synced folders.
- [page](https://create.roblox.com/docs/scripting/sync) **[[data-persistence]]** Don't sync scripts that have attributes or tags; Script Sync ignores them, which can cause data loss when creating, deleting, or syncing older files.
- [page](https://create.roblox.com/docs/scripting/sync) **[[common-mistakes]]** Don't have multiple people sync the same script and edit files simultaneously; collaborators can overwrite each other's changes.
- [page](https://create.roblox.com/docs/scripting/sync) **[[common-mistakes]]** Don't delete a top-level synced instance on disk; first Stop Sync in Studio, then delete the file or folder, or Studio throws an error.
- [page](https://create.roblox.com/docs/scripting/sync) **[[common-mistakes]]** Keep script names compatible with the file system: no duplicate names or unsupported characters, or sync will error until resolved.
- [page](https://create.roblox.com/docs/scripting/sync) **[[common-mistakes]]** Don't disable Auto resume sync on place open; it dramatically reduces Script Sync's usefulness.
- [page](https://create.roblox.com/docs/scripting/sync) **[[scripting-and-performance]]** Use the file naming suffixes (.server.luau, .client.luau, .local.luau, .legacy.luau, .plugin.luau) to set script types; plain .luau becomes a ModuleScript.
- [page](https://create.roblox.com/docs/scripting/sync) **[[version-control-and-tooling]]** Use selene for linting and StyLua for formatting alongside Script Sync (community-maintained; verify source before installing).

## Numbers
- [page](https://create.roblox.com/docs/scripting/sync) Max scripts per top-level synced instance: **10,000** (Script Sync scale limit per top-level synced instance)
- [page](https://create.roblox.com/docs/scripting/sync) Max top-level synced instances: **128** (Script Sync scale limit for a place)

## Tools
Roblox Studio Script Sync, Visual Studio Code, Roblox Luau LSP, Luau Language Server Companion, selene, StyLua, Rojo

## He points to
- Script types and locations (Roblox docs)

## Topics
[[common-mistakes]] [[data-persistence]] [[development-process-and-speed]] [[scripting-and-performance]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
