# claude-kit installer for Windows (PowerShell 5.1+). Safe to run again. No questions, no admin, sets nothing global.
#   ON-DEMAND STORE (Roblox dev mode, not read by normal Claude sessions): agents\* -> %USERPROFILE%\.claude\claude-kit\vault-mode\.claude\agents\   skills\* -> ...\vault-mode\.claude\skills\   mode\CLAUDE.md -> ...\vault-mode\CLAUDE.md
#   /load-rbxdev-vault copies the store's skills+agents into the CURRENT PROJECT's .claude\ (tools\vault-mode.py); /unload-rbxdev-vault removes exactly those copies.
#   ALWAYS-ON (the only kit skills in %USERPROFILE%\.claude\skills, listed in mode\always-on.txt): load-rbxdev-vault unload-rbxdev-vault update-rbxdev-vault update-check-rbxdev-vault uninstall-rbxdev-vault
#   tools\* -> %USERPROFILE%\.claude\claude-kit\tools\  systems\* -> %USERPROFILE%\.claude\claude-kit\systems\  skillpack\* -> ...\claude-kit\skillpack\ (NOT skills: opened on demand by the /rbx router skill)
# An older install (kit skills/agents directly in .claude\skills and \agents) is migrated by tools\vault-mode.py migrate: kit files move to a backup folder, your own skills/agents/CLAUDE.md are untouched, idempotent, reversible.
# Kit wins: a target file the user changed is replaced by the kit version, no question. The user's version is first copied to %USERPROFILE%\.claude\claude-kit\backup\<date>\<relpath>, so nothing is lost.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 [-KitHome <dir>] [-DryRun] [-WithHooks | -RemoveHooks] [-WithMods]
# -WithMods (opt-in): also install the /hud-rbxdev-vault and /graph-rbxdev-vault Claude Code plugins (plugins load in every session, so they are no longer installed by default).
# -WithHooks / -RemoveHooks (opt-in, never automatic): merge into / remove from %USERPROFILE%\.claude\settings.json the two /low-usage-mode-rbxdev-vault hooks and the mentor-rbxdev-vault suggestion hook (UserPromptSubmit) (backup first, idempotent, keeps all other settings).
param([string]$KitHome = $(if ($env:CLAUDE_KIT_HOME) { $env:CLAUDE_KIT_HOME } else { $env:USERPROFILE }), [switch]$DryRun, [switch]$WithHooks, [switch]$RemoveHooks, [switch]$WithMods)
$ErrorActionPreference = 'Stop'
$Kit = Split-Path -Parent $MyInvocation.MyCommand.Path
$C = Join-Path $KitHome '.claude'
$Man = Join-Path $C 'claude-kit\installed.tsv'
function Sha([string]$p) { (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToLower() }

$SM = 'claude-kit/vault-mode'
$ao = @('load-rbxdev-vault', 'unload-rbxdev-vault', 'update-rbxdev-vault', 'update-check-rbxdev-vault', 'uninstall-rbxdev-vault')
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
$nNew = 0; $nUpd = 0; $nSame = 0; $nRepl = 0
$bkRoot = Join-Path $C ('claude-kit\backup\' + (Get-Date -Format 'yyyy-MM-dd'))

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
    $env:CLAUDE_CONFIG_DIR = $prevCfgR; if (-not $prevCfgR) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    if ($renameMsg -match 'commands renamed') { $renamed = $true }
  } else { Write-Output 'kit-rename: no working Python 3, so old command names were not migrated; install Python 3 and run the update again' }
}

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
    $ns = Sha $_.FullName; $rec = $ns
    if (-not (Test-Path -LiteralPath $dst)) {
      if (-not $DryRun) { New-Item -ItemType Directory -Force (Split-Path -Parent $dst) | Out-Null; Copy-Item -LiteralPath $_.FullName -Destination $dst }
      $nNew++
    } elseif ((Sha $dst) -eq $ns) {
      $nSame++
    } elseif ($old.ContainsKey($rel) -and (Sha $dst) -eq $old[$rel]) {
      if (-not $DryRun) { Copy-Item -LiteralPath $_.FullName -Destination $dst -Force }
      $nUpd++
    } else {
      if (-not $DryRun) {
        $bk = Join-Path $bkRoot ($rel.Replace('/', '\')); $i = 1
        while (Test-Path -LiteralPath $bk) { $i++; $bk = (Join-Path $bkRoot ($rel.Replace('/', '\'))) + ".$i" }
        New-Item -ItemType Directory -Force (Split-Path -Parent $bk) | Out-Null
        Copy-Item -LiteralPath $dst -Destination $bk
        Copy-Item -LiteralPath $_.FullName -Destination $dst -Force
      }
      $nRepl++
    }
    if ($rec) { $new.Add("$rel`t$rec") }
  }
}
if (-not $DryRun) {
  New-Item -ItemType Directory -Force (Split-Path -Parent $Man) | Out-Null
  [IO.File]::WriteAllText($Man, (($new | Sort-Object -Unique) -join "`n") + "`n", (New-Object Text.UTF8Encoding $false))
}
# move an older always-on layout into the store (idempotent; silent when there is nothing to move)
$vm = Join-Path $C 'claude-kit\tools\vault-mode.py'
if (-not $DryRun -and (Test-Path -LiteralPath $vm)) {
  $mpy = $null
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $mpy = $cmd.Source; break } } catch { } } }
  if ($mpy) { $prevCfgM = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C; $mo = (& $mpy -I $vm migrate --config $C 2>&1 | Out-String).Trim(); $env:CLAUDE_CONFIG_DIR = $prevCfgM; if (-not $prevCfgM) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }; if ($mo) { $migrateOut = $mo } }
  elseif (Test-Path -LiteralPath $preMode) { $migrateOut = 'vault-mode: no working Python 3, so the old always-on kit skills were not moved; install Python 3 and run /update-rbxdev-vault' }
}
if ($renamed -and -not $DryRun -and (Test-Path -LiteralPath $vm)) {
  # folders that have Roblox dev mode loaded: swap the old-named copies for the new-named ones (vault-mode.py sync is idempotent)
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $prevCfgS = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C; $ea1 = $ErrorActionPreference; $ErrorActionPreference = 'Continue'; $so = (& $cmd.Source -I $vm sync --config $C 2>&1 | Out-String).Trim(); $ErrorActionPreference = $ea1; $env:CLAUDE_CONFIG_DIR = $prevCfgS; if (-not $prevCfgS) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }; if ($so) { Write-Output $so }; break } } catch { } } }
}
Write-Output "claude-kit: installed $nNew new, updated $nUpd, unchanged $nSame, replaced-yours $nRepl (into $C)"
if ($renameMsg) { Write-Output $renameMsg }
if ($migrateOut) { Write-Output $migrateOut }
if ($nRepl) { Write-Output "claude-kit: replaced $nRepl of your edited files with the kit version (kit wins); your originals are saved under $bkRoot" }
if ($WithHooks -or $RemoveHooks) {
  $py = $null
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $py = $cmd.Source; break } } catch { } } }
  $lum = Join-Path $C 'claude-kit\vault-mode\.claude\skills\low-usage-mode-rbxdev-vault\scripts\lum.py'
  if (-not $py) { Write-Output 'low-usage-mode-rbxdev-vault hooks: skipped (no working Python 3)' }
  elseif ($DryRun) { Write-Output 'low-usage-mode-rbxdev-vault hooks: dry run, settings.json not touched' }
  elseif (-not (Test-Path -LiteralPath $lum)) { Write-Output 'low-usage-mode-rbxdev-vault hooks: skipped (skill not installed)' }
  else { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $lum $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
  # mentor-rbxdev-vault suggestion hook (UserPromptSubmit; same opt-in flags, backup first, idempotent)
  $mh = Join-Path $C 'claude-kit\tools\mentor-hook.py'
  if ($py -and -not $DryRun -and (Test-Path -LiteralPath $mh)) { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $mh $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
}
# similar user skills (other names) -> listed; the kit wins at routing time (precedence line in the kit entry points)
$sim = Join-Path $Kit 'tools\similar-skills.py'
if ((Test-Path -LiteralPath $sim)) {
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { $o = (& $cmd.Source -I $sim --kit $Kit --config $C 2>$null | Out-String).Trim(); if ($LASTEXITCODE -eq 0) { if ($o) { Write-Output $o }; break } } catch { } } }
}
# kit mods (Claude Code plugins: /hud-rbxdev-vault workflow tree, /graph-rbxdev-vault vault graph) from <vault>/claude-kit/mods. OPT-IN (-WithMods): plugins load in every Claude session. Needs the claude CLI; idempotent (already installed = OK).
$modsDir = Join-Path $Kit 'mods'; $mk = 'roblox-vault-kit-mods'
if ((Test-Path -LiteralPath (Join-Path $modsDir '.claude-plugin\marketplace.json')) -and -not $DryRun -and $WithMods) {
  function ClaudeRun([string]$exe, [string[]]$a) { $ea = $ErrorActionPreference; $ErrorActionPreference = 'Continue'; try { $o = (& $exe @a 2>&1 | Out-String); return @{ code = $LASTEXITCODE; out = $o } } catch { return @{ code = 1; out = $_.Exception.Message } } finally { $ErrorActionPreference = $ea } }
  $cl = Get-Command claude -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($cl) {
    $prevCfg = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
    $ok = $true; $why = ''
    $lst = ClaudeRun $cl.Source @('plugin', 'list', '--json')
    $have = ($lst.code -eq 0) -and ($lst.out -match "hud-rbxdev-vault@$mk") -and ($lst.out -match "graph-rbxdev-vault@$mk")
    # plugins installed under their previous names (before the vault-suffixed rename): uninstall them, refresh the marketplace listing, install the new ones below
    $oldMods = $false
    foreach ($om in 'workflow-hud', 'vault-graph') { if ($lst.out -match "$om@$mk") { [void](ClaudeRun $cl.Source @('plugin', 'uninstall', "$om@$mk")); $oldMods = $true } }  # legacy plugin names
    if ($oldMods) { [void](ClaudeRun $cl.Source @('plugin', 'marketplace', 'update', $mk)) }
    if (-not $have) {
      $r = ClaudeRun $cl.Source @('plugin', 'marketplace', 'add', $modsDir)
      if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = 'marketplace add failed' }
      foreach ($m in 'hud-rbxdev-vault', 'graph-rbxdev-vault') {
        if (-not $ok) { break }
        $r = ClaudeRun $cl.Source @('plugin', 'install', "$m@$mk")
        if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = "install of $m failed" }
      }
    }
    $env:CLAUDE_CONFIG_DIR = $prevCfg; if (-not $prevCfg) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    if ($ok) { Write-Output 'mods: hud-rbxdev-vault (/hud-rbxdev-vault), graph-rbxdev-vault (/graph-rbxdev-vault): installed' }
    else { Write-Output "mods: not installed ($why). In a Claude session run: /plugin marketplace add $modsDir  then  /plugin install hud-rbxdev-vault@$mk  and  /plugin install graph-rbxdev-vault@$mk  then  /reload-plugins" }
  } else {
    Write-Output "mods: claude CLI not found. In a Claude session run: /plugin marketplace add $modsDir  then  /plugin install hud-rbxdev-vault@$mk  and  /plugin install graph-rbxdev-vault@$mk  then  /reload-plugins"
  }
}
if ($firstWf -and -not $DryRun) { Write-Output 'The Roblox Dev Mastery Vault kit is installed and OFF by default, so your other Claude sessions stay clean (nothing from the vault is loaded). In a Roblox project folder start Claude and type /load-rbxdev-vault: that session enters Roblox dev mode (the vault skills, agents, art-direction and visual-QA rules, reference images, learn step) and /unload-rbxdev-vault turns it off again. Always available: /load-rbxdev-vault /unload-rbxdev-vault /update-rbxdev-vault /update-check-rbxdev-vault /uninstall-rbxdev-vault. After /load-rbxdev-vault: /game-idea-rbxdev-vault (one fresh idea) or /game-dev-workflow (idea, rating, plan, build); /make-roblox-game; judgement and your games (kept in the vault under Games/, never overwritten by updates): /game-dev-critic /game-dev-weekly /game-dev-launch-kit /game-dev-harvest /contribute-rbxdev-vault; Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>; looks (a game is never called done without it): /game-dev-art-direction /game-dev-visual-qa; mentor: /mentor-rbxdev-vault; research: /deep-topic-research-rbxdev-vault; manager: /manager-mode-rbxdev-vault; vault: /update-clean-rbxdev-vault /setup-check-rbxdev-vault /light-mode-on-rbxdev-vault /light-mode-off-rbxdev-vault /list-rbxdev-vault; usage: /low-usage-mode-rbxdev-vault. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)' }
if ($env:CLAUDE_KIT_NOFOOTER -ne '1') { Write-Output ''; Write-Output '>>> Type /load-rbxdev-vault in a Roblox project folder to use the kit (then /list-rbxdev-vault shows everything it contains).' }
exit 0
