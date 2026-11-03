---
title: GnomeCode - Mindset & Process
creator: GnomeCode
tags: [roblox, gnomecode, theme]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# GnomeCode: Mindset & Process

All GnomeCode tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[analytics-metrics]]
- 2024-11-07 [9:44](https://youtu.be/g9UbIrR0RbU?t=584) Calculate ad cost per new player and compare it to your actual revenue per player; a game with low monetisation loses money on each ad-acquired player. ([[2024-11-07 - I spent 400 USD on Roblox Ads|I spent 400 USD on Roblox Ads...]])
- 2025-03-08 [0:40](https://youtu.be/u_8p65Bsm2Y?t=40) Map your game as ordered funnel steps (join, lobby, elevator, teleport, each checkpoint) and log each with AnalyticsService:LogOnboardingFunnelStepEvent; best for linear games. ([[2025-03-08 - How to Boost your Game using Roblox Funnel Analytics|How to Boost your Game using Roblox Funnel Analyti]])
- 2025-03-08 [2:42](https://youtu.be/u_8p65Bsm2Y?t=162) Log funnel steps server-side from the point where the player actually progresses, e.g. just before teleport logic, so drop-offs reflect real progress. ([[2025-03-08 - How to Boost your Game using Roblox Funnel Analytics|How to Boost your Game using Roblox Funnel Analyti]])
- 2025-03-08 [4:23](https://youtu.be/u_8p65Bsm2Y?t=263) Expect ~24 hours before funnel charts appear; check View Events first to confirm events are arriving. ([[2025-03-08 - How to Boost your Game using Roblox Funnel Analytics|How to Boost your Game using Roblox Funnel Analyti]])
- 2025-03-08 [6:17](https://youtu.be/u_8p65Bsm2Y?t=377) Look for big red drops in step completion; they point to the exact spot to fix, such as a hard encounter or bug. ([[2025-03-08 - How to Boost your Game using Roblox Funnel Analytics|How to Boost your Game using Roblox Funnel Analyti]])

## [[development-process-and-speed]]
- 2021-06-14 [11:05](https://youtu.be/0rMO-VHSuGs?t=665) Set up game state in a per-character setup script on CharacterAdded: clone items and NPCs from templates to spawn points, so respawns restore everything. ([[2021-06-14 - Are YOU making these Game Dev Mistakes|Are YOU making these Game Dev Mistakes?]])
- 2021-12-14 [0:14](https://youtu.be/DanjB0cTfw0?t=14) Use a fixed path with manually placed waypoints for tower defense; it avoids building many invisible walls for PathfindingService. ([[2021-12-14 - How to make a Tower Defense Game - 1 Path Navigation|How to make a Tower Defense Game -  #1 Path Naviga]])
- 2021-12-14 [3:27](https://youtu.be/DanjB0cTfw0?t=207) Organise path pieces and waypoints into separate folders in Workspace to keep the map manageable. ([[2021-12-14 - How to make a Tower Defense Game - 1 Path Navigation|How to make a Tower Defense Game -  #1 Path Naviga]])
- 2023-03-11 [8:37](https://youtu.be/QRwTkEPPChM?t=517) Tidy the workspace at the end of each build session using folders, groups and consistent naming; messy workspaces greatly slow development and collaboration. ([[2023-03-11 - Developer Secrets to Amazing Roblox Building|Developer Secrets to Amazing Roblox Building]])
- 2023-05-18 [31:14](https://youtu.be/TJnV2ycnXZc?t=1874) Finish projects rather than leaving many 'coming soon' games unfinished; the creator names this as his main ongoing weakness. ([[2023-05-18 - My First Games Were Terrible|My First Games Were Terrible...]])
- 2023-07-30 [1:22](https://youtu.be/UsPYgIW3rv8?t=82) Avoid duplicating scripts into every model; keep one script and update all copies from it, so changes are made once. ([[2023-07-30 - Stop Repeating Yourself! Improve Your Code with Collection Service|Stop Repeating Yourself! Improve Your Code with Co]])
- 2024-09-19 [0:35](https://youtu.be/oEWoyT-GBZY?t=35) Enable Output window before coding so errors are visible while building systems step by step. ([[2024-09-19 - How to make a Round Based Game|How to make a Round Based Game]])
- 2024-09-20 [0:00](https://youtu.be/SUZPuQrKJuU?t=0) Name UI image buttons exactly as the map models in ReplicatedStorage.Maps; a spelling mismatch silently breaks the vote lookup. ([[2024-09-20 - How to make a Voting System|How to make a Voting System]])

## [[common-mistakes]]
- 2021-06-14 [0:00](https://youtu.be/0rMO-VHSuGs?t=0) Don't include vanity buttons (info, credits) that do nothing or settings windows with 'coming soon'. Add buttons only when their content exists. ([[2021-06-14 - Are YOU making these Game Dev Mistakes|Are YOU making these Game Dev Mistakes?]])
- 2021-06-14 [9:11](https://youtu.be/0rMO-VHSuGs?t=551) Never kick players on death (e.g. 'please restart'). Kicking forces a full rejoin and hurts replayability; reset the player instead. ([[2021-06-14 - Are YOU making these Game Dev Mistakes|Are YOU making these Game Dev Mistakes?]])
- 2021-07-06 [26:11](https://youtu.be/7vXk_YqxW-c?t=1571) Do not repeat identical free models everywhere; mix plant pots, colours and sizes so the game has its own identity. ([[2021-07-06 - Secrets of Roblox Building - Tips for Better Building|Secrets of Roblox Building - Tips for Better Build]])
- 2022-09-23 [1:22](https://youtu.be/aFKaY-PmR08?t=82) Don't edit other people's scripts until you understand the fundamentals (if statements, functions, properties, variables); otherwise debugging them becomes very hard. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2023-05-18 [15:52](https://youtu.be/TJnV2ycnXZc?t=952) Avoid copy-pasting repeated script blocks; use loops and functions instead. Early repeated if-blocks over 1000 lines were a sign of learning, but refactor early. ([[2023-05-18 - My First Games Were Terrible|My First Games Were Terrible...]])
- 2023-05-18 [8:51](https://youtu.be/TJnV2ycnXZc?t=531) Don't leave large empty spaces in a map; more stuff does not make a map better. Plan where the player goes before adding content. ([[2023-05-18 - My First Games Were Terrible|My First Games Were Terrible...]])
- 2025-02-18 [4:19](https://youtu.be/OyPgQgBSIe4?t=259) Scattering teleport logic across many functions causes mistakes; centralise all teleport-to-room logic in one function so it resets state (e.g. walk speed) consistently. ([[2025-02-18 - How I Fix Bugs in my new Game|How I Fix Bugs in my new Game]])

## [[mindset-and-strategy]]
- 2023-05-18 [20:01](https://youtu.be/TJnV2ycnXZc?t=1201) Keep enjoying the learning process; mocking beginners' code discourages them from continuing to build. ([[2023-05-18 - My First Games Were Terrible|My First Games Were Terrible...]])

## [[testing-debugging-and-qa]]
- 2021-12-14 [7:05](https://youtu.be/DanjB0cTfw0?t=425) Keep the Output window open while scripting; a MoveTo error (passing a Part instead of .Position) only shows there. ([[2021-12-14 - How to make a Tower Defense Game - 1 Path Navigation|How to make a Tower Defense Game -  #1 Path Naviga]])
- 2022-09-23 [3:05](https://youtu.be/aFKaY-PmR08?t=185) Keep code formatted and indented as you write it; use Format Document to make logic blocks readable when hunting bugs. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [4:16](https://youtu.be/aFKaY-PmR08?t=256) Treat any red underline as a real problem; hover for the tooltip. Blue highlighting means Studio recognizes a keyword, so a mismatch shows as red. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [5:38](https://youtu.be/aFKaY-PmR08?t=338) Keep the Output window open while scripting. Click an error there to jump straight to the offending line. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [7:53](https://youtu.be/aFKaY-PmR08?t=473) Read errors as: the script path and line number plus the message. 'attempt to index nil' means the value before the dot was nil, so check for typos and missing objects. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [10:06](https://youtu.be/aFKaY-PmR08?t=606) Syntax errors show in Output, but logic bugs often don't. For those, add print statements at each step to see how far execution gets. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [11:57](https://youtu.be/aFKaY-PmR08?t=717) Print each condition's inputs inside event handlers to confirm the handler fires and each if-check passes. Missing prints show which condition failed. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [14:02](https://youtu.be/aFKaY-PmR08?t=842) Check Instance names for case-sensitive typos. 'humanoid' vs 'Humanoid' causes FindFirstChild or FirstChild lookups to silently return nil. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [15:02](https://youtu.be/aFKaY-PmR08?t=902) Use breakpoints and the Watch window instead of prints to inspect variable values line by line. Remove breakpoints when done. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [18:15](https://youtu.be/aFKaY-PmR08?t=1095) Check the Roblox Creator Hub/Wiki first for each API. It lists required structure (e.g. HumanoidRootPart, Head connected to Torso) and gotchas with code samples. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2022-09-23 [19:40](https://youtu.be/aFKaY-PmR08?t=1180) Search the Developer Forum for your exact error message before asking; the same problem has often been solved already. ([[2022-09-23 - The Dark Arts of Troubleshooting|The Dark Arts of Troubleshooting]])
- 2024-09-20 [14:18](https://youtu.be/SUZPuQrKJuU?t=858) Make sure the map-selection function actually returns its value; a missing return caused 'attempt to index nil' when spawning players. ([[2024-09-20 - How to make a Voting System|How to make a Voting System]])
- 2025-02-18 [0:52](https://youtu.be/OyPgQgBSIe4?t=52) Reproduce race-condition bugs by adding artificial replication lag in Studio settings (e.g. 0.5s) to expose double-pickup exploits. ([[2025-02-18 - How I Fix Bugs in my new Game|How I Fix Bugs in my new Game]])

Up: [[GnomeCode - How to make successful Roblox games]]
