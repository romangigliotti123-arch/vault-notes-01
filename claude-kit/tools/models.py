#!/usr/bin/env python3
"""models.py - the small, strict library of reusable 3D models for /rbx-workflow. Stdlib only. Never touches anything outside Models/ (the PROJECT folder is read-only).

Models/ lives in the VAULT FOLDER (nearest folder at or above the cwd with .claude/vault-mode.json), next to Games/; never in ~/.claude or HOME; in any other folder this tool says to start a session in the vault folder and creates nothing. Created lazily by the first `add`; updates, unload and sync never touch it.
Layout:  Models/README.md (instructions)  Models/INDEX.md (generated, one line per model)  Models/LOG.md (removals)  Models/<category>/<slug>/{model.md, build.luau and/or *.rbxm|*.rbxmx, preview.png}

  models.py where                              print the Models root that will be used
  models.py template                           print a model.md skeleton to fill in
  models.py check <dir|file> [--scores K=V ...]   run the admission rules: PASS or FAIL with every reason (K: quality, reuse, model_gate, placement_gate)
  models.py add <dir|file> [--scores K=V ...]     only after check PASS: copy into the library (replaces a worse duplicate, evicts the lowest when full), rebuild INDEX.md
  models.py find <words>                       search INDEX.md and every model.md; best match first
  models.py list                               every model, one line each
  models.py use <slug> --game <game-slug>      record that a game uses the model
  models.py remove <slug>                      delete a model (logged)
Models root: --models DIR, else env MODELS_ROOT, else <vault folder>/Models; else an error that names the vault folder.
"""
import argparse, datetime, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import games as G  # same folder: project_root, read, write, fm_of, set_fm, fill

MAX_TOTAL, MAX_CAT = 40, 6
MIN_QUALITY, MIN_REUSE, MIN_GENRES, MIN_PARTS, MIN_MATERIALS, MIN_PARAMS = 8.0, 7.0, 3, 10, 2, 2
CATEGORIES = ("prop", "furniture", "building", "vehicle", "nature", "ui3d", "accessory", "tool", "effect", "decor")
KEEP_EXT = (".luau", ".lua", ".md", ".rbxm", ".rbxmx", ".png", ".jpg", ".jpeg", ".json", ".txt")
MAX_FILE = 3 * 1024 * 1024
STOP = set("the and for with from that this into over under made make model small large big simple basic new old for your use used".split())
BAD_CODE = re.compile(r"RemoteEvent|RemoteFunction|FireServer|FireClient|FireAllClients|InvokeServer|OnServerEvent|OnClientEvent|rbxassetid|DataStore|MarketplaceService|ServerScriptService|ServerStorage|ReplicatedStorage|\brequire\s*\(|\bgame\.Players\b|LocalPlayer")
WIP = re.compile(r"\b(todo|tbd|wip|placeholder|lorem|fixme|work in progress|temp)\b", re.I)


def today():
    return datetime.date.today().isoformat()


def models_root(a):
    if getattr(a, "models", None):
        return os.path.abspath(a.models)
    if os.environ.get("MODELS_ROOT"):
        return os.path.abspath(os.environ["MODELS_ROOT"])
    pr = G.project_root()
    if pr:
        return os.path.join(pr, "Models")
    sys.exit(G.not_in_vault("models.py"))


def games_slugs(root):
    gd = os.path.join(os.path.dirname(root), "Games")
    return [d for d in sorted(os.listdir(gd)) if os.path.isfile(os.path.join(gd, d, "GAME.md"))] if os.path.isdir(gd) else []


def num(v):
    try:
        return float(str(v).split("/")[0])
    except ValueError:
        return None


def csv(v):
    return [x.strip() for x in re.split(r"[,;]", v or "") if x.strip() and x.strip() not in ("-", "none")]


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", (s or "").lower()) if len(w) >= 3 and w not in STOP}


def jac(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def entries(root):
    out = []
    for c in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        for s in sorted(os.listdir(os.path.join(root, c))) if os.path.isdir(os.path.join(root, c)) else []:
            p = os.path.join(root, c, s, "model.md")
            if os.path.isfile(p):
                f = G.fm_of(G.read(p))
                f.update(slug=s, category=c, dir=os.path.dirname(p))
                out.append(f)
    return out


def score(f):
    return (num(f.get("quality")) or 0) * 10 + (num(f.get("reuse")) or 0)


def find_src(arg):
    p = os.path.abspath(arg)
    d = os.path.dirname(p) if os.path.isfile(p) else p
    return d, os.path.join(d, "model.md")


def parse_scores(items):
    out = {}
    for it in items or []:
        for part in re.split(r"[,\s]+", it):
            if "=" in part:
                k, v = part.split("=", 1)
                out[k.strip().lower().replace("-", "_")] = v.strip()
    return out


def run_check(arg, scores, root):
    """-> (fails, notes, fm, replace_entry, evict_entry)"""
    d, md = find_src(arg)
    fails, notes = [], []
    if not os.path.isfile(md):
        return ["no model.md in %s" % d], notes, {}, None, None
    fm = G.fm_of(G.read(md))
    fm.update(scores)
    files = [f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]
    code = [f for f in files if f == "build.luau"]
    bins = [f for f in files if f.endswith((".rbxm", ".rbxmx"))]
    if not code and not bins:
        fails.append("no build.luau and no .rbxm/.rbxmx (a model with nothing to build from)")
    for f in files:
        if os.path.getsize(os.path.join(d, f)) > MAX_FILE:
            fails.append("%s is over 3 MB" % f)
    slug, cat = fm.get("slug", ""), fm.get("category", "")
    if not G.SLUG_RE.match(slug):
        fails.append("slug missing or not lowercase-dashes")
    if cat not in CATEGORIES:
        fails.append("category %r not one of: %s" % (cat, ", ".join(CATEGORIES)))
    desc = fm.get("description", "")
    if len(desc) < 25 or not fm.get("name"):
        fails.append("name and a description of at least 25 characters are required")
    if WIP.search(" ".join([fm.get("name", ""), desc, fm.get("status", ""), slug])) or fm.get("status", "final") not in ("final", "stable", ""):
        fails.append("looks like WIP/placeholder (status must be final; no TODO/WIP/placeholder words)")
    q, r = num(fm.get("quality")), num(fm.get("reuse"))
    if q is None or q < MIN_QUALITY:
        fails.append("quality %s < %g/10 (critic/judge score)" % (fm.get("quality", "missing"), MIN_QUALITY))
    if r is None or r < MIN_REUSE:
        fails.append("reuse score %s < %g/10 (how likely it appears in many games)" % (fm.get("reuse", "missing"), MIN_REUSE))
    for g in ("model_gate", "placement_gate"):
        if str(fm.get(g, "")).lower() != "pass":
            fails.append("%s must be pass (got %s): run the %s gate on this model" % (g, fm.get(g, "missing"), "model-quality (rbx-critic)" if g == "model_gate" else "placement (rbx-placement)"))
    parts = num(fm.get("parts"))
    if parts is None or parts < MIN_PARTS:
        fails.append("parts %s < %d (too simple to be worth keeping)" % (fm.get("parts", "missing"), MIN_PARTS))
    if len(csv(fm.get("materials"))) < MIN_MATERIALS:
        fails.append("materials: list at least %d distinct materials" % MIN_MATERIALS)
    genres = {g.lower() for g in csv(fm.get("genres"))}
    if len(genres) < MIN_GENRES:
        fails.append("genres: %d listed, need >= %d different genres where it fits" % (len(genres), MIN_GENRES))
    if len(csv(fm.get("parameters"))) < MIN_PARAMS:
        fails.append("parameters: list at least %d theme parameters (colour, material, size, ...)" % MIN_PARAMS)
    src = G.read(os.path.join(d, "build.luau")) if code else ""
    if code and not re.search(r"function\s*\(\s*(params|opts|options)\b", src):
        fails.append("build.luau must return function(params) so it themes without editing code")
    if not code and fm.get("param_mode", "") != "attributes":
        fails.append("rbxm-only model: set param_mode: attributes and expose the parameters as Attributes on the model")
    m = BAD_CODE.search(src)
    if m:
        fails.append("not self-contained: build.luau uses %r (no remotes, game services, requires or asset ids)" % m.group(0))
    low = fm.get("licence", fm.get("license", "")).lower()
    if low not in ("original", "cc0"):
        fails.append("licence must be original or CC0")
    elif low == "cc0" and not fm.get("credits", "").strip():
        fails.append("CC0 model needs credits (source and author)")
    nm = toks(slug.replace("-", " ") + " " + fm.get("name", "") + " " + desc)
    for g in games_slugs(root):
        gt = toks(g.replace("-", " "))
        if gt and (len(gt) >= 2 or len(g) >= 4) and gt <= nm:
            fails.append("game-specific: mentions the game %r" % g)
    ex = [e for e in entries(root)]
    repl = None
    for e in ex:
        if e["slug"] == slug and e["category"] == cat:
            repl = e
        else:
            same = e["category"] == cat
            n1 = jac(toks(slug.replace("-", " ") + " " + fm.get("name", "")), toks(e["slug"].replace("-", " ") + " " + e.get("name", "")))
            d1 = jac(toks(desc), toks(e.get("description", "")))
            if e["slug"] == slug or (same and (n1 >= 0.5 or d1 >= 0.6)) or d1 >= 0.75:
                repl = repl or e
    me = (q or 0) * 10 + (r or 0)
    if repl:
        if me > score(repl):
            notes.append("REPLACES %s (%s/%s, better than the existing %s/%s)" % (repl["slug"], fm.get("quality"), fm.get("reuse"), repl.get("quality"), repl.get("reuse")))
        else:
            fails.append("duplicate of %s (not better: quality+reuse %s/%s vs %s/%s)" % (repl["slug"], fm.get("quality"), fm.get("reuse"), repl.get("quality"), repl.get("reuse")))
    evict = None
    rest = [e for e in ex if e is not repl]
    incat = [e for e in rest if e["category"] == cat]
    pool = incat if len(incat) >= MAX_CAT else (rest if len(rest) >= MAX_TOTAL else None)
    if pool:
        low_e = min(pool, key=score)
        if me > score(low_e):
            evict = low_e
            notes.append("EVICTS %s (%s, lowest in a full %s)" % (low_e["slug"], low_e.get("quality"), "category" if pool is incat else "library"))
        else:
            fails.append("library full (%s): must beat the lowest entry %s (%s/%s)" % ("category cap %d" % MAX_CAT if pool is incat else "cap %d" % MAX_TOTAL, low_e["slug"], low_e.get("quality"), low_e.get("reuse")))
    return fails, notes, fm, repl, evict


def cmd_check(a):
    root = models_root(a)
    fails, notes, fm, _, _ = run_check(a.src, parse_scores(a.scores), root)
    for n in notes:
        print("NOTE: " + n)
    for f in fails:
        print("FAIL: " + f)
    print("%s %s" % ("FAIL" if fails else "PASS", fm.get("slug", a.src)))
    return 1 if fails else 0


README_TPL = r"""# Models: your small library of reusable 3D models

Only the best, most reusable models live here. It is deliberately hard to get in: at most {{total}} models, {{cat}} per category. Claude saves a model here by itself when it passes every rule below, says one line, and reuses it in later games. Nothing here is overwritten or deleted by `/rbx-update`, `/rbx-unload` or `/rbx-clean`. Do not edit INDEX.md by hand (it is rebuilt).

## What belongs here (ALL must be true)
1. Quality: critic/judge score of at least 8/10, the model-quality gate (part count, materials, bevels, detail) PASS and the placement gate PASS for this model.
2. Generic function that fits at least 3 different genres (prop, furniture, building piece, vehicle, nature, ui3d, accessory, tool, effect, decor), listed in `genres:`.
3. Theme-able by parameters (colours, materials, size) without editing code: `build.luau` returns `function(params)`; list at least 2 parameters.
4. Self-contained: no game scripts, remotes, game names, DataStores, requires or asset ids. Detailed enough to be worth keeping (at least 10 parts, 2 materials).
5. Original, or CC0 with credits.
6. Not a duplicate: a near-duplicate is refused unless it is better, then it replaces the old one.
7. Final: never WIP, placeholder or one-off. When the library is full a new model must beat the lowest-scored one in its category (that one is removed and logged in LOG.md).

## How a model is saved
Claude builds the model in `<work dir>/` with `build.luau` and a `model.md` (run `models.py template` for the skeleton), runs the gates, then `models.py check <dir>`. On PASS it runs `models.py add <dir>`; on FAIL it says nothing. Each model is stored as `Models/<category>/<slug>/` with `build.luau` and/or `.rbxm`, `model.md` (what it is, size/scale, parts, materials, parameters, gate results, genres, licence/credits) and an optional `preview.png`.

## How to reuse
Before building any model Claude runs `models.py find <words>`. A match is built with `build.luau` (pass your theme as params) or inserted from the `.rbxm`, then placed with the placement step. `models.py use <slug> --game <game-slug>` records which game uses it. `models.py list` shows everything; `models.py remove <slug>` deletes one.
"""

MODEL_TPL = r"""---
name: Lantern Post
slug: lantern-post
category: decor
description: One-line description of what it is and what it is for (25+ characters)
quality: 8.5
reuse: 8
parts: 24
materials: Metal, Glass, Wood
genres: obby, tycoon, roleplay
parameters: color, material, size
param_mode: code
status: final
model_gate: pass
placement_gate: pass
licence: original
credits:
size: 4 x 1 x 1 studs, Y up, pivot at the base
---
# Lantern Post
What it is, how it looks, what to change through params.

## Parameters
- color (Color3), material (Enum.Material), size (number scale)

## Quality gate results
Critic score, model-quality gate and placement gate results (paste the lines).

## Credits and licence
Original, or CC0 source and author.
"""


def rebuild_index(root):
    es = sorted(entries(root), key=lambda e: (e["category"], e["slug"]))
    lines = ["# Models index", "", "Generated by models.py from each model.md; do not edit. %d of %d models." % (len(es), MAX_TOTAL), "",
             "| slug | category | description | quality | reuse | parts | games used in |", "|---|---|---|---|---|---|---|"]
    for e in es:
        lines.append("| %s | %s | %s | %s | %s | %s | %s |" % (e["slug"], e["category"], e.get("description", "").replace("|", "/"), e.get("quality", "?"), e.get("reuse", "?"), e.get("parts", "?"), e.get("games_used", "") or "-"))
    if not es:
        lines.append("| (none yet) | | | | | | |")
    G.write(os.path.join(root, "INDEX.md"), "\n".join(lines) + "\n")


def ensure_root(root):
    os.makedirs(root, exist_ok=True)
    rp = os.path.join(root, "README.md")
    if not os.path.isfile(rp):
        G.write(rp, G.fill(README_TPL, total=str(MAX_TOTAL), cat=str(MAX_CAT)))


def log(root, msg):
    p = os.path.join(root, "LOG.md")
    G.write(p, (G.read(p) or "# Models log\n\n") + "- %s %s\n" % (today(), msg))


def drop(root, e, why):
    shutil.rmtree(e["dir"], ignore_errors=True)
    try:
        os.rmdir(os.path.dirname(e["dir"]))
    except OSError:
        pass
    log(root, "removed %s (%s/%s, %s)" % (e["slug"], e.get("quality", "?"), e.get("reuse", "?"), why))


def cmd_add(a):
    root = models_root(a)
    sc = parse_scores(a.scores)
    fails, notes, fm, repl, evict = run_check(a.src, sc, root)
    if fails:
        for f in fails:
            print("FAIL: " + f)
        print("FAIL %s (not added)" % fm.get("slug", a.src))
        return 1
    d, md = find_src(a.src)
    ensure_root(root)
    if repl:
        keep = csv(repl.get("games_used"))
        drop(root, repl, "replaced by a better %s" % fm["slug"])
    else:
        keep = []
    if evict:
        drop(root, evict, "evicted by %s" % fm["slug"])
    dest = os.path.join(root, fm["category"], fm["slug"])
    os.makedirs(dest, exist_ok=True)
    for f in os.listdir(d):
        if os.path.isfile(os.path.join(d, f)) and (f.endswith(KEEP_EXT)):
            shutil.copy2(os.path.join(d, f), os.path.join(dest, f))
    t = G.read(os.path.join(dest, "model.md"))
    for k in ("quality", "reuse", "model_gate", "placement_gate"):
        if k in sc:
            t = G.set_fm(t, k, sc[k])
    t = G.set_fm(t, "added", today())
    if keep:
        t = G.set_fm(t, "games_used", ", ".join(keep))
    G.write(os.path.join(dest, "model.md"), t)
    rebuild_index(root)
    for n in notes:
        print("NOTE: " + n)
    print("ADDED %s -> %s (quality %s/10, reuse %s/10)" % (fm["slug"], dest, fm.get("quality"), fm.get("reuse")))
    return 0


def cmd_find(a):
    root = models_root(a)
    ws = [w for w in re.findall(r"[a-z0-9]+", " ".join(a.words).lower()) if len(w) >= 2]
    hits = []
    for e in entries(root):
        text = (e["slug"] + " " + e["category"] + " " + G.read(os.path.join(e["dir"], "model.md"))).lower()
        n = sum(1 for w in ws if w in text)
        if n:
            hits.append((n, score(e), e))
    hits.sort(key=lambda h: (-h[0], -h[1]))
    for n, _, e in hits[:8]:
        print("%s | %s | %s | quality %s reuse %s | params: %s | %s" % (e["slug"], e["category"], e.get("description", ""), e.get("quality", "?"), e.get("reuse", "?"), e.get("parameters", "?"), e["dir"]))
    print("(%d match%s)%s" % (len(hits), "" if len(hits) == 1 else "es", "" if hits else " none: build it new, then run the save step") if ws else "usage: models.py find <words>")
    return 0


def cmd_list(a):
    root = models_root(a)
    es = sorted(entries(root), key=lambda e: (e["category"], e["slug"]))
    for e in es:
        print("%s | %s | %s | quality %s | reuse %s | parts %s | games: %s" % (e["slug"], e["category"], e.get("description", ""), e.get("quality", "?"), e.get("reuse", "?"), e.get("parts", "?"), e.get("games_used", "") or "-"))
    print("(%d model%s)" % (len(es), "" if len(es) == 1 else "s"))
    return 0


def cmd_use(a):
    root = models_root(a)
    e = next((x for x in entries(root) if x["slug"] == a.slug), None)
    if not e:
        sys.exit("models.py: no model %r" % a.slug)
    if not G.SLUG_RE.match(a.game or ""):
        sys.exit("models.py: --game must be a game slug (lowercase letters, digits, dashes)")
    p = os.path.join(e["dir"], "model.md")
    cur = csv(e.get("games_used"))
    if a.game not in cur:
        cur.append(a.game)
    G.write(p, G.set_fm(G.read(p), "games_used", ", ".join(cur)))
    rebuild_index(root)
    print("USED %s in %s (%d game%s)" % (a.slug, a.game, len(cur), "" if len(cur) == 1 else "s"))
    return 0


def cmd_remove(a):
    root = models_root(a)
    e = next((x for x in entries(root) if x["slug"] == a.slug), None)
    if not e:
        sys.exit("models.py: no model %r" % a.slug)
    drop(root, e, "removed on request")
    rebuild_index(root)
    print("REMOVED %s" % a.slug)
    return 0


def main():
    ap = argparse.ArgumentParser(description="reusable models library")
    ap.add_argument("--models")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("where")
    sub.add_parser("template")
    sub.add_parser("list")
    for n in ("check", "add"):
        s = sub.add_parser(n)
        s.add_argument("src")
        s.add_argument("--scores", nargs="*")
    s = sub.add_parser("find")
    s.add_argument("words", nargs="+")
    s = sub.add_parser("use")
    s.add_argument("slug")
    s.add_argument("--game", required=True)
    s = sub.add_parser("remove")
    s.add_argument("slug")
    a = ap.parse_args()
    if a.cmd == "template":
        sys.stdout.write(MODEL_TPL)
        return 0
    if a.cmd == "where":
        r = models_root(a)
        print("MODELS=%s%s" % (r, "" if os.path.isdir(r) else " (not created yet)"))
        return 0
    return {"check": cmd_check, "add": cmd_add, "find": cmd_find, "list": cmd_list, "use": cmd_use, "remove": cmd_remove}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main() or 0)
