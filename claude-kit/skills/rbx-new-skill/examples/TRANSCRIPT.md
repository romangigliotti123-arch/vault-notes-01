# Worked example: a user makes `my-demo-devforum-bug`

A real run of `rbx-new-skill` in a throw-away copy of a vault (a temp install of this kit, a git clone as the vault folder, nothing of the real vault touched). The skill that came out is `my-demo-devforum-bug/SKILL.md` next to this file; it passes the shipped check exactly as written. The helper is `scripts/my_skill.py` (shown as `my_skill.py`; paths shortened).

## 1. Goal (one line)

> "When I find a Studio bug I paste a messy description and the Output lines. I want a clean DevForum bug report out of that."

Kind: a **skill** (instructions Claude follows in the main chat; no separate worker needed).

## 2. Overlap check

```
$ my_skill.py overlap "turn a messy bug description and my Output log lines into a clean DevForum bug report"
/rbx-low-usage             skill overlap 0.30 (3 shared words)
rbx-selfbuilder            agent overlap 0.30 (3 shared words)
rbx-auditor                agent overlap 0.20 (2 shared words)
OVERLAP: none close (best 0.30). A new item is justified; keep its description distinct from the three above.
```

`/rbx-list` shows nothing about forum posts either (`rbx-playtest` keeps an internal bug ledger, a different job), so a new skill is justified.

## 3. Short research (official docs only, 2 pages)

Roblox's own page "How to post a Bug Report" (devforum.roblox.com) asks for: an accurate title; a description of expected vs actual behavior; where (place, user or group links, never "my group"); when it started with timezone; media; **minimal, specific reproduction steps with how often they reproduce (100%, 50%, rarely)**; a minimal repro place file for script/setup bugs; and extra information by type (Studio bugs: still happens with plugins disabled; crashes: dump file; lag: microprofiler dump; graphics: system information). The skill is built on exactly that list.

## 4. Scaffold, write, check

```
$ my_skill.py new skill my-demo-devforum-bug
created My-Skills/my-demo-devforum-bug/SKILL.md (fill every FILL-IN marker, then run check)
```

Claude filled the template: a 346-character description with the words the user really says, six numbered steps, three rules, the bold footer.

```
$ my_skill.py check My-Skills/my-demo-devforum-bug
PASS name rule: starts with my-, lowercase letters/digits/hyphens, max 64 (my-demo-devforum-bug)
PASS description length 346 <= 400
PASS no template marker left (FILL-IN / TODO / ONE LINE)
PASS bold footer labels **Done** / **You** / **Next** in the body
PASS does not edit vault-owned files
PASS no secrets in the file
PASS description is distinct from the others (closest: rbx-launch-kit, similarity 0.09)
PASS session total ~6504 tokens of the 10000 limit (vault 6412 + your other items 0 + this one 92; every skill/agent adds its listing to EVERY session)
PASS this skill costs ~92 tokens in every session (name + description) and ~680 tokens when it runs
SUMMARY: 18 PASS, 0 WARN, 0 FAIL
```

## 5. Trigger self-test (3 prompts it should match, 2 it should not)

```
PASS should match: 'write a devforum bug report for this studio bug' -> best my-demo-devforum-bug (1.00)
PASS should match: 'clean up this bug description for the forum, here are my output lines' -> best my-demo-devforum-bug (0.86)
PASS should match: 'report this Studio bug on the devforum with repro steps' -> best my-demo-devforum-bug (1.00)
PASS should NOT match: 'find me a game idea for a tycoon' -> best rbx-ideas (0.75); this item 0.00
PASS should NOT match: 'fix my shop screen buttons that overlap on phones' -> best rbx-ui (1.00); this item 0.00
SELF-TEST (word-overlap estimate, not the real model): OK.
```

## 6. Load

```
$ my_skill.py sync
OK 1 of your item is in <vault>/.claude. Skills usually show up at once; if not, type /reload-skills, or start a new Claude session in the vault folder.
```

State afterwards: `My-Skills/my-demo-devforum-bug/SKILL.md` (the source, yours), `.claude/skills/my-demo-devforum-bug/SKILL.md` (the copy sessions read), `git status` of the vault clean (both folders are git-excluded), `rbx-update` and `vault-mode.py load/sync/unload` never write to `My-Skills/`.

## 7. Using it (the sample input below is invented for this demo; it is not a real engine bug)

User: *"ok so my shop button fires twice after you die. like i click Buy once after respawn and get charged twice. ScreenGui has ResetOnSpawn off. Output says Purchase requested: Sword (x2). only in studio i think, happens most times"*

The skill asks once: "Only in Studio, or also in a game joined from the website? And how often: always, about half, rarely?" Answer: *"studio only, about 3 of 4 tries"*. Result:

````
Category: Studio Bugs (only in Studio)

**Title**: TextButton.MouseButton1Click fires twice after respawn when ScreenGui.ResetOnSpawn is false

**Description**
Expected: one click on the Buy button runs the purchase handler once.
Actual: after the character has died and respawned, one click runs the handler twice (the Output line appears twice).

**Where**: UNKNOWN - fill in (place link, or attach the repro place file)
**When**: UNKNOWN - fill in (date, time, timezone it started)

**Reproduction steps**
1. Create a ScreenGui with ResetOnSpawn = false containing a TextButton named Buy.
2. In a LocalScript, connect Buy.MouseButton1Click to a function that prints "Purchase requested: Sword".
3. Press Play in Studio and wait for the character to load.
4. Let the character die (Humanoid.Health = 0) and wait for the respawn.
5. Click Buy once.

**Frequency**: about 75% (3 of 4 tries)

**Environment**: Studio only. Studio version: UNKNOWN. OS: UNKNOWN. Still happens with plugins disabled: UNKNOWN.

**Output**
```
Purchase requested: Sword
Purchase requested: Sword
```

**Workaround**: none given.
````

**Attach before posting**
- [ ] a minimal repro place file (script bug: always include one)
- [ ] a short video of steps 4-5
- [ ] fill the UNKNOWN fields above

Footer the user sees:

**Done** - wrote the report for Studio Bugs from your text; nothing invented.
**You** - fill the 5 UNKNOWN fields and attach the repro place file, then paste it.
**Next** - say "tighten the repro steps" if you want them shorter.

## 8. What the recipe guaranteed

- The skill is yours: `My-Skills/` is never changed by `/rbx-update`, never emptied by sync or unload, rescued by uninstall, git-excluded like `Games/`.
- Cost visible before it was kept: 92 tokens in every session, session total 6,504 of the 10,000 limit.
- Nothing in the vault's own skills was edited. A wish to change one of those is a vault matter (use `/rbx-update`); a `my-` skill of your own is the supported way to get a different behavior.
