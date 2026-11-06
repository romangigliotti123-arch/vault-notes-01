#!/usr/bin/env python3
"""kit-install-files.py: the file-copy loop of install.sh in ONE process (stdlib only).

install.sh used to spawn about seven processes per kit file (sha256sum twice, awk, dirname, mkdir, cp, ...): about 4 minutes for ~1000 files on Git Bash
(process creation is slow there). This does the same work in-process: same layout, same decisions, same installed.tsv.

  kit-install-files.py --kit KITDIR --config CONFIGDIR --always-on "rbx-update rbx-check ..." [--dry-run]

Layout (relative to CONFIGDIR = ~/.claude):
  tools|systems|skillpack/<r>   -> claude-kit/<sub>/<r>
  agents/<r>                    -> claude-kit/vault-mode/.claude/agents/<r>
  mode/<r>                      -> claude-kit/vault-mode/<r>   (mode/cold/<topic>/<file> = the cold area: store only, never copied into a project)
  skills/<name>/<r>             -> skills/<name>/<r> when <name> is in --always-on, else claude-kit/vault-mode/.claude/skills/<name>/<r>
Per file (the vault owns every file it installs): missing -> copy (new); identical -> unchanged; anything else -> overwritten with the incoming version (updated). No keep, no conflicts, no
backups. A file that left the kit (it is in the old installed.tsv, not in the kit any more) is removed. Anything not in the manifest is never touched (your Games/, Models/, your own
skills and agents, claude-kit/state/ settings).
installed.tsv ("<rel> TAB <sha256>"; an older third column is read and dropped) is written atomically (sorted, unique) unless --dry-run, only to find files that left the kit and to stay idempotent.
Last stdout line: "RESULT new=N upd=N same=N gone=N fail=N". Exit 0. A write that fails (read-only file ...) is reported as FAILED and counted in fail.
"""
import argparse
import hashlib
import json
import os
import shutil
import sys
import time

SUBS = ("agents", "skills", "mode", "tools", "systems", "skillpack")
SM = "claude-kit/vault-mode"
RETIRED = ("rbx-load", "rbx-unload")   # always-on commands that no longer exist: their old global files are removed by the gone-file logic


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def kit_files(kit):
    """(sub, 'sub/relpath') for every kit file, __pycache__ and .pyc skipped, sorted."""
    out = []
    for sub in SUBS:
        root = os.path.join(kit, sub)
        if not os.path.isdir(root):
            continue
        for d, dirs, files in os.walk(root):
            dirs[:] = [x for x in dirs if x != "__pycache__"]
            for n in files:
                if n.endswith(".pyc") or os.path.islink(os.path.join(d, n)):
                    continue
                out.append((sub, os.path.relpath(os.path.join(d, n), kit).replace(os.sep, "/")))
    return sorted(out, key=lambda x: x[1])


def rel_of(sub, r, ao):
    if sub in ("tools", "systems", "skillpack"):
        return "claude-kit/" + r
    if sub == "agents":
        return "%s/.claude/%s" % (SM, r)
    if sub == "mode":
        return "%s/%s" % (SM, r[len("mode/"):])
    nm = r[len("skills/"):].split("/")[0]
    return r if nm in ao else "%s/.claude/%s" % (SM, r)


def read_manifest(path):
    old = {}
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for ln in f.read().split("\n"):
                p = ln.split("\t")
                if len(p) >= 2 and p[0] not in old:
                    old[p[0]] = p[1]
    except OSError:
        pass
    return old


class Lock(object):
    """advisory lock file: waits up to 30 s for another run, takes over a lock older than 120 s, never blocks for good"""

    def __init__(self, path):
        self.path, self.have = path, False

    def __enter__(self):
        end = time.time() + 30
        while True:
            try:
                os.makedirs(os.path.dirname(self.path), exist_ok=True)
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                self.have = True
                return self
            except FileExistsError:
                try:
                    if time.time() - os.path.getmtime(self.path) > 120:
                        os.remove(self.path)
                        continue
                except OSError:
                    pass
            except OSError:
                return self
            if time.time() > end:
                return self
            time.sleep(0.2)

    def __exit__(self, *exc):
        if self.have:
            try:
                os.remove(self.path)
            except OSError:
                pass
        return False


def put_file(src, dst):
    tmp = dst + ".kit-tmp"
    try:
        if os.path.lexists(tmp):
            os.remove(tmp)
        shutil.copy(src, tmp)
        try:
            os.replace(tmp, dst)
        except PermissionError:
            os.chmod(dst, 0o644)
            os.replace(tmp, dst)
    finally:
        if os.path.lexists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass


def safe_rel(rel):
    return bool(rel) and not rel.startswith("/") and ".." not in rel.split("/") and ":" not in rel and "\\" not in rel


def rmdirs_up(path, stop):
    d = os.path.dirname(path)
    stop = os.path.realpath(stop)
    while os.path.realpath(d) != stop and os.path.realpath(d).startswith(stop + os.sep):
        try:
            os.rmdir(d)
        except OSError:
            return
        d = os.path.dirname(d)


def cleanup_allowed(c):
    try:
        with open(os.path.join(c, "claude-kit", "vault-mode", "layout.json"), encoding="utf-8") as f:
            lay = json.load(f)
        return lay.get("auto") is not False and lay.get("rename_auto") is not False
    except (OSError, ValueError, AttributeError):
        return True


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--kit", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--always-on", default="rbx-update rbx-check rbx-uninstall")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    kit, c = os.path.abspath(a.kit), os.path.abspath(a.config)
    if a.dry_run:
        return run(a, kit, c)
    with Lock(os.path.join(c, "claude-kit", ".install.lock")):
        return run(a, kit, c)


def run(a, kit, c):
    ao = set(a.always_on.split())
    man = os.path.join(c, "claude-kit", "installed.tsv")
    old = read_manifest(man)
    n_new = n_upd = n_same = n_gone = n_fail = 0
    rec = {}
    for sub, r in kit_files(kit):
        src = os.path.join(kit, *r.split("/"))
        rel = rel_of(sub, r, ao)
        dst = os.path.join(c, *rel.split("/"))
        try:
            ns = sha(src)
            if os.path.islink(dst) and not os.path.exists(dst):
                if not a.dry_run:
                    os.unlink(dst)
            if os.path.isdir(dst):
                raise OSError("a folder is in the way")
            rec[rel] = ns
            if not os.path.exists(dst):
                if not a.dry_run:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    put_file(src, dst)
                n_new += 1
            elif sha(dst) == ns:
                n_same += 1
            else:
                if not a.dry_run:
                    put_file(src, dst)
                n_upd += 1
        except OSError as e:
            n_fail += 1
            print("FAILED %s: %s" % (rel, e))
            rec.pop(rel, None)
            if rel in old:
                rec[rel] = old[rel]
    if cleanup_allowed(c):
        for rel in sorted(old):
            if rel in rec or not safe_rel(rel) or not (rel.startswith("claude-kit/") or (rel.startswith("skills/") and (rel.split("/")[1] in ao or rel.split("/")[1] in RETIRED))):
                continue
            f = os.path.join(c, *rel.split("/"))
            try:
                if os.path.isfile(f) and not os.path.islink(f):
                    if not a.dry_run:
                        os.remove(f)
                        rmdirs_up(f, os.path.join(c, rel.split("/")[0]))
                    n_gone += 1
            except OSError:
                pass
    if not a.dry_run:
        os.makedirs(os.path.dirname(man), exist_ok=True)
        tmp = man + ".%d.tmp" % os.getpid()
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write("".join("%s\t%s\n" % (k, v) for k, v in sorted(rec.items())))
        os.replace(tmp, man)
    print("RESULT new=%d upd=%d same=%d gone=%d fail=%d" % (n_new, n_upd, n_same, n_gone, n_fail))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
