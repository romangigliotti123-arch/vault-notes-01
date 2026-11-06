# claude-kit installer for Windows (PowerShell 5.1+). Safe to run again. No questions, no admin, sets no environment variables or shell profiles; the two mods (see MODS below) are the one thing that touches your Claude plugin settings.
#   ON-DEMAND STORE (Roblox dev mode, not read by normal Claude sessions): agents\* -> %USERPROFILE%\.claude\claude-kit\vault-mode\.claude\agents\   skills\* -> ...\vault-mode\.claude\skills\   mode\CLAUDE.md -> ...\vault-mode\CLAUDE.md
#   The VAULT FOLDER (the notes clone, e.g. %USERPROFILE%\Obsidian\claudes-vault) is permanently loaded: tools\vault-mode.py load --project <vault> (run here at the end, quietly, and by every update) copies the store's skills+agents+rules into <vault>\.claude\, hidden from git together with Games\ and Models\. Older loaded project folders are cleaned. No load/unload commands exist.
#   COLD AREA: mode\cold\<topic>\* rides the mode\* mapping -> ...\claude-kit\vault-mode\cold\ (installed, refreshed, in installed.tsv, removed by uninstall; never copied into a folder; read with tools\vault-mode.py cold).
#   ALWAYS-ON (the only kit skills in %USERPROFILE%\.claude\skills, listed in mode\always-on.txt): rbx-update rbx-check rbx-uninstall
#   tools\* -> %USERPROFILE%\.claude\claude-kit\tools\  systems\* -> %USERPROFILE%\.claude\claude-kit\systems\  skillpack\* -> ...\claude-kit\skillpack\ (NOT skills: opened on demand by the /rbx router skill)
# An older install (kit skills/agents directly in .claude\skills and \agents) is migrated by tools\vault-mode.py migrate: kit files move to a backup folder, your own skills/agents/CLAUDE.md are untouched, idempotent, reversible.
# The vault owns every file it installs: an install/update overwrites each one with the incoming version and removes files that left the kit (no keep, no conflicts). The only content that is yours is your project's Games/ and Models/ folders and anything outside the vault's own paths; nothing here touches them. claude-kit/state/ holds a few tiny settings (rbx-mockup on/off) that are never deleted.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 [-KitHome <dir>] [-DryRun] [-WithHooks | -RemoveHooks] [-NoMods]
# MODS (default ON, no flag): also installs the /rbx-subagent-hud (agent sidebar) and /rbx-graph (vault graph link) Claude Code plugins from claude-kit\mods. They register hooks and are enabled in the user's .claude plugin settings, so they apply to ALL Claude sessions. -NoMods: do not install them and uninstall them if present (a later update will not bring them back); -WithMods: accepted (old docs), also re-installs them after -NoMods or after you removed them with /plugin. Any problem (no claude CLI, offline, plugins disabled by policy, plugin errors) prints ONE "Mods skipped: <reason>. Run again later: <command>" line and the install still succeeds.
# -WithHooks / -RemoveHooks (opt-in, never automatic): merge into / remove from %USERPROFILE%\.claude\settings.json the two /rbx-low-usage hooks and the rbx-mentor suggestion hook (UserPromptSubmit) (backup first, idempotent, keeps all other settings).
param([string]$KitHome = $(if ($env:CLAUDE_KIT_HOME) { $env:CLAUDE_KIT_HOME } else { $env:USERPROFILE }), [switch]$DryRun, [switch]$WithHooks, [switch]$RemoveHooks, [switch]$WithMods, [switch]$NoMods)
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
# kit mods (Claude Code plugins: /rbx-subagent-hud agent sidebar, /rbx-graph vault graph link) from <vault>\claude-kit\mods. ON BY DEFAULT (opt out: -NoMods). They register hooks and are enabled in the user's .claude plugin settings for ALL sessions; the welcome text and the closing block say so.
# Never fails the install: any problem prints ONE "Mods skipped: <reason>. Run again later: <command>" line. State file claude-kit\state\mods-choice: "on" after a successful install, "off" after -NoMods. Mods installed once and later removed with /plugin are NOT brought back by updates (-WithMods forces).
# Legacy plugin names (workflow-hud, vault-graph, hud-rbxdev-vault, graph-rbxdev-vault) are uninstalled on every run that can list plugins.
$modsDir = Join-Path $Kit 'mods'; $mk = 'roblox-vault-kit-mods'; $mState = ''; $mWhy = ''
$sd = Join-Path $C 'claude-kit\state'; $mchF = Join-Path $sd 'mods-choice'; $mch = ''
if (Test-Path -LiteralPath $mchF) { try { $mch = ([IO.File]::ReadAllText($mchF)).Trim() } catch { } }
$instPath = Join-Path $Kit 'install.ps1'
$mCmd = 'powershell -NoProfile -ExecutionPolicy Bypass -File "' + $instPath + '" -WithMods'
function MSet([string]$v) { if ($DryRun) { return }; try { New-Item -ItemType Directory -Force -Path $sd | Out-Null; [IO.File]::WriteAllText($mchF, $v + "`n") } catch { } }
function MFirst([string]$t) { $l = ($t -split "`r?`n" | Where-Object { $_.Trim() } | Select-Object -First 1); if ($l) { if ($l.Length -gt 120) { $l = $l.Substring(0, 120) }; return $l }; return '' }
function ClaudeRun([string]$exe, [string[]]$a) { $ea = $ErrorActionPreference; $ErrorActionPreference = 'Continue'; try { $o = (& $exe @a 2>&1 | Out-String); return @{ code = $LASTEXITCODE; out = $o } } catch { return @{ code = 1; out = $_.Exception.Message } } finally { $ErrorActionPreference = $ea } }
$modsOn = -not $NoMods; $force = [bool]$WithMods -and $modsOn
try {
  $cl = Get-Command claude -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($DryRun) { $mState = 'skipped'; $mWhy = 'dry run' }
  elseif (-not (Test-Path -LiteralPath (Join-Path $modsDir '.claude-plugin\marketplace.json'))) { $mState = 'skipped'; $mWhy = 'the mods folder is missing from this kit' }
  elseif (-not $cl) {
    $mState = 'skipped'; $mWhy = 'the claude command was not found on this computer'
    if (-not $modsOn) { MSet 'off'; $mWhy = '-NoMods was used' }
  } else {
    $prevCfg = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
    try {
      $lst = ClaudeRun $cl.Source @('plugin', 'list', '--json')
      if ($lst.code -ne 0) { $mState = 'skipped'; $mWhy = 'claude plugin list failed (' + (MFirst $lst.out) + ')' }
      else {
        $leg = $false
        foreach ($om in 'workflow-hud', 'vault-graph', 'hud-rbxdev-vault', 'graph-rbxdev-vault') { if ($lst.out -match ([regex]::Escape($om) + '@' + $mk)) { [void](ClaudeRun $cl.Source @('plugin', 'uninstall', "$om@$mk")); $leg = $true } }  # legacy plugin names
        if ($leg) {
          foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { [void](& $cmd.Source -I (Join-Path $Kit 'tools\kit-rename.py') plugins --drop-legacy --config $C 2>&1); break } } catch { } } }
        }
        if ($leg) { [void](ClaudeRun $cl.Source @('plugin', 'marketplace', 'update', $mk)) }   # a legacy plugin was uninstalled: refresh the marketplace listing before installing the new names
        $have = ($lst.out -match "rbx-subagent-hud@$mk") -and ($lst.out -match "rbx-graph@$mk")
        if (-not $modsOn) {   # opt out: remove the two mods if present
          foreach ($m in 'rbx-subagent-hud', 'rbx-graph') { if ($lst.out -match "$m@$mk") { [void](ClaudeRun $cl.Source @('plugin', 'uninstall', "$m@$mk")) } }
          MSet 'off'; $mState = 'skipped'; $mWhy = '-NoMods was used'
        }
        elseif ((-not $force) -and $mch -eq 'off') { $mState = 'skipped'; $mWhy = 'you turned the mods off earlier' }
        elseif ((-not $force) -and $mch -eq 'on' -and (-not $have) -and (-not $leg)) { $mState = 'skipped'; $mWhy = 'you removed them earlier with /plugin' }
        else {
          $ok = $true; $why = ''
          if (-not $have) {
            $r = ClaudeRun $cl.Source @('plugin', 'marketplace', 'add', $modsDir)
            if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = 'marketplace add failed (' + (MFirst $r.out) + ')' }
            foreach ($m in 'rbx-subagent-hud', 'rbx-graph') {
              if (-not $ok) { break }
              $r = ClaudeRun $cl.Source @('plugin', 'install', "$m@$mk")
              if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = "install of $m failed (" + (MFirst $r.out) + ')' }
            }
          }
          if ($ok) {   # copy semantics: an installed plugin keeps its old copy until updated
            [void](ClaudeRun $cl.Source @('plugin', 'marketplace', 'update', $mk))
            foreach ($m in 'rbx-subagent-hud', 'rbx-graph') { [void](ClaudeRun $cl.Source @('plugin', 'update', "$m@$mk")) }
            MSet 'on'; if ($have) { $mState = 'uptodate' } else { $mState = 'installed' }
          } else { $mState = 'skipped'; $mWhy = $why }
        }
      }
    } finally { $env:CLAUDE_CONFIG_DIR = $prevCfg; if (-not $prevCfg) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue } }
  }
} catch { $mState = 'skipped'; $mWhy = 'the mods step failed (' + $_.Exception.Message + ')' }
if ($mState -eq 'installed') { Write-Output 'Mods installed: rbx-subagent-hud, rbx-graph' }
elseif ($mState -eq 'uptodate') { Write-Output 'Mods up to date: rbx-subagent-hud, rbx-graph' }
else { Write-Output ('Mods skipped: ' + $mWhy + '. Run again later: ' + $mCmd) }
# the closing-block section (printed by the footer below, and read by the sync-setup scripts from claude-kit\state\mods-block.txt)
if ($mState -eq 'installed' -or $mState -eq 'uptodate') {
  $mb = (@('**THE TWO MODS (ALREADY INSTALLED)**',
    ('- Type /reload-plugins once (or start a new session) to activate them. They are Claude Code plugins that add an agent sidebar and a graph view and register hooks; they are enabled in your Claude user settings (' + $C + ') and apply to ALL your Claude sessions, not only the vault folder.'),
    '- /rbx-subagent-hud opens the agent sidebar; /rbx-graph shows the link to the vault graph site.',
    ('- To turn them off: /plugin (disable or uninstall rbx-subagent-hud and rbx-graph), or run the installer with -NoMods: powershell -NoProfile -ExecutionPolicy Bypass -File "' + $instPath + '" -NoMods')) -join "`n")
} else {
  $mb = (@('**THE TWO MODS (NOT INSTALLED)**',
    ('- Skipped: ' + $mWhy + '. The vault works without them. To install them run: ' + $mCmd + '   then type /reload-plugins.'),
    ('- They are Claude Code plugins that add an agent sidebar (/rbx-subagent-hud) and a graph view (/rbx-graph) and register hooks; installing them changes your Claude user settings (' + $C + ') and applies to ALL your Claude sessions. Turn them off any time with /plugin or the installer''s -NoMods.')) -join "`n")
}
if (-not $DryRun) { try { New-Item -ItemType Directory -Force -Path $sd | Out-Null; [IO.File]::WriteAllText((Join-Path $sd 'mods-block.txt'), $mb + "`n") } catch { } }
if ($vh) { $vsay = $vh } else { $vsay = 'your vault folder (not found on this computer: clone the vault first, see SETUP-FOR-CLAUDE.md, then run this installer again)' }
if ($firstWf -and -not $DryRun) { Write-Output ('The Roblox Dev Mastery Vault kit is installed. TO USE THE VAULT: load it by starting a Claude session in ' + $vsay + ' (that folder is the loaded vault: the vault skills, agents, art-direction, placement, lighting and visual-QA rules and reference images are there automatically; no load command is needed; your other Claude sessions stay clean). Always available in every session: /rbx-update /rbx-check /rbx-uninstall. In the vault folder: /rbx-idea-quick (one fresh idea) or /rbx-workflow (idea, rating, plan, build); /rbx-make; judgement and your games (in the Games/ folder of the vault, never touched by updates): /rbx-critic /rbx-weekly /rbx-launch-kit /rbx-harvest; Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>; placement, lighting and looks (a game is never called done without them): /rbx-placement /rbx-lighting /rbx-art /rbx-visual; measure the vault itself: /rbx-bench; mentor: /rbx-mentor; research: /rbx-research; manager: /rbx-manager; vault: /rbx-clean /rbx-setup /rbx-light-on /rbx-light-off /rbx-list; usage: /rbx-low-usage. Two mods (Claude Code plugins that add an agent sidebar and a graph view and register hooks) are part of the kit: they are enabled in your Claude user settings and apply to all your Claude sessions; turn them off with /plugin or run the installer with -NoMods. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)') }
if ($env:CLAUDE_KIT_NOFOOTER -ne '1') { Write-Output ''; Write-Output '**HOW TO START USING**'; Write-Output ('- ' + 'Start a new Claude session in ' + $vsay + ' (Claude app: New, choose that folder; terminal: cd "' + $vsay + '" then claude; Obsidian: Open folder as vault on the same path). That folder loads the whole vault automatically; no load command.'); Write-Output ''; Write-Output '**HOW TO SEE SKILLS AND AGENTS**'; Write-Output '- In that session type /rbx-list (skills, agents, mods), or type / and start typing rbx-. To learn what one skill does, ask "what does /rbx-<name> do".'; Write-Output ''; Write-Output $mb; Write-Output ''; Write-Output '**HOW TO MAKE A GAME IDEA**'; Write-Output '- /rbx-ideas: finds ONE fresh idea based on what is doing best on the charts (single-player or open world). Reply "another" for a different one, "build it" to create the game folder, "plan" for the full plan.'; Write-Output '- /rbx-idea-creator: type it with your own idea to build it up, or on its own and it asks a few quick questions.'; Write-Output ''; Write-Output '**HOW TO BUILD A GAME**'; Write-Output ('- ' + '/rbx-workflow: takes a game from idea to launch one stage at a time. Games live in ' + $vsay + '\Games\<game name>\' + ' (each has a README). In any new session say "I want to work on <game name>" and Claude picks it up. Good reusable models are saved to ' + $vsay + '\Models\' + ' automatically.'); Write-Output ''; Write-Output '**HOW TO UPDATE**'; Write-Output '- Type /rbx-update (works from any session).' }
if ($nFail) { exit 1 }
exit 0
