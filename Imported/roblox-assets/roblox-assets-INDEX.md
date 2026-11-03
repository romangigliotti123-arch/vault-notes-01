# roblox-assets INDEX

Generated 2026-10-29 by claude-host\tools\build-assets-catalog.py. Root: ~\roblox-assets\ (total 2.17 GB).
Every pack has SOURCE.md or LICENSE inside and a catalog note in `catalog\`. Search the last column for tag words.


## Code libraries and tools

| Name | What | License | Size | Path / URL | How it helps / import | Tags |
|---|---|---|---|---|---|---|
| ByteNet | Buffer-based networking library with typed packets and namespaces | MIT | 0.2 MB | `code\ByteNet` | Cuts remote bandwidth for fast games (shooters, big servers). | networking, remotes, buffers |
| Charm | Atomic state management (roblox-ts / Luau) | MIT | 0.6 MB | `code\Charm` | Sync state client/server with a small footprint. | state management, sync |
| Cmdr | In-game command console with typed arguments | MIT | 2.0 MB | `code\Cmdr` | Admin commands and debug tools for testing without custom UI. | admin commands, console, debug |
| Flamework | roblox-ts game framework with decorators and dependency injection | MIT | 0.2 MB | `code\Flamework` | Type-safe structure if you write TypeScript for Roblox. | framework, roblox-ts |
| Fusion | Reactive UI library (state, computed, observers, tweens) | MIT | 19.4 MB | `code\Fusion` | Declarative UI without a heavy framework; strong docs and examples. | ui framework, reactive ui |
| GoodSignal | Fast Signal class with RBXScriptSignal parity (Stravant) | MIT | 0.0 MB | `code\GoodSignal` | Use for custom events inside modules. | signal, events |
| Janitor | Cleanup/Maid-style object (disconnect connections, destroy instances) | MIT | 0.3 MB | `code\Janitor` | Prevents memory leaks from forgotten connections. | maid, cleanup, trove |
| Knit | Lightweight service/controller framework (archived, still widely used) | MIT | 1.2 MB | `code\Knit` | Structure server and client code into services and controllers with remote calls; read it to learn the pattern. | game framework, services, architecture |
| Lapis | DataStore abstraction with typed documents and migrations | MIT | 0.1 MB | `code\Lapis` | Lightweight document-style persistence. | datastore wrapper |
| Luau | The Luau language implementation (VM, analyzer, docs) | MIT | 18.8 MB | `code\Luau` | Reference for language features, type system and performance. | luau language, type checker |
| Lune | Standalone Luau runtime for scripts outside Roblox | MPL-2.0 | 2.0 MB | `code\Lune` | Run build scripts, tests and tooling in Luau on the PC. | scripting tools, runtime, build scripts |
| Lyra | Player data management with schema validation, migrations and transactions | MIT | 0.5 MB | `code\Lyra` | Safer alternative to raw DataStore for games with trades or purchases. | datastore, player data, transactions |
| Nevermore | Quenty's huge modular engine: many small packages (UI, binders, cameras, rx) | MIT | 16.8 MB | `code\Nevermore` | Mine it for well-tested modules such as Binder, Maid, Rx, camera stack, ragdoll, Spring. | binder, maid, rx, camera, ragdoll, utilities |
| ProfileService | Older session-locked DataStore library | Apache-2.0 | 0.4 MB | `code\ProfileService` | Same job as ProfileStore; many tutorials and games still use it. | datastore wrapper, player data |
| ProfileStore | Session-locked DataStore saving (successor to ProfileService) | Apache-2.0 | 0.2 MB | `code\ProfileStore` | Player data: load/save a profile table per player with session locking; the standard choice for inventories, currencies and progress. | datastore wrapper, player data, saving |
| Promise | Promise implementation (evaera) | MIT | 0.1 MB | `code\Promise` | Async flow control for Roblox yields; many libraries depend on it. | promise, async |
| RbxUtil | Sleitnick's utility modules: Signal, Trove, TableUtil, Comm, Timer, Input, Spring, Shake and more | MIT | 0.6 MB | `code\RbxUtil` | Drop-in building blocks for almost every game (events, cleanup, tables, input, camera shake). | signal, trove, utilities, camera shake, input |
| Rojo | Sync Roblox projects with the file system and Git | MPL-2.0 | 6.0 MB | `code\Rojo` | Edit scripts in VS Code, use Git; the basis of a professional workflow. | rojo, vscode, git workflow |
| Rokit | Toolchain manager (Rojo, Wally, StyLua, Selene, Lune) | MIT | 0.4 MB | `code\Rokit` | One command installs pinned tool versions per project. | toolchain, tools install |
| Selene | Lua/Luau linter with a Roblox standard library | MPL-2.0 | 1.1 MB | `code\Selene` | Catches bugs early in CI or the editor. | linter |
| StyLua | Opinionated Lua/Luau formatter | MPL-2.0 | 1.8 MB | `code\StyLua` | Consistent code style. | formatter |
| Vide | Reactive Luau UI library, lighter than Fusion | MIT | 0.2 MB | `code\Vide` | Fast fine-grained reactivity for UI. | ui framework, reactive ui |
| Wally | Package manager for Roblox (wally.toml) | MPL-2.0 | 1.1 MB | `code\Wally` | Installs libraries from the Wally registry into a Packages folder. | package manager, dependencies |
| Zap | Remote-event code generator with an IDL, strong type safety and tiny payloads | MIT | 0.6 MB | `code\Zap` | Define remotes in a schema, get typed Luau/TS code; replaces hand-written RemoteEvents. | networking, remotes |
| ZonePlus | Zone detection (players/parts entering regions) | MIT | 0.1 MB | `code\ZonePlus` | Trigger areas, shops, safe zones without per-frame loops. | zones, regions, triggers |
| game-bocchi-upgrade-tree | Upgrade-tree incremental game | MIT | 1.5 MB | `code\game-bocchi-upgrade-tree` | Example of incremental progression systems. | incremental, upgrade tree example |
| game-factorial-defence | Tycoon / defence game | MIT | 0.9 MB | `code\game-factorial-defence` | Example tycoon structure. | tycoon example |
| game-rice-simulator | Small simulator side project | Apache-2.0 | 0.2 MB | `code\game-rice-simulator` | Beginner simulator layout. | simulator example |
| game-simple-roblox-game | Starter project with modular server architecture | MIT | 4.0 MB | `code\game-simple-roblox-game` | Template layout to fork for a new game. | game template, starter |
| game-slither | Open-source roblox-ts game using Charm, React and Flamework | MIT | 6.3 MB | `code\game-slither` | Real example of a polished small multiplayer game architecture. | open source game example, roblox-ts |
| game-ts-halloween-simulator | Roblox TypeScript simulator learning project (CC0) | CC0-1.0 | 2.4 MB | `code\game-ts-halloween-simulator` | Small simulator loop example in roblox-ts. | simulator example |
| jecs | Fast archetype ECS for Luau | MIT | 1.9 MB | `code\jecs` | Modern high-performance ECS with relationships. | ecs, entity component system, performance |
| jest-lua | Jest-style test runner for Luau | MIT | 3.6 MB | `code\jest-lua` | Unit tests for modules; run in Studio or via Lune. | testing, unit tests |
| luau-lsp | Language server for Luau (autocomplete, type checking, Rojo aware) | MIT | 18.0 MB | `code\luau-lsp` | Full IDE support in VS Code. | language server, vscode, autocomplete |
| matter | ECS library with hot reloading and debugger | MIT | 0.5 MB | `code\matter` | Entity-component-system for large simulations (many NPCs, projectiles). | ecs, entity component system |
| open-game-eval | Roblox's open evaluation framework for AI agents making Roblox games | MIT | 23.3 MB | `code\open-game-eval` | Benchmark/test AI coding agents on Studio tasks. | ai eval, agents, benchmark |
| rbx-dom | Rust library and reflection data for the Roblox DOM and file formats | MIT | 14.2 MB | `code\rbx-dom` | Build tools that read/write rbxl/rbxm files and the API dump. | file format, tooling |
| react-lua | Roblox's port of React 17 plus ReactRoblox (Roact successor) | MIT | 5.9 MB | `code\react-lua` | Component-based UI as used in Roblox's own tools; hooks supported. | ui framework, react |
| roblox-ts | TypeScript to Luau compiler | MIT | 1.7 MB | `code\roblox-ts` | Write Roblox games in TypeScript with full typing. | typescript, compiler |
| studio-rust-mcp-server | Official Roblox Studio MCP server (standalone) | MIT | 0.2 MB | `code\studio-rust-mcp-server` | Lets Claude/other MCP clients inspect and edit an open Studio place. | mcp, studio, ai tool |
| t | Runtime type checker for Roblox/Luau values | MIT | 0.1 MB | `code\t` | Validate RemoteEvent payloads and function arguments (anti-exploit hygiene). | type check, validation, remote security |

## 3D models

| Name | What | License | Size | Path / URL | How it helps / import | Tags |
|---|---|---|---|---|---|---|
| kenney-3d-road-tiles | Download this package (300 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 6.6 MB | `3d-models\kenney-3d-road-tiles` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-animated-characters-retro | Download this package (8 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 2.2 MB | `3d-models\kenney-animated-characters-retro` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-animated-characters-survivors | Download this package (8 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 2.3 MB | `3d-models\kenney-animated-characters-survivors` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-blaster-kit | Download this package (40 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 4.3 MB | `3d-models\kenney-blaster-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-blocky-characters | Download this package (20 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 12.3 MB | `3d-models\kenney-blocky-characters` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-brick-kit | Download this package (290 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 14.6 MB | `3d-models\kenney-brick-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-building-kit | Download this package (80 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 4.3 MB | `3d-models\kenney-building-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-car-kit | Download this package (45 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 13.8 MB | `3d-models\kenney-car-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-castle-kit | Download this package (75 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 6.5 MB | `3d-models\kenney-castle-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-city-kit-commercial | Download this package (50 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 10.7 MB | `3d-models\kenney-city-kit-commercial` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-city-kit-industrial | Download this package (40 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 10.5 MB | `3d-models\kenney-city-kit-industrial` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-city-kit-roads | Download this package (90 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 6.7 MB | `3d-models\kenney-city-kit-roads` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-city-kit-suburban | Download this package (40 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 7.7 MB | `3d-models\kenney-city-kit-suburban` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-coaster-kit | Download this package (180 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 19.9 MB | `3d-models\kenney-coaster-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-cube-pets | Download this package (24 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 14.3 MB | `3d-models\kenney-cube-pets` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-factory-kit | Download this package (140 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 11.6 MB | `3d-models\kenney-factory-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-fantasy-town-kit | Download this package (160 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 10.2 MB | `3d-models\kenney-fantasy-town-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-food-kit | Download this package (200 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 13.0 MB | `3d-models\kenney-food-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-furniture-kit | Download this package (140 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 16.9 MB | `3d-models\kenney-furniture-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-graveyard-kit | Download this package (90 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 12.0 MB | `3d-models\kenney-graveyard-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-hexagon-kit | Download this package (70 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 6.1 MB | `3d-models\kenney-hexagon-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-holiday-kit | Download this package (100 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 10.1 MB | `3d-models\kenney-holiday-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-marble-kit | Download this package (160 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 12.4 MB | `3d-models\kenney-marble-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-mini-arcade | Download this package (20 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 4.1 MB | `3d-models\kenney-mini-arcade` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-mini-arena | Download this package (20 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 2.1 MB | `3d-models\kenney-mini-arena` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-mini-characters | Download this package (25 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 13.2 MB | `3d-models\kenney-mini-characters` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-mini-dungeon | Download this package (30 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 4.5 MB | `3d-models\kenney-mini-dungeon` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-mini-forest | Download this package (20 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 3.1 MB | `3d-models\kenney-mini-forest` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-mini-market | Download this package (20 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 3.2 MB | `3d-models\kenney-mini-market` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-mini-skate | Download this package (40 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 5.6 MB | `3d-models\kenney-mini-skate` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-minigolf-kit | Download this package (125 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 8.0 MB | `3d-models\kenney-minigolf-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-modular-buildings | Download this package (100 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 4.7 MB | `3d-models\kenney-modular-buildings` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-modular-cave-kit | Download this package (40 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 16.7 MB | `3d-models\kenney-modular-cave-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-modular-dungeon-kit | Download this package (40 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 18.7 MB | `3d-models\kenney-modular-dungeon-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-modular-space-kit | Download this package (40 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 20.1 MB | `3d-models\kenney-modular-space-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-nature-kit | Download this package (330 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 28.1 MB | `3d-models\kenney-nature-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-pirate-kit | Download this package (70 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 8.9 MB | `3d-models\kenney-pirate-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-platformer-kit | Download this package (150 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 13.0 MB | `3d-models\kenney-platformer-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-prototype-kit | Download this package (145 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 9.9 MB | `3d-models\kenney-prototype-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-racing-kit | Download this package (110 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 17.4 MB | `3d-models\kenney-racing-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-retro-fantasy-kit | Download this package (100 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 5.3 MB | `3d-models\kenney-retro-fantasy-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-retro-urban-kit | Download this package (120 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 5.2 MB | `3d-models\kenney-retro-urban-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-space-kit | Download this package (150 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 18.0 MB | `3d-models\kenney-space-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-space-station-kit | Download this package (90 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 5.0 MB | `3d-models\kenney-space-station-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-survival-kit | Download this package (80 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 5.0 MB | `3d-models\kenney-survival-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-tower-defense-kit | Download this package (160 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 15.9 MB | `3d-models\kenney-tower-defense-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-toy-car-kit | Download this package (100 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 13.7 MB | `3d-models\kenney-toy-car-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-train-kit | Download this package (100 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 17.7 MB | `3d-models\kenney-train-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| kenney-watercraft-kit | Download this package (45 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 5.6 MB | `3d-models\kenney-watercraft-kit` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |
| quaternius-stylized-nature | Quaternius Ultimate Stylized Nature low-poly trees, rocks, plants (FBX). Original Drive downloads from quaternius.com were rate-limited, so  | repo MIT; models by Quaternius, published CC0 1.0 at https://quaternius.com | 237.3 MB | `3d-models\quaternius-stylized-nature` | Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the  | 3d-models |

## Textures

| Name | What | License | Size | Path / URL | How it helps / import | Tags |
|---|---|---|---|---|---|---|
| ambientcg-materials-1k | ambientcg-materials-1k: 150 CC0 items | CC0 1.0 (public domain) | 1007.1 MB | `textures\ambientcg-materials-1k` | Create a SurfaceAppearance on a MeshPart (or a MaterialVariant in MaterialService): ColorMap from *_Color/*_diff | textures |
| polyhaven-textures-1k | polyhaven-textures-1k: 100 CC0 items | CC0 1.0 (public domain) | 243.4 MB | `textures\polyhaven-textures-1k` | Create a SurfaceAppearance on a MeshPart (or a MaterialVariant in MaterialService): ColorMap from *_Color/*_diff | textures |

## HDRIs

| Name | What | License | Size | Path / URL | How it helps / import | Tags |
|---|---|---|---|---|---|---|
| polyhaven-hdris-1k | polyhaven-hdris-1k: 40 CC0 items | CC0 1.0 (public domain) | 59.7 MB | `hdris\polyhaven-hdris-1k` | Roblox cannot import HDRI directly: convert the  | hdris |

## Audio

| Name | What | License | Size | Path / URL | How it helps / import | Tags |
|---|---|---|---|---|---|---|
| kenney-casino-audio | Download this package (50 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 0.9 MB | `audio\kenney-casino-audio` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-digital-audio | Download this package (60 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 1.0 MB | `audio\kenney-digital-audio` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-impact-sounds | Download this package (130 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 1.0 MB | `audio\kenney-impact-sounds` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-interface-sounds | Download this package (100 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 0.9 MB | `audio\kenney-interface-sounds` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-music-jingles | Download this package (85 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 1.4 MB | `audio\kenney-music-jingles` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-rpg-audio | Download this package (50 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 1.0 MB | `audio\kenney-rpg-audio` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-sci-fi-sounds | Download this package (70 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 5.7 MB | `audio\kenney-sci-fi-sounds` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-ui-audio | Download this package (50 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 0.5 MB | `audio\kenney-ui-audio` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-voiceover-pack | Download this package (90 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 1.9 MB | `audio\kenney-voiceover-pack` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |
| kenney-voiceover-pack-fighter | Download this package (45 assets) for free, CC0 licensed! | CC0 1.0 (public domain; see License.txt inside if present) | 1.2 MB | `audio\kenney-voiceover-pack-fighter` | Studio > View > Asset Manager > Audio > Bulk Import the  | audio |

## References (not downloaded)

| Name | What | License | Size | Path / URL | How it helps / import | Tags |
|---|---|---|---|---|---|---|
| Roblox Cube (cube3d) foundation model for 3D generation | Roblox's open 3D foundation model: text-to-3D shape generation and cubepart; weights on Hugging Face (not downloaded, large). | OpenRAIL (weights), repo license NOASSERTION - check before use | - | https://github.com/Roblox/cube / https://huggingface.co/Roblox/cube3d-v0.5 | Prototype meshes from text prompts for blockouts; needs a GPU (Roman's CachyOS PC) - run there, never on the always-on Windows PC. | ai |
| Roblox/luau_corpus dataset | Official Luau code corpus released by Roblox. | MIT | - | https://huggingface.co/datasets/Roblox/luau_corpus | Fine-tuning or retrieval source for Luau-aware assistants; also useful as a large snippet reference. | ai |
| TorpedoSoftware/Roblox-Luau-Reasoning-v1.0 dataset | Reasoning-style Roblox/Luau training dataset. | MIT | - | https://huggingface.co/datasets/TorpedoSoftware/Roblox-Luau-Reasoning-v1.0 | Training/eval data for Luau coding models. | ai |
| TorpedoSoftware/RobloxQA-v2.0 dataset | Question-answer pairs about Roblox development. | MIT | - | https://huggingface.co/datasets/TorpedoSoftware/RobloxQA-v2.0 | Evaluate how well an agent knows Roblox APIs. | ai |
| TorpedoSoftware/Luau-Devstral-24B-Instruct-v0.2 | 24B Luau-tuned coding model (GGUF quants by mradermacher). Large; not downloaded. | Apache-2.0 | - | https://huggingface.co/TorpedoSoftware/Luau-Devstral-24B-Instruct-v0.2 | Local Luau code model option on Roman's CachyOS GPU PC. | ai |
| TorpedoSoftware/Luau-Qwen3-4B-FIM-v0.1 | 4B fill-in-the-middle Luau completion model. | Apache-2.0 | - | https://huggingface.co/TorpedoSoftware/Luau-Qwen3-4B-FIM-v0.1 | Tiny local autocomplete for Luau; fits a modest GPU. | ai |
| preferedev/Roblox-Coder-v2_gguf | Community Roblox coding model in GGUF. | MIT | - | https://huggingface.co/preferedev/Roblox-Coder-v2_gguf | Quick local experiments; quality unverified. | ai |
| Roblox/roblox-pii-classifier-v2 | Open classifier that detects personal information in chat text. | Apache-2.0 | - | https://huggingface.co/Roblox/roblox-pii-classifier-v2 | Chat-safety filter for experiences with custom text input. | ai |
| Roblox/voice-safety-classifier-v3 | Open voice-chat toxicity classifier. | Apache-2.0 | - | https://huggingface.co/Roblox/voice-safety-classifier-v3 | Moderation research reference. | ai |
| Roblox open-game-eval (cloned in code/) | Evaluation harness for AI agents building Roblox games; cloned under code/open-game-eval. | MIT | - | https://github.com/Roblox/open-game-eval | Measure whether Claude agents + MCP actually build working Studio features. | ai |
| Roblox Studio built-in MCP server and Assistant | Studio ships an MCP server so external agents can drive Studio; standalone Rust version cloned under code/studio-rust-mcp-server. | Roblox ToS | - | https://create.roblox.com/docs/studio/mcp | Connect Claude Code to a live place for script edits and playtests. | ai |
| Kenney Game Assets All-in-1 | Every Kenney pack in one bundle ($ donation); individual packs are free and already downloaded. | CC0 (paid bundle) | - | https://kenney.itch.io/kenney-game-assets | Only worth buying to support Kenney; needs Roman's approval to spend. | asset |
| Poly Pizza low-poly models | Searchable library of low-poly models (Quaternius and others), per-model license; download needs a click per model. | CC0 and CC-BY per model | - | https://poly.pizza | Single props not covered by the packs; check each model's license field. | asset |
| OpenGameArt.org | Large community art and audio repository filterable by license. | CC0 / CC-BY / GPL per item | - | https://opengameart.org | Sound effects, music and 2D art; filter CC0 only. | asset |
| Freesound CC0 sounds | Huge sound-effect library; API key and login needed for bulk download. | CC0 filter | - | https://freesound.org/search/?f=license%3A%22Creative+Commons+0%22 | Fills SFX gaps; Roman must make a free API key for bulk fetch. | asset |
| Sonniss GDC Game Audio bundles | Yearly free bundles of professional SFX, 7-30 GB each. | Royalty-free custom license (not CC0) | - | https://sonniss.com/gameaudiogdc | Excellent SFX but license forbids redistribution; check terms and size budget before downloading. | asset |
| Roblox Creator Store (Toolbox) free models and audio | Official marketplace; free assets usable directly in Studio without import. | Roblox ToS | - | https://create.roblox.com/store | Fastest way to place models and audio; vet scripts inside models for malware. | asset |
| Roblox 3D Importer docs (in creator-docs vault) | Official guide for FBX/OBJ/glTF import, scale, materials and collision. Mirrored in Imported/roblox-creator-docs. | CC-BY-4.0 | - | https://create.roblox.com/docs/art/modeling/3d-importer | Use for every pack import in INDEX.md. | doc |

## Import cheat sheet

- **3d-models**: Studio > Home > Import 3D (or Asset Manager > Bulk Import), pick the .fbx/.obj/.glb from the pack's FBX/OBJ/GLB folder. Kenney packs share one colormap texture: keep it next to the mesh so the importer links it, or apply it as a SurfaceAppearance/TextureID. Kenney units are metres: set import scale about 3.5 (1 stud = 0.28 m) so a person is about 5 studs tall.
- **audio**: Studio > View > Asset Manager > Audio > Bulk Import the .ogg/.wav files (Roblox moderation applies, and audio upload needs ID verification), then reference the rbxassetid in a Sound.
- **textures**: Create a SurfaceAppearance on a MeshPart (or a MaterialVariant in MaterialService): ColorMap from *_Color/*_diff.jpg, NormalMap from *_Normal*/nor_gl, RoughnessMap from *_Roughness/rough. Bulk Import the images first. Keep maps at 1K.
- **hdris**: Roblox cannot import HDRI directly: convert the .hdr to six cube faces with a free cubemap tool, upload the faces and assign them to a Sky object (SkyboxBk/Dn/Ft/Lf/Rt/Up). Also useful as lighting reference.
