---
title: byteblox100 - Mindset & Process
creator: byteblox100
tags: [roblox, byteblox100, theme]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# byteblox100: Mindset & Process

All byteblox100 tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[analytics-metrics]]
- 2024-11-20 [18:09](https://youtu.be/Jl0SdXksQsI?t=1089) Estimate revenue as sessions times average session length times price per interval. Use real playtime data, not guesses, before pricing anything. ([[2024-11-20 - I Made Literally Everything Cost Robux|I Made Literally Everything Cost Robux]])

## [[development-process-and-speed]]
- 2023-12-17 [0:41](https://youtu.be/9YwYDuIuih4?t=41) Learn debugging early: the speaker argues being able to fix errors is what keeps beginners motivated to keep learning. ([[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]])

## [[common-mistakes]]
- 2024-02-20 [5:11](https://youtu.be/okGvZjneq60?t=311) Do not spam ads everywhere; irrational ad placement annoys players and hurts retention. ([[2024-02-20 - Should Your Roblox Game Have Ads|Should Your Roblox Game Have Ads?]])
- 2024-05-10 [3:09](https://youtu.be/D6DwmHcmwwQ?t=189) Uncleaned particles or effects added on character respawn cause steady lag and eventual crashes; delete old effects on reset. ([[2024-05-10 - How One Memory Leak Can Kill Your Game|How One Memory Leak Can Kill Your Game]])
- 2024-06-07 [1:22](https://youtu.be/s2XUzTyCdK4?t=82) A while true loop with no yield will exhaust execution time and hang the game; games cannot run true infinity, so simulate it instead. ([[2024-06-07 - How “Impossible” Features Are Actually Coded|How “Impossible” Features Are Actually Coded]])
- 2024-06-07 [18:33](https://youtu.be/s2XUzTyCdK4?t=1113) Ensure triggers have CanCollide off and transparency off so they do not block the player while remaining invisible when intended. ([[2024-06-07 - How “Impossible” Features Are Actually Coded|How “Impossible” Features Are Actually Coded]])
- 2024-06-24 [13:20](https://youtu.be/ekM2z9FMhZc?t=800) Parenting a cloned item to the wrong container or forgetting to connect the button's Activated event on every clone causes bugs; verify each step. ([[2024-06-24 - How to Make a Game Addictive in 15 Minutes|How to Make a Game Addictive in 15 Minutes]])
- 2024-11-17 [26:54](https://youtu.be/1KKQ6YrktTk?t=1614) Don't treat mobile as an afterthought; developers who build for PC first get bad mobile experiences, while top games cater to mobile heavily. ([[2024-11-17 - Roblox Mobile Developers Are Insanely Lazy|Roblox Mobile Developers Are Insanely Lazy]])
- 2024-11-20 [16:06](https://youtu.be/Jl0SdXksQsI?t=966) Do not gate basic movement or camera behind purchases. The creator says this breaks Roblox ToS and risks account suspension. ([[2024-11-20 - I Made Literally Everything Cost Robux|I Made Literally Everything Cost Robux]])

## [[testing-debugging-and-qa]]
- 2023-12-17 [2:30](https://youtu.be/9YwYDuIuih4?t=150) Click the gutter next to a line to set a breakpoint; the game enters debug mode and halts there so you can inspect state. ([[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]])
- 2023-12-17 [4:21](https://youtu.be/9YwYDuIuih4?t=261) Step Into runs the next line that does something; Step Over runs a function without entering it; Step Out runs to the end of the current function. ([[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]])
- 2023-12-17 [9:18](https://youtu.be/9YwYDuIuih4?t=558) Add a condition to a breakpoint (e.g. testVar == 100) so it only halts when that condition is true, avoiding manual stopping in long runs. ([[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]])
- 2023-12-17 [10:33](https://youtu.be/9YwYDuIuih4?t=633) Use a log message on a breakpoint (a log point) to print variable values without halting; enable Continue Execution to keep the script running. ([[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]])
- 2023-12-17 [14:10](https://youtu.be/9YwYDuIuih4?t=850) Enable Remove Breakpoint on Hit when debugging loops so the breakpoint deletes itself after the first hit. ([[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]])
- 2023-12-17 [14:58](https://youtu.be/9YwYDuIuih4?t=898) Set Trigger At to client, server, or edit so breakpoints in shared ModuleScripts only fire in the context you're debugging. ([[2023-12-17 - Roblox Debugging (done efficiently)|Roblox Debugging (done efficiently)]])
- 2024-02-26 [2:57](https://youtu.be/VitH_k_-AZU?t=177) Compare unreliable vs reliable remotes by firing both in a loop and counting received messages on the server; mismatched counts reveal dropped events. ([[2024-02-26 - All Use Cases for UnreliableRemoteEvents|All Use Cases for UnreliableRemoteEvents]])
- 2024-05-10 [2:51](https://youtu.be/D6DwmHcmwwQ?t=171) Print the child count of your spawn folder (#folder:GetChildren()) to confirm instance counts stay near expected values. ([[2024-05-10 - How One Memory Leak Can Kill Your Game|How One Memory Leak Can Kill Your Game]])
- 2024-05-10 [5:17](https://youtu.be/D6DwmHcmwwQ?t=317) In large codebases, a single missed Destroy call causes a leak; add count logging to find where instances pile up before players feel lag. ([[2024-05-10 - How One Memory Leak Can Kill Your Game|How One Memory Leak Can Kill Your Game]])
- 2024-06-07 [16:45](https://youtu.be/s2XUzTyCdK4?t=1005) Verify generation by placing marker parts and checking whether they disappear after touching the trigger. ([[2024-06-07 - How “Impossible” Features Are Actually Coded|How “Impossible” Features Are Actually Coded]])

Up: [[byteblox100 - How to make successful Roblox games]]
