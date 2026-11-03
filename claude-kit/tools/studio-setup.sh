#!/usr/bin/env bash
# studio-setup.sh: OPT-IN setup so Claude Code can build and test Roblox games (macOS and Linux).
# Nothing here runs by itself; the kit installer never calls it. Every step says what it does and asks first (--yes answers yes).
# Safe to run again: each step checks its state first. Ends with a verification table.
#
#   1. Rokit (toolchain manager)    brew install rokit            (only if `rokit` is missing and Homebrew exists; otherwise a link is printed)
#   2. Tools pinned in systems/rokit.toml: rojo, selene, stylua, luau-lsp, lune     rokit install --no-trust-check (official GitHub releases)
#   3. Rojo Studio plugin           rojo plugin install           (macOS only: Studio does not run on Linux)
#   4. Roblox Studio MCP server     claude mcp add --scope <scope> Roblox_Studio -- /Applications/RobloxStudio.app/Contents/MacOS/StudioMCP
#      The server ships inside Studio (no download, no API key, local stdio). macOS only.
#   5. Verify and print what is left for you to do inside Studio.
#
# Usage: bash studio-setup.sh [--yes] [--dry-run] [--verify-only] [--skip-toolchain] [--skip-mcp] [--with-wally]
#                             [--scope user|project|local] [--project-dir <dir>]
# CLAUDE_CONFIG_DIR is honoured by `claude` itself (use a temp dir to test without touching your real config).
set -u
YES=0; DRY=0; VERIFY=0; SKIPTC=0; SKIPMCP=0; WALLY=0; SCOPE=user; PDIR=""
while [ $# -gt 0 ]; do
  case "$1" in
    --yes|-y) YES=1;; --dry-run) DRY=1;; --verify-only) VERIFY=1;; --skip-toolchain) SKIPTC=1;; --skip-mcp) SKIPMCP=1;;
    --with-wally) WALLY=1;; --scope) shift; SCOPE="${1:-user}";; --project-dir) shift; PDIR="${1:-}";;
    -h|--help) sed -n '2,17p' "$0"; exit 0;;
    *) echo "unknown option: $1"; exit 64;;
  esac; shift
done
case "$SCOPE" in user|project|local) ;; *) echo "--scope must be user, project or local"; exit 64;; esac
HERE="$(cd "$(dirname "$0")" && pwd)"
SYS="$(cd "$HERE/.." && pwd)/systems"
[ -f "$SYS/rokit.toml" ] || SYS="$HERE/roblox-project-template"
OS="$(uname -s)"
STUDIO_MCP="/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP"
export PATH="$HOME/.rokit/bin:$PATH"
have() { command -v "$1" >/dev/null 2>&1; }
ask() {
  [ "$VERIFY" = 1 ] && return 1
  if [ "$DRY" = 1 ]; then echo "  [dry run] would ask: $1"; return 1; fi
  [ "$YES" = 1 ] && return 0
  if [ ! -t 0 ]; then echo "  (not interactive: skipped. Re-run with --yes to allow.)"; return 1; fi
  printf '  %s [y/N] ' "$1"; read -r a; case "$a" in y|Y|yes|YES) return 0;; *) return 1;; esac
}
ROWS=""; BAD=""
row() { ROWS="$ROWS$(printf '%-26s %-14s %s' "$1" "$2" "$3")
"; case "$2" in MISSING|"NOT registered") BAD="$BAD $1";; esac; }

echo "Roblox Studio setup for Claude Code (opt-in). Nothing is changed without your yes."
have claude || echo 'Note: the `claude` command (Claude Code) was not found on PATH; step 4 will be skipped.'

if [ "$SKIPTC" = 0 ]; then
  echo; echo "[1/4] Rokit: the toolchain manager that installs Rojo, Selene, StyLua, luau-lsp and Lune at pinned versions."
  if have rokit; then echo "  already installed."
  elif have brew; then
    ask "Install Rokit with Homebrew (brew install rokit)?" && brew install rokit
  else
    echo "  Homebrew not found. Download Rokit from https://github.com/rojo-rbx/rokit/releases (pick your platform), unpack it, run './rokit self-install', open a new terminal, re-run this script."
  fi

  echo; echo "[2/4] Tools: rojo, selene, stylua, luau-lsp, lune pinned in $SYS/rokit.toml (downloaded from their official GitHub releases)."
  if have rokit; then
    if ask 'Run `rokit install --no-trust-check` for those pinned tools (it trusts exactly the tools listed in that file)?'; then
      (cd "$SYS" && rokit install --no-trust-check)
      if [ "$WALLY" = 1 ] && ask "Also add Wally (Roblox package manager, UpliftGames/wally) globally?"; then rokit add --global UpliftGames/wally; fi
    fi
  else echo "  skipped: Rokit not available."; fi

  echo; echo "[3/4] Rojo plugin: lets Studio receive file changes from 'rojo serve'."
  if [ "$OS" != "Darwin" ]; then echo "  skipped: Roblox Studio runs on Windows and macOS only (on Linux use Rojo for builds/checks: 'rojo build -o game.rbxl')."
  elif have rokit; then
    if [ -f "$HOME/Documents/Roblox/Plugins/RojoManagedPlugin.rbxm" ]; then echo "  plugin file already present."
    elif ask "Install the Rojo plugin into the Studio Plugins folder (rojo plugin install)?"; then (cd "$SYS" && rojo plugin install); fi
  fi
fi

if [ "$SKIPMCP" = 0 ]; then
  echo; echo "[4/4] Studio MCP server: Studio's built-in server that lets Claude read/write scripts, run Luau, start playtests and read Output."
  echo "  It is the official one (create.roblox.com/docs/studio/mcp). Registering adds a config entry only; nothing runs until Studio is open."
  if [ "$OS" != "Darwin" ]; then echo "  skipped: Roblox Studio (and its MCP server) is not available on $OS."
  elif ! have claude; then echo "  skipped: Claude Code not found."
  elif claude mcp get Roblox_Studio >/dev/null 2>&1; then echo "  Roblox_Studio is already registered (leaving it as is)."
  elif ask "Register the Roblox_Studio MCP server with Claude Code (scope: $SCOPE)?"; then
    wd="$PWD"; [ "$SCOPE" = project ] && [ -n "$PDIR" ] && wd="$PDIR"
    (cd "$wd" && claude mcp add --scope "$SCOPE" Roblox_Studio -- "$STUDIO_MCP")
  fi
fi

echo; echo "Verifying..."
for t in rokit rojo selene stylua luau-lsp lune; do
  if have "$t"; then
    v="$(cd "$SYS" && "$t" --version 2>&1 | head -1)"
    case "$v" in *ERROR*|*Failed*) row "$t" MISSING "on PATH but not installed for this folder: run 'rokit install' in $SYS";; *) row "$t" ok "$v";; esac
  else row "$t" MISSING "not on PATH"; fi
done
if have wally; then row wally ok "$(wally --version 2>&1 | head -1)"; else row wally optional "not installed (--with-wally)"; fi
if [ "$OS" = "Darwin" ]; then
  [ -f "$HOME/Documents/Roblox/Plugins/RojoManagedPlugin.rbxm" ] && row "Rojo plugin" ok "Documents/Roblox/Plugins" || row "Rojo plugin" MISSING "run: rojo plugin install"
  [ -x "$STUDIO_MCP" ] && row "Roblox Studio MCP" ok "$STUDIO_MCP" || row "Roblox Studio" MISSING "install from create.roblox.com/landing (you sign in yourself)"
  if have claude; then
    if out="$(claude mcp get Roblox_Studio 2>&1)"; then row "claude mcp Roblox_Studio" ok "$(echo "$out" | grep -E 'Scope|Command' | tr -s ' \n' ' ')"
    else row "claude mcp Roblox_Studio" "NOT registered" "run this script again without --skip-mcp"; fi
  else row claude MISSING "Claude Code not on PATH"; fi
else
  row "Studio / Studio MCP" "n/a" "$OS has no Roblox Studio: Rojo + the checks work, live Studio does not"
fi
printf '%s' "$ROWS"
echo
echo "What is left for you (only you can do these):"
echo '  A. Open Roblox Studio, sign in with your Roblox account, open or create a place.'
echo '  B. Studio: Assistant > ... menu > Manage MCP Servers > turn on "Enable Studio as MCP server" (a green indicator shows connected clients).'
echo '  C. Restart Studio and Claude Code. In Claude Code, /mcp should list Roblox_Studio as connected while Studio is running.'
echo '  D. Only connect clients you trust: an MCP client can read and modify the open place. Keep a backup / version history.'
[ "$DRY" = 1 ] && echo "Dry run: nothing was changed."
if [ -n "$BAD" ]; then echo "Incomplete:$BAD"; exit 2; fi
exit 0
