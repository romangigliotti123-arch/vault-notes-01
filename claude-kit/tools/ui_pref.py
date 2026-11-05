#!/usr/bin/env python3
"""ui_pref.py: the /rbx-mockup toggle, the Figma notice and the one-time update notice. Stdlib only, no network, no secrets, no tokens.

  ui_pref.py get                         prints on or off (default off when unset, unreadable or unanswered)
  ui_pref.py set on|off                  stores the preference in <claude config dir>/claude-kit/state/ui-mockup.json (idempotent; same answer = same file)
  ui_pref.py toggle ARG                  what /rbx-mockup runs: on|off = set, anything else prints `UIPREF action=status`
  ui_pref.py status [--tools LIST|-] [--game DIR]   mode names, Figma connected or not (+ the notice line), the preference file path
  ui_pref.py figma --tools LIST|- [--game DIR] [--force]   the Figma check of the UI step: ONE line once per game (marker DIR/ui-design-qa/state.json), nothing after that
  ui_pref.py notice [--mark-only]        the one-time NOTICE FOR THE USER line for existing installs (marker <config>/claude-kit/state/ui-mockup-notice.done); --mark-only = fresh install, marks silently
  LIST = the tool names the agent sees, comma or newline separated ('-' reads stdin). Connected = any name contains "figma" (case-insensitive).
Modes: off (default) = automatic design-first; on = manual Nano Banana 2.1 package (ui_mock.py). The preference means only that. The Figma connection is the user's own; this tool never asks for
or stores a Figma token or account and never installs anything.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit_state

QUESTION = ("Manual UI mockups: want Claude to give you prompts, reference images and steps to make UI mockups yourself with Nano Banana 2.1 on the Gemini website? "
            "Default is no: Claude designs the UI itself first. Change any time with /rbx-mockup on|off.")
FIGMA_DOCS = "https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/"
NOT_CONNECTED = ("Figma isn't connected. UI creation works best with it on. Using the local HTML/CSS design sheet for now. To connect Figma: %s" % FIGMA_DOCS)
CONNECTED = "Figma connected: the UI design step uses it (reads the frame structure and variables; writes the design only if the connector allows writes, else it compares read-only)."
UPDATE_NOTICE = ("NOTICE FOR THE USER (show this): UI mockups now default to automatic design-first: Claude designs each UI button and screen layout itself before building. "
                 "To make mockups yourself with Nano Banana 2.1 on the Gemini website, run /rbx-mockup on (switch back with /rbx-mockup off, see the mode with /rbx-mockup status).")


def config_dir():
    c = os.environ.get("CLAUDE_CONFIG_DIR")
    return c if c else os.path.join(os.path.expanduser("~"), ".claude")


def pref_path():
    return kit_state.path("ui-mockup.json", config_dir())


def get_mode():
    try:
        with open(pref_path(), encoding="utf-8-sig") as f:
            return "on" if json.load(f).get("manual_mockups") is True else "off"
    except (OSError, ValueError, AttributeError):
        return "off"


def set_mode(v):
    p = pref_path()
    text = json.dumps({"manual_mockups": v == "on"}, indent=1) + "\n"
    try:
        if open(p, encoding="utf-8").read() == text:
            return False
    except OSError:
        pass
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return True


def names_from(arg):
    raw = sys.stdin.read() if arg == "-" else (arg or "")
    return [n.strip() for n in raw.replace("\n", ",").split(",") if n.strip()]


def figma_connected(names):
    return any("figma" in n.lower() for n in names)


def state_path(game):
    return os.path.join(game, "ui-design-qa", "state.json")


def seen(game):
    try:
        with open(state_path(game), encoding="utf-8") as f:
            return bool(json.load(f).get("figma_notice_shown"))
    except (OSError, ValueError, AttributeError):
        return False


def mark_seen(game, connected):
    p = state_path(game)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"figma_notice_shown": True, "connected": bool(connected)}, f)
        f.write("\n")


def figma_line(names, game, force=False):
    """-> the line to show (or '' when already shown for this game)"""
    ok = figma_connected(names)
    if game and not force and seen(game):
        return ""
    line = CONNECTED if ok else NOT_CONNECTED
    if game and not force:
        mark_seen(game, ok)
    return line


def marker_path():
    return kit_state.path("ui-mockup-notice.done", config_dir())


def notice(mark_only=False):
    m = marker_path()
    if os.path.exists(m):
        return ""
    os.makedirs(os.path.dirname(m), exist_ok=True)
    with open(m, "w", encoding="utf-8", newline="\n") as f:
        f.write("shown\n")
    return "" if mark_only else UPDATE_NOTICE


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a and a.index(n) + 1 < len(a) else d
    c = a[0]
    if c == "get":
        print(get_mode())
        return 0
    if c == "set":
        v = (a[1] if len(a) > 1 else "").lower()
        if v not in ("on", "off"):
            print("usage: ui_pref.py set on|off", file=sys.stderr)
            return 2
        ch = set_mode(v)
        print("UI mockups: %s (%s). %s" % ("manual Nano Banana 2.1 package" if v == "on" else "automatic design-first", "changed" if ch else "already set", pref_path()))
        return 0
    if c == "toggle":
        v = (a[1] if len(a) > 1 else "").strip().lower()
        if v in ("on", "off"):
            return main(["set", v])
        print("UIPREF action=status")
        return 0
    if c == "status":
        m = get_mode()
        print("UI mockups: %s%s" % ("manual Nano Banana 2.1 package (on)" if m == "on" else "automatic design-first (off, the default)", "" if m == "on" else "; /rbx-mockup on switches to the manual Nano Banana 2.1 package"))
        if opt("--tools") is None:
            print("Figma: not checked here (the agent checks its own tool list for a tool whose name contains figma and passes the names with --tools)")
        else:
            names = names_from(opt("--tools"))
            print("Figma: connected" if figma_connected(names) else "Figma: not connected")
            print(figma_line(names, None))
        print("Preference file: " + pref_path())
        return 0
    if c == "figma":
        if opt("--tools") is None:
            print("usage: ui_pref.py figma --tools <names>|- [--game DIR] [--force]", file=sys.stderr)
            return 2
        line = figma_line(names_from(opt("--tools")), opt("--game"), "--force" in a)
        if line:
            print(line)
        return 0
    if c == "notice":
        line = notice("--mark-only" in a)
        if line:
            print(line)
        return 0
    print("unknown command " + c, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
