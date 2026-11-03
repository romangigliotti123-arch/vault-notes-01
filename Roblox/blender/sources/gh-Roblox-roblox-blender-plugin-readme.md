---
type: research-source
id: gh-Roblox-roblox-blender-plugin-readme
title: "Roblox/roblox-blender-plugin README: A Blender plugin to upload selected assets in Blender to Roblox using Roblox's Open Cloud API."
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin"
published: "2026-04-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0019
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "open-cloud-automation", "other", "roblox-import-pipeline"]
---
# gh-Roblox-roblox-blender-plugin-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox's README for its reference Blender add-on that uploads selected meshes/collections to Roblox via Open Cloud as packages. Covers Blender 3.2+ install, browser login, creator dropdown, package versioning via PackageLink AutoUpdate, and dev/CI/release steps. Says nothing about blender-mcp, Claude, bpy headless scripting, export scale/rigs, or mesh/texture limits.

## Claims
- c1: Roblox blender plugin uploads selected Blender meshes or collections to Roblox via Open Cloud API; each selected object becomes its own asset; a Collection uploads as one asset. *(doc, high; roblox-import-pipeline)*
- c2: Requires Blender 3.2 or greater. *(doc, high; claude-blender-mcp)*
- c3: Install: download zip from releases page, Install from Disk without unzipping, enable 'Upload to Roblox', click Install Dependencies once in N-panel Roblox tab, then restart Blender. *(doc, high; roblox-import-pipeline)*
- c4: Login uses browser OAuth; user picks account/groups, then selects creator from 'Upload to:' dropdown. *(doc, high; open-cloud-automation)*
- c5: Uploaded objects are published as Roblox packages; in Studio they appear under Toolbox > Inventory > My Packages, searchable by object name. *(doc, high; roblox-import-pipeline)*
- c6: PackageLink AutoUpdate property, when checked, makes inserted package update automatically to new Blender uploads, overwriting local modifications. *(doc, high; roblox-import-pipeline)*
- c7: Roblox Package ID is stored as custom property on object/collection; deleting it makes the next upload create a new asset ID instead of a new version. *(doc, high; open-cloud-automation)*
- c8: Roblox states plugin is a reference implementation; it will NOT accept PRs adding features, only bug-fix PRs. *(doc, high; other)*
- c9: Dev workflow: VS Code with JacquesLucke.blender-development extension, run 'Blender: Build and Start'; 'Blender: Reload Addons' to reload. *(doc, high; bpy-scripting-headless)*
- c10: Manual install from source: zip top-level folder so the archive contains a single inner folder, then install as a normal add-on. *(doc, high; bpy-scripting-headless)*
- c11: CI requires black formatting matching the version in requirements-dev.txt before merge to main. *(doc, high; bpy-scripting-headless)*
- c12: Releases auto-built by GitHub Actions on tags matching v[0-9]+.[0-9]+.[0-9]+; plugin version is injected at release and not committed to code. *(doc, high; open-cloud-automation)*
- c13: README lists no triangle, texture, scale, rig or material constraints; the export settings and mesh limits are not covered by this source. *(doc, high; other)*
- c14: No mention of blender-mcp, Claude, or bpy headless scripting in this README; source is off-topic for the Claude-with-Blender part of the topic. *(doc, high; claude-blender-mcp)*

## Numbers
- n1: **Minimum Blender version**: 3.2 
- n2: **Release tag pattern**: v[0-9]+.[0-9]+.[0-9]+ 

## Techniques
- t1: **Package-based versioning**: Upload selected object; in Studio insert package, select PackageLink, enable AutoUpdate so later Blender uploads propagate. Delete Roblox Package ID custom property to force new asset ID.
- t2: **VS Code add-on dev loop**: Open repo in VS Code with Blender Development extension; run Build and Start; reload with Reload Addons; debugger attached.

## Quotes (brief, for attribution)
> Roblox is providing this plugin source as a reference implementation, and we encourage the community to extend and build upon this!  (Roblox)
> we will not be accepting Pull Requests that introduce new features or functionality  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/releases
- https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development
- https://black.readthedocs.io/en/stable/index.html
- https://semver.org/
