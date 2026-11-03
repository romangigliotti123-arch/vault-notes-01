---
title: "Professional Roblox Game Development with Rojo + Visual Studio Code + Git Version Control"
url: https://youtu.be/0K-5sifYhxs
creator: Dev Total
official: false
advice_density: medium
date: 2022-11-23
views: 16112
transcript: auto-captions
confidence: high
tags: [roblox, devtotal, youtube-learn]
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# Professional Roblox Game Development with Rojo + Visual Studio Code + Git Version Control

[Watch](https://youtu.be/0K-5sifYhxs) | DevTotal | 16,112 views | 2022-11-23

## Summary
Setup tutorial for developing Roblox games in Visual Studio Code using the Rojo VS Code extension and Rojo plugin for Studio, with live file sync. Covers boilerplate project structure, script mapping to Studio, and Git version control basics (init, commit, stage, revert). Ends with a brief tour of a tower defense project using PathfindingService and class-like modules.

## Tips
- [1:47](https://youtu.be/0K-5sifYhxs?t=107) **[[ai-and-tools]]** Install the Rojo VS Code extension (by Avera) and use the command palette (Ctrl+Shift+P) to run Rojo init and build the place file.
- [8:35](https://youtu.be/0K-5sifYhxs?t=515) **[[ai-and-tools]]** Install the Rojo plugin (version 7) in Roblox Studio, start the Rojo server from VS Code, and click Connect so edits sync live.
- [12:05](https://youtu.be/0K-5sifYhxs?t=725) **[[ai-and-tools]]** Write code in VS Code, not Studio; Rojo syncs saved changes into Studio immediately.
- [12:58](https://youtu.be/0K-5sifYhxs?t=778) **[[version-control-and-tooling]]** Use Git from day one: Rojo init creates a local repo and .gitignore; commit early with descriptive messages to track and revert changes.
- [19:13](https://youtu.be/0K-5sifYhxs?t=1153) **[[version-control-and-tooling]]** Track the .rbxl place file in Git too; commit it after changes so you can revert binary place edits.
- [17:49](https://youtu.be/0K-5sifYhxs?t=1069) **[[version-control-and-tooling]]** Push the local repo to GitHub (origin) to back up work and share it with team members.
- [20:34](https://youtu.be/0K-5sifYhxs?t=1234) **[[version-control-and-tooling]]** For fine-grained revert control across commits, consider the GitLens VS Code extension.
- [0:40](https://youtu.be/0K-5sifYhxs?t=40) **[[team-and-budget]]** Keep code in a structured folder layout (shared, server, client modules) so multiple team members can work together more easily.
- [22:48](https://youtu.be/0K-5sifYhxs?t=1368) **[[scripting-and-performance]]** Precompute and hardcode frequently used path positions from PathfindingService output into a module instead of calling PathfindingService every time, for speed.
- [24:52](https://youtu.be/0K-5sifYhxs?t=1492) **[[scripting-and-performance]]** Use PathfindingService material cost settings (e.g., set a material to 0 to make it preferred) to control enemy routes.

## Games
- **Tower Defense game (presenter's own project)** [22:07](https://youtu.be/0K-5sifYhxs?t=1327): Painted path with a paintbrush; zombie follows it via PathfindingService; path positions cached in a module for speed.

## Tools
Visual Studio Code, Rojo (VS Code extension by Avera), Rojo Studio plugin v7, Git, GitHub, GitLens

## He points to
- Rojo docs (rojo.space)
- GitLens VS Code extension

## Topics
[[ai-and-tools]] [[scripting-and-performance]] [[team-and-budget]] [[version-control-and-tooling]]

Back to [[DevTotal - How to make successful Roblox games]]
