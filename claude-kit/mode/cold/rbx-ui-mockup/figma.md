<!-- cold: rbx-ui-mockup/figma.md | read when: Figma is connected (use it) or the user asks how to connect Figma or what the connector can do. -->

# Figma (optional, only if the user already has it connected)

Verified 2026-11-05 at Figma's docs. Official setup: https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/ (Claude Code: `claude plugin install figma@claude-plugins-official`, restart, `/plugin`, sign in in the browser with "Allow access"; or `claude mcp add --transport http figma https://mcp.figma.com/mcp`, then `/mcp` > figma > Authenticate). Sign-in is a browser account login; the pages mention no API token.
Can read (help.figma.com Guide to the Figma MCP server): design context from a linked frame or layer (copy the link to the selection), variables, components, layout data, FigJam content.
Can write (same guide): native Figma content back to the canvas (frames, components, variables, auto layout) on the REMOTE server; writing needs a Full seat to write outside your drafts and is free during the beta (it may become usage-based); the desktop server cannot write. Plan and seat rules change: check the page.

## How the UI step uses it (connected)
1. Say "Figma connected" once (the `ui_pref.py figma` line).
2. Read: ask the user for the link to the frame (never guess ids); read its structure and variables through the connector; map names to the brief (frame = screen, layer name = Instance name, variables = palette and fonts).
3. Write (if the connector's write tools are available): create the tokens, the four button states and one frame per screen (phone 844x390, desktop 1920x1080) from the same brief. Figma then holds the design; the spec still comes from the numbers in the brief (and from the local sheet when it renders), so build and compare stay numeric. Read-only otherwise: compare the Figma frame structure against the local sheet and note differences.
4. Gate line mode: `figma`.
The vault never asks for, stores or handles a Figma token, never installs the connector, never enters credentials.
