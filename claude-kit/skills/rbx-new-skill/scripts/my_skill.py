#!/usr/bin/env python3
"""my_skill.py: helper of rbx-new-skill. Makes, checks and loads YOUR OWN skills and agents. Stdlib only, no network, never edits a vault-owned file.

  my_skill.py where                                  vault folder, My-Skills/, My-Agents/ and what is in them
  my_skill.py overlap "<goal in one line>"           closest existing vault skills/agents and your own (word overlap); says when one already does the job
  my_skill.py new skill|agent my-<name> [--force]    start from the template: My-Skills/my-<name>/SKILL.md or My-Agents/my-<name>.md
  my_skill.py check <path> [--json]                  PASS/WARN/FAIL lines: frontmatter, name rule, description <= 400 chars, trigger overlap, bold footer, secrets, tokens vs the 10,000 session limit
  my_skill.py selftest <path> --yes P --yes P --yes P --no Q --no Q     tiny trigger self-test (3 prompts it should match, 2 it should not)
  my_skill.py sync                                   copy My-Skills/ and My-Agents/ into <vault>/.claude (what the vault update also does)
  my_skill.py remove my-<name> --yes                 delete one of YOUR items (source and copy)
Options: --vault DIR (default: the registered vault folder), --config DIR (default $CLAUDE_CONFIG_DIR or ~/.claude).
Exit 1 when a check FAILs. Names of your items always start with my-; the vault's start with rbx-, so they never collide."""
import io
import json
import math
import os
import re
import shutil
import subprocess
import sys

LIMIT = 10000                   # vault session limit (tokens, ceil(chars/4)) from the vault budget
DESC_MAX = 400
NAME_RX = re.compile(r"my-[a-z0-9]+(?:-[a-z0-9]+)*")
MODELS = ("haiku", "sonnet", "opus", "inherit")
EFFORTS = ("low", "medium", "high", "xhigh", "max")
WRITE_TOOLS = ("write", "edit", "bash", "notebookedit", "multiedit")
STOP = set("a an the and or of to for in on at is are be it its this that with from by as my me i you your we our do does can will would should please want need make makes making use used using when then than so if not no into out up down over any all some one new just also have has had get got set let like about what which who how why where".split())
SECRET_RX = [
    (re.compile(r"sk-[A-Za-z0-9_-]{20,}"), "API key (sk-...)"),
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"), "GitHub token"),
    (re.compile(r"AK​IA[0-9A-Z]{16}"), "AWS key id"),
    (re.compile(r"AIza[0-9A-Za-z_-]{30,}"), "Google API key"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"), "Slack token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIV​ATE KEY-----"), "private key"),
    (re.compile(r"_\|WARNING:-DO-NOT-SHARE", re.I), "Roblox .ROBLOSECURITY cookie"),
    (re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*[\"']?[A-Za-z0-9+/_=-]{12,}"), "password/secret/token assignment"),
    (re.compile(r"(?i)bearer\s+[A-Za-z0-9._-]{20,}"), "bearer token"),
]
HERE = os.path.dirname(os.path.abspath(__file__))
out = []


def say(s=""):
    print(s)


def cfg_dir(a):
    d = a.get("config") or os.environ.get("CLAUDE_CONFIG_DIR")
    if d:
        return os.path.abspath(os.path.expanduser(d))
    if os.environ.get("CLAUDE_KIT_HOME"):
        return os.path.join(os.path.expanduser(os.environ["CLAUDE_KIT_HOME"]), ".claude")
    return os.path.join(os.path.expanduser("~"), ".claude")


def read(p):
    try:
        with io.open(p, encoding="utf-8-sig", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def frontmatter(text):
    """-> (dict, body, first_line_ok). Plain/quoted single-line values and folded blocks; not a general YAML parser."""
    t = text.replace("\r\n", "\n")
    if not t.startswith("---\n"):
        return {}, t, False
    end = t.find("\n---", 4)
    if end < 0:
        return {}, t, False
    head, body = t[4:end], t[end + 4:].lstrip("\n")
    fm, key, buf = {}, None, []

    def flush():
        if key is not None:
            v = " ".join(x.strip() for x in buf).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            fm[key] = v
    for line in head.split("\n"):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            flush()
            key, v = m.group(1), m.group(2)
            buf = [] if v in (">", "|", ">-", "|-") else [v]
        elif key is not None:
            buf.append(line)
    flush()
    return fm, body, True


def toks(n):
    return int(math.ceil(n / 4.0)) if n > 0 else 0


def words(s):
    ws = []
    for w in re.findall(r"[a-z0-9][a-z0-9'+#/-]*", s.lower()):
        w = w.strip("'-/")
        if len(w) < 3 or w in STOP:
            continue
        for suf in ("ing", "ed", "es", "s"):
            if w.endswith(suf) and len(w) - len(suf) >= 4:
                w = w[:-len(suf)]
                break
        ws.append(w)
    return set(ws)


# ---------------------------------------------------------------- locations
def vault_of(a):
    if a.get("vault"):
        return os.path.abspath(os.path.expanduser(a["vault"]))
    env = os.environ.get("CLAUDES_VAULT")
    if env and os.path.isdir(env):
        return os.path.abspath(env)
    vm = os.path.join(cfg_dir(a), "claude-kit", "tools", "vault-mode.py")
    if os.path.isfile(vm):
        try:
            r = subprocess.run([sys.executable, "-I", vm, "--config", cfg_dir(a), "home"], capture_output=True, text=True, timeout=30)
            h = r.stdout.strip().splitlines()[0] if r.stdout.strip() else ""
            if h and os.path.isdir(h):
                return h
        except (OSError, subprocess.SubprocessError, IndexError):
            pass
    return None


def need_vault(a):
    v = vault_of(a)
    if not v:
        say("FAIL no vault folder found. Run this from a Claude session in the vault folder, or pass --vault <folder>. Your files live in <vault>/My-Skills and <vault>/My-Agents.")
        sys.exit(2)
    return v


def vault_items(a, vault):
    """{name: (kind, description, path)} of everything the vault installed (skills and agents)"""
    items = {}
    bases = []
    if vault:
        bases.append(os.path.join(vault, ".claude"))
    bases.append(os.path.join(cfg_dir(a), "claude-kit", "vault-mode", ".claude"))
    for b in bases:
        sd, ad = os.path.join(b, "skills"), os.path.join(b, "agents")
        for n in sorted(os.listdir(sd)) if os.path.isdir(sd) else []:
            p = os.path.join(sd, n, "SKILL.md")
            if os.path.isfile(p) and not NAME_RX.fullmatch(n) and n not in items:
                items[n] = ("skill", frontmatter(read(p))[0].get("description", ""), p)
        for f in sorted(os.listdir(ad)) if os.path.isdir(ad) else []:
            if f.endswith(".md") and not NAME_RX.fullmatch(f[:-3]) and f[:-3] not in items:
                items[f[:-3]] = ("agent", frontmatter(read(os.path.join(ad, f)))[0].get("description", ""), os.path.join(ad, f))
    sk = os.path.join(cfg_dir(a), "skills")          # the three always-on commands
    for n in ("rbx-update", "rbx-check", "rbx-uninstall"):
        p = os.path.join(sk, n, "SKILL.md")
        if os.path.isfile(p) and n not in items:
            items[n] = ("skill", frontmatter(read(p))[0].get("description", ""), p)
    return items


def own_items(vault):
    """{name: (kind, description, path)} of YOUR items in My-Skills/ and My-Agents/"""
    items = {}
    sd, ad = os.path.join(vault, "My-Skills"), os.path.join(vault, "My-Agents")
    for n in sorted(os.listdir(sd)) if os.path.isdir(sd) else []:
        p = os.path.join(sd, n, "SKILL.md")
        if os.path.isfile(p):
            items[n] = ("skill", frontmatter(read(p))[0].get("description", ""), p)
    for f in sorted(os.listdir(ad)) if os.path.isdir(ad) else []:
        if f.endswith(".md"):
            items[f[:-3]] = ("agent", frontmatter(read(os.path.join(ad, f)))[0].get("description", ""), os.path.join(ad, f))
    return items


def hints(a):
    """extra trigger phrases the vault keeps per skill (tools/data/skill-match-hints.json), used only to make the overlap check smarter"""
    for p in (os.path.join(cfg_dir(a), "claude-kit", "tools", "data", "skill-match-hints.json"), os.path.join(HERE, "..", "..", "..", "tools", "data", "skill-match-hints.json")):
        try:
            d = json.load(io.open(p, encoding="utf-8"))
            return {k: v for k, v in d.items() if isinstance(v, str) and not k.startswith("_")}
        except (OSError, ValueError):
            continue
    return {}


def kind_dir(vault, kind):
    return os.path.join(vault, "My-Skills" if kind == "skill" else "My-Agents")


# ---------------------------------------------------------------- scoring
def score(prompt_words, item_words):
    if not prompt_words:
        return 0.0
    return len(prompt_words & item_words) / float(len(prompt_words))


def rank(prompt, pool, hint):
    pw = words(prompt)
    rows = []
    for n, (k, d, p) in pool.items():
        iw = words(n.replace("-", " ") + " " + d + " " + hint.get(n, ""))
        rows.append((score(pw, iw), len(pw & iw), n, k))
    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
    return rows


# ---------------------------------------------------------------- commands
def cmd_where(a):
    v = vault_of(a)
    if not v:
        say("No vault folder found (pass --vault <folder>).")
        return 2
    say("vault folder: " + v)
    for d, k in (("My-Skills", "skill"), ("My-Agents", "agent")):
        own = [n for n, (kk, _, _) in own_items(v).items() if kk == k]
        say("%s/: %s (%s)" % (d, os.path.join(v, d), ", ".join(own) if own else "empty"))
    return 0


def cmd_overlap(a):
    goal = a["args"][0] if a["args"] else ""
    if not goal.strip():
        say("FAIL overlap needs the goal in one line, in quotes.")
        return 2
    v = vault_of(a)
    pool = dict(vault_items(a, v))
    if v:
        pool.update(own_items(v))
    if not pool:
        say("WARN no installed vault skills found to compare with; check PICKS/rbx-list by hand.")
        return 0
    rows = rank(goal, pool, hints(a))[:3]
    for s, n, name, k in rows:
        say("%-26s %-5s overlap %.2f (%d shared words)" % ("/" + name if k == "skill" else name, k, s, n))
    best = rows[0]
    if best[0] >= 0.5 and best[1] >= 2:
        say("OVERLAP: /%s probably already does this (%.2f). Tell the user and ask whether they still want their own." % (best[2], best[0]))
    else:
        say("OVERLAP: none close (best %.2f). A new item is justified; keep its description distinct from the three above." % best[0])
    return 0


def template(kind):
    p = os.path.join(HERE, "..", "templates", "skill.md" if kind == "skill" else "agent.md")
    return read(p)


def cmd_new(a):
    if len(a["args"]) < 2 or a["args"][0] not in ("skill", "agent"):
        say("usage: my_skill.py new skill|agent my-<name>")
        return 2
    kind, name = a["args"][0], a["args"][1]
    if not NAME_RX.fullmatch(name) or len(name) > 64:
        say("FAIL name %r: must start with my-, then lowercase letters, digits and single hyphens (max 64). Example: my-patch-notes" % name)
        return 1
    v = need_vault(a)
    if name in vault_items(a, v):
        say("FAIL %s is a vault name." % name)
        return 1
    dest = os.path.join(kind_dir(v, kind), name, "SKILL.md") if kind == "skill" else os.path.join(kind_dir(v, kind), name + ".md")
    if os.path.exists(dest) and not a.get("force"):
        say("FAIL %s already exists. Edit it, or pick another name (--force replaces it)." % dest)
        return 1
    t = template(kind)
    if not t:
        say("FAIL template missing next to this script (templates/).")
        return 1
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with io.open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.replace("my-NAME", name))
    say("created %s (fill every FILL-IN marker, then run check)" % dest)
    return 0


def check_item(a, path, quiet=False):
    """returns (results, info). results = [(PASS|WARN|FAIL, text)]"""
    res = []

    def ck(level, text):
        res.append((level, text))
    text = read(path)
    if not text:
        ck("FAIL", "cannot read %s" % path)
        return res, {}
    fm, body, fm_ok = frontmatter(text)
    is_skill = os.path.basename(path) == "SKILL.md"
    kind = "skill" if is_skill else "agent"
    folder = os.path.basename(os.path.dirname(path)) if is_skill else os.path.basename(path)[:-3]
    ck("PASS" if fm_ok else "FAIL", "frontmatter: file starts with --- and has a closing ---" if fm_ok else "frontmatter: the file must start with a line --- and close it with ---")
    name, desc = fm.get("name", ""), fm.get("description", "")
    ck("PASS" if name else "FAIL", "name: %s" % (name or "missing"))
    if name:
        ck("PASS" if NAME_RX.fullmatch(name) and len(name) <= 64 else "FAIL", "name rule: starts with my-, lowercase letters/digits/hyphens, max 64 (%s)" % name)
        ck("PASS" if name == folder else "FAIL", "name equals the %s (%s)" % ("folder name" if is_skill else "file name", folder))
    v = vault_of(a)
    vi = vault_items(a, v)
    ck("PASS" if name not in vi and folder not in vi else "FAIL", "name does not collide with a vault skill or agent")
    ck("PASS" if desc else "FAIL", "description present")
    ck("PASS" if len(desc) <= DESC_MAX else "FAIL", "description length %d <= %d" % (len(desc), DESC_MAX))
    ck("PASS" if len(desc) >= 40 or not desc else "WARN", "description is specific enough (%d chars)" % len(desc))
    ck("PASS" if re.search(r"(?i)\buse\b|\bwhen\b|\bsay\b|/my-", desc) or not desc else "WARN", "description names when to use it (a 'Use when/for ...' phrase or the words the user says)")
    ck("PASS" if "\n" not in (re.search(r"(?m)^description:.*$", text) or [""])[0] else "FAIL", "description is one line")
    marks = re.findall(r"FILL-IN|TODO|ONE LINE", text)
    ck("PASS" if not marks else "FAIL", "no template marker left (FILL-IN / TODO / ONE LINE)" if not marks else "template marker still in the file: %s" % ", ".join(sorted(set(marks))))
    lab = [l for l in ("**Done**", "**You**", "**Next**") if l in body]
    ck("PASS" if len(lab) == 3 else ("FAIL" if is_skill else "WARN"), "bold footer labels **Done** / **You** / **Next** in the %s" % ("body" if is_skill else "body (agents report to the caller; labels are optional)"))
    if kind == "agent":
        ck("PASS" if fm.get("model", "") in MODELS else "FAIL", "agent model is one of %s (%s)" % ("/".join(MODELS), fm.get("model", "missing")))
        ck("PASS" if fm.get("effort", "") in EFFORTS or not fm.get("effort") else "FAIL", "agent effort is one of %s (%s)" % ("/".join(EFFORTS), fm.get("effort") or "default"))
        tools = [t.strip() for t in re.split(r"[,\s]+", fm.get("tools", "")) if t.strip()]
        ck("PASS" if tools else "FAIL", "agent lists its tools (minimal list, no tools line = ALL tools)")
        writers = [t for t in tools if t.lower().split("(")[0] in WRITE_TOOLS]
        ck("PASS" if not writers else "WARN", "agent is read-only" if not writers else "agent can change things (%s): only keep these if the job needs them, and say why in the body" % ", ".join(writers))
    ow = re.findall(r"(?i)(?:\.claude/(?:skills|agents)/rbx-|skills/rbx-[a-z-]+/SKILL\.md|agents/rbx-[a-z-]+\.md|claude-kit/(?:tools|skills|mode))", body)
    ck("PASS" if not ow else "FAIL", "does not edit vault-owned files" if not ow else "mentions vault-owned paths (%s): your items must never edit the vault's own files" % ", ".join(sorted(set(ow))[:3]))
    leaks = [label for rx, label in SECRET_RX if rx.search(text)]
    ck("PASS" if not leaks else "FAIL", "no secrets in the file" if not leaks else "looks like a secret: %s (remove it; keys never go in a skill)" % ", ".join(leaks))
    lines = body.count("\n") + 1
    ck("PASS" if lines <= 120 else ("WARN" if lines <= 500 else "FAIL"), "body length %d lines (aim <= 120, hard limit 500)" % lines)
    # overlap with the existing descriptions (disjoint triggers)
    pool = dict(vi)
    if v:
        pool.update({k: x for k, x in own_items(v).items() if k != name})
    worst = (0.0, "")
    mine = words(desc)
    for n, (k, d, p) in pool.items():
        ow2 = words(d)
        j = len(mine & ow2) / float(len(mine | ow2) or 1)
        if j > worst[0]:
            worst = (j, n)
    ck("PASS" if worst[0] < 0.35 else ("WARN" if worst[0] < 0.5 else "FAIL"), "description is distinct from the others (closest: %s, similarity %.2f)" % (worst[1] or "none", worst[0]))
    # tokens
    listing = toks(len(name) + 2 + len(desc))
    body_t = toks(len(body))
    base = None
    try:
        import importlib.util
        for p in (os.path.join(HERE, "..", "..", "rbx-bench", "scripts", "vault_cost.py"), os.path.join(cfg_dir(a), "claude-kit", "vault-mode", ".claude", "skills", "rbx-bench", "scripts", "vault_cost.py")):
            if os.path.isfile(p):
                spec = importlib.util.spec_from_file_location("vault_cost_ns", p)
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                base = m.measure_installed(cfg_dir(a), 4.0, 600, 3)["totals"]["session_with_load_tokens"] if os.path.isdir(os.path.join(cfg_dir(a), "claude-kit", "vault-mode")) else None
                break
    except Exception:
        base = None
    others = sum(toks(len(n2) + 2 + len(d2)) for n2, (k2, d2, p2) in (own_items(v).items() if v else []) if n2 != name)
    info = {"name": name, "kind": kind, "desc_chars": len(desc), "listing_tokens": listing, "body_tokens": body_t, "lines": lines, "vault_session_tokens": base, "your_other_items_tokens": others}
    if base is not None:
        total = base + others + listing
        ck("PASS" if total <= LIMIT - 500 else ("WARN" if total <= LIMIT else "FAIL"), "session total ~%d tokens of the %d limit (vault %d + your other items %d + this one %d; every skill/agent adds its listing to EVERY session)" % (total, LIMIT, base, others, listing))
        info["session_total"] = total
    else:
        ck("WARN", "vault session size unknown here (rbx-bench or the installed store not found): this item adds ~%d tokens to every session, ~%d more when it runs; the limit for the whole session is %d" % (listing, body_t, LIMIT))
    ck("PASS", "this %s costs ~%d tokens in every session (name + description) and ~%d tokens when it runs" % (kind, listing, body_t))
    return res, info


def cmd_check(a):
    if not a["args"]:
        say("usage: my_skill.py check <path to SKILL.md or agent .md or the skill folder>")
        return 2
    p = os.path.abspath(a["args"][0])
    if os.path.isdir(p):
        p = os.path.join(p, "SKILL.md")
    res, info = check_item(a, p)
    if a.get("json"):
        say(json.dumps({"results": res, "info": info}, indent=1))
    else:
        for lv, tx in res:
            say("%s %s" % (lv, tx))
        say("SUMMARY: %d PASS, %d WARN, %d FAIL" % tuple(sum(1 for r in res if r[0] == k) for k in ("PASS", "WARN", "FAIL")))
    return 1 if any(r[0] == "FAIL" for r in res) else 0


def cmd_selftest(a):
    if not a["args"]:
        say("usage: my_skill.py selftest <path> --yes <prompt> x3 --no <prompt> x2")
        return 2
    p = os.path.abspath(a["args"][0])
    if os.path.isdir(p):
        p = os.path.join(p, "SKILL.md")
    fm = frontmatter(read(p))[0]
    is_skill = os.path.basename(p) == "SKILL.md"
    name = fm.get("name") or (os.path.basename(os.path.dirname(p)) if is_skill else os.path.basename(p)[:-3])
    v = vault_of(a)
    pool = dict(vault_items(a, v))
    if v:
        pool.update(own_items(v))
    pool[name] = ("skill" if is_skill else "agent", fm.get("description", ""), p)
    hint = hints(a)
    yes, no = a.get("yes", []), a.get("no", [])
    bad = 0
    if len(yes) < 3 or len(no) < 2:
        say("WARN the self-test wants 3 prompts it should match (--yes) and 2 it should not (--no); got %d and %d." % (len(yes), len(no)))
        bad += 1
    for q in yes:
        rows = rank(q, pool, hint)
        top = rows[0]
        mine = [r for r in rows if r[2] == name][0]
        ok = top[2] == name and mine[1] >= 2
        say("%s should match: %r -> best %s (%.2f, %d shared words); this item %.2f" % ("PASS" if ok else "FAIL", q, top[2], top[0], top[1], mine[0]))
        bad += 0 if ok else 1
    for q in no:
        rows = rank(q, pool, hint)
        top = rows[0]
        mine = [r for r in rows if r[2] == name][0]
        ok = top[2] != name or mine[1] < 2
        say("%s should NOT match: %r -> best %s (%.2f, %d shared words); this item %.2f" % ("PASS" if ok else "FAIL", q, top[2], top[0], top[1], mine[0]))
        bad += 0 if ok else 1
    say("SELF-TEST (word-overlap estimate, not the real model): %s. If a line FAILs, change the description's trigger words and run it again." % ("OK" if not bad else "%d problem(s)" % bad))
    return 1 if bad else 0


def cmd_sync(a):
    v = need_vault(a)
    vm = os.path.join(cfg_dir(a), "claude-kit", "tools", "vault-mode.py")
    if not os.path.isfile(vm):
        vm = os.path.join(HERE, "..", "..", "..", "tools", "vault-mode.py")
    if not os.path.isfile(vm):
        say("FAIL vault-mode.py not found (is the vault kit installed? run /rbx-update).")
        return 1
    r = subprocess.run([sys.executable, "-I", vm, "--config", cfg_dir(a), "load", "--project", v, "--quiet"], capture_output=True, text=True, timeout=300)
    say((r.stdout + r.stderr).strip() or "synced")
    own = own_items(v)
    miss = [n for n, (k, d, p) in own.items() if not os.path.exists(os.path.join(v, ".claude", "skills" if k == "skill" else "agents", n if k == "skill" else n + ".md"))]
    if r.returncode or miss:
        say("FAIL not copied into .claude: %s" % (", ".join(miss) or "vault-mode.py exit %d" % r.returncode))
        return 1
    say("OK %d of your item%s in %s. Skills usually show up at once; if not, type /reload-skills, or start a new Claude session in the vault folder." % (len(own), " is" if len(own) == 1 else "s are", os.path.join(v, ".claude")))
    return 0


def cmd_remove(a):
    if not a["args"] or not NAME_RX.fullmatch(a["args"][0]):
        say("usage: my_skill.py remove my-<name> --yes   (only your own my- items can be removed)")
        return 2
    n = a["args"][0]
    v = need_vault(a)
    own = own_items(v)
    if n not in own:
        say("FAIL %s is not in My-Skills/ or My-Agents/." % n)
        return 1
    if not a.get("yes"):
        say("DRY RUN: would delete %s. Add --yes after the user said yes." % (os.path.dirname(own[n][2]) if own[n][0] == "skill" else own[n][2]))
        return 0
    if own[n][0] == "skill":
        shutil.rmtree(os.path.dirname(own[n][2]))
    else:
        os.remove(own[n][2])
    return cmd_sync(a)


def parse(argv):
    a = {"args": [], "yes": [], "no": []}
    argv = list(argv)
    cmd = ""
    for t in argv:              # the command is the first word that is not an option (options may come before it)
        if not t.startswith("--"):
            prev = argv[argv.index(t) - 1] if argv.index(t) else ""
            if prev not in ("--vault", "--config", "--yes", "--no"):
                cmd = t
                break
    rest = list(argv)
    if cmd:
        rest.pop(argv.index(cmd))
    i = 0
    while i < len(rest):
        t = rest[i]
        if t in ("--vault", "--config") and i + 1 < len(rest):
            a[t[2:]] = rest[i + 1]
            i += 2
        elif t == "--yes" and cmd == "selftest" and i + 1 < len(rest):
            a["yes"].append(rest[i + 1])
            i += 2
        elif t == "--no" and i + 1 < len(rest):
            a["no"].append(rest[i + 1])
            i += 2
        elif t == "--yes" and cmd == "remove":
            a["yes"] = True
            i += 1
        elif t in ("--force", "--json"):
            a[t[2:]] = True
            i += 1
        else:
            a["args"].append(t)
            i += 1
    return cmd, a


def main(argv):
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(errors="replace", encoding="utf-8")
        except Exception:
            pass
    cmd, a = parse(argv)
    fn = {"where": cmd_where, "overlap": cmd_overlap, "new": cmd_new, "check": cmd_check, "selftest": cmd_selftest, "sync": cmd_sync, "remove": cmd_remove}.get(cmd)
    if not fn:
        say(__doc__)
        return 2
    return fn(a) or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
