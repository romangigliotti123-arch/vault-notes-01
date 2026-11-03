---
title: Ai And Tools
topic: ai-and-tools
theme: Studio & Scripting
sources: 184 videos
creators: [#7Phantom, BloxxedDev, BubuTheDev, Business of Creators, ByteBlox, CallMeDogey, Crusherfire, Deconstructor of Fun, Dev Total, Duckable, GamesBeat, GnomeCode, GuideRealm, JustDucksey, LovJak, Matt The Method, MonarchDev, MoseyTube, Naavik Gaming Podcast, Platform Aeronaut (transcript), PocketGamer.biz, Possible Panda, RoBuilder, Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, Roblox Investor Relations, Roblox Newsroom, RoyalDev, SimTek Game Development, Suphi Kaner, TheDankDeveloper, TheNexusAvenger, Tizzy, VuukStudios, Xaiyne, janisjanis01, kra_DeZ, mats-dept2, rasdev, studio rook., tef, waveshine]
source_dates: 2017-03-30 to 2026-10-30
tags: [roblox, knowledge-base, ai-and-tools]
---

# Ai And Tools

_AI-assisted development (vibe coding), Studio plugins, external tools._

Evidence base: 457 extracted items from 184 videos by #7Phantom, BloxxedDev, BubuTheDev, Business of Creators, ByteBlox, CallMeDogey, Crusherfire, Deconstructor of Fun, Dev Total, Duckable, GamesBeat, GnomeCode, GuideRealm, JustDucksey, LovJak, Matt The Method, MonarchDev, MoseyTube, Naavik Gaming Podcast, Platform Aeronaut (transcript), PocketGamer.biz, Possible Panda, RoBuilder, Roblox, Roblox Creator Docs, Roblox Creators, Roblox DevForum, Roblox Investor Relations, Roblox Newsroom, RoyalDev, SimTek Game Development, Suphi Kaner, TheDankDeveloper, TheNexusAvenger, Tizzy, VuukStudios, Xaiyne, janisjanis01, kra_DeZ, mats-dept2, rasdev, studio rook., tef, waveshine (2017-03-30 to 2026-10-30). Roblox changes quickly: check the date on each source and see Date context below.

## Overview
Roblox AI tooling has moved from single-prompt generation toward supervised agents. Studio Assistant plans multi-step work from a to-do list you can edit before it runs, and completed steps serve as revert points. Build (prompt-based creation) has published about 9,000 games, most by people who never used Studio. Generation tools (meshes, procedural models, scenes, NPC behavior) accept reference images, part-level naming and tags, and returned outputs remain editable. Roblox's own skills (Scene Analysis) and runtime bridges let agents verify behavior in a running game. Quotas, concurrency limits and several features (unified agent permissions, NPC Dynamic Behavior, texture tool) are announced for late 2026 and should be verified before relying on them. Playbooks, skill files and API keys are the path to unattended pipelines, which need tight scoping.

## Rules and findings
- **Prompt one mechanic or feature at a time** (multiple-creators): Ask for a core mechanic first, test in Studio, then add the next feature (e.g. plots, then economy UI, then shop). Small increments worked better than one massive prompt in Lemonade and Claude builds. Add reference screenshots where useful. Sources: [TheDankDeveloper 2026-01 0:00](https://youtu.be/3y7EU49_d7s?t=0), [TheDankDeveloper 2026-04 0:00](https://youtu.be/Ufr0SVq-o98?t=0), [TheDankDeveloper 2026-10 0:41](https://youtu.be/Mftq7v8nAcs?t=41), [TheDankDeveloper 2026-01 4:38](https://youtu.be/BYhhm9o3H_E?t=278), [TheDankDeveloper 2026-10 0:00](https://youtu.be/Mftq7v8nAcs?t=0). Newest source 2026-10-21.
- **Playtest after every AI prompt** (multiple-creators): AI-generated scripts often introduce errors that break earlier features (Claude's build broke after adding combat). Testing after each step catches breakage early. Sources: [TheDankDeveloper 2026-01 6:18](https://youtu.be/3y7EU49_d7s?t=378), [TheDankDeveloper 2026-04 0:00](https://youtu.be/Ufr0SVq-o98?t=0). Newest source 2026-04-19.
- **Paste errors back to the AI to fix them** (multiple-creators): Expect generated scripts to error (e.g. forgotten anchoring, infinite yield blocking UI). Paste the error into the AI and ask for a fix; this worked on the first try in the cited cases. Expect to debug and build UI yourself with some tools (ChatGPT). Sources: [TheDankDeveloper 2025-09 2:44](https://youtu.be/pRfzkw-wHgA?t=164), [TheDankDeveloper 2026-05 1:21](https://youtu.be/uYuiCJrAcmI?t=81), [TheDankDeveloper 2026-01 0:00](https://youtu.be/BYhhm9o3H_E?t=0). Newest source 2026-05-25.
- **Write long, specific prompts with concrete numbers** (multiple-creators): Avoid one-liners like 'make a game'. Describe mechanics concretely, e.g. 'enemy follows the player and deals 10 damage on contact', or a pathfinding zombie that chases and damages. Specificity improves output. Sources: [MoseyTube 2026-05 2:44](https://youtu.be/400F-3qXoHE?t=164), [MoseyTube 2026-05 2:44](https://youtu.be/400F-3qXoHE?t=164), [TheDankDeveloper 2026-05 4:51](https://youtu.be/uYuiCJrAcmI?t=291). Newest source 2026-05-25.
- **Use a master prompt for a full foundation only with a strong model setting** (one-creator-repeated): One long master prompt covering map, progression, customers, monetisation and data saving generated a game foundation in one pass (~1 hour build) at ultra effort. Use medium effort for simple checks like connection tests. This conflicts with the one-feature-at-a-time advice. Sources: [MoseyTube 2026-07 2:26](https://youtu.be/PstV93OnOdM?t=146), [MoseyTube 2026-07 1:50](https://youtu.be/PstV93OnOdM?t=110), [MoseyTube 2026-07 2:26](https://youtu.be/PstV93OnOdM?t=146). Newest source 2026-07-19.
- **Connect Claude/Codex to Studio via MCP** (multiple-creators): In Studio open Assistant settings, then Manage MCP servers, and enable Studio as an MCP server. Confirm the green indicator shows a client connected. Use quick connect for Codex CLI after installing the Codex desktop app and signing in with ChatGPT. Claude Code can also connect via MCP before building. MoseyTube claims ~80% scripting time saved (unverified). Sources: [MoseyTube 2026-04 2:04](https://youtu.be/sFr7htxsnR4?t=124), [MoseyTube 2026-07 0:49](https://youtu.be/PstV93OnOdM?t=49), [MoseyTube 2026-07 1:29](https://youtu.be/PstV93OnOdM?t=89), [TheDankDeveloper 2026-10 0:40](https://youtu.be/4ojmHWn_rxY?t=40), [MoseyTube 2026-04 2:04](https://youtu.be/sFr7htxsnR4?t=124). Newest source 2026-10-13.
- **Use Lemonade-style AI plugins to script from plain English** (one-creator-repeated): Lemonade scripts features (group/like gating, cast-and-reel mechanic, billboard coin GUI) from prompts. ChatGPT can write the prompts. Prebuilt prompt cards (e.g. survival card gave health/hunger bars) are starting points to tweak. Sources: [TheDankDeveloper 2025-08 2:46](https://youtu.be/OauiTUkK7og?t=166), [TheDankDeveloper 2025-09 0:18](https://youtu.be/pRfzkw-wHgA?t=18), [TheDankDeveloper 2025-09 3:25](https://youtu.be/pRfzkw-wHgA?t=205), [TheDankDeveloper 2025-12 1:10](https://youtu.be/D6Ej1CgiWOc?t=70), [TheDankDeveloper 2026-01 4:38](https://youtu.be/BYhhm9o3H_E?t=278). Newest source 2026-05-25.
- **Check AI-generated objects land in the correct parent/folder** (single-mention): A rainbow background only worked after moving it out of a folder. Sources: [TheDankDeveloper 2025-08 6:05](https://youtu.be/OauiTUkK7og?t=365). Newest source 2025-08-20.
- **Add a health system before testing combat** (single-mention): Without visible health values you cannot tell whether hit detection works. Sources: [TheDankDeveloper 2026-01 5:21](https://youtu.be/3y7EU49_d7s?t=321). Newest source 2026-01-27.
- **Use a full-screen screenshot as a reference, not a crop** (single-mention): Cropped references produced oversized, misplaced buttons; full screenshots let the AI size buttons and HUD correctly. Sources: [TheDankDeveloper 2026-10 1:22](https://youtu.be/Mftq7v8nAcs?t=82), [TheDankDeveloper 2026-10 0:41](https://youtu.be/Mftq7v8nAcs?t=41). Newest source 2026-10-21.
- **Start from template/generator plugins** (multiple-creators): Simulator/clicker generator plugins give a scripted, playable base (CallMeDogey built one with no coding); then reskin art, UI and maps yourself. Sources: [TheDankDeveloper 2024-07 0:40](https://youtu.be/maRjVb1NAYc?t=40), [CallMeDogey 2025-01 3:14](https://youtu.be/USJC5l_wpuY?t=194). Newest source 2025-01-15.
- **Use Studio's built-in AI assistant and generation tools** (one-creator-repeated): Assistant handles tedious work: scattering thousands of trees, generating meshes from prompts, converting Blender avatars, code completion. 3D and texture generation make meshes and PBR textures; segmented meshes ease adding behavior. Prompt to Avatar (due by end of year) makes compliant R15+ rigs with layered clothing; keep artistic control. Sources: [Roblox 2025-09 36:50](https://youtu.be/6iB5__RCQDc?t=2210), [Roblox 2026-09 29:19](https://youtu.be/53dj7AG3foA?t=1759), [Roblox 2026-09 42:31](https://youtu.be/53dj7AG3foA?t=2551), [Roblox 2025-09 3:22](https://youtu.be/3h25HUtBHFk?t=202), [Roblox 2025-09 3:22](https://youtu.be/3h25HUtBHFk?t=202). Newest source 2026-09-17.
- **Use AI for concept and prototype validation** (multiple-creators): Have ChatGPT generate a game concept then a detailed prompt for the scripting tool. Build a prototype with AI and free models before hiring a developer; duplicate the backup, tweak feel with AI, and batch changes into one request to the programmer. Sources: [TheDankDeveloper 2025-09 0:18](https://youtu.be/pRfzkw-wHgA?t=18), [Tizzy 2026-05 8:55](https://youtu.be/7tYPvXYlif8?t=535), [Tizzy 2026-05 15:45](https://youtu.be/7tYPvXYlif8?t=945). Newest source 2026-05-26.
- **Use AI image tools for UI and thumbnails, then fix details** (multiple-creators): Forge UI icon mode with a short prompt (e.g. 'X close button, cartoony style'), refine with follow-ups; Magic Edit restyles from a screenshot; generate variants (4 per click) and pick the best. RoVis works best with a reference image (icons fine without). Fix missing text in Photopea. Sources: [TheDankDeveloper 2026-04 0:43](https://youtu.be/i5sldtdF8m0?t=43), [TheDankDeveloper 2026-04 4:03](https://youtu.be/i5sldtdF8m0?t=243), [TheDankDeveloper 2026-04 4:03](https://youtu.be/i5sldtdF8m0?t=243), [CallMeDogey 2026-04 4:06](https://youtu.be/SjjPGduApZU?t=246), [CallMeDogey 2026-04 5:29](https://youtu.be/SjjPGduApZU?t=329). Newest source 2026-04-25.
- **Understand the code; use AI as a tutor** (multiple-creators): waveshine says use AI to explain errors/lines and read documentation, not generate whole systems you don't understand. kra_DeZ speeds up with AI but says to understand the code. Sources: [waveshine 2026-07 7:10](https://youtu.be/hQ1lrFLEF1c?t=430), [kra_DeZ 2026-09 6:59](https://youtu.be/cJ-YzHHhQs8?t=419). Newest source 2026-09-06.
- **Budget AI usage limits** (multiple-creators): MoseyTube moved from Claude Pro to Max 5x ($100/mo) because limits stalled sessions. TheDankDeveloper hit 73% then 100% of the Pro session limit in one build; a simple prompt used ~1%, a full 3-prompt game ~13%. Sources: [MoseyTube 2026-08 1:23](https://youtu.be/5zz5ao0zV_Y?t=83), [MoseyTube 2026-08 1:23](https://youtu.be/5zz5ao0zV_Y?t=83), [TheDankDeveloper 2026-10 4:50](https://youtu.be/Mftq7v8nAcs?t=290), [TheDankDeveloper 2026-10 4:50](https://youtu.be/Mftq7v8nAcs?t=290), [TheDankDeveloper 2026-10 0:40](https://youtu.be/4ojmHWn_rxY?t=40). Newest source 2026-10-21.
- **Constrain in-game LLM output** (single-mention): Put an LLM check in front of generated objects to reject off-theme items. Have NPC LLMs reply in JSON with a fixed action set so scripts can map responses to game actions. Sources: [Roblox 2025-09 31:36](https://youtu.be/3h25HUtBHFk?t=1896), [Roblox 2025-09 8:11](https://youtu.be/3h25HUtBHFk?t=491). Newest source 2025-09-26.
- **Mind copyright and player sentiment toward AI** (multiple-creators): AI-generated output likely can't be copyrighted; human modifications and arrangements can be. One generated-UGC system draws only from its own catalog for quality; players wanted creation help but not AI use. Sources: [Roblox 2025-09 5:03](https://youtu.be/2HotST5mF3A?t=303), [Roblox 2026-10 17:41](https://youtu.be/gCp4zzjjJ14?t=1061), [Roblox 2026-10 17:41](https://youtu.be/gCp4zzjjJ14?t=1061). Newest source 2026-10-12.
- **Plan UI for localization and text expansion** (one-creator-repeated): Leave ~30-50% extra space for long strings and 2-3x for short ones. Automatic translation breaks on typewriter text, incomplete strings and changed source text; use it as a fallback and move to localization APIs for maintained games (2018 advice). Sources: [Roblox 2018-07 13:24](https://youtu.be/qoWMP-AFT08?t=804), [Roblox 2018-07 19:26](https://youtu.be/qoWMP-AFT08?t=1166), [Roblox 2018-07 13:24](https://youtu.be/qoWMP-AFT08?t=804). Newest source 2018-07-24.
- **Use helper tools for color, sun and shadows** (single-mention): Adobe color tools find contrasting pairs; Celestial Body Dragger moves sun/moon by mouse; bake shadows in 3D Coat, ZBrush, Maya or Blender, or use real-time lighting where it changes. Sources: [Roblox Creators 2023-04 5:37](https://youtu.be/syQcaeRqqc4?t=337), [Roblox 2024-09 22:10](https://youtu.be/vWx8UTxsi0A?t=1330), [Roblox 2018-07 34:04](https://youtu.be/u0SxwDxFQB8?t=2044). Newest source 2024-09-23.
- **Batch tedious Studio edits through Assistant actions** (multiple-creators): Use Assistant actions for bulk chores instead of manual work: placing hundreds of trees, renaming, grouping into folders, selecting by property criteria, and bulk property changes. Demo benchmark: 77 trees placed from one prompt in about 20 seconds. Verify count and parent folder afterward. Sources: [Roblox 2024-09 1:42](https://youtu.be/XrxUy51NsvI?t=102), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/get-started/tools), [Roblox 2024-09 9:45](https://youtu.be/XrxUy51NsvI?t=585). Newest source 2026-10-28.
- **Write pseudo-code-style prompts for Assistant scripts** (single-mention): Structure Assistant prompts as detailed pseudo-code (steps, conditions, variable names) rather than a loose sentence. The speaker says a ~10-line prompt can yield ~100 lines of script. Review the generated line count and logic before running it. Sources: [Roblox 2024-09 9:45](https://youtu.be/XrxUy51NsvI?t=585). Newest source 2024-09-23.
- **Expect re-rolling from generative tools and narrow scope** (single-mention): Generative tools can feel like a slot machine with little control, so expect repeated regenerations. Narrow each request (smaller area, one asset) to reduce re-rolls. Roblox said direct region selection and image inputs were coming to add control; check whether they have shipped. Sources: [Roblox 2024-09 4:51](https://youtu.be/XrxUy51NsvI?t=291). Newest source 2024-09-23.
- **Start AI tool experiments early and expect failures** (one-creator-repeated): Adopt AI tools early and play with them, including open models. Roblox's guidance is to start early and fail early, because teams must fully embrace AI before workflows actually change. Cheap early experiments are preferred over waiting for a polished workflow. Sources: [Roblox 2024-09 27:17](https://youtu.be/XrxUy51NsvI?t=1637), [Roblox 2024-09 27:17](https://youtu.be/XrxUy51NsvI?t=1637). Newest source 2024-09-23.
- **Use Studio code explanation and autocomplete when debugging** (single-mention): When debugging, ask Studio to explain the code before editing it. The speaker says code explanation is among the highest-rated Studio AI features. Use autocomplete for routine code entry. Pair this with the rule to understand code before accepting changes. Sources: [Roblox 2024-09 33:37](https://youtu.be/XrxUy51NsvI?t=2017). Newest source 2024-09-23.
- **Tune onboarding values with Configs and Experiments, not hardcoded numbers** (single-mention): Put tunable onboarding values (timings, step counts, reward amounts) into Roblox Configs and Experiments so they can be changed live. Hardcoding them forces a republish for every tweak. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/game-design/onboarding-techniques). Newest source 2026-10-28.
- **Answer the AI interaction question by in-game player access, not by dev process** (single-mention): When a platform form asks about AI, answer based on whether players can interact with generative AI inside the experience. Using AI only during development does not by itself make the answer yes. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/production/promotion/content-maturity). Newest source 2026-10-28.
- **Back up the place before any AI edit or conversion** (multiple-creators): AI tools modify the live project directly. Use File > Publish to Roblox As before Assistant or MCP edits, and before the rbx-convert-to-streaming skill (typically 20-30 min and about 200,000 tokens). Sources: [GuideRealm 2026-10 2:24](https://youtu.be/ltbZzXRrDF8?t=144), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/workspace/streaming/techniques), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/workspace/streaming/techniques), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/workspace/streaming/techniques). Newest source 2026-10-28.
- **Prefer the built-in Studio MCP server over custom bridges** (multiple-creators): Enable it via Assistant > ... > Manage MCP Servers and turn on needed features under File > Beta Features. Update Studio first, confirm the green connected-client indicator, then ask the client to name the open project. Supersedes the 2025 third-party bridge steps. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/accelerated-workflows), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/accelerated-workflows), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/mcp), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/mcp), [GuideRealm 2026-10 1:11](https://youtu.be/ltbZzXRrDF8?t=71). Newest source 2026-10-28.
- **Connect only trusted MCP clients** (single-mention): MCP clients can read and modify content in your open Roblox places, so only connect clients you trust. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/mcp). Newest source 2026-10-28.
- **Run one agent on a custom MCP server at a time** (single-mention): A custom MCP server accepts only one agent. When you hit usage limits on Claude, switch to Codex (or the reverse) rather than running both. Sources: [Crusherfire 2025-11 12:17](https://youtu.be/6kcWSMJFaS4?t=737). Newest source 2025-11-22.
- **Follow exact steps if you must use a third-party MCP bridge** (one-creator-repeated): Run npm install, npm run build, then npm start (listens on localhost port 3002). Register with claude mcp add (stdio) and verify with /mcp. Copy the .rbxm plugin into Studio's Plugins folder, restart Studio, click Connect. Legacy path; prefer the built-in server. Sources: [Crusherfire 2025-11 0:00](https://youtu.be/6kcWSMJFaS4?t=0), [Crusherfire 2025-11 6:16](https://youtu.be/6kcWSMJFaS4?t=376), [Crusherfire 2025-11 8:39](https://youtu.be/6kcWSMJFaS4?t=519), [Crusherfire 2025-11 10:12](https://youtu.be/6kcWSMJFaS4?t=612). Newest source 2025-11-22.
- **Use Script Sync for external editors; use MCP for reach** (one-creator-repeated): Enable Script Sync (File > Beta Features) and select the top-level project folder, not a subfolder, so services match by name. Script Sync cannot reach StarterGui or StarterPack; use the MCP server for those. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/coding-harness), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/coding-harness), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/coding-harness). Newest source 2026-10-28.
- **Plan first, review, then Build** (one-creator-repeated): For complex requests, run /plan or switch to Plan mode, read the Markdown plan, then click Build. Plans never auto-execute. Build world and core gameplay first; add scripts and secondary systems later. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/build-with-assistant), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide). Newest source 2026-10-28.
- **Click Continue when Assistant hits max output** (single-mention): Long builds can hit the output limit. Click Continue so Assistant resumes where it stopped rather than restarting the build. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/build-with-assistant). Newest source 2026-10-28.
- **Reference selected objects and separate steps with ### delimiters** (one-creator-repeated): Select objects in Studio so prompts can modify, duplicate, or extend them. In multi-step prompts, separate code from questions with ### delimiters to get clearer step-by-step explanations. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/prompt-engineering), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/prompt-engineering). Newest source 2026-10-28.
- **Select a Part before /generate_mesh** (one-creator-repeated): The selected Part's size and location form the bounding box, keeping output in that space. Default max triangle count is 10,000 (lower gives lower poly). Each request takes text or a reference image, not both. Expect 4 preview images. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide). Newest source 2026-10-28.
- **Let players regenerate the 2D preview before 3D** (single-mention): In player-facing AI generation, let players repeat the 2D preview until satisfied. The 3D generation is the costly step, so regeneration at 2D is cheaper. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/avatar/avatar-generation). Newest source 2026-10-28.
- **Write descriptive names and comments to improve Code Assist; verify output** (one-creator-repeated): Use descriptive script, part and function names, and comments stating inputs and outputs. Break code into named functions, which give better hints than anonymous ones. Always test: Code Assist can produce wrong code or suggest Lua or older APIs instead of Luau. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/script-editor), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/script-editor), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/script-editor), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/script-editor), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/script-editor). Newest source 2026-10-28.
- **Build terrain by hand, fine-tune AI output in Studio tools** (one-creator-repeated): Brush strokes and material edits are hard to reproduce with AI, so sculpt terrain directly. Use Assistant to generate or modify content, then adjust positions, materials, lighting and UI with built-in tools. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-an-environment-with-terrain), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/build-with-assistant). Newest source 2026-10-28.
- **Ask for pointers, type AI code by hand, read every chunk** (one-creator-repeated): Request directions ('follow the breadcrumbs') instead of full code, read every AI chunk until you understand it, and type suggested code out rather than pasting. Overuse erodes the struggle that builds skill. Sources: [Duckable 2026-09 18:20](https://youtu.be/MBRNAqkDEFA?t=1100), [Duckable 2026-09 19:02](https://youtu.be/MBRNAqkDEFA?t=1142), [Duckable 2026-09 19:02](https://youtu.be/MBRNAqkDEFA?t=1142), [Duckable 2026-09 19:44](https://youtu.be/MBRNAqkDEFA?t=1184), [Duckable 2026-08 21:21](https://youtu.be/Cc7HT3uNjeQ?t=1281). Newest source 2026-09-12.
- **Turn style rules into reusable AI skills, then refactor old code** (single-mention): Write architecture and code-style rules as reusable AI skills, then have AI refactor older code to match. Speaker reports cutting a few weeks of work to one or two days. Low-advice; verify with tests. Sources: [Crusherfire 2026-10 3:52](https://youtu.be/4n7thZAAF-E?t=232). Newest source 2026-10-24.
- **Match effort level to task size** (single-mention): Use extra high effort for complex whole-game generation (GuideRealm draft: 7 min 18 s with Codex). Keep medium for simple queries. Sources: [GuideRealm 2026-10 3:45](https://youtu.be/ltbZzXRrDF8?t=225), [GuideRealm 2026-10 4:12](https://youtu.be/ltbZzXRrDF8?t=252). Newest source 2026-10-17.
- **Give a master prompt that covers every system** (single-mention): List map, systems, persistence, offline earnings and mobile controls in the master prompt. Speaker says the more detail, the better the AI build. Sources: [GuideRealm 2026-10 2:24](https://youtu.be/ltbZzXRrDF8?t=144). Newest source 2026-10-17.
- **Give reference images alongside prompts for visual matching** (single-mention): Attach reference images with text prompts so the AI has visuals to match. Speaker reports output much closer to the intended look. Low-advice. Sources: [tef 2026-10 1:35](https://youtu.be/OfObWnrucRY?t=95). Newest source 2026-10-23.
- **Generate icons and thumbnails at fixed sizes; add text in an editor** (one-creator-repeated): Use ChatGPT for the cheapest, fastest route. Specify 512x512 for icons and 1920x1080 for thumbnails. Image models handle text poorly, so add text in an editor afterward. Sources: [rasdev 2026-07 4:05](https://youtu.be/_Tt-l7EMEHE?t=245), [rasdev 2026-07 4:45](https://youtu.be/_Tt-l7EMEHE?t=285). Newest source 2026-07-27.
- **Use AI art for placeholders; hire animators; clean AI meshes in Blender** (one-creator-repeated): AI icons and tool art cover placeholders fast, though quality varies. Hire animators for custom animation. Meshie.ai generates 3D meshes quickly; clean up in Blender. Sources: [janisjanis01 2025-09 3:30](https://youtu.be/YVKHlrlWn-k?t=210), [janisjanis01 2026-06 3:16](https://youtu.be/CltiB53QTHw?t=196). Newest source 2026-06-06.
- **Validate avatar assets before importing** (one-creator-repeated): Run the Blender Validation Tool before importing avatar items, and the Blender Calisthenics Tool to check skinning data. The Roblox Blender plugin uploads models straight from modeling software. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/avatar/resources), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/art/overview-dcc). Newest source 2026-10-28.
- **Capture animations first, then refine keyframes** (one-creator-repeated): Capture tools generate animations in minutes; refine keyframes manually. Face Animation Editor: Avatar tab > Clip Editor > Face; Ctrl+Z/Ctrl+Y to undo/redo; right-click slider > Reset Selected. Graph > Create Animate script scaffolds Animate, RunClient and RunServer. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/animation/capture), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/art/characters/facial-animation/moods), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/animation/graph-editor). Newest source 2026-10-28.
- **Start Open Cloud with an API key, test in Postman, then scope down** (one-creator-repeated): API keys are the easiest start; use OAuth 2.0 for user-authorized apps. Test endpoints in Postman with the OpenAPI descriptions first. Send the key in the x-api-key header and grant only needed scopes (for ads: ad.campaign:read, ad.campaign:write, ad.billing:read). Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/advertising), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud-services/secrets). Newest source 2026-10-28.
- **Upload assets with the Assets API and poll the operation** (one-creator-repeated): The Assets API uploads or updates an asset in one HTTP request instead of manual Studio imports; it is beta. Limit is 20 MB and one asset per call. Poll Get Operation with the returned ID; read the status field to see why an upload failed. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets). Newest source 2026-10-28.
- **Tune live values and send live messages from external tools** (one-creator-repeated): Use Google Sheets with Apps Script and Open Cloud to change item prices or colours without republishing. Use Open Cloud to send live messages from external tools instead of manual Studio scripts. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/instance), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-messaging). Newest source 2026-10-28.
- **Validate every client-sent value on the server** (single-mention): Assume the client is hostile. Never trust client-sent data; validate everything in RemoteEvent and RemoteFunction handlers on the server. Sources: [Roblox DevForum 2022-01](https://devforum.roblox.com/t/how-exploits-work-and-how-to-combat-them/1627229). Newest source 2022-01-14.
- **Filter all LLM-generated text before showing players** (single-mention): Run generated text through TextService:FilterStringAsync() before display; this is required for LLM NPC dialogue. Pair with output constraints. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/accelerated-workflows). Newest source 2026-10-28.
- **Use FastCast Redux for raycast bullets with drop** (single-mention): For bullets that need gravity drop, FastCast Redux is recommended; gravity values of -100 to -500 work well. Dated 2020; confirm the module is still maintained. Sources: [Roblox DevForum 2020-05](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791). Newest source 2020-05-18.
- **Keep plugins and addons on latest versions; check rig warnings** (single-mention): Incompatible versions cause errors; an error mentioning object.name = partnames[-index] means the addon is outdated. Check the rig shows no warnings in the exporter and loads in the default Roblox Animation Editor for clearer errors. Dated 2017. Sources: [Roblox DevForum 2017-03](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729), [Roblox DevForum 2017-03](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729). Newest source 2017-03-30.
- **Use Assistant for routine setup; hand-build the player-facing core** (multiple-creators): Delegate folders, models, parts, boilerplate event handlers, leaderboards, RemoteFunctions and deterministic bulk placement at exact CFrames. Build terrain, colors, lighting, gameplay design, map and UI yourself; players can spot AI UI and leave. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/core), [VuukStudios 2026-10 10:49](https://youtu.be/0ENzqNB_EUo?t=649), [VuukStudios 2026-10 10:49](https://youtu.be/0ENzqNB_EUo?t=649), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets), [MonarchDev 2026-09 4:47](https://youtu.be/LD7LGP10dRc?t=287). Newest source 2026-10-28.
- **Open Assistant inside Studio and rename objects before prompting** (one-creator-repeated): The Studio version can reference your game's objects and scripts, unlike the web version. Rename parts (e.g. GlitterPart) so Assistant targets the right one, then check generated objects land in the correct parent. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant). Newest source 2026-10-28.
- **Rephrase requests instead of blind retries** (one-creator-repeated): Small wording changes can yield a new script, code added to an existing script, or just a ParticleEmitter. If results are wrong, rephrase and try again rather than editing blindly. Re-running an identical texture prompt gives only slightly different results. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator). Newest source 2026-10-28.
- **Undo AI changes the right way** (single-mention): Ctrl+Z reverts non-script changes made by Assistant. For generated scripts, delete the script in Explorer instead. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant). Newest source 2026-10-28.
- **Name the problem and the target look in every visual fix** (multiple-creators): Replace 'make this better' with a named problem and target, e.g. 'too low-saturation, make it cartoonish and highly saturated'. Include color, trigger and timing details; fewer details produce unpredictable results. Sources: [MonarchDev 2026-10 2:26](https://youtu.be/WA4RzzT39Dw?t=146), [MonarchDev 2026-10 2:26](https://youtu.be/WA4RzzT39Dw?t=146), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant). Newest source 2026-10-28.
- **Write texture prompts with material, color and pattern; set Preview to Manual if needed** (one-creator-repeated): 'make it out of wood' gives inconsistent results; name material, color, pattern and distinctive features. Avoid prompts that change mesh geometry, reference the current texture or other objects, or describe reflectivity or transparency. Image prompts yield a style guide, not an exact template. If Automatic picks a poor angle, set Preview orientation to Manual and orbit the mesh. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator). Newest source 2026-10-28.
- **Use /generate_procedural_model with a text prompt or reference image** (single-mention): Run it from Assistant or the Studio MCP server. Reference images improve accuracy, so attach one when the target look is specific. Sources: [Roblox DevForum 2026-04](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056). Newest source 2026-04-23.
- **Refresh stale context in long AI sessions** (multiple-creators): Quality degrades in long sessions (around 900k of a 1M-token context in one example). Compress the session or start fresh. Periodically paste current scripts, folder structure and Explorer layout and say 'continue from here' to avoid mismatched suggestions. Sources: [MonarchDev 2026-10 4:48](https://youtu.be/WA4RzzT39Dw?t=288), [MonarchDev 2026-10 4:48](https://youtu.be/WA4RzzT39Dw?t=288), [Matt The Method 2026-08 2:19](https://youtu.be/1mYF-cWJPmQ?t=139). Newest source 2026-10-26.
- **Limit AI code to work you can verify; avoid it for paid client work** (one-creator-repeated): Use AI to speed up your own game. Avoid it for paid client commissions where originality matters. Use AI for code only if you already understand scripting, since without that knowledge it produces inaccurate code. Sources: [VuukStudios 2026-07 10:06](https://youtu.be/Bltv__PoNcA?t=606), [VuukStudios 2026-08 12:18](https://youtu.be/m7015JSIrpw?t=738). Newest source 2026-08-26.
- **Use AI for roadmaps and explanations, not full scripts** (multiple-creators): Ask AI for a full roadmap and goals, and to explain code you don't understand. Write or review scripts yourself. Learn basic Luau so you can check samples against your use case before accepting them. Sources: [VuukStudios 2025-11 12:25](https://youtu.be/U4nduRcszJ4?t=745), [VuukStudios 2025-11 12:25](https://youtu.be/U4nduRcszJ4?t=745), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/education/lesson-plans/build-an-obby-lesson). Newest source 2026-10-28.
- **Use MCP to review your project, not to generate the whole game** (multiple-creators): Connect Claude or GPT to Studio via MCP to scan code and infrastructure for improvements. Don't expect a complete game from one prompt; build in stages with frequent, detailed instructions. Sources: [VuukStudios 2026-10 12:51](https://youtu.be/0ENzqNB_EUo?t=771), [MonarchDev 2026-10 0:00](https://youtu.be/WA4RzzT39Dw?t=0). Newest source 2026-10-26.
- **Connect an external LLM to Assistant through Manage API Keys** (single-mention): Get an API key from the provider, open Assistant, click the three-dot menu, choose Manage API Keys, select provider, enter the key, then pick the model in the Model drop-down. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/mcp). Newest source 2026-10-28.
- **Use built-in rbx skills for debugging, profiling and tests** (one-creator-repeated): rbx-debug inspects call stacks and variables at runtime instead of print statements. rbx-perf-profiling uses MicroProfiler traces for lag, frame-time spikes and memory growth. rbx-unit-test tests ModuleScript contracts with stubs in Play. Pause a spike and ask Assistant to analyse the capture. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/performance-optimization/microprofiler). Newest source 2026-10-28.
- **Duplicate Roblox skills instead of editing; write precise skill descriptions** (one-creator-repeated): Roblox-authored skills are read-only, and editing the original auto-disables it, so duplicate first. Duplicates get no upstream updates; re-duplicate for the latest version. Don't use the reserved rbx- prefix. Assistant loads a skill from its description alone, so make it specific; keep name and description on one line each. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/skills). Newest source 2026-10-28.
- **Use the Command Bar for quick Luau outside scripts** (multiple-creators): Press Ctrl+9 (Cmd+9 on Mac) to run Luau. Enable Multi-line Command Bar in File > Beta Features; it starts at 2 lines and grows to 10. Recent history keeps the last 10 commands. During the beta, run require("@rbx/AvatarAbilities") after each Studio reload to force-load autocomplete. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/overview), [Roblox DevForum 2026-02](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/overview), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/overview). Newest source 2026-10-28.
- **Build plugin widgets with correct parenting, theme and input handling** (one-creator-repeated): Call CreateDockWidgetPluginGui only from the command bar or a plugin script. Parent every widget GuiObject to the DockWidgetPluginGui. Sync colors with settings().Studio.Theme:GetColor() and reconnect on Studio.ThemeChanged. UserInputService does not work in widgets; use a transparent full-screen Frame's InputBegan. For drag and drop, use Plugin:StartDrag() and handle PluginDragDropped. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/build-studio-widgets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/build-studio-widgets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/build-studio-widgets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/build-studio-widgets), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/build-studio-widgets). Newest source 2026-10-28.
- **Use ReflectionService for API inspection plugins** (single-mention): Build plugins that analyze new engine API releases, or Studio plugins that change instance classes faster than manual edits. Sources: [Roblox DevForum 2025-11](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522). Newest source 2025-11-18.
- **Scope Open Cloud API keys and confirm analytics access** (single-mention): Grant only the needed Access Permissions scopes. The key owner must also have analytics access, or requests return 403. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/error-reporting). Newest source 2026-10-28.
- **Use OAuth 2.0 for third-party tools instead of shared credentials** (one-creator-repeated): OAuth lets third-party tools access your games without your password, and you choose permitted resources. Register the app for a client ID and secret, select the openid scope so the token includes an ID token, and go through review for more user quota. Authorizing users must be 13+; developers must be ID-verified. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-overview), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-overview), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-overview), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-overview), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-overview). Newest source 2026-10-28.
- **Review endpoint risk before using Try it out** (one-creator-repeated): Read the endpoint's functionality and impact first, especially Medium and High risk endpoints that modify data. Critical endpoints have Try it out disabled. High-risk endpoints, typically DELETE, show two confirmation dialogs per session. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/risk-levels), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/risk-levels), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/risk-levels), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/risk-levels). Newest source 2026-10-28.
- **Automate publishing from CI after integration tests pass** (single-mention): Call the Place Publishing API from CI, such as a GitHub Action, after integration tests pass, instead of publishing manually from Studio. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-place-publishing). Newest source 2026-10-28.
- **Trigger Age Check on a deliberate player action** (single-mention): Call Player:PromptAgeCheck() on a deliberate player action, not on spawn, and check Player.AgeChecked. Sources: [Roblox DevForum 2026-04](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091). Newest source 2026-04-30.
- **Enable Voice Chat before using speech-to-text** (single-mention): Turn on Voice Chat in Experience Settings > Communication to use the speech-to-text API. Sources: [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/chat/voice-chat). Newest source 2026-10-28.
- **Don't treat ML or client-side checks as anti-cheat** (one-creator-repeated): One creator states plainly that a simple ML check is not a proper anti-cheat. For a simple obby exploit check, invisible checkpoints are more practical than a model. Where ML fits, use real player-generated data; the author's synthetic-noise model reached about 85% test accuracy and real data is much better. Validate on the server. Sources: [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460), [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460), [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460), [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460). Newest source 2024-01-07.
- **Use vetted open-source networking and utility modules instead of rebuilding** (multiple-creators): Packet (free toolbox model) replaces RemoteEvents and RemoteFunctions to cut network data. BridgeNet2, TopbarPlus and ProfileService should be used, not rebuilt; keep only one copy in the project. A RemoteFunction wrapper adds timeouts and nil-return handling. Wrapper libraries cut HTTP boilerplate. Sources: [Suphi Kaner 2025-03 0:17](https://youtu.be/WoIElUdj64A?t=17), [Roblox DevForum 2023-11](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585), [Suphi Kaner 2024-01 0:00](https://youtu.be/A14qFAyFYhQ?t=0), [Roblox DevForum 2019-09](https://devforum.roblox.com/t/roblox-requests-simple-powerful-http-in-roblox/355294). Newest source 2025-03-26.
- **Publish animation keyframes with Overwrite and use the Curve Editor** (multiple-creators): Publish from the Animation Editor with 'Overwrite existing asset' to get an ID; later edits only need re-publishing. Use the Curve Editor's color-coded curves to smooth rig changes between keyframes. The Animation Graph Clip Editor is in Beta: File > Beta Features > Animation Graph, then the Avatar tab on a rig with an Animator. Sources: [Suphi Kaner 2024-10 8:26](https://youtu.be/ZPviBfpPloE?t=506), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/tutorials/curriculums/animator/next-steps), [Roblox DevForum 2026-04](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788). Newest source 2026-10-28.
- **Scan imported scripts for common virus patterns** (single-mention): Use View > Find Results to search for fenv, RoSync, require and loadstring. Not every hit is malicious, so review each one before deleting. Sources: [Roblox DevForum 2021-03](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437). Newest source 2021-03-27.
- **Keep a non-AI fallback asset plan** (single-mention): One creator's AI texture generation crashed, so have a non-AI texture plan rather than relying on AI tools to deliver. Sources: [JustDucksey 2025-04 1:23](https://youtu.be/BbNlDGBROdg?t=83). Newest source 2025-04-10.
- **Use utility plugins to speed building and typing** (multiple-creators): Developer Tools, Auto Anchor, AutoScale Lite, Model Reflect and ResizeAlign speed building and GUI scaling (2021 list; check current versions). The Global Types plugin regenerates a types module if you tag it with a boolean attribute named 'Global types'. Sources: [Roblox DevForum 2021-03](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437), [Suphi Kaner 2024-11 6:02](https://youtu.be/SVLFkdeh6c8?t=362). Newest source 2024-11-28.
- **Sync VS Code edits into Studio with Rojo** (one-creator-repeated): Install the Rojo VS Code extension, run Rojo init and build from the command palette, then install the Rojo Studio plugin (v7 in the source), start the server from VS Code and click Connect. Write code in VS Code; saved changes sync into Studio immediately. The source is from 2022, so prefer built-in Script Sync where it is available. Sources: [Dev Total 2022-11 1:47](https://youtu.be/0K-5sifYhxs?t=107), [Dev Total 2022-11 8:35](https://youtu.be/0K-5sifYhxs?t=515), [Dev Total 2022-11 12:05](https://youtu.be/0K-5sifYhxs?t=725). Newest source 2022-11-23.
- **Test feature-flag edits only on a copy of your place** (single-mention): Editing feature flags can corrupt data and destabilize Studio. Make the change on a duplicate place, never on live data, and back up first. Sources: [TheNexusAvenger 2022-09 2:15](https://youtu.be/C4ASAayPpkY?t=135). Newest source 2022-09-19.
- **Use AI to write boilerplate you already understand** (single-mention): Use AI to automate repetitive code you can already check, such as leaderstats, DataStore skeletons, UI button functionality and tweens. Review each output against what you know before using it. Sources: [RoyalDev 2026-08 4:46](https://youtu.be/erhgduyGzdM?t=286). Newest source 2026-08-29.
- **Use AI for CFrame angle, sine/cosine and VFX math** (single-mention): Ask AI for advanced math such as CFrame angles and sine/cosine curves, especially for VFX and particle motion. Verify the result visually in Studio, since math errors show up as wrong motion. Sources: [RoyalDev 2026-08 7:30](https://youtu.be/erhgduyGzdM?t=450). Newest source 2026-08-29.
- **Use a current image-to-3D model for UGC base meshes** (one-creator-repeated): The speaker used Tripo AI to make base meshes for UGC items, saying older AI models looked too poor to sell. Choose the cheaper HD setting over Smart Mesh unless the extra quality is needed, since Smart Mesh costs substantially more credits. Refine in Blender if time allows. Sources: [Xaiyne 2026-10 0:41](https://youtu.be/KhKOSmdX8sc?t=41), [Xaiyne 2026-10 2:48](https://youtu.be/KhKOSmdX8sc?t=168). Newest source 2026-10-12.
- **Export UGC AI meshes with 2K texture, PBR off and under 4,000 triangles** (one-creator-repeated): Set the Tripo export to 2K texture with PBR off to reduce upload cost, and keep the triangle count under Roblox's 4,000 maximum (the speaker used 3,990). Check the final count in Studio before uploading. Sources: [Xaiyne 2026-10 2:47](https://youtu.be/wkfCP_09CI8?t=167). Newest source 2026-10-21.
- **Use Reclass to change an instance's class without losing properties** (single-mention): The Reclass plugin converts an instance to another class, such as Frame to ImageLabel or ImageButton, and keeps its properties. Use it instead of rebuilding UI elements by hand, then verify children and events still work. Sources: [BubuTheDev 2025-06 3:28](https://youtu.be/0UYtSJvYe4U?t=208). Newest source 2025-06-09.
- **Use Scribe Studio to inspect live player data, with a fallback** (single-mention): A Studio plugin such as Scribe Studio can show live player data in the server tab. The speaker warns it can be finicky, so keep a fallback such as print statements or your own debug UI. Sources: [Possible Panda 2026-09 9:12](https://youtu.be/KVmPyoOPmRI?t=552). Newest source 2026-09-20.
- **Use hard-surface CAD tools for guns and mechanical pieces** (single-mention): For hard-surface models like guns, a CAD tool such as Plasticity fits better than sculpting tools. The speaker notes it is a one-time purchase rather than a subscription. Export to Roblox-compatible formats and check scale and triangle count. Sources: [studio rook. 2026-10 1:50](https://youtu.be/z04_RTBiMgg?t=110). Newest source 2026-10-21.
- **Use AI coding for discrete systems like plot assignment** (single-mention): AI coding assistants such as Rebirth AI can build self-contained systems, like plot assignment, in short time (the speaker said under 30 minutes). Limit the scope to one discrete system and test it before combining it with other code. Sources: [LovJak 2026-06 3:00](https://youtu.be/ImcICq5XfL8?t=180). Newest source 2026-06-19.
- **Start prototypes in Build, then finish in Studio** (multiple-creators): Build turns a prompt into a playable starting game and hands off to Studio for refinement. Alpha access was NZ-only in July 2026, then Serbia and Singapore by September. Outside listed regions, start in Studio with Assistant or MCP instead. Sources: [Platform Aeronaut (transcript) 2026-07](https://transcripts.platformaeronaut.com/transcripts/RBLX-2Q26-transcript), [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/), [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/). Newest source 2026-09-10.
- **Check analytics and monetization inside Build** (multiple-creators): Sources agree Build lets creators review analytics and add monetization without opening Studio. Set up monetization and check performance data before publishing, rather than treating the prototype as ready. Sources: [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/), [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm). Newest source 2026-09-30.
- **Refine generated layouts in Studio** (single-mention): Scene Generator is announced to create layouts from a text prompt plus reference image. Treat output as a draft: verify parenting, collisions, and scale in Studio before building gameplay on top of it. Sources: [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/). Newest source 2026-09-10.
- **Use mobile Build for reviews and small edits only** (single-mention): Build supports making, publishing, reviewing analytics, and adding monetization from mobile (Sept 2026). Use phones for quick checks and minor changes; keep complex scripting and layout work in desktop Studio. Sources: [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm). Newest source 2026-09-30.
- **Treat announced agents as upcoming, not available** (single-mention): Roblox announced Playtesting (automated QA), Analytics (natural-language performance queries), and Experiment (A/B test recommendations) agents as upcoming. Keep manual playtesting after prompts and your own Experiments until these ship. Sources: [Roblox Investor Relations 2026-07](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm). Newest source 2026-07-30.
- **Use completed to-dos as revert checkpoints** (single-mention): Assistant planning mode lets you confirm, edit or reject the to-do list before agents run. Treat each completed to-do as a checkpoint you can revert to, so one bad AI step does not force a restart. Pair this with a place backup before large edits. Sources: [Roblox 2026-04 12:26](https://youtu.be/8IcYpOl4Sdk?t=746), [Roblox 2026-04 28:23](https://youtu.be/8IcYpOl4Sdk?t=1703). Newest source 2026-04-16.
- **Generate NPC behavior by prompt, then inspect the runner** (one-creator-repeated): NPC Dynamic Behavior (announced late 2026) populates NPCs from prompts. Behavior trees run on a runner you can inspect and modify in the visualizer and editor, so edit, version and reuse behavior across NPCs instead of trusting it as a black box. Sources: [Roblox DevForum 2026-09](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880), [Roblox 2026-10 2:48](https://youtu.be/QvNAMmGqdd4?t=168). Newest source 2026-10-12.
- **Run Scene Analysis skills before shipping** (single-mention): Roblox's Scene Analysis agent skills check scene health, rendering optimization and memory optimization, and can fix leaks. They are available through MCP or any agent. Run them on larger scenes before publishing, then verify fixes in playtest. Sources: [Roblox 2026-10 19:47](https://youtu.be/3gnK649VNbY?t=1187). Newest source 2026-10-12.
- **Give the agent a runtime bridge to verify behavior** (single-mention): Let the AI execute Luau, capture the viewport and read the console in the running game. The agent then verifies runtime behavior itself instead of you acting as its eyes. Keep the bridge limited to a trusted MCP client. Sources: [Roblox 2026-10 19:50](https://youtu.be/KB5iAzy86Fo?t=1190). Newest source 2026-10-12.
- **Pick the layout from a concept image before 3D generation** (single-mention): Start from a concept image and iterate prompts until the layout is right, then generate the 3D scene. Scene generation (about 3 minutes) follows the image's top-down layout, so layout mistakes are cheaper to catch in 2D. Sources: [Roblox 2026-10 2:36](https://youtu.be/QhZpK2hdnjE?t=156). Newest source 2026-10-12.
- **Name parts in generation prompts for per-part scripts** (single-mention): Define part segmentation in the mesh prompt, such as body, motor and seat. Generated meshes then have distinct parts that scripts can attach to individually, instead of one monolithic model. Sources: [Roblox 2026-10 7:37](https://youtu.be/QhZpK2hdnjE?t=457). Newest source 2026-10-12.
- **Tag meshes with 4D capability tags for drivable or shootable objects** (single-mention): Use the 4D behavior library: tag a mesh with the 4D capability tag and set attributes to make it drivable or shootable. Study the referenced DevForum experience for attribute names before tagging, and test the result in playtest. Sources: [Roblox 2026-10 10:20](https://youtu.be/QhZpK2hdnjE?t=620). Newest source 2026-10-12.
- **Send several style images at once for consistent output** (one-creator-repeated): Give the assistant several reference images in one request and state which style to match. Mesh generation follows images closely. Procedural models only approximate them with primitives, so use meshes when the look matters. Sources: [Roblox 2026-10 42:39](https://youtu.be/QhZpK2hdnjE?t=2559), [Roblox 2026-10 42:39](https://youtu.be/QhZpK2hdnjE?t=2559). Newest source 2026-10-12.
- **Write a model-per-task playbook before unattended runs** (one-creator-repeated): Record which AI model is best for images, meshes and objects. Then build a reusable asset-workflow skill (isolate objects, mesh them, upload via Open Cloud). Only then give the agent API keys for unattended runs, with Open Cloud keys scoped to the minimum needed. Sources: [Roblox 2026-10 16:08](https://youtu.be/KB5iAzy86Fo?t=968), [Roblox 2026-10 16:48](https://youtu.be/KB5iAzy86Fo?t=1008). Newest source 2026-10-12.
- **Use playtest agents that see only player-visible information** (one-creator-repeated): Roblox's human-like agents learn by imitation on gameplay data plus reinforcement learning. They see only what a real player sees and input via keyboard and mouse, and do not know about other players' positions outside their view. Use this model for fair playtests of AI-driven behavior. Sources: [Roblox 2026-10 19:19](https://youtu.be/QvNAMmGqdd4?t=1159), [Roblox 2026-10 19:19](https://youtu.be/QvNAMmGqdd4?t=1159). Newest source 2026-10-12.
- **Confirm the AI's understanding before building** (single-mention): After a build prompt, ask the AI to restate what it understood and list gaps. Then make targeted edits (for example, move one text label) rather than re-prompting the whole build. Sources: [RoyalDev 2026-10 2:03](https://youtu.be/xaWGP-slzdM?t=123). Newest source 2026-10-01.
- **Review each AI script diff, or accept and check the diff after** (one-creator-repeated): In Assistant Agent mode, which can edit scripts and the place, use the 'review each script change' option to read diffs before accepting. If you accept all, check the diff afterward. Sources: [SimTek Game Development 2026-09 0:40](https://youtu.be/-0H6JRtrA2Y?t=40), [SimTek Game Development 2026-09 2:01](https://youtu.be/-0H6JRtrA2Y?t=121). Newest source 2026-09-26.
- **Ask for full replacement scripts, not partial diffs** (one-creator-repeated): Partial code diffs invite paste errors. Ask the AI for the full script and replace the whole file. Sources: [LovJak 2026-10 4:11](https://youtu.be/YXcV0Ba0RJc?t=251), [LovJak 2026-10 5:36](https://youtu.be/YXcV0Ba0RJc?t=336). Newest source 2026-10-15.
- **Verify server vs client location of every AI script** (one-creator-repeated): Before testing, confirm each generated script sits in the right service (ServerScriptService, StarterPlayerScripts, etc.). This complements the parent/folder check already listed. Sources: [LovJak 2026-10 4:11](https://youtu.be/YXcV0Ba0RJc?t=251). Newest source 2026-10-15.
- **Name concrete parts, scale and exact values in build prompts** (single-mention): For buildings, list parts (walls, floor, roof, doorway, window) and scale. Put exact values in the prompt, such as sprint speed 30. Expect rough output and polish it by hand. Sources: [SimTek Game Development 2026-09 8:08](https://youtu.be/-0H6JRtrA2Y?t=488), [SimTek Game Development 2026-09 2:01](https://youtu.be/-0H6JRtrA2Y?t=121). Newest source 2026-09-26.
- **When output is wrong, describe the feel and the reference-game structure** (multiple-creators): Replace vague re-prompts with a detailed description of the target feeling and the structure of a reference game. Detailed prompts gave better results and a complex system worked on first run. Sources: [MonarchDev 2026-10 4:31](https://youtu.be/hPWJlFwp5Xs?t=271), [LovJak 2026-10 3:28](https://youtu.be/YXcV0Ba0RJc?t=208). Newest source 2026-10-16.
- **Treat AI-generated games as a strong first draft** (one-creator-repeated): Expect to fix layout, balance and gameplay feel yourself. Generated UI, sound effects and meshes save the most time, but check their fidelity; AI-only output without checks looks noticeably worse. Sources: [MonarchDev 2026-10 10:08](https://youtu.be/QwdZRB6xRKk?t=608), [MonarchDev 2026-10 10:50](https://youtu.be/QwdZRB6xRKk?t=650), [MonarchDev 2026-10 10:50](https://youtu.be/QwdZRB6xRKk?t=650). Newest source 2026-10-12.
- **Verify the MCP link before prompting** (one-creator-repeated): Create an API key in Creator Hub, connect the AI client, then connect Roblox Studio. Confirm the link by asking the AI which place it sees. Sources: [MonarchDev 2026-10 0:56](https://youtu.be/QwdZRB6xRKk?t=56), [MonarchDev 2026-10 1:18](https://youtu.be/hPWJlFwp5Xs?t=78). Newest source 2026-10-16.
- **Benchmark AI tools with a fixed prompt and time budget** (single-mention): Use the identical prompt and a fixed time limit per run so results are comparable across games. One creator used 1h, 2h, 3h and 4h budgets across four tests. Sources: [MonarchDev 2026-10 1:23](https://youtu.be/QwdZRB6xRKk?t=83), [MonarchDev 2026-10 1:23](https://youtu.be/QwdZRB6xRKk?t=83). Newest source 2026-10-12.
- **Plan AI disclosure for non-Roblox storefronts** (single-mention): Steam requires disclosure of shipped generative AI in art, audio, voice, localized text and store assets. Coding assistance is exempt. Plan disclosure if you ship elsewhere. Sources: [Deconstructor of Fun 2026-10 23:51](https://youtu.be/NrPjXO_7oKk?t=1431). Newest source 2026-10-29.
- **Escalate to a stronger model when a cheaper one repeats the same mistake** (one-creator-repeated): If a cheaper model repeats an error even after correction, switch to a stronger model and paste the error and current script. One creator reported Claude 3.7 fixed a carry script that DeepSeek could not, and DeepSeek repeated the same mistake after correction. Sources: [BloxxedDev 2025-03 2:29](https://youtu.be/CipKM4DBWxg?t=149), [BloxxedDev 2025-03 0:00](https://youtu.be/y5aNv16bT3s?t=0). Newest source 2025-03-29.
- **Keep a backup AI tool for service outages** (one-creator-repeated): Heavy AI use can hit busy-server errors. One creator lost about 40 minutes before getting a working DeepSeek response. Have a second AI tool or a retry plan ready so a stalled service does not block the session. Sources: [BloxxedDev 2025-03 0:28](https://youtu.be/CipKM4DBWxg?t=28), [BloxxedDev 2025-03 0:28](https://youtu.be/CipKM4DBWxg?t=28). Newest source 2025-03-09.
- **Give the AI project context and full scripts up front** (single-mention): Open each request with the game type, map, and core concept, and paste the relevant scripts in. Send any error messages back for fixes. This gives the model the state it needs instead of guessing. Sources: [BloxxedDev 2025-03 2:11](https://youtu.be/CipKM4DBWxg?t=131). Newest source 2025-03-09.
- **Check that AI-written listeners also handle items that already exist** (single-mention): One creator's AI added a listener for future coins, so coins already in the game were never processed. When AI writes a ChildAdded-style or event listener, also verify that objects present at startup are handled, and test with pre-existing objects. Sources: [ByteBlox 2025-01 7:52](https://youtu.be/SCtYVCRVzM8?t=472). Newest source 2025-01-24.
- **Ask AI to strip excessive comments from generated code** (single-mention): Generated scripts often carry heavy comment blocks. Ask the AI to remove excess comments so the script is readable and easy to review line by line before you accept it. Sources: [Duckable 2025-08 3:57](https://youtu.be/Em5H7sNWN7I?t=237). Newest source 2025-08-29.
- **Use AI to propose balanced tycoon button prices** (single-mention): Balancing tycoon button prices by hand is slow. AI can generate a candidate price curve, which you then verify in playtests before shipping. Treat the numbers as a starting point, not final values. Sources: [Duckable 2025-08 6:06](https://youtu.be/Em5H7sNWN7I?t=366). Newest source 2025-08-29.
- **Budget hours for AI iteration on complex systems** (single-mention): Complex systems take many prompt-test cycles. One creator spent about 3 hours overnight fixing a fireworks system, with waiting between tests. Plan a block of time and test after each iteration rather than expecting a single-pass fix. Sources: [Duckable 2025-08 8:16](https://youtu.be/Em5H7sNWN7I?t=496), [Duckable 2025-08 7:09](https://youtu.be/Em5H7sNWN7I?t=429). Newest source 2025-08-29.
- **Keep game balance values human-set, not AI-configured** (one-creator-repeated): janisjanis01 reversed course: AI balancing advice was used for tuning in 2025-12, but by 2026-10 AI-configured upgrades were a time sink and they advise against letting AI configure balance. Use AI for UI assets and boilerplate, and set upgrade costs and balance numbers yourself in Configs. Sources: [janisjanis01 2025-12 10:16](https://youtu.be/JYvGdKRzwEo?t=616), [janisjanis01 2026-10 4:05](https://youtu.be/A2QD-eT3IG0?t=245), [janisjanis01 2026-10 8:57](https://youtu.be/A2QD-eT3IG0?t=537). Newest source 2026-10-25.
- **Bind a shortcut to Go To Module and pair it with Require Autocomplete** (one-creator-repeated): Go To Module has no default shortcut. Assign one via File > Advanced > Customize Shortcuts (the demo used Ctrl+Q). Pairing it with Require Autocomplete lets you insert require lines quickly and jump to those modules. Sources: [Crusherfire 2024-05 0:34](https://youtu.be/yncfwrBAWVw?t=34), [Crusherfire 2024-05 4:53](https://youtu.be/yncfwrBAWVw?t=293). Newest source 2024-05-30.

## Checklist
- [ ] Enable Studio as an MCP server and confirm the green client-connected indicator
- [ ] Pick the model effort level: medium for checks, ultra for big builds
- [ ] Write a specific prompt with numbers for one mechanic
- [ ] Include a full-screen reference screenshot for UI
- [ ] Playtest after each prompt
- [ ] Paste errors back to the AI to fix
- [ ] Check generated objects' parent/folder
- [ ] Add a health system before testing combat
- [ ] Generate UI icons with Forge UI and refine with edit prompts
- [ ] Fix text in Photopea
- [ ] Monitor usage limits and plan around resets
- [ ] Read and understand AI-written code
- [ ] Use Studio Assistant for bulk tasks like tree scattering
- [ ] Reskin template plugin outputs
- [ ] Have ChatGPT draft prompts
- [ ] Prototype with AI before hiring
- [ ] Batch change requests to programmers
- [ ] Plan 30-50% extra UI text space
- [ ] Constrain in-game LLMs with JSON and theme checks
- [ ] Consider copyright and player attitude to AI content
- [ ] Before doing repetitive Studio edits (many placements, renames, folder grouping, property-based selection), try Assistant actions first.
- [ ] After any bulk Assistant operation, check the object count and that each object landed in the correct parent folder.
- [ ] Write Assistant script requests as pseudo-code with explicit steps and conditions, then compare the output line count against the request.
- [ ] When generated content misses, narrow the request scope and regenerate, instead of repeating the same broad prompt.
- [ ] When debugging unfamiliar code, ask Studio's AI to explain it before asking for a fix.
- [ ] Move tunable onboarding values into Roblox Configs and Experiments rather than hardcoding them.
- [ ] When answering an AI disclosure question, check whether players can interact with generative AI in the experience.
- [ ] Early in a project, run quick experiments with new AI tools and log what fails.
- [ ] Back up the place with File > Publish to Roblox As before any AI edit or conversion skill.
- [ ] Update Roblox Studio to the latest version before connecting an MCP client.
- [ ] Enable Studio MCP via Assistant > ... > Manage MCP Servers; enable needed features under File > Beta Features.
- [ ] After setup, check the green connected-client indicator, then ask the client to name the open project.
- [ ] Only connect MCP clients you trust; they can read and modify open places.
- [ ] Use Plan mode for complex requests; review the Markdown plan before clicking Build.
- [ ] Click Continue when Assistant hits max output so it resumes building.
- [ ] Use one chat per task; use the branch icon to fork a response into a new chat.
- [ ] Select objects before prompting so Assistant can modify, duplicate or extend them.
- [ ] Name exact instances, the service (e.g. TweenService) and the instance type (part or model) in prompts.
- [ ] Select a Part before /generate_mesh and keep max triangle count at the 10,000 default unless you need lower poly.
- [ ] Pick text or a reference image for /generate_mesh per request; not both.
- [ ] Check Blender Validation Tool and Calisthenics Tool before importing avatar items.
- [ ] Use Script Sync from the top-level project folder so services match by name.
- [ ] Use Graph > Create Animate script for Animate, RunClient and RunServer scaffolding.
- [ ] Start from the makeup template head and do not rename or delete its data model.
- [ ] Start from a starter project with LLM-friendly markdown context files for a coding harness.
- [ ] Bring your own Anthropic, OpenAI or Google keys via Assistant > ... > Manage API Keys.
- [ ] Use Google Sheets + Apps Script with Open Cloud to tune values without republishing.
- [ ] Write a master prompt covering map, systems, persistence, offline earnings and mobile controls.
- [ ] Generate icons at 512x512 and thumbnails at 1920x1080; add text in an editor.
- [ ] Edit custom textures in Photoshop (paid) or Krita (open-source).
- [ ] Connect Claude or ChatGPT to Studio as an alternative to paid standalone generators.
- [ ] If Toolbox fails on Windows, close Studio and delete %LOCALAPPDATA%\Roblox\RobloxStudio\WebView2; on Mac, delete the Roblox Studio WebKit and Caches folders.
- [ ] Open Assistant inside Studio, not the web version, and rename parts before prompting.
- [ ] Delegate folders, boilerplate, leaderboards, RemoteFunctions and exact-CFrame placement to Assistant.
- [ ] Build terrain, lighting, gameplay, map and UI yourself, since players notice AI-looking UI.
- [ ] When Assistant output is wrong, reword the prompt and try again instead of editing blindly.
- [ ] Use Ctrl+Z for non-script Assistant changes; delete generated scripts in Explorer.
- [ ] Name the problem and the target look in every visual fix request.
- [ ] Give texture prompts a material, color and pattern; set Preview orientation to Manual if the angle is poor.
- [ ] Watch session length; at about 900k of 1M tokens, compress or start fresh with current scripts and Explorer layout pasted in.
- [ ] Understand scripts (basic Luau) before accepting AI code; ask AI to explain anything unclear.
- [ ] Avoid AI-generated core code for paid client commissions where originality matters.
- [ ] Pause a performance spike and ask Assistant to analyse the capture.
- [ ] Duplicate Roblox-authored skills before customizing; re-duplicate to get updates.
- [ ] Use Ctrl+9 (Cmd+9) for quick Luau in the Command Bar; enable multi-line beta if needed.
- [ ] Parent every plugin widget GuiObject to the DockWidgetPluginGui.
- [ ] Use Theme:GetColor() and reconnect on ThemeChanged so plugin widgets match the user's theme.
- [ ] Keep one copy of open-source modules such as BridgeNet2, TopbarPlus and ProfileService.
- [ ] Publish animation keyframes with 'Overwrite existing asset' to keep the same ID.
- [ ] Scope Open Cloud keys to needed permissions and confirm the key owner has analytics access (403 otherwise).
- [ ] Check an endpoint's risk level and read its impact before using Try it out.
- [ ] Call the Place Publishing API from CI after integration tests pass.
- [ ] Call Player:PromptAgeCheck() on a deliberate player action, not on spawn.
- [ ] Validate on the server; don't rely on ML or client checks for anti-cheat.
- [ ] Search imported scripts for fenv, RoSync, require and loadstring, then review each hit.
- [ ] Keep a non-AI fallback plan for textures and other AI-generated assets.
- [ ] During the Studio beta, rerun require("@rbx/AvatarAbilities") in the Command Bar after each reload to restore autocomplete.
- [ ] Before using Rojo, confirm the current plugin version and whether built-in Script Sync covers your need.
- [ ] Make feature-flag tests on a duplicate place, not live data.
- [ ] Ask AI for boilerplate only when you can read and verify the output.
- [ ] For CFrame or trig-heavy VFX, check the math with a visual test in Studio.
- [ ] Compare HD vs Smart Mesh output and credit cost on one asset before batch generating.
- [ ] Set image-to-3D exports to 2K texture, PBR off, and triangle count under 4,000.
- [ ] Count triangles in Studio after import and before upload.
- [ ] Use Reclass for class swaps, then check children, events and properties.
- [ ] Keep a fallback debug method ready when using a live-data inspector plugin.
- [ ] Use CAD tools for hard-surface pieces and check scale before importing into Roblox.
- [ ] Before recommending Build, confirm the user's region is in the alpha list (New Zealand, Serbia, Singapore as of Sept 2026).
- [ ] If prototyping from a prompt, generate in Build, then open and refine the result in Studio.
- [ ] Back up the place before importing or editing any Build or AI-generated output in Studio.
- [ ] After Build generates a game, review analytics and monetization settings before publishing.
- [ ] Verify Scene Generator layouts in Studio: parenting, collisions, scale, and spawn points.
- [ ] Limit mobile Build use to reviews, monetization checks, and small edits.
- [ ] Check your plan's prompt-capacity tier (free base vs paid) before planning a heavy generation session.
- [ ] Keep manual playtests after each prompt; don't wait for the Playtesting Agent.
- [ ] Keep A/B tests on your own Experiments; don't assume the Experiment Agent exists yet.
- [ ] For external AI tools, connect through the Studio MCP server rather than custom bridges.
- [ ] Before a multi-step Assistant run, read the to-do list and edit or reject steps before confirming.
- [ ] After each completed to-do, note it as a revert point before starting the next step.
- [ ] For NPC population, write one prompt, then inspect the behavior runner before reusing the behavior across NPCs.
- [ ] Run Scene Analysis (scene health, rendering, memory, leaks) on larger scenes before publishing.
- [ ] Give the agent runtime access (execute Luau, capture viewport, read console) so it can verify its own changes.
- [ ] Settle the layout from a concept image before generating a 3D scene.
- [ ] Name the parts in a mesh prompt (body, motor, seat) when scripts need per-part behavior.
- [ ] Attach several style reference images in one request when you need a consistent look.
- [ ] Write a per-task model playbook before giving an agent API keys for unattended asset runs.
- [ ] Scope any API key used by an unattended pipeline to the minimum endpoints and place needed.
- [ ] Check generation quotas and concurrency (about 50 procedural models/day, several dozen meshes/day, 5 to 10 concurrent jobs) before planning a batch.
- [ ] Restate the AI's understanding and list its gaps before accepting a build.
- [ ] In Assistant Agent mode, turn on per-change review or accept all and check the diff afterward.
- [ ] After a partial diff, ask for the full replacement script before pasting.
- [ ] Paste each generated script into its service and confirm server vs client.
- [ ] List concrete parts and scale in build prompts (walls, floor, roof, doorway, window).
- [ ] Put exact numeric values (for example, sprint speed 30) in prompts.
- [ ] Create a Creator Hub API key, connect the AI client, then connect Roblox Studio.
- [ ] Confirm the MCP connection by asking the AI which place it sees.
- [ ] Benchmark tools with identical prompts and a fixed time budget.
- [ ] Playtest and fix layout, balance and feel after any AI draft.
- [ ] Fidelity-check AI-generated UI, sound effects and meshes before shipping.
- [ ] Describe target feel and reference-game structure when fixing wrong output.
- [ ] Prefer Tripo 3.1 over 2.5 Legacy for image-to-3D meshes.
- [ ] Plan AI disclosure before shipping on Steam or other storefronts.
- [ ] If a cheaper model repeats the same bug after correction, switch to a stronger model and paste the error with the current script.
- [ ] Before a heavy AI session, set up a backup AI tool or a retry plan in case the service is busy.
- [ ] Start each AI request with game type, map, core concept, and the relevant scripts.
- [ ] Ask the AI to remove excess comments from generated scripts before reviewing them.
- [ ] After AI writes an event listener, confirm it also processes objects that already exist at startup.
- [ ] For tycoon button prices, ask AI for a candidate curve and verify it in playtests.
- [ ] Budget multiple hours for AI iteration on complex systems such as fireworks, testing after each change.
- [ ] For a single-line fix, state the exact line to change and expect the diff to be larger than one line; check it.
- [ ] Open File > Advanced > Customize Shortcuts and bind a key to Go To Module (no default; demo used Ctrl+Q).
- [ ] Use Go To Module together with Require Autocomplete to insert require lines and jump between modules.
- [ ] Expect to modify AI-generated UI vectors and boilerplate before using them in the game.
- [ ] Keep upgrade costs and balance numbers in your own Configs; limit AI to code boilerplate and UI assets.

## Numbers and benchmarks

| Metric | Value | Context | Sources |
|---|---|---|---|
| AI share of top creators' hours | 57% of hours by top 10,000 creators involve AI; up 600%+ in 6 months | Roblox-reported | [Roblox 2026-09 6:13](https://youtu.be/53dj7AG3foA?t=373) |
| Assistant usage | hundreds of thousands of requests/day from 30,000+ users; millions of scripts/month | Per official speaker | [Roblox 2025-09 3:22](https://youtu.be/3h25HUtBHFk?t=202), [Roblox 2025-09 3:22](https://youtu.be/3h25HUtBHFk?t=202) |
| Avatars set up in Studio | 100,000+ monthly; saves 4-8 hours per character | Per speaker | [Roblox 2025-09 3:22](https://youtu.be/3h25HUtBHFk?t=202) |
| 3D generations | >1 million since March launch | Cube 3D | [Roblox 2025-09 3:22](https://youtu.be/3h25HUtBHFk?t=202) |
| Claimed scripting time saved | ~80%; a day's work in ~20 minutes | MoseyTube, unverified | [MoseyTube 2026-04 2:04](https://youtu.be/sFr7htxsnR4?t=124), [MoseyTube 2026-04 2:04](https://youtu.be/sFr7htxsnR4?t=124) |
| Master-prompt build | ~1 hour | My Pizzeria tycoon, ultra effort | [MoseyTube 2026-07 2:26](https://youtu.be/PstV93OnOdM?t=146) |
| Claude Max 5x | $100/mo | Replaced Pro due to limits | [MoseyTube 2026-08 1:23](https://youtu.be/5zz5ao0zV_Y?t=83) |
| Session usage | simple prompt ~1% (~30s); full 3-prompt game ~13% (22% with treadmill step); 73% then 100% on Pro, reset ~1h34m | TheDankDeveloper | [TheDankDeveloper 2026-10 0:40](https://youtu.be/4ojmHWn_rxY?t=40), [TheDankDeveloper 2026-10 4:50](https://youtu.be/Mftq7v8nAcs?t=290), [TheDankDeveloper 2026-10 4:50](https://youtu.be/Mftq7v8nAcs?t=290) |
| Build comparison | ChatGPT 1 hour; Lemonade ~40 min prompting; 1 hour limit per AI | Same prompt, indie test | [TheDankDeveloper 2026-01 0:00](https://youtu.be/BYhhm9o3H_E?t=0), [TheDankDeveloper 2026-01 0:00](https://youtu.be/3y7EU49_d7s?t=0) |
| Lemonade plot system generation | ~4-5 minutes | One prompt | [TheDankDeveloper 2026-04 0:40](https://youtu.be/Ufr0SVq-o98?t=40) |
| Forge UI variants | 4 per generation |  | [TheDankDeveloper 2026-04 4:03](https://youtu.be/i5sldtdF8m0?t=243) |
| RoVis cost | ~2-5 credits per thumbnail | Creator estimate | [CallMeDogey 2026-04 5:29](https://youtu.be/SjjPGduApZU?t=329) |
| Text expansion | 30-50% extra for long strings; 2-3x for short | IBM guidelines | [Roblox 2018-07 13:24](https://youtu.be/qoWMP-AFT08?t=804), [Roblox 2018-07 13:24](https://youtu.be/qoWMP-AFT08?t=804) |
| Localization demo | ~1.5 min Spanish demo; ~30 verb forms for 'demonstrate' | 2018 | [Roblox 2018-07 5:41](https://youtu.be/qoWMP-AFT08?t=341), [Roblox 2018-07 8:34](https://youtu.be/qoWMP-AFT08?t=514) |
| Claude plan | Free then upgraded to Pro mid-build |  | [TheDankDeveloper 2026-01 1:26](https://youtu.be/3y7EU49_d7s?t=86) |
| Example forged weapon | Damage 64, speed 0.5, quality 93, value 320 | Claude-built | [TheDankDeveloper 2026-01 3:19](https://youtu.be/3y7EU49_d7s?t=199) |
| In-experience creation | Millions of unique creations | ~10 months after launch | [Roblox 2026-10 16:21](https://youtu.be/gCp4zzjjJ14?t=981) |
| AI build time claim | about two days (kra_DeZ); months to days | Self-reported | [kra_DeZ 2026-08 10:08](https://youtu.be/oMI-GhUcfFE?t=608), [kra_DeZ 2026-09 6:59](https://youtu.be/cJ-YzHHhQs8?t=419), [kra_DeZ 2026-08 10:11](https://youtu.be/oMI-GhUcfFE?t=611) |
| Material generation output increase | +60% more material variants | Speaker-cited Studio AI usage stat, Roblox Sept 2024 talk; a usage figure, not a quality measure. | [Roblox 2024-09 4:51](https://youtu.be/XrxUy51NsvI?t=291) |
| Code output increase with Code Assist/Assistant | +80% more code | Speaker-cited Studio AI usage stat, Roblox Sept 2024 talk; a usage figure, not a quality measure. | [Roblox 2024-09 6:17](https://youtu.be/XrxUy51NsvI?t=377) |
| Tree forest generation speed | 77 trees in ~20 seconds | Assistant placed trees from a single prompt in the Roblox demo. | [Roblox 2024-09 9:45](https://youtu.be/XrxUy51NsvI?t=585) |
| Assistant prompt-to-script ratio | ~10-line prompt yields ~100 lines of script | Speaker claim from Roblox Sept 2024 talk; typical, not guaranteed. | [Roblox 2024-09 9:45](https://youtu.be/XrxUy51NsvI?t=585) |
| Procedural model generation limit | 50 per 24-hour rolling window | Via /generate_procedural_model; official, 2026-10 | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide) |
| Default max triangle count for generated meshes | 10,000 | Optional input for /generate_mesh; lower values give lower-poly results | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide), [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide) |
| Max parts per generated model | 8 | Segmentation via Part Names entries | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide) |
| Preview images per mesh generation | 4 | Shown after Confirm on the segmentation plan | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/assistant/guide) |
| Max file size per Create/Update Asset call | 20 MB | One asset per call for content uploads | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/guides/usage-assets) |
| script_search results cap | 10 | Fuzzy name search for scripts in the Studio MCP server | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/mcp) |
| script_grep results cap | 50 matches | String pattern search across all game scripts | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/mcp) |
| Quick Connect supported MCP clients | 7 | Antigravity, Codex CLI, Claude Code, Claude Desktop, Cursor, Gemini CLI, VS Code | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/mcp) |
| AI skill conversion time | 20-30 minutes | Frontier model, typical rbx-convert-to-streaming run | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/workspace/streaming/techniques) |
| AI skill token usage | about 200,000 tokens | Typical conversion context usage | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/workspace/streaming/techniques) |
| Free prompts per day | Creator-set limit; resets daily; each message counts as one | Official prompt limit setting, 2026-10 | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/build) |
| Rollout | Gradual, starting with New Zealand | Official rollout note, 2026-10 | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/build) |
| Build audience age | Users aged 9+ who completed an age check | Eligibility as extracted; the feature it applies to is not named in the source | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/build) |
| Code Assist auto-trigger | After pausing a few seconds on a line; manual trigger Alt+\ (Option+\ on Mac) | Official, 2026-10 | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/script-editor) |
| Code Assist daily suggestion cap | Capped per day; no more until next day (exact number not stated) | Official stated limitation | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/script-editor) |
| Bullet gravity for drop (FastCast Redux) | -100 to -500 | Indie recommendation, 2020 | [Roblox DevForum 2020-05](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791) |
| Blender animation export frame step | 1 at 30 fps (high quality); 2-5 for smoother | Sampling parameter, 2017; check against current exporter | [Roblox DevForum 2017-03](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729) |
| Icon and thumbnail generation sizes | Icons 512x512; thumbnails 1920x1080 | Indie ChatGPT workflow, 2026-07 | [rasdev 2026-07 4:05](https://youtu.be/_Tt-l7EMEHE?t=245) |
| Super Bullet token balance after one run | -25,000 tokens (card shop build errored; account in debt) | Indie self-reported, 2026-09 | [Duckable 2026-09 2:21](https://youtu.be/MBRNAqkDEFA?t=141) |
| Super Bullet paid-tier progress | 2 of 6 phases after 18 min on $20 subscription; system not functional | Indie self-reported, 2026-09 | [Duckable 2026-09 14:12](https://youtu.be/MBRNAqkDEFA?t=852) |
| Roblox Assistant time per prompt (indie) | about 27-30 minutes per prompt (shelf, highlight, upgrade features) | Indie self-reported, 2026-09 | [Duckable 2026-09 15:08](https://youtu.be/MBRNAqkDEFA?t=908) |
| Forge GUI charge after free trial | $16 (trial credits ran out after one message) | Indie self-reported, 2026-09 | [Duckable 2026-09 6:58](https://youtu.be/MBRNAqkDEFA?t=418) |
| Lemonade.gg credits remaining | 0.2 credits before core game finished | Indie self-reported, 2026-09 | [Duckable 2026-09 5:08](https://youtu.be/MBRNAqkDEFA?t=308) |
| AI draft build time (GuideRealm) | 7 min 18 s with Codex at extra high effort | Indie self-reported, 2026-10 | [GuideRealm 2026-10 4:12](https://youtu.be/ltbZzXRrDF8?t=252) |
| Example shooter prompt rules | Rounds 60 seconds; first to 3 rounds wins match | Official example of a specific prompt | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/ai/build-with-assistant) |
| Default Walk animation ID | 507777826 | Example clip in the docs' basic graph tutorial | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/animation/graph-editor) |
| Default Wave animation ID | 507770239 | Example additive clip in the docs' basic graph tutorial | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/animation/graph-editor) |
| Long-session context budget | ~900,000 of ~1,000,000 tokens | Speaker's example of a session that needs compressing or restarting. | [MonarchDev 2026-10 4:48](https://youtu.be/WA4RzzT39Dw?t=288), [MonarchDev 2026-10 4:48](https://youtu.be/WA4RzzT39Dw?t=288) |
| Texture preview generation time | ~10 seconds for three preview images | Texture Generator Preview step (Roblox Creator Docs, Oct 2026). | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator) |
| Texture Fast mode output time | 1K diffuse texture in under 30 seconds | Fast generation mode. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator) |
| Texture Quality mode output | 4K PBR texture, takes a couple of minutes | Quality generation mode. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/texture-generator) |
| Command Bar history size | Last 10 executed commands | Recent tab in Command Bar history popup. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/overview) |
| Multi-line Command Bar height | Starts at 2 lines, grows to 10 | Requires Multi-line Command Bar beta enabled in File > Beta Features. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/overview) |
| Try it out risk levels | 4 (Low, Medium, High, Critical) | Critical endpoints have Try it out disabled. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/risk-levels) |
| Medium-risk confirmation frequency | Once per endpoint per browser session | Confirmation dialog before sending. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/risk-levels) |
| High-risk confirmation dialogs | 2 per session | Enforced per session, not per endpoint; typically DELETE and destructive actions. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/reference/risk-levels) |
| Minimum account age to authorize OAuth 2.0 apps | 13+ | Required for users authorizing OAuth apps. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-overview) |
| Developer requirement for OAuth apps | ID verified | Required to register and publish OAuth 2.0 apps. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/cloud/auth/oauth2-overview) |
| DockWidgetPluginGuiInfo parameters | 7 ordered parameters | InitialDockState, InitialEnabled, InitialEnabledShouldOverrideRestore, FloatingXSize, FloatingYSize, MinWidth, MinHeight. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/build-studio-widgets) |
| Example floating widget size | 200x300 px default, 150x150 px minimum | Example from Creator Docs. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/studio/build-studio-widgets) |
| glTF export status | Beta | Enable via File > Beta Features > glTF Export. | [Roblox Creator Docs 2026-10](https://create.roblox.com/docs/art/modeling/gltf-export) |
| Synthetic obby exploit dataset | 10 normal + 10 exploiting runs augmented to ~1.2k runs (70 noisy copies per normal path) | Mock data, 2024; indie demo, not production benchmark. | [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460) |
| Synthetic model test accuracy | ~85% | Keras MLP (Dense 64, sigmoid output, 15 epochs, batch 15); author says player-generated data is much better. | [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460), [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460) |
| Train/test split | 80/20 with random shuffle | Used in the 2024 obby classifier demo. | [Roblox DevForum 2024-01](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460) |
| Animation learning time budget | 1 hour self-imposed | Creator with no prior animation experience; low-advice, self-reported. | [BloxxedDev 2025-07 0:00](https://youtu.be/rjQtLR9w2s0?t=0) |
| Roblox UGC mesh triangle maximum | 4,000 | Indie-reported limit used as a target; verify against official Roblox docs before relying on it. Speaker kept meshes at 3,990. | [Xaiyne 2026-10 2:47](https://youtu.be/wkfCP_09CI8?t=167) |
| Time to build an AI-generated thumbnail | about 20 minutes | Speaker iterated prompts with reference images rather than one-shot prompting. | [RoyalDev 2026-09 2:44](https://youtu.be/rxeLNsNUVTQ?t=164) |
| AI-assisted plot assignment system build time | under 30 minutes | Self-reported, for one discrete system using Rebirth AI. | [LovJak 2026-06 3:00](https://youtu.be/ImcICq5XfL8?t=180) |
| Bug bounty for IKControl leg/arm math fix | 100,000 Robux | Posted 2023-01 and listed as still open in the source; confirm status before relying on it. | [TheNexusAvenger 2023-01 0:00](https://youtu.be/6V6WOKBZI7I?t=0) |
| Rojo Studio plugin version | 7 | Version from a 2022 source; check current Rojo release. | [Dev Total 2022-11 8:35](https://youtu.be/0K-5sifYhxs?t=515) |
| AI-using creators saying AI speeds launch or update timelines | 95% | Investor Relations survey, July 2026; superseded by the 97% figure below (different denominator: all AI users vs regular AI users). | [Roblox Investor Relations 2026-07](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm) |
| Regular AI-using creators saying AI accelerated development timelines | 97% (survey of several thousand) | Investor Relations, Sept 2026; latest figure. Self-reported survey, not a measured benchmark. | [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm), [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm) |
| Creators reporting over 50% faster publishing | Nearly half of AI-using creators | Investor Relations, July 2026. | [Roblox Investor Relations 2026-07](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm) |
| Top 100 games (by hours) using AI tools in past month | >80% | Investor Relations, Sept 2026. | [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm), [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm) |
| Creator-generated 3D assets / daily Cube use | Over 60,000 assets; ~1,400 games use Cube daily | Investor Relations, July 2026. | [Roblox Investor Relations 2026-07](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm) |
| Build users who published games (official) | 500,000+ users; 70,000+ games | Investor Relations, Sept 2026; official scope. | [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm) |
| Games published with Build since NZ alpha (indie) | About 9,000 | GamesBeat, self-reported, Sept 2026; scope and dates differ from N7259. | [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/) |
| Build game creators who had never used Studio | 71% | GamesBeat, self-reported; out of thousands of Build creators. | [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/) |
| Build availability | New Zealand (alpha, July 2026); + Serbia and Singapore (Sept 2026) | Check current region list before recommending. | [Platform Aeronaut (transcript) 2026-07](https://transcripts.platformaeronaut.com/transcripts/RBLX-2Q26-transcript), [GamesBeat 2026-09](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/) |
| Daily MCP user growth among top creators | Nearly 5x since Q2 | Investor Relations, Sept 2026; reflects Studio MCP server adoption. | [Roblox Investor Relations 2026-09](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm) |
| Games published via Build | About 9,000 (data through Sept 1, 2026) | Build is prompt-based creation; PocketGamer.biz figure is self-reported, Roblox Newsroom is official. | [PocketGamer.biz 2026-09](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/), [Roblox Newsroom 2026-09](https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play) |
| Build creators who never used Roblox Studio | 71% | Share of users who created a game with Build; shows Build lowers the entry barrier. | [PocketGamer.biz 2026-09](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/), [Roblox Newsroom 2026-09](https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play) |
| Top 10,000 developers using AI for game creation | >50% | Roblox official, Oct 2026. | [Roblox 2026-10 0:00](https://youtu.be/QhZpK2hdnjE?t=0) |
| Mesh generation time | About 30 seconds | Per mesh, Oct 2026. | [Roblox 2026-10 6:42](https://youtu.be/QhZpK2hdnjE?t=402) |
| Scene generation time | About 3 minutes | Per generated scene, Oct 2026. | [Roblox 2026-10 8:19](https://youtu.be/QhZpK2hdnjE?t=499) |
| Daily quota, procedural models | About 50 per day (approx.) | Approximate; verify current limits in the Studio dashboard. | [Roblox 2026-10 33:41](https://youtu.be/QhZpK2hdnjE?t=2021) |
| Daily quota, mesh generation | Several dozen per day | Approximate; exact value not stated. | [Roblox 2026-10 33:41](https://youtu.be/QhZpK2hdnjE?t=2021) |
| Concurrent generation jobs | 5 to 10, depending on model | Plan batch sizes around the lower bound. | [Roblox 2026-10 33:41](https://youtu.be/QhZpK2hdnjE?t=2021) |
| Animation iteration effort | 4 days; weekly usage reset twice on a $200 plan | Iterating animation by driving Blender via MCP with Astro; shows usage cost of agent loops. | [Roblox 2026-10 25:19](https://youtu.be/KB5iAzy86Fo?t=1519) |
| Studio texture tool restyle time | A few minutes per model; release announced as next week | Restyles existing content from a prompt; treat as announced until confirmed available. | [Roblox 2026-10 4:25](https://youtu.be/KB5iAzy86Fo?t=265) |
| Sprint speed set in prompt | 30 | Example of an exact value named in a build prompt (self-reported indie). | [SimTek Game Development 2026-09 2:01](https://youtu.be/-0H6JRtrA2Y?t=121) |
| Benchmark time budget per game | 1h, 2h, 3h, 4h | Escalating limits for four identical-prompt tests (low-advice, self-reported). | [MonarchDev 2026-10 1:23](https://youtu.be/QwdZRB6xRKk?t=83) |
| Fortnite-clone build time | ~2 hours | Time to generate animations and assets (low-advice, self-reported). | [MonarchDev 2026-10 3:41](https://youtu.be/QwdZRB6xRKk?t=221) |
| Model and effort for full builds | Claude Opus 5.5 at extra-high effort | Self-reported model choice; effort level is for full builds only. Check current model names. | [MonarchDev 2026-10 1:58](https://youtu.be/hPWJlFwp5Xs?t=118) |
| Token exhaustion | Ran out of tokens after asking for permission twice | Super Bullet build; some meshes came from free Creator Store models (low-advice). | [MonarchDev 2026-10 6:08](https://youtu.be/3bUysm7IFxg?t=368) |
| First-time builder growth since AI tools launched (Sept) | ~10x | Self-reported industry observation (low-advice). | [Deconstructor of Fun 2026-10 38:30](https://youtu.be/oU3oz6Ddz7g?t=2310) |
| Steam games with AI disclosure | ~10% (2024) to ~34% (2026 YTD) | Rising disclosure share on Steam (low-advice). | [Deconstructor of Fun 2026-10 24:31](https://youtu.be/NrPjXO_7oKk?t=1471) |
| Steam AI disclosure by category | Art 80%, audio 27%, text 21%, tech 14% | Share of disclosures per category (low-advice). | [Deconstructor of Fun 2026-10 25:52](https://youtu.be/NrPjXO_7oKk?t=1552) |
| Routine typing share of coding time (claim) | 70% routine, 30% hard problems | Tim Sweeney's claim about UE1 writing time; not a Roblox measurement (low-advice). | [Deconstructor of Fun 2026-10 19:59](https://youtu.be/NrPjXO_7oKk?t=1199) |
| 99 Nights in the Forest scale | 30B visits, 14M CCU, 3 developers | Original game stats cited as reference (low-advice). | [MonarchDev 2026-10 5:29](https://youtu.be/QwdZRB6xRKk?t=329) |
| Bloxburg reference | 10B visits, reportedly sold for $100M, 25 Robux entry until 2024 | Original game stats cited as reference; sale price is reported, not verified (low-advice). | [MonarchDev 2026-10 7:25](https://youtu.be/QwdZRB6xRKk?t=445) |
| Forza Horizon 6 first-week revenue reference | ~$325M | Non-Roblox benchmark, estimated real-world figure (low-advice). | [MonarchDev 2026-10 1:41](https://youtu.be/QwdZRB6xRKk?t=101) |
| Tripo model quality | 3.1 better than 2.5 Legacy; 2.5 Legacy works on free accounts but looks worse | Self-reported model comparison (indie). | [Xaiyne 2026-10 2:04](https://youtu.be/vGfWK6vbuYk?t=124) |
| AI corrections needed per generated script | ~1-2 corrections now vs nearly every line previously | Speaker's self-estimate for ChatGPT-written Roblox code, 2025-01. Shows improvement over time but still needs review. | [ByteBlox 2025-01 2:00](https://youtu.be/SCtYVCRVzM8?t=120) |
| Time lost to AI service downtime | ~40 minutes | DeepSeek busy-server errors before a working response, 2025-03. | [BloxxedDev 2025-03 0:28](https://youtu.be/CipKM4DBWxg?t=28), [BloxxedDev 2025-03 0:28](https://youtu.be/CipKM4DBWxg?t=28) |
| AI response time for a single-line change | ~40 seconds, adding ~26 lines | Duckable changing one line with AI, 2025-08. Explicit scope limits are needed to avoid extra edits. | [Duckable 2025-08 7:09](https://youtu.be/Em5H7sNWN7I?t=429) |
| AI generation time for large script requests | over 100 seconds | Large script tasks, 2025-08. Plan for long waits on big requests. | [Duckable 2025-08 7:09](https://youtu.be/Em5H7sNWN7I?t=429) |
| Time to fix fireworks system with AI | ~3 hours overnight | Iterative prompt-test cycles with waiting between tests, 2025-08. | [Duckable 2025-08 8:16](https://youtu.be/Em5H7sNWN7I?t=496) |

## Where creators agree
- TheDankDeveloper, MoseyTube and Tizzy agree AI speeds development and prototyping.
- TheDankDeveloper (T2404, T2527, T3300) repeatedly says one feature at a time with testing.
- TheDankDeveloper, MoseyTube and waveshine agree AI output needs debugging/understanding.
- kra_DeZ and waveshine agree you should understand the code.
- Template/generator plugins are endorsed by TheDankDeveloper and CallMeDogey.
- Roblox official frames AI as an extension of building blocks (Q420).
- Roblox official sources agree that Studio AI should absorb tedious bulk edits so creators can focus on creative work (T3612, T4263; Q718 frames it as a dishwasher for creativity).
- Roblox official sources agree on early, low-cost AI experimentation (T3620, Q720).
- Review and verify AI-generated code before trusting it: Roblox Creator Docs (T9539) and Duckable (T6762).
- Back up before AI edits existing projects: GuideRealm (T6870) and Roblox Creator Docs (T8589).
- Use AI for routine and placeholder work, and hand-build creative or complex parts: Roblox Creator Docs (T7718, T9865) and Duckable (T6764).
- Be specific and detailed in prompts: Roblox Creator Docs (T8236) and GuideRealm (T6864).
- MCP gives AI direct read/write access to the open project: Roblox Creator Docs (T9780) and Crusherfire (T6359).
- Official Roblox docs and indie creators agree that Assistant suits routine, repetitive setup while core design, lighting, terrain and gameplay stay hand-built (T15427, T13934).
- Official and indie sources agree on learning basic Luau before trusting AI output (T13990, T15199, T13958, T13639).
- Specific prompts naming the problem and target beat vague or whole-game prompts; build in stages (T13949, T13952, T13985, Q1459).
- ML or client-side checks are not anti-cheat; validate on the server (Q1236, existing server-validation rule).
- Creators agree AI-generated code must be understood and checked before use (RoyalDev T16626 supports the 'verify what you can read' rule already in the file).
- Creators agree that AI-generated 3D meshes need cleanup and triangle checks before they are used in game (Xaiyne T16763, T16772).
- AI accelerates Roblox development timelines: official survey figures (T17511, T17543) and the official quote on compressing idea-to-playable time (Q1760) agree.
- Build provides a prompt-to-game start with a handoff to Studio: indie reporting (T17501, T17539) matches official material (T17552).
- Build supports analytics and monetization in-tool: GamesBeat (T17539) and Investor Relations (T17552) agree.
- Build's scale and low barrier are confirmed by both PocketGamer.biz (self-reported, 9,000 games and 71% never used Studio) and Roblox Newsroom (official, same figures).
- Plan-then-execute with reversible steps is recommended: planning mode with editable to-dos (T17605, Q1780) and revert checkpoints (T17606).
- Multiple reference images improve visual consistency for generation (T17740, Q1794).
- Agents that play should see only what players see (T17750, Q1798).
- AI output is a rough first draft that needs manual polish for layout, balance and feel (SimTek, MonarchDev: T17893, T17908, Q1827).
- Creators should learn to use AI rather than avoid it; asking AI to explain its code is part of learning (SimTek, MonarchDev: Q1823, T17932).
- Detailed, specific prompts produce better output (MonarchDev: T17921, T17926).
- AI-generated Roblox code needs human correction before it works (ByteBlox, BloxxedDev, Duckable).
- Errors and failures should be sent back to the AI and tested, not accepted as-is (BloxxedDev, Duckable, ByteBlox).

## Where creators disagree
- **Incremental prompting vs one master prompt**
  - TheDankDeveloper: step by step, avoid one massive prompt (T3300, T2404)
  - MoseyTube: one long master prompt at ultra effort builds a foundation (T2852)
- **How much to rely on AI**
  - waveshine: use AI as tutor, not to generate systems you don't understand (T2893)
  - kra_DeZ and MoseyTube: AI built most of the game (Q597, Q498)
- **AI in player-facing creation**
  - Roblox official: promotes AI tools (Q420, N1300)
  - RobloxOfficial speaker: players said they did not want AI use (Q647, T3242)
- **How much code to let AI write**
  - Duckable: ask for pointers, type code by hand, use AI sparingly (T6761, T6763, T6764)
  - Crusherfire: write style rules as AI skills and have AI refactor old code; cut weeks to 1-2 days (T6906)
  - Roblox Creator Docs: use Assistant to modify scripts in place and optimize code instead of manually (T8246)
- **Whether Roblox Assistant saves time**
  - Roblox Creator Docs: Assistant handles routine tasks and frees time for creative work (T7718)
  - Duckable: 27-30 min per prompt and a failed Super Bullet build after 18 min on a $20 plan (N2888, N2887)
  - GuideRealm: a detailed master prompt built a draft in 7 min 18 s (N2945)
- **Whether a whole game can be built in one AI pass**
  - GuideRealm: detailed master prompt with extra high effort works (T6864, T6871)
  - Duckable: large systems stalled; build errored and left account in token debt (N2886, N2887)
- **Third-party MCP bridge vs built-in server**
  - Crusherfire (2025-11): custom npm bridge, port 3002, one agent at a time (T6360, T6363)
  - Roblox Creator Docs (2026-10): built-in Studio MCP, multiple Quick Connect clients (T9779, N3153)
- **Whether non-coders can rely on AI output**
  - MonarchDev (T13958): users without basic coding knowledge can still succeed, just more slowly.
  - VuukStudios (T13639): without scripting knowledge AI produces inaccurate code; avoid it for paid work.
  - Roblox Creator Docs (T13990, T15199): learn Luau and basic properties before accepting Assistant code.
- **AI for paid work**
  - VuukStudios (T13757, T13639): avoid AI for paid client commissions where originality matters.
  - MonarchDev (T13798): AI coding tools are a practical advantage for solo developers building shops and save systems. This is a scope difference (own projects vs client work), not a direct contradiction.
- **Scale of Build output**
  - GamesBeat (indie, self-reported): about 9,000 games published since the NZ alpha (N7247).
  - Roblox Investor Relations (official): 70,000+ games published by 500,000+ users (N7259).
- **Use of mobile Build for testing and monetization**
  - Existing knowledge rule: use mobile Build for reviews and small edits only.
  - Roblox Newsroom (T17682, 2026-09, official): mobile Build can be used to test ideas quickly, analyze and add monetization, with in-app ad launches planned.
  - Resolution: prefer the newer Sept 2026 official guidance; the older rule is outdated for idea testing and monetization, though heavier editing still belongs in Studio.
- **Whether AI-built games will be noticed by players**
  - MonarchDev: AI-only output without fidelity checks tends to look noticeably worse (T17909).
  - Deconstructor of Fun: as mods and decompilations improve, players will stop noticing when AI was used (Q1843).
- **Role of AI when learning Roblox scripting**
  - Existing knowledge file: 'Understand the code; use AI as a tutor' (prior creator, unnamed).
  - Duckable (T18281, Q1860, 2025-08): AI is a tool, not a teacher; review and rewrite generated code yourself, and Vibe Coder helps make games rather than create them.
- **Whether AI should propose or configure game balance and prices**
  - janisjanis01 (T18616, 2025-12): used AI balancing advice for tuning.
  - janisjanis01 (T18723, Q1930, 2026-10): never let AI configure balance; AI-configured upgrades were a time sink.
  - Existing knowledge-file rule 'Use AI to propose balanced tycoon button prices' conflicts with the newer janisjanis01 view; prefer the 2026-10 advice and qualify the older rule.

## Date context (what may be outdated)
- 2018 localization, shadow-baking items are old; the localization APIs have likely evolved.
- AI tool advice is from 2025-2026 and changes fast; plan limits, pricing and MCP setup steps may shift.
- Earlier 2025 advice used plugins like Lemonade; by 2026 MCP-connected Claude/Codex are common (T2539, T3256).
- Prefer official statements for Studio mechanics; indie time-saved and usage numbers are unverified.
- Sept 2024 Roblox talk (T3612-T3621, N1599-N1603, Q718-Q720) predates the Oct 2026 Creator Docs (T4263, T4284, T4692). Where they conflict, prefer the 2026 docs; no direct conflict found.
- T3615 says region selection and image inputs for gen tools were 'coming' as of Sept 2024. Treat as possibly shipped by 2026; verify before advising.
- N1599 and N1600 are 2024 usage stats and may be outdated.
- Official Roblox docs (2026-10) supersede indie workflows: prefer the built-in Studio MCP server (T9779, T9780) over the 2025-11 custom npm bridge (T6359-T6363).
- Duckable (2026-09) costs, credits and Assistant speed (N2886-N2890) predate official 2026-10 limits (N3268, N3317); pricing and credits are volatile, so re-check.
- Items dated 2017 (T4924, T4925, N2214) concern old exporter and Animation Editor behaviour; verify against current Studio.
- FastCast Redux advice (T5293, 2020) needs a check that the module is still maintained.
- Beta features may change: Script Sync (T9027), Assets API endpoints (T9275, T9283), and Beta Features MCP toggles (T9779).
- Code Assist daily cap is stated without a number (N3784); check current limits.
- Official 2026-10 Assistant and mesh caps (N3317-N3320) may change with rollout (N3269).
- Newest guidance is Roblox Creator Docs (Oct 2026). Where older indie advice conflicts, prefer official: Assistant should be opened inside Studio (T13983), not the web version.
- Official docs now document Texture Generator Fast and Quality modes (N5735-N5737). The AI texture crash in T12686 (Apr 2025) predates that; AI texture reliability may have changed, but keep a fallback.
- Packet (T12644, Mar 2025) is newer networking advice than general RemoteEvent wrappers (T11994, Jan 2024); the two are complementary, not conflicting.
- Audio Discovery (T11322) deadline was March 22, 2022, which has passed; no action needed now.
- Justice (T10931, Feb 2021) was pre-release; verify its current status before use.
- The utility plugin list (T10993, Mar 2021) and the 2021-era plugin advice may be outdated; check current versions.
- Beta features (Animation Graph T13243 Apr 2026; multi-line Command Bar T14655; glTF export N6056; AvatarAbilities autocomplete T13206 Feb 2026) may change or be removed; don't present them as stable.
- Age Check API (T13334, Apr 2026) and OAuth/skills/Open Cloud scoping (Oct 2026) are newer than most of the older advice in this topic.
-  ML obby examples (T11995, T12000, 2024) are small-scale demos and should not be generalized.
- Rojo advice dates from 2022-11 (T15982-T15984), with plugin version 7. Studio now ships built-in Script Sync, which the existing file already prefers for external editors, so treat Rojo as a legacy or alternative option.
- Feature-flag advice (T15971) is from 2022-09 and may not reflect current Studio behavior.
- Image-to-3D advice (T16763, T16766, T16772) is from 2026-10. The speaker said older AI models were too poor to sell, so newer models are the baseline.
- IKControl bounty (N6244) was posted 2023-01 and listed as still open; verify status.
- Plugin advice (Reclass, Scribe Studio) is self-reported and may be finicky or out of date with current Studio versions.
- July 2026: Build was NZ-only alpha (T17501); agent roles were announced as upcoming (T17512); 95% AI-timeline stat (T17511).
- Sept 2026: Build expanded to Serbia and Singapore (N7249); mobile authoring and monetization added; free base tier with paid prompt-capacity tiers (T17552); Scene Generator announced (T17539); 97% stat replaces 95% (T17543).
- Sept 2026 sources are the newest in this batch; agent and Scene Generator availability remains unconfirmed.
- Q1760 claims faster idea-to-playable and cross-device adaptation with no numbers; treat as direction, not benchmark.
- As of 2026-11-01: Unified agentic permission (announced for late 2026, T17639) will govern what Assistant, MCP, Plugins and OCALE can access. Not yet confirmed as shipped; check permission settings before assuming scope.
- NPC Dynamic Behavior (T17657) is announced for late 2026. Verify it is available in your Studio build before planning around it.
- Studio texture tool (N7578) was announced as releasing 'next week' in Oct 2026. Treat as likely released but verify.
- Build figures (~9,000 games, 71% new to Studio) are dated through Sept 1, 2026 and will change; re-check before quoting.
- Oct 2026 generation quotas and concurrency (N7584 to N7586) are approximate and plan-dependent; verify current values.
- Newer advice supersedes the older mobile Build rule (see disagreements).
- 2026-09 (SimTek): Roblox Assistant Agent mode can edit scripts and the place. This extends the older 'Assistant only' advice; prefer it where available.
- 2026-10 (MonarchDev): MCP setup walkthrough via Creator Hub API key, then the AI client, then Studio. It refines the older 'connect via MCP' rule without conflicting with it.
- 2026-10 (Xaiyne): Tripo 3.1 supersedes 2.5 Legacy for quality. Legacy remains usable on free accounts.
- 2026-10 (MonarchDev): Claude Opus 5.5 extra-high effort is the model cited for full builds. Model names change quickly, so verify current options as of 2026-11.
- 2026-10 (Deconstructor of Fun): Steam AI disclosure share has risen sharply, from ~10% in 2024 to ~34% in 2026 YTD. Verify current Steam policy before relying on it.
- Sept 2026 is the launch reference point for the reported ~10x growth in first-time builders.
- Model names in these notes (ChatGPT, DeepSeek, Claude 3.7) are from 2025 and are outdated as of 2026-11. Re-benchmark current models before choosing one.
- ByteBlox (2025-01) reported far fewer corrections than earlier. Newer models may be better still, but the review requirement stands.
- Outage and response-time figures (2025-03 and 2025-08) are self-reported and may not reflect current service reliability.
- Duckable's Vibe Coder notes (2025-08) describe a tool whose features may have changed.
- janisjanis01's 2026-10 advice (T18723, Q1930) supersedes their 2025-12 use of AI balancing advice (T18616). Prefer the newer view: do not let AI set balance.
- The existing rule 'Use AI to propose balanced tycoon button prices' should be qualified as a suggestion only, with human review and tuning in Configs.

## Instructions for an agent using this file
- If asked to build a game with AI, then split into one mechanic per prompt and playtest between each.
- If a generated script errors, then paste the exact error back and ask for a fix.
- If setting up an external LLM, then enable Studio as an MCP server in Assistant settings and verify the green indicator.
- If generating UI with a reference, then supply a full-screen screenshot.
- If the user hits usage limits, then suggest a higher tier or batching prompts, noting costs are self-reported.
- If the user wants to learn Luau, then recommend using AI as a tutor and reading the docs.
- If publishing AI-made assets, then warn that copyright may not apply to raw AI output and players may dislike AI use.
- If integrating an in-game LLM, then require JSON with a fixed action set and theme validation.
- If combat is being tested, then add health display first.
- If quoting time-saved or revenue claims from indie creators, then label them unverified.
- If a task involves many repetitive Studio edits, then propose Assistant actions before manual steps.
- If asked to generate a script with Assistant, then write a pseudo-code prompt and review the output before running it.
- If generated output keeps missing, then narrow the scope and regenerate rather than re-rolling the same broad prompt.
- If debugging unfamiliar code, then use Studio code explanation before changing anything.
- If onboarding or tuning values are hardcoded, then recommend moving them into Configs and Experiments.
- If asked whether an experience uses AI for a disclosure, then base the answer on player-facing generative AI, not development use.
- If a user is new to AI tools, then encourage early, cheap experiments and treat failures as useful.
- If a user asks how to connect Claude or Codex to Studio, recommend the built-in Studio MCP server (Manage MCP Servers, Beta Features). Use a custom bridge only if the built-in one is unavailable.
- If an AI action will edit an existing place or run a conversion skill, first tell the user to back up via File > Publish to Roblox As.
- If a request is a whole-game build, use a master prompt listing map, systems, persistence, offline earnings and mobile controls, with extra high effort; use medium for simple queries.
- If the user is learning a system, give pointers and direction instead of full code, and ask them to type suggested code by hand.
- If generating a mesh, require a selected Part for the bounding box, one input type (text or reference image), and the 10,000-triangle default unless asked otherwise.
- If generating icons or thumbnails, specify 512x512 or 1920x1080 and tell the user to add text in an editor.
- If setting up Open Cloud, start with an API key, test endpoints in Postman, grant least-privilege scopes, and move to OAuth 2.0 for user-authorized apps.
- If in-game LLM text will be shown to players, pass it through TextService:FilterStringAsync() and constrain the output.
- If writing remote handlers, validate every client-sent value on the server.
- If Assistant output is truncated, click Continue; for complex requests, use Plan mode before Build.
- If a user asks Assistant to build a whole game or write paid client code, advise against it and recommend staged, human-reviewed building.
- If generated output is wrong, reword the prompt and re-run; don't keep patching blindly (T13987, T14514).
- If a session is long (around 900k of 1M tokens) or code looks stale, compress it or start fresh with current scripts and Explorer layout pasted in (T13955, T13736).
- If the user doesn't know Luau, teach the relevant basics before accepting Assistant code (T13990, T13958).
- If the user asks about anti-cheat, say ML and client-side checks are not anti-cheat and move validation to the server (Q1236).
- For Open Cloud or OAuth, scope the minimum permissions, confirm analytics access, and follow the registration and review steps (T14024, T14997, T15002).
- Before using Try it out on an endpoint, check its risk level and never test Critical or destructive endpoints on live data (T14952, N5885).
- For plugin widgets, follow the parenting, theme and input rules; don't call CreateDockWidgetPluginGui from regular scripts (T15553).
- When official 2026 guidance conflicts with older indie advice, prefer the official guidance and say so.
- Label beta features as subject to change and don't recommend them for shipping production systems.
- If a user asks to sync code from an external editor, recommend Script Sync first, then mention Rojo as an alternative with its 2022 version caveat.
- If a user asks to test a feature-flag change, tell them to use a duplicate place and back up first.
- If a user asks for AI-generated code for boilerplate, confirm they can read and verify the output before using it.
- If a user asks about UGC mesh generation, recommend a current image-to-3D model, HD setting, 2K texture, PBR off, and a triangle count under 4,000 (verify official limit).
- If a user asks about a live-data inspector plugin, name the plugin, warn it may be finicky, and offer a fallback.
- If a user asks about CFrame or trig math for VFX, offer AI help but advise a visual test in Studio.
- If a user asks about a bounty, state the source is from 2023 and the status must be checked.
- If the user's region is not in Build's listed alpha regions, do not recommend Build; use Studio, Assistant, and MCP.
- If the user wants a quick prototype from a prompt, suggest Build first, then Studio refinement (T17539).
- Do not state that Playtesting, Analytics, or Experiment agents are available; describe them as announced and upcoming (T17512).
- Prefer official figures (N7259, T17543, N7258) over indie figures (N7247, N7248) when citing scale.
- Describe survey and self-reported stats as sentiment or claims, not measured benchmarks of game quality.
- When a user asks about scale, note the scope and date of each figure, since N7247 and N7259 differ.
- Always pair Build-generated or Scene Generator output with Studio verification and a backup first.
- Use Studio MCP (T17544) as the default route for connecting external AI tools to a project.
- If a user asks for multi-step Assistant work, first produce or review the to-do list and confirm steps before running agents.
- If a user is about to run unattended asset pipelines, require a model-per-task playbook and scoped API keys first.
- If a user asks about NPC behavior generation, explain that behavior trees are inspectable and editable, and check availability for late 2026 features.
- If a user asks for a visual style match, recommend several reference images in one request, and use meshes rather than procedural models when fidelity matters.
- If a user asks about quotas or throughput, quote the approximate figures and flag that they are approximate and plan-dependent.
- If a user asks about mobile Build for testing or monetization, use the Sept 2026 official guidance and note it supersedes the older rule.
- If a user needs playtest bots, prefer player-visible-only agents and say what they cannot see.
- Do not describe announced late-2026 features (unified permissions, NPC Dynamic Behavior, texture tool) as available without verification.
- If the user wants many script edits by Assistant, enable per-change review. If not possible, accept all and check the diff right after.
- If the AI returns a partial code diff, request the full replacement script before pasting it.
- If the user connects MCP, verify the link by asking the AI which place it sees before running any edit.
- If the user is comparing AI tools, fix the prompt text and time budget and keep them identical across runs.
- If output is wrong, ask for the feel and reference-game structure in detail rather than a vague retry.
- If writing a build prompt, include named parts, scale and exact numeric values.
- If the user plans to ship on Steam, flag that generative art, audio, voice, localized text and store assets require disclosure; coding assistance is exempt.
- Do not present low-advice revenue or visit figures as Roblox benchmarks without verification. Label them as self-reported.
- Prefer Tripo 3.1 over 2.5 Legacy when the user asks about image-to-3D mesh quality.
- Treat AI output as a first draft; recommend playtesting and fidelity checks before shipping.
- If a model repeats the same error after correction, switch to a stronger model instead of retrying with the same one.
- If the AI service returns busy or timeout errors, switch to the backup tool rather than waiting in a loop.
- When asked to fix a small thing, state the exact line and expect extra lines; diff and reject unrelated changes.
- After AI writes a listener or event handler, check that objects already in the workspace are also handled.
- Strip excess comments from AI scripts only when asked, and keep the script readable for review.
- For balance values such as tycoon prices, propose a curve from AI but mark it as unverified until a playtest confirms it.
- Do not treat AI output as a finished product; review and rewrite before shipping.
- If the user asks AI to set upgrade costs, prices, or balance values, warn that AI-configured upgrades were a time sink (T18723, Q1930) and suggest a human-set table in Configs instead.
- If the user asks for AI help with UI vectors or icons, say to expect to modify the output before use (T18616).
- If the user asks how to speed up require lines or module navigation, give the File > Advanced > Customize Shortcuts path to bind Go To Module, and pair it with Require Autocomplete (T18519, T18522).

## Not covered here (research elsewhere)
- No detail on Studio Assistant's exact prompts, limits or pricing.
- No security or privacy guidance for MCP access.
- No official guidance on Roblox policy for AI-generated content and moderation.
- No benchmarks comparing AI models for Luau quality.
- No coverage of version control or backups when AI edits a place.
- Localization APIs currently in use are not covered beyond 2018.
- Whether direct region selection and image inputs for Studio generation tools have shipped (T3615 says 'coming').
- Assistant accuracy, error rates, or quality benchmarks; the 60%/80% figures measure output volume only (N1599, N1600).
- Pricing, usage limits, or quotas for Assistant and generation tools.
- Setup details and limits for Roblox Configs and Experiments (T4284 is a single mention).
- Which open models were tested and how they compared (T3620 does not name them).
- Accessibility feature requests via DevForum (T3495, Q698) were not added because they fall outside the AI and tools topic.
- No current cost or performance comparison across Assistant, Claude, Codex, Meshie.ai and ChatGPT.
- No Open Cloud rate limits or quotas.
- No stability data for Script Sync or Assets API beyond beta labels.
- Code Assist daily cap number is not given.
- No IP or licensing status for Meshie.ai, ChatGPT or Assistant-generated assets.
- No measured gameplay quality, frame time or memory impact of AI-generated code.
- Toolbox recovery steps are cited for Windows and Mac only; untested on other setups.
- No guidance on LLM NPC cost, latency or moderation beyond TextService filtering.
- Indie claims (Crusherfire, GuideRealm, Duckable) are self-reported and unverified.
- Assistant quotas, pricing and usage limits beyond the general AI-budget rule.
- Roblox policy on AI-generated content, copyright and monetization (only player sentiment is covered).
- Quantitative quality benchmarks for Assistant or procedural model/mesh output.
- Full skill authoring beyond naming, description and duplication.
- Full MCP security and trust model setup for external agents.
- Age Check policy, compliance and failure handling beyond PromptAgeCheck and AgeChecked.
- Speech-to-text pricing, limits and accuracy for Voice Chat.
- NPC animation details (animateNPC, copying the Animate script, R6 vs R15 specifics) from T10649, T11346, T14440 were not fully vetted.
- Beta feature stability and deprecation timelines.
- Plugin specifics not verified here (Justice internals, Library/CPI import steps, SmoothChase docs).
- Performance numbers comparing Packet against RemoteEvents or other networking libraries.
- No official Roblox docs were provided to confirm the 4,000 triangle limit or the current UGC mesh rules.
- No pricing or credit figures were given for Tripo AI or Plasticity beyond 'substantially more' and 'one-time purchase'.
- Current Rojo compatibility with latest Studio builds was not verified.
- Scribe Studio and Reclass plugin availability and current behavior are not documented here.
- Rebirth AI pricing, limits and accuracy are not covered.
- Status of the IKControl bounty (N6244) as of today is not confirmed.
- Official guidance on feature-flag safety in Studio is not provided.
- Build pricing, prompt-capacity limits per tier, and what the free base tier covers.
- Full region list and expansion timeline beyond New Zealand, Serbia, and Singapore.
- Whether Build output is editable as native Studio content, export format, and known limitations.
- Release dates and scope for Playtesting, Analytics, and Experiment agents, and for Scene Generator.
- Quality and reliability of Build and Scene Generator output compared with Studio Assistant.
- Licensing and copyright status of Build-generated content and assets.
- Player sentiment toward Build-made games (existing rule covers general AI sentiment only).
- Mobile authoring limits and what features are desktop-only.
- How the 9,000 (indie) and 70,000+ (official) published-game figures reconcile in scope and time.
- Cube tool details and its licensing; the N7224 figures are not explained.
- Pricing, credits and plan tiers for Build, generation quotas and the $200 plan usage limits beyond the figures above.
- Exact setup steps for the Scene Analysis skills and the runtime bridge (tool names, configuration, permissions).
- Details of the unified agentic permission system (scopes, UI, rollout dates).
- Exact attribute names and tags for the 4D behavior library, and the referenced reference experience.
- Availability and access criteria for the imitation-learning human-like agents for creators.
- Texture tool capabilities, supported inputs and limits after release.
- Build's ad launch and monetization timeline and revenue terms.
- Best practices for auditing unattended AI pipeline output and cost control beyond what is listed.
- No official Roblox documentation on Assistant Agent mode limits, token pricing or diff-review UI; verify on the Creator Hub before advising.
- No DevForum or official evidence in these notes for the Creator Hub MCP setup steps; they are indie walkthroughs.
- No measured quality or reliability data for AI tools; all benchmark and revenue figures are self-reported and mostly low-advice.
- No comparison of Tripo against other image-to-3D tools.
- No Roblox-specific AI disclosure or moderation policy; the Steam disclosure figures are not Roblox policy.
- No cost data per build or per token; the Opus 5.5 effort guidance has no price context.
- No evidence on how AI-built experiences perform on Roblox engagement or monetization.
- No official Roblox documentation or DevForum sources are cited for AI tool reliability, outages, or model quality.
- No measured benchmarks comparing current AI models on Roblox scripting tasks (accuracy, cost, latency).
- No details on Vibe Coder features, pricing, or how it differs from Studio Assistant or MCP.
- No methodology for balancing tycoon prices with AI beyond the single mention.
- No data on how often AI service outages occur or how to choose a backup tool.
- Fireworks and carry-script examples lack code, so reusable patterns are unclear.
- No time or cost figures for AI iteration on balance or upgrade systems.
- No guidance on what replaces AI-proposed balance (for example playtest data or analytics).
- Go To Module plugin version, availability, and default-shortcut status are self-reported and not verified against official docs.
- No official Roblox docs cited on AI config or balance in these notes.

## Quotes (near-verbatim)
- "Please use the DevForum to either show your support for feature requests related to accessibility or make those requests directly." ([Roblox Creators 2023-05 1:00:04](https://youtu.be/K1pEI6LVJJA?t=3604))
- "this is NOT a proper anti-cheat for your games!" ([Roblox DevForum 2024-01 ](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460))
- "you'd be better off not using ML in this example, but there are plenty of situations where you definitely could & should" ([Roblox DevForum 2024-01 ](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460))
- "We want to be basically your dishwasher, so we want to let you focus on creativity." ([Roblox 2024-09 4:51](https://youtu.be/XrxUy51NsvI?t=291))
- "Start early, fail early, play around." ([Roblox 2024-09 27:17](https://youtu.be/XrxUy51NsvI?t=1637))
- "The AI put it in the wrong order; it listens for future coins, so the coins already added never worked." ([ByteBlox 2025-01 7:52](https://youtu.be/SCtYVCRVzM8?t=472))
- "We will never implement an AI algorithm unless it is more accurate than humans." ([Roblox 2025-07 2:26](https://youtu.be/ckNAwhl-n0g?t=146))
- "AI is a tool, not a teacher. Vibe Coder is a very handy tool for helping make Roblox games, not for creating them." ([Duckable 2025-08 12:11](https://youtu.be/Em5H7sNWN7I?t=731))
- "We view AI as nothing but an extension of [the] building blocks. We hope that it'll be a power up for you all." ([Roblox 2025-09 4:24](https://youtu.be/3h25HUtBHFk?t=264))
- "Use AI as a tool to help guide you... make a full roadmap... Obviously don't use AI to make full entire scripts for you." ([VuukStudios 2025-11 12:25](https://youtu.be/U4nduRcszJ4?t=745))
- "Lemonade is a really powerful tool. Most of the game was made by Lemonade." ([TheDankDeveloper 2026-01 10:52](https://youtu.be/BYhhm9o3H_E?t=652))
- "I didn't have to paste any scripts or anything. I think it did everything for me." ([TheDankDeveloper 2026-01 4:38](https://youtu.be/BYhhm9o3H_E?t=278))
- "none of them really match my game, so I don't think I'll be taking any of them." ([TheDankDeveloper 2026-04 4:44](https://youtu.be/i5sldtdF8m0?t=284))
- "now that my game is full of UI, it's kind of hard to change." ([TheDankDeveloper 2026-04 4:44](https://youtu.be/i5sldtdF8m0?t=284))
- "The magical of the planning mode is to understand the creator intent and give creator control." ([Roblox 2026-04 12:26](https://youtu.be/8IcYpOl4Sdk?t=746))
- "So, all this has to do is start the 1-hour timer and press enter." ([TheDankDeveloper 2026-04 0:00](https://youtu.be/Ufr0SVq-o98?t=0))
- "the thing with Gemini is I actually have to import everything myself." ([TheDankDeveloper 2026-04 7:27](https://youtu.be/Ufr0SVq-o98?t=447))
- "I'm saving probably 80% of the time I'd normally spend scripting. Things that would probably take me a whole day are getting done in like 20 minutes." ([MoseyTube 2026-04 2:04](https://youtu.be/sFr7htxsnR4?t=124))
- "AI didn't make me dumber. It just made me forget how it felt to struggle." ([Duckable 2026-08 21:21](https://youtu.be/Cc7HT3uNjeQ?t=1281))
- "We're not using AI to make art assets... we use it to help fill the gaps with our programmers for speed." ([Business of Creators 2026-08 21:06](https://youtu.be/lpIzMycpiKo?t=1266))
- "Most of this game is made using like Claude... Most of it was literally just AI." ([kra_DeZ 2026-08 10:11](https://youtu.be/oMI-GhUcfFE?t=611))
- "If you're getting advanced code from these systems, there's zero debugging capability that you have." ([RoyalDev 2026-08 0:40](https://youtu.be/erhgduyGzdM?t=40))
- "it can replace a ton of packages in your workflow, honestly. And this is what I've been using for a while now, and I love it." ([Possible Panda 2026-09 9:12](https://youtu.be/KVmPyoOPmRI?t=552))
- "if you're worried about losing your job as a programmer to AI, the best thing you can do is learn how to use AI" ([SimTek Game Development 2026-09 0:00](https://youtu.be/-0H6JRtrA2Y?t=0))
- "The time it takes to go from an idea to a playable game is compressing dramatically, and so is the time it takes to adapt a game for new devices." ([Roblox Investor Relations 2026-09 ](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm))
- "Stop making AI slop... this means stop producing and misusing the AI." ([VuukStudios 2026-10 10:49](https://youtu.be/0ENzqNB_EUo?t=649))
- "What works really well is when you're working with MCP is to give it several images and to tell it, hey, this is the style that I want." ([Roblox 2026-10 42:39](https://youtu.be/QhZpK2hdnjE?t=2559))
- "it actually doesn't cheat. It doesn't see for instance you're in the same server as all the players." ([Roblox 2026-10 19:19](https://youtu.be/QvNAMmGqdd4?t=1159))
- "It doesn't mean you can just sit back and have everything ready... it's important that you, as a creator, put your own mind into it." ([MonarchDev 2026-10 11:32](https://youtu.be/QwdZRB6xRKk?t=692))
- "Most AI models, even connected to MCP, can't do that just yet. And when they do, it's not the quality you expect." ([MonarchDev 2026-10 10:50](https://youtu.be/QwdZRB6xRKk?t=650))
- "We always prefer to build on top of Roblox's analytic stack instead of rebuilding the basics ourselves." ([Roblox 2026-10 15:27](https://youtu.be/bVU69VImiEc?t=927))
- "Players told me that they were not artists and they wanted help in creating their vision, but they were also clear about not wanting AI use." ([Roblox 2026-10 17:41](https://youtu.be/gCp4zzjjJ14?t=1061))
- "As you get better at it, each time ask it to explain how it did a particular thing." ([MonarchDev 2026-10 8:22](https://youtu.be/hPWJlFwp5Xs?t=502))
- "I'm going to be doing everything step-by-step like I showed you guys in my last video." ([TheDankDeveloper 2026-10 0:00](https://youtu.be/Mftq7v8nAcs?t=0))
- "I think the AI is doing a pretty good job." ([TheDankDeveloper 2026-10 4:50](https://youtu.be/Mftq7v8nAcs?t=290))
- "I'm never letting AI configure this again. It's a nightmare." ([janisjanis01 2026-10 8:57](https://youtu.be/A2QD-eT3IG0?t=537))
- "You can't simply say, "Oh, yeah, make this better." What does it even mean?" ([MonarchDev 2026-10 2:26](https://youtu.be/WA4RzzT39Dw?t=146))
- "As the mods or decompilings get better and better, players are going to stop being able to notice when it is because AI used to equal slop." ([Deconstructor of Fun 2026-10 33:27](https://youtu.be/NrPjXO_7oKk?t=2007))

## Verified additions

_Hand-added, labelled and sourced rows kept in `youtube-learn/supplements/topics/ai-and-tools.md`; they survive rebuilds._
- **Cube and Studio AI as of RDC26** (official, 2026-09): Cube 3D/4D generates functional objects (segmented parts with scripts, e.g. drivable boats, windmills) rather than static meshes; Scene Generation (late 2026) builds a layout from an image; NPC Dynamic Behavior (late 2026) creates NPCs from prompts in Studio, editable and versioned; three NPC layers (default behaviour trees, dynamic runtime behaviour limited to an allowlist of actions, human-like gameplay model); Character Control Library v2 for NPCs presented as 2-4x more efficient than Humanoid. Sources: [DevForum RDC26: What We Announced 2026-09](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880), [Building 3D Worlds with AI RDC26](https://www.youtube.com/watch?v=QhZpK2hdnjE), [Fast Path to Smarter NPCs RDC26](https://www.youtube.com/watch?v=QvNAMmGqdd4), [Tech Talks EP32](https://www.youtube.com/watch?v=8Djgx0jEyfs). Newest source 2026-09.

## Appendix: every extracted tip on this topic

- 2017-03-30 Roblox DevForum [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729): Use the latest plugin and addon versions; incompatible versions cause errors. An error mentioning object.name = partnames[-index] means the addon is outdated.
- 2017-03-30 Roblox DevForum [page](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729): Check that the rig shows no warnings in the exporter plugin, and that it loads in the default Roblox Animation Editor, which gives clearer error messages.
- 2018-07-24 Roblox [13:24](https://youtu.be/qoWMP-AFT08?t=804): Leave roughly 30-50% extra space for long-text languages and up to 2-3x for short strings; plan UI for text overflow.
- 2018-07-24 Roblox [19:26](https://youtu.be/qoWMP-AFT08?t=1166): Automatic translation can't handle typewriter text or incomplete strings and breaks when source text changes; use it as a fallback and move to localization APIs for maintained games.
- 2018-07-24 Roblox [34:04](https://youtu.be/u0SxwDxFQB8?t=2044): Bake shadows by painting them in 3D Coat, ZBrush, Maya or Blender for discrete control, or use Studio's real-time lighting where it can change.
- 2019-09-22 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-requests-simple-powerful-http-in-roblox/355294): Use a wrapper library like Roblox Requests instead of raw HttpService to cut boilerplate for HTTP calls, per the author's stated main purpose.
- 2020-05-02 GnomeCode [0:52](https://youtu.be/uF-BGGv6otQ?t=52): Copy the default Animate LocalScript from the character into a server Script so NPC animations play when no player controls it.
- 2020-05-18 Roblox DevForum [page](https://devforum.roblox.com/t/writing-an-fps-framework-part-2-2020/581791): Use FastCast Redux for raycast-based bullets with bullet drop; gravity values of -100 to -500 work well.
- 2021-02-05 Roblox DevForum [page](https://devforum.roblox.com/t/justice-the-awesome-npc-system/1026927): Treat Justice as a starting point: it is pre-release and designed to be heavily modified before use in a full game.
- 2021-03-27 Roblox DevForum [page](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437): Search scripts for fenv, RoSync, require, and loadstring via View > Find Results to spot common virus code; not every hit is malicious.
- 2021-03-27 Roblox DevForum [page](https://devforum.roblox.com/t/developing-expert-developers-advice-from-all-around-the-world/1134437): Use plugins such as Developer Tools, Auto Anchor, AutoScale Lite, and Stravant's Model Reflect and ResizeAlign to speed building and GUI scaling.
- 2021-11-13 Roblox DevForum [page](https://devforum.roblox.com/t/dynamic-weather-library-beta-10/1547614): Import the module into ReplicatedStorage, open Library, drag the CPI folder contents into matching services (Workspace, ServerScriptService, etc.).
- 2022-01-14 Roblox DevForum [page](https://devforum.roblox.com/t/how-exploits-work-and-how-to-combat-them/1627229): Assume the client is hostile: never trust client-sent data; validate everything in remote handlers on the server.
- 2022-02-26 Roblox DevForum [page](https://devforum.roblox.com/t/my-intro-to-raycasting-what-why-and-how/1681977): Use raycasts for NPC line-of-sight checks, asking whether a player is visible before the NPC reacts.
- 2022-03-16 Roblox DevForum [page](https://devforum.roblox.com/t/update-changes-to-asset-privacy-for-audio/1715717): Use the Audio Discovery plugin in Studio to review ownership of all audio assets in your experience before the March 22 deadline.
- 2022-04-18 Roblox DevForum [page](https://devforum.roblox.com/t/benis-pathfinding-customizable-easy-to-use-auto-animating-r6-r15-support/1759994): Set animateNPC to true to auto-animate the NPC; works with both R6 and R15 rigs.
- 2022-09-19 TheNexusAvenger [2:15](https://youtu.be/C4ASAayPpkY?t=135): Feature-flag editing risks data corruption and unstable Studio; only do it on a copy of your place, never live data.
- 2022-11-23 Dev Total [1:47](https://youtu.be/0K-5sifYhxs?t=107): Install the Rojo VS Code extension (by Avera) and use the command palette (Ctrl+Shift+P) to run Rojo init and build the place file.
- 2022-11-23 Dev Total [8:35](https://youtu.be/0K-5sifYhxs?t=515): Install the Rojo plugin (version 7) in Roblox Studio, start the Rojo server from VS Code, and click Connect so edits sync live.
- 2022-11-23 Dev Total [12:05](https://youtu.be/0K-5sifYhxs?t=725): Write code in VS Code, not Studio; Rojo syncs saved changes into Studio immediately.
- 2023-04-13 Roblox Creators [5:37](https://youtu.be/syQcaeRqqc4?t=337): Use Adobe's color tools (color picker with contrast suggestions) to find contrasting color pairs quickly.
- 2023-05-18 Roblox Creators [1:00:04](https://youtu.be/K1pEI6LVJJA?t=3604): Use Roblox DevForum to request or upvote accessibility features like a color contrast checker and text-to-speech API.
- 2023-11-02 Roblox DevForum [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585): Use the open-source modules BridgeNet2, TopbarPlus, ProfileService and similar rather than rebuilding them; keep only one copy in the project.
- 2024-01-07 Suphi Kaner [0:00](https://youtu.be/A14qFAyFYhQ?t=0): Suphi's RemoteFunction module (Toolbox, creator 5UPI) wraps remote request/response with timeouts and nil-return handling; a ready-made alternative to hand-rolling it.
- 2024-01-07 Roblox DevForum [page](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460): Use ML only where it fits; for a simple obby exploit check, invisible checkpoints are more practical than an ML model.
- 2024-01-07 Roblox DevForum [page](https://devforum.roblox.com/t/lets-teach-an-ai-to-catch-exploiters/2783460): Expect real-world data to outperform synthetic noise; the author's noise-augmented model reached ~85% test accuracy and says player-generated data is much better.
- 2024-05-30 Crusherfire [0:34](https://youtu.be/yncfwrBAWVw?t=34): Assign a keyboard shortcut to the Go To Module plugin via File > Advanced > Customize Shortcuts; it has none by default (demo used Ctrl+Q).
- 2024-05-30 Crusherfire [4:53](https://youtu.be/yncfwrBAWVw?t=293): Pair Go To Module with Require Autocomplete to insert require lines quickly and then jump to those modules.
- 2024-07-16 TheDankDeveloper [0:40](https://youtu.be/maRjVb1NAYc?t=40): Start from a template plugin (Generate a Simulator) to get scripted core mechanics quickly, then reskin art, UI and maps yourself.
- 2024-09-23 Roblox [1:42](https://youtu.be/XrxUy51NsvI?t=102): Use Assistant actions for bulk, tedious Studio edits like placing hundreds of trees, renaming, grouping into folders, or selecting by property criteria, instead of doing them manually.
- 2024-09-23 Roblox [9:45](https://youtu.be/XrxUy51NsvI?t=585): Write detailed pseudo-code-style prompts for Assistant; a ~10-line prompt can yield ~100 lines of script, per the speaker.
- 2024-09-23 Roblox [4:51](https://youtu.be/XrxUy51NsvI?t=291): Gen tools feel like a slot machine without control; the speaker says direct region selection and image inputs are coming to reduce re-rolling.
- 2024-09-23 Roblox [27:17](https://youtu.be/XrxUy51NsvI?t=1637): Start early, fail early, and experiment with open models; the fireside guest says teams must first fully embrace AI before it changes workflows.
- 2024-09-23 Roblox [33:37](https://youtu.be/XrxUy51NsvI?t=2017): Use Studio autocomplete and code explanation for debugging; the speaker says code explanation is among the highest-rated features.
- 2024-09-23 Roblox [22:10](https://youtu.be/vWx8UTxsi0A?t=1330): Use the Celestial Body Dragger plugin to move the sun or moon by mouse instead of tuning time of day and latitude.
- 2024-10-10 Suphi Kaner [8:26](https://youtu.be/ZPviBfpPloE?t=506): Publish the Animation Editor keyframes to Roblox with 'Overwrite existing asset' to get an animation ID; later edits only need re-publishing, not a new ID.
- 2024-11-28 Suphi Kaner [6:02](https://youtu.be/SVLFkdeh6c8?t=362): Install the Global Types plugin and tag the module with a boolean attribute named Global types so the plugin can regenerate it.
- 2025-01-15 CallMeDogey [3:14](https://youtu.be/USJC5l_wpuY?t=194): Use a clicker-generator Studio plugin (Simulator Generator) to get a playable base quickly; he built it with no coding.
- 2025-03-09 BloxxedDev [2:11](https://youtu.be/CipKM4DBWxg?t=131): Give the AI context up front (game type, map, core concept) and paste its scripts in; send any error messages back to it for fixes.
- 2025-03-09 BloxxedDev [2:29](https://youtu.be/CipKM4DBWxg?t=149): Expect AI-generated code to need repeated fixes; the creator noted DeepSeek repeated the same mistake even after correction.
- 2025-03-09 BloxxedDev [0:28](https://youtu.be/CipKM4DBWxg?t=28): Expect AI service outages during heavy use; the creator lost roughly 40 minutes to busy-server errors, so keep a backup tool or retry plan.
- 2025-03-26 Suphi Kaner [0:17](https://youtu.be/WoIElUdj64A?t=17): Use Packet (free toolbox model by 5PHI) to replace RemoteEvents/RemoteFunctions and cut network data sent between server and clients.
- 2025-03-29 BloxxedDev [0:00](https://youtu.be/y5aNv16bT3s?t=0): Use a stronger AI model when a cheaper one repeatedly fails; the speaker said Claude 3.7 fixed the carry script that DeepSeek could not.
- 2025-04-10 JustDucksey [1:23](https://youtu.be/BbNlDGBROdg?t=83): Roblox AI texture generation crashed for the creator; have a fallback texture plan rather than relying on AI tools.
- 2025-05-13 Roblox DevForum [page](https://devforum.roblox.com/t/smooth-pathfinding-chase/3648450): Drop the SmoothChase module into ServerScriptService to use it; full docs are in the project's GitHub README.
- 2025-06-09 BubuTheDev [0:08](https://youtu.be/0UYtSJvYe4U?t=8): Install a service autocomplete plugin so typing a service name like 'players' and pressing Tab auto-adds the local variable line.
- 2025-06-09 BubuTheDev [3:28](https://youtu.be/0UYtSJvYe4U?t=208): Use the Reclass plugin to convert an instance to a different class (e.g. Frame to ImageLabel or ImageButton) while keeping its properties.
- 2025-06-26 RoBuilder [39:37](https://youtu.be/krMTcTvaj_8?t=2377): Use Studio folders rather than groups for organising instances.
- 2025-08-20 TheDankDeveloper [2:46](https://youtu.be/OauiTUkK7og?t=166): Use an AI Roblox coding plugin (Lemonade) to script features from a plain-English prompt, e.g. group-and-like gating, instead of writing Luau yourself.
- 2025-08-20 TheDankDeveloper [6:05](https://youtu.be/OauiTUkK7og?t=365): Check AI-generated scripts land in the correct folder/parent; the rainbow background only worked after moving it out of a folder.
- 2025-08-29 Duckable [3:16](https://youtu.be/Em5H7sNWN7I?t=196): Treat AI coding assistants as a tool, not a teacher; review and rewrite generated code yourself rather than trusting it blindly.
- 2025-08-29 Duckable [3:57](https://youtu.be/Em5H7sNWN7I?t=237): Ask AI to strip excessive comments from generated code to keep scripts readable and reviewable.
- 2025-08-29 Duckable [3:16](https://youtu.be/Em5H7sNWN7I?t=196): Be very specific in AI prompts; vague requests produce wrong results. Give exact changes and say 'only change this one line' to avoid extra edits.
- 2025-08-29 Duckable [6:06](https://youtu.be/Em5H7sNWN7I?t=366): AI can be useful for generating balanced prices for tycoon buttons, which is otherwise time-consuming.
- 2025-09-05 Roblox [36:50](https://youtu.be/6iB5__RCQDc?t=2210): Use Studio's AI assistant for tedious work: scatter thousands of trees, generate meshes from prompts, convert Blender avatars, and code completion.
- 2025-09-07 janisjanis01 [3:30](https://youtu.be/YVKHlrlWn-k?t=210): AI-generated icons and tool art can cover placeholder assets quickly, though quality varies; hire animators for custom animation.
- 2025-09-23 TheDankDeveloper [0:18](https://youtu.be/pRfzkw-wHgA?t=18): Use ChatGPT to generate a simple game concept, then ask it to write a detailed prompt for an AI Roblox scripting tool like Lemonade.
- 2025-09-23 TheDankDeveloper [2:44](https://youtu.be/pRfzkw-wHgA?t=164): Expect AI-generated scripts to error; iterate by pasting errors back and asking the AI to fix them (e.g., forgotten anchoring).
- 2025-09-23 TheDankDeveloper [3:25](https://youtu.be/pRfzkw-wHgA?t=205): Add small features (e.g., a billboard GUI showing player coin count) by prompting the AI rather than scripting manually.
- 2025-09-26 Roblox [5:03](https://youtu.be/2HotST5mF3A?t=303): AI-generated output likely can't be copyrighted; modifications and arrangements by a human author can be.
- 2025-09-26 Roblox [31:36](https://youtu.be/3h25HUtBHFk?t=1896): Put an LLM check in front of generated objects to reject off-theme items (e.g., 'is this a spooky swampy object?') to keep the game aesthetic.
- 2025-09-26 Roblox [8:11](https://youtu.be/3h25HUtBHFk?t=491): Ask the NPC's LLM to reply in JSON with a fixed action set (small talk, claim quest) so your script can parse and map responses to game actions.
- 2025-11-18 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522): Use ReflectionService to build API inspection plugins that analyze new engine API releases, or Studio plugins that change instance classes faster.
- 2025-11-22 Crusherfire [0:00](https://youtu.be/6kcWSMJFaS4?t=0): Use an MCP server to let Claude Code or Codex read your open Studio project directly, avoiding a move to VS Code and Rojo.
- 2025-11-22 Crusherfire [6:16](https://youtu.be/6kcWSMJFaS4?t=376): Build the MCP server with npm install, npm run build, then npm start; it listens on localhost port 3002 for the Studio plugin.
- 2025-11-22 Crusherfire [8:39](https://youtu.be/6kcWSMJFaS4?t=519): Register the MCP server with 'claude mcp add' (stdio transport) and verify with '/mcp' inside Claude Code; Claude scopes it to that folder.
- 2025-11-22 Crusherfire [10:12](https://youtu.be/6kcWSMJFaS4?t=612): Install the MCP plugin .rbxm into Studio's Plugins folder, restart Studio, then click Connect in the MCP plugin widget.
- 2025-11-22 Crusherfire [12:17](https://youtu.be/6kcWSMJFaS4?t=737): Only one agent can use the MCP server at a time, so switch between Claude and Codex when you hit usage limits.
- 2025-11-28 VuukStudios [12:25](https://youtu.be/U4nduRcszJ4?t=745): Use AI as a guide for roadmaps and goals, not to write full scripts; ask it to explain code you don't understand.
- 2025-12-02 TheDankDeveloper [1:10](https://youtu.be/D6Ej1CgiWOc?t=70): Use Lemonade (AI Roblox Studio plugin) to script features by typing prompts; ChatGPT can generate the prompts to paste in.
- 2025-12-13 janisjanis01 [10:16](https://youtu.be/JYvGdKRzwEo?t=616): Use AI assistants for boilerplate like UI vectors, but expect to modify output; balancing advice from AI was used for tuning.
- 2025-12-22 #7Phantom [0:00](https://youtu.be/peTkfSG79rM?t=0): Learn clothing design by watching the channels he recommends, then grind by making every type of clothing piece.
- 2026-01-09 TheDankDeveloper [4:38](https://youtu.be/BYhhm9o3H_E?t=278): Connect Lemonade to Roblox Studio and prompt one mechanic at a time; it built a working cast-and-reel mechanic from one prompt.
- 2026-01-09 TheDankDeveloper [0:00](https://youtu.be/BYhhm9o3H_E?t=0): Expect to fix AI-generated errors and build the UI yourself; ChatGPT's output needed manual debugging and UI work.
- 2026-01-27 TheDankDeveloper [0:00](https://youtu.be/3y7EU49_d7s?t=0): Give AI tools one step at a time: ask for a core mechanic first, test in Studio, then add the next feature. Lemonade worked better in small increments.
- 2026-01-27 TheDankDeveloper [6:18](https://youtu.be/3y7EU49_d7s?t=378): Playtest after every AI prompt; AI-generated scripts often introduce errors that break earlier features (Claude's build broke after adding combat).
- 2026-01-27 TheDankDeveloper [5:21](https://youtu.be/3y7EU49_d7s?t=321): Add a health system before testing combat; without visible health values you cannot tell whether hit detection works.
- 2026-02-18 Roblox DevForum [page](https://devforum.roblox.com/t/studio-beta-avatarabilities-library-for-a-luau-based-character-controller/4403904): Force-load autocomplete by running require("@rbx/AvatarAbilities") in the command bar after each Studio reload while the beta is active.
- 2026-03-09 GamesBeat [page](https://gamesbeat.com/roblox-unveils-jumpstart-and-incubator-programs-to-help-creators-expand-possibilities-exclusive/): Studio's built-in MCP client (Assistant) and MCP server let external clients such as Claude Code, Cursor and Codex run creation flows.
- 2026-04-02 Roblox DevForum [page](https://devforum.roblox.com/t/studio-beta-introducing-the-animation-graph-system/4554788): Enable via File > Beta Features > Animation Graph in Studio; open the Clip Editor (Animation Graph Editor) from the Avatar tab on a rig with an Animator.
- 2026-04-11 TheDankDeveloper [0:43](https://youtu.be/i5sldtdF8m0?t=43): Use Forge UI icon mode with a short prompt (e.g. 'X close button, cartoony style') to generate UI assets, then refine with follow-up edit prompts.
- 2026-04-11 TheDankDeveloper [4:03](https://youtu.be/i5sldtdF8m0?t=243): Use Forge UI's Magic Edit by uploading a screenshot of an existing frame and prompting for a restyle; generate variants to pick the best match.
- 2026-04-16 Roblox [12:26](https://youtu.be/8IcYpOl4Sdk?t=746): Use Studio Assistant planning mode: state intent with text, images or sketches, answer clarifying questions, then confirm, edit or reject the generated to-do list before agents run.
- 2026-04-16 Roblox [28:23](https://youtu.be/8IcYpOl4Sdk?t=1703): Treat each completed to-do as a checkpoint you can revert to, so you don't restart from scratch when an AI step goes wrong.
- 2026-04-19 TheDankDeveloper [0:00](https://youtu.be/Ufr0SVq-o98?t=0): Give AI assistants one clear feature per prompt (plots, then economy UI, then shop) and playtest after each step to catch breakage early.
- 2026-04-23 Roblox DevForum [page](https://devforum.roblox.com/t/studio-beta-introducing-procedural-models-build-parametrized-3d-models-with-code-or-ai/4592056): Use /generate_procedural_model with a text prompt or reference image in Assistant or Studio MCP; reference images improve accuracy.
- 2026-04-25 CallMeDogey [4:06](https://youtu.be/SjjPGduApZU?t=246): With RoVis, give a reference image plus a prompt; the creator says it works best with references, and icon prompts work fine without one.
- 2026-04-25 CallMeDogey [5:29](https://youtu.be/SjjPGduApZU?t=329): Fix missing text or details in Photopea after generating with AI, since AI tools may not add text well.
- 2026-04-30 Roblox DevForum [page](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091): Use the Age Check API: Player:PromptAgeCheck() on a deliberate player action, not on spawn; check Player.AgeChecked.
- 2026-04-30 MoseyTube [2:04](https://youtu.be/sFr7htxsnR4?t=124): Connect Claude to Roblox Studio via an MCP server so it can read the game and write scripts from chat; he claims ~80% scripting time saved.
- 2026-05-19 MoseyTube [2:44](https://youtu.be/400F-3qXoHE?t=164): Write long, detailed prompts rather than one-liners like 'make a game'; specificity directly improves the output quality.
- 2026-05-19 MoseyTube [2:44](https://youtu.be/400F-3qXoHE?t=164): Describe concrete mechanics with numbers, e.g. 'enemy follows the player and deals 10 damage on contact'.
- 2026-05-25 TheDankDeveloper [0:00](https://youtu.be/uYuiCJrAcmI?t=0): Use prebuilt prompt cards from Lemonade's inventory as starting points, then tweak the prompt; the creator dropped a survival card in and got health/hunger bars immediately.
- 2026-05-25 TheDankDeveloper [1:21](https://youtu.be/uYuiCJrAcmI?t=81): When AI-generated code errors (e.g. infinite yield blocking UI), paste the error back into the AI and ask it to fix; this worked on the first try.
- 2026-05-25 TheDankDeveloper [4:51](https://youtu.be/uYuiCJrAcmI?t=291): Write a specific prompt for enemies (e.g. pathfinding zombie that chases and deals damage); the AI implemented it in one pass.
- 2026-05-26 Tizzy [8:55](https://youtu.be/7tYPvXYlif8?t=535): Build a working prototype with AI (e.g. Claude) and free models before hiring a developer to validate the idea quickly.
- 2026-05-26 Tizzy [15:45](https://youtu.be/7tYPvXYlif8?t=945): Duplicate the game backup and tweak feel with AI to reduce back-and-forth with the programmer, then batch changes into one request.
- 2026-06-06 janisjanis01 [3:16](https://youtu.be/CltiB53QTHw?t=196): Use Meshie.ai to generate 3D meshes quickly, then clean up in Blender.
- 2026-06-19 LovJak [3:00](https://youtu.be/ImcICq5XfL8?t=180): Use an AI coding assistant (Rebirth AI cited) for discrete systems like plot assignment; speaker says it took under 30 minutes.
- 2026-07-19 MoseyTube [0:49](https://youtu.be/PstV93OnOdM?t=49): In Studio, open Assistant settings, go to Manage MCP servers, enable Studio as an MCP server, and confirm the green indicator shows a client connected.
- 2026-07-19 MoseyTube [1:29](https://youtu.be/PstV93OnOdM?t=89): Connect via MCP quick connect by selecting Codex CLI, after installing the Codex desktop app and signing in with a ChatGPT account.
- 2026-07-19 MoseyTube [1:50](https://youtu.be/PstV93OnOdM?t=110): Use medium effort for simple checks like connection tests, and switch to ultra effort for large master-prompt builds; the speaker says quality difference is noticeable.
- 2026-07-19 MoseyTube [2:26](https://youtu.be/PstV93OnOdM?t=146): Give the model one long master prompt covering map, progression, customers, monetisation and data saving to generate a full game foundation in one pass.
- 2026-07-27 rasdev [4:05](https://youtu.be/_Tt-l7EMEHE?t=245): Generate icons and thumbnails with ChatGPT for the cheapest, fastest route; specify 512x512 for icons and 1920x1080 for thumbnails.
- 2026-07-27 rasdev [4:45](https://youtu.be/_Tt-l7EMEHE?t=285): Expect AI limits: it handles text poorly, so add text in an editor rather than relying on the model.
- 2026-07-27 waveshine [7:10](https://youtu.be/hQ1lrFLEF1c?t=430): Use AI as a tutor (explain this error/line), not to generate whole systems you don't understand; read the documentation with code snippets.
- 2026-07-29 VuukStudios [10:06](https://youtu.be/Bltv__PoNcA?t=606): Use AI for coding only if you already understand scripting; without that knowledge it produces inaccurate code. Avoid it for paid client work.
- 2026-07-30 Platform Aeronaut (transcript) [page](https://transcripts.platformaeronaut.com/transcripts/RBLX-2Q26-transcript): Build lets creators start an experience from a conversational AI interface and finish it in Roblox Studio. Roblox is currently live only in New Zealand.
- 2026-07-30 Roblox Investor Relations [page](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm): Creator survey: 95% of AI-using creators say AI speeds launch or update timelines; nearly half saw over 50% faster publishing.
- 2026-07-30 Roblox Investor Relations [page](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm): Upcoming Roblox agents: Playtesting Agent (automated QA), Analytics Agent (natural-language performance queries), Experiment Agent (recommends A/B tests for engagement, retention, monetization).
- 2026-08-04 Duckable [21:21](https://youtu.be/Cc7HT3uNjeQ?t=1281): Creator's view: AI is useful as a tool for saving time but overuse removes the struggle that builds skill; use it deliberately.
- 2026-08-07 MoseyTube [1:23](https://youtu.be/5zz5ao0zV_Y?t=83): Pay for a higher AI usage tier (Claude Max 5x, $100/mo) if usage limits stall your build sessions; waiting on resets defeats using AI to build faster.
- 2026-08-21 Business of Creators [21:06](https://youtu.be/lpIzMycpiKo?t=1266): Use AI for spitballing design docs and quick grey-box vertical slices to test if the core idea is fun within about two days; keep art and UI human-made.
- 2026-08-24 Roblox DevForum [page](https://devforum.roblox.com/t/x/4828676): If using an MCP-enabled AI agent, use the Open Cloud API reference skill so it can discover and work with these APIs.
- 2026-08-26 Matt The Method [2:19](https://youtu.be/1mYF-cWJPmQ?t=139): Periodically paste current scripts, folder structure and Explorer layout into the AI and say 'continue from here' to avoid stale, mismatched code suggestions.
- 2026-08-26 VuukStudios [12:18](https://youtu.be/m7015JSIrpw?t=738): Use AI to speed up your own game development; avoid using it for paid client commissions where originality matters.
- 2026-08-26 kra_DeZ [10:08](https://youtu.be/oMI-GhUcfFE?t=608): Use AI (he cites Claude) to build most of the game; he says it cut build time to about two days.
- 2026-08-29 RoyalDev [0:00](https://youtu.be/erhgduyGzdM?t=0): New devs should learn how code works before pasting AI output; otherwise they have zero debugging ability and can't fix bugs.
- 2026-08-29 RoyalDev [4:46](https://youtu.be/erhgduyGzdM?t=286): Use AI to automate boilerplate you already understand, such as leaderstats, DataStore skeletons, UI functionality, and tweens.
- 2026-08-29 RoyalDev [5:28](https://youtu.be/erhgduyGzdM?t=328): Paste error output into an AI assistant for faster debugging, and ask it to point out the problem so you fix it yourself.
- 2026-08-29 RoyalDev [6:08](https://youtu.be/erhgduyGzdM?t=368): Ask AI for a quick rundown of an unfamiliar service (e.g. TeleportService) to learn its core usage faster than reading docs.
- 2026-08-29 RoyalDev [7:30](https://youtu.be/erhgduyGzdM?t=450): Use AI for advanced math such as CFrame angles and sine/cosine, especially for VFX and particles.
- 2026-09-00 Roblox DevForum [page](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208): Unified agentic permission (Late 2026) will control what Assistant, MCP, Plugins and OCALE can access and do.
- 2026-09-00 PocketGamer.biz [page](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/): Build (prompt-based creation) has published about 9,000 games; 71% of its creators had never used Roblox Studio, so it lowers the entry barrier.
- 2026-09-06 kra_DeZ [6:59](https://youtu.be/cJ-YzHHhQs8?t=419): Use AI to speed up development and thumbnails, but understand the code yourself; he says a months-long build can take days with AI.
- 2026-09-10 GamesBeat [page](https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/): Build lets anyone make a game from prompts in the Roblox app. Creators can review analytics and add monetization there. Scene Generator will create layouts from a prompt and reference image, to refine in Studio.
- 2026-09-11 MonarchDev [4:47](https://youtu.be/LD7LGP10dRc?t=287): Using AI coding tools to speed up building shops and save systems is a practical advantage for solo developers.
- 2026-09-11 Roblox DevForum [page](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880): Use Studio's NPC Dynamic Behavior (late 2026) to populate NPCs via prompts; edit, version, and reuse the behavior across NPCs.
- 2026-09-11 Roblox Newsroom [page](https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play): Build (mobile prompt-based game creation) can be used to test ideas quickly; it can analyze and add monetization, with in-app ad launches planned.
- 2026-09-12 Duckable [18:20](https://youtu.be/MBRNAqkDEFA?t=1100): Ask AI for pointers and directions instead of full code ("follow the breadcrumbs") so you still write the logic yourself.
- 2026-09-12 Duckable [19:02](https://youtu.be/MBRNAqkDEFA?t=1142): Read every AI-generated chunk until you understand it; don't paste blindly.
- 2026-09-12 Duckable [19:02](https://youtu.be/MBRNAqkDEFA?t=1142): Type AI-suggested code out by hand instead of pasting it; it keeps you learning how the system works.
- 2026-09-12 Duckable [19:44](https://youtu.be/MBRNAqkDEFA?t=1184): Use AI sparingly. Vibe-coding without thinking erodes critical thinking and makes you dependent on the tool.
- 2026-09-12 Duckable [16:58](https://youtu.be/MBRNAqkDEFA?t=1018): Roblox lets you connect Claude or ChatGPT to Studio; this is an alternative to paid standalone Roblox AI generators.
- 2026-09-17 Roblox [54:49](https://youtu.be/3a2RbLOAl4A?t=3289): Use NPC dynamic behavior: describe a character and their goals in a prompt instead of writing dialogue trees or behaviour trees.
- 2026-09-17 Roblox [1:05:12](https://youtu.be/3a2RbLOAl4A?t=3912): Procedural models generated by scripts expose properties so resizing adds instances, useful for fences and tire stacks.
- 2026-09-17 Roblox [29:19](https://youtu.be/53dj7AG3foA?t=1759): Studio 3D generation and texture generation tools can create meshes and PBR textures from prompts; segmented meshes make adding behavior easier.
- 2026-09-17 Roblox [42:31](https://youtu.be/53dj7AG3foA?t=2551): Prompt to Avatar (by end of year) produces compliant R15+ rigs, layered clothing and modesty layers from a concept prompt; keep artistic control.
- 2026-09-18 Roblox DevForum [page](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208): Note that a unified agentic permission will control what Assistant, MCP, Plugins and OCALE can access (Late 2026).
- 2026-09-20 Possible Panda [9:12](https://youtu.be/KVmPyoOPmRI?t=552): Use a Studio plugin like Scribe Studio to inspect live player data in the server tab; it may be finicky, so have a fallback.
- 2026-09-25 Possible Panda [0:00](https://youtu.be/B6VDcOTKKRY?t=0): placeholder
- 2026-09-26 SimTek Game Development [0:40](https://youtu.be/-0H6JRtrA2Y?t=40): Use Roblox AI Assistant in Agent mode; it can edit scripts and the place. Be specific: name keys, speeds, and release behaviour in the prompt.
- 2026-09-26 SimTek Game Development [2:01](https://youtu.be/-0H6JRtrA2Y?t=121): Use 'review each script change' to read diffs before accepting, or accept all and check the diff afterwards.
- 2026-09-26 SimTek Game Development [8:08](https://youtu.be/-0H6JRtrA2Y?t=488): For builds, give concrete parts (walls, floor, roof, doorway, window) and scale; AI output is rough and needs manual polish.
- 2026-09-30 Roblox Investor Relations [page](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm): 97% of regularly-AI-using creators said AI accelerated development timelines; over 80% of top 100 games used AI tools for creation.
- 2026-09-30 Roblox Investor Relations [page](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm): Connect external AI via the Studio MCP server; daily MCP users grew nearly 5x since Q2 among top creators.
- 2026-09-30 Roblox Investor Relations [page](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026068235/ex991-q32026earningsshar.htm): Build lets creators make, publish, review analytics and add monetization from mobile; free base tier with paid prompt-capacity tiers.
- 2026-09-30 RoyalDev [2:44](https://youtu.be/rxeLNsNUVTQ?t=164): Generate thumbnails with AI by iterating prompts and supplying reference images rather than one-shot prompting; the speaker spent about 20 minutes on one.
- 2026-10-01 RoyalDev [0:01](https://youtu.be/xaWGP-slzdM?t=1): Use a reference thumbnail from a successful game plus a screenshot of your own model; ask the AI to match the reference style and swap in your character.
- 2026-10-01 RoyalDev [2:03](https://youtu.be/xaWGP-slzdM?t=123): Prompt iteratively: confirm what the AI understood, ask it for gaps, then make targeted edits like moving text, rather than one-shot prompting.
- 2026-10-10 mats-dept2 [0:30](https://youtu.be/Y5QtYzd95v8?t=30): Use AI to agree on and stress-test the core loop and design direction before building.
- 2026-10-11 VuukStudios [10:49](https://youtu.be/0ENzqNB_EUo?t=649): Use AI to speed up development but build core content like map, UI and scripting yourself; players can often spot AI UI and leave.
- 2026-10-11 VuukStudios [12:51](https://youtu.be/0ENzqNB_EUo?t=771): Connect Claude or GPT to Studio via MCP to scan your code and infrastructure for improvements, rather than asking AI to build the whole game.
- 2026-10-12 Roblox [19:47](https://youtu.be/3gnK649VNbY?t=1187): Use the Scene Analysis agent skills: scene health, rendering optimization, memory optimization, and fix leaks, available via MCP or any agent.
- 2026-10-12 Roblox [16:08](https://youtu.be/KB5iAzy86Fo?t=968): Write down which AI model is best for each task (images, meshes, objects) as a playbook, then give the agent API keys so it runs the pipeline unattended.
- 2026-10-12 Roblox [16:48](https://youtu.be/KB5iAzy86Fo?t=1008): Capture a multi-step asset workflow as a reusable skill file (isolate objects, mesh them, upload via Open Cloud) so any scene can be processed unattended.
- 2026-10-12 Roblox [19:50](https://youtu.be/KB5iAzy86Fo?t=1190): Give the AI a bridge into the running game (execute Luau, capture viewport, read console) so it can verify runtime behaviour instead of you being the eyes.
- 2026-10-12 Xaiyne [0:41](https://youtu.be/KhKOSmdX8sc?t=41): Use a current image-to-3D model (speaker used Tripo AI) for UGC base meshes; older AI models looked too poor to sell. Refine in Blender if time allows.
- 2026-10-12 Xaiyne [2:48](https://youtu.be/KhKOSmdX8sc?t=168): Choose the cheaper HD model setting over Smart Mesh; Smart Mesh gives better results but costs substantially more credits.
- 2026-10-12 Roblox [2:36](https://youtu.be/QhZpK2hdnjE?t=156): Start from a concept image and iterate prompts to pick a layout before generating 3D; scene generation matches the image's top-down layout.
- 2026-10-12 Roblox [7:37](https://youtu.be/QhZpK2hdnjE?t=457): Define part segmentation in the generation prompt (e.g. body, motor, seat) so generated meshes can have scripts attached to individual parts.
- 2026-10-12 Roblox [10:20](https://youtu.be/QhZpK2hdnjE?t=620): Use the 4D behavior library (from the DevForum post, with a reference experience) by tagging a mesh with the 4D capability tag and attributes to make it drivable or shootable.
- 2026-10-12 Roblox [42:39](https://youtu.be/QhZpK2hdnjE?t=2559): For consistent style, give the assistant several reference images at once; mesh generation follows images closely, procedural models only approximate them via primitives.
- 2026-10-12 Roblox [2:48](https://youtu.be/QvNAMmGqdd4?t=168): Generated NPC behavior is editable: behavior trees run on a runner you can inspect and modify in the planned visualizer and editor, not a black box.
- 2026-10-12 Roblox [19:19](https://youtu.be/QvNAMmGqdd4?t=1159): Human-like agents learn via imitation learning on gameplay data plus reinforcement learning; they see only what a real player sees and input via keyboard/mouse.
- 2026-10-12 MonarchDev [1:23](https://youtu.be/QwdZRB6xRKk?t=83): Use a fixed prompt and time budget when benchmarking AI tools so results are comparable across games.
- 2026-10-12 MonarchDev [0:56](https://youtu.be/QwdZRB6xRKk?t=56): Connect AI to Roblox via MCP: create an API key in Creator Hub, connect the AI client, then connect Roblox Studio.
- 2026-10-12 MonarchDev [10:08](https://youtu.be/QwdZRB6xRKk?t=608): Treat AI-generated games as a strong first draft; expect to fix layout, balance, and gameplay feel yourself.
- 2026-10-12 MonarchDev [10:50](https://youtu.be/QwdZRB6xRKk?t=650): Generated UI, sound effects and meshes are the main time savers; AI-only output without fidelity checks tends to look noticeably worse.
- 2026-10-12 Roblox [17:41](https://youtu.be/gCp4zzjjJ14?t=1061): The speaker's generated-UGC system draws only from their own catalog of UGC items to keep quality high, and players said they did not want AI use.
- 2026-10-13 TheDankDeveloper [0:40](https://youtu.be/4ojmHWn_rxY?t=40): Connect Claude Code to Roblox Studio via MCP before building; search for setup tutorials if needed.
- 2026-10-15 LovJak [4:11](https://youtu.be/YXcV0Ba0RJc?t=251): Ask the AI for a full script and paste it into the correct service; verify the server/client location of each piece before testing.
- 2026-10-15 LovJak [5:36](https://youtu.be/YXcV0Ba0RJc?t=336): When AI gives partial code diffs, ask for the full replacement script to avoid pasting errors.
- 2026-10-15 LovJak [3:28](https://youtu.be/YXcV0Ba0RJc?t=208): Write detailed, specific prompts for AI coding tools; the creator used a generated long prompt for a complex system and it worked on first run.
- 2026-10-16 MonarchDev [1:18](https://youtu.be/hPWJlFwp5Xs?t=78): Connect Claude to Roblox Studio via the Studio MCP server setting, then ask Claude which place it sees to verify the connection.
- 2026-10-16 MonarchDev [1:58](https://youtu.be/hPWJlFwp5Xs?t=118): Use high effort for building whole games and lower effort for small fixes; it is quicker and cheaper.
- 2026-10-16 MonarchDev [4:31](https://youtu.be/hPWJlFwp5Xs?t=271): When output is wrong, describe the feeling and the reference-game structure in detail; more detailed prompts yield better results.
- 2026-10-16 MonarchDev [8:22](https://youtu.be/hPWJlFwp5Xs?t=502): Ask the AI to explain how each script or function works as you go to learn Luau while building.
- 2026-10-16 Roblox DevForum [page](https://devforum.roblox.com/t/weekly-recap-october-12-18-2026/4938638): Try Quality mode texture generation (beta) via Model > Texture or /generate_texture in Assistant to get 4K PBR textures with color, roughness, and metalness maps.
- 2026-10-17 GuideRealm [2:24](https://youtu.be/ltbZzXRrDF8?t=144): Write a detailed master prompt covering map, systems, persistence, offline earnings, and mobile controls; the more detail, the better the AI build.
- 2026-10-17 GuideRealm [2:24](https://youtu.be/ltbZzXRrDF8?t=144): Back up the place before letting the AI edit an existing project, since it modifies the game directly.
- 2026-10-17 GuideRealm [3:45](https://youtu.be/ltbZzXRrDF8?t=225): Use a higher effort level (extra high) for complex whole-game generation; keep medium for simple queries.
- 2026-10-17 GuideRealm [1:11](https://youtu.be/ltbZzXRrDF8?t=71): Enable Studio as MCP server and ChatGPT Codex under Quick Connect in the Assistant settings; verify by asking it to identify the open project.
- 2026-10-21 TheDankDeveloper [0:41](https://youtu.be/Mftq7v8nAcs?t=41): Prompt one mechanic at a time with reference screenshots rather than one massive prompt; the creator says this is how the build succeeded.
- 2026-10-21 TheDankDeveloper [1:22](https://youtu.be/Mftq7v8nAcs?t=82): Send a full-screen game screenshot, not a cropped reference, so the AI sizes buttons and HUD correctly; cropped references produced oversized, misplaced buttons.
- 2026-10-21 TheDankDeveloper [4:50](https://youtu.be/Mftq7v8nAcs?t=290): Watch AI plan usage: the creator hit 73% then 100% of session limit on the Pro plan during one build session.
- 2026-10-21 Xaiyne [2:47](https://youtu.be/wkfCP_09CI8?t=167): In Tripo AI, set texture 2K, PBR off (cheaper upload), triangle count under Roblox's 4,000 max (he used 3,990).
- 2026-10-21 studio rook. [1:50](https://youtu.be/z04_RTBiMgg?t=110): Hard-surface pieces like guns suit CAD tools such as Plasticity; it is a one-time purchase rather than a subscription.
- 2026-10-23 tef [1:35](https://youtu.be/OfObWnrucRY?t=95): Give the AI reference images with prompts so it has visuals to match; the speaker said this made the output far closer to the intended look.
- 2026-10-24 Crusherfire [3:52](https://youtu.be/4n7thZAAF-E?t=232): Write your architecture and code-style rules as reusable AI skills, then have AI refactor old code to match; speaker says this cut a few weeks of work to a day or two.
- 2026-10-25 janisjanis01 [4:05](https://youtu.be/A2QD-eT3IG0?t=245): Using AI-generated vectors/icons (ChatGPT) and AI config work worked for UI assets but AI-configured upgrades were a time sink; the speaker advises against letting AI configure game balance.
- 2026-10-26 MonarchDev [0:00](https://youtu.be/WA4RzzT39Dw?t=0): Don't expect AI to generate a complete game from one prompt. Build iteratively in stages, with frequent detailed instructions.
- 2026-10-26 MonarchDev [2:26](https://youtu.be/WA4RzzT39Dw?t=146): Avoid vague prompts like 'make this better'. Name the specific problem and the target look, e.g. 'too low-saturation, make it cartoonish and highly saturated'.
- 2026-10-26 MonarchDev [4:48](https://youtu.be/WA4RzzT39Dw?t=288): Long AI sessions degrade (around 900k of a 1M context in his example). Compress or start fresh sessions rather than expecting one long prompt to succeed.
- 2026-10-26 MonarchDev [5:20](https://youtu.be/WA4RzzT39Dw?t=320): Basic coding knowledge helps you judge and fix AI output; users without it can still succeed, just more slowly.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant): Open Assistant inside Studio rather than the web version so it can reference your game's objects and scripts.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant): Rename parts (e.g. GlitterPart) before prompting so Assistant knows which part to script.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant): Include specific details in prompts (color, trigger, timing); fewer details produce more unpredictable results.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant): Word choice matters: small rephrasings can yield a new script, code in an existing script, or just a ParticleEmitter.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant): If results are wrong, rephrase the request and try again rather than editing blindly.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant): Undo unwanted changes with Ctrl+Z for non-script changes, or delete the generated script in Explorer.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building/code-with-assistant): Learn basic Luau before accepting code, so you can review Assistant's samples for your use case.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/error-reporting): Use an API key with only the needed Access Permissions scopes; the key owner must also have analytics access or requests return 403.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/overview): Use Assistant in Studio to write scripts, insert and modify objects, and automate repetitive tasks so you can focus on creation.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/overview): Ask the documentation Assistant to clarify concepts, provide sample code for a specific use case, or compare approaches to a problem.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/building): Use AI Assistant to generate code that modifies part behavior, rather than writing scripts from scratch as a beginner.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud): Use API keys or OAuth 2.0 for Open Cloud calls; they have strong stability guarantees and regular updates. API keys are the easiest way to start.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud): Test Open Cloud endpoints with Postman using the OpenAPI descriptions, or with the OAuth 2.0 sample app, before writing integration code.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-messaging): Use Open Cloud to send live messages from external tools instead of writing manual Studio scripts.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/mcp): Only connect MCP clients you trust: they can read and modify content in your open Roblox places.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/mcp): Verify the connection by checking for the green connected-client indicator under Manage MCP Servers after setup.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/mcp): Make sure the latest Roblox Studio version is installed before connecting an MCP client.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/animation/capture): Use capture tools to generate animations in minutes, then refine keyframes manually rather than animating from scratch.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/art/characters/facial-animation/moods): Use the Face Animation Editor (Avatar tab > Clip Editor > Face) to create mood animations; undo/redo with Ctrl+Z/Ctrl+Y, right-click slider > Reset Selected.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/avatar/avatar-generation): Let players repeat the 2D preview step until satisfied; the workflow supports regeneration before the costly 3D generation.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-a-project): Studio's built-in Assistant can handle routine tasks like creating instances, setting properties and generating scripts, freeing time for creative work.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/avatar/resources): Run the Blender Validation Tool before importing avatar items into Studio; use Blender Calisthenics Tool to check skinning data.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/npc-kit): Customize NPC animations by swapping AnimationId values in the Animate script poses or Animations folder; for finer changes, copy existing animations and edit Animate or NPC scripts.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/npc-kit): Adding rigs with WeldConstraints to UpperTorso lets you attach extra geometry without modifying the original Rthro base rig.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets): Assistant is effective for repetitive, deterministic setup such as placing many assets at exact CFrame values, though manual placement is also offered.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/build-with-assistant): Switch Assistant to Plan mode and review the step-by-step plan before building; start with world and core gameplay, add scripts and secondary systems later.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/build-with-assistant): If Assistant hits max output length, click Continue so it resumes building where it left off.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/build-with-assistant): Mix workflows: generate or modify content with Assistant, then fine-tune positioning, materials, lighting and UI with Studio's built-in tools.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/guide): Select a Part before prompting /generate_mesh so Assistant uses its size and location as a bounding box, keeping the generated mesh within that space.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/guide): Set a maximum triangle count for generated meshes when needed; lower values give lower-poly results. Default is 10,000.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/guide): Use /generate_mesh with a reference image instead of text when you need a specific look; it accepts one input type per request, not both.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/guide): Run /plan or choose Plan mode for complex requests and review the Markdown plan before clicking Build; plans never auto-execute.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/guide): Use separate chats per task and the branch icon to fork a response into a new chat, keeping the original context intact. Each chat has its own context window.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/guide): Use Creator Store search filters (price, audio duration, verified creators) and asset type filters when inserting assets via Assistant.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/texture-generator): Write detailed prompts naming material, color, pattern and distinctive features; simple prompts like 'make it out of wood' give inconsistent results.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/texture-generator): Refine the prompt rather than regenerating previews with the same prompt, which yields only slightly different results.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/texture-generator): Set Preview orientation to Manual and orbit the mesh to choose the view, if Automatic picks a poor angle.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/texture-generator): Avoid prompts that change mesh geometry, reference the current texture, other scene objects, or previous textures, or describe reflectivity/transparency.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/texture-generator): With image prompts, expect a style guide rather than an exact template; details may not be preserved.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/get-started/tools): Use the AI Assistant in Studio for code snippets, answers, asset insertion, and bulk property modifications to save time on chores.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/prompt-engineering): Be specific: use exact instance names, name the function/service to use (e.g. TweenService), and state the instance type such as part or model.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/prompt-engineering): If Assistant fails, add more detail and retry; outputs are non-deterministic, so small prompt tweaks can change results.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/prompt-engineering): Use selection in Studio to reference objects in prompts, e.g. to modify multiple objects, duplicate them, or continue a placement pattern.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/prompt-engineering): Separate code from questions with ### delimiters in multi-step prompts to get better step-by-step explanations.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/prompt-engineering): Procedural model generation is slower than text replies; you can type the next prompt while it generates.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio): Use Assistant to add objects in bulk, modify scripts in place, and optimize code, instead of doing these manually.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques): Use Roblox Configs and Experiments to tune onboarding values live rather than hardcoding them.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/animator/next-steps): Use Studio's Curve Editor to view and modify rig position/orientation changes between keyframes via color-coded curve graphs, for smoother animations.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/resources/battle-royale/run-the-game): Close any open Studio places before running, then open the target place page from the Recent list and click the play button to test the game.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/avatar/dynamic-heads/validate): Use Avatar Setup to auto-generate head cage and FACS facial animation; then edit the output, or download as .gltf to adjust FACS/cage in a modeling tool.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/overview): Duplicate a default tab before editing it; default tabs can't be modified directly, but duplicated tabs can be freely changed.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/overview): Use the Command Bar (Ctrl+9 / ⌘+9) to run Luau outside scripts; enable Multi-line Command Bar in File > Beta Features.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/instance): Use Google Sheets + Apps Script with Open Cloud to tune game values (e.g., item prices, colours) without republishing in Studio.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/workspace/streaming/techniques): Back up the game first (File > Publish to Roblox As) before running the rbx-convert-to-streaming AI skill; a typical conversion takes 20-30 minutes and about 200,000 tokens.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/mcp): Use Roblox's open-source Studio MCP server to let external AI coding tools read, write, test and modify your game code and data directly.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/mcp): To use an external LLM in Studio Assistant: get an API key from the provider, open Assistant, click ⋯ > Manage API Keys, select provider, enter key, then pick model in Model drop-down.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/activity-history): Use the ⋯ menu on an event to jump straight to the related setting in Studio or Creator Hub.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/coding-harness): Use Script Sync (File → Beta Features) to write Luau in your own editor; files in synced folders appear in Studio automatically.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/coding-harness): Connect Script Sync by selecting the top-level project folder, not its subfolders, so services match folders by name.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/coding-harness): Use the Studio MCP server to let the agent read the game tree, create objects, run scripts and check output; it covers StarterGui and StarterPack, which Script Sync cannot reach.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/reference/risk-levels): Review an endpoint's functionality and potential impact before testing, especially medium and high risk endpoints that can modify your data.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview): Use the OAuth 2.0 grant to let third-party tools access your games without sharing your password or personal credentials; you choose the permitted resources.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview): When adding permission scopes in Creator Dashboard, select the openid identity scope so the token response includes an ID token.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview): Register your app with Roblox to obtain a client ID and secret before implementing the authorization code flow.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/auth/oauth2-overview): Go through Roblox's review process after implementation to get more user quota for your app.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-place-publishing): Automate publishing by calling the Place Publishing API from CI (e.g. a GitHub Action) after integration tests pass, instead of publishing manually from Studio.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-assets): Use the Assets API to upload/update assets with one HTTP request instead of manual Studio imports; beta endpoints may change.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-assets): Poll the Get Operation endpoint with the returned operation ID to check upload status, or read the status field to see why an upload failed.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/usage-assets): Use asset:read and asset:write scopes when registering an OAuth 2.0 app that uploads assets for users (beta).
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/animation/graph-editor): Use Graph > Create Animate script to generate the Animate, RunClient and RunServer scaffolding instead of writing it by hand.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/assets/toolbox): If the Toolbox fails to load, close all Studio instances, then delete the WebView2 data folder at %LOCALAPPDATA%\Roblox\RobloxStudio\WebView2 on Windows; Studio recreates it on launch.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/projects/assets/toolbox): On Mac, delete ~/Library/WebKit/com.Roblox.RobloxStudio and ~/Library/Caches/com.Roblox.RobloxStudio/WebKit to reset the Toolbox web view.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/avatar/makeup/specifications): Start from the provided Roblox makeup template head; it already has correct objects and naming. Do not rename or delete its data model, or import may fail.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/script-editor): Use descriptive script, part and function names plus comments stating inputs/outputs; this produces more accurate Code Assist suggestions.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/script-editor): Always review, test and verify Code Assist suggestions; the tool can generate incorrect code and may suggest older APIs or Lua instead of Luau.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/script-editor): Break code into smaller named functions; named functions produce better Code Assist hints than anonymous functions.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/chat/voice-chat): Enable Voice Chat in Experience Settings > Communication to use the speech-to-text API.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/lesson-plans/build-an-obby-lesson): Learn basic coding and properties concepts so you can check and steer AI output, since AI does not always generate the code you intended.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/production/promotion/content-maturity): Answer the AI interaction question based on whether players can interact with generative AI in the game, not on whether AI was used in development.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/accelerated-workflows): Enable Studio as MCP server via Assistant → … → Manage MCP Servers, and turn on needed features under File → Beta Features; GA features are on by default.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/accelerated-workflows): Point an MCP-aware client at the Studio MCP server so it can read the data model, create and run scripts, edit instances, and playtest.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/accelerated-workflows): Start from the starter project with LLM-friendly markdown context files so a coding harness can plan and build the first game quickly.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/accelerated-workflows): Bring your own API keys via Assistant → … → Manage API Keys to use Anthropic, OpenAI, or Google models.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/ai/accelerated-workflows): Run all generated text through TextService:FilterStringAsync() before showing it to players, as required for LLM NPC dialogue.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/education/build-it-play-it-galactic-speedway/colors-and-textures): Create custom textures by editing provided texture files in Photoshop (paid) or Krita (open-source), varying colors or adding designs.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-an-environment-with-terrain): Build terrain directly in Studio rather than relying on Assistant; brush strokes and material edits are hard to reproduce with AI.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/tutorials/curriculums/core): Use Studio Assistant for routine tasks (creating folders, models, parts, boilerplate event handlers, leaderboards, RemoteFunctions) and do terrain, colors, lighting and gameplay design yourself.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/parts/procedural-models): Procedural models can be generated with Assistant or the Roblox Studio MCP server, or inserted from the Creator Store and customized.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud/guides/advertising): Store the API key and send it in the x-api-key header; grant only ad.campaign:read, ad.campaign:write and ad.billing:read scopes.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/cloud-services/secrets): Open Cloud can also manage secrets programmatically if you prefer automation over the dashboard.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/art/overview-dcc): Use the Roblox Blender plugin to connect your modeling software to Studio and upload model assets directly between applications.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/build-studio-widgets): Call CreateDockWidgetPluginGui only from the command bar or a plugin script; it cannot be called from regular scripts.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/build-studio-widgets): Use the Studio GitHub GUI kit for checkboxes, radio buttons and inputs so widgets match Studio's look and support dark theme.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/build-studio-widgets): Sync widget colors with settings().Studio.Theme:GetColor() and reconnect on Studio.ThemeChanged so widgets follow the user's theme.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/build-studio-widgets): Parent every widget GuiObject to the DockWidgetPluginGui, as you would parent in-game GUI to a ScreenGui.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/build-studio-widgets): UserInputService does not work in Studio widgets; capture keyboard input with a transparent full-screen Frame's InputBegan event instead.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/studio/build-studio-widgets): Use Plugin:StartDrag() on MouseButton1Down and handle PluginDragDropped on the target widget for drag-and-drop between widgets.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/performance-optimization/microprofiler): Pause a spike in Studio and ask Assistant to analyse the capture; it can report bottlenecks and propose fixes, and works via the Studio MCP server.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Write the skill description as specific as possible about what it does and when to use it; Assistant decides whether to load a skill from the description alone.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Keep skill name and description each on a single line when creating manually in the Skills tab.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Don't use the reserved rbx- prefix for your own skill names; it is reserved for Roblox-authored skills.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): To customize a Roblox-authored skill, duplicate it rather than editing it; Roblox skills are read-only and the original gets auto-disabled.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Duplicated Roblox skills don't receive upstream updates; re-duplicate the updated original to get the latest version.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Use rbx-debug to inspect call stacks and variables at runtime instead of adding print statements.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Use rbx-perf-profiling with MicroProfiler traces to diagnose lag, frame-time spikes and memory growth using real data.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Use rbx-unit-test to test ModuleScript contracts with stubs for dependencies and run tests in Play.
- 2026-10-28 Roblox Creator Docs [page](https://create.roblox.com/docs/assistant/skills): Skills are tied to your Roblox account and apply in every place you open in Studio; changes take effect on your next message.
- 2026-10-29 Deconstructor of Fun [23:51](https://youtu.be/NrPjXO_7oKk?t=1431): Steam requires disclosure of shipped generative AI (art, audio, voice, text localization, store assets); coding assistance is exempt. Disclosure may reduce sales, per Yoast analysis.
- 2026-10-30 Roblox DevForum [page](https://devforum.roblox.com/t/x/4966810): Try Scene Generation (/generate_scene in Assistant or Generate > Scene) to prototype scenes from prompts or images; output is editable models, textures and terrain.
- 2026-10-30 Xaiyne [2:04](https://youtu.be/vGfWK6vbuYk?t=124): Use Tripo's 3.1 model for better quality; 2.5 Legacy works on free accounts but looks worse.

Index: [[README]] | Master: [[master-playbook]]
