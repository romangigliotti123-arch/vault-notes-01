---
name: my-demo-devforum-bug
description: "Turns my messy bug description and pasted Output log lines into a clean Roblox DevForum bug report: specific title, expected vs actual, minimal numbered repro steps, frequency, environment, exact log lines, and a list of what I still must attach. Use for 'write a devforum bug report', 'clean up this bug for the forum', 'report this Studio bug'."
---

# my-demo-devforum-bug

Writes one paste-ready DevForum bug report from whatever the user knows, following the structure Roblox asks for in "How to post a Bug Report" (title, expected vs actual, where, when, media, minimal repro steps with frequency, repro file, extra info per bug type).

## Steps
1. Read what the user gave: the description, any Output or console lines, a place link, screenshots. Ask ONCE for the two things that decide the category and cannot be guessed: does it happen only in Studio, or also in a game joined from the website; and how often it reproduces (always, about half, rarely).
2. Pick the category: only in Studio = Studio Bugs; also in a joined game = Engine Bugs; website or app = the matching website category; a crash, freeze or disconnect = say so and ask for the dump file.
3. Write the post in this order, each part short:
   - **Title**: names the exact symptom and the object, under 90 characters, no "help" or "bug" alone.
   - **Description**: expected behavior, then actual behavior, two or three sentences.
   - **Where**: place or user links as given; never "my game" or "my group".
   - **When**: date, time and timezone it started, if the user knows.
   - **Reproduction steps**: numbered, minimal, one action per step, specific names (Explorer paths, property values), enough that nobody has to guess.
   - **Frequency**: 100%, about 50%, or rare, as the user said.
   - **Environment**: Studio version, operating system, device, and whether it still happens with plugins disabled.
   - **Output**: the log lines exactly as pasted in a code block, at most 15, nothing edited.
   - **Workaround**: only if the user has one.
4. Mark every missing fact as `UNKNOWN - fill in` and list those, plus the attachments the category needs, as a checklist: a minimal repro place file (always for script, instance or setup bugs), a short video or screenshot, a dump file for crashes, a microprofiler dump for lag, system information for graphics.
5. Check before replying: nothing invented (versions, times, counts), steps can be followed in order, the title matches the description, no private place link or token in the text.
6. Reply in short dot points with the post inside one code block, then the checklist. End with three lines: `**Done** - <what was written>` / `**You** - <what is UNKNOWN and what to attach>` / `**Next** - <post it in the category named above, or ask me to tighten the repro steps>`.

## Rules
- Facts only from the user's own text and files. A guess is written as a guess.
- Never post anything anywhere; the user pastes it.
- "Me too" replies are not bug reports: for someone else's thread, write a reply that adds new reproduction detail or stay silent.
