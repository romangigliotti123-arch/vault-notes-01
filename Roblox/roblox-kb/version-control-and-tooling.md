---
title: Version Control And Tooling
topic: version-control-and-tooling
theme: Studio & Scripting
sources: 58 videos
creators: [B Ricey, BloxianCode, Chase Higgins, Dev Total, Last Level Studios, Leif, MonarchDev, Possible Panda, Roblox, Roblox Creator Docs, Roblox DevForum, SimTek Game Development, Suphi Kaner, janisjanis01]
source_dates: 2018-08-31 to 2026-10-28
tags: [roblox, knowledge-base, version-control-and-tooling]
---

# Version Control And Tooling

_Rojo, Wally, Argon, Git, VS Code/Luau LSP, Open Cloud, plugins, build pipelines, external tooling._

Evidence base: 124 extracted items from 58 videos by B Ricey, BloxianCode, Chase Higgins, Dev Total, Last Level Studios, Leif, MonarchDev, Possible Panda, Roblox, Roblox Creator Docs, Roblox DevForum, SimTek Game Development, Suphi Kaner, janisjanis01 (2018-08-31 to 2026-10-28). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Two creators cover Roblox version control and external tooling. B Ricey (indie, self-reported, March 2021) teaches a Rojo-first workflow: VS Code, Rojo sync to Studio, Git via GitHub Desktop, and branch-based test builds. Roblox Creator Docs (official, October 2026) describes the current stack: Drafts Mode and Script Sync for in-Studio source control, Rojo as the file-system-first option, Rokit and Wally for toolchain and packages, Luau LSP with the companion plugin, selene and StyLua for lint and format, Open Cloud for automation, and .rbxlx place files in Git. Where they conflict, the 2026 official guidance wins. Items marked low-advice are weaker evidence.

## Rules and findings
- **Prefer official 2026 tooling over 2021 indie tooling** (multiple-creators): B Ricey's 2021 workflow (Rojo VS Code extension, rojo: Initialize, plugin management) predates Rokit, Script Sync, Drafts Mode and the Luau LSP companion plugin. For new projects, follow the official 2026 stack and treat the 2021 steps as historical. Sources: [B Ricey 2021-03 5:11](https://youtu.be/ulBM7UdHk_4?t=311), [B Ricey 2021-03 8:14](https://youtu.be/ulBM7UdHk_4?t=494), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/sync), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/sync). Newest source 2026-10-28.
- **Choose Script Sync for code-only version control** (multiple-creators): If you want only scripts in Git while the rest of the place stays in Studio, use Script Sync. If the whole project should be the on-disk source of truth, use Rojo instead. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/sync), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools). Newest source 2026-10-28.
- **Choose Rojo for file-system-first projects** (multiple-creators): If you want all game instances as local files that Git and external editors can manage, run Rojo. Map folders to services in default.project.json via the path property, and keep the Packages directory mapped so Wally packages sync to Roblox. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools), [B Ricey 2021-03 12:05](https://youtu.be/ulBM7UdHk_4?t=725), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools). Newest source 2026-10-28.
- **Use Drafts Mode for in-Studio collaboration without external tools** (one-creator-repeated): Drafts Mode is off by default. Enable it in File > Experience Settings to edit scripts locally and commit to a shared repo. Before committing collaborator changes, use Compare With Server and Merge From Server to resolve conflicts. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/collaboration), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/collaboration). Newest source 2026-10-28.
- **Install both Luau LSP pieces when using Script Sync** (one-creator-repeated): Install the Roblox Luau LSP VS Code extension and the Luau Language Server Companion Studio plugin. Language features do not work correctly with Script Sync using only one of them. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/sync), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools). Newest source 2026-10-28.
- **Match Studio editor features in external editors** (multiple-creators): Outside Studio, add a linter (selene), a formatter (StyLua) and the Luau Language Server. Community tools: verify the source before installing. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/scripting/sync). Newest source 2026-10-28.
- **Pin tool versions with Rokit and upgrade cautiously** (one-creator-repeated): Declare tool versions in the .toml (rokit.toml). Example pins: Rojo 7.6.1, Wally 0.3.2, Lune 0.10.4. Before adopting a new version, bump it, upgrade with Rokit, and downgrade if problems appear. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools). Newest source 2026-10-28.
- **Keep the place binary out of Git and version the sources** (multiple-creators): Keep the place as .rbxlx in a Git repo with a .gitignore that excludes .rbxlx. Commit only after sync and MCP are verified. .rbxl is compact but binary; .rbxlx is XML, readable, and much larger. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/coding-harness), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/place-files). Newest source 2026-10-28.
- **Use branches to isolate test code** (single-mention): Use Git branches such as production, alpha and beta so test code can be shared without breaking the main build. Use GitHub Desktop if you prefer a GUI over the Git CLI; it keeps backup and branching features. Sources: [B Ricey 2021-03 0:07](https://youtu.be/ulBM7UdHk_4?t=7), [B Ricey 2021-03 0:41](https://youtu.be/ulBM7UdHk_4?t=41), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/accelerated-workflows). Newest source 2026-10-28.
- **Treat Rojo sync direction as one-way (indie claim)** (single-mention): B Ricey (2021) says edits in VS Code replicate to Studio but Studio edits do not flow back to files. No official item confirms or rebuts this for the 2026 Rojo version, so verify it in your own setup before relying on it. Sources: [B Ricey 2021-03 11:44](https://youtu.be/ulBM7UdHk_4?t=704), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools). Newest source 2026-10-28.
- **Name script files by suffix to set their class** (single-mention): In Rojo-style projects, .lua maps to ModuleScript, .server.lua to Script, and .client.lua to LocalScript. Only the indie 2021 source covers this; confirm against current Rojo behavior. Sources: [B Ricey 2021-03 13:26](https://youtu.be/ulBM7UdHk_4?t=806). Newest source 2021-03-21.
- **Start live sync on the default port** (single-mention): Run Rojo: Start Server and connect the Studio Rojo plugin on localhost:34872 (the 2021 default). Verify the port against the current Rojo release if the connection fails. Sources: [B Ricey 2021-03 10:22](https://youtu.be/ulBM7UdHk_4?t=622), [B Ricey 2021-03 10:22](https://youtu.be/ulBM7UdHk_4?t=622). Newest source 2021-03-21.
- **Verify the Rojo build before live work** (single-mention): Run rojo build to output a .rbxlx, open it in Studio, and check the generated instance structure before using live sync. Sources: [B Ricey 2021-03 9:41](https://youtu.be/ulBM7UdHk_4?t=581), [B Ricey 2021-03 7:32](https://youtu.be/ulBM7UdHk_4?t=452). Newest source 2021-03-21.
- **Publish or save a backup before risky terrain edits** (multiple-creators): Publish the game before major terrain changes so you can revert to the saved version. In Team Create, after toggling Expanded Terrain, exit and wait about 15 seconds before reopening to avoid meshing or visual bugs. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/build-it-play-it-create-and-destroy/island-terrain), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/parts/custom-terrain-materials). Newest source 2026-10-28.
- **Write meaningful publish messages for audit and rollback** (single-mention): Revisions record the publish message, publishedBy, and per-key before and after values. Use a clear message on each publish so you can audit changes and roll back. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/configs). Newest source 2026-10-28.
- **Automate updates with Open Cloud, not legacy APIs** (one-creator-repeated): Use Open Cloud scripts (which are not synced to Studio) to update published games or restart servers. Avoid legacy Open Cloud APIs for production: they use cookie auth and may change without notice. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud). Newest source 2026-10-28.
- **Scope Open Cloud API keys to the endpoints you call** (one-creator-repeated): Create the API key with assets access permission plus Read/Write on the target game, depending on which endpoints you call. Only .fbx updates are supported for existing assets, and each update creates a new version. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets). Newest source 2026-10-28.
- **Pin plugin debugging workflow** (one-creator-repeated): Enable Plugin Debugging in Studio settings to use PluginDebugService for live debugging and reloading. After Save as Local Plugin, delete the original script and edit only the copy, so changes do not land on the wrong script. Store the last recording ID in attributes to cancel unfinished recordings on reload. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/plugins), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/plugins), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/plugins). Newest source 2026-10-28.
- **Publish reusable plugins to your inventory** (single-mention): Use Publish as Plugin to make a plugin available across all your projects. Use a 512x512 thumbnail. The plugin is open source and built on Open Cloud, so you can fork it for your own pipeline tooling. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/plugins), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/art/modeling/roblox-blender-plugin). Newest source 2026-10-28.
- **Use list_roblox_studios when several Studio windows are open** (single-mention): Call list_roblox_studios to get studio_id and place ID. Same-named instances are told apart by place ID. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/mcp). Newest source 2026-10-28.
- **Capture verbose logs when debugging command-line Studio** (single-mention): Studio pipes verbose logs to stdout when launched from the command line, which is more detailed than the Output window. Quote file paths containing spaces. Arguments are case-insensitive and use a double-dash prefix. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/cli), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/cli). Newest source 2026-10-28.
- **Re-save via Publish to keep the game linked** (single-mention): Re-save with File > Publish or Alt+P (Option+P on Mac). The game stays linked to your account so you can edit it from any machine. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/artist/test-and-save). Newest source 2026-10-28.
- **Restore missing Studio panels from the Window menu** (single-mention): If Explorer or Properties is missing, toggle it on from the Window menu. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/opening-the-template). Newest source 2026-10-28.
- **Keep recovery backups in mind with collaboration enabled** (single-mention): With collaboration on, Studio keeps recovery files for the last 3 failed save attempts. Check them if a save fails. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/place-files). Newest source 2026-10-28.
- **Check Blender version for the Validation Tool** (single-mention): The Validation Tool plugin requires Blender 3.5.1 or later. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/art/characters/validation-tool). Newest source 2026-10-28.
- **Commit a Git snapshot before risky changes** (multiple-creators): Commit with a clear message before refactors or risky edits, and push snapshots to GitHub. If the change goes wrong, roll back to the last commit. Check file history on GitHub to recover earlier versions of individual files. Sources: [Roblox DevForum 2018-08](https://devforum.roblox.com/t/guide-to-web-development/173780), [BloxianCode 2024-04 0:24](https://youtu.be/TmSZl5CcIKE?t=24), [BloxianCode 2024-04 3:53](https://youtu.be/TmSZl5CcIKE?t=233), [BloxianCode 2024-04 5:54](https://youtu.be/TmSZl5CcIKE?t=354). Newest source 2024-04-20.
- **Use GitHub Desktop with one repo per game** (multiple-creators): Create a repo per game with GitHub Desktop, set VS Code as its default editor, and open the synced project folder in VS Code beside Studio. Edit scripts in VS Code and commit and push from GitHub Desktop. Sources: [Roblox DevForum 2020-10](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182), [BloxianCode 2024-04 0:24](https://youtu.be/TmSZl5CcIKE?t=24), [BloxianCode 2024-04 2:47](https://youtu.be/TmSZl5CcIKE?t=167). Newest source 2024-04-20.
- **Start the Rojo server from VS Code before pressing Connect in Studio** (one-creator-repeated): Install the Rojo VS Code extension and choose 'MANAGE IT FOR ME' so it manages the Studio plugin. Start Rojo first, then Connect in Studio. If the plugin fails, read the Studio Output window for the cause. Sources: [Roblox DevForum 2020-10](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182), [Roblox DevForum 2020-10](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182). Newest source 2020-10-26.
- **Map $path to a dedicated child folder, not a service** (single-mention): In default.project.json, point $path at a src folder inside a dedicated child folder such as GameFiles. Mapping directly into a service like Workspace or ServerScriptService deletes any non-Rojo instances already in that service. Sources: [Roblox DevForum 2020-10](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182). Newest source 2020-10-26.
- **Use one Git branch per feature and rebase main in often** (one-creator-repeated): Make each feature its own branch, rebase main into feature branches frequently, then merge features into main. Frequent rebasing reduces merge conflicts. Sources: [Roblox DevForum 2023-10](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661), [Roblox DevForum 2023-10](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661). Newest source 2023-10-29.
- **Gate merges with StyLua --check and Selene in CI** (single-mention): Run StyLua --check and Selene in CI so style and lint failures block merges and releases. This stops unformatted or lint-failing Luau from reaching main. Sources: [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689). Newest source 2022-05-18.
- **Build packaged modules in CI instead of committing binaries** (one-creator-repeated): Keep pack.rbxm in .gitignore and build it in CI. Use a separate Rojo project file for packing, with init.lua as the module entry point. Use a Linking.lua file that requires Wally dependencies so they bundle into the .rbxm. Sources: [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689), [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689), [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689). Newest source 2022-05-18.
- **Store the Wally token as a CI secret and bump the version before pushing** (one-creator-repeated): Keep the Wally auth token in a GitHub secret (WALLY_AUTH_TOKEN) and avoid logging in or out after setup. Bump the version in wally.toml before pushing to main, since the version drives the Wally publish and the GitHub release tag. Sources: [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689), [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689). Newest source 2022-05-18.
- **Install third-party libraries through Wally and check they are maintained** (multiple-creators): Install packages with Wally (e.g. text21/rewind@1.0.0) or Sling via Wally, and Wally is the recommended route; RBXM downloads are the fallback. Before adopting a networking or other library, confirm it is still actively maintained. Sources: [Roblox DevForum 2025-12](https://devforum.roblox.com/t/archived-rewind-server-authoritative-hit-validation-custom-character-replication/4160622), [Roblox DevForum 2026-06](https://devforum.roblox.com/t/sling-a-modern-and-reactive-backpack-ui/4686535), [Roblox DevForum 2025-04](https://devforum.roblox.com/t/netray-high-performance-roblox-networking-library/3592849). Newest source 2026-06-17.
- **Upgrade dependencies deliberately; major versions may need rescripting** (multiple-creators): Keep plugin dependencies such as Text+ on the latest release, using GitHub release notes to review changes. Major upgrades can break integration: RaycastHitboxV3 to V4 may need rescripting. Test upgrades on a branch first. Sources: [Roblox DevForum 2021-09](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506), [Roblox DevForum 2025-03](https://devforum.roblox.com/t/text-custom-fonts-advanced-control/3521684). Newest source 2025-03-02.
- **Keep the 'local globals' marker intact in plugin-managed modules** (single-mention): Do not edit or remove the 'local globals' marker in an updating plugin's module. Removing its 's' stops the plugin from updating the module, so you silently stop receiving fixes from updates. Sources: [Suphi Kaner 2024-11 12:15](https://youtu.be/SVLFkdeh6c8?t=735). Newest source 2024-11-28.
- **Split parallel AI work by file and use one integrator** (one-creator-repeated): Current Roblox API and MCP connections are limited, so multiple AI sessions editing the same script will clash. Split work by file or feature, and have one integrator merge the results. Sources: [MonarchDev 2026-10 5:20](https://youtu.be/WA4RzzT39Dw?t=320), [MonarchDev 2026-10 5:20](https://youtu.be/WA4RzzT39Dw?t=320). Newest source 2026-10-26.
- **Check serialization before building tooling around a property** (single-mention): Use GetPropertiesOfClass to see whether a property is serialized (saved and loaded) and its security level. Confirm this before writing save or tooling logic that depends on it. Sources: [Roblox DevForum 2025-11](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522). Newest source 2025-11-18.
- **Import Roblox's openapi.json into Swagger or generate clients from it** (one-creator-repeated): Import openapi.json into Swagger Editor or Postman to test Open Cloud calls, or use OpenAPI Generator to produce a client in your language. The published spec is OpenAPI 3.0.4. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/openapi), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/openapi), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/openapi). Newest source 2026-10-28.
- **Do not rely on x-roblox-* vendor extensions long-term** (single-mention): The x-roblox-* extensions in the OpenAPI document are experimental and may change without notice. Prefer the official OpenAPI fields in any tooling you keep. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/openapi). Newest source 2026-10-28.
- **Set the correct Content-Type when uploading a place and verify the result** (one-creator-repeated): Send .rbxlx files as application/xml and .rbxl files as application/octet-stream. The API accepts only HTTPS. Check the versionNumber in the success response, then confirm the upload in Studio or on the Creator Dashboard. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-place-publishing), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-place-publishing). Newest source 2026-10-28.
- **Add version notes on every Save to Roblox** (one-creator-repeated): Use File > Save to Roblox with Notes (Ctrl+Alt+S, or Cmd+Option+S on Mac) to create searchable checkpoints. Publish notes are auto-drafted only from notes logged between publishes, so gaps produce no summary. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/version-history), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/version-history). Newest source 2026-10-28.
- **Add notes to older versions to make them searchable** (single-mention): Versions saved before notes were used lack the metadata fields and cannot be filtered. Add notes to them after the fact if you need to search or audit them. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/version-history). Newest source 2026-10-28.
- **Close other Studio instances of the game before a mass update** (single-mention): Before a mass update across places, close other Studio instances of the same game. An unsaved instance left open can overwrite your updates when it saves. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/assets/packages). Newest source 2026-10-28.
- **Enable auto-update on PackageLink** (single-mention): Turn on auto-update for PackageLink so edits to the package apply to every use automatically, instead of running 'update all' manually each time. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture). Newest source 2026-10-28.
- **Persist environment variables in your shell profile** (single-mention): Variables set in a terminal last only for that session. Add them to .zshrc or .bashrc to keep them across sessions when running CLI tooling or Open Cloud scripts. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-sample). Newest source 2026-10-28.
- **Drive AI-assisted MicroProfiler checks through Studio MCP** (single-mention): Connect your own AI agent via Studio MCP so it can run MicroProfiler analysis inside an agentic loop. This lets you measure how each change affects performance rather than guessing. Sources: [Roblox DevForum 2026-06](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417). Newest source 2026-06-26.
- **Track production on a project board with per-asset checklists** (single-mention): Use a board such as ClickUp, Trello or Jira with a pre-filled checklist card per asset, and Completed and Live columns, to see what is built and shipped. Sources: [Roblox DevForum 2020-05](https://devforum.roblox.com/t/game-design-theory-project-management-with-devops-analytics-and-pipelines-for-successful-games-and-productive-teams/568057). Newest source 2020-05-10.
- **Initialize Git on day one and commit early** (single-mention): Start the repo at project creation and commit small changes with descriptive messages so any change can be reverted. Confirm whether rojo init creates the repo and .gitignore before relying on it; no other source confirms this. Sources: [Dev Total 2022-11 12:58](https://youtu.be/0K-5sifYhxs?t=778). Newest source 2022-11-23.
- **Push the local Git repo to a remote for backup and sharing** (single-mention): Add GitHub as origin so work is backed up off-machine and teammates can clone it. Pairs with the one-repo-per-game rule. Sources: [Dev Total 2022-11 17:49](https://youtu.be/0K-5sifYhxs?t=1069). Newest source 2022-11-23.
- **Use GitLens for per-commit revert control** (single-mention): For finer-grained reverts across commits in VS Code, consider the GitLens extension. Optional convenience, not a requirement. Sources: [Dev Total 2022-11 20:34](https://youtu.be/0K-5sifYhxs?t=1234). Newest source 2022-11-23.
- **Install libraries under their canonical Wally package name** (one-creator-repeated): Use the upstream package name (e.g. eltab/fusion for Fusion, sleitnick/ scope for RbxUtil). Forks are often clones that stop receiving updates, so check the name points to the maintained upstream before installing. Sources: [Possible Panda 2025-11 1:36](https://youtu.be/3e406QQHt7o?t=96), [Possible Panda 2025-12 0:41](https://youtu.be/aSE2D4_TwoU?t=41). Newest source 2025-12-21.
- **Fall back to manual .rbxm import only when no package manager is used** (one-creator-repeated): Without Rojo, download the release .rbxm from the GitHub releases tab (e.g. QueryAuth) and drag it into ReplicatedStorage or Studio. This bypasses version tracking, so prefer Wally or Pesta when Rojo is in use. Sources: [Possible Panda 2025-11 1:36](https://youtu.be/3e406QQHt7o?t=96), [Possible Panda 2025-11 1:07](https://youtu.be/Xi--YI0Hk7M?t=67). Newest source 2025-11-09.
- **List Wally packages in default.project.json before rojo serve** (single-mention): Packages installed by Wally must be mapped in default.project.json so Rojo syncs them. Check the mapping exists before starting the server and testing. Sources: [Chase Higgins 2026-07 3:26](https://youtu.be/p86bt9ROQfk?t=206). Newest source 2026-07-08.
- **Restart Rojo and reconnect after a Wally install** (single-mention): After adding a package to wally.toml and running wally install, restart rojo serve and reconnect Studio so the source map picks up the new package. Sources: [Chase Higgins 2026-07 2:03](https://youtu.be/e9ElODFv8lo?t=123). Newest source 2026-07-24.
- **Regenerate the Luau LSP source map instead of restarting everything** (single-mention): When packages or new instances stop being referenced by the editor, regenerate the Luau LSP source map (Chase's config uses a space+LR binding) rather than restarting all tools. The keybinding is his own setup. Sources: [Chase Higgins 2026-07 33:51](https://youtu.be/e9ElODFv8lo?t=2031). Newest source 2026-07-24.
- **Use Luau LSP in non-VS Code editors such as Neovim** (single-mention): The Luau LSP plugin with Rojo gives autocomplete and types for Studio instances, including ones not saved to disk. Extends the 'match Studio features in external editors' rule to other editors. Sources: [Chase Higgins 2026-07 0:00](https://youtu.be/e9ElODFv8lo?t=0). Newest source 2026-07-24.
- **Use the Studio MCP server for external AI tools** (single-mention): Connect the Studio MCP server so external tools such as Cursor or Claude Code get the same Studio tools as the built-in Assistant. Use it instead of ad hoc scripts or copy-pasted instructions when an external agent needs to act on a Studio session. Sources: [Roblox 2026-04 39:20](https://youtu.be/8IcYpOl4Sdk?t=2360). Newest source 2026-04-16.
- **Build a plugin when a repeated pain point gets forum traction** (single-mention): If many users request the same workflow fix, build a plugin for it rather than waiting. Roblox's UGC Makers Toolbox was built after a thumbnail-fix request got 33 forum upvotes and Roblox did not ship it. Publish the result to your inventory so others can use it. Sources: [Roblox 2026-09 23:38](https://youtu.be/HXZRH-2zurk?t=1418). Newest source 2026-09-17.
- **Do not depend on Branch and Merge yet** (single-mention): Roblox's Branch and Merge (announced for early 2027) will add isolated Place branches with property- and script-line-level conflict resolution. Until it ships, keep using Git branches and the Git workflow rules for source, and keep the place binary out of Git. Sources: [Roblox DevForum 2026-09](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880). Newest source 2026-09-11.
- **Format and lint on save locally, not only in CI** (single-mention): Add a selene.toml to the project and enable StyLua format-on-save in your editor so bad practices and style drift are caught while you type. This complements the existing CI gate (StyLua --check and Selene) rather than replacing it. Sources: [Leif 2025-05 5:45](https://youtu.be/IJDg6tRJmHo?t=345). Newest source 2025-05-19.
- **Enable Luau LSP auto-import for services and modules** (single-mention): With auto-import on, the language server suggests services (for example GetService calls) and module names and writes the require/GetService lines for you. This cuts boilerplate. Confirm the setting is enabled in your editor's Luau extension. Sources: [Leif 2025-05 7:11](https://youtu.be/IJDg6tRJmHo?t=431). Newest source 2025-05-19.
- **Keep server-only Wally packages in the server dependency section** (single-mention): List shared libraries (for example ProfileService, Promise, Fusion) in the normal dependency section and server-only packages in the separate server dependency section. This keeps server-only code from being mixed into shared dependencies. Sources: [Leif 2025-05 8:38](https://youtu.be/IJDg6tRJmHo?t=518). Newest source 2025-05-19.
- **Run wally-package-types after every Wally install** (single-mention): Wally does not export Luau types automatically. Running wally-package-types after installing packages makes the exported types available to the editor for autocomplete and type checking. Sources: [Leif 2025-05 10:17](https://youtu.be/IJDg6tRJmHo?t=617). Newest source 2025-05-19.
- **Gitignore Wally output, server packages, and generated sourcemap** (single-mention): Ignore packages/, server packages, sourcemap.json and wally.lock so installed and generated files are not committed. Ignoring wally.lock is one creator's choice; some teams commit it for reproducible installs, so decide per team policy. Sources: [Leif 2025-05 11:55](https://youtu.be/IJDg6tRJmHo?t=715). Newest source 2025-05-19.
- **Don't rely on Studio autosave as your only safety net** (single-mention): An indie creator (self-reported, low-advice) reported a crash that erased a full day's scripts and staging work despite autosave. Save manually often and keep version control current, so a crash loses little work. This is a single-source tip and not official guidance. Sources: [janisjanis01 2024-03 4:11](https://youtu.be/IBswE0CyjA8?t=251). Newest source 2024-03-08.

## Checklist
- [ ] Pick one source-of-truth model: Script Sync (code only), Rojo (whole project on disk), or Drafts Mode (in Studio).
- [ ] Enable Drafts Mode in File > Experience Settings if collaborating in Studio (off by default).
- [ ] Install Rokit and declare Rojo, Wally and Lune versions in rokit.toml.
- [ ] Install the Roblox Luau LSP VS Code extension and the Luau Language Server Companion plugin together.
- [ ] Add selene (lint) and StyLua (format) to external projects; verify community tools before installing.
- [ ] Map folders to services in default.project.json using path; map Packages for Wally.
- [ ] Run rojo build to a .rbxlx and check the structure in Studio before live sync.
- [ ] Connect the Rojo Studio plugin on localhost:34872 after starting the server.
- [ ] Add a .gitignore that excludes .rbxlx before the first commit.
- [ ] Commit only after sync and MCP are verified.
- [ ] Use branches (production, alpha, beta) to isolate test code.
- [ ] Publish before major terrain edits; wait about 15 seconds after toggling Expanded Terrain in Team Create.
- [ ] Write meaningful publish messages for rollback and audit.
- [ ] Create Open Cloud keys with only the permissions the endpoints need.
- [ ] Replace legacy Open Cloud API calls with current Open Cloud endpoints for production.
- [ ] Use list_roblox_studios to target the right place when multiple Studios are open.
- [ ] Enable Plugin Debugging before developing plugins; edit only the local-plugin copy.
- [ ] Publish reusable plugins with a 512x512 thumbnail.
- [ ] Pass --verbose-style flags and capture stdout when debugging Studio from the command line.
- [ ] Before any risky edit, commit to Git with a clear message and push.
- [ ] Open the synced project in VS Code beside Studio and commit with GitHub Desktop.
- [ ] Start the Rojo server from VS Code before pressing Connect in Studio.
- [ ] If the Rojo plugin fails to connect, read the Studio Output window first.
- [ ] Map $path into a dedicated child folder, never directly into a service.
- [ ] Create a feature branch per feature, rebase main in often, then merge into main.
- [ ] Run StyLua --check and Selene in CI before allowing merges.
- [ ] Keep pack.rbxm in .gitignore and build it in CI.
- [ ] Store WALLY_AUTH_TOKEN as a GitHub secret.
- [ ] Bump the wally.toml version before pushing to main.
- [ ] Confirm a library is still maintained before adopting it.
- [ ] Test major dependency upgrades on a branch before merging.
- [ ] Keep the 'local globals' marker intact in plugin-managed modules.
- [ ] Use GetPropertiesOfClass to check serialization before building save tooling.
- [ ] Import openapi.json into Swagger or Postman to test Open Cloud calls.
- [ ] Avoid x-roblox-* extensions in long-lived tooling.
- [ ] Send .rbxlx as application/xml and .rbxl as application/octet-stream.
- [ ] Check versionNumber in the publish response and verify in Studio or the Creator Dashboard.
- [ ] Add notes on every Save to Roblox (Ctrl+Alt+S / Cmd+Option+S).
- [ ] Close other Studio instances of the game before a mass update.
- [ ] Turn on auto-update for PackageLink.
- [ ] Persist shell environment variables in .zshrc or .bashrc.
- [ ] Split parallel AI work by file and assign one integrator.
- [ ] Run git init at project start and make a first commit; decide explicitly whether the .rbxl is versioned (see disagreements).
- [ ] Push the repo to GitHub as origin for backup and team access.
- [ ] Install Rojo and Wally via Rokit, then run rojo init and wally init in a new project folder.
- [ ] Add the package to wally.toml and run wally install.
- [ ] Confirm the package is listed in default.project.json before running rojo serve.
- [ ] After a Wally install, restart rojo serve and reconnect Studio.
- [ ] Regenerate the Luau LSP source map after package or instance changes instead of restarting all tools.
- [ ] Verify a library's Wally name points to the maintained upstream, not a fork.
- [ ] Optional: run the editor and rojo serve in separate tmux panes to keep context.
- [ ] Optional: install GitLens for per-commit reverts in VS Code.
- [ ] Connect the Studio MCP server when an external AI tool (Cursor, Claude Code) needs Studio access.
- [ ] Log repeated forum requests for tooling gaps and track their upvote counts before deciding to build a plugin.
- [ ] Plan Branch and Merge adoption for after its early 2027 release, and verify its availability in Studio before changing workflow.
- [ ] Add selene.toml to the project root and turn on StyLua format-on-save in your editor.
- [ ] Enable Luau LSP auto-import in your editor so services and modules are suggested and require/GetService lines are written.
- [ ] Split Wally dependencies into a shared section and a server-only section.
- [ ] Run wally-package-types after installing Wally packages so their types are available.
- [ ] Add packages/, server packages, sourcemap.json to .gitignore; decide on wally.lock per team policy.
- [ ] Save manually at regular intervals in Studio and do not treat autosave as a backup.
- [ ] Commit to Git (or otherwise version the sources) at least daily so a crash cannot erase a full day of scripts or staging work.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| Rojo live-sync default server address | localhost:34872 | Default port used by the Studio Rojo plugin (2021 indie source; not contradicted by official items). | [B Ricey 2021-03 10:22](https://youtu.be/ulBM7UdHk_4?t=622), [B Ricey 2021-03 10:22](https://youtu.be/ulBM7UdHk_4?t=622) |
| Example Rojo version in rokit.toml | 7.6.1 | Example pin, not a recommendation of the latest release. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools) |
| Example Wally version in rokit.toml | 0.3.2 | Example pin. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools) |
| Example Lune version in rokit.toml | 0.10.4 | Example pin. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/external-tools) |
| Recovery backups kept with collaboration on | last 3 failed save attempts | Studio backs up failed saves as recovery files when collaboration is enabled. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/place-files) |
| Minimum Blender version for Validation Tool plugin | 3.5.1 | Plugin compatibility requirement. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/art/characters/validation-tool) |
| Plugin thumbnail size | 512x512 | Required for Publish as Plugin. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/plugins) |
| Team Create Expanded Terrain wait after toggling | about 15 seconds | Exit and wait before reopening to avoid meshing or visual bugs. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/parts/custom-terrain-materials) |
| Drafts Mode default state | disabled | Enable in File > Experience Settings. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/collaboration) |
| Open Cloud API key permissions | assets access + Read/Write on target game | Depends on endpoints called. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets) |
| Supported asset update format | .fbx only; each update creates a new version | Only .fbx content updates are supported for existing assets. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets) |
| Place file formats | .rbxl (compact, binary) vs .rbxlx (XML, readable, much larger) | Exports for version control or external tools. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/place-files), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/coding-harness) |
| Recording state on plugin reload | last recording ID stored in attributes | Used to cancel unfinished recordings. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/plugins) |
| Save-to-Roblox notes shortcut | Ctrl+Alt+S (Windows) / Cmd+Option+S (Mac) | Official; opens Save to Roblox with Notes. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/projects/version-history) |
| Open Cloud place upload Content-Type | application/xml for .rbxlx; application/octet-stream for .rbxl; HTTPS only | Official publish endpoint requirements. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-place-publishing) |
| OpenAPI spec version | 3.0.4 | Version of Roblox's published Cloud API openapi.json. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/openapi) |
| Rojo version pinned in 2022 guide | 7.0.0 (Rojo 7 plugin required; older plugin will not work) | 2022 snapshot; check current Rojo release before pinning. | [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) |
| Minimum Rust for installing Foreman via cargo | 1.53.0 | 2022 snapshot; Foreman is superseded by Rokit in existing guidance. | [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) |
| Foreman-pinned toolchain (2022) | Rojo 7.0.0, Wally 0.3.1, StyLua 0.13.1, Selene 0.9.2 | Example only; versions are outdated by 2026. | [Roblox DevForum 2022-05](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689) |
| Forum upvotes that led to UGC Makers Toolbox | 33 | Thumbnail-fix feature request Roblox did not ship; the team built a plugin instead. | [Roblox 2026-09 23:38](https://youtu.be/HXZRH-2zurk?t=1418) |
| Branch and Merge expected availability | early 2027 | Isolated Place branches with property- and script-line-level conflict resolution. Not available as of 2026-11-01. | [Roblox DevForum 2026-09](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880) |

## Where creators agree
- Both creators support using Git for version control of Roblox projects (T5441, T5442, T9030, T9782).
- Both creators support working with external editors and file-based projects via Rojo (T5443-T5447, T7968, T9930).
- Both creators point to separating test code from the main build via branches or equivalent isolation (T5442, T8646).
- Both creators recommend keeping the place in Git excluding the binary place file, or working from source files (T9030, T7968).
- Both creators treat the Rojo live-sync server and Studio plugin as the link between files and Studio (T5447, T7968).
- Commit to Git with clear messages before risky changes so you can roll back (DevForum 2018, BloxianCode 2024, DevForum 2020 via GitHub Desktop).
- Use feature branches and merge them into main, rebasing main in regularly (DevForum 2023, same post repeated).
- Parallel AI sessions editing the same scripts clash, so split work and keep one integrator (MonarchDev 2026).
- Rojo plus an external editor plus Git is the standard workflow (Last Level Studios T15765, Dev Total T15985).
- Wally is the preferred package path for Rojo projects (Possible Panda T16294, T16326, T16367; Chase Higgins T16505).

## Where creators disagree
- **Primary Rojo workflow tooling**
  - B Ricey (2021, indie): install the Rojo VS Code extension, enable plugin management, and run Rojo: Initialize from the command palette (T5443, T5445).
  - Roblox Creator Docs (2026, official): install Rojo via Rokit with pinned versions and use Luau LSP plus companion plugin, selene and StyLua (T7969, T8647, T7970). Official guidance supersedes the 2021 extension-centric steps.
- **Sync direction for Rojo**
  - B Ricey (2021, indie): Rojo is one-way; Studio edits do not flow back to files (T5448).
  - Roblox Creator Docs (2026, official): Rojo is file-system-first, which implies files are the source of truth, but no item states the direction explicitly (T7968). Treat the one-way claim as unverified for the current version.
- **Whether to keep only script mappings in default.project.json**
  - B Ricey (2021, indie): keep only script mappings to simplify setup (T5449).
  - Roblox Creator Docs (2026, official): map the Packages directory into the Rojo project so Wally packages sync (T7971). Both can apply; the official guidance adds the Packages mapping for dependencies.
- **Where to branch for feature work today**
  - T13818 (Roblox official, 2026-09): built-in Place Branch and Merge with property and script-line conflict resolution is planned for early 2027.
  - T11882 (DevForum indie, 2023-10): use Git feature branches now, rebasing main in often.
- **Whether to version the .rbxl place file in Git**
  - Dev Total (T15986, 2022-11): track the .rbxl in Git and commit after changes so binary place edits can be reverted.
  - Existing knowledge-file rule: keep the place binary out of Git and version the sources. The source date of this rule is not recorded; treat it as the default unless the user asks for binary history.

## Date context (what may be outdated)
- B Ricey's items are from 2021-03 and self-reported; they predate Rokit, Wally usage in official docs, Script Sync, Drafts Mode, the Luau LSP companion plugin and Open Cloud scripts. Treat them as historical unless re-verified.
- The Roblox Creator Docs items are from 2026-10 and are the most recent guidance. Where they conflict with 2021 indie advice, prefer the 2026 official guidance (for example, Rokit-managed tooling, Script Sync for code-only sync).
- The rokit.toml version numbers (Rojo 7.6.1, Wally 0.3.2, Lune 0.10.4) are examples from the 2026 docs, not the latest releases. Check current versions before pinning.
- Default port 34872 comes from the 2021 indie source; confirm against the current Rojo release.
- Legacy Open Cloud APIs are flagged as unsafe for production (T7427); current Open Cloud endpoints are the supported path.
- 2020 items (T10854–T10862) describe the early Rojo VS Code extension and Rojo plugin flow; verify current extension behavior before following them.
- 2022 items (T11373–T11379, N4367, N4368) pin Rojo 7.0.0, Wally 0.3.1, StyLua 0.13.1, Selene 0.9.2 and use Foreman; the existing rule prefers Rokit, so treat these pins as examples only.
- Official Save-to-Roblox notes (T15351–T15353, 2026-10) are newer guidance; older saves lack notes and cannot be filtered.
- Place Branch and Merge (T13818) is announced for early 2027 and was not available as of 2026-10-29; use Git branches until it ships.
- x-roblox-* OpenAPI extensions (T14306) are experimental as of 2026-10 and may change without notice.
- Indie Git/GitHub Desktop guides span 2020 to 2024; the Git workflow itself is stable, but UI steps may have changed.
- Dev Total's Git guidance (T15985-T15988, 2022-11) is the oldest here; the Rojo/Wally/Rokit workflow (2025-2026) is newer. Where tooling detail conflicts, prefer the 2025-2026 advice.
- Chase Higgins (2026-07) is the most recent source; his Neovim keybindings and tmux setup are personal config, not defaults.
- Possible Panda (2025-11/12) package install steps may change as packages update; re-check package names and release pages before use.
- All items are indie, self-reported; none are official Roblox ground truth.
- 2026-04: Studio MCP server is available for external tools (Cursor, Claude Code) to access the same Studio tools as built-in Assistant (T17613).
- 2026-09: Branch and Merge was announced for early 2027. It is not available as of 2026-11-01, so Git branching remains the workflow for now (T17677).
- 2026-09: UGC Makers Toolbox origin story (T17689) is a precedent for plugin-building from forum demand.
- Leif's tips are dated 2025-05; today is 2026-11-01. Re-verify current Wally, Selene, StyLua, Luau LSP and wally-package-types versions and config keys before applying these steps.
- Leif is an indie creator (self-reported), so treat these as community practice rather than official guidance.
- T18740 dates from 2024-03 and is an indie, self-reported tip. Studio autosave and crash-recovery behavior may have changed by 2026, so verify current behavior in the official Studio documentation before relying on specific autosave settings or intervals.

## Instructions for an agent using this file
- If the user asks about a new project, then recommend the 2026 official stack (Rokit, Rojo or Script Sync, Wally, Luau LSP plus companion, selene, StyLua) over the 2021 indie steps.
- If the user wants only scripts in Git with the place kept in Studio, then recommend Script Sync.
- If the user wants the whole project on disk as the source of truth, then recommend Rojo with default.project.json.
- If the user collaborates in Studio without external tools, then recommend enabling Drafts Mode and using Compare With Server and Merge From Server before committing.
- If the user installs Script Sync, then tell them to install both the Luau LSP VS Code extension and the Luau Language Server Companion plugin.
- If the user asks about the place file in Git, then recommend .rbxlx with a .gitignore excluding .rbxlx, and mention the .rbxl binary alternative.
- If the user asks about Open Cloud automation, then recommend Open Cloud scripts with narrowly scoped keys and warn against legacy cookie-auth APIs.
- If the user asks about version pinning, then recommend Rokit with a rokit.toml, bumping one tool at a time, and downgrading if problems appear.
- If the user asks about the 2021 Rojo one-way sync claim or port 34872, then label them as unverified indie claims and advise checking the current Rojo release.
- If the user asks about revenue, CCU or visit numbers, then say they are unverified indie self-reports (none appear in these items) and prefer official statements.
- If the user asks how to version a game, recommend Git plus commit and push before risky changes, and add Studio save notes for in-Studio checkpoints.
- If the user asks about rolling back, point them to Git file history and to the Studio version history with notes.
- If the user asks about Open Cloud publishing, check the Content-Type for .rbxl versus .rbxlx and verify versionNumber in the response.
- If the user asks about parallel AI work, recommend splitting by file or feature with one integrator.
- If the user asks about Place Branch and Merge, say it is announced for early 2027 and not yet available.
- If the user asks about pinning tools in CI, prefer Rokit per existing guidance; mention Foreman only as older 2022 practice.
- If the user asks about third-party libraries, recommend installing via Wally and checking maintenance status first.
- If the user asks about x-roblox-* fields, warn they are experimental and prefer official OpenAPI fields.
- If a source is a 2020–2022 indie post, check whether its Rojo, Wally, or plugin versions still apply before advising.
- If the user asks about CI for Luau packages, run StyLua --check and Selene and keep packed .rbxm files out of Git.
- If a project uses Rojo and a Wally package, check default.project.json mapping, then restart rojo serve and reconnect Studio after wally install before testing.
- If a library is requested, verify the Wally package name against the upstream repo and avoid forks that are not maintained.
- If Rojo is not in use, the manual .rbxm import is the fallback; mention that it has no version tracking.
- If the user asks whether to commit the .rbxl, flag the disagreement and default to the existing rule (sources in Git, place binary out) unless the user asks for binary history.
- Do not state that rojo init creates a Git repo or .gitignore without verifying it; the only source is T15985.
- Prefer 2025-2026 package and LSP workflow advice over 2022 Git advice when they conflict in tooling details.
- If an external AI agent needs Studio access, then point it at the Studio MCP server rather than building a custom bridge.
- If a Roblox feature is announced but not yet released (for example Branch and Merge), then keep the current Git-based workflow and do not assume the feature exists.
- If a forum request has strong community demand and Roblox has not shipped it, then consider building and publishing a plugin.
- If the user asks for shared and server-only libraries, place server-only Wally packages in the server dependency section.
- If Wally packages are installed but types are missing in autocomplete, run wally-package-types and check the editor again.
- If the user is committing a Wally project to Git, add generated folders and sourcemap.json to .gitignore, and ask before ignoring wally.lock.
- If the user asks to set up linting or formatting, add selene.toml and StyLua format-on-save locally in addition to the CI gate.
- When citing these 2025-05 indie tips, mark them as self-reported and recommend checking current tool versions.
- If advising on data-loss risk in Studio, recommend manual saves and version control together; do not present autosave as sufficient protection.
- If a user reports a crash that lost work, check whether recent sources (sources from 2026) are available that describe current recovery behavior before stating how recovery works.

## Not covered here (research elsewhere)
- Argon is not mentioned in any item; research it separately if the user asks.
- No items give exact install steps, CLI commands or config files for Rokit, Wally, Rojo 7.x or Lune beyond the example versions.
- No items cover CI/build pipelines (GitHub Actions, automated publish) or Git LFS for large binaries.
- No items describe the Drafts Mode merge workflow in detail beyond Compare With Server and Merge From Server.
- No items give Open Cloud endpoint lists, rate limits or request examples.
- No items cover Luau LSP configuration settings or the Studio MCP server setup beyond list_roblox_studios.
- No items cover Git branch naming or merge strategy beyond production, alpha and beta.
- No items cover publishing plugins to the Creator Marketplace review process or plugin security rules.
- GitHub Actions specifics (workflow files, runners, caching) for Rojo or Wally builds are not covered.
- Git LFS or other strategies for storing .rbxl binaries are not covered.
- Current 2026 versions of Rojo, Wally, StyLua, Selene, and Luau LSP are not given; the numbers here are 2022-era.
- Open Cloud rate limits, error codes, and retry behavior are not covered.
- Details of Place Branch and Merge (workflow, permissions, UI) are not yet available.
- Studio MCP setup, auth, and tool list are not covered beyond the single MicroProfiler mention.
- Sling's current feature set and install docs are not covered.
- Limits on Save-to-Roblox notes (length, searchability) are not covered.
- How Rojo, Wally, and Git interact with Studio Drafts or collaboration is not covered.
- No official Rojo, Wally, or Luau LSP documentation is cited; verify rojo init behavior and default.project.json syntax on the Rojo docs.
- No guidance on Git LFS or other handling for large .rbxl binaries.
- No CI or automated build content in these new items; cross-check with existing CI rules.
- No version pinning or compatibility details for Fusion, Vide, RbxUtil, or QueryAuth.
- Pesta is mentioned as a package option but not explained.
- No Windows or PowerShell-specific setup steps for Rokit, Wally, or Rojo.
- Luau LSP source map regeneration is described only as a keybinding in one creator's config; the underlying command is not documented.
- No details on Studio MCP setup, configuration, or supported tools beyond the summary in T17613.
- No details on Branch and Merge's workflow, UI, or merge tooling; only the announced capabilities in T17677.
- No details on how UGC Makers Toolbox was built or distributed; only the origin story in T17689.
- No official Wally, Selene, StyLua or wally-package-types documentation was provided to verify these tips.
- No selene.toml or StyLua configuration examples; exact rule sets and formatting options are not covered.
- No Luau LSP auto-import settings or version compatibility details.
- No exact wally-package-types install and usage steps, or the exact wally.toml syntax for the server section.
- Policy on committing wally.lock (commit vs ignore) is unverified and only one creator addresses it.
- No CI configuration examples for the lint and format gate.
- No information on Studio autosave interval, location of autosave files, or recovery steps after a crash.
- No official (OFFICIAL) source cited on autosave reliability; the only evidence is one indie self-reported report.
- Does not cover whether Roblox Cloud/Team Create saves provide any additional recovery protection.

## Quotes (near-verbatim)
- "Merge features into main, rebase main into features." ([Roblox DevForum 2023-10 ](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661))
- "you cannot have multiple sessions working on the same thing at the same time simply because they'll clash one another" ([MonarchDev 2026-10 5:20](https://youtu.be/WA4RzzT39Dw?t=320))

## Appendix: every extracted tip on this topic

- 2018-08-31 Roblox DevForum [page](https://devforum.roblox.com/t/guide-to-web-development/173780): Commit to Git with a message before risky changes so you can roll back in an emergency; use nodemon to auto-restart on save.
- 2020-03-01 Last Level Studios [25:51](https://youtu.be/4fz4fpJLUSQ?t=1551): Use Rojo to write code in a normal editor (VS Code) and sync to Studio, enabling Git and external tooling.
- 2020-05-10 Roblox DevForum [page](https://devforum.roblox.com/t/game-design-theory-project-management-with-devops-analytics-and-pipelines-for-successful-games-and-productive-teams/568057): Track production with a project board (ClickUp, Trello or Jira) using pre-filled checklist cards per asset, with Completed and Live columns.
- 2020-10-26 Roblox DevForum [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182): Install GitHub Desktop, create a repo per game, and set VSCode as its default editor to commit and push changes easily.
- 2020-10-26 Roblox DevForum [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182): Install the Rojo VSCode extension, then use 'rojo welcome screen' > 'MANAGE IT FOR ME' so the extension manages the Studio plugin automatically.
- 2020-10-26 Roblox DevForum [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182): Start Rojo in VSCode before pressing Connect in Studio; if the plugin fails, check the Studio output.
- 2020-10-26 Roblox DevForum [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182): In default.project.json, map $path to a src folder under a dedicated child folder (e.g. GameFiles); mapping directly into a service deletes any non-Rojo instances there.
- 2020-10-26 Roblox DevForum [page](https://devforum.roblox.com/t/setup-rojo-fast-the-easy-way-to-setup-rojo-with-git-support/838182): Use GitLens, Prettier and lua-indent in VSCode to match Studio's formatting and see commit history per line.
- 2021-03-21 B Ricey [0:41](https://youtu.be/ulBM7UdHk_4?t=41): Use GitHub Desktop instead of raw Git CLI; it wraps Git with a GUI while keeping its backup and branching features.
- 2021-03-21 B Ricey [0:07](https://youtu.be/ulBM7UdHk_4?t=7): Use Git branches (production, alpha, beta) so test code can be shared without breaking the main build.
- 2021-03-21 B Ricey [5:11](https://youtu.be/ulBM7UdHk_4?t=311): Install the Rojo VS Code extension and enable plugin management so it can auto-manage the Studio plugin.
- 2021-03-21 B Ricey [7:32](https://youtu.be/ulBM7UdHk_4?t=452): Create project folders in a stable location like Documents, then open them in VS Code via File > Open Folder.
- 2021-03-21 B Ricey [8:14](https://youtu.be/ulBM7UdHk_4?t=494): Run 'Rojo: Initialize' from the VS Code command palette (Ctrl+Shift+P) to generate boilerplate project files.
- 2021-03-21 B Ricey [9:41](https://youtu.be/ulBM7UdHk_4?t=581): Use 'rojo build' to output a .rbxlx place file, then open it in Studio to verify the generated structure.
- 2021-03-21 B Ricey [10:22](https://youtu.be/ulBM7UdHk_4?t=622): Run 'Rojo: Start Server' and connect from the Studio Rojo plugin using default localhost:34872 settings for live sync.
- 2021-03-21 B Ricey [11:44](https://youtu.be/ulBM7UdHk_4?t=704): Remember Rojo syncs one way only: edits in VS Code replicate to Studio, but Studio edits do not flow back to files.
- 2021-03-21 B Ricey [12:05](https://youtu.be/ulBM7UdHk_4?t=725): Map folders to Roblox services in default.project.json using the path property; keep only the script mappings to simplify setup.
- 2021-03-21 B Ricey [13:26](https://youtu.be/ulBM7UdHk_4?t=806): Name files by suffix: .lua becomes ModuleScript, .server.lua becomes Script, .client.lua becomes LocalScript.
- 2021-09-07 Roblox DevForum [page](https://devforum.roblox.com/t/open-source-lock-on-combat-in-3d/1458506): The template uses RaycastHitboxV3 by Swordphin123; upgrading to V4 may need rescripting.
- 2022-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689): Use Foreman to pin tool versions (Rojo 7.0.0, Wally 0.3.1, StyLua 0.13.1, Selene 0.9.2) in foreman.toml so all contributors share the same toolchain.
- 2022-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689): Keep separate Rojo project files: one for testing in Studio, one for packing a .rbxm, so packages can be tested and distributed without Wally.
- 2022-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689): Make the module entry point init.lua and use a Linking.lua file that requires Wally dependencies so they get bundled into the .rbxm.
- 2022-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689): Add pack.rbxm to .gitignore and build it in CI rather than committing binaries.
- 2022-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689): Run StyLua --check and Selene in CI so style and lint failures block merges and releases.
- 2022-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689): Store the Wally auth token as a GitHub repository secret (WALLY_AUTH_TOKEN) and never log in or out of Wally after setup.
- 2022-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/creating-a-proper-open-source-project-with-devops/1796689): Bump the version in wally.toml before pushing to main; the version string drives the Wally publish and GitHub release tag.
- 2022-11-23 Dev Total [12:58](https://youtu.be/0K-5sifYhxs?t=778): Use Git from day one: Rojo init creates a local repo and .gitignore; commit early with descriptive messages to track and revert changes.
- 2022-11-23 Dev Total [19:13](https://youtu.be/0K-5sifYhxs?t=1153): Track the .rbxl place file in Git too; commit it after changes so you can revert binary place edits.
- 2022-11-23 Dev Total [17:49](https://youtu.be/0K-5sifYhxs?t=1069): Push the local repo to GitHub (origin) to back up work and share it with team members.
- 2022-11-23 Dev Total [20:34](https://youtu.be/0K-5sifYhxs?t=1234): For fine-grained revert control across commits, consider the GitLens VS Code extension.
- 2023-10-29 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661): Use Git with Rojo and Wally; the Luau LSP VS Code extension gives the same typechecking as Studio.
- 2023-10-29 Roblox DevForum [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661): Make each feature its own branch; rebase main into feature branches often and merge features into main, to avoid merge conflicts.
- 2024-03-08 janisjanis01 [4:11](https://youtu.be/IBswE0CyjA8?t=251): Don't rely on Studio autosave. Save manually often, or use version control, since a crash erased a day's scripts and stage.
- 2024-04-20 BloxianCode [0:24](https://youtu.be/TmSZl5CcIKE?t=24): Use GitHub Desktop to set up a repo for your Studio project so every change is tracked and can be rolled back.
- 2024-04-20 BloxianCode [2:47](https://youtu.be/TmSZl5CcIKE?t=167): Open the synced project folder in VS Code alongside Roblox Studio to edit scripts while keeping the project under Git.
- 2024-04-20 BloxianCode [3:53](https://youtu.be/TmSZl5CcIKE?t=233): Commit and push changes via GitHub Desktop to save a snapshot of your game to GitHub.
- 2024-04-20 BloxianCode [5:54](https://youtu.be/TmSZl5CcIKE?t=354): Check file history on GitHub to review past changes and recover earlier versions of files.
- 2024-11-28 Suphi Kaner [12:15](https://youtu.be/SVLFkdeh6c8?t=735): Keep the 'local globals' marker intact; removing its 's' stops the plugin updating the module, so you won't get fixes from updates.
- 2025-03-02 Roblox DevForum [page](https://devforum.roblox.com/t/text-custom-fonts-advanced-control/3521684): Keep Text+ on the latest release; the author recommends updating to get new features and fixes, with releases listed on GitHub.
- 2025-04-04 Roblox DevForum [page](https://devforum.roblox.com/t/netray-high-performance-roblox-networking-library/3592849): Check whether a third-party networking library is still maintained before adopting it; this one is no longer actively maintained.
- 2025-05-19 Leif [2:18](https://youtu.be/IJDg6tRJmHo?t=138): Install Rokit as a toolchain manager to pin and install Rojo, Wally and other CLI tools per project.
- 2025-05-19 Leif [3:28](https://youtu.be/IJDg6tRJmHo?t=208): Use Rojo with VS Code and the Rojo Studio plugin to live-sync files between your editor and Roblox Studio.
- 2025-05-19 Leif [5:45](https://youtu.be/IJDg6tRJmHo?t=345): Add Selene (linter) with a selene.toml file and StyLua (formatter) with format-on-save to catch bad practices early.
- 2025-05-19 Leif [7:11](https://youtu.be/IJDg6tRJmHo?t=431): Enable auto-import in the Luau Language Server so it suggests services and modules and writes require/GetService lines automatically.
- 2025-05-19 Leif [8:38](https://youtu.be/IJDg6tRJmHo?t=518): Manage shared libraries (e.g. ProfileService, Promise, Fusion) with Wally; put server-only packages in a separate server dependency section.
- 2025-05-19 Leif [10:17](https://youtu.be/IJDg6tRJmHo?t=617): Run wally-package-types after installing so exported types are available, since Wally doesn't export types automatically.
- 2025-05-19 Leif [11:55](https://youtu.be/IJDg6tRJmHo?t=715): Add packages/, server packages, sourcemap.json and wally.lock to .gitignore so generated and installed files aren't committed.
- 2025-05-19 Leif [14:01](https://youtu.be/IJDg6tRJmHo?t=841): Create a feature branch for each feature (e.g. a tank class) and merge via pull request to keep main stable.
- 2025-07-07 SimTek Game Development [0:40](https://youtu.be/DcLba0yVLHs?t=40): Set a model's Humanoid DisplayDistanceType to None to hide overhead name labels that clutter NPC speech bubbles.
- 2025-11-04 Possible Panda [1:36](https://youtu.be/3e406QQHt7o?t=96): Install Fusion via Wally using eltab/fusion; other forks are clones that won't be updated. Without Rojo, drag fusion.rbxm into Studio.
- 2025-11-09 Possible Panda [1:07](https://youtu.be/Xi--YI0Hk7M?t=67): Install QueryAuth by downloading query author.rbxm from the GitHub releases tab and dragging it into ReplicatedStorage, or use Wally/Pesta.
- 2025-11-18 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522): Use GetPropertiesOfClass to check whether a property is serialized (saved/loaded) and its security level before building tooling around it.
- 2025-12-18 Roblox DevForum [page](https://devforum.roblox.com/t/archived-rewind-server-authoritative-hit-validation-custom-character-replication/4160622): Install via Wally (text21/rewind@1.0.0) or download the RBXM release; Wally is the recommended route.
- 2025-12-21 Possible Panda [0:41](https://youtu.be/aSE2D4_TwoU?t=41): Install RbxUtil modules by copying init.lua into a modules folder, or via Wally using the sleitnick/ package name.
- 2026-04-16 Roblox [39:20](https://youtu.be/8IcYpOl4Sdk?t=2360): Use the Studio MCP server so external tools like Cursor or Claude Code get the same Studio tools as built-in Assistant.
- 2026-06-17 Roblox DevForum [page](https://devforum.roblox.com/t/sling-a-modern-and-reactive-backpack-ui/4686535): Install Sling via Wally or GitHub Releases; follow the docs' installation guide.
- 2026-06-26 Roblox DevForum [page](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417): Connect your own AI agent via Studio MCP to run MicroProfiler analysis inside agentic loops and measure how each change affects performance.
- 2026-07-08 Chase Higgins [3:26](https://youtu.be/p86bt9ROQfk?t=206): Install Vide via Wally (search on wally.run), then ensure packages are listed in default.project.json before running rojo serve.
- 2026-07-24 Chase Higgins [0:00](https://youtu.be/e9ElODFv8lo?t=0): Use the Luau LSP plugin with Rojo in Neovim to get autocomplete and types for Studio instances, including ones not saved to disk.
- 2026-07-24 Chase Higgins [2:03](https://youtu.be/e9ElODFv8lo?t=123): After adding a Wally package in wally.toml and running wally install, restart Rojo serve and reconnect so the source map picks up the package.
- 2026-07-24 Chase Higgins [33:51](https://youtu.be/e9ElODFv8lo?t=2031): Regenerate the Luau LSP source map (space LR in his config) when packages or new instances stop being referenced, instead of restarting everything.
- 2026-07-24 Chase Higgins [36:10](https://youtu.be/e9ElODFv8lo?t=2170): Run Neovim in one tmux pane and Rojo serve in another so you can switch between them without losing context.
- 2026-07-24 Chase Higgins [38:30](https://youtu.be/e9ElODFv8lo?t=2310): Install Rojo and Wally via Rokit, then run rojo init and wally init in a new project folder.
- 2026-09-11 Roblox DevForum [page](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880): Branch and Merge (early 2027) lets isolated Place branches be merged with property and script-line conflict resolution.
- 2026-09-11 Roblox DevForum [page](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880): Branch and Merge (early 2027) lets teams build in isolated Place branches and merge with property- and script-line-level conflict resolution.
- 2026-09-17 Roblox [23:38](https://youtu.be/HXZRH-2zurk?t=1418): Build a plugin for a repeated pain point. UGC Makers Toolbox was built after 33 forum upvotes for a thumbnail-fix feature Roblox didn't ship.
- 2026-09-25 Roblox DevForum [page](https://devforum.roblox.com/t/weekly-recap-september-21-25-2026/4894110): Integrations hitting thumbnail endpoints should check for an error object before reading response.imageUri; genuine outages still return 503.
- 2026-10-26 MonarchDev [5:20](https://youtu.be/WA4RzzT39Dw?t=320): Current Roblox API and MCP connections are limited, so parallel AI work on shared scripts clashes. Split work by file or feature with one integrator.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/collaboration): Enable Drafts Mode (File > Experience Settings) to edit scripts locally and commit to a shared repository, similar to source control; it is disabled by default.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/collaboration): In Drafts, use Compare With Server and Merge From Server to resolve conflicts before committing collaborator changes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud): Avoid legacy Open Cloud APIs for production: they use cookie auth, may change without notice, and have minimal stability guarantees.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/art/modeling/roblox-blender-plugin): The plugin is open-source and built on Open Cloud API; fork or extend it for your own pipeline tooling.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/plugins): Enable Plugin Debugging Enabled in Studio settings to get PluginDebugService for live debugging and reloading plugin code.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/plugins): Delete the original script after 'Save as Local Plugin' and edit only the copy in PluginDebugService to avoid applying changes to the wrong script.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/plugins): Store the last recording identifier in attributes so an unfinished recording can be cancelled when the plugin reloads.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/plugins): Publish plugins to your inventory via Publish as Plugin to make them available across all your projects; use a 512x512 thumbnail.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/mcp): Use list_roblox_studios to get studio_id and place ID when multiple Studio windows are open; same-named instances are told apart by place ID.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/reference/openapi): Import Roblox's openapi.json into Swagger Editor or Postman to test Cloud API calls and speed up development.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/reference/openapi): Use OpenAPI Generator with openapi.json to generate client libraries in your preferred programming language.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/reference/openapi): Don't rely on x-roblox-* vendor extensions long-term; they are experimental and may change without notice in favour of official OpenAPI fields.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/beyond-the-dark/building-architecture): Enable auto-update on PackageLink so package edits apply to all uses without manual 'update all'.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/external-tools): Run Rojo (file system-first) to keep game instances as local files, synced to Studio via the Rojo plugin, enabling Git and external editors.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/external-tools): Test new tool versions before adopting: bump the version in the .toml, upgrade with Rokit, and downgrade if problems appear.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/external-tools): Add linters (selene), formatters (StyLua) and Luau Language Server to match Studio script editor capabilities in an external editor.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/external-tools): Use Wally for reproducible package management, then map the Packages directory into the Rojo project so it syncs to Roblox.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/external-tools): Use Open Cloud scripts (not synced to Studio) to update published games or restart servers.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/configs): Write a meaningful publish message; revisions record message, publishedBy and per-key before/after values for auditing and rollback.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/overview): Share custom tab layouts with your team by sharing their .json files from the local CustomRibbonTabs folder, then use Reload custom tabs.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/parts/custom-terrain-materials): In Team Create, editing terrain may cause meshing or visual bugs; after toggling Expanded Terrain, exit and wait about 15 seconds before reopening.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/sync): Use Script Sync for code in version control while keeping the rest of the place in Studio; use Rojo if the whole project should live on disk as source of truth.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/sync): Install both the Roblox Luau LSP VS Code extension and the Luau Language Server Companion Studio plugin so language features work correctly with Script Sync.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting/sync): Use selene for linting and StyLua for formatting alongside Script Sync (community-maintained; verify source before installing).
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/assets/packages): Close other Studio instances of the game's places before a mass update to prevent an unsaved instance from overwriting your updates.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/place-files): Export places to .rbxl or .rbxlx for version control or external tools; .rbxl is compact but binary, .rbxlx is XML and human-readable but much larger.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/battle-royale-series/project-setup): Organise parts into folders (Lobby, Arena, SpawnLocations) to keep the project manageable.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/cli): Studio pipes verbose logs to stdout when launched from the command line, which is more detailed than the Output window; capture it when debugging.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/cli): Quote file paths containing spaces; arguments are case-insensitive and use a double-dash prefix.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-create-and-destroy/island-terrain): Publish the game before major terrain edits so you can revert to the saved version if the changes turn out badly.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/coding-harness): Keep the place as .rbxlx in a Git repo with a .gitignore excluding .rbxlx, and commit once sync and MCP are verified.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/auth/oauth2-sample): Environment variables set in a terminal only last for that session; add them to .zshrc or .bashrc to persist them.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing): Create an API key with universe-places access permission and Write operation scoped to the specific game before calling the publish endpoint.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing): Send the place file as Content-Type application/xml for .rbxlx or application/octet-stream for .rbxl; the API only supports HTTPS requests.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing): Check the returned versionNumber in the success response and verify the upload in Studio or on the Creator Dashboard.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-assets): Create the API key with assets access permission plus Read/Write on the target game, depending on which endpoints you call.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-assets): Only .fbx content updates are supported for existing assets; each update creates a new version.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/accelerated-workflows): Use Rojo and Git to build and version control Roblox projects via the file system.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/scripting): Many developers use an external text editor and version control with Script Sync or third-party tools instead of the built-in editor.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/version-history): Add version notes to every save (File > Save to Roblox with Notes, Ctrl+Alt+S / Cmd+Option+S) to create searchable development checkpoints.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/version-history): Write version notes consistently; publish notes are auto-drafted only from notes logged between publishes, so gaps produce no summary.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/version-history): Add notes to pre-existing versions to make them searchable; older versions lack the metadata fields and cannot be filtered.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/artist/test-and-save): Re-save later via File > Publish or Alt+P (Option+P on Mac); the game stays linked to your account for editing anywhere.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/opening-the-template): If Explorer or Properties are missing, toggle them on from the Window menu.

Index: [[README]] | Master: [[master-playbook]]
