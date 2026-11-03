---
title: "vim for roblox"
url: https://youtu.be/e9ElODFv8lo
creator: Chase Higgins
official: false
advice_density: low
date: 2026-07-24
views: 3574
transcript: auto-captions
confidence: high
tags: [roblox, chasehiggins69, youtube-learn]
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# vim for roblox

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/e9ElODFv8lo) | chasehiggins69 | 3,574 views | 2026-07-24

## Summary
Chase sets up a Windows-to-WSL Fedora environment with ZSH, Antidote, and Neovim configured in Lua (lazy.nvim, Telescope, Harpoon, Mason, blink, treesitter, tokyonight), plus the Luau LSP plugin, tmux, and Rojo/Wally for a Roblox project. Tooling tutorial with no game-business advice.

## Tips
- [0:00](https://youtu.be/e9ElODFv8lo?t=0) **[[version-control-and-tooling]]** Use the Luau LSP plugin with Rojo in Neovim to get autocomplete and types for Studio instances, including ones not saved to disk.
- [2:03](https://youtu.be/e9ElODFv8lo?t=123) **[[version-control-and-tooling]]** After adding a Wally package in wally.toml and running wally install, restart Rojo serve and reconnect so the source map picks up the package.
- [33:51](https://youtu.be/e9ElODFv8lo?t=2031) **[[version-control-and-tooling]]** Regenerate the Luau LSP source map (space LR in his config) when packages or new instances stop being referenced, instead of restarting everything.
- [36:10](https://youtu.be/e9ElODFv8lo?t=2170) **[[version-control-and-tooling]]** Run Neovim in one tmux pane and Rojo serve in another so you can switch between them without losing context.

## Tools
Neovim, WSL Fedora 44, ZSH, Antidote

## Topics
[[version-control-and-tooling]]

Back to [[chasehiggins69 - How to make successful Roblox games]]
