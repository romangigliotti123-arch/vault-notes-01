# claude-kit installer for Windows (PowerShell 5.1+). Safe to run again. No questions, no admin, sets nothing global.
#   agents\*  -> %USERPROFILE%\.claude\agents\     skills\*  -> %USERPROFILE%\.claude\skills\     tools\* -> %USERPROFILE%\.claude\claude-kit\tools\  systems\* -> %USERPROFILE%\.claude\claude-kit\systems\
# Kit wins: a target file the user changed is replaced by the kit version, no question. The user's version is first copied to %USERPROFILE%\.claude\claude-kit\backup\<date>\<relpath>, so nothing is lost.
# User skills with other names are never touched or removed; similar ones are listed ("kit versions will be used") and the kit entry points say the kit skill wins at routing time.
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 [-KitHome <dir>] [-DryRun] [-WithHooks | -RemoveHooks]
# -WithHooks / -RemoveHooks (opt-in, never automatic): merge into / remove from %USERPROFILE%\.claude\settings.json the two /low-usage-mode hooks and the vault-mentor suggestion hook (UserPromptSubmit) (backup first, idempotent, keeps all other settings).
param([string]$KitHome = $(if ($env:CLAUDE_KIT_HOME) { $env:CLAUDE_KIT_HOME } else { $env:USERPROFILE }), [switch]$DryRun, [switch]$WithHooks, [switch]$RemoveHooks)
$ErrorActionPreference = 'Stop'
$Kit = Split-Path -Parent $MyInvocation.MyCommand.Path
$C = Join-Path $KitHome '.claude'
$Man = Join-Path $C 'claude-kit\installed.tsv'
function Sha([string]$p) { (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToLower() }

$old = @{}
if (Test-Path -LiteralPath $Man) {
  foreach ($l in [IO.File]::ReadAllLines($Man)) { $p = $l -split "`t"; if ($p.Count -ge 2) { $old[$p[0]] = $p[1] } }
}
$new = New-Object System.Collections.Generic.List[string]
$nNew = 0; $nUpd = 0; $nSame = 0; $nRepl = 0; $firstWf = $false
$bkRoot = Join-Path $C ('claude-kit\backup\' + (Get-Date -Format 'yyyy-MM-dd'))

foreach ($sub in 'agents', 'skills', 'tools', 'systems', 'skillpack') {
  $root = Join-Path $Kit $sub
  if (-not (Test-Path -LiteralPath $root)) { continue }
  Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object { $_.FullName -notmatch '\\__pycache__\\' -and $_.Extension -ne '.pyc' } | Sort-Object FullName | ForEach-Object {
    $r = $_.FullName.Substring($Kit.Length + 1).Replace('\', '/')
    $rel = if ($sub -eq 'tools' -or $sub -eq 'systems' -or $sub -eq 'skillpack') { "claude-kit/$r" } else { $r }
    $dst = Join-Path $C ($rel.Replace('/', '\'))
    $ns = Sha $_.FullName; $rec = $ns
    if (-not (Test-Path -LiteralPath $dst)) {
      if ($rel -eq 'skills/game-dev-workflow/SKILL.md') { $firstWf = $true }
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
Write-Output "claude-kit: installed $nNew new, updated $nUpd, unchanged $nSame, replaced-yours $nRepl (into $C)"
if ($nRepl) { Write-Output "claude-kit: replaced $nRepl of your edited files with the kit version (kit wins); your originals are saved under $bkRoot" }
if ($WithHooks -or $RemoveHooks) {
  $py = $null
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { & $cmd.Source -c 'import sys' 2>$null | Out-Null; if ($LASTEXITCODE -eq 0) { $py = $cmd.Source; break } } catch { } } }
  $lum = Join-Path $C 'skills\low-usage-mode\scripts\lum.py'
  if (-not $py) { Write-Output 'low-usage-mode hooks: skipped (no working Python 3)' }
  elseif ($DryRun) { Write-Output 'low-usage-mode hooks: dry run, settings.json not touched' }
  elseif (-not (Test-Path -LiteralPath $lum)) { Write-Output 'low-usage-mode hooks: skipped (skill not installed)' }
  else { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $lum $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
  # vault-mentor suggestion hook (UserPromptSubmit; same opt-in flags, backup first, idempotent)
  $mh = Join-Path $C 'claude-kit\tools\mentor-hook.py'
  if ($py -and -not $DryRun -and (Test-Path -LiteralPath $mh)) { $env:CLAUDE_CONFIG_DIR = $C; & $py -I $mh $(if ($RemoveHooks) { 'uninstall-hooks' } else { 'install-hooks' }) --config $C }
}
# similar user skills (other names) -> listed; the kit wins at routing time (precedence line in the kit entry points)
$sim = Join-Path $Kit 'tools\similar-skills.py'
if ((Test-Path -LiteralPath $sim)) {
  foreach ($n in 'python3', 'python', 'py') { $cmd = Get-Command $n -ErrorAction SilentlyContinue; if ($cmd -and $cmd.Source -notmatch 'WindowsApps') { try { $o = (& $cmd.Source -I $sim --kit $Kit --config $C 2>$null | Out-String).Trim(); if ($LASTEXITCODE -eq 0) { if ($o) { Write-Output $o }; break } } catch { } } }
}
# kit mods (Claude Code plugins: /hud workflow tree, /graph vault graph) from <vault>/claude-kit/mods. Needs the claude CLI; idempotent (already installed = OK).
$modsDir = Join-Path $Kit 'mods'; $mk = 'roblox-vault-kit-mods'
if ((Test-Path -LiteralPath (Join-Path $modsDir '.claude-plugin\marketplace.json')) -and -not $DryRun) {
  function ClaudeRun([string]$exe, [string[]]$a) { $ea = $ErrorActionPreference; $ErrorActionPreference = 'Continue'; try { $o = (& $exe @a 2>&1 | Out-String); return @{ code = $LASTEXITCODE; out = $o } } catch { return @{ code = 1; out = $_.Exception.Message } } finally { $ErrorActionPreference = $ea } }
  $cl = Get-Command claude -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($cl) {
    $prevCfg = $env:CLAUDE_CONFIG_DIR; $env:CLAUDE_CONFIG_DIR = $C
    $ok = $true; $why = ''
    $lst = ClaudeRun $cl.Source @('plugin', 'list', '--json')
    $have = ($lst.code -eq 0) -and ($lst.out -match "workflow-hud@$mk") -and ($lst.out -match "vault-graph@$mk")
    if (-not $have) {
      $r = ClaudeRun $cl.Source @('plugin', 'marketplace', 'add', $modsDir)
      if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = 'marketplace add failed' }
      foreach ($m in 'workflow-hud', 'vault-graph') {
        if (-not $ok) { break }
        $r = ClaudeRun $cl.Source @('plugin', 'install', "$m@$mk")
        if ($r.code -ne 0 -and $r.out -notmatch 'already') { $ok = $false; $why = "install of $m failed" }
      }
    }
    $env:CLAUDE_CONFIG_DIR = $prevCfg; if (-not $prevCfg) { Remove-Item Env:\CLAUDE_CONFIG_DIR -ErrorAction SilentlyContinue }
    if ($ok) { Write-Output 'mods: workflow-hud (/hud), vault-graph (/graph): installed' }
    else { Write-Output "mods: not installed ($why). In a Claude session run: /plugin marketplace add $modsDir  then  /plugin install workflow-hud@$mk  and  /plugin install vault-graph@$mk  then  /reload-plugins" }
  } else {
    Write-Output "mods: claude CLI not found. In a Claude session run: /plugin marketplace add $modsDir  then  /plugin install workflow-hud@$mk  and  /plugin install vault-graph@$mk  then  /reload-plugins"
  }
}
if ($firstWf -and -not $DryRun) { Write-Output 'The Roblox Dev Mastery Vault is now set up. Start a new Claude session and run /game-idea (one fresh idea) or /game-dev-workflow (idea, rating, plan, build). Judgement and your games (kept in the vault under Games/, never overwritten by updates): /game-dev-critic /game-dev-weekly /game-dev-launch-kit /game-dev-harvest /vault-contribute. Roblox skill pack (300+ focused skills, zero context until used): /rbx list, /rbx find <words>, /rbx <name>. Side skills: /game-dev-rate /game-dev-plan /game-dev-ads /game-dev-update /game-dev-playtest /game-dev-thumbnail; looks (a game is never called done without it): /game-dev-art-direction /game-dev-visual-qa; mentor (start here): /vault-mentor (works with you on any job and suggests the right skill, agent or note at each step); research: /deep-topic-research; find skills and agents: /use-the-ai-library; manager: /manager-mode; vault: /vault-update /vault-update-clean /update-check (newer version? changes nothing) /setup-check (missing software + install commands) /light-mode-on /light-mode-off; usage: /low-usage-mode. How it works: the vault Roblox knowledge base feeds the agents; /game-dev-workflow elaborates, rates and plans your idea, then builds it after you say Ready to build. Full list: README.md. Built and maintained by Roman (GitHub: romangigliotti123-arch)' }
if ($env:CLAUDE_KIT_NOFOOTER -ne '1') { Write-Output ''; Write-Output '>>> Use /kit-list to see all the new installed skills, agents and mods (one line each).' }
exit 0
