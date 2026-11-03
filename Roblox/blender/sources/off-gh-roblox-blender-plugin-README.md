---
type: research-source
id: off-gh-roblox-blender-plugin-README
title: "Roblox Blender plugin README (main, repo pushed 2026-04-20)"
source_type: "github"
creator: "Roblox"
url: "https://github.com/Roblox/roblox-blender-plugin#readme"
published: "2026-04-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 3
density: medium
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import"]
---
# off-gh-roblox-blender-plugin-README

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox's reference Blender add-on "Upload to Roblox" uploads selected meshes or collections to Roblox via Open Cloud as packages. Covers install (Blender 3.2+, zip install, Install Dependencies), OAuth login, upload, PackageLink AutoUpdate versioning, and dev/release workflow. No bpy/MCP or mesh-limit content.

## Claims
- c1: Roblox Blender plugin uploads selected meshes or collections via Open Cloud API; each selected object becomes its own asset, collections become one asset. *(doc, high; automation-and-creator-workflows)*
- c2: Plugin requires Blender 3.2 or greater; install by zipping add-on and using Edit > Preferences > Add-ons > Install from Disk without unzipping. *(doc, high; blender-roblox-export-import)*
- c3: After install, Install Dependencies must be clicked once in the N-panel Roblox tab, then Blender restarted. *(doc, high; automation-and-creator-workflows)*
- c4: Login is OAuth via browser; user selects account/groups to authorize, then picks creator from Upload to: dropdown. *(doc, high; automation-and-creator-workflows)*
- c5: Uploaded assets appear in Studio under Home > Toolbox > Inventory > My Packages; list is unordered, so search by object name. *(doc, high; automation-and-creator-workflows)*
- c6: Uploads are packages; PackageLink AutoUpdate pulls new versions and overwrites local modifications in Studio. *(doc, high; automation-and-creator-workflows)*
- c7: Blender stores the package link as a 'Roblox Package ID' custom property on the object or collection; deleting it makes the next upload create a new asset ID. *(doc, high; automation-and-creator-workflows)*
- c8: Roblox states it accepts only bug-fix PRs, not new features; the repo is a reference implementation for Open Cloud integrations. *(doc, high; automation-and-creator-workflows)*
- c9: Releases are built by GitHub Actions when a tag matching v[0-9]+.[0-9]+.[0-9]+ is pushed; plugin version is injected at release, not committed. *(doc, high; automation-and-creator-workflows)*
- c10: Dev workflow: VS Code with JacquesLucke.blender-development extension, run 'Blender: Build and Start'; CI requires black formatting to pass. *(doc, high; automation-and-creator-workflows)*
- c11: Plugin uploads directly from Blender; README gives no FBX/glTF export settings, scale, axis options, mesh, texture, or triangle limits. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **minimum Blender version**: 3.2 
- n2: **release tag format**: v[major].[minor].[patch] 

## Techniques
- t1: **Re-version a package**: Upload from Blender updates existing package. Enable PackageLink AutoUpdate in Studio. To publish to a new asset ID, delete the Roblox Package ID custom property in Blender.
- t2: **Group into one asset**: Group objects into a Collection and select the Collection, then Upload to publish them as a single asset.

### Code: Tag a release to trigger GitHub Actions build
```shell
git tag -a v0.0.0 HEAD -m "My message for v0.0.0"
git push --tags
```

### Code: Format Python before pushing (CI black check)
```shell
pip install -r requirements-dev.txt
black .
```

## Quotes (brief, for attribution)
> A Blender plugin to upload selected assets in Blender to Roblox using Roblox's Open Cloud API.  (Roblox)
> Roblox is providing this plugin source as a reference implementation, and we encourage the community to extend and build upon this!  (Roblox)

## Points to
- https://github.com/Roblox/roblox-blender-plugin/releases
- https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development
- https://black.readthedocs.io/en/stable/index.html
- https://semver.org/
