#!/usr/bin/env python3
"""kit-install-files.py: the file-copy loop of install.sh in ONE process (stdlib only).

install.sh used to spawn about seven processes per kit file (sha256sum twice, awk, dirname, mkdir, cp, ...): about 4 minutes for ~1000 files on Git Bash
(process creation is slow there). This does the same work in-process: same layout, same decisions, same backups, same installed.tsv.

  kit-install-files.py --kit KITDIR --config CONFIGDIR --always-on "load-rbxdev-vault unload-rbxdev-vault ..." [--dry-run]

Layout (relative to CONFIGDIR = ~/.claude):
  tools|systems|skillpack/<r>   -> claude-kit/<sub>/<r>
  agents/<r>                    -> claude-kit/vault-mode/.claude/agents/<r>
  mode/<r>                      -> claude-kit/vault-mode/<r>
  skills/<name>/<r>             -> skills/<name>/<r> when <name> is in --always-on, else claude-kit/vault-mode/.claude/skills/<name>/<r>
Per file (kit wins, nothing of yours is lost): missing -> copy (new); identical -> unchanged; equal to the sha recorded in the old installed.tsv -> copy over (updated);
anything else (you edited it) -> your version is copied to claude-kit/backup/<date>/<rel> (.2, .3 ... if that exists), then the kit version is copied (replaced-yours).
installed.tsv is rewritten (sorted, unique, "<rel>\\t<sha256>") unless --dry-run. Last stdout line: "RESULT new=N upd=N same=N repl=N". Exit 0.
"""
import argparse
import datetime
import hashlib
import os
import shutil
import sys

SUBS = ("agents", "skills", "mode", "tools", "systems", "skillpack")
SM = "claude-kit/vault-mode"


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
                if n.endswith(".pyc"):
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
                if len(p) >= 2 and p[0] not in old:      # awk: first match wins
                    old[p[0]] = p[1]
    except OSError:
        pass
    return old


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--kit", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--always-on", default="load-rbxdev-vault unload-rbxdev-vault update-rbxdev-vault update-check-rbxdev-vault uninstall-rbxdev-vault")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    kit, c = os.path.abspath(a.kit), os.path.abspath(a.config)
    ao = set(a.always_on.split())
    man = os.path.join(c, "claude-kit", "installed.tsv")
    old = read_manifest(man)
    bk_root = os.path.join(c, "claude-kit", "backup", datetime.date.today().strftime("%Y-%m-%d"))
    n_new = n_upd = n_same = n_repl = 0
    rec = set()
    for sub, r in kit_files(kit):
        src = os.path.join(kit, *r.split("/"))
        rel = rel_of(sub, r, ao)
        dst = os.path.join(c, *rel.split("/"))
        ns = sha(src)
        if not os.path.exists(dst):
            if not a.dry_run:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy(src, dst)
            n_new += 1
        else:
            ds = sha(dst) if os.path.isfile(dst) else ""
            if ds == ns:
                n_same += 1
            elif old.get(rel) and ds == old[rel]:
                if not a.dry_run:
                    shutil.copy(src, dst)
                n_upd += 1
            else:
                if not a.dry_run:
                    bk, i = os.path.join(bk_root, *rel.split("/")), 1
                    while os.path.lexists(bk):
                        i += 1
                        bk = os.path.join(bk_root, *rel.split("/")) + ".%d" % i
                    os.makedirs(os.path.dirname(bk), exist_ok=True)
                    if os.path.isfile(dst):
                        shutil.copy2(dst, bk)
                    shutil.copy(src, dst)
                n_repl += 1
        rec.add("%s\t%s" % (rel, ns))
    if not a.dry_run:
        os.makedirs(os.path.dirname(man), exist_ok=True)
        tmp = man + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write("".join(x + "\n" for x in sorted(rec)))
        os.replace(tmp, man)
    print("RESULT new=%d upd=%d same=%d repl=%d" % (n_new, n_upd, n_same, n_repl))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
