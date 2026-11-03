---
title: "Docs: scripting / security / third-party-vulnerabilities"
url: https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / third-party-vulnerabilities

[Open](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on third-party asset security. Explains backdoor scripts in Creator Store models, and how to contain them using model sandboxing and Capabilities. Warns about risky capabilities and advises inspecting scripts before use.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) **[[anti-exploit-and-security]]** Inspect all scripts in Toolbox models before use; watch for obfuscated code and whitespace hiding code off-screen in Studio.
- [page](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) **[[anti-exploit-and-security]]** Sandbox third-party models: set SandboxedInstance to Experimental on Workspace, then set the model's Sandboxed property to true.
- [page](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) **[[anti-exploit-and-security]]** Grant only the Capabilities an asset needs via its Capabilities property, rather than broad access.
- [page](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) **[[anti-exploit-and-security]]** Be especially cautious granting Network, DataStore, AssetRequire, CapabilityControl, or LoadString capabilities to third-party assets; backdoors commonly exploit these.
- [page](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) **[[anti-exploit-and-security]]** Prefer highly-rated community assets vetted by other developers, but popularity does not guarantee safety.
- [page](https://create.roblox.com/docs/scripting/security/third-party-vulnerabilities) **[[anti-exploit-and-security]]** Expect some features to error with 'lacking Capability Unassigned' while sandboxed during beta; grant the needed capability.

## Tools
Roblox Studio Toolbox (Creator Store), Workspace.SandboxedInstance, Model.Sandboxed property, Model.Capabilities property

## He points to
- Script Capabilities documentation

## Topics
[[anti-exploit-and-security]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
