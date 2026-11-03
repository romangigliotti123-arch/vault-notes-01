---
title: "Docs: projects / place-files"
url: https://create.roblox.com/docs/projects/place-files.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / place-files

[Open](https://create.roblox.com/docs/projects/place-files.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on place files: how Studio uploads and exports places (.rbxl vs .rbxlx), the 100 MB place size limit, auto-recovery file locations, and steps to troubleshoot oversized places (redundant parts, terrain simplification, collision fidelity, splitting into multiple teleported places).

## Tips
- [page](https://create.roblox.com/docs/projects/place-files) **[[version-control-and-tooling]]** Export places to .rbxl or .rbxlx for version control or external tools; .rbxl is compact but binary, .rbxlx is XML and human-readable but much larger.
- [page](https://create.roblox.com/docs/projects/place-files) **[[optimization-and-streaming]]** If a place nears the 100 MB limit, check for obfuscated or unclear text in models and scripts; it compresses poorly and may indicate a backdoor. Delete and report such models.
- [page](https://create.roblox.com/docs/projects/place-files) **[[optimization-and-streaming]]** Find redundant parts (same size, shape, position) and duplicate instances like SurfaceAppearances or textures; delete them. Creator Store plugins can help find them.
- [page](https://create.roblox.com/docs/projects/place-files) **[[building-and-level-design]]** Keep subsurface terrain as horizontal layers of the same material; sloped layers compress much worse. Check Show Wireframe Rendering for holes or misplaced water under terrain.
- [page](https://create.roblox.com/docs/projects/place-files) **[[optimization-and-streaming]]** Simplify terrain by avoiding dense forests and complex hills; this reduces place size and improves runtime performance.
- [page](https://create.roblox.com/docs/projects/place-files) **[[optimization-and-streaming]]** Set CollisionFidelity to Box or Hull on meshes where appropriate; these are more memory efficient than the default.
- [page](https://create.roblox.com/docs/projects/place-files) **[[development-process-and-speed]]** If other reductions fail, split the universe into multiple smaller places linked by teleports; serialization and upload happen per place, so the universe can grow place by place.
- [page](https://create.roblox.com/docs/projects/place-files) **[[common-mistakes]]** Unreferenced or hidden assets accumulate over time and silently inflate place size; audit them periodically rather than assuming the place is clean.

## Numbers
- [page](https://create.roblox.com/docs/projects/place-files) Max place size: **100 MB (104,857,600 bytes)** (Beyond this, Save to Roblox and Publish to Roblox might fail)
- [page](https://create.roblox.com/docs/projects/place-files) Recovery backups kept with collaboration on: **last 3 save attempts** (Studio backs up failed save attempts as recovery files when collaboration is enabled)

## Tools
Roblox Studio, Creator Store plugins (redundant part finders, terrain optimizers)

## He points to
- Roblox Troubleshooting (place size)

## Topics
[[building-and-level-design]] [[common-mistakes]] [[development-process-and-speed]] [[optimization-and-streaming]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
