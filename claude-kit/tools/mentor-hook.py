#!/usr/bin/env python3
"""mentor-hook - opt-in UserPromptSubmit hook: runs vault-find on the user's prompt and injects the top 3 vault matches
(skill, agent, KB topic, creator hub, Manager topic, combined brain, Roblox skill-pack skill = /rbx <name>) as short "Suggestion" lines. Stdlib only, no network.

  mentor-hook.py hook                       Claude Code hook entry (reads the event JSON on stdin; prints nothing when no good match)
  mentor-hook.py suggest "<prompt>" [--vault PATH ...] [--debug]     same logic from the command line (tests)
  mentor-hook.py install-hooks | uninstall-hooks [--config DIR]       merge into / remove from <config>/settings.json (backup first)
  mentor-hook.py status [--config DIR]

Silent (prints nothing, exit 0) when: the prompt is short, a slash command or a question about the hook itself, fewer than 2
meaningful words, the best score is below the threshold, no vault index is cached yet (it then refreshes the index in the
background for the next prompt), or the file <config>/state/mentor-hook.off exists. Output is capped at about 300 tokens.
The index is the one vault-find.py builds (cached; rebuilt when a vault's git HEAD changes).
"""
import datetime, importlib.util, json, os, subprocess, sys

HOOK_ID = "claude-kit/tools/mentor-hook"   # substring that identifies our hook entry in settings.json
MIN_SCORE = 9.0                              # calibrated against vault-find scores (see tests in the kit docs)
MAX_CHARS = 1100                             # about 300 tokens
HERE = os.path.dirname(os.path.abspath(__file__))


def cfg_dir(override=None):
    d = override or os.environ.get("CLAUDE_CONFIG_DIR")
    return os.path.abspath(d) if d else os.path.join(os.path.expanduser("~"), ".claude")


def load_vf():
    spec = importlib.util.spec_from_file_location("vault_find", os.path.join(HERE, "vault-find.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def lum_on(c):
    return os.path.exists(os.path.join(c, "state", "low-usage-mode-rbxdev-vault.on"))


def cached_records(vf, vaults):
    """Records from the cached index only (never scan inline: a cold scan is too slow for a hook). -> (recs, missing)"""
    import hashlib
    recs, missing = [], []
    for side, v in vaults:
        key = hashlib.sha1(v.encode("utf-8")).hexdigest()[:10]
        cp = os.path.join(vf.cache_dir(), "vault-find-%s.json" % key)
        try:
            d = json.load(open(cp, encoding="utf-8"))
            if d.get("v") not in (3, 4):
                raise ValueError
        except (OSError, ValueError):
            missing.append(v)
            continue
        if d.get("stamp") != vf.head_stamp(v):
            missing.append(v)   # stale: still used now, refreshed in the background
        for r in d["recs"]:
            r = dict(r)
            r["vault"] = v
            recs.append(r)
    return recs, missing


def refresh_background(vf, vaults):
    args = [sys.executable, "-I", os.path.join(HERE, "vault-find.py"), "refresh index", "-n", "1", "--reindex"]
    for _, v in vaults:
        args += ["--vault", v]
    try:
        kw = dict(stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
        if os.name == "nt":
            kw["creationflags"] = 0x00000008 | 0x00000200   # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
        else:
            kw["start_new_session"] = True
        subprocess.Popen(args, **kw)
    except Exception:
        pass


def short(s, n):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 3].rstrip() + "..."


def suggest(prompt, vault_args=None, debug=False, c=None):
    c = c or cfg_dir()
    if os.path.exists(os.path.join(c, "state", "mentor-hook.off")):
        return ""
    p = (prompt or "").strip()
    if len(p) < 12 or p.startswith("/") or "mentor-hook" in p:
        return ""
    vf = load_vf()
    if len(set(vf.toks(p))) < 2:
        return ""
    vaults = vf.find_vaults(vault_args or [])
    if not vaults:
        return ""
    recs, missing = cached_records(vf, vaults)
    if missing:
        refresh_background(vf, [x for x in vaults if x[1] in missing])
    for side, v in vaults:   # the user's protected Games/ area is never cached: scan it live (small), reusable items rank first
        if side == "roblox":
            for r in vf.scan_games(side, v) + vf.scan_systems(side) + [x for x in vf.scan_skillpack(side) if x.get("built")]:
                r = dict(r)
                r["vault"] = r.get("root") or v
                recs.append(r)
    if not recs:
        return ""
    recs = [r for r in recs if r["type"] in ("skill", "agent", "kb", "manager", "creator", "brain", "game", "reusable", "system", "skillpack")]
    ranked = vf.rank(recs, p[:600], vf.picks_set(vaults))
    if debug:
        for s, r in ranked[:5]:
            sys.stderr.write("%.1f %s %s\n" % (s, r["type"], r["path"]))
    seen, uniq = set(), []
    for s, r in ranked:
        k = (r["type"], r["name"].split("/")[-1].lower())
        if s >= MIN_SCORE and k not in seen:
            seen.add(k)
            uniq.append((s, r))
    ranked = uniq[: (2 if lum_on(c) else 3)]
    if not ranked:
        return ""
    lines = ["Vault mentor: possible matches for this prompt (vault-find; use only if relevant, read the note before applying):"]
    for s, r in ranked:
        name = r["name"].split("/")[-1]
        kind = r["type"]
        if kind == "skillpack":
            lines.append("Suggestion: [skillpack] /rbx %s - %s" % (name, short(r["desc"].split(" - ", 1)[-1], 90)))
        else:
            lines.append("Suggestion: [%s] %s - %s/%s - %s" % (kind, name, os.path.basename(r["vault"]), r["path"], short(r["desc"], 90)))
    out = "\n".join(lines)
    return out if len(out) <= MAX_CHARS else out[: MAX_CHARS - 3] + "..."


# ---- settings.json merge (same safety rules as low-usage-mode-rbxdev-vault: backup first, idempotent, keeps everything else)
def read_settings(path):
    if not os.path.exists(path):
        return {}
    txt = open(path, "r", encoding="utf-8-sig").read()
    if not txt.strip():
        return {}
    data = json.loads(txt)
    if not isinstance(data, dict):
        raise ValueError("settings.json is not a JSON object")
    return data


def write_settings(path, data):
    if os.path.exists(path):
        bak = path + ".mentor-bak-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        with open(path, "rb") as s, open(bak, "wb") as d:
            d.write(s.read())
        print("backup: " + bak)
    tmp = path + ".mentor-tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, path)


def is_ours(h):
    return isinstance(h, dict) and HOOK_ID in str(h.get("command", ""))


def present(data):
    groups = (data.get("hooks") or {}).get("UserPromptSubmit") or []
    return any(is_ours(h) for g in groups if isinstance(g, dict) for h in (g.get("hooks") or []))


def install(c):
    path = os.path.join(c, "settings.json")
    try:
        data = read_settings(path)
    except Exception as e:
        print("mentor hook: NOT changed, settings.json is not valid JSON (%s). Fix it first." % type(e).__name__)
        return 2
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        print("mentor hook: NOT changed, settings.json 'hooks' is not an object.")
        return 2
    if present(data):
        print("mentor hook: already installed (no change)")
        return 0
    cmd = 'sh "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/claude-kit/tools/mentor-hook" hook'
    hooks.setdefault("UserPromptSubmit", []).append({"hooks": [{"type": "command", "command": cmd, "timeout": 10}]})
    os.makedirs(c, exist_ok=True)
    write_settings(path, data)
    print("mentor hook: installed in " + path + " (UserPromptSubmit). Start a new session or open /hooks to load it. Mute without uninstalling: create " + os.path.join(c, "state", "mentor-hook.off"))
    return 0


def uninstall(c):
    path = os.path.join(c, "settings.json")
    try:
        data = read_settings(path)
    except Exception as e:
        print("mentor hook: NOT changed, settings.json is not valid JSON (%s)." % type(e).__name__)
        return 2
    hooks = data.get("hooks")
    if not isinstance(hooks, dict) or not present(data):
        print("mentor hook: not found (no change)")
        return 0
    groups = hooks.get("UserPromptSubmit") or []
    keep = []
    for g in groups:
        if isinstance(g, dict) and isinstance(g.get("hooks"), list):
            g["hooks"] = [h for h in g["hooks"] if not is_ours(h)]
            if not g["hooks"]:
                continue
        keep.append(g)
    if keep:
        hooks["UserPromptSubmit"] = keep
    else:
        del hooks["UserPromptSubmit"]
    if not hooks:
        del data["hooks"]
    write_settings(path, data)
    print("mentor hook: removed from " + path)
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    cfg = None
    if "--config" in rest:
        i = rest.index("--config")
        cfg = rest[i + 1]
        rest = rest[:i] + rest[i + 2:]
    c = cfg_dir(cfg)
    if cmd == "hook":
        try:
            raw = sys.stdin.read() if not sys.stdin.isatty() else ""
            prompt = json.loads(raw).get("prompt", "") if raw.strip() else ""
            out = suggest(prompt, c=c)
        except Exception:
            return 0   # a hook must never break the user's prompt
        if out:
            try:
                sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass
            sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": out}}, ensure_ascii=False) + "\n")
        return 0
    if cmd == "suggest":
        debug = "--debug" in rest
        vaults, words, i = [], [], 0
        while i < len(rest):
            if rest[i] == "--vault":
                vaults.append(rest[i + 1])
                i += 2
            elif rest[i] == "--debug":
                i += 1
            else:
                words.append(rest[i])
                i += 1
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
        out = suggest(" ".join(words), vaults, debug, c)
        print(out if out else "(silent: no good match)")
        return 0
    if cmd == "install-hooks":
        return install(c)
    if cmd == "uninstall-hooks":
        return uninstall(c)
    if cmd == "status":
        try:
            print("mentor hook: %s (config %s)" % ("installed" if present(read_settings(os.path.join(c, "settings.json"))) else "not installed", c))
        except Exception as e:
            print("mentor hook: unreadable settings (%s)" % type(e).__name__)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
