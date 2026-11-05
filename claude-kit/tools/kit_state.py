#!/usr/bin/env python3
"""kit_state.py: where the vault keeps what YOUR use of it produces (stdlib only; imported by learn.py, hiccup.py, ui_pref.py, rbx-bench).

All of it lives under <claude config dir>/claude-kit/state/, a folder no installer or updater ever writes a kit file into, replaces or deletes (the registry tools/user-state.json lists every path):
  state/learnings-queue/      queued /rbx-learn notes (pending, sent, rejected, ready-to-send, repo)
  state/hiccups/              the hiccup ledger (ledger.jsonl, games.jsonl, settings.json)
  state/ui-mockup.json        the /rbx-mockup preference            state/ui-mockup-notice.done   one-time notice marker
  state/overrides/            local-rules.md: your own rules, read by the hiccup pre-flight; never touched by an update
  state/conflicts.json, state/conflicts/   vault files you edited that an update kept (see kit-conflicts.py)
Older installs kept the first four directly under claude-kit/. migrate() moves them over once (idempotent: a file already there is never overwritten, identical leftovers are removed, a differing
leftover stays where it was and is reported); path(name) migrates on demand, so a tool always finds the data, and falls back to the old place when the move is impossible.

  kit_state.py migrate [--config DIR]     move the old locations over, print one line when something moved
  kit_state.py path NAME [--config DIR]   print the path of a state item
"""
import os
import shutil
import sys

STATE = ("claude-kit", "state")
LEGACY = {"learnings-queue": ("claude-kit", "learnings-queue"), "hiccups": ("claude-kit", "hiccups"),
          "ui-mockup.json": ("claude-kit", "ui-mockup.json"), "ui-mockup-notice.done": ("claude-kit", "ui-mockup-notice.done")}
NAMES = tuple(LEGACY) + ("overrides", "conflicts", "conflicts.json")


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


def _move_tree(src, dst, left):
    """move src (file or folder) to dst without overwriting anything; True when src is gone afterwards"""
    if os.path.isdir(src) and not os.path.islink(src):
        os.makedirs(dst, exist_ok=True)
        for n in sorted(os.listdir(src)):
            _move_tree(os.path.join(src, n), os.path.join(dst, n), left)
        try:
            os.rmdir(src)
            return True
        except OSError:
            return False
    if not os.path.lexists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        try:
            os.replace(src, dst)
            return True
        except OSError:
            shutil.copy2(src, dst)
            os.remove(src)
            return True
    try:
        with open(src, "rb") as a, open(dst, "rb") as b:
            same = a.read() == b.read()
    except OSError:
        same = False
    if same:
        os.remove(src)
        return True
    left.append(src)
    return False


def migrate_one(name, cfg=None):
    """-> number of entries moved or merged for one legacy item (0 when there is nothing to do)"""
    c = config_dir(cfg)
    old = os.path.join(c, *LEGACY[name])
    new = os.path.join(state_dir(cfg), name)
    if not os.path.lexists(old):
        return 0
    left = []
    try:
        _move_tree(old, new, left)
    except OSError:
        return 0
    return 1


def migrate(cfg=None):
    moved = [n for n in LEGACY if migrate_one(n, cfg)]
    return moved


def path(name, cfg=None):
    """the state path of an item; moves an old-location copy over first, falls back to the old place when that is impossible"""
    new = os.path.join(state_dir(cfg), name)
    if name in LEGACY:
        old = os.path.join(config_dir(cfg), *LEGACY[name])
        if os.path.lexists(old):
            migrate_one(name, cfg)
            if os.path.lexists(old) and not os.path.lexists(new):
                return old
    return new


def main(argv):
    cfg = None
    if "--config" in argv:
        i = argv.index("--config")
        cfg = argv[i + 1] if i + 1 < len(argv) else None
        argv = argv[:i] + argv[i + 2:]
    if argv[:1] == ["migrate"]:
        moved = migrate(cfg)
        if moved:
            print("claude-kit: your data moved to %s (%s)" % (state_dir(cfg), ", ".join(moved)))
        return 0
    if argv[:1] == ["path"] and len(argv) == 2 and argv[1] in NAMES:
        print(path(argv[1], cfg))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
