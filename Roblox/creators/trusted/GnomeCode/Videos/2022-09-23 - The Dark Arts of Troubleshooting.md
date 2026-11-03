---
title: "The Dark Arts of Troubleshooting"
url: https://youtu.be/aFKaY-PmR08
creator: GnomeCode
official: false
advice_density: medium
date: 2022-09-23
views: 33531
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# The Dark Arts of Troubleshooting

[Watch](https://youtu.be/aFKaY-PmR08) | GnomeCode | 33,531 views | 2022-09-23

## Summary
Beginner tutorial on debugging Roblox Luau scripts. Covers reading red underlines and tooltips, using the Output window to trace errors back to lines, formatting code, print statements and breakpoints with the watch window for logic bugs, and where to get help (Wiki, Developer Forum, Discord) and how to ask well.

## Tips
- [1:22](https://youtu.be/aFKaY-PmR08?t=82) **[[common-mistakes]]** Don't edit other people's scripts until you understand the fundamentals (if statements, functions, properties, variables); otherwise debugging them becomes very hard.
- [3:05](https://youtu.be/aFKaY-PmR08?t=185) **[[testing-debugging-and-qa]]** Keep code formatted and indented as you write it; use Format Document to make logic blocks readable when hunting bugs.
- [4:16](https://youtu.be/aFKaY-PmR08?t=256) **[[testing-debugging-and-qa]]** Treat any red underline as a real problem; hover for the tooltip. Blue highlighting means Studio recognizes a keyword, so a mismatch shows as red.
- [5:38](https://youtu.be/aFKaY-PmR08?t=338) **[[testing-debugging-and-qa]]** Keep the Output window open while scripting. Click an error there to jump straight to the offending line.
- [7:53](https://youtu.be/aFKaY-PmR08?t=473) **[[testing-debugging-and-qa]]** Read errors as: the script path and line number plus the message. 'attempt to index nil' means the value before the dot was nil, so check for typos and missing objects.
- [10:06](https://youtu.be/aFKaY-PmR08?t=606) **[[testing-debugging-and-qa]]** Syntax errors show in Output, but logic bugs often don't. For those, add print statements at each step to see how far execution gets.
- [11:57](https://youtu.be/aFKaY-PmR08?t=717) **[[testing-debugging-and-qa]]** Print each condition's inputs inside event handlers to confirm the handler fires and each if-check passes. Missing prints show which condition failed.
- [14:02](https://youtu.be/aFKaY-PmR08?t=842) **[[testing-debugging-and-qa]]** Check Instance names for case-sensitive typos. 'humanoid' vs 'Humanoid' causes FindFirstChild or FirstChild lookups to silently return nil.
- [15:02](https://youtu.be/aFKaY-PmR08?t=902) **[[testing-debugging-and-qa]]** Use breakpoints and the Watch window instead of prints to inspect variable values line by line. Remove breakpoints when done.
- [18:15](https://youtu.be/aFKaY-PmR08?t=1095) **[[testing-debugging-and-qa]]** Check the Roblox Creator Hub/Wiki first for each API. It lists required structure (e.g. HumanoidRootPart, Head connected to Torso) and gotchas with code samples.
- [18:57](https://youtu.be/aFKaY-PmR08?t=1137) **[[scripting-and-performance]]** Read event and method docs for hidden behaviour. For example, Humanoid:MoveTo stops after about 8 seconds and needs handling for long moves.
- [19:40](https://youtu.be/aFKaY-PmR08?t=1180) **[[testing-debugging-and-qa]]** Search the Developer Forum for your exact error message before asking; the same problem has often been solved already.
- [20:18](https://youtu.be/aFKaY-PmR08?t=1218) **[[community-and-discord]]** When asking for help, include the exact error, script, line number, and what you already tried. Narrow the problem down first and thank helpers.

## Numbers
- [18:57](https://youtu.be/aFKaY-PmR08?t=1137) Humanoid:MoveTo timeout: **8 seconds** (Humanoid stops walking after eight seconds per the Wiki's MoveTo docs)
- [17:12](https://youtu.be/aFKaY-PmR08?t=1032) Velocity threshold in demo script: **200** (Demo trampoline script checks root velocity below 200 before applying force)

## Tools
Roblox Studio Output window, Roblox Studio Watch window, Roblox Studio breakpoints, Format Document (Studio script editor), Roblox Creator Hub/Wiki, Roblox Developer Forum

## He points to
- Roblox Wiki (documentation)
- Roblox Developer Forum
- Gnomeland Discord (presenter's server)
- NumCode's beginner scripting series

## Quotes
- [20:18](https://youtu.be/aFKaY-PmR08?t=1218) "it's really important that you try and give it as much information as possible"

## Topics
[[common-mistakes]] [[community-and-discord]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[GnomeCode - How to make successful Roblox games]]
