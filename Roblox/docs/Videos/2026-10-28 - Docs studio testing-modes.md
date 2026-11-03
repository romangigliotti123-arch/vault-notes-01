---
title: "Docs: studio / testing-modes"
url: https://create.roblox.com/docs/studio/testing-modes.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / testing-modes

[Open](https://create.roblox.com/docs/studio/testing-modes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Studio docs on testing modes: Test/Test Here/Run playtests, client/server toggle, pause/resume, multi-client, Party Simulator, Team Test, Device Simulator, Network Simulator, scripted testing services, VR emulation and setup, Player Emulator for localization and region policy.

## Tips
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[testing-debugging-and-qa]]** Test in multiple modes before release because of the client-server model; use Test/Test Here for client-server solo playtests and Server & Clients for multiplayer.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[testing-debugging-and-qa]]** Use Client/Server toggle during solo playtests to see which objects exist on each side; Output labels are blue for client, green for server.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[testing-debugging-and-qa]]** Use Pause/Resume Client or Server (via arrow menu) and Step Forward (1/60 s) to debug ephemeral mechanisms without disabling rendering.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[testing-debugging-and-qa]]** Usually 1-2 simulated clients is sufficient for multi-client tests; up to eight are supported.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[testing-debugging-and-qa]]** Use Network Simulator to add latency, jitter and packet loss when testing Server Authority and UnreliableRemoteEvents, which can be lost or arrive out of order.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[localization-and-international]]** Use Player Emulator with Pseudolocalize and Elongate to find untranslated strings and UI that breaks with longer text; Spanish averages ~30% longer than English, German longer still.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[testing-debugging-and-qa]]** Use StudioTestService and VirtualInput to script multi-client join/leave stress tests and end-to-end UI flow automation in build pipelines.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[cross-platform-and-console]]** Use Device Simulator with Controller Emulator to preview touch, screen size, DPI and gamepad/VR input without owning the device.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[cross-platform-and-console]]** For VR testing on Windows, configure the OpenXR runtime before launching Studio; with multiple headsets, configure only the one you want to test with.
- [page](https://create.roblox.com/docs/studio/testing-modes) **[[social-features-and-virality]]** Use Party Simulator to test party APIs (PartyId, SocialService:GetPartyAsync) with Server & Clients tests without publishing.

## Numbers
- [page](https://create.roblox.com/docs/studio/testing-modes) Simulated clients: **1-2 usually sufficient; up to 8 supported** (Server & Clients multi-client playtest)
- [page](https://create.roblox.com/docs/studio/testing-modes) Step Forward duration: **1/60 s (60 Hz)** (Stepping while simulation is paused)
- [page](https://create.roblox.com/docs/studio/testing-modes) Spanish text length vs English: **~30% longer on average** (Per docs; German is even longer)
- [page](https://create.roblox.com/docs/studio/testing-modes) Minimum GPU for Oculus VR: **NVIDIA GeForce GTX 1060 or equivalent** (Oculus drivers requirement)

## Tools
Roblox Studio, Device Simulator, Network Simulator, Player Emulator, StudioTestService, VirtualInput

## He points to
- Roblox Creator Docs: Studio testing modes

## Topics
[[cross-platform-and-console]] [[localization-and-international]] [[social-features-and-virality]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
