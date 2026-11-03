---
title: "How to setup Rojo, VSCode, and Git for professional Roblox Studio Development"
url: https://youtu.be/ulBM7UdHk_4
creator: B Ricey
official: false
advice_density: medium
date: 2021-03-21
views: 69183
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to setup Rojo, VSCode, and Git for professional Roblox Studio Development

[Watch](https://youtu.be/ulBM7UdHk_4) | BRicey | 69,183 views | 2021-03-21

## Summary
Setup tutorial: installs Git, GitHub Desktop, and VS Code, adds the Rojo VS Code extension and Studio plugin, then creates and syncs a basic Rojo project (file-system scripts into Studio) and explains default.project.json mapping.

## Tips
- [0:41](https://youtu.be/ulBM7UdHk_4?t=41) **[[version-control-and-tooling]]** Use GitHub Desktop instead of raw Git CLI; it wraps Git with a GUI while keeping its backup and branching features.
- [0:07](https://youtu.be/ulBM7UdHk_4?t=7) **[[version-control-and-tooling]]** Use Git branches (production, alpha, beta) so test code can be shared without breaking the main build.
- [5:11](https://youtu.be/ulBM7UdHk_4?t=311) **[[version-control-and-tooling]]** Install the Rojo VS Code extension and enable plugin management so it can auto-manage the Studio plugin.
- [7:32](https://youtu.be/ulBM7UdHk_4?t=452) **[[version-control-and-tooling]]** Create project folders in a stable location like Documents, then open them in VS Code via File > Open Folder.
- [8:14](https://youtu.be/ulBM7UdHk_4?t=494) **[[version-control-and-tooling]]** Run 'Rojo: Initialize' from the VS Code command palette (Ctrl+Shift+P) to generate boilerplate project files.
- [9:41](https://youtu.be/ulBM7UdHk_4?t=581) **[[version-control-and-tooling]]** Use 'rojo build' to output a .rbxlx place file, then open it in Studio to verify the generated structure.
- [10:22](https://youtu.be/ulBM7UdHk_4?t=622) **[[version-control-and-tooling]]** Run 'Rojo: Start Server' and connect from the Studio Rojo plugin using default localhost:34872 settings for live sync.
- [11:44](https://youtu.be/ulBM7UdHk_4?t=704) **[[version-control-and-tooling]]** Remember Rojo syncs one way only: edits in VS Code replicate to Studio, but Studio edits do not flow back to files.
- [12:05](https://youtu.be/ulBM7UdHk_4?t=725) **[[version-control-and-tooling]]** Map folders to Roblox services in default.project.json using the path property; keep only the script mappings to simplify setup.
- [13:26](https://youtu.be/ulBM7UdHk_4?t=806) **[[version-control-and-tooling]]** Name files by suffix: .lua becomes ModuleScript, .server.lua becomes Script, .client.lua becomes LocalScript.

## Numbers
- [10:22](https://youtu.be/ulBM7UdHk_4?t=622) Rojo default server port: **34872 (localhost)** (Default Rojo server address used to connect the Studio plugin)

## Tools
Git, GitHub Desktop, Visual Studio Code, Rojo, Rojo VS Code extension, Rojo Studio plugin, IntelliCode

## He points to
- git-scm.com
- desktop.github.com
- github.com
- Rojo documentation

## Topics
[[version-control-and-tooling]]

Back to [[BRicey - How to make successful Roblox games]]
