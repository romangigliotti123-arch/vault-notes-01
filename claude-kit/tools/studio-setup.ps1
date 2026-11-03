# studio-setup.ps1: OPT-IN setup so Claude Code can build and test Roblox games (Windows, PowerShell 5.1+).
# Nothing here runs by itself; the kit installer never calls it. Every step says what it does and asks first (-Yes answers yes to all).
# Safe to run again: each step checks its state first. Ends with a verification table.
#
#   1. Rokit (toolchain manager)   winget install Rojo.Rokit                       (only if `rokit` is missing)
#   2. Tools pinned in systems\rokit.toml: rojo, selene, stylua, luau-lsp, lune     rokit install (official GitHub releases)
#      (+ wally with -WithWally)
#   3. Rojo Studio plugin           rojo plugin install                             (writes RojoManagedPlugin.rbxm to the Studio Plugins folder)
#   4. Roblox Studio MCP server     claude mcp add --scope <Scope> Roblox_Studio -- cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat
#      The server ships inside Studio (no download, no API key, local stdio). Registering only tells Claude Code how to start it.
#   5. Verify and print what is left for you to do inside Studio.
#
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File studio-setup.ps1 [-Yes] [-DryRun] [-VerifyOnly]
#        [-SkipToolchain] [-SkipMcp] [-WithWally] [-Scope user|project|local] [-ProjectDir <dir for project scope>]
# Environment: CLAUDE_CONFIG_DIR is honoured by `claude` itself (use a temp dir to test without touching your real config).
param(
  [switch]$Yes, [switch]$DryRun, [switch]$VerifyOnly, [switch]$SkipToolchain, [switch]$SkipMcp, [switch]$WithWally,
  [ValidateSet('user', 'project', 'local')][string]$Scope = 'user',
  [string]$ProjectDir = ''
)
$ErrorActionPreference = 'Continue'
$Systems = Join-Path (Split-Path -Parent $PSScriptRoot) 'systems'
if (-not (Test-Path -LiteralPath (Join-Path $Systems 'rokit.toml'))) { $Systems = Join-Path (Split-Path -Parent $PSScriptRoot) 'tools\roblox-project-template' }
$Results = New-Object System.Collections.Generic.List[object]
function Add-Result([string]$Name, [string]$Status, [string]$Detail) { $Results.Add([pscustomobject]@{ Check = $Name; Status = $Status; Detail = $Detail }) }
function Has([string]$cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function Say([string]$m) { Write-Host $m }
function Ask([string]$what) {
  if ($VerifyOnly) { return $false }
  if ($DryRun) { Say "  [dry run] would ask: $what"; return $false }
  if ($Yes) { return $true }
  if ([Console]::IsInputRedirected) { Say "  (not interactive: skipped. Re-run with -Yes to allow.)"; return $false }
  $a = Read-Host "  $what [y/N]"
  return ($a -match '^(y|yes)$')
}
function Add-RokitToPath {
  $b = Join-Path $env:USERPROFILE '.rokit\bin'
  if ((Test-Path -LiteralPath $b) -and ($env:PATH -notlike "*$b*")) { $env:PATH = "$b;$env:PATH" }
}
Add-RokitToPath

Say 'Roblox Studio setup for Claude Code (opt-in). Nothing is changed without your yes.'
if (-not (Has 'claude')) { Say 'Note: the `claude` command (Claude Code) was not found on PATH; step 4 will be skipped.' }

# ---- 1 + 2 + 3 toolchain
if (-not $SkipToolchain) {
  Say "`n[1/4] Rokit: the toolchain manager that installs Rojo, Selene, StyLua, luau-lsp and Lune at pinned versions."
  if (Has 'rokit') { Say '  already installed.' }
  elseif (Ask 'Install Rokit with winget (package Rojo.Rokit, official)?') {
    if (Has 'winget') { winget install --id Rojo.Rokit -e --accept-source-agreements --accept-package-agreements; Add-RokitToPath }
    else { Say '  winget not found. Install Rokit from https://github.com/rojo-rbx/rokit/releases (rokit.exe self-install), then re-run.' }
  }

  Say "`n[2/4] Tools: rojo, selene, stylua, luau-lsp, lune pinned in $Systems\rokit.toml (downloaded from their official GitHub releases)."
  if (Has 'rokit') {
    if (Ask 'Run `rokit install --no-trust-check` for those pinned tools (it trusts exactly the tools listed in that file)?') {
      Push-Location $Systems
      try { rokit install --no-trust-check } finally { Pop-Location }
      if ($WithWally) {
        if (Ask 'Also add Wally (Roblox package manager, UpliftGames/wally) globally?') { rokit add --global UpliftGames/wally }
      }
    }
  } else { Say '  skipped: Rokit not available.' }

  Say "`n[3/4] Rojo plugin: lets Studio receive file changes from 'rojo serve'."
  if (Has 'rokit') {
    Push-Location $Systems
    $have = Test-Path -LiteralPath (Join-Path $env:LOCALAPPDATA 'Roblox\Plugins\RojoManagedPlugin.rbxm')
    if ($have) { Say '  plugin file already present.' }
    elseif (Ask 'Install the Rojo plugin into the Studio Plugins folder (rojo plugin install)?') { rojo plugin install }
    Pop-Location
  }
}

# ---- 4 Studio MCP
$mcpBat = Join-Path $env:LOCALAPPDATA 'Roblox\mcp.bat'
$mcpExists = $false
if (-not $SkipMcp) {
  Say "`n[4/4] Studio MCP server: Studio's built-in server that lets Claude read/write scripts, run Luau, start playtests and read Output."
  Say "  It is the official one (create.roblox.com/docs/studio/mcp). Registering adds a config entry only; nothing runs until Studio is open."
  if (-not (Has 'claude')) { Say '  skipped: Claude Code not found.' }
  else {
    $exists = $false
    $prev = $ErrorActionPreference; $ErrorActionPreference = 'SilentlyContinue'
    $null = & claude mcp get Roblox_Studio 2>&1
    if ($LASTEXITCODE -eq 0) { $exists = $true }
    $ErrorActionPreference = $prev
    if ($exists) { Say '  Roblox_Studio is already registered (leaving it as is).' }
    elseif (Ask "Register the Roblox_Studio MCP server with Claude Code (scope: $Scope)?") {
      $wd = if ($Scope -eq 'project' -and $ProjectDir) { $ProjectDir } else { (Get-Location).Path }
      Push-Location $wd
      try { & claude mcp add --scope $Scope Roblox_Studio -- cmd.exe /c '%LOCALAPPDATA%\Roblox\mcp.bat' } finally { Pop-Location }
    }
  }
}

# ---- 5 verify
Say "`nVerifying..."
$prev = $ErrorActionPreference; $ErrorActionPreference = 'SilentlyContinue'
foreach ($t in 'rokit', 'rojo', 'selene', 'stylua', 'luau-lsp', 'lune') {
  if (Has $t) {
    Push-Location $Systems
    $v = (& $t --version 2>&1 | Select-Object -First 1)
    Pop-Location
    if ($v -match 'ERROR|Failed') { Add-Result $t 'MISSING' 'on PATH but not installed for this folder: run `rokit install` in systems\' } else { Add-Result $t 'ok' "$v" }
  } else { Add-Result $t 'MISSING' 'not on PATH' }
}
if (Has 'wally') { Add-Result 'wally' 'ok' ((& wally --version 2>&1 | Select-Object -First 1)) } else { Add-Result 'wally' 'optional' 'not installed (-WithWally)' }
Add-Result 'Rojo plugin' $(if (Test-Path -LiteralPath (Join-Path $env:LOCALAPPDATA 'Roblox\Plugins\RojoManagedPlugin.rbxm')) { 'ok' } else { 'MISSING' }) 'Roblox\Plugins\RojoManagedPlugin.rbxm'
$studioDir = Join-Path $env:LOCALAPPDATA 'Roblox\Versions'
$studioInstalled = (Test-Path -LiteralPath (Join-Path $env:LOCALAPPDATA 'Roblox\StudioMCP')) -or (Test-Path -LiteralPath $studioDir) -or (Test-Path -LiteralPath 'C:\Program Files (x86)\Roblox\Versions')
Add-Result 'Roblox Studio' $(if ($studioInstalled) { 'ok' } else { 'MISSING' }) 'install from create.roblox.com/landing (you sign in yourself)'
Add-Result 'mcp.bat' $(if (Test-Path -LiteralPath $mcpBat) { 'ok' } else { 'not yet' }) 'written by Studio when you enable the MCP server (step B below)'
if (Has 'claude') {
  $out = (& claude mcp get Roblox_Studio 2>&1 | Out-String)
  if ($LASTEXITCODE -eq 0) { Add-Result 'claude mcp Roblox_Studio' 'ok' ((($out -split "`n") | Where-Object { $_ -match 'Scope|Command|Args' } | ForEach-Object { $_.Trim() }) -join ' | ') }
  else { Add-Result 'claude mcp Roblox_Studio' 'NOT registered' 'run this script again without -SkipMcp' }
} else { Add-Result 'claude' 'MISSING' 'Claude Code not on PATH' }
$ErrorActionPreference = $prev
$Results | Format-Table -AutoSize | Out-String | Write-Host

Say 'What is left for you (only you can do these):'
Say '  A. Open Roblox Studio, sign in with your Roblox account, open or create a place.'
Say '  B. Studio: Assistant > ... menu > Manage MCP Servers > turn on "Enable Studio as MCP server" (a green indicator shows connected clients).'
Say '  C. Restart Studio and Claude Code. In Claude Code, /mcp should list Roblox_Studio as connected while Studio is running.'
Say '  D. Only connect clients you trust: an MCP client can read and modify the open place. Keep a backup / version history.'
$bad = @($Results | Where-Object { $_.Status -eq 'MISSING' -or $_.Status -eq 'NOT registered' })
if ($DryRun) { Say 'Dry run: nothing was changed.' }
if ($bad.Count -gt 0) { Say ("Incomplete: " + (($bad | ForEach-Object { $_.Check }) -join ', ')); exit 2 }
exit 0
