---
title: stewiepfing - Studio & Scripting
creator: stewiepfing
tags: [roblox, stewiepfing, theme]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# stewiepfing: Studio & Scripting

All stewiepfing tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2024-04-23 [10:50](https://youtu.be/qMdRT1xf9GM?t=650) Spawn popup orbs on the client with a LocalScript so only the player sees them; setting the count too high can crash the game. ([[2024-04-23 - Making Your Game More Satisfying Roblox Studio|Making Your Game More Satisfying | Roblox Studio]])
- 2024-04-23 [5:15](https://youtu.be/qMdRT1xf9GM?t=315) Run each orb in its own task.spawn thread so the loop doesn't block. ([[2024-04-23 - Making Your Game More Satisfying Roblox Studio|Making Your Game More Satisfying | Roblox Studio]])
- 2025-04-27 [0:19](https://youtu.be/e48wgHQll2Y?t=19) Scale UI strokes with viewport height: store thickness at 1080p baseline and set thickness = viewportSize.Y × (originalThickness/1080) so borders look the same on phones. ([[2025-04-27 - Simple Things Mobile Players LOVE! Roblox Studio|Simple Things Mobile Players LOVE! | Roblox Studio]])
- 2025-04-27 [4:30](https://youtu.be/e48wgHQll2Y?t=270) Use WaitForChild on required modules in replicated scripts; otherwise code runs before replication and errors on load. ([[2025-04-27 - Simple Things Mobile Players LOVE! Roblox Studio|Simple Things Mobile Players LOVE! | Roblox Studio]])
- 2025-08-10 [7:34](https://youtu.be/THpSS73tveg?t=454) Format numbers inside the display module, not before sending them, because adding 1k to a number fails if the number is already a string. ([[2025-08-10 - Must-Have Features For YOUR Simulator Game! Roblox Studio|Must-Have Features For YOUR Simulator Game! | Robl]])

## [[building-art-and-assets]]
- 2024-04-23 [2:39](https://youtu.be/qMdRT1xf9GM?t=159) Use your own custom currency icon rather than default toolbox icons; the creator says custom is better. ([[2024-04-23 - Making Your Game More Satisfying Roblox Studio|Making Your Game More Satisfying | Roblox Studio]])
- 2025-04-27 [8:50](https://youtu.be/e48wgHQll2Y?t=530) Apply UIAspectRatioConstraint to frames and images so shapes keep their proportions across phone, tablet and PC resolutions. ([[2025-04-27 - Simple Things Mobile Players LOVE! Roblox Studio|Simple Things Mobile Players LOVE! | Roblox Studio]])
- 2025-08-10 [2:18](https://youtu.be/THpSS73tveg?t=138) Store pet info as a data table with name, rarity, add-on and generic keys; the script checks for add-on keys and falls back to generic text. ([[2025-08-10 - Must-Have Features For YOUR Simulator Game! Roblox Studio|Must-Have Features For YOUR Simulator Game! | Robl]])
- 2025-08-10 [5:28](https://youtu.be/THpSS73tveg?t=328) Format numbers in the thousands (5,000+) into compact form like 1k so they are readable; unformatted large numbers are hard for players to read. ([[2025-08-10 - Must-Have Features For YOUR Simulator Game! Roblox Studio|Must-Have Features For YOUR Simulator Game! | Robl]])
- 2025-08-10 [12:00](https://youtu.be/THpSS73tveg?t=720) When building gradients, always set a transparency sequence and end the color sequence with the starting color so the animated gradient loops without clipping. ([[2025-08-10 - Must-Have Features For YOUR Simulator Game! Roblox Studio|Must-Have Features For YOUR Simulator Game! | Robl]])
- 2025-08-10 [15:02](https://youtu.be/THpSS73tveg?t=902) Drive orb effects with clamped elapsed time divided by duration and bezier curves; disconnect and tween parts out when the clamp reaches 1. ([[2025-08-10 - Must-Have Features For YOUR Simulator Game! Roblox Studio|Must-Have Features For YOUR Simulator Game! | Robl]])

Up: [[stewiepfing - How to make successful Roblox games]]
