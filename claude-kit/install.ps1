# claude-kit installer for Windows (PowerShell 5.1+). Safe to run again. No questions, no admin, sets no environment variables or shell profiles; the two mods (see MODS below) are the one thing that touches your Claude plugin settings.
#   ON-DEMAND STORE (Roblox dev mode, not read by normal Claude sessions): agents\* -> %USERPROFILE%\.claude\claude-kit\vault-mode\.claude\agents\   skills\* -> ...\vault-mode\.claude\skills\   mode\CLAUDE.md -> ...\vault-mode\CLAUDE.md
#   The VAULT FOLDER (the notes clone, e.g. %USERPROFILE%\Obsidian\claudes-vault) is permanently loaded: tools\vault-mode.py load --project <vault> (run here at the end, quietly, and by every update) copies the store's skills+agents+rules into <vault>\.claude\, hidden from git together with Games\, Models\, My-Skills\ and My-Agents\ (your own skills and agents are copied in too; the vault never changes those folders). Older loaded project folders are cleaned. No load/unload commands exist.
#   COLD AREA: mode\cold\<topic>\* rides the mode\* mapping -> ...\claude-kit\vault-mode\cold\ (installed, refreshed, in installed.tsv, removed by uninstall; never copied into a folder; read with tools\vault-mode.py cold).
#   ALWAYS-ON (the only kit skills in %USERPROFILE%\.claude\skills, listed in mode\always-on.txt): rbx-update rbx-check rbx-uninstall
#   tools\* -> %USERPROFILE%\.claude\claude-kit\tools\  systems\* -> %USERPROFILE%\.claude\claude-kit\systems\  skillpack\* -> ...\claude-kit\skillpack\ (NOT skills: opened on demand by the /rbx router skill)
# An older install (kit skills/agents directly in .claude\skills and \agents) is migrated by tools\vault-mode.py migrate: kit files move to a backup folder, your own skills/agents/CLAUDE.md are untouched, idempotent, reversible.
# The vault owns every file it installs: an install/update overwrites each one with the incoming version and removes files that left the kit (no keep, no conflicts). The only content that is yours is your project's Games/, Models/, My-Skills/ and My-Agents/ folders and anything outside the vault's own paths; nothing here touches them. claude-kit/state/ holds a few tiny settings (rbx-mockup on/off) that are never deleted.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 [-KitHome <dir>] [-DryRun] [-WithHooks | -RemoveHooks] [-NoMods] [-NoAssets]
# ONE RUN DOES EVERYTHING: after the kit files, the two mods and the vault load, this script runs tools\vault-sync-all.py for the resolved vault folder: extra notes repositories (vault-shards.py), the Roblox reference screenshots (refs-sync.py, ~30 MB) and the asset zips (assets-sync.py, ~1 GB), with short progress lines (`assets: 3/6 zips ...`). It FAILS SOFT: a failed download prints ONE `Assets incomplete: <reason>. To finish, run (resumes): <command>` line and the script still exits 0; running it again resumes. -NoAssets (env CLAUDE_ASSETS_SKIP=1) skips the asset zips only. Callers that sync themselves (kit-refresh, the sync-setup scripts: env CLAUDE_KIT_NOFOOTER=1 or CLAUDE_KIT_NOLOAD=1) skip this part. Test knobs: env CLAUDE_SYNC_BASE (a mirror URL), CLAUDE_SYNC_DRY=1 (report only).
# MODS (default ON, no flag): tools\kit-mods.py installs the /rbx-subagent-hud (agent sidebar) and /rbx-graph (vault graph link) Claude Code plugins from the vault's claude-kit\mods at PROJECT scope of the VAULT FOLDER (claude plugin ... --scope project, enabledPlugins in <vault>\.claude\settings.json, hidden from git): the hooks apply only to sessions started in the vault folder, never to other sessions. An older USER-scope install is migrated (uninstalled from user scope, installed at project scope, one notice line). -NoMods: do not install them and uninstall them (both scopes) if present (a later update will not bring them back); -WithMods: accepted (old docs), also re-installs them after -NoMods or after you removed them with /plugin. Any problem (no claude CLI, offline, plugins disabled by policy, plugin errors) prints ONE "Mods skipped: <reason>. Run again later: <command>" line and the install still succeeds.
# -WithHooks / -RemoveHooks (opt-in, never automatic): merge into / remove from %USERPROFILE%\.claude\settings.json the two /rbx-low-usage hooks and the rbx-mentor suggestion hook (UserPromptSubmit) (backup first, idempotent, keeps all other settings).
param([string]$KitHome = $(if ($env:CLAUDE_KIT_HOME) { $env:CLAUDE_KIT_HOME } else { $env:USERPROFILE }), [switch]$DryRun, [switch]$WithHooks, [switch]$RemoveHooks, [switch]$WithMods, [switch]$NoMods, [switch]$NoAssets)
$ErrorActionPreference = 'Stop'
$assetsOn = (-not $NoAssets) -and ($env:CLAUDE_ASSETS_SKIP -ne '1')
$Kit = Split-Path -Parent $MyInvocation.MyCommand.Path
$C = Join-Path $KitHome '.claude'
if (-not $PSBoundParameters.ContainsKey('KitHome') -and -not $env:CLAUDE_KIT_HOME -and $env:CLAUDE_CONFIG_DIR) { $C = $env:CLAUDE_CONFIG_DIR }
function Get-Py { foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { return $cmd.Source } } catch { } } }; return $null }
# ONE FOLDER: the kit is installed INSIDE the vault folder (<vault>\.rbx\claude-kit); only 3 stub skills + a pointer file stay in $C. No vault folder (kit-only install, tests): the old layout in $C.
$vh = ''; $py0 = Get-Py; $kpk = Join-Path $Kit 'tools\kit_paths.py'
if ($py0 -and (Test-Path -LiteralPath $kpk)) {
  $pCfg0 = $env:CLAUDE_CONFIG_DIR; $pKh0 = $env:CLAUDE_KIT_HOME; $env:CLAUDE_CONFIG_DIR = $C; $env:CLAUDE_KIT_HOME = $KitHome
  $ea0 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  $vh = [string](((& $py0 -I $kpk vault --config $C 2>$null | Out-String).Trim() -split "`r?`n" | Select-Object -Last 1))
  $ErrorActionPreference = $ea0
  $env:CLAUDE_CONFIG_DIR = $pCfg0; if (-not $pCfg0) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
  $env:CLAUDE_KIT_HOME = $pKh0; if (-not $pKh0) { Remove-Item Env:\CLAUDE_KIT_HOME -ErrorAction SilentlyContinue }
}
$KH = $C; if ($vh -and (Test-Path -LiteralPath $vh -PathType Container)) { if ($env:RBX_LAYOUT -ne 'legacy') { $KH = Join-Path $vh '.rbx' } } else { $vh = '' }      # env RBX_LAYOUT=legacy keeps the old layout (claude-kit in the config folder; tests)
$env:RBX_KIT_HOME = $KH
$relocMsg = ''
if (($KH -ne $C) -and -not $DryRun -and $py0 -and (Test-Path -LiteralPath (Join-Path $C 'claude-kit') -PathType Container) -and (Test-Path -LiteralPath (Join-Path $Kit 'tools\vault-mode.py'))) {   # MIGRATION of an old install: move ~\.claude\claude-kit into the vault folder (idempotent, resumable; only provable duplicates are deleted)
  New-Item -ItemType Directory -Force (Join-Path $KH 'claude-kit') | Out-Null
  $pCfg1 = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
  $ea0 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  $relocMsg = (& $py0 -I (Join-Path $Kit 'tools\vault-mode.py') relocate --config $C 2>&1 | Out-String).Trim()
  $ErrorActionPreference = $ea0
  $env:CLAUDE_CONFIG_DIR = $pCfg1; if (-not $pCfg1) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
  if ($relocMsg) { Write-Output $relocMsg }
}
$Man = Join-Path $KH 'claude-kit\installed.tsv'
function Sha([string]$p) { (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToLower() }

$SM = 'claude-kit/vault-mode'
$ao = @('rbx-update', 'rbx-check', 'rbx-uninstall')
$aof = Join-Path $Kit 'mode\always-on.txt'
if (Test-Path -LiteralPath $aof) { $ao = @([IO.File]::ReadAllLines($aof) | ForEach-Object { $_.Trim() } | Where-Object { $_ -and -not $_.StartsWith('#') }) }
$firstWf = -not (Test-Path -LiteralPath $Man)     # fresh install: print the welcome text at the end
# an older layout: keep its manifest for the migration step (only once; vault-mode.py migrate moves it into its backup folder)
$preMode = Join-Path $KH 'claude-kit\installed.tsv.pre-mode'
if ((Test-Path -LiteralPath $Man) -and -not (Test-Path -LiteralPath (Join-Path $KH 'claude-kit\vault-mode\layout.json')) -and -not (Test-Path -LiteralPath $preMode) -and -not $DryRun) { Copy-Item -LiteralPath $Man -Destination $preMode }
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
    if ((-not $NoMods) -and -not $DryRun) { $plMsg = (& $rpy -I $kr 'plugins' '--config' $C 2>&1 | Out-String).Trim(); if ($plMsg) { Write-Output $plMsg } }   # enabledPlugins keys of the mods under their old names
    $env:CLAUDE_CONFIG_DIR = $prevCfgR; if (-not $prevCfgR) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    if ($renameMsg -match 'commands (renamed|merged)') { $renamed = $true }
  } else { Write-Output 'kit-rename: no working Python 3, so old command names were not migrated; install Python 3 and run the update again' }
}

# FAST PATH (default): one Python process does the whole copy loop, the stale-file removal and the manifest (tools\kit-install-files.py); the PowerShell loop below is the fallback without Python 3 (or CLAUDE_KIT_SLOW=1)
$fastDone = $false; $fpy = $null
foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $fpy = $cmd.Source; break } } catch { } } }
$kif = Join-Path $Kit 'tools\kit-install-files.py'
if ($fpy -and (Test-Path -LiteralPath $kif) -and $env:CLAUDE_KIT_SLOW -ne '1') {
  $ka = @('-I', $kif, '--kit', $Kit, '--config', $C, '--kit-home', $KH, '--always-on', ($ao -join ' ')); if ($DryRun) { $ka += '--dry-run' }
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
      'skills' { $nm = $r.Split('/')[1]; if (($ao -contains $nm) -and ($KH -eq $C)) { $r } else { "$SM/.claude/$r" } }
      default { "claude-kit/$r" } }
    $dst = Join-Path $(if ($rel.StartsWith('claude-kit/')) { $KH } else { $C }) ($rel.Replace('/', '\'))
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
$layF = Join-Path $KH 'claude-kit\vault-mode\layout.json'
if (Test-Path -LiteralPath $layF) { try { $lay = Get-Content -LiteralPath $layF -Raw | ConvertFrom-Json; if ($lay.auto -eq $false -or $lay.rename_auto -eq $false) { $layOk = $false } } catch { } }
if ($layOk) {
  $seen = New-Object 'System.Collections.Generic.HashSet[string]'
  foreach ($e in $new) { [void]$seen.Add(($e -split "`t")[0]) }
  foreach ($rel in @($old.Keys | Sort-Object)) {
    if ($seen.Contains($rel)) { continue }
    $parts = $rel.Split('/')
    if ($rel.StartsWith('/') -or ($parts -contains '..') -or $rel.Contains(':') -or $rel.Contains('\')) { continue }
    if (-not ($rel.StartsWith('claude-kit/') -or ($rel.StartsWith('skills/') -and $parts.Count -gt 1 -and (($KH -eq $C -and ($ao -contains $parts[1])) -or $parts[1] -eq 'rbx-load' -or $parts[1] -eq 'rbx-unload')))) { continue }
    $kb0 = if ($rel.StartsWith('claude-kit/')) { $KH } else { $C }
    $f = Join-Path $kb0 ($rel.Replace('/', '\'))
    try {
      if ((Test-Path -LiteralPath $f -PathType Leaf) -and -not ((Get-Item -LiteralPath $f -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
        if (-not $DryRun) {
          Remove-Item -LiteralPath $f -Force
          $stop = Join-Path $kb0 $parts[0]; $d = Split-Path -Parent $f
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
$vm = Join-Path $KH 'claude-kit\tools\vault-mode.py'
if (-not $DryRun -and (Test-Path -LiteralPath $vm)) {
  $mpy = $null
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $mpy = $cmd.Source; break } } catch { } } }
  if ($mpy) { $prevCfgM = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C; $mo = (& $mpy -I $vm migrate --config $C 2>&1 | Out-String).Trim(); $env:CLAUDE_CONFIG_DIR = $prevCfgM; if (-not $prevCfgM) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }; if ($mo) { $migrateOut = $mo }
    if ($KH -ne $C) {   # ONE FOLDER: the 3 thin stub skills + where.py + the pointer file in $C (an old full copy is replaced, anything of yours in it is backed up first); hooks of an old install are re-pointed
      $pCfg2 = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
      $ea0 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
      $so = (& $mpy -I $vm stubs --config $C --quiet 2>&1 | Out-String).Trim(); if ($so) { Write-Output $so }
      $sj = Join-Path $C 'settings.json'
      if (Test-Path -LiteralPath $sj) {
        $sjt = [IO.File]::ReadAllText($sj)
        $mhp = Join-Path $KH 'claude-kit\tools\mentor-hook.py'; $lmp = Join-Path $KH 'claude-kit\vault-mode\.claude\skills\rbx-low-usage\scripts\lum.py'
        if (($sjt -match 'claude-kit/tools/mentor-hook') -and (Test-Path -LiteralPath $mhp)) { (& $mpy -I $mhp install-hooks --config $C 2>&1 | Out-String) -split "`r?`n" | Where-Object { $_ -match 'path updated' } | ForEach-Object { Write-Output $_ } }
        if (($sjt -match 'rbx-low-usage/scripts/lum') -and (Test-Path -LiteralPath $lmp)) { (& $mpy -I $lmp install-hooks --config $C 2>&1 | Out-String) -split "`r?`n" | Where-Object { $_ -match 'hooks: installed' } | ForEach-Object { Write-Output $_ } }
      }
      $ErrorActionPreference = $ea0
      $env:CLAUDE_CONFIG_DIR = $pCfg2; if (-not $pCfg2) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    } }
  elseif (Test-Path -LiteralPath $preMode) { $migrateOut = 'vault-mode: no working Python 3, so the old always-on kit skills were not moved; install Python 3 and run /rbx-update' }
}
# the vault folder is THE loaded environment: resolve it (the clone that holds this claude-kit folder, $env:CLAUDES_VAULT, the registered one, ~\Obsidian\claudes-vault) and load it quietly (env CLAUDE_KIT_NOLOAD=1: the caller, kit-refresh, does it)
$loadOut = ''
$kitVm = Join-Path $Kit 'tools\vault-mode.py'
if (Test-Path -LiteralPath $kitVm) {
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) {
    $prevCfgH = $env:CLAUDE_CONFIG_DIR; $prevKh = $env:CLAUDE_KIT_HOME; $env:CLAUDE_CONFIG_DIR = $C; $env:CLAUDE_KIT_HOME = $KitHome
    $ea1 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    if (-not $vh) { $vh = [string]((& $cmd.Source -I $kitVm home --kit $Kit --config $C 2>$null | Out-String).Trim() -split "`r?`n" | Select-Object -Last 1) }
    if ($vh -and -not $DryRun -and $env:CLAUDE_KIT_NOLOAD -ne '1' -and (Test-Path -LiteralPath $vm)) {
      $la = @('-I', $vm, 'load', '--project', $vh, '--quiet', '--config', $C); if (-not $firstWf) { $la += '--announce' }
      $loadOut = (& $cmd.Source @la 2>&1 | Out-String).Trim()
    }
    $ErrorActionPreference = $ea1
    $env:CLAUDE_CONFIG_DIR = $prevCfgH; if (-not $prevCfgH) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    $env:CLAUDE_KIT_HOME = $prevKh; if (-not $prevKh) { Remove-Item Env:\CLAUDE_KIT_HOME -ErrorAction SilentlyContinue }
    break } } catch { } } }
}
Write-Output ("claude-kit: installed $nNew new, updated $nUpd, unchanged $nSame" + $(if ($nGone) { ", removed $nGone no longer in the kit" }) + $(if ($nFail) { ", FAILED $nFail" }) + " (into $KH)")
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
  $lum = Join-Path $KH 'claude-kit\vault-mode\.claude\skills\rbx-low-usage\scripts\lum.py'
  if (-not $py) { Write-Output 'rbx-low-usage hooks: skipped (no working Python 3)' }
  elseif ($DryRun) { Write-Output 'rbx-low-usage hooks: dry run, settings.json not touched' }
  elseif (-not (Test-Path -LiteralPath $lum)) { Write-Output 'rbx-low-usage hooks: skipped (skill not installed)' }
  else { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $lum $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
  # rbx-mentor suggestion hook (UserPromptSubmit; same opt-in flags, backup first, idempotent)
  $mh = Join-Path $KH 'claude-kit\tools\mentor-hook.py'
  if ($py -and -not $DryRun -and (Test-Path -LiteralPath $mh)) { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $mh $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
}
# similar user skills (other names) -> listed; the kit wins at routing time (precedence line in the kit entry points)
$sim = Join-Path $Kit 'tools\similar-skills.py'
if ((Test-Path -LiteralPath $sim)) {
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { $o = (& $cmd.Source -I $sim --kit $Kit --config $C 2>$null | Out-String).Trim(); if ($LASTEXITCODE -eq 0) { if ($o) { Write-Output $o }; break } } catch { } } }
}
# kit mods (Claude Code plugins: /rbx-subagent-hud agent sidebar, /rbx-graph vault graph link): tools\kit-mods.py, PROJECT scope of the vault folder (see the header). ON BY DEFAULT (opt out: -NoMods).
# Never fails the install: any problem prints ONE "Mods skipped: <reason>. Run again later: <command>" line. State file claude-kit\state\mods-choice: "on" after a successful install, "off" after -NoMods. Mods installed once and later removed with /plugin are NOT brought back by updates (-WithMods forces).
# Legacy plugin names (workflow-hud, vault-graph, hud-rbxdev-vault, graph-rbxdev-vault) are uninstalled on every run that can list plugins; user-scope copies of the two mods are migrated to the vault folder.
$sd = Join-Path $KH 'claude-kit\state'
$inst = Join-Path $Kit 'install.ps1'; if ($vh) { $vi = Join-Path $vh 'claude-kit\install.ps1'; if (Test-Path -LiteralPath $vi) { $inst = $vi } }   # a path that survives (the installer may run from a temporary clone of the kit repository)
$mCmd = 'powershell -NoProfile -ExecutionPolicy Bypass -File "' + $inst + '" -WithMods'
$mOff = 'powershell -NoProfile -ExecutionPolicy Bypass -File "' + $inst + '" -NoMods'
$kpy = $null
foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $kpy = $cmd.Source; break } } catch { } } }
$mbF = Join-Path $sd 'mods-block.txt'
Remove-Item -LiteralPath $mbF -Force -ErrorAction SilentlyContinue
$mb = ''
if ($kpy -and (Test-Path -LiteralPath (Join-Path $Kit 'tools\kit-mods.py'))) {
  $ka = @('-I', (Join-Path $Kit 'tools\kit-mods.py'), '--kit', $Kit, '--config', $C, '--on-cmd', $mCmd.Replace('"', '\"'), '--off-cmd', $mOff.Replace('"', '\"'))
  if ($vh) { $ka += @('--vault', $vh) }
  if ($DryRun) { $ka += '--dry-run' }
  if ($NoMods) { $ka += '--no-mods' }
  if ($WithMods -and -not $NoMods) { $ka += '--with-mods' }
  $ea2 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  $mo2 = (& $kpy @ka 2>&1 | Out-String).Trim(); $ErrorActionPreference = $ea2
  if ($mo2) { Write-Output $mo2 }
  if (Test-Path -LiteralPath $mbF) { try { $mb = ([IO.File]::ReadAllText($mbF)).Trim() } catch { } }
} else { Write-Output ('Mods skipped: no working Python 3 on this computer. Run again later: ' + $mCmd) }
if (-not $mb) {
  $mb = (@('**THE TWO MODS (NOT INSTALLED)**',
    ('- Skipped: the mods step did not run. Install them: ' + $mCmd + '   then start a new session in the vault folder.')) -join "`n")
}
# the single run also downloads the rest: extra notes repositories, reference screenshots, assets (tools\vault-sync-all.py; fails soft, prints ONE retry line, exits 0)
$assetB = ''
if ((-not $DryRun) -and $vh -and (Test-Path -LiteralPath $vh) -and $env:CLAUDE_KIT_NOFOOTER -ne '1' -and $env:CLAUDE_KIT_NOLOAD -ne '1' -and $env:CLAUDE_KIT_NOSYNC -ne '1') {
  $rcmd = 'powershell -NoProfile -ExecutionPolicy Bypass -File "' + $inst + '"'
  if ($kpy -and (Test-Path -LiteralPath (Join-Path $Kit 'tools\vault-sync-all.py'))) {
    $sa = @('-I', (Join-Path $Kit 'tools\vault-sync-all.py'), '--vault', $vh, '--config', $C, '--retry-cmd', $rcmd.Replace('"', '\"'))
    if (-not $assetsOn) { $sa += '--no-assets' }
    if ($env:CLAUDE_SYNC_BASE) { $sa += @('--base', $env:CLAUDE_SYNC_BASE) }
    if ($env:CLAUDE_SYNC_DRY -eq '1') { $sa += '--dry-run' }
    $ea3 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    & $kpy @sa 2>&1 | ForEach-Object { Write-Output ([string]$_) }
    $ErrorActionPreference = $ea3
    $asF = Join-Path $sd 'assets-status.txt'
    if (Test-Path -LiteralPath $asF) { try { $assetB = ([IO.File]::ReadAllLines($asF) | Select-Object -Skip 1 -First 1); if (([IO.File]::ReadAllLines($asF) | Select-Object -First 1) -eq 'complete') { $assetB = '' } } catch { } }
  } else {
    Write-Output ('Assets incomplete: no working Python 3 on this computer. To finish, install Python 3 and run (resumes): ' + $rcmd)
    $assetB = '- Assets: INCOMPLETE (no working Python 3). Install Python 3, then run this (it resumes): ' + $rcmd
  }
}
if ($vh) { $vsay = $vh } else { $vsay = 'your vault folder (not found on this computer: clone the vault first, see SETUP-FOR-CLAUDE.md, then run this installer again)' }
if ($firstWf -and -not $DryRun) { Write-Output ('The Roblox Dev Mastery Vault kit is installed. Start a new Claude session in ' + $vsay + ' to use it. Always available: /rbx-update /rbx-check /rbx-uninstall. Two mods (agent sidebar, graph view) are enabled for the vault folder only; turn them off with /plugin or -NoMods. More details: MANUAL-READ.md in the vault folder (or https://vault-hhmi60uo.netlify.app/manual). Built and maintained by Roman (GitHub: romangigliotti123-arch)') }
$cbl = New-Object System.Collections.Generic.List[string]
function CBadd($s) { [void]$cbl.Add([string]$s) }
CBadd '**HOW TO START USING**'; CBadd ('- Start a new Claude session in ' + $vsay + '; that folder has everything loaded.'); if ($assetB) { CBadd $assetB }; CBadd ''; CBadd '**HOW TO SEE SKILLS AND AGENTS**'; CBadd '- Type /rbx-list in that session, or / then rbx-. Make your own skill: ask Claude to use /rbx-new-skill.'; CBadd ''; CBadd $mb; CBadd ''; CBadd '**HOW TO MAKE A GAME IDEA**'; CBadd '- /rbx-ideas finds one fresh idea (reply another, build it or plan); /rbx-idea-creator starts from yours.'; CBadd ''; CBadd '**HOW TO BUILD A GAME**'; CBadd '- /rbx-workflow builds a game stage by stage; resume with "I want to work on <game name>".'; CBadd ''; CBadd '**HOW TO UPDATE**'; CBadd '- Type /rbx-update (works from any session, even after you move the vault folder).'; CBadd ''; CBadd '**NOT SURE WHICH SKILL?**'; CBadd '- Just describe what you want; Claude offers the right skill and you reply yes.'; CBadd ''; CBadd 'More details: MANUAL-READ.md in the vault folder (or https://vault-hhmi60uo.netlify.app/manual).'
$cb = ($cbl -join "`n")
if (-not $DryRun -and $vh -and (Test-Path -LiteralPath $vh)) {
  try { [IO.File]::WriteAllText((Join-Path $vh 'START-HERE.md'), $cb + "`n", (New-Object Text.UTF8Encoding $false)) } catch { }
  try { $gx = (& git -C $vh rev-parse --git-path info/exclude 2>$null | Select-Object -First 1); if ($LASTEXITCODE -eq 0 -and $gx) { if (-not [IO.Path]::IsPathRooted($gx)) { $gx = Join-Path $vh $gx }; $cur = ''; if (Test-Path -LiteralPath $gx) { $cur = [IO.File]::ReadAllText($gx) }; if (($cur -split "`r?`n") -notcontains '/START-HERE.md') { [IO.File]::AppendAllText($gx, $(if ($cur -and -not $cur.EndsWith("`n")) { "`n" } else { '' }) + "/START-HERE.md`n") } } } catch { }
}
if ($env:CLAUDE_KIT_NOFOOTER -ne '1') { Write-Output ''; Write-Output '=== COPY THIS TO THE USER EXACTLY, AS THE END OF YOUR FINAL MESSAGE (nothing after it; also saved as START-HERE.md in the vault folder) ==='; Write-Output $cb; Write-Output '=== END OF THE BLOCK TO COPY ===' }
if ($nFail) { exit 1 }
exit 0
