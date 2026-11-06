# claude-kit installer for Windows (PowerShell 5.1+). Safe to run again. No questions, no admin, sets nothing global.
#   ON-DEMAND STORE (Roblox dev mode, not read by normal Claude sessions): agents\* -> %USERPROFILE%\.claude\claude-kit\vault-mode\.claude\agents\   skills\* -> ...\vault-mode\.claude\skills\   mode\CLAUDE.md -> ...\vault-mode\CLAUDE.md
#   The VAULT FOLDER (the notes clone, e.g. %USERPROFILE%\Obsidian\claudes-vault) is permanently loaded: tools\vault-mode.py load --project <vault> (run here at the end, quietly, and by every update) copies the store's skills+agents+rules into <vault>\.claude\, hidden from git together with Games\ and Models\. Older loaded project folders are cleaned. No load/unload commands exist.
#   COLD AREA: mode\cold\<topic>\* rides the mode\* mapping -> ...\claude-kit\vault-mode\cold\ (installed, refreshed, in installed.tsv, removed by uninstall; never copied into a folder; read with tools\vault-mode.py cold).
#   ALWAYS-ON (the only kit skills in %USERPROFILE%\.claude\skills, listed in mode\always-on.txt): rbx-update rbx-check rbx-uninstall
#   tools\* -> %USERPROFILE%\.claude\claude-kit\tools\  systems\* -> %USERPROFILE%\.claude\claude-kit\systems\  skillpack\* -> ...\claude-kit\skillpack\ (NOT skills: opened on demand by the /rbx router skill)
# An older install (kit skills/agents directly in .claude\skills and \agents) is migrated by tools\vault-mode.py migrate: kit files move to a backup folder, your own skills/agents/CLAUDE.md are untouched, idempotent, reversible.
# The vault owns every file it installs: an install/update overwrites each one with the incoming version and removes files that left the kit (no keep, no conflicts). The only content that is yours is your project's Games/ and Models/ folders and anything outside the vault's own paths; nothing here touches them. claude-kit/state/ holds a few tiny settings (rbx-mockup on/off) that are never deleted.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 [-KitHome <dir>] [-DryRun] [-WithHooks | -RemoveHooks] [-WithMods]
# -WithMods (opt-in): also install the /rbx-subagent-hud and /rbx-graph Claude Code plugins (plugins load in every session, so they are no longer installed by default).
# -WithHooks / -RemoveHooks (opt-in, never automatic): merge into / remove from %USERPROFILE%\.claude\settings.json the two /rbx-low-usage hooks and the rbx-mentor suggestion hook (UserPromptSubmit) (backup first, idempotent, keeps all other settings).
param([string]$KitHome = $(if ($env:CLAUDE_KIT_HOME) { $env:CLAUDE_KIT_HOME } else { $env:USERPROFILE }), [switch]$DryRun, [switch]$WithHooks, [switch]$RemoveHooks, [switch]$WithMods)
$ErrorActionPreference = 'Stop'
$Kit = Split-Path -Parent $MyInvocation.MyCommand.Path
$C = Join-Path $KitHome '.claude'
if (-not $PSBoundParameters.ContainsKey('KitHome') -and -not $env:CLAUDE_KIT_HOME -and $env:CLAUDE_CONFIG_DIR) { $C = $env:CLAUDE_CONFIG_DIR }
$Man = Join-Path $C 'claude-kit\installed.tsv'
function Sha([string]$p) { (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToLower() }

$SM = 'claude-kit/vault-mode'
$ao = @('rbx-update', 'rbx-check', 'rbx-uninstall')
$aof = Join-Path $Kit 'mode\always-on.txt'
if (Test-Path -LiteralPath $aof) { $ao = @([IO.File]::ReadAllLines($aof) | ForEach-Object { $_.Trim() } | Where-Object { $_ -and -not $_.StartsWith('#') }) }
$firstWf = -not (Test-Path -LiteralPath $Man)     # fresh install: print the welcome text at the end
# an older layout: keep its manifest for the migration step (only once; vault-mode.py migrate moves it into its backup folder)
$preMode = Join-Path $C 'claude-kit\installed.tsv.pre-mode'
if ((Test-Path -LiteralPath $Man) -and -not (Test-Path -LiteralPath (Join-Path $C 'claude-kit\vault-mode\layout.json')) -and -not (Test-Path -LiteralPath $preMode) -and -not $DryRun) { Copy-Item -LiteralPath $Man -Destination $preMode }
$old = @{}
if (Test-Path -LiteralPath $Man) {
  foreach ($l in [IO.File]::ReadAllLines($Man)) { $p = $l -split "`t"; if ($p.Count -ge 2) { $old[$p[0]] = $p[1] } }
}
$new = New-Object System.Collections.Generic.List[string]
$nNew = 0; $nUpd = 0; $nSame = 0; $nGone = 0; $nFail = 0

# one-time rename migration (old generic command names -> <verb>-<slug>-vault; names in tools\vault-names.json): removes the OLD-named vault skills/agents that the kit installed and that are
# unchanged (backup + undo: kit-rename.py migrate --revert); never touches a skill/agent of yours with an old name. Runs BEFORE the copy so the old manifest still lists the old names. Silent when nothing is to do.
$renameMsg = ''; $renamed = $false
$kr = Join-Path $Kit 'tools\kit-rename.py'
if ((Test-Path -LiteralPath $kr) -and (Test-Path -LiteralPath $Man) -and ((Get-Item -LiteralPath $Man).Length -gt 0)) {
  $rpy = $null
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $rpy = $cmd.Source; break } } catch { } } }
  if ($rpy) {
    $prevCfgR = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
    $ra = @('-I', $kr, 'migrate', '--config', $C); if ($DryRun) { $ra += '--dry-run' }
    $ea0 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    $renameMsg = (& $rpy @ra 2>&1 | Out-String).Trim()
    $ErrorActionPreference = $ea0
    if ($WithMods -and -not $DryRun) { $plMsg = (& $rpy -I $kr 'plugins' '--config' $C 2>&1 | Out-String).Trim(); if ($plMsg) { Write-Output $plMsg } }   # enabledPlugins keys of the mods under their old names
    $env:CLAUDE_CONFIG_DIR = $prevCfgR; if (-not $prevCfgR) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    if ($renameMsg -match 'commands (renamed|merged)') { $renamed = $true }
  } else { Write-Output 'kit-rename: no working Python 3, so old command names were not migrated; install Python 3 and run the update again' }
}

# FAST PATH (default): one Python process does the whole copy loop, the stale-file removal and the manifest (tools\kit-install-files.py); the PowerShell loop below is the fallback without Python 3 (or CLAUDE_KIT_SLOW=1)
$fastDone = $false; $fpy = $null
foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $fpy = $cmd.Source; break } } catch { } } }
$kif = Join-Path $Kit 'tools\kit-install-files.py'
if ($fpy -and (Test-Path -LiteralPath $kif) -and $env:CLAUDE_KIT_SLOW -ne '1') {
  $ka = @('-I', $kif, '--kit', $Kit, '--config', $C, '--always-on', ($ao -join ' ')); if ($DryRun) { $ka += '--dry-run' }
  $ea0 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  $fo = (& $fpy @ka 2>&1 | Out-String); $ErrorActionPreference = $ea0
  $rm = [regex]::Match($fo, '(?m)^RESULT new=(\d+) upd=(\d+) same=(\d+) gone=(\d+) fail=(\d+)')
  if ($rm.Success) {
    $nNew = [int]$rm.Groups[1].Value; $nUpd = [int]$rm.Groups[2].Value; $nSame = [int]$rm.Groups[3].Value; $nGone = [int]$rm.Groups[4].Value; $nFail = [int]$rm.Groups[5].Value
    foreach ($fl in ($fo -split "`r?`n" | Where-Object { $_ -like 'FAILED *' } | Select-Object -First 5)) { Write-Output $fl }
    $fastDone = $true
  } else { Write-Output ("claude-kit: fast installer failed, using the PowerShell loop (" + (($fo -split "`r?`n" | Where-Object { $_.Trim() } | Select-Object -Last 1)) + ")") }
}
if (-not $fastDone) {
foreach ($sub in 'agents', 'skills', 'mode', 'tools', 'systems', 'skillpack') {
  $root = Join-Path $Kit $sub
  if (-not (Test-Path -LiteralPath $root)) { continue }
  Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object { $_.FullName -notmatch '\\__pycache__\\' -and $_.Extension -ne '.pyc' } | Sort-Object FullName | ForEach-Object {
    $r = $_.FullName.Substring($Kit.Length + 1).Replace('\', '/')
    $rel = switch ($sub) {
      'agents' { "$SM/.claude/$r" }
      'mode' { "$SM/" + $r.Substring(5) }
      'skills' { $nm = $r.Split('/')[1]; if ($ao -contains $nm) { $r } else { "$SM/.claude/$r" } }
      default { "claude-kit/$r" } }
    $dst = Join-Path $C ($rel.Replace('/', '\'))
    $rec = $null
    try {
    $ns = Sha $_.FullName; $rec = $ns
    if (Test-Path -LiteralPath $dst -PathType Container) { throw 'a folder is in the way' }
    if (-not (Test-Path -LiteralPath $dst)) {
      if (-not $DryRun) { New-Item -ItemType Directory -Force (Split-Path -Parent $dst) | Out-Null; Copy-Item -LiteralPath $_.FullName -Destination $dst }
      $nNew++
    } elseif ((Sha $dst) -eq $ns) {
      $nSame++
    } else {
      if (-not $DryRun) { Copy-Item -LiteralPath $_.FullName -Destination $dst -Force }
      $nUpd++
    }
    } catch {
      $nFail++; $rec = $old[$rel]; Write-Output "FAILED ${rel}: $($_.Exception.Message)"
    }
    if ($rec) { $new.Add("$rel`t$rec") }
  }
}
$layOk = $true
$layF = Join-Path $C 'claude-kit\vault-mode\layout.json'
if (Test-Path -LiteralPath $layF) { try { $lay = Get-Content -LiteralPath $layF -Raw | ConvertFrom-Json; if ($lay.auto -eq $false -or $lay.rename_auto -eq $false) { $layOk = $false } } catch { } }
if ($layOk) {
  $seen = New-Object 'System.Collections.Generic.HashSet[string]'
  foreach ($e in $new) { [void]$seen.Add(($e -split "`t")[0]) }
  foreach ($rel in @($old.Keys | Sort-Object)) {
    if ($seen.Contains($rel)) { continue }
    $parts = $rel.Split('/')
    if ($rel.StartsWith('/') -or ($parts -contains '..') -or $rel.Contains(':') -or $rel.Contains('\')) { continue }
    if (-not ($rel.StartsWith('claude-kit/') -or ($rel.StartsWith('skills/') -and $parts.Count -gt 1 -and ($ao -contains $parts[1])))) { continue }
    $f = Join-Path $C ($rel.Replace('/', '\'))
    try {
      if ((Test-Path -LiteralPath $f -PathType Leaf) -and -not ((Get-Item -LiteralPath $f -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
        if (-not $DryRun) {
          Remove-Item -LiteralPath $f -Force
          $stop = Join-Path $C $parts[0]; $d = Split-Path -Parent $f
          while ($d.Length -gt $stop.Length -and $d.StartsWith($stop + '\') -and -not (Get-ChildItem -LiteralPath $d -Force | Select-Object -First 1)) { Remove-Item -LiteralPath $d -Force; $d = Split-Path -Parent $d }
        }
        $nGone++
      }
    } catch { }
  }
}
if (-not $DryRun) {
  New-Item -ItemType Directory -Force (Split-Path -Parent $Man) | Out-Null
  [IO.File]::WriteAllText($Man, (($new | Sort-Object -Unique) -join "`n") + "`n", (New-Object Text.UTF8Encoding $false))
}
}
# move an older always-on layout into the store (idempotent; silent when there is nothing to move)
$vm = Join-Path $C 'claude-kit\tools\vault-mode.py'
if (-not $DryRun -and (Test-Path -LiteralPath $vm)) {
  $mpy = $null
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $mpy = $cmd.Source; break } } catch { } } }
  if ($mpy) { $prevCfgM = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C; $mo = (& $mpy -I $vm migrate --config $C 2>&1 | Out-String).Trim(); $env:CLAUDE_CONFIG_DIR = $prevCfgM; if (-not $prevCfgM) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }; if ($mo) { $migrateOut = $mo } }
  elseif (Test-Path -LiteralPath $preMode) { $migrateOut = 'vault-mode: no working Python 3, so the old always-on kit skills were not moved; install Python 3 and run /rbx-update' }
}
# the vault folder is THE loaded environment: resolve it (the clone that holds this claude-kit folder, $env:CLAUDES_VAULT, the registered one, ~\Obsidian\claudes-vault) and load it quietly (env CLAUDE_KIT_NOLOAD=1: the caller, kit-refresh, does it)
$vh = ''; $loadOut = ''
$kitVm = Join-Path $Kit 'tools\vault-mode.py'
if (Test-Path -LiteralPath $kitVm) {
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) {
    $prevCfgH = $env:CLAUDE_CONFIG_DIR; $prevKh = $env:CLAUDE_KIT_HOME; $env:CLAUDE_CONFIG_DIR = $C; $env:CLAUDE_KIT_HOME = $KitHome
    $ea1 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    $vh = ((& $cmd.Source -I $kitVm home --kit $Kit --config $C 2>$null | Out-String).Trim() -split "`r?`n" | Select-Object -Last 1)
    if ($vh -and -not $DryRun -and $env:CLAUDE_KIT_NOLOAD -ne '1' -and (Test-Path -LiteralPath $vm)) {
      $la = @('-I', $vm, 'load', '--project', $vh, '--quiet', '--config', $C); if (-not $firstWf) { $la += '--announce' }
      $loadOut = (& $cmd.Source @la 2>&1 | Out-String).Trim()
    }
    $ErrorActionPreference = $ea1
    $env:CLAUDE_CONFIG_DIR = $prevCfgH; if (-not $prevCfgH) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    $env:CLAUDE_KIT_HOME = $prevKh; if (-not $prevKh) { Remove-Item Env:\CLAUDE_KIT_HOME -ErrorAction SilentlyContinue }
    break } } catch { } } }
}
Write-Output ("claude-kit: installed $nNew new, updated $nUpd, unchanged $nSame" + $(if ($nGone) { ", removed $nGone no longer in the kit" }) + $(if ($nFail) { ", FAILED $nFail" }) + " (into $C)")
if ($renameMsg) { Write-Output $renameMsg }
if ($loadOut) { Write-Output $loadOut }
# UI mockups default to automatic design-first: ONE non-blocking NOTICE FOR THE USER line per install (marker claude-kit/ui-mockup-notice.done); a fresh install only sets the marker (the setup text asks the question)
$uip = Join-Path $Kit 'tools\ui_pref.py'
if ((Test-Path -LiteralPath $uip) -and -not $DryRun) {
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) {
    $prevCfgU = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
    $ua = @('-I', $uip, 'notice'); if ($firstWf) { $ua += '--mark-only' }
    $ea1 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'; $uim = (& $cmd.Source @ua 2>$null | Out-String).Trim(); $ErrorActionPreference = $ea1
    $env:CLAUDE_CONFIG_DIR = $prevCfgU; if (-not $prevCfgU) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    if ($uim) { Write-Output $uim }
    break } } catch { } } }
}

if ($migrateOut) { Write-Output $migrateOut }
if ($WithHooks -or $RemoveHooks) {
  $py = $null
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $py = $cmd.Source; break } } catch { } } }
  $lum = Join-Path $C 'claude-kit\vault-mode\.claude\skills\rbx-low-usage\scripts\lum.py'
  if (-not $py) { Write-Output 'rbx-low-usage hooks: skipped (no working Python 3)' }
  elseif ($DryRun) { Write-Output 'rbx-low-usage hooks: dry run, settings.json not touched' }
  elseif (-not (Test-Path -LiteralPath $lum)) { Write-Output 'rbx-low-usage hooks: skipped (skill not installed)' }
  else { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $lum $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
  # rbx-mentor suggestion hook (UserPromptSubmit; same opt-in flags, backup first, idempotent)
  $mh = Join-Path $C 'claude-kit\tools\mentor-hook.py'
  if ($py -and -not $DryRun -and (Test-Path -LiteralPath $mh)) { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $mh $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
}
# similar user skills (other names) -> listed; the kit wins at routing time (precedence line in the kit entry points)
$sim = Join-Path $Kit 'tools\similar-skills.py'
if ((Test-Path -LiteralPath $sim)) {
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { $o = (& $cmd.Source -I $sim --kit $Kit --config $C 2>$null | Out-String).Trim(); if ($LASTEXITCODE -eq 0) { if ($o) { Write-Output $o }; break } } catch { } } }
}
# kit mods (Claude Code plugins: /rbx-subagent-hud workflow tree, /rbx-graph vault graph) from <vault>/claude-kit/mods. OPT-IN (-WithMods): plugins load in every Claude session. Needs the claude CLI; idempotent (already installed = OK).
$modsDir = Join-Path $Kit 'mods'; $mk = 'roblox-vault-kit-mods'
if ((Test-Path -LiteralPath (Join-Path $modsDir '.claude-plugin\marketplace.json')) -and -not $DryRun -and $WithMods) {
  function ClaudeRun([string]$exe, [string[]]$a) { $ea = $ErrorActionPreference; $ErrorActionPreference = 'Continue'; try { $o = (& $exe @a 2>&1 | Out-String); return @{ code = $LASTEXITCODE; out = $o } } catch { return @{ code = 1; out = $_.Exception.Message } } finally { $ErrorActionPreference = $ea } }
  $cl = Get-Command claude -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($cl) {
    $prevCfg = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
    $ok = $true; $why = ''
    $lst = ClaudeRun $cl.Source @('plugin', 'list', '--json')
    $have = ($lst.code -eq 0) -and ($lst.out -match "rbx-subagent-hud@$mk") -and ($lst.out -match "rbx-graph@$mk")
    # plugins installed under their previous names (before the vault-suffixed rename): uninstall them, refresh the marketplace listing, install the new ones below
    $oldMods = $false
    foreach ($om in 'workflow-hud', 'vault-graph', 'hud-rbxdev-vault', 'graph-rbxdev-vault', 'rbx-subagent-hud') { if ($lst.out -match "$om@$mk") { [void](ClaudeRun $cl.Source @('plugin', 'uninstall', "$om@$mk")); $oldMods = $true } }  # legacy plugin names
    if ($oldMods) { [void](ClaudeRun $cl.Source @('plugin', 'marketplace', 'update', $mk)); $have = $false }   # REL4: a plugin was uninstalled above: install both again, never leave one missing
    if (-not $have) {
      $r = ClaudeRun $cl.Source @('plugin', 'marketplace', 'add', $modsDir)
      if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = 'marketplace add failed' }
      foreach ($m in 'rbx-subagent-hud', 'rbx-graph') {
        if (-not $ok) { break }
        $r = ClaudeRun $cl.Source @('plugin', 'install', "$m@$mk")
        if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = "install of $m failed" }
      }
    }
    if ($ok) {   # SM: copy semantics: a plugin that was already installed keeps its old copy until updated (rbx-graph 0.2.0 = link only)
      [void](ClaudeRun $cl.Source @('plugin', 'marketplace', 'update', $mk))
      foreach ($m in 'rbx-subagent-hud', 'rbx-graph') { [void](ClaudeRun $cl.Source @('plugin', 'update', "$m@$mk")) }
    }
    $env:CLAUDE_CONFIG_DIR = $prevCfg; if (-not $prevCfg) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    if ($ok) { Write-Output 'mods: rbx-subagent-hud (/rbx-subagent-hud), rbx-graph (/rbx-graph): installed' }
    else { Write-Output "mods: not installed ($why). In a Claude session run: /plugin marketplace add $modsDir  then  /plugin install rbx-subagent-hud@$mk  and  /plugin install rbx-graph@$mk  then  /reload-plugins" }
  } else {
    Write-Output "mods: claude CLI not found. In a Claude session run: /plugin marketplace add $modsDir  then  /plugin install rbx-subagent-hud@$mk  and  /plugin install rbx-graph@$mk  then  /reload-plugins"
  }
}
# legacy kit-mod plugins (see install.sh): on every run without -WithMods uninstall them via the claude CLI; best effort, silent without the CLI or without legacy plugins.
if (-not $DryRun -and -not $WithMods) {
  try {
    $clL = Get-Command claude -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($clL) {
      $prevCfgL = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C; $ea0 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
      $lstL = (& $clL.Source plugin list --json 2>$null | Out-String); $oldL = $false
      foreach ($om in 'workflow-hud', 'vault-graph', 'hud-rbxdev-vault', 'graph-rbxdev-vault') { if ($lstL -match ('"?' + [regex]::Escape($om) + '@roblox-vault-kit-mods')) { [void](& $clL.Source plugin uninstall "$om@roblox-vault-kit-mods" 2>&1); $oldL = $true } }  # legacy plugin names
      if ($oldL) {
        $pyL = $null
        foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $pyL = $cmd.Source; break } } catch { } } }
        if ($pyL) { [void](& $pyL -I (Join-Path $Kit 'tools\kit-rename.py') plugins --drop-legacy --config $C 2>&1) }
        if (-not (($lstL -match 'rbx-subagent-hud@roblox-vault-kit-mods') -and ($lstL -match 'rbx-graph@roblox-vault-kit-mods'))) { Write-Output 'Old vault plugins removed. To add the HUD and graph: run the installer with --with-mods (claude-kit/install.sh --with-mods or install.ps1 -WithMods), then /reload-plugins.' }
      }
      $ErrorActionPreference = $ea0; $env:CLAUDE_CONFIG_DIR = $prevCfgL; if (-not $prevCfgL) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    }
  } catch { }
}
if ($vh) { $vsay = $vh } else { $vsay = 'your vault folder (not found on this computer: clone the vault first, see SETUP-FOR-CLAUDE.md, then run this installer again)' }
if ($firstWf -and -not $DryRun) { Write-Output ('The Roblox Dev Mastery Vault kit is installed. TO USE THE VAULT: load it by starting a Claude session in ' + $vsay + ' (that folder is the loaded vault: the vault skills, agents, art-direction, placement, lighting and visual-QA rules and reference images are there automatically; no load command is needed; your other Claude sessions stay clean). Always available in every session: /rbx-update /rbx-check /rbx-uninstall. In the vault folder: /rbx-idea-quick (one fresh idea) or /rbx-workflow (idea, rating, plan, build); /rbx-make; judgement and your games (in the Games/ folder of the vault, never touched by updates): /rbx-critic /rbx-weekly /rbx-launch-kit /rbx-harvest; Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>; placement, lighting and looks (a game is never called done without them): /rbx-placement /rbx-lighting /rbx-art /rbx-visual; measure the vault itself: /rbx-bench; mentor: /rbx-mentor; research: /rbx-research; manager: /rbx-manager; vault: /rbx-clean /rbx-setup /rbx-light-on /rbx-light-off /rbx-list; usage: /rbx-low-usage. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)') }
if ($env:CLAUDE_KIT_NOFOOTER -ne '1') { Write-Output ''; Write-Output ('>>> Load the vault by starting a Claude session in ' + $vsay + ' (then /rbx-list shows everything it contains).') }
if ($nFail) { exit 1 }
exit 0
