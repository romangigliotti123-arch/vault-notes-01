#!/usr/bin/env python3
"""games.py - the per-game community helper for /game-dev-workflow. Stdlib only. Never touches anything outside Games/ (and the PROJECT folder, read-only).

Games/ lives in the vault root and is PROTECTED: /vault-update and /vault-update-clean never overwrite or remove it, origin never ships it.
Layout:  Games/README.md (hub)  Games/_profile.json (onboarding answers)  Games/<slug>/{GAME,design,decisions,systems}.md + playtests/ weekly/ critic/  Games/_Reusable/<name>/README.md + code

  games.py where                                       print the Games root that will be used
  games.py profile [--level L --type T] [--reset]      show / store the one-time onboarding answers (level: new|some|experienced; type: free text)
  games.py init <slug> [--pitch TXT] [--genre TXT] [--project DIR] [--rojo]     create Games/<slug>/ from the templates (idempotent: never overwrites a file).
       --rojo also scaffolds a Rojo project (default.project.json, src/server, src/client, src/shared, rokit/selene/stylua configs) in --project DIR, or in Games/<slug>/project/ when no DIR is given (kept in the protected Games/ folder so the code is never lost by a vault update), and records it as `project:` in GAME.md
  games.py system list                                 the kit's tested drop-in systems (PlayerData, Shop, DailyRewards, Analytics, Admin)
  games.py system add <Name> [--game SLUG | --project DIR]   copy a system's src/ into <project>/src/server/Systems/<Name>/ (never overwrites a changed file: writes <file>.new)
  games.py list                                        games with claimed stage, evidence stage, last change
  games.py detect <slug> [--project DIR] [--json]      read the REAL stage from evidence (files, scripts, playtests, critic verdicts, numbers) and compare with GAME.md
  games.py verdict <slug> [--stage S]                  latest critic verdict (GOOD | NOT YET | BAD) for the stage
  games.py advance <slug> --to STAGE [--project DIR]   move GAME.md to STAGE only if the critic's latest verdict for the CURRENT stage is GOOD (and, from prototype on, its file says visual: pass) and the evidence supports it
  games.py reusable add <name> --src PATH --what TXT [--from-game SLUG] [--tested y|n] [--rating N] [--tags TXT]    save a reusable building block
  games.py reusable list
  games.py contribute <name>                           zip a reusable item into ~/vault-contribute/ for the owner (never uploads anything)
Games root: --games DIR, else env GAMES_ROOT, else <vault>/Games (vault = env CLAUDES_VAULT, else ~/Obsidian/claudes-vault).
"""
import argparse, datetime, glob, json, os, re, shutil, sys, zipfile

STAGES = ["idea", "prototype", "playtest", "launch", "growth", "live-ops"]
HERE = os.path.dirname(os.path.abspath(__file__))
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,48}$")


def today():
    return datetime.date.today().isoformat()


def vault_root():
    for c in (os.environ.get("CLAUDES_VAULT"), os.path.join(os.path.expanduser("~"), "Obsidian", "claudes-vault")):
        if c and os.path.isdir(c):
            return os.path.abspath(c)
    return None


def games_root(a):
    if getattr(a, "games", None):
        return os.path.abspath(a.games)
    if os.environ.get("GAMES_ROOT"):
        return os.path.abspath(os.environ["GAMES_ROOT"])
    v = vault_root()
    if not v:
        sys.exit("games.py: vault not found. Set CLAUDES_VAULT, pass --games DIR, or run /vault-update first.")
    return os.path.join(v, "Games")


def template_dir():
    for c in (os.path.join(HERE, "..", "skills", "game-dev-workflow", "templates", "game"),
              os.path.join(HERE, "..", "..", "skills", "game-dev-workflow", "templates", "game")):
        if os.path.isdir(c):
            return os.path.abspath(c)
    sys.exit("games.py: templates not found (is the kit installed? run install.ps1 / install.sh)")


def read(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def write(p, txt):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)


def fm_of(text):
    text = text.replace("\r\n", "\n")
    out = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            for ln in text[4:end].split("\n"):
                m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", ln)
                if m:
                    out[m.group(1)] = m.group(2).strip().strip("\"'")
    return out


def set_fm(text, key, val):
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return "---\n%s: %s\n---\n%s" % (key, val, text)
    end = text.find("\n---", 4)
    head, rest = text[4:end], text[end:]
    if re.search(r"^%s:" % re.escape(key), head, re.M):
        head = re.sub(r"^%s:.*$" % re.escape(key), "%s: %s" % (key, val), head, flags=re.M)
    else:
        head += "\n%s: %s" % (key, val)
    return "---\n" + head + rest


def fill(text, **kw):
    for k, v in kw.items():
        text = text.replace("{{%s}}" % k, v)
    return text


def game_dir(root, slug):
    if not SLUG_RE.match(slug or ""):
        sys.exit("games.py: slug must be lowercase letters, digits and dashes (got %r)" % slug)
    return os.path.join(root, slug)


# ---------------------------------------------------------------- hub
def rebuild_hub(root):
    games = sorted(d for d in os.listdir(root) if os.path.isfile(os.path.join(root, d, "GAME.md"))) if os.path.isdir(root) else []
    re_dir = os.path.join(root, "_Reusable")
    items = sorted(d for d in os.listdir(re_dir) if os.path.isfile(os.path.join(re_dir, d, "README.md"))) if os.path.isdir(re_dir) else []
    lines = ["---", "type: games-hub", "updated: %s" % today(), "---", "# Games (your protected game communities)", "",
             "Each game below is its own cluster in Obsidian's graph (GAME.md hub with design, decisions, systems, playtests, weekly reports, critic verdicts, linked into the Roblox KB). "
             "`/vault-update` and `/vault-update-clean` never touch this folder. Start with `/game-dev-workflow`.", "", "## Games", ""]
    for g in games:
        f = fm_of(read(os.path.join(root, g, "GAME.md")))
        lines.append("- [[%s/GAME|%s]] - stage **%s** - %s" % (g, g, f.get("stage", "?"), f.get("pitch", "")))
    if not games:
        lines.append("- (none yet: run /game-dev-workflow)")
    lines += ["", "## Reusable building blocks (use these first in every new game)", ""]
    for i in items:
        f = fm_of(read(os.path.join(re_dir, i, "README.md")))
        lines.append("- [[_Reusable/%s/README|%s]] - %s (tested: %s, rating: %s, from: %s)" % (i, i, f.get("what", ""), f.get("tested", "?"), f.get("rating", "?"), f.get("from_game", "?")))
    if not items:
        lines.append("- (none yet: finished systems are saved here by the harvest step)")
    write(os.path.join(root, "README.md"), "\n".join(lines) + "\n")


# ---------------------------------------------------------------- commands
def cmd_where(a):
    r = games_root(a)
    print("GAMES=%s%s" % (r, "" if os.path.isdir(r) else " (not created yet)"))


def cmd_profile(a):
    root = games_root(a)
    p = os.path.join(root, "_profile.json")
    if a.reset and os.path.exists(p):
        os.remove(p)
    cur = {}
    try:
        cur = json.loads(read(p) or "{}")
    except ValueError:
        cur = {}
    if a.level or a.type:
        if a.level:
            if a.level not in ("new", "some", "experienced"):
                sys.exit("games.py: --level must be new, some or experienced")
            cur["level"] = a.level
        if a.type:
            cur["type"] = a.type
        cur["set"] = today()
        write(p, json.dumps(cur, indent=1) + "\n")
    print(json.dumps(cur) if cur else "PROFILE: none (first run: ask experience level and game type once, then store with --level/--type)")


def cmd_init(a):
    root = games_root(a)
    gd = game_dir(root, a.slug)
    td = template_dir()
    created = []
    project = os.path.abspath(a.project) if a.project else None
    if getattr(a, "rojo", False):
        project = project or os.path.join(gd, "project")
    kw = dict(slug=a.slug, date=today(), pitch=a.pitch or "TODO one-sentence pitch", genre=a.genre or "TODO", project=project or "TODO")
    for name in sorted(os.listdir(td)):
        src = os.path.join(td, name)
        if not os.path.isfile(src) or name.startswith("_"):
            continue
        dst = os.path.join(gd, name)
        if os.path.exists(dst):
            continue
        write(dst, fill(read(src), **kw))
        created.append(os.path.relpath(dst, root))
    for sub in ("playtests", "weekly", "critic"):
        idx = os.path.join(gd, sub, "README.md")
        if not os.path.exists(idx):
            write(idx, "---\ntype: index\n---\n# %s - %s\n\nBack to [[%s/GAME|%s]]. Notes in this folder: playtest reports / weekly numbers plans / critic verdicts, newest last, one file per date and stage.\n" % (a.slug, sub, a.slug, a.slug))
            created.append(os.path.relpath(idx, root))
    if getattr(a, "rojo", False):
        created += ["(project) " + m for m in scaffold_rojo(project, a.slug)]
    rebuild_hub(root)
    print("GAME=%s\nCREATED=%d file(s)%s" % (gd, len(created), ("\n  " + "\n  ".join(created)) if created else " (already existed, nothing overwritten)"))


def scaffold_rojo(dest, slug):
    """Create a Rojo project skeleton in dest from tools/roblox-project-template. Never overwrites. Returns created relative paths."""
    tpl = os.path.join(HERE, "roblox-project-template")
    if not os.path.isdir(tpl):
        sys.exit("games.py: roblox-project-template not found next to games.py (is the kit installed?)")
    made = []
    for rel in ("default.project.json", "rokit.toml", "stylua.toml", ".gitignore",
                "src/server/Main.server.luau", "src/client/Main.client.luau", "src/shared/Config.luau"):
        dst = os.path.join(dest, *rel.split("/"))
        if os.path.exists(dst):
            continue
        txt = read(os.path.join(tpl, *rel.split("/")))
        if rel == "default.project.json":
            txt = txt.replace('"name": "MyRobloxGame"', '"name": "%s"' % slug)
        write(dst, txt)
        made.append(rel)
    sel = os.path.join(dest, "selene.toml")
    if not os.path.exists(sel):
        std = os.path.join(tpl, "roblox").replace("\\", "/")
        write(sel, 'std = "%s"\n' % std)
        made.append("selene.toml")
    sysdir = os.path.join(dest, "src", "server", "Systems")
    os.makedirs(sysdir, exist_ok=True)
    readme = os.path.join(dest, "README.md")
    if not os.path.exists(readme):
        write(readme, "# %s\n\nRojo project. Edit files in `src/`, then:\n\n- `rokit install` once (tools pinned in rokit.toml)\n- `rojo serve` and click Connect in the Rojo plugin inside Studio (or `rojo build -o %s.rbxl`)\n- `bash %s/luau-check.sh src` (stylua, selene, luau-lsp)\n- add a tested system: `python %s/games.py system add PlayerData --project .`\n\n`src/server` -> ServerScriptService.Server, `src/client` -> StarterPlayer.StarterPlayerScripts.Client, `src/shared` -> ReplicatedStorage.Shared.\n" % (slug, slug, tpl.replace("\\", "/"), HERE.replace("\\", "/")))
        made.append("README.md")
    return made


def systems_root():
    for c in (os.path.join(HERE, "..", "systems"), os.path.join(HERE, "..", "..", "systems")):
        if os.path.isdir(c):
            return os.path.abspath(c)
    sys.exit("games.py: systems library not found (is the kit installed? run install.ps1 / install.sh)")


def game_project(root, slug):
    t = read(os.path.join(game_dir(root, slug), "GAME.md"))
    m = re.search(r"^project:\s*(.+)$", t, re.M)
    v = m.group(1).strip().strip("\"'") if m else ""
    return v if v and v != "TODO" else None


def cmd_system(a):
    sr = systems_root()
    names = sorted(d for d in os.listdir(sr) if os.path.isdir(os.path.join(sr, d, "src")))
    if a.action == "list":
        for n in names:
            f = fm_of(read(os.path.join(sr, n, "README.md")))
            print("%s | %s | tested: %s" % (n, f.get("what", ""), f.get("tested", "?")))
        return
    if a.name not in names:
        sys.exit("games.py: unknown system %r. Available: %s" % (a.name, ", ".join(names)))
    project = a.project
    if not project and a.game:
        project = game_project(games_root(a), a.game)
    if not project:
        sys.exit("games.py: give --project DIR, or --game SLUG whose GAME.md has a project: folder")
    dest = os.path.join(os.path.abspath(project), "src", "server", "Systems", a.name)
    src = os.path.join(sr, a.name, "src")
    new = same = kept = 0
    for fn in sorted(os.listdir(src)):
        s_, d_ = os.path.join(src, fn), os.path.join(dest, fn)
        if not os.path.isfile(s_):
            continue
        if not os.path.exists(d_):
            os.makedirs(dest, exist_ok=True)
            shutil.copy2(s_, d_)
            new += 1
        elif read(d_) == read(s_):
            same += 1
        else:
            shutil.copy2(s_, d_ + ".new")
            kept += 1
    print("SYSTEM=%s\nINTO=%s\nfiles: %d new, %d unchanged, %d differ (kit version saved as .new, yours kept)" % (a.name, dest, new, same, kept))
    print("NEXT: read %s and follow its Setup (require path from a script in src/server: script.Parent.Systems.%s.<Module>). Not tested in live Studio until you have run it there." % (os.path.join(sr, a.name, "README.md"), a.name))


def project_evidence(project):
    ev = {"scripts": 0, "script_lines": 0, "rojo": False, "place_file": False, "docs": [], "playtest_doc": False, "plan": False}
    if not project or not os.path.isdir(project):
        return ev
    for d, dirs, files in os.walk(project):
        dirs[:] = [x for x in dirs if x not in (".git", "node_modules", "Packages", "__pycache__", "Systems", "tests")]  # Systems = copied tested drop-ins (not the game's own code)
        for fn in files:
            low = fn.lower()
            if low.endswith((".lua", ".luau")):
                ev["scripts"] += 1
                ev["script_lines"] += read(os.path.join(d, fn)).count("\n")
            elif low == "default.project.json":
                ev["rojo"] = True
            elif low.endswith((".rbxl", ".rbxlx")):
                ev["place_file"] = True
    for n in ("game-plan.md", "docs/idea.md", "docs/rating.md", "docs/elaboration.md"):
        if os.path.exists(os.path.join(project, n)):
            ev["docs"].append(n)
    ev["plan"] = os.path.exists(os.path.join(project, "game-plan.md"))
    ev["playtest_doc"] = os.path.exists(os.path.join(project, "docs", "PLAYTEST.md"))
    return ev


def verdicts(gd):
    out = []
    for p in sorted(glob.glob(os.path.join(gd, "critic", "*.md"))):
        if os.path.basename(p).lower() == "readme.md":
            continue
        f = fm_of(read(p))
        if f.get("verdict"):
            out.append(dict(file=p, stage=f.get("stage", ""), verdict=f.get("verdict", "").upper(), date=f.get("date", ""), score=f.get("score", ""), visual=f.get("visual", "missing")))
    return out


def detect(root, slug, project=None):
    gd = game_dir(root, slug)
    gm = read(os.path.join(gd, "GAME.md"))
    if not gm:
        return None
    f = fm_of(gm)
    claimed = f.get("stage", "idea")
    project = project or (f.get("project") if f.get("project", "TODO") != "TODO" else None)
    ev = project_evidence(project)
    n_play = len([p for p in glob.glob(os.path.join(gd, "playtests", "*.md")) if os.path.basename(p).lower() != "readme.md"])
    n_week = len([p for p in glob.glob(os.path.join(gd, "weekly", "*.md")) if os.path.basename(p).lower() != "readme.md"])
    vs = verdicts(gd)
    good = {v["stage"] for v in vs if v["verdict"] == "GOOD"}
    published = f.get("published", "").lower() in ("yes", "true", "y") or bool(re.search(r"^\s*-?\s*(place|universe)[ _-]?id:\s*\d+", gm, re.M | re.I))
    has_numbers = bool(re.search(r"\|\s*(D1|D7|CCU|Session|PTR|Visits)[^|]*\|\s*[0-9][0-9.,%]*", gm, re.I))
    reasons = []
    st = "idea"
    if ev["plan"] or ev["docs"] or f.get("pitch", "TODO") != "TODO one-sentence pitch":
        reasons.append("idea: pitch/plan/docs exist")
    if ev["scripts"] >= 3 and ev["script_lines"] >= 150:
        st = "prototype"; reasons.append("prototype: %d scripts, %d lines" % (ev["scripts"], ev["script_lines"]))
    elif ev["scripts"]:
        reasons.append("only %d script(s)/%d lines: still idea (needs >=3 scripts and >=150 lines for prototype)" % (ev["scripts"], ev["script_lines"]))
    if st == "prototype" and (n_play or ev["playtest_doc"]):
        st = "playtest"; reasons.append("playtest: %d playtest report(s) in Games, project PLAYTEST.md=%s" % (n_play, ev["playtest_doc"]))
    if st == "playtest" and "playtest" in good and (published or os.path.exists(os.path.join(gd, "launch.md"))):
        st = "launch"; reasons.append("launch: critic GOOD for playtest and (published or launch.md)")
    if st == "launch" and published and (n_week or has_numbers):
        st = "growth"; reasons.append("growth: published and real numbers/weekly reports exist")
    if st == "growth" and n_week >= 4 and "growth" in good:
        st = "live-ops"; reasons.append("live-ops: >=4 weekly reports and critic GOOD for growth")
    gate = "ok"
    if STAGES.index(claimed if claimed in STAGES else "idea") > STAGES.index(st):
        gate = "CLAIM EXCEEDS EVIDENCE: GAME.md says %s, evidence supports %s" % (claimed, st)
    return dict(slug=slug, claimed=claimed, evidence=st, gate=gate, reasons=reasons, project=project or "none",
                project_evidence=ev, playtests=n_play, weekly=n_week, published=published, numbers_in_game_md=has_numbers,
                critic_verdicts=[dict(stage=v["stage"], verdict=v["verdict"], date=v["date"]) for v in vs],
                studio="not checked here: if Studio MCP tools exist in your tool list, read the open place (scripts, Output, a playtest) and add it to the evidence")


def cmd_detect(a):
    d = detect(games_root(a), a.slug, a.project)
    if d is None:
        sys.exit("games.py: no GAME.md for %r (run: games.py init %s)" % (a.slug, a.slug))
    if a.json:
        print(json.dumps(d, indent=1))
        return
    print("GAME %s | claimed stage: %s | evidence stage: %s | %s" % (d["slug"], d["claimed"], d["evidence"], d["gate"]))
    for r in d["reasons"]:
        print("  - " + r)
    print("  project: %s | playtest reports: %d | weekly reports: %d | published: %s" % (d["project"], d["playtests"], d["weekly"], d["published"]))
    print("  critic: %s" % (", ".join("%s=%s" % (v["stage"], v["verdict"]) for v in d["critic_verdicts"]) or "no verdict yet"))
    print("  studio: " + d["studio"])


def cmd_list(a):
    root = games_root(a)
    if not os.path.isdir(root):
        print("no Games folder yet")
        return
    n = 0
    for g in sorted(os.listdir(root)):
        if os.path.isfile(os.path.join(root, g, "GAME.md")):
            d = detect(root, g)
            n += 1
            print("%s | claimed %s | evidence %s | %s" % (g, d["claimed"], d["evidence"], d["gate"] if d["gate"] != "ok" else "ok"))
    print("(%d game(s))" % n)


def cmd_verdict(a):
    gd = game_dir(games_root(a), a.slug)
    vs = verdicts(gd)
    if a.stage:
        vs = [v for v in vs if v["stage"] == a.stage]
    if not vs:
        print("VERDICT: none (a critic pass is required before this stage can be called done or advanced)")
        return
    v = vs[-1]
    print("VERDICT: %s | stage %s | %s | score %s | %s" % (v["verdict"], v["stage"], v["date"], v["score"], os.path.relpath(v["file"], gd)))


def cmd_advance(a):
    root = games_root(a)
    gd = game_dir(root, a.slug)
    d = detect(root, a.slug, a.project)
    if d is None:
        sys.exit("games.py: no GAME.md for %r" % a.slug)
    if a.to not in STAGES:
        sys.exit("games.py: stage must be one of %s" % ", ".join(STAGES))
    cur = d["claimed"] if d["claimed"] in STAGES else "idea"
    if STAGES.index(a.to) != STAGES.index(cur) + 1:
        sys.exit("BLOCKED: GAME.md stage is %s; the next stage is %s, not %s (stages are never skipped)" % (cur, STAGES[min(STAGES.index(cur) + 1, 5)], a.to))
    vs = [v for v in verdicts(gd) if v["stage"] == cur]
    if not vs:
        sys.exit("BLOCKED: no critic verdict for stage %s. Run /game-dev-critic first." % cur)
    if vs[-1]["verdict"] != "GOOD":
        sys.exit("BLOCKED: latest critic verdict for %s is %s (%s). Apply the top fixes, re-run the critic." % (cur, vs[-1]["verdict"], vs[-1]["date"]))
    if cur != "idea" and vs[-1].get("visual", "missing") != "pass":
        sys.exit("BLOCKED: visual gate not passed for %s (critic file says visual: %s). Status: playable prototype, visuals not polished. Run /game-dev-visual-qa, then a fresh /game-dev-critic." % (cur, vs[-1].get("visual", "missing")))
    if STAGES.index(d["evidence"]) < STAGES.index(a.to) - 1 and a.to != "prototype":
        sys.exit("BLOCKED: evidence only supports stage %s (%s)" % (d["evidence"], "; ".join(d["reasons"][-2:])))
    p = os.path.join(gd, "GAME.md")
    t = set_fm(read(p), "stage", a.to)
    t = set_fm(t, "stage_since", today())
    write(p, t)
    dec = os.path.join(gd, "decisions.md")
    write(dec, read(dec).rstrip() + "\n\n- %s: stage %s -> %s (critic GOOD %s: [[critic/%s]])\n" % (today(), cur, a.to, vs[-1]["date"], os.path.splitext(os.path.basename(vs[-1]["file"]))[0]))
    rebuild_hub(root)
    print("ADVANCED %s: %s -> %s" % (a.slug, cur, a.to))


def cmd_reusable(a):
    root = games_root(a)
    re_dir = os.path.join(root, "_Reusable")
    if a.action == "list":
        if not os.path.isdir(re_dir):
            print("no reusable items yet")
            return
        for i in sorted(os.listdir(re_dir)):
            f = fm_of(read(os.path.join(re_dir, i, "README.md")))
            if f:
                print("%s | %s | tested %s | rating %s | from %s" % (i, f.get("what", ""), f.get("tested", "?"), f.get("rating", "?"), f.get("from_game", "?")))
        return
    if not a.name or not SLUG_RE.match(a.name):
        sys.exit("games.py: reusable name must be lowercase-with-dashes")
    if not a.src or not os.path.exists(a.src):
        sys.exit("games.py: --src PATH (file or folder with the code) is required and must exist")
    if not a.what:
        sys.exit("games.py: --what 'one line: what it does' is required")
    dst = os.path.join(re_dir, a.name)
    os.makedirs(dst, exist_ok=True)
    if os.path.isdir(a.src):
        for item in os.listdir(a.src):
            s, t = os.path.join(a.src, item), os.path.join(dst, item)
            if item in (".git", "node_modules", "__pycache__"):
                continue
            if os.path.isdir(s):
                shutil.copytree(s, t, dirs_exist_ok=True)
            else:
                shutil.copy2(s, t)
    else:
        shutil.copy2(a.src, dst)
    readme = os.path.join(dst, "README.md")
    if not os.path.exists(readme):
        txt = fill(read(os.path.join(template_dir(), "_reusable-README.md.tpl")), name=a.name, what=a.what, date=today(),
                   from_game=a.from_game or "unknown", tested=a.tested or "n", rating=a.rating or "unrated", tags=a.tags or a.name.replace("-", " "))
        write(readme, txt)
    else:
        t = read(readme)
        for k, v in (("what", a.what), ("tested", a.tested), ("rating", a.rating), ("from_game", a.from_game)):
            if v:
                t = set_fm(t, k, v)
        write(readme, t)
    if a.from_game:
        sysf = os.path.join(game_dir(root, a.from_game), "systems.md")
        if os.path.exists(sysf):
            line = "- [[_Reusable/%s/README|%s]] - %s (harvested %s)" % (a.name, a.name, a.what, today())
            t = read(sysf)
            if "_Reusable/%s/README" % a.name not in t:
                write(sysf, t.rstrip() + "\n" + line + "\n")
    rebuild_hub(root)
    print("REUSABLE=%s\nREADME=%s\nNEXT: open the README and fill 'How to use' and 'Tested' with what you actually ran" % (dst, readme))


def cmd_contribute(a):
    root = games_root(a)
    src = os.path.join(root, "_Reusable", a.name)
    if not os.path.isdir(src):
        sys.exit("games.py: no such reusable item %r" % a.name)
    out_dir = os.path.join(os.path.expanduser("~"), "vault-contribute")
    os.makedirs(out_dir, exist_ok=True)
    zp = os.path.join(out_dir, "%s-%s.zip" % (a.name, today()))
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for d, _, files in os.walk(src):
            for fn in files:
                full = os.path.join(d, fn)
                z.write(full, os.path.join(a.name, os.path.relpath(full, src)))
    print("BUNDLE=%s\nNothing was uploaded. To contribute it, send this file to the vault owner (Tailscale file share / scp to the host) and ask them to review it." % zp)


def main():
    ap = argparse.ArgumentParser(description="per-game community helper")
    ap.add_argument("--games")
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("where")
    p = sp.add_parser("profile"); p.add_argument("--level"); p.add_argument("--type"); p.add_argument("--reset", action="store_true")
    p = sp.add_parser("init"); p.add_argument("slug"); p.add_argument("--pitch"); p.add_argument("--genre"); p.add_argument("--project"); p.add_argument("--rojo", action="store_true")
    sp.add_parser("list")
    p = sp.add_parser("system"); p.add_argument("action", choices=["add", "list"]); p.add_argument("name", nargs="?"); p.add_argument("--game"); p.add_argument("--project")
    p = sp.add_parser("detect"); p.add_argument("slug"); p.add_argument("--project"); p.add_argument("--json", action="store_true")
    p = sp.add_parser("verdict"); p.add_argument("slug"); p.add_argument("--stage")
    p = sp.add_parser("advance"); p.add_argument("slug"); p.add_argument("--to", required=True); p.add_argument("--project")
    p = sp.add_parser("reusable"); p.add_argument("action", choices=["add", "list"]); p.add_argument("name", nargs="?")
    p.add_argument("--src"); p.add_argument("--what"); p.add_argument("--from-game", dest="from_game"); p.add_argument("--tested", choices=["y", "n"]); p.add_argument("--rating"); p.add_argument("--tags")
    p = sp.add_parser("contribute"); p.add_argument("name")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    {"where": cmd_where, "profile": cmd_profile, "init": cmd_init, "list": cmd_list, "detect": cmd_detect, "verdict": cmd_verdict,
     "advance": cmd_advance, "reusable": cmd_reusable, "system": cmd_system, "contribute": cmd_contribute}[a.cmd](a)


if __name__ == "__main__":
    main()
