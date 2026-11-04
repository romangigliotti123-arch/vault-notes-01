#!/usr/bin/env python3
"""setup-check.py: READ-ONLY software check for the whole Roblox Dev Mastery Vault setup (Windows, macOS, Linux). Installs nothing, changes nothing.
Prints a table: tool | needed for | required/optional | found (version/path) | missing -> exact install command for this OS.
Usage: python setup-check.py [--json] [--missing] [--os windows|mac|linux]     (stdlib only, Python 3.8+)
Exit code 0, unless a REQUIRED tool is missing: then 2 (so setup scripts can notice)."""
import argparse, glob, json, os, platform, re, shutil, subprocess, sys

HOME = os.path.expanduser("~")
OS = {"Windows": "windows", "Darwin": "mac"}.get(platform.system(), "linux")
APPDATA = os.environ.get("APPDATA", "")
LOCAL = os.environ.get("LOCALAPPDATA", "")
ROKIT_BIN = [os.path.join(HOME, ".rokit", "bin"), os.path.join(HOME, ".aftman", "bin")]


def pm():
    for m in ("pacman", "apt", "dnf"):
        if shutil.which(m):
            return m
    return "pacman"


def pkg(pacman, apt=None, dnf=None):
    m = pm()
    if m == "pacman":
        return "sudo pacman -S --needed " + pacman
    if m == "apt":
        return "sudo apt install " + (apt or pacman)
    return "sudo dnf install " + (dnf or apt or pacman)


def run(cmd, t=12, cwd=None):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=t, stdin=subprocess.DEVNULL, cwd=cwd)
        return (p.stdout + p.stderr).strip()
    except Exception:
        return None


def which(n, extra=()):
    p = shutil.which(n)
    if p and "WindowsApps" in p and n.startswith("python"):
        p = None
    if p:
        return p
    for d in extra:
        for ext in ("", ".exe", ".cmd", ".bat"):
            c = os.path.join(d, n + ext)
            if os.path.isfile(c):
                return c
    return None


def first_line(s):
    return s.strip().splitlines()[0][:70] if s and s.strip() else ""


def cli(name, flag="--version", extra=()):
    p = which(name, extra)
    if not p:
        return None
    v = first_line(run([p, flag]))
    return "%s  (%s)" % (v or "installed", p)


def studio():
    if OS == "windows":
        for base in (os.path.join(LOCAL, "Roblox", "Versions"), r"C:\Program Files (x86)\Roblox\Versions", r"C:\Program Files\Roblox\Versions"):
            g = glob.glob(os.path.join(base, "*", "RobloxStudioBeta.exe"))
            if g:
                return "installed  (%s)" % os.path.dirname(g[0])
    elif OS == "mac":
        if os.path.isdir("/Applications/RobloxStudio.app"):
            return "installed  (/Applications/RobloxStudio.app)"
    else:
        p = which("vinegar") or which("sober")
        if p:
            return "via Vinegar/Sober  (%s)" % p
        for d in (os.path.join(HOME, ".var/app/org.vinegarhq.Vinegar"), os.path.join(HOME, ".local/share/vinegar")):
            if os.path.exists(d):
                return "via Vinegar  (%s)" % d
    return None


def claude_mcp(name):
    c = which("claude")
    if not c:
        return None
    out = run([c, "mcp", "get", name], 25)
    low = (out or "").lower()
    if out and "no mcp server" not in low and "not found" not in low and "error" not in low[:40]:
        return "registered in Claude Code"
    return None


def studio_mcp():
    r = claude_mcp("Roblox_Studio")
    if OS == "windows":
        bat = os.path.join(LOCAL, "Roblox", "mcp.bat")
        has = os.path.isfile(bat)
        if r:
            return r + ("; mcp.bat present" if has else "; mcp.bat not yet written by Studio")
        if has:
            return "mcp.bat present (%s) but not registered in Claude Code" % bat
    elif OS == "mac":
        if r:
            return r
        if os.path.exists("/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP"):
            return "StudioMCP present but not registered in Claude Code"
    return None


def blender():
    extra = []
    if OS == "windows":
        extra = [os.path.dirname(g) for g in glob.glob(r"C:\Program Files\Blender Foundation\Blender *\blender.exe")]
    elif OS == "mac":
        extra = ["/Applications/Blender.app/Contents/MacOS"]
    p = which("blender", extra)
    if not p:
        return None
    out = run([p, "--version"], 40)
    m = re.search(r"Blender\s+([0-9][0-9.]*)", out or "")
    return "Blender %s  (%s)" % (m.group(1) if m else "?", p)


def blender_mcp():
    roots = {"windows": [os.path.join(APPDATA, "Blender Foundation", "Blender")],
             "mac": [os.path.join(HOME, "Library/Application Support/Blender")],
             "linux": [os.path.join(HOME, ".config/blender")]}[OS]
    for r in roots:
        for g in glob.glob(os.path.join(r, "*", "scripts", "addons", "*")) + glob.glob(os.path.join(r, "*", "extensions", "*", "*")):
            if "mcp" in os.path.basename(g).lower():
                return "addon found  (%s)" % g
    r = claude_mcp("blender")
    if r:
        return r + " (server entry only; also enable the addon in Blender)"
    return None


def obsidian():
    cands = {"windows": [os.path.join(LOCAL, "Obsidian", "Obsidian.exe"), r"C:\Program Files\Obsidian\Obsidian.exe"],
             "mac": ["/Applications/Obsidian.app"],
             "linux": ["/usr/bin/obsidian", "/opt/Obsidian/obsidian", os.path.join(HOME, ".var/app/md.obsidian.Obsidian")]}[OS]
    for c in cands:
        if os.path.exists(c):
            return "installed  (%s)" % c
    p = which("obsidian")
    return "installed  (%s)" % p if p else None


def python_row():
    v = "Python %s  (%s)" % (platform.python_version(), sys.executable)
    return v if sys.version_info >= (3, 8) else v + " (too old: need 3.8+)"


def pip_row():
    out = run([sys.executable, "-m", "pip", "--version"])
    return first_line(out) if out and out.lower().startswith("pip ") else None


def node_row():
    n = cli("node")
    if not n:
        return None
    return n + " + npm " + (first_line(run([which("npm") or "npm", "--version"])) or "missing")


def tailscale():
    ex = [r"C:\Program Files\Tailscale"] if OS == "windows" else ["/Applications/Tailscale.app/Contents/MacOS"]
    return cli("tailscale", "version", ex)


def sysdir():
    here = os.path.dirname(os.path.abspath(__file__))
    for c in (os.path.join(here, "..", "systems"), os.path.join(here, "roblox-project-template"), os.path.join(here, "..", "..", "claude-kit", "systems")):
        if os.path.isfile(os.path.join(c, "rokit.toml")):
            return os.path.abspath(c)
    return None


def rk(tool):
    # Rokit shims only work inside a folder with a rokit.toml: run them there; an error means the tool is not installed for it.
    def f():
        p = which(tool, ROKIT_BIN)
        if not p:
            return None
        out = re.sub(r"\x1b\[[0-9;]*m", "", run([p, "--version"], 15, sysdir()) or "")
        if not out or "ERROR" in out or "Failed" in out:
            return None
        return "%s  (%s)" % (first_line(out), p)
    return f


def inst(win, mac, lin):
    return {"windows": win, "mac": mac, "linux": lin}


KIT_CMD = "rokit install --no-trust-check   (run inside ~/.claude/claude-kit/systems)"
KIT_TOOL = inst(KIT_CMD, KIT_CMD, KIT_CMD)
BL_MCP = ("uvx mcp-for-blender install-addon ; in Blender enable 'Interface: MCP for Blender' ; "
          "claude mcp add blender uvx mcp-for-blender")


def table():
    return [
        ("git", "clone and update the vault", True, lambda: cli("git"),
         inst("winget install --id Git.Git -e", "brew install git", pkg("git"))),
        ("Python 3", "all kit tools (kbq, vault-find, assets-sync, skillpack, checks)", True, python_row,
         inst("winget install --id Python.Python.3.12 -e", "brew install python", pkg("python", "python3", "python3"))),
        ("pip", "optional Python packages", False, pip_row,
         inst("py -3 -m ensurepip --upgrade", "python3 -m ensurepip --upgrade", pkg("python-pip", "python3-pip", "python3-pip"))),
        ("Claude Code", "runs the kit skills and agents", True, lambda: cli("claude"),
         inst("irm https://claude.ai/install.ps1 | iex", "curl -fsSL https://claude.ai/install.sh | bash",
              "curl -fsSL https://claude.ai/install.sh | bash")),
        ("Node.js / npm", "nothing in the kit; only some third-party MCP servers", False, node_row,
         inst("winget install --id OpenJS.NodeJS.LTS -e", "brew install node", pkg("nodejs npm", "nodejs npm", "nodejs npm"))),
        ("uv / uvx", "Blender MCP (uvx mcp-for-blender)", False, lambda: cli("uvx"),
         inst("winget install --id astral-sh.uv -e", "brew install uv", "curl -LsSf https://astral.sh/uv/install.sh | sh   (or: " + pkg("uv") + ")")),
        ("Obsidian", "browse the vault (Claude does not need it)", False, obsidian,
         inst("winget install --id Obsidian.Obsidian -e", "brew install --cask obsidian",
              "flatpak install flathub md.obsidian.Obsidian   (or: " + pkg("obsidian") + ")")),
        ("Roblox Studio", "run and test games live (not needed for writing code)", False, studio,
         inst("Install from https://create.roblox.com/landing (you sign in yourself)",
              "Install from https://create.roblox.com/landing (you sign in yourself)",
              "Studio is not native on Linux. Community runners: Vinegar (https://vinegarhq.org) or Sober (https://sober.vinegarhq.org). Rojo and the static checks work without it")),
        ("Roblox Studio MCP (built-in, first choice)", "Claude reads/runs/playtests in the open Studio; built-in server of Studio (docs create.roblox.com/docs/studio/mcp), the older Rust server is only a fallback", False, studio_mcp,
         inst("In Studio enable Assistant > Manage MCP Servers, then run tools\\studio-setup.ps1 (registers: claude mcp add --scope user Roblox_Studio -- cmd.exe /c %LOCALAPPDATA%\\Roblox\\mcp.bat)",
              "bash ~/.claude/claude-kit/tools/studio-setup.sh   (registers: claude mcp add --scope user Roblox_Studio -- /Applications/RobloxStudio.app/Contents/MacOS/StudioMCP)",
              "n/a on Linux (no native Studio)")),
        ("Rokit", "installs Rojo, Selene, StyLua, luau-lsp, Lune at pinned versions", False, rk("rokit"),
         inst("Download the Windows build from https://github.com/rojo-rbx/rokit/releases, run 'rokit self-install', open a new terminal",
              "brew install rokit",
              "Download the Linux build from https://github.com/rojo-rbx/rokit/releases, run './rokit self-install', open a new terminal")),
        ("Rojo", "sync files to Studio, build places", False, rk("rojo"), KIT_TOOL),
        ("StyLua", "Luau formatter (static checks)", False, rk("stylua"), KIT_TOOL),
        ("Selene", "Luau linter (static checks)", False, rk("selene"), KIT_TOOL),
        ("luau-lsp", "Luau type check (static checks)", False, rk("luau-lsp"), KIT_TOOL),
        ("Lune", "run Luau scripts outside Studio (systems checks)", False, rk("lune"), KIT_TOOL),
        ("Wally", "Roblox package manager (only if a project uses packages)", False, rk("wally"),
         inst(*(["rokit add --global UpliftGames/wally"] * 3))),
        ("Blender", "Blender-to-Roblox asset pipeline notes and scripts", False, blender,
         inst("winget install --id BlenderFoundation.Blender -e", "brew install --cask blender", pkg("blender"))),
        ("Blender MCP", "Claude drives Blender (community addon mcp-for-blender; Blender 3.0+, needs uv)", False, blender_mcp,
         inst(BL_MCP, BL_MCP, BL_MCP)),
        ("ffmpeg", "rbx-research video frames", False, lambda: cli("ffmpeg", "-version"),
         inst("winget install --id Gyan.FFmpeg -e", "brew install ffmpeg", pkg("ffmpeg"))),
        ("yt-dlp", "rbx-research YouTube transcripts", False, lambda: cli("yt-dlp"),
         inst("winget install --id yt-dlp.yt-dlp -e", "brew install yt-dlp", pkg("yt-dlp"))),
        ("GitHub CLI (gh)", "GitHub rate limits, GitHub login for the vault", False, lambda: cli("gh"),
         inst("winget install --id GitHub.cli -e", "brew install gh", pkg("github-cli", "gh", "gh"))),
        ("Tailscale", "only for the owner's private share (not needed: vault and assets come from GitHub)", False, tailscale,
         inst("winget install --id Tailscale.Tailscale -e", "brew install --cask tailscale",
              "curl -fsSL https://tailscale.com/install.sh | sh   (or: " + pkg("tailscale") + ")")),
    ]


def main():
    global OS
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--missing", action="store_true", help="only list missing tools")
    ap.add_argument("--os", choices=["windows", "mac", "linux"], help="show install commands for this OS (detection still uses this machine)")
    a = ap.parse_args()
    if a.os:
        OS = a.os
    rows = []
    for name, need, req, det, ins in table():
        try:
            found = det()
        except Exception:
            found = None
        rows.append({"tool": name, "needed_for": need, "level": "REQUIRED" if req else "optional", "found": found,
                     "install": None if found else ins[OS]})
    bad = [r["tool"] for r in rows if not r["found"] and r["level"] == "REQUIRED"]
    if a.json:
        print(json.dumps({"os": OS, "rows": rows}, indent=1))
    else:
        print("Setup check on %s (read-only: nothing is installed or changed)\n" % platform.platform())
        print("| tool | needed for | level | found | if missing: install command |")
        print("|---|---|---|---|---|")
        for r in rows:
            if a.missing and r["found"]:
                continue
            print("| %s | %s | %s | %s | %s |" % (r["tool"], r["needed_for"], r["level"],
                                                   ("OK: " + r["found"]) if r["found"] else "MISSING", r["install"] or ""))
        opt = [r["tool"] for r in rows if not r["found"] and r["level"] != "REQUIRED"]
        print("\nREQUIRED missing: %s" % (", ".join(bad) or "none"))
        print("optional missing: %s" % (", ".join(opt) or "none"))
        print("Nothing was installed. Claude runs an install command only after your yes.")
    sys.exit(2 if bad else 0)


if __name__ == "__main__":
    main()
