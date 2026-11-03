---
name: collection-tag-wiring
description: "Drive behaviour from CollectionService tags with one central binder instead of a script in every part: bind existing and future tagged instances, run per-instance setup and cleanup, contain errors. Use for kill bricks, doors, pickups, spawners, prompts and any repeated object."
category: scripting
tags: collectionservice, tags, binder, kill brick, repeated objects, component, getinstanceaddedsignal, cleanup, studio tag editor
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/luau-language-and-types.md
related: proximity-prompt-wiring, connection-leak-auditor, attribute-config-builder, module-architecture-planner, event-bus-builder
---

# collection-tag-wiring

A tag says what an instance is; a binder says what that means. 300 kill bricks become one script: fix it once, it is fixed everywhere. `scripts/TagBinder.luau` gives the lifecycle: bind current instances, bind future ones, clean up when the tag is removed or the instance dies.

## When to use
The same behaviour on many instances, objects created at runtime that need behaviour, or parts that streaming brings and removes. Not for: a unique one-off object (a plain script is clearer), or when per-instance data is large (give the instance a ModuleScript component instead).

## Inputs (max 2)
1. The behaviours (tag name, what happens on setup, what must be cleaned). 2. Per-instance settings (default: Attributes on the instance, see `attribute-config-builder`).

## Procedure
1. Name tags as nouns in constants (`"KillBrick"`, `"Door"`); put them on instances in the Studio Tag Editor or `CollectionService:AddTag` at runtime. Constants avoid typos; an unknown tag does nothing, silently.
2. One binder per system: `local binder = TagBinder.new(game:GetService("CollectionService") :: any, onError)`.
3. `binder:Bind("KillBrick", function(part) local c = part.Touched:Connect(function(hit) ... end); return function() c:Disconnect() end end)`. The behaviour receives the instance and returns a cleanup (a function, or an object with `Destroy` such as a `Janitor`). Existing tagged instances are bound immediately; later ones as they arrive; each instance is bound once per tag.
4. Cleanup runs when the tag is removed from the instance or the instance is removed from the game; `binder:Unbind(tag)` and `binder:Destroy()` run all remaining cleanups. A behaviour that throws is reported through `onError` and does not stop the others.
5. Settings per instance live in Attributes (`part:GetAttribute("Damage")`), read at bind time and via `GetAttributeChangedSignal` if live changes matter.
6. Scope: if you query rather than bind, create queries from a small root, not the whole workspace, and avoid expensive combinators (the vault flags this). Guard tag iteration so a stray tag from a free model cannot break a system (only bind tags you own, ignore unknown ones).
7. Run server-side tags for authoritative behaviour (damage, rewards) and client-side binders for visuals; the same tag can have both, in separate scripts.
8. Streaming: instances can appear and disappear on the client; the added/removed signals handle both, which is why cleanup must be complete.
9. Test: `lune run ../skillpack/scripting/collection-tag-wiring/scripts/tests/TagBinder.test.luau` from the kit `systems` folder.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` / `execute_luau` (Edit) listing `CollectionService:GetTagged("KillBrick")` count -> `multi_edit` the binder script and delete per-part scripts -> `start_stop_play` -> `get_console_output` for bind counts and errors.

## Fallback
Lune tests for the binder with a fake service. Engine signal timing (tag changes during replication or streaming) is `untested` without a place.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: use CollectionService tags and one central script (e.g. 300 killing bricks) so fixing one fixes all; scope CollectionService queries with a small root and avoid expensive combinators; use attributes correctly; debounce Touched. `Roblox/roblox-kb/code-architecture-and-frameworks.md`: drive behaviour from tags, one manager per tag category; guard tag iteration so stray tags cannot break the game.

## Output
`TagBinder.luau`, one behaviour module per tag, the tag list with their attributes, the test result.

## Acceptance checks
- [ ] Executed: Lune test quoted (`6 passed, 0 failed`).
- [ ] No per-instance copies of the same script remain.
- [ ] Every behaviour returns a complete cleanup.
- [ ] Tag names are constants; unknown tags are ignored.
- [ ] Bound count matches `GetTagged` count in play, or marked untested.

## Pitfalls
Binding the same tag from two scripts (the binder refuses a second bind). Forgetting cleanup so removed parts keep connections. Behaviours that yield at setup (they block that instance's setup; spawn the long part). Putting server secrets in attributes on replicated instances.

## Related
`proximity-prompt-wiring`, `connection-leak-auditor`, `attribute-config-builder`, `module-architecture-planner`.
