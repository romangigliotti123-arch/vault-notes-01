---
title: "Docs: projects / external-tools"
url: https://create.roblox.com/docs/projects/external-tools.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / external-tools

[Open](https://create.roblox.com/docs/projects/external-tools.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs page on using third-party external tools with Roblox projects. Covers the syncing problem, installing Rojo via Rokit, running Rojo with the Studio plugin, Wally package management, and version control/editor tooling. Emphasises that the tools are unmaintained by Roblox and there is no lock-in.

## Tips
- [page](https://create.roblox.com/docs/projects/external-tools) **[[development-process-and-speed]]** Use Rokit with a per-project rokit.toml pinning tool versions so every team member runs identical Rojo/Wally/Lune versions.
- [page](https://create.roblox.com/docs/projects/external-tools) **[[version-control-and-tooling]]** Run Rojo (file system-first) to keep game instances as local files, synced to Studio via the Rojo plugin, enabling Git and external editors.
- [page](https://create.roblox.com/docs/projects/external-tools) **[[version-control-and-tooling]]** Test new tool versions before adopting: bump the version in the .toml, upgrade with Rokit, and downgrade if problems appear.
- [page](https://create.roblox.com/docs/projects/external-tools) **[[version-control-and-tooling]]** Add linters (selene), formatters (StyLua) and Luau Language Server to match Studio script editor capabilities in an external editor.
- [page](https://create.roblox.com/docs/projects/external-tools) **[[version-control-and-tooling]]** Use Wally for reproducible package management, then map the Packages directory into the Rojo project so it syncs to Roblox.
- [page](https://create.roblox.com/docs/projects/external-tools) **[[version-control-and-tooling]]** Use Open Cloud scripts (not synced to Studio) to update published games or restart servers.
- [page](https://create.roblox.com/docs/projects/external-tools) **[[team-and-budget]]** Consider external tooling mainly for larger teams that need change tracking, code review and familiar languages; use Script Sync if you only need an external editor or version control.
- [page](https://create.roblox.com/docs/projects/external-tools) **[[code-architecture-and-frameworks]]** Organise code using Script types and locations guidance and the projects in Roblox/resources before structuring the Rojo project tree.

## Numbers
- [page](https://create.roblox.com/docs/projects/external-tools) Example Rojo version: **7.6.1 (rokit.toml example)**
- [page](https://create.roblox.com/docs/projects/external-tools) Example Wally version: **0.3.2 (rokit.toml example)**
- [page](https://create.roblox.com/docs/projects/external-tools) Example Lune version: **0.10.4 (rokit.toml example)**

## Tools
Rojo, Rokit, Wally, Lune, Script Sync, Selene, StyLua, Luau Language Server

## He points to
- React + Roblox (Roblox docs)
- Script types and locations (Roblox docs)
- Roblox/resources GitHub projects
- Rojo documentation
- Rokit documentation

## Topics
[[code-architecture-and-frameworks]] [[development-process-and-speed]] [[team-and-budget]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
