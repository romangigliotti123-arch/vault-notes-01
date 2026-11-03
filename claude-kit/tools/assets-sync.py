#!/usr/bin/env python3
"""assets-sync.py - keep <vault>/Assets in sync with the asset mirror on the host PC's Tailscale-only share (stdlib only; Windows/macOS/Linux).

  python assets-sync.py --vault <vault folder> [--base URL ...] [--verify] [--dry-run] [--jobs 6] [--verbose]

What it does: fetches assets-manifest.json from the share (path, size, sha256 per file), compares it with <vault>/Assets, downloads only new or
changed files (to <file>.part with HTTP Range resume, sha256-verified, then renamed atomically), and deletes files that the previous sync tracked but the
manifest no longer lists (only inside <vault>/Assets). Assets never go through git or GitHub.
Quiet when nothing changed (no output). One line if the share is unreachable (Tailscale off): the sync is skipped and the exit code is still 0.

WEBSITE (zip) MODE: with --base <url> (or a base remembered from an earlier run) the tool first reads <base>/repos.json (the vault's list of asset sources: each
entry is a folder URL holding SHA256SUMS and <type>.zip, for example a GitHub release or the website's /assets folder; adding a source never needs a client change),
and falls back to <base>/assets/SHA256SUMS (old layout). HTTP redirects (301/302/303/307/308, at most 3, also to another host such as GitHub's download servers) are
followed and the Range header is kept, so resume works. If sources exist it syncs per-type zips instead of single files: compares each zip's sha256 with the one it extracted last time (state: <vault>/Assets/.assets-sync-zip-state.json),
downloads only changed zips (HTTP Range resume, into <vault>/Assets/.zip-cache), verifies sha256, extracts into a temp folder inside Assets and swaps it in
atomically as <vault>/Assets/<type>. Nothing outside <vault>/Assets is ever created or deleted. Extra option: --only 3d-models,catalog (zip mode only).
The share mode above is unchanged and is tried first for every base; zip mode is used when the base has no assets-manifest.version.
Exit codes: 0 ok / nothing to do / share unreachable (skipped); 1 some files failed (run again to resume); 2 usage error (vault missing).
State (what was synced, for incremental runs and deletions): <vault>/Assets/.assets-sync-state.json. Lock: <vault>/Assets/.assets-sync.lock.
"""
import argparse, concurrent.futures as cf, hashlib, http.client, json, os, re, shutil, stat, sys, threading, time, urllib.parse, zipfile

DEFAULT_BASES = ["https://raw.githubusercontent.com/romangigliotti123-arch/vault-kit-01/main", "https://vault-hhmi60uo.netlify.app"]
STATE_NAME = ".assets-sync-state.json"
ZSTATE_NAME = ".assets-sync-zip-state.json"
ZCACHE = ".zip-cache"
LOCK_NAME = ".assets-sync.lock"
CHUNK = 256 * 1024
BAD_CHARS = re.compile(r'[<>:"|?*\x00-\x1f\\]')
T0 = time.time()


def fs(p):
    """Filesystem path; on Windows use the \\\\?\\ prefix so paths longer than 260 chars work."""
    p = os.path.abspath(p)
    if os.name == "nt" and not p.startswith("\\\\?\\"):
        p = "\\\\?\\UNC\\" + p[2:] if p.startswith("\\\\") else "\\\\?\\" + p
    return p


def say(msg):
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()


def safe_rel(rel):
    """True only for a clean relative path that stays inside Assets (no .., no absolute, no drive, no odd characters)."""
    if not isinstance(rel, str) or not rel or rel.startswith("/") or BAD_CHARS.search(rel):
        return False
    parts = rel.split("/")
    for p in parts:
        if p in ("", ".", "..") or p.endswith(" ") or p.endswith("."):
            return False
    return True


def sha256_file(path):
    h = hashlib.sha256()
    with open(fs(path), "rb") as f:
        while True:
            b = f.read(1024 * 1024)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def split_base(base):
    u = urllib.parse.urlsplit(base)
    https = u.scheme == "https"
    return u.hostname, u.port or (443 if https else 80), u.path.rstrip("/"), https


MAX_REDIRECTS = 3
REDIRECT_CODES = (301, 302, 303, 307, 308)


class Http(object):
    """One keep-alive connection per worker thread. Follows up to MAX_REDIRECTS redirects (also cross-host; never https -> http) and keeps the request headers (Range)."""

    def __init__(self, base, timeout=60):
        self.host, self.port, self.prefix, self.https = split_base(base)
        self.timeout = timeout
        self.conn = None
        self.extra = None      # single-use connection to a redirect target; stays open until the response is read (closed by the next request or close())

    @staticmethod
    def _shut(c):
        if c is not None:
            try:
                c.close()
            except Exception:
                pass

    def _open(self):
        self._shut(self.conn)
        cls = http.client.HTTPSConnection if self.https else http.client.HTTPConnection
        self.conn = cls(self.host, self.port, timeout=self.timeout)

    def close(self):
        self._shut(self.conn)
        self.conn = None
        self._shut(self.extra)
        self.extra = None

    def _own(self, url, headers):
        """GET on the keep-alive connection of the base host. Retries once on a stale keep-alive connection."""
        for attempt in (0, 1):
            if self.conn is None:
                self._open()
            try:
                self.conn.request("GET", url, headers=dict(headers or {}))
                return self.conn.getresponse()
            except (http.client.HTTPException, OSError):
                self._shut(self.conn)
                self.conn = None
                if attempt:
                    raise
        raise OSError("unreachable")

    def request(self, path, headers=None):
        """GET path (relative to the base). Returns the open response (caller must read it)."""
        self._shut(self.extra)
        self.extra = None
        host, port, https, target = self.host, self.port, self.https, self.prefix + path
        for hop in range(MAX_REDIRECTS + 1):
            if hop == 0:
                r = self._own(target, headers)
            else:
                cls = http.client.HTTPSConnection if https else http.client.HTTPConnection
                self._shut(self.extra)
                self.extra = cls(host, port, timeout=self.timeout)
                self.extra.request("GET", target, headers=dict(headers or {}))
                r = self.extra.getresponse()
            if r.status not in REDIRECT_CODES:
                return r
            loc = r.getheader("Location")
            r.read()
            if not loc:
                raise OSError("HTTP %d without Location for %s" % (r.status, path))
            if hop == MAX_REDIRECTS:
                raise OSError("more than %d redirects for %s" % (MAX_REDIRECTS, path))
            cur = "%s://%s:%d%s" % ("https" if https else "http", host, port, target)
            u = urllib.parse.urlsplit(urllib.parse.urljoin(cur, loc))
            if u.scheme not in ("http", "https") or not u.hostname or (https and u.scheme != "https"):
                raise OSError("redirect to %s refused" % (loc[:80],))
            host, https = u.hostname, u.scheme == "https"
            port = u.port or (443 if https else 80)
            target = u.path or "/"
            if u.query:
                target += "?" + u.query
        raise OSError("redirect loop for %s" % path)

    def get_bytes(self, path, limit=200 * 1024 * 1024):
        r = self.request(path)
        if r.status != 200:
            r.read()
            raise OSError("HTTP %d for %s" % (r.status, path))
        data = r.read(limit)
        return data


def pick_base(bases, verbose):
    """First base whose assets-manifest.version answers. Returns (base, version_line) or (None, None)."""
    for b in bases:
        h = Http(b, timeout=8)
        try:
            line = h.get_bytes("/assets-manifest.version", 4096).decode("utf-8", "replace").strip()
            if line:
                return b, line
        except Exception as e:
            if verbose:
                say("assets-sync: %s not reachable (%s)" % (b, e))
        finally:
            h.close()
    return None, None


class State(object):
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()
        self.version = None
        self.files = {}  # rel -> [size, mtime_ns, sha256]
        self.dirty = False
        self.last_flush = time.time()
        try:
            with open(fs(path), "r", encoding="utf-8") as f:
                d = json.load(f)
            self.version = d.get("version")
            self.files = d.get("files", {})
        except (OSError, ValueError):
            pass

    def flush(self, force=False):
        with self.lock:
            if not self.dirty and not force:
                return
            tmp = self.path + ".tmp"
            data = json.dumps({"format": 1, "version": self.version, "files": self.files}, separators=(",", ":")).encode("utf-8")
            with open(fs(tmp), "wb") as f:
                f.write(data)
            os.replace(fs(tmp), fs(self.path))
            self.dirty = False
            self.last_flush = time.time()

    def set(self, rel, size, mtime_ns, sha):
        with self.lock:
            self.files[rel] = [size, mtime_ns, sha]
            self.dirty = True

    def drop(self, rel):
        with self.lock:
            self.files.pop(rel, None)
            self.dirty = True


def ensure_exclude(vault):
    """Keep Assets/ out of git on a clone (the repo .gitignore has it too; this covers clones from before that line existed)."""
    gd = os.path.join(vault, ".git")
    if not os.path.isdir(gd):
        return
    try:
        ex = os.path.join(gd, "info", "exclude")
        os.makedirs(os.path.dirname(ex), exist_ok=True)
        cur = ""
        if os.path.exists(ex):
            with open(ex, "r", encoding="utf-8", errors="replace") as f:
                cur = f.read()
        if not any(l.strip() in ("Assets/", "/Assets/", "/Assets") for l in cur.splitlines()):
            with open(ex, "a", encoding="utf-8") as f:
                f.write(("" if cur.endswith("\n") or not cur else "\n") + "/Assets/\n")
    except OSError:
        pass


def pid_alive(pid):
    if pid <= 0:
        return False
    if os.name == "nt":
        try:
            import ctypes
            k = ctypes.windll.kernel32
            h = k.OpenProcess(0x1000, False, pid)   # PROCESS_QUERY_LIMITED_INFORMATION
            if not h:
                return False
            code = ctypes.c_ulong(0)
            ok = k.GetExitCodeProcess(h, ctypes.byref(code))
            k.CloseHandle(h)
            return bool(ok) and code.value == 259     # STILL_ACTIVE
        except Exception:
            return True
    try:
        os.kill(pid, 0)
        return True
    except PermissionError:
        return True
    except OSError:
        return False


def acquire_lock(assets):
    lp = os.path.join(assets, LOCK_NAME)
    for _ in range(2):
        try:
            fd = os.open(fs(lp), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, ("%d %d\n" % (os.getpid(), int(time.time()))).encode())
            os.close(fd)
            return lp
        except FileExistsError:
            try:
                age = time.time() - os.path.getmtime(fs(lp))
            except OSError:
                continue
            try:
                with open(fs(lp), "r") as f:
                    pid = int((f.read().split() or ["0"])[0])
            except (OSError, ValueError):
                pid = 0
            if age < 3 * 3600 and pid_alive(pid):
                return None            # a live run holds the lock; a crashed/killed run (dead pid) is taken over
            try:
                os.remove(fs(lp))
            except OSError:
                return None
    return None


def prune_empty_dirs(assets, start):
    d = os.path.dirname(start)
    root = os.path.abspath(assets)
    while os.path.abspath(d) != root and os.path.abspath(d).startswith(root + os.sep):
        try:
            os.rmdir(fs(d))
        except OSError:
            break
        d = os.path.dirname(d)


def remove_file(path):
    try:
        os.remove(fs(path))
    except PermissionError:
        try:
            os.chmod(fs(path), 0o700)
            os.remove(fs(path))
        except OSError:
            return False
    except FileNotFoundError:
        pass
    except OSError:
        return False
    return True


def main():
    ap = argparse.ArgumentParser(description="Sync <vault>/Assets from the host share.")
    ap.add_argument("--vault", required=True)
    ap.add_argument("--base", action="append", help="base URL (repeatable or comma separated): the vault-kit raw URL or the website (they list the asset sources in repos.json), or the private share; default: the built-in list")
    ap.add_argument("--verify", action="store_true", help="re-hash every local file instead of trusting the saved state")
    ap.add_argument("--dry-run", action="store_true", help="only report what would change")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--only", help="website (zip) mode only: comma separated asset types to sync, e.g. catalog,audio")
    ap.add_argument("--throttle-kbps", type=int, default=0, help=argparse.SUPPRESS)  # test aid: slow each download
    a = ap.parse_args()
    vault = os.path.abspath(os.path.expanduser(a.vault))
    if not os.path.isdir(vault):
        say("assets-sync: vault folder not found: %s" % vault)
        return 2
    bases = []
    assets = os.path.join(vault, "Assets")
    cand = list(a.base or [])
    if not cand:
        rb = remembered_base(assets)
        cand = ([rb] if rb else []) + DEFAULT_BASES
    for b in cand:
        bases += [x.strip().rstrip("/") for x in b.split(",") if x.strip()]
    mode, base, vline = None, None, None
    for b in bases:
        base, vline = pick_base([b], a.verbose)
        if base:
            mode = "share"
            break
        zb, sums, where = pick_zip_base(b, a.verbose)
        if zb:
            mode, base, vline = "zip", zb, (sums, where)
            break
    if base is None:
        say("assets-sync: no asset source reachable (offline? the private share needs Tailscale); skipped, Assets unchanged")
        return 0
    os.makedirs(fs(assets), exist_ok=True)
    ensure_exclude(vault)
    lockp = acquire_lock(assets) if not a.dry_run else None
    if lockp is None and not a.dry_run:
        say("assets-sync: another assets-sync is running; skipped")
        return 0
    try:
        if mode == "zip":
            return run_zip(a, vault, assets, base, vline)
        return run(a, vault, assets, base, vline)
    finally:
        if lockp:
            try:
                os.remove(fs(lockp))
            except OSError:
                pass


# ---------------------------------------------------------------- website (zip) mode
SUMS_RE = re.compile(r"^([0-9a-fA-F]{64})[ \t]+\*?([A-Za-z0-9][A-Za-z0-9._-]*\.zip)[ \t]*$")


def remembered_base(assets):
    try:
        with open(fs(os.path.join(assets, ZSTATE_NAME)), "r", encoding="utf-8") as f:
            b = json.load(f).get("base")
        return b if isinstance(b, str) and b.startswith(("http://", "https://")) else None
    except (OSError, ValueError):
        return None


def pick_zip_base(base, verbose):
    """Website mode probe. Asset folders come from <base>/repos.json ("assets": [{"dir": URL}]) or, for the old layout, <base>/assets.
    Each folder holds SHA256SUMS with lines '<sha256>  <type>.zip'. Returns (base, {type: sha}, {type: folder URL}) or (None, None, None)."""
    dirs = []
    h = Http(base, timeout=15)
    try:
        j = json.loads(h.get_bytes("/repos.json", 262144).decode("utf-8", "replace"))
        for e in (j.get("assets") or []):
            d = e.get("dir") if isinstance(e, dict) else None
            if isinstance(d, str) and d.startswith(("http://", "https://")) and d.rstrip("/") not in dirs:
                dirs.append(d.rstrip("/"))
    except Exception as e:
        if verbose:
            say("assets-sync: %s has no usable /repos.json (%s)" % (base, e))
    finally:
        h.close()
    if not dirs:
        dirs = [base.rstrip("/") + "/assets"]
    sums, where = {}, {}
    for d in dirs:
        hd = Http(d, timeout=15)
        try:
            txt = hd.get_bytes("/SHA256SUMS", 1024 * 1024).decode("utf-8", "replace")
            for line in txt.splitlines():
                m = SUMS_RE.match(line.strip())
                if m and m.group(2)[:-4] not in sums:      # first listed source wins for a type
                    sums[m.group(2)[:-4]] = m.group(1).lower()
                    where[m.group(2)[:-4]] = d
        except Exception as e:
            if verbose:
                say("assets-sync: %s has no SHA256SUMS (%s)" % (d, e))
        finally:
            hd.close()
    if sums:
        return base, sums, where
    return None, None, None


def rmtree_force(path):
    def onerr(func, p, exc):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except OSError:
            pass
    if os.path.lexists(fs(path)):
        shutil.rmtree(fs(path), onerror=onerr)


def download_zip(base, name, sha, cache_dir, verbose):
    """Download <base>/<name>.zip (base = a folder URL from repos.json) to cache_dir/<name>.zip (resumes cache_dir/<name>.zip.part), verifies sha256. Returns the zip path."""
    final = os.path.join(cache_dir, name + ".zip")
    part = final + ".part"
    os.makedirs(fs(cache_dir), exist_ok=True)
    h = Http(base, timeout=120)
    last = None
    try:
        for attempt in range(4):
            try:
                have = os.path.getsize(fs(part)) if os.path.exists(fs(part)) else 0
                if attempt == 3:
                    remove_file(part)
                    have = 0
                hdr = {"Range": "bytes=%d-" % have} if have else {}
                r = h.request("/" + urllib.parse.quote(name + ".zip"), hdr)
                mode = "ab"
                if r.status == 206 and have:
                    total = have + int(r.getheader("Content-Length", "0"))
                    if verbose:
                        say("assets-sync: resuming %s.zip from byte %d" % (name, have))
                elif r.status == 200:
                    mode, have = "wb", 0
                    total = int(r.getheader("Content-Length", "0"))
                elif r.status == 416:
                    r.read()
                    if sha256_file(part) == sha:
                        break
                    remove_file(part)
                    raise OSError("range not satisfiable; restarting")
                else:
                    r.read()
                    raise OSError("HTTP %d" % r.status)
                got = 0
                with open(fs(part), mode) as f:
                    while True:
                        b = r.read(CHUNK)
                        if not b:
                            break
                        f.write(b)
                        got += len(b)
                if total and have + got != total:
                    raise OSError("incomplete (%d of %d bytes)" % (have + got, total))
                if sha256_file(part) != sha:
                    remove_file(part)
                    raise OSError("sha256 mismatch")
                break
            except (OSError, http.client.HTTPException) as e:
                last = e
                h.close()
                time.sleep(0.5 + attempt)
        else:
            raise OSError("download of %s.zip failed: %s" % (name, last))
        if sha256_file(part) != sha:
            remove_file(part)
            raise OSError("sha256 mismatch for %s.zip" % name)
        os.replace(fs(part), fs(final))
        return final
    finally:
        h.close()


def extract_zip_atomic(zip_path, assets, name):
    """Extract <name>/... from the zip into Assets/.extract-<name>, then swap it in as Assets/<name>. Returns the file count."""
    tmp = os.path.join(assets, ".extract-" + name)
    old = os.path.join(assets, ".old-" + name)
    dest = os.path.join(assets, name)
    rmtree_force(tmp)
    rmtree_force(old)
    os.makedirs(fs(tmp))
    n = 0
    troot = os.path.realpath(tmp)
    with zipfile.ZipFile(fs(zip_path)) as zf:
        for zi in zf.infolist():
            nm = zi.filename.replace("\\", "/")
            isdir = nm.endswith("/")
            nm = nm.rstrip("/")
            if not nm or not safe_rel(nm) or nm.split("/")[0] != name:
                raise OSError("unsafe or unexpected path in zip: %r" % zi.filename)
            if (zi.external_attr >> 16) & 0o170000 == 0o120000:
                continue            # never create symlinks
            target = os.path.join(tmp, *nm.split("/"))
            chk = os.path.realpath(target if isdir else os.path.dirname(target))
            if chk != troot and not chk.startswith(troot + os.sep):
                raise OSError("zip path escapes Assets: %r" % zi.filename)
            if isdir:
                os.makedirs(fs(target), exist_ok=True)
                continue
            os.makedirs(fs(os.path.dirname(target)), exist_ok=True)
            with zf.open(zi) as src, open(fs(target), "wb") as out:
                shutil.copyfileobj(src, out, CHUNK)
            n += 1
    new_root = os.path.join(tmp, name)
    if not os.path.isdir(fs(new_root)):
        os.makedirs(fs(new_root))
    if os.path.lexists(fs(dest)):
        os.replace(fs(dest), fs(old))
    os.replace(fs(new_root), fs(dest))
    rmtree_force(old)
    rmtree_force(tmp)
    return n


def run_zip(a, vault, assets, base, srcs):
    sums, where = srcs
    zpath = os.path.join(assets, ZSTATE_NAME)
    try:
        with open(fs(zpath), "r", encoding="utf-8") as f:
            zs = json.load(f)
    except (OSError, ValueError):
        zs = {}
    zips = zs.get("zips", {}) if isinstance(zs.get("zips"), dict) else {}
    only = None
    if a.only:
        only = [x.strip() for x in a.only.split(",") if x.strip()]
        bad = [x for x in only if x not in sums]
        if bad:
            say("assets-sync: unknown type(s) %s; available: %s" % (", ".join(bad), ", ".join(sorted(sums))))
            return 2
    types = [t for t in sorted(sums) if (only is None or t in only) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", t)]
    need = [t for t in types if zips.get(t) != sums[t] or not os.path.isdir(fs(os.path.join(assets, t)))]
    if a.dry_run:
        say("assets-sync (dry run, website mode): %d zip(s) to download (%s), %d up to date" % (len(need), ", ".join(need) or "-", len(types) - len(need)))
        return 0

    def save():
        tmp = zpath + ".tmp"
        with open(fs(tmp), "w", encoding="utf-8") as f:
            json.dump({"format": 1, "mode": "zip", "base": base, "zips": zips, "updated": int(time.time())}, f, indent=1)
        os.replace(fs(tmp), fs(zpath))

    if not need:
        save()
        if a.verbose:
            say("assets-sync: up to date (%d zip types, website mode)" % len(types))
        return 0
    say("assets-sync: website mode %s: %d zip(s) to fetch: %s" % (base, len(need), ", ".join(need)))
    if a.verbose:
        for t in need:
            say("assets-sync:   %s from %s" % (t, where[t]))
    cache = os.path.join(assets, ZCACHE)
    failed = 0
    for t in need:
        try:
            t1 = time.time()
            zp = download_zip(where[t], t, sums[t], cache, a.verbose)
            n = extract_zip_atomic(zp, assets, t)
            remove_file(zp)
            zips[t] = sums[t]
            save()
            say("assets-sync: %s ok (%d files, %.0fs)" % (t, n, time.time() - t1))
        except Exception as e:
            failed += 1
            say("assets-sync: %s FAILED: %s (run again to resume)" % (t, e))
    try:
        os.rmdir(fs(cache))
    except OSError:
        pass
    save()
    say("assets-sync: website mode done: %d fetched, %d failed, %d already up to date, %.0fs" % (len(need) - failed, failed, len(types) - len(need), time.time() - T0))
    return 1 if failed else 0


def run(a, vault, assets, base, vline):
    state = State(os.path.join(assets, STATE_NAME))
    remote_version = vline.split()[0]
    if state.version == remote_version and state.files and not a.verify:
        # manifest unchanged since the last fully successful sync: rebuild the list from the saved state, no 8 MB download
        man = {"version": remote_version, "files": [{"path": k, "size": v[0], "sha256": v[2]} for k, v in state.files.items()]}
    else:
        http0 = Http(base)
        try:
            man = json.loads(http0.get_bytes("/assets-manifest.json").decode("utf-8"))
        except Exception as e:
            say("assets-sync: could not read the manifest (%s); skipped" % e)
            return 0
        finally:
            http0.close()
    files = man.get("files", [])
    entries = {}
    rejected = 0
    for f in files:
        rel = f.get("path")
        if not safe_rel(rel) or not isinstance(f.get("size"), int) or not re.fullmatch(r"[0-9a-f]{64}", str(f.get("sha256", ""))):
            rejected += 1
            continue
        entries[rel] = (f["size"], f["sha256"])
    aroot = os.path.realpath(assets)

    def inside(rp):
        return rp == aroot or rp.startswith(aroot + os.sep)

    # 1. decide what is up to date
    need = []        # rel needing download
    ok_count = 0
    for rel, (size, sha) in sorted(entries.items()):
        p = os.path.join(assets, *rel.split("/"))
        try:
            st = os.stat(fs(p))
        except OSError:
            need.append(rel)
            continue
        if st.st_size != size:
            need.append(rel)
            continue
        rec = state.files.get(rel)
        if not a.verify and rec and rec[0] == size and rec[2] == sha and rec[1] == st.st_mtime_ns:
            ok_count += 1
            continue
        try:
            good = sha256_file(p) == sha
        except OSError:
            good = False
        if good:
            state.set(rel, size, st.st_mtime_ns, sha)
            ok_count += 1
        else:
            need.append(rel)
    stale = [r for r in state.files if r not in entries]
    first = len(state.files) == 0 and ok_count == 0
    if a.dry_run:
        say("assets-sync (dry run): %d to download (%.1f MB), %d to delete, %d up to date" % (len(need), sum(entries[r][0] for r in need) / 1e6, len(stale), ok_count))
        return 0
    if not need and not stale:
        state.version = man.get("version")
        state.flush(force=state.dirty)
        if a.verbose:
            say("assets-sync: up to date (%d files)" % len(entries))
        return 0
    total_dl = sum(entries[r][0] for r in need)
    if first or total_dl > 200 * 1024 * 1024:
        say("assets-sync: %s %d files (%.2f GB) from %s into %s ..." % ("first sync, downloading" if first else "downloading", len(need), total_dl / 1e9, base, assets))

    # 2. deletions (only files this tool tracked, only inside Assets)
    removed = 0
    for rel in stale:
        if not safe_rel(rel):
            state.drop(rel)
            continue
        p = os.path.join(assets, *rel.split("/"))
        if not inside(os.path.realpath(os.path.dirname(p))):
            state.drop(rel)
            continue
        if remove_file(p):
            removed += 1
            prune_empty_dirs(assets, p)
        state.drop(rel)

    # 3. downloads
    stats = {"done": 0, "bytes": 0, "resumed": 0, "failed": 0}
    slock = threading.Lock()
    failures = []
    tl = threading.local()
    last_progress = [time.time()]

    def conn():
        if not hasattr(tl, "h"):
            tl.h = Http(base)
        return tl.h

    def fetch(rel):
        size, sha = entries[rel]
        dest = os.path.join(assets, *rel.split("/"))
        ddir = os.path.dirname(dest)
        os.makedirs(fs(ddir), exist_ok=True)
        if not inside(os.path.realpath(ddir)) or os.path.islink(fs(dest)):
            raise OSError("refusing path outside Assets: %s" % rel)
        part = dest + ".part"
        url = "/assets/" + urllib.parse.quote(rel, safe="/")
        last_err = None
        for attempt in range(3):
            try:
                have = 0
                try:
                    have = os.path.getsize(fs(part))
                except OSError:
                    have = 0
                if have > size or attempt == 2:
                    remove_file(part)
                    have = 0
                hdr = {"Range": "bytes=%d-" % have} if have else {}
                r = conn().request(url, hdr)
                mode = "ab"
                if r.status == 206 and have:
                    cr = r.getheader("Content-Range", "")
                    if not cr.startswith("bytes %d-" % have):
                        r.read()
                        conn().close()
                        remove_file(part)
                        raise OSError("bad Content-Range %s" % cr)
                    with slock:
                        stats["resumed"] += 1
                elif r.status == 200:
                    mode = "wb"      # server ignored Range (or none requested): start over
                    have = 0
                elif r.status == 416:
                    r.read()
                    remove_file(part)
                    raise OSError("range not satisfiable, restarting")
                else:
                    r.read()
                    raise OSError("HTTP %d" % r.status)
                got = 0
                with open(fs(part), mode) as f:
                    while True:
                        b = r.read(CHUNK)
                        if not b:
                            break
                        f.write(b)
                        got += len(b)
                        if a.throttle_kbps:
                            time.sleep(len(b) / 1024.0 / a.throttle_kbps)
                if have + got != size:
                    raise OSError("incomplete (%d of %d bytes)" % (have + got, size))
                if sha256_file(part) != sha:
                    remove_file(part)
                    raise OSError("sha256 mismatch")
                os.replace(fs(part), fs(dest))
                st = os.stat(fs(dest))
                state.set(rel, size, st.st_mtime_ns, sha)
                with slock:
                    stats["done"] += 1
                    stats["bytes"] += size
                return
            except (OSError, http.client.HTTPException) as e:
                last_err = e
                conn().close()
                time.sleep(0.5 + attempt)
        raise OSError(str(last_err))

    def task(rel):
        try:
            fetch(rel)
        except Exception as e:
            with slock:
                stats["failed"] += 1
                failures.append("%s: %s" % (rel, e))
        now = time.time()
        if now - last_progress[0] > 60:
            with slock:
                if now - last_progress[0] > 60:
                    last_progress[0] = now
                    say("assets-sync: %d/%d files, %.2f GB ..." % (stats["done"] + stats["failed"], len(need), stats["bytes"] / 1e9))
                    try:
                        os.utime(fs(os.path.join(assets, LOCK_NAME)), None)
                    except OSError:
                        pass
            state.flush()

    # biggest first keeps the tail short
    order = sorted(need, key=lambda r: -entries[r][0])
    try:
        with cf.ThreadPoolExecutor(max_workers=max(1, a.jobs)) as ex:
            list(ex.map(task, order))
    finally:
        if not stats["failed"]:
            state.version = man.get("version")
        state.flush(force=True)

    secs = time.time() - T0
    msg = "assets-sync: %d downloaded (%.1f MB%s), %d removed, %d up to date, %d files total, %.0fs" % (
        stats["done"], stats["bytes"] / 1e6, ", %d resumed" % stats["resumed"] if stats["resumed"] else "", removed, ok_count, len(entries), secs)
    if rejected:
        msg += ", %d manifest entries rejected (unsafe path)" % rejected
    if stats["failed"]:
        msg += ", %d FAILED (run again to retry/resume)" % stats["failed"]
    say(msg)
    for f in failures[:5]:
        say("  failed: " + f)
    return 1 if stats["failed"] else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
