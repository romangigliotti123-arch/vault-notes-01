#!/usr/bin/env python3
"""kit_state.py: where the vault keeps the few tiny settings that must survive an update (stdlib only; imported by ui_pref.py).

They live under <claude config dir>/claude-kit/state/, a folder the installer never writes a kit file into and never deletes:
  state/ui-mockup.json          the /rbx-mockup on/off preference
  state/ui-mockup-notice.done   one-time notice marker
  state/ideas-history.tsv       spark.py hist: titles + one-line pitches of past ideas (capped 200 lines)
  state/market-brief.md         idea-brief.py: dated market brief for idea generation
Everything else the vault installs is vault-owned and is overwritten by every install/update. Old leftovers in state/ (learnings-queue, hiccups, conflicts, overrides, thumbnails)
are ignored by the kit; delete them by hand if you like: they are not read any more.

  kit_state.py path NAME [--config DIR]   print the path of a state item
"""
import os
import sys

STATE = ("claude-kit", "state")
NAMES = ("ui-mockup.json", "ui-mockup-notice.done", "ideas-history.tsv", "market-brief.md")


def config_dir(cfg=None):
    if cfg:
        return os.path.abspath(os.path.expanduser(cfg))
    if os.environ.get("CLAUDE_CONFIG_DIR"):
        return os.path.abspath(os.path.expanduser(os.environ["CLAUDE_CONFIG_DIR"]))
    if os.environ.get("CLAUDE_KIT_HOME"):
        return os.path.join(os.path.abspath(os.path.expanduser(os.environ["CLAUDE_KIT_HOME"])), ".claude")
    return os.path.join(os.path.expanduser("~"), ".claude")


def state_dir(cfg=None):
    return os.path.join(config_dir(cfg), *STATE)


def path(name, cfg=None):
    """the path of a state item (the file may not exist yet)"""
    return os.path.join(state_dir(cfg), name)


def main(argv):
    cfg = None
    if "--config" in argv:
        i = argv.index("--config")
        cfg = argv[i + 1] if i + 1 < len(argv) else None
        argv = argv[:i] + argv[i + 2:]
    if argv[:1] == ["path"] and len(argv) == 2 and argv[1] in NAMES:
        print(path(argv[1], cfg))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
