---
tags: [roblox-assets, code, library]
---
# Zap (library)

Remote-event code generator with an IDL, strong type safety and tiny payloads

- Path: `~\roblox-assets\code\Zap\`
- Source: https://github.com/red-blox/zap @ `8cd17ab781`
- License: MIT
- Size: 0.6 MB
- Searchable as: networking, remotes

## How it helps
Define remotes in a schema, get typed Luau/TS code; replaces hand-written RemoteEvents.

## How to use
- Wally-compatible libraries: add to `wally.toml` or copy the module folder (usually `src/` or `lib/`) into the project via Rojo.
- Check the license terms (MIT) before shipping; keep the license file with copied code.
- Tools (Rojo, Wally, StyLua, Selene, Lune, luau-lsp, Rokit) are source checkouts; prefer installing releases with Rokit over building them.
