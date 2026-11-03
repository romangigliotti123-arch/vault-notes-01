---
title: "Protect Your Games with Script Capabilities Sandboxing"
url: https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642
creator: Roblox DevForum
official: true
advice_density: medium
date: 2026-05-13
views: 330
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Protect Your Games with Script Capabilities Sandboxing

[Open](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) | Roblox DevForum | 330 views | 2026-05-13

## Summary
Roblox staff post announcing that Studio now sandboxes assets inserted from the Creator Store by default, blocking high-risk capabilities (LoadAsset, LoadString, LoadUnownedAsset, CapabilityControl, getfenv/setfenv). Covers how blocked calls surface as errors, a one-time grandparenting list for trusted tools, the Experimental SandboxedInstanceMode override, and follow-up sandboxing rules for remotes, bindables and modules.

## Tips
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) **[[client-server-and-remotes]]** Sandboxed scripts can only fire remotes/bindables that are sandboxed with the same or a subset of the caller's capabilities; check new error messages when remotes stop working.
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) **[[anti-exploit-and-security]]** Do not grant sandbox capability overrides to assets from sources you do not explicitly know and trust; this could expose your experience and players to risk.
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) **[[anti-exploit-and-security]]** Review Output errors from blocked capabilities; clicking the error jumps to the offending script, which may indicate hidden code in an inserted Store asset.
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) **[[scripting-and-performance]]** Avoid require(id), LoadAsset, LoadString and getfenv/setfenv in Store assets; these are blocked in sandboxed assets and prohibited by Store policy.
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) **[[common-mistakes]]** Inserting Store assets that rely on banned capabilities will now break at runtime; replace them with self-contained code rather than expecting them to work.
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) **[[data-persistence]]** Sandboxed scripts cannot require unsandboxed ModuleScripts; keep shared modules sandboxed or move them under a matching-capability container.

## Numbers
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) Banned capabilities for Store assets: **4 (LoadUnownedAsset, LoadAsset, LoadString, CapabilityControl) plus getfenv/setfenv** (Enforced by default on all Creator Store inserted assets)
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) Error message example: **'the target has additional capabilities: LoadUnownedAsset (and 37 more)'** (Shown in Studio Output for blocked BindableEvent:Fire() in release 722)

## Games
- **HD Admin**: Grandparented as a trusted community tool so it keeps working after the sandboxing rollout.
- **Kohl's Admin**: Grandparented as a trusted community tool so it keeps working after the sandboxing rollout.
- **Adonis**: Grandparented as a trusted community tool so it keeps working after the sandboxing rollout.

## Tools
Roblox Studio, SandboxedInstanceMode (Workspace property, beta), Output window

## He points to
- Roblox docs: Interactions between containers section
- Roblox docs: sandboxing and capabilities

## Quotes
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) "Granting an override for an asset you did not create could put your experience and your players at risk."
- [page](https://devforum.roblox.com/t/protect-your-games-with-script-capabilities-sandboxing/4634642) "Studio will automatically sandbox it. For most of the legitimate assets on the Store, you won't notice a difference."

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
