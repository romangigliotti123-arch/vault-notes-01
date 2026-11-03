#!/usr/bin/env python3
"""low-usage-mode helper. Standard library only; no network; never prints secrets.

Usage: lum.py run [on|off|status|install-hooks|uninstall-hooks]   (what the /low-usage-mode skill calls; empty = on)
       lum.py hook <UserPromptSubmit|SessionStart>                 (hook entry; prints nothing when the mode is off)
       lum.py on | off | status | install-hooks | uninstall-hooks [--config DIR]
Config dir: --config DIR, else env CLAUDE_CONFIG_DIR, else ~/.claude. Marker file: <config>/state/low-usage-mode.on
The rules text below is duplicated in lum.ps1 (PowerShell fallback); keep the two in step.
"""
import datetime
import json
import os
import sys

MARKER = "low-usage-mode.on"
HOOK_ID = "low-usage-mode/scripts/lum"  # substring that identifies our hook entries in settings.json
PREFIX = "low usage mode enabled."
RULES = (
    "LOW USAGE MODE IS ON (the user turned it on with /low-usage-mode; '/low-usage-mode off' ends it). "
    "Begin EVERY reply with exactly: " + PREFIX + " (all lowercase, then continue). "
    "Rules: use the cheapest model that fits (sonnet by default, haiku for lookups, simple edits and any subagent, "
    "opus only if the user asks). At most 1 subagent at a time; no agent teams, workflows or fan-out. "
    "Keep replies short: answer first, no preamble or recap. Keep tool output small: targeted reads (offset/limit), "
    "grep, head/tail, never dump whole files or repos. No screenshots or images unless essential. "
    "Batch independent tool calls in one message. Ask before anything expensive (long runs, big reads, many agents). "
    "If the conversation is large, say once that /compact or /clear would save usage."
)


def cfg_dir(override=None):
    d = override or os.environ.get("CLAUDE_CONFIG_DIR")
    return os.path.abspath(d) if d else os.path.join(os.path.expanduser("~"), ".claude")


def marker_path(c):
    return os.path.join(c, "state", MARKER)


def hook_cmd(event):
    return '"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/low-usage-mode/scripts/lum" hook ' + event


def wanted():
    # sh is the shell Claude Code uses for hook commands on macOS/Linux and (Git Bash) on Windows
    return {
        "UserPromptSubmit": {"hooks": [{"type": "command", "command": "sh " + hook_cmd("UserPromptSubmit"), "timeout": 10}]},
        "SessionStart": {"matcher": "startup|resume|compact",
                         "hooks": [{"type": "command", "command": "sh " + hook_cmd("SessionStart"), "timeout": 10}]},
    }


def is_ours(handler):
    return isinstance(handler, dict) and HOOK_ID in str(handler.get("command", ""))


def read_settings(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8-sig") as f:
        txt = f.read()
    if not txt.strip():
        return {}
    data = json.loads(txt)
    if not isinstance(data, dict):
        raise ValueError("settings.json is not a JSON object")
    return data


def write_settings(path, data):
    if os.path.exists(path):
        stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        bak = path + ".lum-bak-" + stamp
        with open(path, "rb") as s, open(bak, "wb") as d:
            d.write(s.read())
        print("backup: " + bak)
    tmp = path + ".lum-tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, path)


def hooks_present(data):
    out = {}
    for ev in ("UserPromptSubmit", "SessionStart"):
        groups = (data.get("hooks") or {}).get(ev) or []
        out[ev] = any(is_ours(h) for g in groups if isinstance(g, dict) for h in (g.get("hooks") or []))
    return out


def hooks_state(c):
    try:
        p = hooks_present(read_settings(os.path.join(c, "settings.json")))
    except Exception as e:  # unreadable settings: report, change nothing
        return "unreadable(" + type(e).__name__ + ")"
    if all(p.values()):
        return "installed"
    if any(p.values()):
        return "partial"
    return "MISSING"


def install_hooks(c):
    path = os.path.join(c, "settings.json")
    try:
        data = read_settings(path)
    except Exception as e:
        print("hooks: NOT changed, settings.json is not valid JSON (" + type(e).__name__ + "). Fix it first.")
        return 2
    present = hooks_present(data)
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        print("hooks: NOT changed, settings.json 'hooks' is not an object.")
        return 2
    changed = False
    for ev, group in wanted().items():
        if present[ev]:
            continue
        hooks.setdefault(ev, []).append(group)
        changed = True
    if not changed:
        print("hooks: already installed (no change)")
        return 0
    os.makedirs(c, exist_ok=True)
    write_settings(path, data)
    print("hooks: installed in " + path + " (UserPromptSubmit + SessionStart). Start a new session or open /hooks to load them.")
    return 0


def uninstall_hooks(c):
    path = os.path.join(c, "settings.json")
    try:
        data = read_settings(path)
    except Exception as e:
        print("hooks: NOT changed, settings.json is not valid JSON (" + type(e).__name__ + ").")
        return 2
    hooks = data.get("hooks")
    if not isinstance(hooks, dict) or not any(hooks_present(data).values()):
        print("hooks: none of ours found (no change)")
        return 0
    for ev in list(hooks):
        groups = hooks.get(ev)
        if not isinstance(groups, list):
            continue
        keep = []
        for g in groups:
            if isinstance(g, dict) and isinstance(g.get("hooks"), list):
                g["hooks"] = [h for h in g["hooks"] if not is_ours(h)]
                if not g["hooks"]:
                    continue
            keep.append(g)
        if keep:
            hooks[ev] = keep
        else:
            del hooks[ev]
    if not hooks:
        del data["hooks"]
    write_settings(path, data)
    print("hooks: removed ours from " + path)
    return 0


def turn_on(c):
    p = marker_path(c)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(json.dumps({"since": datetime.datetime.now().isoformat(timespec="seconds")}) + "\n")


def turn_off(c):
    try:
        os.remove(marker_path(c))
    except FileNotFoundError:
        pass


def status_line(action, c):
    on = os.path.exists(marker_path(c))
    return "LUM action=%s mode=%s hooks=%s config=%s" % (action, "on" if on else "off", hooks_state(c), c)


def hook(event):
    c = cfg_dir()
    if not os.path.exists(marker_path(c)):
        return 0
    try:  # drain the event JSON Claude Code sends (not needed); skip on a terminal
        if not sys.stdin.isatty():
            sys.stdin.read()
    except Exception:
        pass
    ctx = RULES
    if event == "SessionStart":
        ctx = "(Restored at session start/resume/compaction.) " + ctx
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": ctx}}) + "\n")
    return 0


def main(argv):
    args = list(argv)
    override = None
    if "--config" in args:
        i = args.index("--config")
        override = args[i + 1] if i + 1 < len(args) else None
        del args[i:i + 2]
    cmd = (args[0] if args else "run").strip().lower()
    if cmd == "hook":
        return hook(args[1] if len(args) > 1 else "UserPromptSubmit")
    if cmd == "run":
        cmd = (args[1] if len(args) > 1 else "").strip().lower() or "on"
        if cmd not in ("on", "off", "status", "install-hooks", "uninstall-hooks"):
            cmd = "on" if cmd in ("enable", "start", "1") else "status"
    c = cfg_dir(override)
    if cmd == "on":
        turn_on(c)
        print(status_line("on", c))
    elif cmd == "off":
        turn_off(c)
        print(status_line("off", c))
    elif cmd == "status":
        print(status_line("status", c))
    elif cmd == "install-hooks":
        rc = install_hooks(c)
        print(status_line("install-hooks", c))
        return rc
    elif cmd == "uninstall-hooks":
        rc = uninstall_hooks(c)
        print(status_line("uninstall-hooks", c))
        return rc
    else:
        print("usage: lum.py run|on|off|status|install-hooks|uninstall-hooks|hook <event> [--config DIR]")
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as e:  # never break a session because of this helper
        sys.stderr.write("lum.py: " + type(e).__name__ + "\n")
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] == "hook" else 1)
