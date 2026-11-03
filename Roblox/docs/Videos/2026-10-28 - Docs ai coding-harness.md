---
title: "Docs: ai / coding-harness"
url: https://create.roblox.com/docs/ai/coding-harness.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ai / coding-harness

[Open](https://create.roblox.com/docs/ai/coding-harness.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs guide for setting up an AI coding harness (VS Code with Claude Code or Cursor) with a Git repo, Script Sync beta to sync .luau files from disk into Studio, and the Studio MCP server so an agent can read the game tree, create objects, run scripts and playtest. Includes a starter WaveSurvival project and verification steps.

## Tips
- [page](https://create.roblox.com/docs/ai/coding-harness) **[[ai-and-tools]]** Use Script Sync (File → Beta Features) to write Luau in your own editor; files in synced folders appear in Studio automatically.
- [page](https://create.roblox.com/docs/ai/coding-harness) **[[ai-and-tools]]** Connect Script Sync by selecting the top-level project folder, not its subfolders, so services match folders by name.
- [page](https://create.roblox.com/docs/ai/coding-harness) **[[ai-and-tools]]** Use the Studio MCP server to let the agent read the game tree, create objects, run scripts and check output; it covers StarterGui and StarterPack, which Script Sync cannot reach.
- [page](https://create.roblox.com/docs/ai/coding-harness) **[[version-control-and-tooling]]** Keep the place as .rbxlx in a Git repo with a .gitignore excluding .rbxlx, and commit once sync and MCP are verified.
- [page](https://create.roblox.com/docs/ai/coding-harness) **[[development-process-and-speed]]** Build the game one tested phase at a time, giving the agent a context file (e.g. WAVE_SURVIVAL.md) describing the design.
- [page](https://create.roblox.com/docs/ai/coding-harness) **[[testing-debugging-and-qa]]** Verify setup end-to-end by having the agent edit scripts, run a playtest, check output and GetStatus sync state, then delete test scripts.

## Tools
Roblox Studio, Script Sync (beta), Studio MCP server, Visual Studio Code, Claude Code, Cursor, Git

## He points to
- Connect to the Roblox Studio MCP server (Roblox docs)
- create.roblox.com
- git-scm.com

## Topics
[[ai-and-tools]] [[development-process-and-speed]] [[testing-debugging-and-qa]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
