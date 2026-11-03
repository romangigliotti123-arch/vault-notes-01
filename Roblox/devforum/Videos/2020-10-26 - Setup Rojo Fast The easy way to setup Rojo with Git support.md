---
title: "Setup Rojo Fast: The easy way to setup Rojo with Git support"
url: https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-10-26
views: 146
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Setup Rojo Fast: The easy way to setup Rojo with Git support

[Open](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) | Roblox DevForum | 146 views | 2020-10-26

## Summary
Tutorial on setting up Rojo with VSCode, GitHub Desktop and Git for external Roblox code editing. Covers the Rojo VSCode extension and Studio plugin, default.project.json structure, optional AeroGameFramework setup, committing and pushing changes, and recommended Luau extensions.

## Tips
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[development-process-and-speed]]** Use an external editor (VSCode) with Rojo and Git so code is saved outside Studio and survives Studio crashes or forced updates.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[version-control-and-tooling]]** Install GitHub Desktop, create a repo per game, and set VSCode as its default editor to commit and push changes easily.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[version-control-and-tooling]]** Install the Rojo VSCode extension, then use 'rojo welcome screen' > 'MANAGE IT FOR ME' so the extension manages the Studio plugin automatically.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[version-control-and-tooling]]** Start Rojo in VSCode before pressing Connect in Studio; if the plugin fails, check the Studio output.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[version-control-and-tooling]]** In default.project.json, map $path to a src folder under a dedicated child folder (e.g. GameFiles); mapping directly into a service deletes any non-Rojo instances there.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[development-process-and-speed]]** Migrate an existing game to Rojo only if it is early; migrating a far-along project requires changing many code references.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[scripting-and-performance]]** Consider AeroGameFramework for new projects to avoid manually handling RemoteEvents/RemoteFunctions; it bundles modules and ProfileService.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[data-persistence]]** Use ProfileService for data saving, as the author recommends for current projects.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[luau-language-and-types]]** Install Roblox LSP, Selene (linter), Roblox Lua Autocompletes and Roblox API Explorer in VSCode to get Luau IntelliSense and diagnostics.
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) **[[version-control-and-tooling]]** Use GitLens, Prettier and lua-indent in VSCode to match Studio's formatting and see commit history per line.

## Numbers
- [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182) VSCode monthly users (2017): **2,600,000+**

## Tools
Rojo, Visual Studio Code, GitHub Desktop, Git, AeroGameFramework, ProfileService, Roblox LSP, Selene

## He points to
- Rojo documentation
- AeroGameFramework extension and official video tutorials
- AeroGameFramework documentation

## Topics
[[data-persistence]] [[development-process-and-speed]] [[luau-language-and-types]] [[scripting-and-performance]] [[version-control-and-tooling]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
