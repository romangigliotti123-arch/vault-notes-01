---
title: MaximumADHD - How to make successful Roblox games
tags: [roblox, maximumadhd, playbook]
videos: 15
generated: 2026-10-29
credibility: insufficient
credibility_score: n/a
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# MaximumADHD - How to make successful Roblox games

This corpus cannot support a full game-making playbook. Of 15 short videos, 12 have no usable transcript and the rest are brief tutorials, so the points below come mostly from titles and are unverified. Across the titles, the creator's focus is engine-level mechanics: rendering and culling, asset streaming, animation and server authority, and wait() timing. The corpus has no verified advice on game ideas, monetisation, growth, or live operations. Treat the steps as directional only and check each against the creator's own videos or Roblox documentation before relying on it.

**Style:** Short, technical, engine-focused videos on rendering, scripting internals, and Roblox platform mechanics, often with demos. Suits developers who want low-level performance and networking knowledge. Not a source for game design, monetisation, or growth strategy.

## Playbook
1. **Idea: pick ideas that exercise engine mechanics** [[game-ideas-and-genres]]: No game-ideation advice exists in the corpus. The only evidence is technical topics (culling, streaming, server authority). Unverified inference: concepts with heavy rendering or networking demands need early performance planning. Based on titles 99kCiZyzJJM and 1dA3Xm2aF6E.
2. **Build: use Source/PBR-ready art pipelines carefully** [[building-art-and-assets]]: Titles suggest importing external models (7BDeV4hDNrA), physically based rendering (DJw4PRsRcK8), custom auto-exposure (9oPMEeTRDfU), and 4k materials (ea85gs86NFA). Transcripts are empty, so no specific settings or thresholds are known. Check new material support against current Roblox docs.
3. **Build: model mesh topology deliberately** [[building-art-and-assets]]: The creator argues old hats had poor topology and calls it worse than other notoriously bad models (aX-hBbCgTJo). This is opinion on quality, not a documented rule. Keep geometry clean and avoid unnecessary density; no numeric targets are given.
4. **Build: avoid wait() for timing under load** [[scripting-and-performance]]: Two videos argue Roblox's stock wait() is unreliable under heavy use (cLXOWrf7l9g, cj_21dL_W38). The fix is not described in any available transcript. Use event-driven or task-based timing and verify under load in a test server.
5. **Build: cull and stream what the camera cannot see** [[optimization-and-streaming]]: Frustum culling (99kCiZyzJJM) and occlusion culling (1dA3Xm2aF6E) skip rendering of hidden objects. Asset streaming (G1rIINVKi1k) can cause softlocks. Note that 1dA3Xm2aF6E's title refers to real-time physics, and its content is unverified. Test streaming on low-end clients.
6. **Build: treat animations and state as server-authoritative** [[client-server-and-remotes]]: Animator desync (i76Eyy9lc3w) and the Server Authority video (_gR7ZmmaulE) indicate that client-side visual state can diverge from the server. Titles only; no implementation details are available. Decide which state the server owns before building combat or movement.
7. **Build: check platform behaviour changes before shipping** [[roblox-platform-changes]]: The Server Authority video (_gR7ZmmaulE, dated 2025-12-09) suggests a platform-level change. The corpus does not explain what changed. Re-read current Roblox release notes for networking changes before launch.
8. **Launch: profile and fix known problem areas before release** [[testing-debugging-and-qa]]: Optimised ctf_2fort (Pg56zq9wLI0) suggests a before-and-after optimisation pass on a real map. The transcript is empty, so the specific techniques are unknown. Profile load time and draw calls on a map of realistic size before launch.
9. **Launch: verify scripts under stress before release** [[testing-debugging-and-qa]]: Repeat the wait() and animation tests in a stress test with many players or NPCs, since the creator's concerns are load-dependent (cLXOWrf7l9g, i76Eyy9lc3w). No threshold values are given in the source.
10. **Growth: announce with visuals** [[trailers-and-video-marketing]]: The corpus has no growth advice. The only audience signal is view counts: 34,136 views on the 4k materials video (ea85gs86NFA), versus 1,215 to 4,851 views on the others. Visual upgrade announcements may draw more interest. This is a single data point, not a tested rule.
11. **Growth: explain technical changes for community reach** [[community-and-discord]]: Videos that explain engine behaviour (wait() instability, server authority) suggest that technical explainers attract developers. Based on title and view counts only, with no transcripts to confirm the approach.
12. **Live ops: fix softlocks and streaming bugs quickly** [[updates-live-ops]]: The asset streaming softlock video (G1rIINVKi1k) and animator desync bug (i76Eyy9lc3w) imply that streaming and replication bugs need prompt patches. No patch process is described in the corpus.
13. **Live ops: ship visual updates as dated releases** [[events-and-seasonal-content]]: The 4k materials update (ea85gs86NFA, 2026-09-09) and optimised ctf_2fort (Pg56zq9wLI0, 2025-10-22) show dated map and material updates. Release updates on a schedule and log what changed for players and testers.

## Key numbers
- cLXOWrf7l9g: 0:47 length, 4604 views (wait() instability, 2020-05-07)
- 7N6uwVLWzpc: 1:56 length, 4851 views (facial animation data, 2023-04-28)
- ea85gs86NFA: 2:59 length, 34136 views (4k materials update, 2026-09-09)
- Pg56zq9wLI0: 2:09 length, 2674 views (optimized ctf_2fort, 2025-10-22)
- G1rIINVKi1k: 1:46 length, 1215 views (asset streaming softlock, 2025-08-11)
- cj_21dL_W38: 47-second video (wait() visualization, 2020-05-25)
- 7BDeV4hDNrA: 9:27 length (Source model autoporting, 2021-08-18)
- 99kCiZyzJJM: 1:23 length (frustum culling, 2018-07-19)
- 1dA3Xm2aF6E: 1:32 length (occlusion culling, 2024-09-07)
- i76Eyy9lc3w: 1:26 length (animator desync, 2022-11-16)
- _gR7ZmmaulE: 1:25 length (server authority, 2025-12-09)
- DJw4PRsRcK8: 1:03 length (PBR, 2019-10-18)
- 9oPMEeTRDfU: 1:13 length (custom autoexposure, 2019-06-23)
- xh9AQtZ4NBA: short tutorial, head scaling via Lua (2018-08-03)
- aX-hBbCgTJo: short rant on hat topology (2024-12-15), no length given

## Common mistakes
- Relying on wait() for precise timing under heavy load (cLXOWrf7l9g, cj_21dL_W38)
- Assuming client-side animations match server state (i76Eyy9lc3w)
- Ignoring asset streaming, which can cause softlocks on slower clients (G1rIINVKi1k)
- Rendering objects outside the camera view instead of culling them (99kCiZyzJJM, 1dA3Xm2aF6E)
- Shipping without optimising maps first (Pg56zq9wLI0)
- Using old, dense, or poorly topologised meshes (aX-hBbCgTJo)
- Missing platform networking changes such as server authority updates (_gR7ZmmaulE)
- Treating title-only videos as verified teaching; most transcripts were empty

## Launch checklist
- [ ] Profile draw calls and frame time on a realistic-size map (Pg56zq9wLI0, 99kCiZyzJJM)
- [ ] Confirm culling and streaming behave on low-end clients (G1rIINVKi1k, 1dA3Xm2aF6E)
- [ ] Replace stock wait() in timing-critical code and test under load (cLXOWrf7l9g, cj_21dL_W38)
- [ ] Stress-test animations and state replication with many players (i76Eyy9lc3w)
- [ ] Decide which state the server owns before shipping combat or movement (_gR7ZmmaulE)
- [ ] Check mesh topology on hero models and remove unnecessary density (aX-hBbCgTJo)
- [ ] Verify material and lighting changes against current Roblox docs (ea85gs86NFA, DJw4PRsRcK8, 9oPMEeTRDfU)
- [ ] Verify imported models, including Source-ported assets (7BDeV4hDNrA)
- [ ] Check head and avatar part scaling with Lua if used (xh9AQtZ4NBA)

## Theme notes
- MaximumADHD - Games Mentioned
- [[MaximumADHD - Numbers & Benchmarks]]
- [[MaximumADHD - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2018-07-19 - Roblox Frustum Culling Visualized|[Roblox] Frustum Culling Visualized]] (10,210 views, 2018-07-19): Title suggests frustum culling demo; transcript empty, so unverified.
- [[2018-08-03 - Instanced Head Scaling in Lua|Instanced Head Scaling in Lua]] (1,917 views, 2018-08-03): Short Lua tutorial on scaling avatar head instances; technical, no business advice.
- [[2019-06-23 - Custom AutoExposure|Custom AutoExposure]] (6,674 views, 2019-06-23): Custom AutoExposure video; title only, content unverified.
- [[2019-10-18 - Roblox Physically Based Rendering|[Roblox] Physically Based Rendering]] (14,068 views, 2019-10-18): Physically based rendering in Roblox; title-only, inferred short material overview.
- [[2020-05-07 - Instability of the wait() function while in heavy use|Instability of the wait() function while in heavy ]] (4,604 views, 2020-05-07): Argues wait() becomes unstable under heavy use; no transcript to confirm.
- [[2020-05-25 - Another visualization of why Roblox's stock wait() function is broken|Another visualization of why Roblox's stock wait()]] (7,039 views, 2020-05-25): Short visual demo of wait() unreliability; transcript missing, content unverified.
- [[2021-08-18 - Autoporting Source Engine models into Roblox|Autoporting Source Engine models into Roblox.]] (19,466 views, 2021-08-18): Title suggests importing Source Engine models into Roblox; transcript empty.
- [[2022-11-16 - Animator Desync Bug|Animator Desync Bug]] (3,137 views, 2022-11-16): Animator desync bug fix, likely replication; no transcript to confirm details.
- [[2023-04-28 - Roblox Facial Animation Data Extraction|Roblox Facial Animation Data Extraction]] (4,851 views, 2023-04-28): Facial animation data extraction; title and metadata only, content unverified.
- [[2024-09-07 - Roblox Occlusion Culling - Real-time Physics|Roblox Occlusion Culling - Real-time Physics]] (4,805 views, 2024-09-07): Occlusion culling with real-time physics; title-only, nothing extracted.
- [[2024-12-15 - Old Roblox hats had the best topology of All Time|Old Roblox hats had the best topology of All Time]] (7,689 views, 2024-12-15): Rant that old hat meshes have poor topology; opinion, not building rules.
- [[2025-08-11 - Asset Streaming Softlock|Asset Streaming Softlock?]] (1,215 views, 2025-08-11): Asset streaming softlock video; title-only, cause and fix unknown.
- [[2025-10-22 - Optimized ctf_2fort|Optimized ctf_2fort]] (2,674 views, 2025-10-22): Optimised ctf_2fort map; transcript empty, techniques unknown.
- [[2025-12-09 - Roblox Server Authority|Roblox Server Authority]] (19,119 views, 2025-12-09): Roblox Server Authority video; title-only, implications unverified.
- [[2026-09-09 - Roblox - 4k Materials Update|Roblox - 4k Materials Update]] (34,136 views, 2026-09-09): 4k materials update, highest-viewed video here; transcript empty.
