---
title: "10x Your Roblox Studio Productivity - Claude Code & OpenAI Codex Integration Guide"
url: https://youtu.be/6kcWSMJFaS4
creator: Crusherfire
official: false
advice_density: low
date: 2025-11-22
views: 94636
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# 10x Your Roblox Studio Productivity - Claude Code & OpenAI Codex Integration Guide

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/6kcWSMJFaS4) | crusherfiredev | 94,636 views | 2025-11-22

## Summary
Shows how to install Node.js, Git, Claude Code and OpenAI Codex CLI, clone and build an open-source Roblox Studio MCP server, and connect both agents to a running Studio session so they can read project contents. Tool setup walkthrough; no game-making advice.

## Tips
- [0:00](https://youtu.be/6kcWSMJFaS4?t=0) **[[ai-and-tools]]** Use an MCP server to let Claude Code or Codex read your open Studio project directly, avoiding a move to VS Code and Rojo.
- [6:16](https://youtu.be/6kcWSMJFaS4?t=376) **[[ai-and-tools]]** Build the MCP server with npm install, npm run build, then npm start; it listens on localhost port 3002 for the Studio plugin.
- [8:39](https://youtu.be/6kcWSMJFaS4?t=519) **[[ai-and-tools]]** Register the MCP server with 'claude mcp add' (stdio transport) and verify with '/mcp' inside Claude Code; Claude scopes it to that folder.
- [10:12](https://youtu.be/6kcWSMJFaS4?t=612) **[[ai-and-tools]]** Install the MCP plugin .rbxm into Studio's Plugins folder, restart Studio, then click Connect in the MCP plugin widget.

## Tools
Node.js, npm, Git, Windows Terminal

## Topics
[[ai-and-tools]]

Back to [[crusherfiredev - How to make successful Roblox games]]
