# rbx-subagent-hud

A side pane that shows the master agent (the session you talk to) at the top and the subagents it starts below it, joined by dotted lines. It answers four questions while a request runs: which subagents exist, which are done, what did the master tell each one, and about how long is left. It makes no notifications, plays no sounds and uses no network. It writes one small file, the finished-subagent durations the estimate learns from (see "Time estimate").

## What it shows

Terminal (and any surface without vector drawing):

```
◆ MASTER working 1m02s
1/5 done  3 running  1 failed
~3 min left (estimate)
┊
├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
┊ ✓ 1 Build terrain    ⠴ 2 Write shop UI
┊   general-purpose 2s   general-purpose 1m
├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
┊ ✗ 3 Audit scripts    ⠴ 5 Check lighting
┊   Explore 2s           general-purpose 1m
╰┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
    ⠴ ↳ 4 Place trees
      general-purpose 1m
```

Desktop app, VS Code and mobile draw a vector graph (glowing cyan diamond for the master, one circle per subagent, curved dotted lines) with a list of buttons under it, one per subagent.

- Layout: the master on top, the subagents it started in rows below it (rows wrap to the pane width), a subagent started by a subagent one level lower and indented.
- Lines: grey dotted lines that flash (bright and dim every half second) while the subagent runs; when it finishes the line turns green and stops flashing; red for failed or stopped; dim and steady for queued. Glyphs carry the same meaning without colour: spinner (running), check (done), cross (failed), circle (queued).
- Counter: `2/4 done`, how many run, how many failed, for the current request. A request starts when you send a prompt; the subagents it starts (also background ones that report back in later master turns) count together. A new prompt resets it; a subagent still running from before carries over.
- Click a subagent (its node, its name or its second line) to open a card with the prompt the master sent it, plus description, type, model, status and time. "show more" expands a long prompt, click the subagent again or "x close" dismisses the card, "view transcript" switches the main view to that subagent's transcript.
- Plan line: if the task list or TodoWrite is in use, a compact bar `50% plan 1/2` is kept at the bottom.

## How to open

`/rbx-subagent-hud` toggles the pane (desktop app: it docks beside the chat like the session rail; terminal: docks in fullscreen from 110 columns, else sits above the prompt). Closing it with its own close mark keeps it closed until you run the command again. It also opens by itself on the first of: the Skill tool called with a `game-dev` skill, a prompt starting with `/game-dev`, the first Agent spawn while a `GAME.md` exists.

On a terminal too narrow for a docked pane a one-line fallback above the prompt shows `2/4 done  ~3 min left (estimate)`; `/rbx-subagent-hud` opens the pane at any width (down to 24 columns).

## Time estimate

The line `~N min left (estimate)` is an estimate, not a promise. Method:

1. Every time a subagent finishes, its duration is stored (rolling median over the last 20, kept per `subagent_type` plus the first three words of its description, and per type; at most 40 classes) in the plugin's `$.store` (a JSON file in the Claude config folder, bounded, shared across sessions).
2. For each unfinished subagent the typical time is the median of its class, else of its type, else of all finished subagents (3 or more), else a 2 minute default.
3. Its remaining time is `max(typical - elapsed, 10 s)` (a queued one: the full typical time). Subagents run in parallel, so the master waits for the longest.
4. Plus the master's own wrap-up after the last subagent, the median of past wrap-ups (20 s default).
5. It updates every second and never goes below 0. With no history it reads `estimating... (~2 min, low confidence)`. "low confidence" is also shown when a class has fewer than 2 samples, a subagent has run past its typical time, or no wrap-up is recorded yet. While no subagent is running and the master is thinking only the elapsed time is shown.

## Install and uninstall

The `mods` folder of the kit is a local plugin marketplace (`mods/.claude-plugin/marketplace.json`, name `roblox-vault-kit-mods`).

INSTALL: `claude plugin install rbx-subagent-hud --marketplace <kit>/mods`

INSTALL (two steps): `claude plugin marketplace add <kit>/mods` then `claude plugin install rbx-subagent-hud@roblox-vault-kit-mods`

INSTALL (inside a terminal session): `/plugin install rbx-subagent-hud --marketplace <kit>/mods`

INSTALL (desktop app, where `/plugin` does not run): click + next to the prompt box, then Plugins, Add marketplace with the path `<kit>/mods`, then Add plugin.

UNINSTALL: `claude plugin uninstall rbx-subagent-hud@roblox-vault-kit-mods`

UNINSTALL (also drop the marketplace): `claude plugin marketplace remove roblox-vault-kit-mods`

Replace `<kit>` with the folder the kit is installed in. Run `/reload-plugins` in an open session after installing. This mod replaces the legacy plugins `hud-rbxdev-vault` and `workflow-hud`: `install.sh --with-mods` / `install.ps1 -WithMods` uninstall those and install this one.

## Limits

- Remote Control and mobile views cannot show it. Panes and the above-prompt line are drawn only on the local terminal, desktop app and VS Code; a phone or remote client gets the normal transcript only.
- Only a button can be clicked: on the desktop the graph itself is a picture, so you click the buttons listed under it (numbered like the circles).
- The engine reports an agent only as spawned or ended: start and end times are measured by the HUD (about half a second resolution); an agent that started before the mod loaded shows time from load and has no prompt to show.
- A subagent that is woken again after it finished (SendMessage) stays shown as done.
- The estimate learns from your own runs; the first runs show "estimating...". Durations are kept per machine, not shared.
- The flashing is drawn by redrawing twice a second while something runs; nothing is redrawn while the master and all subagents are idle.
- Kept in memory: the last 60 subagents and the last 50 prompts (20000 characters each, longer ones are cut and marked).
