#!/usr/bin/env python3
"""doctor: report which tools deep-topic-research can use and exactly how to install the missing ones.
Never installs anything. Usage: python3 doctor.py [--net] [--json]"""
import json, platform, shutil, sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from common import run, tool_cmd, http_get  # noqa: E402

OS = {"Windows": "win", "Darwin": "mac"}.get(platform.system(), "linux")

HOW = {
    "yt-dlp": {"win": "winget install yt-dlp.yt-dlp   (or: py -m pip install -U yt-dlp)",
               "mac": "brew install yt-dlp   (or: python3 -m pip install -U yt-dlp)",
               "linux": "python3 -m pip install -U yt-dlp   (or your package manager: apt/dnf/pacman install yt-dlp)"},
    "ffmpeg": {"win": "winget install Gyan.FFmpeg", "mac": "brew install ffmpeg",
               "linux": "sudo apt install ffmpeg   (or dnf/pacman install ffmpeg)"},
    "gh": {"win": "winget install GitHub.cli   then: gh auth login", "mac": "brew install gh   then: gh auth login",
           "linux": "see https://cli.github.com/ (apt/dnf/pacman install gh)   then: gh auth login"},
    "python": {"win": "winget install Python.Python.3.12", "mac": "brew install python", "linux": "sudo apt install python3"},
    "claude": {"win": "see https://docs.claude.com/en/docs/claude-code (install Claude Code)",
               "mac": "see https://docs.claude.com/en/docs/claude-code", "linux": "see https://docs.claude.com/en/docs/claude-code"},
    "faster-whisper": {"win": "py -m pip install faster-whisper", "mac": "python3 -m pip install faster-whisper",
                       "linux": "python3 -m pip install faster-whisper"},
}


def ver(cmd, flag="--version"):
    r = run(cmd + [flag], timeout=30)
    return (r.stdout or r.stderr).strip().splitlines()[0][:60] if r.returncode == 0 and (r.stdout or r.stderr).strip() else ""


def main():
    rows = []  # name, status, detail, needed_for, required
    pv = sys.version_info
    rows.append(("python", pv >= (3, 8), f"{pv.major}.{pv.minor}.{pv.micro}", "all scripts", True))
    yt = tool_cmd("yt-dlp")
    rows.append(("yt-dlp", bool(yt), ver(yt) if yt else "", "YouTube search, listing, transcripts", False))
    rows.append(("ffmpeg", bool(shutil.which("ffmpeg")), ver(["ffmpeg"], "-version")[:40] if shutil.which("ffmpeg") else "",
                 "visual contact sheets, whisper audio (optional)", False))
    gh = shutil.which("gh")
    auth = ""
    if gh:
        auth = "logged in" if run([gh, "auth", "status"], timeout=30).returncode == 0 else "NOT logged in (run: gh auth login; 60 req/h anonymous fallback works)"
    rows.append(("gh", bool(gh), (ver([gh]) + " " + auth).strip() if gh else "", "GitHub search with a good rate limit (optional; anonymous REST fallback exists)", False))
    cl = tool_cmd("claude")
    rows.append(("claude", bool(cl), ver(cl) if cl else "", "headless worker pool for extraction/synthesis (else subagent mode)", False))
    try:
        import faster_whisper  # noqa: F401
        fw = True
    except Exception:
        fw = False
    rows.append(("faster-whisper", fw, "installed" if fw else "", "local transcription fallback when a video has no captions (optional, needs your OK)", False))

    if "--json" in sys.argv:
        print(json.dumps([{"name": n, "ok": ok, "detail": d, "for": f, "required": rq,
                           "install": HOW.get(n, {}).get(OS, "")} for n, ok, d, f, rq in rows], indent=1))
    else:
        print(f"deep-topic-research doctor ({platform.system()} {platform.machine()})")
        print(f"  python command to use for every script: {sys.executable}")
        if OS == "win" and "WindowsApps" in (shutil.which("python3") or ""):
            print("  note: `python3` on this PC is the Microsoft Store stub; use the command above (or `py -3`) instead.")
        for n, ok, d, f, rq in rows:
            print(f"  [{'ok' if ok else ('MISSING' if rq else 'missing')}] {n:15s} {d}  -- {f}")
            if not ok and n in HOW:
                print(f"         install: {HOW[n][OS]}")
        print("Nothing was installed. Ask your assistant to run an install command only if you say yes.")
        mode = "A (manager mode, if your Claude Code session offers the Agent tool)" if any(n == "claude" and ok for n, ok, *_ in rows) else "C (sequential: no `claude` command found; install Claude Code for pools)"
        print(f"  orchestration available: {mode}; B (headless pool) needs the `claude` command.")
    if "--net" in sys.argv:
        for name, url in (("youtube", "https://www.youtube.com/robots.txt"), ("reddit", "https://www.reddit.com/robots.txt"),
                          ("github-api", "https://api.github.com/zen"), ("hn", "https://hn.algolia.com/api/v1/search?query=test&hitsPerPage=1")):
            r = http_get(url, retries=0, timeout=10)
            print(f"  net {name}: HTTP {r.status} {r.err}".rstrip())
    sys.exit(0 if all(ok for n, ok, d, f, rq in rows if rq) else 1)


if __name__ == "__main__":
    main()
