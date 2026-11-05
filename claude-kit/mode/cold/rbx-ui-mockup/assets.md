<!-- cold: rbx-ui-mockup/assets.md | read when: before a UI art file (icon, panel art, background) is made or imported into Roblox. -->

# UI assets

Prefer no uploaded art: Frame + UICorner + UIStroke + UIGradient (StyleKit) covers most UI. Art only for icons and illustrated panels.
Folder (project, not the vault): `ui/{brief.md, brief.json, design/, assets-src/ (source of truth), assets-export/ (what is imported), uploads.json}`; `ui_assets.py layout|name|check|export|record|ref|steps`. File names `<game>_<screen>_<element>[_<state>]_<W>x<H>.png`; sha256 in `uploads.json` so re-runs reuse recorded ids.
9-slice: uniform border, flat or simple gradient fill, trim to the smallest tile; `ScaleType = Slice` and `SliceCenter` (Studio 9-Slice Editor): corners do not scale. Transparent backgrounds: do not install tools; ask the user to cut the background in an editor they own.
Upload is manual (Studio Asset Manager, Bulk Import) or the Open Cloud Assets API run by the user with their own key (`ui_assets.py steps` prints both; the tool never makes a network call). Ask before any upload; ids come only from the user or tool results.
