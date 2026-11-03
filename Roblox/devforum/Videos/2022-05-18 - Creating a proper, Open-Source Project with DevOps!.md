---
title: "Creating a proper, Open-Source Project with DevOps!"
url: https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-05-18
views: 59
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating a proper, Open-Source Project with DevOps!

[Open](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) | Roblox DevForum | 59 views | 2022-05-18

## Summary
Tutorial by FxllenCode on setting up an open-source Roblox package with a DevOps pipeline: Foreman for toolchains, Rojo project structure (lib, testing, pack projects), Wally publishing, StyLua/Selene linting, and a GitHub Actions CI workflow that builds .rbxm artifacts and publishes to Wally on main.

## Tips
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[development-process-and-speed]]** Develop on a dev branch and only merge to main when production-ready; pushes to main trigger publishing and release creation.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[version-control-and-tooling]]** Use Foreman to pin tool versions (Rojo 7.0.0, Wally 0.3.1, StyLua 0.13.1, Selene 0.9.2) in foreman.toml so all contributors share the same toolchain.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[version-control-and-tooling]]** Keep separate Rojo project files: one for testing in Studio, one for packing a .rbxm, so packages can be tested and distributed without Wally.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[version-control-and-tooling]]** Make the module entry point init.lua and use a Linking.lua file that requires Wally dependencies so they get bundled into the .rbxm.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[version-control-and-tooling]]** Add pack.rbxm to .gitignore and build it in CI rather than committing binaries.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[version-control-and-tooling]]** Run StyLua --check and Selene in CI so style and lint failures block merges and releases.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[version-control-and-tooling]]** Store the Wally auth token as a GitHub repository secret (WALLY_AUTH_TOKEN) and never log in or out of Wally after setup.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[version-control-and-tooling]]** Bump the version in wally.toml before pushing to main; the version string drives the Wally publish and GitHub release tag.
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) **[[development-process-and-speed]]** Use Rojo's live sync (rojo serve) with the Rojo Studio plugin to test code changes in Studio while editing in your text editor.

## Numbers
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) Minimum Rust version for installing Foreman via cargo: **1.53.0** (Required before running cargo install foreman)
- [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) Rojo version pinned: **7.0.0** (Rojo 7 plugin required; older plugin will not work)

## Tools
Foreman, Rojo 7, Wally 0.3.1, StyLua 0.13.1, Selene 0.9.2, GitHub Actions, Roblox/setup-foreman, softprops/action-gh-release

## He points to
- https://github.com/FxllenCode/devops-rblx-tutorial
- https://rojo.space
- https://github.com/UpliftGames/wally

## Topics
[[development-process-and-speed]] [[version-control-and-tooling]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
