# MANUAL-READ: the Roblox Dev Mastery Vault in detail

Built and maintained by Roman (GitHub: romangigliotti123-arch)

The short version is in `START-HERE.md`. This is the long one: read only the part you need. Everything below is generated from the real kit (68 skills, 18 agents), so it matches your install.

| Jump to | |
|---|---|
| [1. What the vault is](#1-what-the-vault-is) | [6. The idea flow](#6-the-idea-flow) |
| [2. Install and update](#2-install-and-update) | [7. Building a game](#7-building-a-game) |
| [3. Start a session](#3-start-a-session) | [8. UI mockups and the prototype](#8-ui-mockups-and-the-prototype) |
| [4. Skills by goal](#4-skills-by-goal) | [9. Troubleshooting](#9-troubleshooting) |
| [5. Every skill and agent](#5-every-skill-and-agent) | [10. Uninstall, safety, FAQ, glossary](#10-uninstall) |

## 1. What the vault is

A folder of Roblox research notes plus a Claude kit. Start a Claude session in the folder and Claude has the notes, 68 skills and 18 agents loaded. It does not ask questions it can answer itself: it writes down its assumptions and carries on.

### Where everything lives

| Place | What is there | Who owns it |
|---|---|---|
| Vault folder (default `~/Obsidian/rbx-dev-vault`; an existing `claudes-vault` keeps its name) | EVERYTHING in one folder: the notes, this manual, `START-HERE.md`, update scripts, your games and the kit. Move the folder and `/rbx-update` finds it again | The vault; `/rbx-update` overwrites its own files |
| `<vault>/.claude/` | The skills, agents and rules Claude loads in this folder only | The kit; rewritten on update |
| `<vault>/Games/<game name>/` | Your games, each with a `README.md` to resume from | You; never touched by an update |
| `<vault>/Models/` | Reusable 3D models Claude saved for you | You; never touched by an update |
| `<vault>/My-Skills/` and `<vault>/My-Agents/` | Skills and agents you made with `/rbx-new-skill` (names start with `my-`) | You; never touched by an update |
| `<vault>/Assets/` | Downloaded Roblox assets (models, textures, audio, code) | Downloaded; hidden from git |
| `<vault>/.rbx/claude-kit` | The kit runtime: tools, skills store, systems (hidden from git, inside the vault folder) | The kit; refreshed on update |
| `~/.claude/skills` and `~/.claude/rbx-dev-vault.path` | Only three thin stubs (`/rbx-update`, `/rbx-check`, `/rbx-uninstall`) and a one-line pointer to the vault folder | The kit |
| Your own skills and agents | Your own `~/.claude/skills` and `~/.claude/agents` | You; the vault never overwrites them |

Light mode keeps Obsidian fast by hiding the big folders (Library, Imported, Assets); Claude still searches everything. Details: `LIGHT-MODE.md`.

### What is in the download

| Part | What it is | Files | Size |
|---|---|---:|---:|
| notes | Notes and sources: the sanitised vault (Library, Roblox, Manager, Imported, scripts, the claude-kit/ copy inside the clone) | 8,764 | 87.5 MB |
| kit | Kit folder: skills, agents, tools, mods, setup runbook (installed to ~/.claude/claude-kit) | 1,118 | 8.4 MB |
| refs | Reference images/library: Roblox reference screenshots (installed to ~/.claude/claude-kit/roblox-reference) | 919 | 107.0 MB |
| assets | Assets: 3D models, textures, HDRIs, audio, code libraries, catalog (extracted into Assets/; zip download 1.02 GB) | 31,615 | 1.42 GB |
| &nbsp;&nbsp;vault-assets-01 | 2 zip(s): 3d-models.zip 153.0 MB, textures.zip 733.9 MB | 15,655 | 1.18 GB |
| &nbsp;&nbsp;vault-assets-02 | 4 zip(s): audio.zip 15.1 MB, catalog.zip 76 KB, code.zip 67.8 MB, hdris.zip 47.8 MB | 15,960 | 232.6 MB |
| **TOTAL** | everything the build publishes (notes + kit + refs + extracted assets) | **42,416** | **1.62 GB** |

**Size on your PC after install: 1.85 GB** (notes clone 208.0 MB incl. git data, kit 8.4 MB, reference images 220.6 MB incl. git data, extracted assets 1.42 GB). Peak during the install is 2.87 GB (the asset zips, 1.02 GB, are deleted after extraction). The download is 1.26 GB. `Games/` and `Models/` are yours and add on top.

## 2. Install and update

**Install**: paste the one-line prompt from `START-HERE.md` (or the website) into Claude on the computer you want to set up. Claude fetches the runbook and runs one installer script. The only thing it needs from you is to approve the commands once.

| The install changes | Where |
|---|---|
| Clones the vault | `~/Obsidian/rbx-dev-vault` |
| Installs the kit | `<vault>/.rbx/claude-kit`; `~/.claude/skills` gets only 3 thin stub commands plus one pointer file |
| Writes vault skills and agents | `<vault>/.claude/` (this folder only) |
| Enables the two mods | `<vault>/.claude/settings.json` (this folder only) |
| Downloads assets | `<vault>/Assets/` (checked by sha256) |
| Sets up an update at logon | one scheduled job |

**Update**: type `/rbx-update` in any session. It pulls the latest notes (this manual too), refreshes the kit and the vault folder's skills, and downloads only new or changed assets. If you changed vault files by hand it saves them to a `local-changes-<time>.patch` file first. `/rbx-check` only looks for a newer version and changes nothing. `/rbx-clean` makes the vault an exact copy of the published one (asks once, keeps `Games/` and `My Research`).

**Mods** (`rbx-graph`, `rbx-subagent-hud`): `rbx-subagent-hud` is an agent sidebar and `rbx-graph` shows the vault graph link. They are enabled for the vault folder only. Run `/reload-plugins` once to activate them. Turn off: `/plugin` then disable, or install with `--no-mods` (Windows `-NoMods`).

**Light mode**: `/rbx-light-on` hides Library, Imported and Assets from Obsidian; `/rbx-light-off` shows everything except Assets. Reopen Obsidian after.

**Assets**: the first `/rbx-update` downloads them (see the size table above). If it was cut off, run `/rbx-update` again; it resumes.

## 3. Start a session

Start a new Claude session in the vault folder. Claude app: New, choose the folder. Terminal: `cd` to it, then `claude`. Obsidian: Open folder as vault on the same path. There is no load command and no unload: a session in any other folder loads nothing from the vault.

Type `/rbx-list` to see what is installed, or `/` then `rbx-`.

## 4. Skills by goal

| I want to... | Use |
|---|---|
| get a game idea | `/rbx-ideas` (one fresh idea) or `/rbx-idea-quick` (fast) |
| grow my own idea | `/rbx-idea-creator <your idea>` |
| build a whole game | `/rbx-workflow` |
| continue a game I started | say `I want to work on <game name>` |
| make a shop or menu screen | `/rbx-ui` (design first with `/rbx-ui-mockup`) |
| click through a mockup before building | `/rbx-ui-prototype` |
| make my own skill or agent | `/rbx-new-skill` |
| make my models cheaper without changing how they look | `/rbx-perf-models` (dry run first, then one yes) |
| check my scripts | `/rbx-code-rate`, `/rbx-remote-sec`, `/rbx-datastore` |
| set up prices and passes | `/rbx-monetize`, then `/rbx-monetize-audit` |
| make a thumbnail | `/rbx-thumbnail` |
| plan an update | `/rbx-game-update`, `/rbx-weekly` |
| see what is popular on Roblox | `/rbx-trends` |
| get the latest vault | `/rbx-update` |
| see every skill | `/rbx-list` |

Not sure? Just describe the task in plain words ("I want to make a shop screen"): Claude checks for a fitting skill, asks "Use /rbx-ui for this? (yes/no)" and starts it when you reply yes. If a skill you expect is missing, you are probably not in the vault folder.

## 5. Every skill and agent

68 skills, grouped. Always available everywhere: `/rbx-update`, `/rbx-check`, `/rbx-uninstall`. The rest work in a session started in the vault folder.

### Ideas

Find or sharpen a game idea.

| Skill | What it does |
|---|---|
| `/rbx-ideas` | Claude invents ONE fresh, strange Roblox game idea, single-player or open-world first. |
| `/rbx-idea-creator` | Start from YOUR idea: '/rbx-idea-creator [idea]' sharpens your own game idea through a blind. |
| `/rbx-idea-quick` | A FAST, ~25-line Roblox game idea checked against today's live charts and trackers |
| `/rbx-trends` | Market research on Roblox only: what is popular or trending right now, as a dated. |
| `/rbx-research` | Deep multi-source research: best creators per source. |
| `/rbx-rate` | Rates or compares Roblox game ideas 1.00-10.00 on 12 weighted criteria with cited evidence. |
| `/rbx-rate-any` | General 1.00-10.00 rater for anything else the user wants judged. |
| `/rbx-clarify` | Asks 3-7 multiple-choice questions before building a vague request. |
| `/rbx-gdd` | Fills in a 1-3 page game design document for a Roblox experience from a concept. |

### Build a game (workflow)

Take a game from idea to launch, with the quality gates.

| Skill | What it does |
|---|---|
| `/rbx-workflow` | Flagship Roblox game workflow, the single entry for every game. |
| `/rbx-make` | Vault research, scored GDD, Rojo/Luau project, checks, how to open it in Studio |
| `/rbx-plan` | Turns a rated Roblox idea into game-plan.md: assumptions, systems. |
| `/rbx-art` | Art direction BEFORE anything visual is built: palette, one UI StyleKit, layout rules. |
| `/rbx-placement` | Mandatory placement gate: every model created. |
| `/rbx-lighting` | Mandatory lighting gate: apply the genre lighting preset early, scan the place against 12 checks |
| `/rbx-visual` | Mandatory visual gate and definition of done: screenshots of the running game. |
| `/rbx-critic` | Independent quality gate: a separate critic agent scores 10 factors with evidence and returns GOOD. |
| `/rbx-playtest` | Playtests a Roblox game: bug and feel report with severities; fixes bugs red-first |
| `/rbx-playtest-list` | Checklist and bug-report format for playtesting a Roblox experience |
| `/rbx-harvest` | Saves anything reusable built or found good in a game to Games/_Reusable/[name]/ with a README. |
| `/rbx-tune` | Metric-gated tuning loop: pick ONE number, baseline it, single-change experiments. |
| `/rbx-bench` | Measures whether vault changes make better Roblox games and what load mode costs: scorecard.py. |
| `/rbx-assets` | Given a Roblox dev need, searches the local roblox-assets index: path, license, import steps |

### UI and art

Screens, mockups and thumbnails.

| Skill | What it does |
|---|---|
| `/rbx-ui` | Build Roblox ScreenGui interfaces that scale across phone, tablet, console and PC. |
| `/rbx-ui-mockup` | Design-first Roblox UI: design buttons and screens, export the spec, build, compare |
| `/rbx-mockup` | Toggle manual Nano Banana 2.1 UI mockups: on, off or status |
| `/rbx-ui-prototype` | Turn a UI mockup image into ONE clickable HTML prototype to open in a browser. |
| `/rbx-thumbnail` | Roblox icons and thumbnails built to get clicked: click-psychology rubric score, prompts. |
| `/rbx-thumb-brief` | Sourced packaging brief for a Roblox experience: icon, 3-5 thumbnail concepts. |

### Luau and code

Writing, structuring and reviewing scripts.

| Skill | What it does |
|---|---|
| `/rbx-luau` | Luau coding standard for Roblox scripts: strict typing, services, modules, task library. |
| `/rbx-arch` | Chooses how to structure a Roblox system by evidence: existing code, lifetimes, profiler data |
| `/rbx-code-rate` | Reviews, rates Luau/Roblox code 1.00-10.00 on weighted criteria with file:line evidence. |
| `/rbx-datastore` | Pattern and review checklist for saving player data without loss or duplication. |
| `/rbx-remote-sec` | Server-authoritative design and exploit review for RemoteEvents/RemoteFunctions. |
| `/rbx-npc` | Implement NPCs and enemies with PathfindingService, state machines. |
| `/rbx-rounds` | Architecture for round-based Roblox games with a server state machine, teams, spawning and cleanup |
| `/rbx-leaderboard` | Implement global leaderboards, badges, timed live events and daily rewards safely |
| `/rbx-perf` | Find and fix performance problems in a Roblox experience: frame time, memory. |
| `/rbx-perf-models` | Run inside any game open in Studio: scans every model and part. |
| `/rbx-rojo` | Set up a file-based Roblox project so Luau lives as plain files under version control. |
| `/rbx-studio` | Connects Claude Code to Roblox Studio and the toolchain and says how to use the connection as. |
| `/rbx-karpathy` | Installs and applies four coding-agent rules in a project CLAUDE.md. |

### Money and marketing

Monetisation, ads and launch.

| Skill | What it does |
|---|---|
| `/rbx-monetize` | Set up and review Roblox monetisation: game passes. |
| `/rbx-monetize-audit` | Audits a Roblox game's monetisation against the knowledge-base checklist: scorecard, fixes. |
| `/rbx-ads` | Plans, budgets and explains Roblox sponsored-experience ads for one game, live-checked. |
| `/rbx-launch-kit` | Launch kit at the playtest-to-launch gate: thumbnail/icon brief, title and description. |
| `/rbx-launch-check` | Builds a phone-friendly launch checklist for one Roblox game from the knowledge base. |
| `/rbx-publish` | Checklist for publishing, going live or updating a Roblox experience: settings. |

### Live-ops and numbers

After launch: updates and weekly numbers.

| Skill | What it does |
|---|---|
| `/rbx-game-update` | Plans future updates for a Roblox game: cadence, live-ops loops, retention levers. |
| `/rbx-weekly` | Weekly numbers check for a live Roblox game: the user pastes Creator Dashboard numbers |
| `/rbx-analytics` | Weekly review of a Roblox experience's Creator Dashboard analytics ending in a ranked list of. |
| `/rbx-metrics` | Sourced table of Roblox benchmark numbers with an official/indie flag per row and a comparison. |

### Knowledge and helpers

Look things up, get a co-pilot, manage Claude.

| Skill | What it does |
|---|---|
| `/rbx-kb` | Cheap, cited answers to Roblox game-making questions from the local knowledge base, no agents. |
| `/rbx-use` | How any Claude uses the claudes-vault Obsidian vault: find it, grep first, read small files. |
| `/rbx-ailib` | How any Claude finds and uses a skill. |
| `/rbx-mentor` | Start the vault mentor: a co-pilot with the combined knowledge of every creator in both vaults |
| `/rbx-manager` | Turns this session into a manager that delegates: sizes the job, picks model and effort. |
| `/rbx-low-usage` | Keep Claude in low usage mode for this session and every later one until turned off. |
| `/rbx-new-skill` | Make your own skill or agent for this vault folder: asks the goal in one line. |

### Vault care

Install, update, view mode, uninstall.

| Skill | What it does |
|---|---|
| `/rbx-update` | Update the claudes-vault and the AI Library Vault on demand: self-healing git update. |
| `/rbx-check` | Check whether a newer vault or kit exists, changing nothing: fetches the git remote. |
| `/rbx-clean` | Make this computer's claudes-vault an EXACT copy of the main vault. |
| `/rbx-light-on` | Turn Obsidian light mode ON for the claudes-vault on this computer: hides Imported, Library. |
| `/rbx-light-off` | Turn Obsidian light mode OFF for the claudes-vault on this computer. |
| `/rbx-list` | See everything the kit installed on this computer: skills, agents and mods. |
| `/rbx-setup` | See which software the vault setup needs and what is missing on this computer: git, Python. |
| `/rbx-uninstall` | Remove the whole Roblox Dev Mastery Vault kit from this computer, keeping only the user's games |
| `/rbx` | Router for the Roblox skill pack |


### Agents (18)

Claude hands work to these specialists by itself; you rarely call them. Ask for one by name if you want ("use rbx-reviewer on this script").

| Agent | Role |
|---|---|
| `rbx-auditor` | Orchestrator for a pre-release audit or full bug sweep of a whole Roblox game or Luau codebase. |
| `rbx-builder` | Single entry point for 'make me a Roblox game': takes an idea, researches the vault. |
| `rbx-coach` | The vault mentor: works alongside the user on any job with the combined knowledge of every creator. |
| `rbx-designer` | Roblox game designer: turns a seed idea into a scored concept, core loop. |
| `rbx-doctor` | Roblox game doctor: given analytics numbers or symptoms diagnoses against knowledge-base benchmarks. |
| `rbx-economist` | Designs and balances a Roblox game's economy with a simulation spreadsheet before any code |
| `rbx-engineer` | Roblox Luau engineer: implements gameplay, economy, data. |
| `rbx-idea-judge` | Hidden-rubric player-appeal judge, used only inside the rbx-ideas / rbx-idea-creator loop. |
| `rbx-judge` | Independent critic for a Roblox game idea, prototype, playtest build. |
| `rbx-lead` | Roblox studio lead: router/orchestrator for any Roblox request |
| `rbx-liveops` | Roblox live-ops planner: update cadence, events calendar, seasons. |
| `rbx-marketer` | Roblox launch and marketing manager: thumbnail/icon/title/description brief. |
| `rbx-money` | Roblox monetisation consultant: audits or designs passes, developer products, starter packs. |
| `rbx-predelivery` | Pre-delivery reviewer for Roblox tools. |
| `rbx-reviewer` | Reviews Luau code for exploits, data-loss bugs, leaks, performance and style. |
| `rbx-selfbuilder` | Builds a playable single-file HTML game from one description. |
| `rbx-tester` | Runs a structured Roblox playtest on this computer, finds bugs. |
| `rbx-verifier` | Verifier subagent for research and reverse-engineering findings. |

### Your own skills and agents

`/rbx-new-skill` makes a skill or an agent that is yours: say `make my own skill` and give the goal in one line. Claude checks that no vault skill already does it, writes `My-Skills/my-<name>/SKILL.md` (or `My-Agents/my-<name>.md`), checks it, shows how many tokens it adds to every session (the whole vault session limit is 10,000) and tries three prompts that should use it and two that should not. Your files stay in the vault folder, are hidden from git like `Games/`, and are copied into `.claude` so sessions in the vault see them; updates and uninstall never delete them (uninstall copies them to the keep folder). It never edits the vault's own skills.

## 6. The idea flow

1. `/rbx-ideas` finds ONE fresh idea. A maker invents it without seeing a rubric, a separate judge (`rbx-idea-judge`) says what is good, bad and where a kid would quit, and the maker edits (up to 3 rounds). You get a short card: hook, first 30 seconds, return plan, money, build ease, category.
2. Reply `another` for a different idea, `build it` to create `Games/<game name>/` with a starting README, or `plan` for the full plan.
3. `/rbx-idea-creator <your idea>` runs the same loop starting from your idea. With no idea it asks a few multiple-choice questions.
4. `/rbx-idea-quick` is the fast version for when you want one short idea checked against today's charts.

## 7. Building a game

`/rbx-workflow` is the single entry for every game. It asks for your idea, rates it, writes a build plan, asks "Ready to build?", then acts as a manager that sends specialist workers and checks their reports.

| Stage | What happens |
|---|---|
| Idea | Idea rated 1.00-10.00 and a plan written |
| Prototype | The core loop is built and tested |
| Playtest | Bug and feel report; fixes are verified |
| Launch | Thumbnail, ads, checklist (`/rbx-launch-kit`) |
| Growth and live-ops | Weekly numbers and updates |

**Resume any time**: start a session in the vault folder and say `I want to work on <game name>`. Claude reads `Games/<game name>/README.md` and `GAME.md` and carries on from the real stage.

**Gates**: before a stage advances or a game is called done, `/rbx-critic` scores it (GOOD, NOT YET or BAD). `/rbx-placement` checks every model is measured, grounded and facing the right way. `/rbx-lighting` applies a genre lighting preset. `/rbx-visual` takes screenshots at phone, tablet and desktop size and checks for overlap. A game that fails stays "playable prototype, visuals not polished" with a list of what to polish.

**Models library**: good reusable models are saved to `Models/` by `tools/models.py`, only if they pass strict quality rules. Claude looks there first before building a model.

## 8. UI mockups and the prototype

By default Claude designs every button and screen before building UI (`/rbx-ui-mockup`), exports the exact sizes and colours, builds from them and compares. `/rbx-mockup on` switches to a manual package for making mockups yourself with an image generator; `/rbx-mockup off` returns to automatic.

`/rbx-ui-prototype` turns a mockup picture (or any screenshot in the game folder) into ONE HTML file you open in a browser: working buttons, screen navigation, a phone/tablet/desktop switcher and a note on what Roblox UI cannot build. Say `prototype this mockup`. It is a stand-in, never the game.

## 9. Troubleshooting

| Problem | Fix |
|---|---|
| Claude shows a permission block during install | Approve it once; the installer is one script and needs it |
| Mods not showing | Type `/reload-plugins`, or start a new session in the vault folder |
| Skills missing | You are not in the vault folder. Start a session there |
| Assets incomplete or a download failed | Run `/rbx-update` again; it resumes and checks sha256 |
| Two footers at the end of a reply | A Stop hook of yours prints its own footer; make it print bold `**You**` |
| Update says local changes saved | Your edits are in the `local-changes-<time>.patch` file; the vault was reset to the latest |
| "no asset source reachable" | You are offline; the notes and kit still updated |
| Obsidian is slow | `/rbx-light-on` |

## 10. Uninstall

`/rbx-uninstall` shows a plan first and deletes nothing until you say yes. It copies your `Games/` (and `My Research`, `Models/`, `My-Skills/` and `My-Agents/`) to a safe folder and checks the copy byte for byte, removes the kit, hooks, scheduled job and the vault folder, and removes itself last. The plan it prints is short (the full list is in a file), only kit files you really edited are backed up, and if your Claude session still has the vault folder open the empty folder is deleted automatically a few seconds after you close that session (your games and backups sit next to the vault folder, so deleting it by hand never touches them). Not touched: other skills and agents, credentials, other settings, MCP servers. To reinstall, repeat the install prompt.

### Safety and privacy

- The install writes only the places in the table in section 2. It stores no secrets and asks for none (image generation uses your own key if you add one).
- The mods' hooks run only in the vault folder.
- Updates never edit your `Games/`, `Models/`, `My-Skills/` or `My-Agents/`. Nothing is sent anywhere except git and asset downloads from public GitHub.
- Notes were gathered by AI from public sources; check numbers against the linked source before relying on them.

### FAQ

| Question | Answer |
|---|---|
| Do I need Obsidian? | No. Claude reads the folder directly; Obsidian is only for browsing |
| Does it work on Mac and Linux? | Yes; the installer has a script for each system |
| Can I use it offline? | Yes after the first install; updates and assets need internet |
| Can I add my own skill? | Yes: put it in your own `~/.claude/skills`; the vault never overwrites it |
| What happens when I describe a task? | Claude checks the skills first and asks one line, "Use /rbx-x for this? (yes/no)"; reply yes to start it on your request, no to go on without it. It does not ask for plain questions, small edits or when you name a skill |
| What do the footers mean? | **Done** - what happened, **You** - what you must do, **Next** - the next step |

### Glossary

| Term | Meaning |
|---|---|
| Vault | The folder of notes and the kit |
| Kit | The skills, agents, tools and mods Claude uses |
| Skill | A slash command such as `/rbx-ideas` |
| Agent | A specialist Claude hands work to |
| Gate | A check a game must pass before it counts as done |
| Mod | A Claude Code plugin (sidebar, graph link) |
| Light mode | Obsidian hides the big folders so it stays fast |

**Done** - this manual lists what the install contains. **You** - start a session in the vault folder. **Next** - type `/rbx-ideas`.
