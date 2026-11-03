---
title: CritDEV - How to make successful Roblox games
tags: [roblox, critdev, playbook]
videos: 3
generated: 2026-10-29
credibility: trusted
credibility_score: 7.8
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# CritDEV - How to make successful Roblox games

CritDEV's playbook is narrow: it covers making Roblox NPCs path, track players, and open doors with the free Forbidden pathfinding module (V2). Core advice: use a module instead of raw PathfindingService, give NPCs a Humanoid, Head, and HumanoidRootPart, run NPC logic on the server, keep server network ownership via an anti-lag script, and model doors as PathfindingLinks with labels. Idea-stage, growth, and live-ops advice does not appear in these three videos, so those stages have no evidence here.

**Style:** Hands-on tool tutorials for scripters building NPC pathing. Walks through a module's config, a test rig, and a concrete example, with little business or marketing content. Suits developers who want working NPC chase or door code, not game-design or monetisation guidance.

## Playbook
1. **Idea: build around NPCs that navigate the map** [[game-ideas-and-genres]]: The videos demonstrate NPCs that track the closest player and pass through doors. Scope a game idea where pathing NPCs are core, not decorative. No broader idea-validation advice is given in these videos.
2. **Build: prepare the NPC rig and insert the module** [[physics-pathfinding-and-npc-ai]]: Give the NPC a Humanoid, a Head, and a HumanoidRootPart (or a PrimaryPart). Insert the Forbidden V2 module, call restoreDefaults before changing any config, and use visualize to debug paths.
3. **Build: run NPC pathing on the server** [[client-server-and-remotes]]: Keep pathfinding and tracking logic on the server. It is not suitable if the logic must run on the client, because of ping and replication.
4. **Build: insert the anti-lag network-ownership script** [[scripting-and-performance]]: Always include the anti-lag script so the server keeps network ownership of NPC parts. Without it, parts stutter and can fly apart near players.
5. **Build: tune chase responsiveness** [[physics-pathfinding-and-npc-ai]]: Adjust the direct-move switch timer in config (the example uses 1 second instead of the default) and target offsets to make NPC chases feel more responsive.
6. **Build: model doors as labelled PathfindingLinks** [[building-and-level-design]]: Place two anchored, non-collidable parts on each side of a door, each with an Attachment, joined by a PathfindingLink. Name the door folder to match the link label (e.g. 'door one').
7. **Build: dispatch link handlers from one manager** [[code-architecture-and-frameworks]]: Put each custom link handler in its own module and dispatch by label from a single manager. Open the door by setting its open BoolValue to true, then humanoid:MoveTo and wait for MoveToFinished. Always return true so pathing resumes.
8. **Launch: set collision groups** [[scripting-and-performance]]: Make doors not collide with NPCs, and NPCs not collide with each other, to prevent stuck NPCs and improve pathing performance.
9. **Launch: strip test code before release** [[testing-debugging-and-qa]]: Remove Config.Tracking and any hardcoded player lookup. These exist only for testing.

## Key numbers
- Around 10x smoother NPC movement claimed with anti-lag enabled (hqWLpWsWF00, 2025-07-25; speaker's own demo)
- About 20 prior Forbidden V1 videos being remade as V2 (hqWLpWsWF00, 2025-07-25)
- 3-second intentional wait after teleporting an NPC over a wall before resuming path (Om2vAKMW1Pw, 2025-08-18)
- 5-second custom wait in the teleport-and-wait link handler example (Om2vAKMW1Pw, 2025-08-18)
- About 30 minutes to integrate a random marketplace door with Forbidden (nEvM3aYY2pY, 2025-10-07)
- Direct-move switch timer example: 1 second instead of default (hqWLpWsWF00, 2025-07-25)

## Common mistakes
- Using raw PathfindingService for chasing moving targets; the videos recommend a module such as Forbidden instead.
- Changing config without calling restoreDefaults first, since config values persist between calls.
- Skipping the anti-lag network-ownership script, so NPC parts stutter and explode near players.
- Forgetting that a PathfindingLink handler must return true, or the Forbidden movement loop stalls.
- Naming a door folder differently from its PathfindingLink label, so the script cannot find the door model.
- Leaving NPCs and doors in default collision, which causes NPCs to block each other and get stuck.
- Running NPC pathing logic on the client, where ping and replication make it unreliable.
- Shipping Config.Tracking or the hardcoded player lookup to release.

## Launch checklist
- [ ] NPC has Humanoid, Head, and HumanoidRootPart (or PrimaryPart).
- [ ] Forbidden V2 module inserted; restoreDefaults called before config changes.
- [ ] Pathing and tracking logic runs on the server.
- [ ] Anti-lag network-ownership script inserted.
- [ ] Direct-move timer and target offsets tuned and tested on a rig.
- [ ] Each door has a folder named to match its PathfindingLink label.
- [ ] Door link parts are anchored, non-collidable, and have Attachments.
- [ ] Each link handler returns true; fallback warns and returns true.
- [ ] Doors open via BoolValue set to true; NPC uses MoveTo and waits for MoveToFinished.
- [ ] Collision groups: doors vs NPCs and NPCs vs NPCs set as described.
- [ ] Config.Tracking and hardcoded player lookup removed.

## How the advice changed over time
- Forbidden V1 is being remade as V2 (hqWLpWsWF00, 2025-07-25); use the V2 module and its config options rather than V1 instructions.

## Theme notes
- [[CritDEV - Studio & Scripting|Studio & Scripting]]
- [[CritDEV - Mindset & Process|Mindset & Process]]
- CritDEV - Games Mentioned
- [[CritDEV - Numbers & Benchmarks]]
- [[CritDEV - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]] (16,136 views, 2025-07-25): Forbidden V2 walkthrough: insert the module, test rig, config options, and track closest player.
- [[2025-08-18 - The ULTIMATE Guide to Pathfinding Links|The ULTIMATE Guide to Pathfinding Links]] (3,405 views, 2025-08-18): Custom PathfindingLink handlers in a label-keyed manager; return true so NPCs resume pathing.
- [[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]] (2,306 views, 2025-10-07): Free Forbidden library lets NPCs open doors via labelled links, with collision groups to avoid jams.
