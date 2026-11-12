# Figma for the design pack

Verified 2026-11-12 at Figma's docs (official, read this date):
- Setup: https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/
- Tools: https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/
- Limits and seats: https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/
- Overview and write-to-canvas: https://developers.figma.com/docs/figma-mcp-server/
Plan and seat rules change: if a call fails, read the pages again before telling the user what is allowed.

## Detect (never assume)
Look in your tool list for any tool whose name contains `figma` (`mcp__figma__*`, `mcp__plugin_figma_*`; ToolSearch "figma" when tools are deferred). `design_gate.py figma <slug> --stage <s> --tools "<names>|none"` decides connected or not and prints the connect prompt once per stage. Pass real names only; none found = `none`.

## Connect (the user runs this; the skill only prints it, never edits settings or MCP config)
Plugin (recommended): `claude plugin install figma@claude-plugins-official`, restart Claude Code if it was running, type `/plugin`, Installed tab, select `figma`, Enter to sign in, click "Allow access", `/plugin` again shows it connected. Organisation blocked plugins: use the manual route.
Manual: `claude mcp add --transport http figma https://mcp.figma.com/mcp` (add `--scope user` for all projects), start a new session, `/mcp`, select figma, Authenticate, "Allow access", `/mcp` again to confirm. Manual setup does not install Figma's skills (they help the write tools; Figma's help centre explains how to add them).
Sign-in is a browser login; no token is ever pasted into the chat.
Seats and limits (as read on the date above): reading needs access to the file; writing to the canvas needs a Full seat (free during the beta, later usage-based), remote server only. Tool calls per seat: Professional Full/Dev 200 per day and 10 per minute, Organization 200 per day and 15 per minute, Enterprise 600 per day and 20 per minute, View/Collab 20 per month, Starter Full/Dev: no allowance listed. Some write tools do not count (create_new_file, generate_figma_design and others the page lists). Keep calls few: batch frames, read with `get_metadata` before `get_design_context`.

## What the connector gives the design pack
Read: `get_design_context` (frame to context and code), `get_screenshot` (see a frame), `get_metadata` (outline), `get_variable_defs` (colours, fonts, tokens), `get_figjam` (read a board), `get_motion_context` (keyframes and easing of animated nodes), `search_design_system`. Needs a link to the frame or selection: ask the user to copy the link, never guess ids.
Write (remote server): `use_figma` (create and edit frames, components, variables, auto layout in Design, FigJam, Slides), `generate_diagram` (FigJam diagram or flow from text or Mermaid: map flow, screen flow, cutscene storyboard), `create_new_file` (a blank Design or FigJam file), `generate_image` (places an image; uses Figma AI credits), `upload_assets`, `html_to_figma` (turn an HTML sheet from the fallback route into editable layers), `add_code_connect_map` (map Figma components to code). Roblox UI is built in Luau, so Code Connect is optional.
Use: part files store the Figma link and a screenshot path per frame; the user's edits in Figma are read back (`get_design_context`) before the part is approved.

## Frame conventions for Roblox (file per game, one page per part)
Pages: `00 refs`, `01 style`, `02 ui`, `03 map`, `04 plan`, `05 extras`.
Frame names: `<screen>/<device>/<version>`, e.g. `Shop/Phone-780x360/v2`, `HUD/Phone-844x390/v1`.
Phone landscape first, always, in this order: 780x360, 844x390, 667x375; then tablet 1180x820 and desktop 1920x1080. Portrait only if the game supports it.
Safe areas (KB `ui-ux-design.md`: the top 36 px topbar inset is reserved; `ScreenInsets` DeviceSafeInsets tucks the HUD to the device edge, CoreUISafeInsets leaves a gap): draw a locked grey "core UI" strip 36 px high across the top of every phone frame and a side guide where device cutouts sit (check the real value in Studio's Device Emulator), and place nothing under them. Bottom-left and bottom-right stay free for the thumbstick and jump button (keep custom UI about 60 px in, the `rbx-art` rule). Text 14 px or larger at phone size, contrast 4.5:1 or better.
Tokens as Figma variables: `color/bg`, `color/panel`, `color/accent`, `color/text`, `radius/panel`, `stroke/panel`, fonts (real Roblox font names, `rbx-ui` lists them). Components: Button (default, hover, pressed, disabled), Panel, Chip, Bar, Toast. Auto layout everywhere so frames resize.
Map frames: one frame, 1 grid cell = 10 studs, labelled in studs; zones as coloured rectangles, flow as arrows, landmarks as numbered pins, legend frame beside it.
Versions: `v1`, `v2`, `v3`; the picked one gets a green `PICKED` sticker and the others stay for reference.

## No Figma (fallback, same method, same approval)
UI: `rbx-ui-prototype` (clickable HTML) or the `rbx-ui-mockup` sheet. Map and boards: one SVG or HTML sheet in `Games/<slug>/design-pack/` with the same grid and legend. Style test: Blender or Studio renders. Re-offer Figma once at the next stage, not inside the stage.
