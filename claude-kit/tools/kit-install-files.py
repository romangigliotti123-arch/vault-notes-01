#!/usr/bin/env python3
"""kit-install-files.py: the file-copy loop of install.sh in ONE process (stdlib only).

install.sh used to spawn about seven processes per kit file (sha256sum twice, awk, dirname, mkdir, cp, ...): about 4 minutes for ~1000 files on Git Bash
(process creation is slow there). This does the same work in-process: same layout, same decisions, same installed.tsv.

  kit-install-files.py --kit KITDIR --config CONFIGDIR --always-on "rbx-load rbx-unload ..." [--dry-run]

Layout (relative to CONFIGDIR = ~/.claude):
  tools|systems|skillpack/<r>   -> claude-kit/<sub>/<r>
  agents/<r>                    -> claude-kit/vault-mode/.claude/agents/<r>
  mode/<r>                      -> claude-kit/vault-mode/<r>   (mode/cold/<topic>/<file> = the cold area: store only, never copied into a project)
  skills/<name>/<r>             -> skills/<name>/<r> when <name> is in --always-on, else claude-kit/vault-mode/.claude/skills/<name>/<r>
Per file (YOUR edits win, nothing of yours is overwritten): missing -> copy (new); identical (also when only the line endings differ) -> unchanged; equal to the hash recorded in the old
installed.tsv (you did not touch it) -> copy over (updated); a file you edited, or a file the manifest never recorded -> KEPT as it is, the incoming kit version is saved as
claude-kit/state/conflicts/<rel>.vault-new and listed in claude-kit/state/conflicts.json (review: kit-conflicts.py list|diff|accept|keep). Only when there is no manifest at all (first install
over existing files) is a differing file backed up to claude-kit/backup/<date>/<rel> and replaced (the newest 10 dated backup folders are kept).
installed.tsv ("<rel> TAB <sha256> TAB <sha256 with CRLF read as LF>") is written atomically (sorted, unique) unless --dry-run.
Last stdout line: "RESULT new=N upd=N same=N repl=N gone=N fail=N conf=N cnew=N" (conf = kept files in the list, cnew = new or changed this run). Exit 0.
A file that left the kit and is unchanged since it was installed is removed (gone); one you edited stays (kind "stale"). A write that fails (read-only file ...) is reported as FAILED and counted in fail.
"""
import argparse
import datetime
import hashlib
import json
import os
import shutil
import sys
import time

SUBS = ("agents", "skills", "mode", "tools", "systems", "skillpack")
SM = "claude-kit/vault-mode"


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def nsha(p):
    """sha256 of the text with CRLF read as LF (binary files: the plain sha), so a line-ending-only difference is not an edit"""
    with open(p, "rb") as f:
        d = f.read()
    return hashlib.sha256(d if b"\0" in d[:8192] else d.replace(b"\r\n", b"\n")).hexdigest()


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
    old, oldn = {}, {}
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for ln in f.read().split("\n"):
                p = ln.split("\t")
                if len(p) >= 2 and p[0] not in old:      # awk: first match wins
                    old[p[0]] = p[1]
                    if len(p) >= 3 and p[2]:
                        oldn[p[0]] = p[2]
    except OSError:
        pass
    return old, oldn


def jread(path):
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def jwrite(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".%d.tmp" % os.getpid()
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


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


def conflict_path(c, rel):
    r = rel[len("claude-kit/"):] if rel.startswith("claude-kit/") else rel
    return os.path.join(c, "claude-kit", "state", "conflicts", *(r + ".vault-new").split("/"))


def prune_backups(c, keep=10):
    root = os.path.join(c, "claude-kit", "backup")
    try:
        days = sorted(d for d in os.listdir(root) if len(d) == 10 and d[:4].isdigit() and d[4] == "-" and os.path.isdir(os.path.join(root, d)))
    except OSError:
        return
    for d in days[:-keep]:
        shutil.rmtree(os.path.join(root, d), ignore_errors=True)


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
    ap.add_argument("--always-on", default="rbx-load rbx-unload rbx-update rbx-check rbx-uninstall")
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
    old, oldn = read_manifest(man)
    cfile = os.path.join(c, "claude-kit", "state", "conflicts.json")
    cdoc = jread(cfile)
    items = cdoc.get("items") if isinstance(cdoc.get("items"), dict) else {}
    acked = cdoc.get("acked") if isinstance(cdoc.get("acked"), dict) else {}
    bk_root = os.path.join(c, "claude-kit", "backup", datetime.date.today().strftime("%Y-%m-%d"))
    n_new = n_upd = n_same = n_repl = n_gone = n_fail = 0
    rec, recn, kept, srcs = {}, {}, {}, {}
    for sub, r in kit_files(kit):
        src = os.path.join(kit, *r.split("/"))
        rel = rel_of(sub, r, ao)
        dst = os.path.join(c, *rel.split("/"))
        try:
            ns, nn = sha(src), nsha(src)
            if os.path.islink(dst) and not os.path.exists(dst):
                if not a.dry_run:
                    os.unlink(dst)
            if os.path.isdir(dst):
                raise OSError("a folder is in the way")
            rec[rel], recn[rel] = ns, nn
            if not os.path.exists(dst):
                if not a.dry_run:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    put_file(src, dst)
                n_new += 1
                continue
            ds = sha(dst)
            dn = nn if ds == ns else nsha(dst)
            if dn == nn:
                n_same += 1
            elif old.get(rel) and (ds == old[rel] or (oldn.get(rel) and dn == oldn[rel])):
                if not a.dry_run:
                    put_file(src, dst)
                n_upd += 1
            elif old.get(rel) == ns or (oldn.get(rel) and oldn[rel] == nn):
                n_same += 1
            elif not old:
                if not a.dry_run:
                    bk, i = os.path.join(bk_root, *rel.split("/")), 1
                    while os.path.lexists(bk):
                        i += 1
                        bk = os.path.join(bk_root, *rel.split("/")) + ".%d" % i
                    os.makedirs(os.path.dirname(bk), exist_ok=True)
                    shutil.copy2(dst, bk)
                    if os.path.islink(dst):
                        os.unlink(dst)
                    put_file(src, dst)
                n_repl += 1
            else:
                if acked.get(rel) == ns:
                    n_same += 1
                else:
                    kept[rel] = {"kind": "edited" if rel in old else "unrecorded", "incoming": ns}
                    srcs[rel] = src
                if rel in old:
                    rec[rel], recn[rel] = old[rel], oldn.get(rel, "")
                else:
                    del rec[rel], recn[rel]
        except OSError as e:
            n_fail += 1
            print("FAILED %s: %s" % (rel, e))
            rec.pop(rel, None)
            recn.pop(rel, None)
            if rel in old:
                rec[rel], recn[rel] = old[rel], oldn.get(rel, "")
    if cleanup_allowed(c):
        for rel, h in sorted(old.items()):
            if rel in rec or rel in kept or not safe_rel(rel) or not (rel.startswith("claude-kit/") or (rel.startswith("skills/") and rel.split("/")[1] in ao)):
                continue
            f = os.path.join(c, *rel.split("/"))
            try:
                if os.path.isfile(f) and not os.path.islink(f):
                    if sha(f) == h or (oldn.get(rel) and nsha(f) == oldn[rel]):
                        if not a.dry_run:
                            os.remove(f)
                            rmdirs_up(f, os.path.join(c, rel.split("/")[0]))
                        n_gone += 1
                    else:
                        kept[rel] = {"kind": "stale", "incoming": ""}
            except OSError:
                pass
    cnew = 0
    for rel, k in kept.items():
        prev = items.get(rel) or {}
        same = prev.get("incoming") == k["incoming"] and prev.get("kind") == k["kind"]
        k["notified"] = bool(same and prev.get("notified"))
        k["at"] = prev["at"] if same and prev.get("at") else datetime.date.today().isoformat()
        k["saved"] = prev.get("saved", "") if same else ""
        cnew += 0 if same else 1
    for rel, prev in items.items():
        if rel in kept or rel in rec:
            continue
        if prev.get("project") and os.path.isdir(str(prev.get("project"))):
            kept[rel] = prev
        elif prev.get("kind") == "stale" and safe_rel(rel) and os.path.isfile(os.path.join(c, *rel.split("/"))):
            kept[rel] = prev
    if not a.dry_run:
        for rel, k in kept.items():
            if k.get("project") or not k["incoming"]:
                continue
            sv = conflict_path(c, rel)
            try:
                os.makedirs(os.path.dirname(sv), exist_ok=True)
                put_file(srcs[rel], sv)
                k["saved"] = os.path.relpath(sv, c).replace(os.sep, "/")
            except (OSError, KeyError) as e:
                print("FAILED saving the incoming %s: %s" % (rel, e))
        for rel, prev in items.items():
            if rel not in kept and prev.get("saved") and safe_rel(prev["saved"]):
                sv = os.path.join(c, *prev["saved"].split("/"))
                try:
                    os.remove(sv)
                    rmdirs_up(sv, os.path.join(c, "claude-kit", "state", "conflicts"))
                except OSError:
                    pass
        if kept or items or acked:
            jwrite(cfile, {"v": 1, "items": kept, "acked": {r: v for r, v in acked.items() if r in rec or r in old or r.startswith("project:")}})
        os.makedirs(os.path.dirname(man), exist_ok=True)
        tmp = man + ".%d.tmp" % os.getpid()
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write("".join(("%s\t%s\t%s\n" % (k, v, recn[k])) if recn.get(k) else ("%s\t%s\n" % (k, v)) for k, v in sorted(rec.items())))
        os.replace(tmp, man)
        prune_backups(c)
    print("RESULT new=%d upd=%d same=%d repl=%d gone=%d fail=%d conf=%d cnew=%d" % (n_new, n_upd, n_same, n_repl, n_gone, n_fail, sum(1 for k in kept.values() if not k.get("project")), cnew))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
