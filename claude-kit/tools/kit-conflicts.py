#!/usr/bin/env python3
"""kit-conflicts.py: review the vault files an update did NOT overwrite because you had changed them (stdlib only).

An update never replaces a vault file whose content differs from what it installed. Your version stays; the incoming one is saved under
<config>/claude-kit/state/conflicts/<path>.vault-new and listed in <config>/claude-kit/state/conflicts.json. Project copies made by /rbx-load work the same way.

  kit-conflicts.py list                 every kept file: what it is, why, where the incoming version is
  kit-conflicts.py diff PATH            your file against the incoming one (unified diff, 200 lines)
  kit-conflicts.py accept PATH|--all    take the incoming version (your file is copied to claude-kit/backup/<date>/ first)
  kit-conflicts.py keep PATH|--all      keep your version for good: this incoming version is not reported again (a later kit change is)
  kit-conflicts.py notice [--peek]      the one NOTICE FOR THE USER line the update prints for kept files not reported yet ('' when none); --peek or env VAULT_UPDATE_QUIET=1 does not mark them reported
  kit-conflicts.py count                number of kept files (status lines use it)
PATH is the first column of `list` (an unambiguous end of it is enough). Config dir: --config DIR, else $CLAUDE_CONFIG_DIR, else $CLAUDE_KIT_HOME/.claude, else ~/.claude.
Customisations that never conflict: put your own rules in <config>/claude-kit/state/overrides/local-rules.md (read by the hiccup pre-flight) and your own skills in <config>/skills/.
"""
import datetime
import difflib
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit_state

_spec = importlib.util.spec_from_file_location("kit_install_files", os.path.join(HERE, "kit-install-files.py"))
KIF = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(KIF)


class Ctx(object):
    def __init__(self, cfg):
        self.c = kit_state.config_dir(cfg)
        self.file = os.path.join(self.c, "claude-kit", "state", "conflicts.json")
        self.man = os.path.join(self.c, "claude-kit", "installed.tsv")
        d = KIF.jread(self.file)
        self.items = d.get("items") if isinstance(d.get("items"), dict) else {}
        self.acked = d.get("acked") if isinstance(d.get("acked"), dict) else {}

    def save(self):
        if self.items or self.acked:
            KIF.jwrite(self.file, {"v": 1, "items": self.items, "acked": self.acked})
        elif os.path.isfile(self.file):
            os.remove(self.file)

    def target(self, rel, k):
        return k["file"] if k.get("project") else os.path.join(self.c, *rel.split("/"))

    def saved(self, k):
        s = k.get("saved") or ""
        return os.path.join(self.c, *s.split("/")) if s and KIF.safe_rel(s) else ""

    def drop(self, rel):
        k = self.items.pop(rel, None)
        sv = self.saved(k) if k else ""
        if sv and os.path.isfile(sv):
            os.remove(sv)
            KIF.rmdirs_up(sv, os.path.join(self.c, "claude-kit", "state", "conflicts"))

    def refresh(self):
        """forget entries that are resolved (file equals the incoming version, is gone, or the user deleted the saved copy of a still-differing file)"""
        for rel, k in list(self.items.items()):
            t = self.target(rel, k)
            sv = self.saved(k)
            if k["kind"] == "stale":
                if not os.path.isfile(t):
                    self.drop(rel)
            elif not os.path.isfile(t) or (sv and os.path.isfile(sv) and KIF.nsha(t) == KIF.nsha(sv)):
                self.drop(rel)
        self.save()


def pick(cx, arg):
    if arg in cx.items:
        return [arg]
    hits = [r for r in cx.items if r.endswith(arg) or r.endswith("/" + arg.replace("\\", "/"))]
    return hits


def backup_of(cx, t, rel):
    root = os.path.join(cx.c, "claude-kit", "backup", datetime.date.today().strftime("%Y-%m-%d"))
    name = rel.replace(":", "_").replace("|", "_").lstrip("/") if rel.startswith("project:") else rel
    bk, i = os.path.join(root, *name.split("/")), 1
    while os.path.lexists(bk):
        i += 1
        bk = os.path.join(root, *name.split("/")) + ".%d" % i
    os.makedirs(os.path.dirname(bk), exist_ok=True)
    shutil.copy2(t, bk)
    KIF.prune_backups(cx.c)
    return bk


def marker_set(k, h):
    mp = os.path.join(k["project"], ".claude", "vault-mode.json")
    m = KIF.jread(mp)
    try:
        m["items"][k["key"]]["files"][k["rel"]] = h
    except (KeyError, TypeError):
        return
    KIF.jwrite(mp, m)


def manifest_set(cx, rel, h, nh):
    old, oldn = KIF.read_manifest(cx.man)
    old[rel], oldn[rel] = h, nh
    tmp = cx.man + ".%d.tmp" % os.getpid()
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(("%s\t%s\t%s\n" % (r, v, oldn[r])) if oldn.get(r) else ("%s\t%s\n" % (r, v)) for r, v in sorted(old.items())))
    os.replace(tmp, cx.man)


def cmd_list(cx):
    cx.refresh()
    if not cx.items:
        print("No vault files are being kept: nothing you changed was held back by an update.")
        return 0
    print("%d vault file(s) kept because you changed them (your version is in place; the incoming one is saved):" % len(cx.items))
    for rel in sorted(cx.items):
        k = cx.items[rel]
        why = {"edited": "you edited it", "unrecorded": "a file of yours was already there", "stale": "no longer in the vault, kept because you edited it", "project": "project copy you edited"}.get(k["kind"], k["kind"])
        print("%s\n    %s; incoming: %s" % (rel, why, cx.saved(k) or "(none)"))
    print("Next: kit-conflicts.py diff PATH | accept PATH | keep PATH   (--all for every file)")
    return 0


def cmd_diff(cx, arg):
    hits = pick(cx, arg)
    if len(hits) != 1:
        print("kit-conflicts: %s" % ("no kept file matches %s" % arg if not hits else "ambiguous: " + ", ".join(hits[:5])), file=sys.stderr)
        return 2
    k = cx.items[hits[0]]
    t, sv = cx.target(hits[0], k), cx.saved(k)
    if not sv or not os.path.isfile(sv):
        print("nothing to compare: no incoming version saved for %s" % hits[0])
        return 0
    try:
        a = open(t, encoding="utf-8", errors="replace").read().splitlines()
        b = open(sv, encoding="utf-8", errors="replace").read().splitlines()
    except OSError as e:
        print("kit-conflicts: %s" % e, file=sys.stderr)
        return 2
    out = list(difflib.unified_diff(a, b, "yours", "incoming", lineterm=""))
    print("\n".join(out[:200]) or "(same text; only line endings differ)")
    if len(out) > 200:
        print("... %d more lines" % (len(out) - 200))
    return 0


def resolve(cx, arg, how):
    hits = list(cx.items) if arg == "--all" else pick(cx, arg)
    if not hits:
        print("kit-conflicts: no kept file matches %s" % arg, file=sys.stderr)
        return 2
    if len(hits) > 1 and arg != "--all":
        print("kit-conflicts: ambiguous: %s" % ", ".join(hits[:5]), file=sys.stderr)
        return 2
    for rel in sorted(hits):
        k = cx.items[rel]
        t, sv = cx.target(rel, k), cx.saved(k)
        if how == "accept":
            if k["kind"] == "stale":
                if os.path.isfile(t):
                    bk = backup_of(cx, t, rel)
                    os.remove(t)
                    print("removed %s (yours saved in %s)" % (rel, bk))
            elif sv and os.path.isfile(sv):
                bk = backup_of(cx, t, rel) if os.path.isfile(t) else "-"
                os.makedirs(os.path.dirname(t), exist_ok=True)
                KIF.put_file(sv, t)
                if k.get("project"):
                    marker_set(k, k["incoming"])
                else:
                    manifest_set(cx, rel, KIF.sha(t), KIF.nsha(t))
                print("took the incoming %s (yours saved in %s)" % (rel, bk))
        else:
            if k["incoming"]:
                cx.acked[rel] = k["incoming"]
            if k.get("project"):
                marker_set(k, k["incoming"])
            print("kept your %s (this incoming version will not be reported again)" % rel)
        cx.drop(rel)
    cx.save()
    return 0


def cmd_notice(cx, peek):
    cx.refresh()
    fresh = [r for r, k in cx.items.items() if not k.get("notified")]
    if not fresh:
        return 0
    n = len(cx.items)
    print("NOTICE FOR THE USER (show this): %d locally changed vault file%s kept; incoming versions saved; review with: python \"%s\" list" % (n, "" if n == 1 else "s", os.path.join(cx.c, "claude-kit", "tools", "kit-conflicts.py")))
    if not peek and os.environ.get("VAULT_UPDATE_QUIET") != "1":
        for r in fresh:
            cx.items[r]["notified"] = True
        cx.save()
    return 0


def main(argv):
    cfg = None
    if "--config" in argv:
        i = argv.index("--config")
        cfg = argv[i + 1] if i + 1 < len(argv) else None
        argv = argv[:i] + argv[i + 2:]
    if not argv:
        print(__doc__)
        return 2
    cx = Ctx(cfg)
    cmd, rest = argv[0], argv[1:]
    if cmd == "list":
        return cmd_list(cx)
    if cmd == "count":
        cx.refresh()
        print(len(cx.items))
        return 0
    if cmd == "notice":
        return cmd_notice(cx, "--peek" in rest)
    if cmd == "diff" and len(rest) == 1:
        return cmd_diff(cx, rest[0])
    if cmd in ("accept", "keep") and len(rest) == 1:
        return resolve(cx, rest[0], cmd)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
