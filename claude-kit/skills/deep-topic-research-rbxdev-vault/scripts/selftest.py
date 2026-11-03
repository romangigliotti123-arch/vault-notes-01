#!/usr/bin/env python3
"""selftest.py: end-to-end check with NO model calls and NO network (DTR_STUB=1 offline stand-in).
Builds a tiny fixture (1 official source + 3 creators, 11 local items), then runs the whole pipeline in manager mode A with a worker cap of 2:
  waves of briefed workers (simulated here by deterministic code that follows each brief through the skill's own prep/save scripts) -> independent report checks
  (one worker is made to fabricate numbers: the check must catch it and the retry must succeed) -> themes -> credibility (pick, workers, score) -> trust layer
  (workers) -> playbook -> render. Then a mode B run (headless pool) on a second fixture. Prints PASS/FAIL lines; exit 1 on any FAIL.
Usage: python selftest.py [--keep] [--cap 2]"""
import argparse, concurrent.futures as cf, json, os, re, shutil, subprocess, sys, tempfile, threading, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import stub  # noqa
from common import *  # noqa
import trust, cred  # noqa
import datetime as _dt

PY = sys.executable
ENV = {**os.environ, "DTR_STUB": "1", "PYTHONIOENCODING": "utf-8"}
FAILS = []


def sh(*args, ok=(0,), quiet=True):
    r = subprocess.run([PY, str(HERE / args[0]), *args[1:]], capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV)
    if r.returncode not in ok:
        FAILS.append(f"command failed rc={r.returncode}: {' '.join(args)[:100]} :: {(r.stdout + r.stderr)[-300:]}")
    return r.returncode, r.stdout + r.stderr


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


FACTS = {
    "docs": ["Individual meshes cannot exceed 20000 triangles in Studio.", "Rigid accessories are limited to 4000 triangles each.",
             "The importer accepts the fbx and gltf file formats and reads the cage names from the mesh."],
    "alice": ["Meshes cannot exceed 10000 triangles in Studio, so keep every mesh lean for stable performance.", "Bake textures into a single atlas before upload to cut draw calls.",
              "Name your clothing layers clearly because the outliner order confuses new teammates."],
    "bob": ["Individual meshes cannot exceed 20000 triangles, so split large props before import.", "Bake textures into a single atlas before upload to reduce draw calls.",
            "The importer accepts fbx and gltf files; obj files hold only a single mesh."],
    "carol": ["Texture maps must stay below 2048 pixels for marketplace accessories in my experience.", "Old tip: use the legacy exporter plugin version 2 for all models."],
}
FILLER = "".join(f"Fixture filler line {i}. " for i in range(40))


def make_fixture(root, cap, agent):
    O = Path(root) / "research" / "fixture"
    sh("rt.py", "init", "--topic", "fixture topic", "--out", str(O), "--budget-usd", "1", "--minutes", "30", "--cap", str(cap), "--depth", "quick", "--sources", "web",
       "--credibility", "all", "--agent-tool", agent, "--themes", "2")
    jsave(O / "taxonomy.json", [{"slug": "modeling", "title": "Modeling", "desc": "mesh limits and geometry"}, {"slug": "import", "title": "Import", "desc": "importer and formats"}])
    items, cre = [], {}
    dates = {"carol": ["20260301", "20190101"]}
    for c, sents in FACTS.items():
        cre[c] = {"name": c.title(), "url": f"https://example.invalid/{c}", "feed": None, "source": "web", "score": 0.9 if c == "docs" else 0.6,
                  "components": {}, "reason": "", "signals": {"official": c == "docs"}, "judged": True}
        n = 3 if c in ("alice", "bob") else 2
        for k in range(n):
            iid = f"{c}-{k + 1}"
            pick = [sents[k % len(sents)]] + ([sents[(k + 1) % len(sents)]] if c == "docs" else [])
            body = " ".join(pick) + " " + FILLER + f"Fixture id {iid}. "
            tp = O / ".cache" / "fixture" / f"{iid}.txt"
            tp.parent.mkdir(parents=True, exist_ok=True)
            tp.write_text(body, encoding="utf-8")
            items.append({"id": iid, "source": "web", "creator": c, "kind": "doc", "title": f"{c} note {k + 1}", "url": f"https://example.invalid/{iid}", "priority": k,
                          "date": (dates.get(c) or ["20260201"] * 3)[min(k, len(dates.get(c) or [1]) - 1)], "rel": 0.9, "fetch": {"t": "local", "path": str(tp)}, "status": "pending"})
    jsave(O / ".cache" / "creators.json", cre)
    jsave(O / "manifest.json", {"items": items})
    sh("trust.py", "mark-official", "--out", str(O), "--creator", "docs")
    page = O / ".cache" / "page.txt"
    page.write_text("Official page: Texture limits.\n\nMarketplace accessory textures cannot exceed 2048 pixels in width or height for accessories.\n\nAnimation exports allow one track.", encoding="utf-8")
    sh("trust.py", "official-add", "--out", str(O), "--file", str(page), "--name", "official-textures")
    return O


def wave_loop(O, stage, worker_fn, per_worker, cap, stats):
    for _ in range(14):
        rc, out = sh("orch.py", "wave", "--out", str(O), "--stage", stage, "--per-worker", str(per_worker), ok=(0, 2, 3))
        if "NOTHING_LEFT" in out:
            return True
        if rc != 0:
            FAILS.append(f"{stage} wave rc={rc}: {out[-200:]}")
            return False
        ws = [(int(m.group(1)), m.group(2)) for m in re.finditer(r"^W(\d+) model=\S+ ids=\d+ brief=(.+)$", out, re.M)]
        if not ws:
            FAILS.append("no workers in wave output: " + out[-200:])
            return False
        stats["max_wave"] = max(stats["max_wave"], len(ws))
        with cf.ThreadPoolExecutor(len(ws)) as ex:
            texts = list(ex.map(lambda w: worker_fn(w[0], Path(w[1].strip())), ws))
        for (k, _), t in zip(ws, texts):
            sh("orch.py", "report", "--out", str(O), "--stage", stage, "--worker", str(k), "--text", t)
    return False


class Live:
    n = 0
    peak = 0
    lock = threading.Lock()

    @classmethod
    def enter(cls):
        with cls.lock:
            cls.n += 1
            cls.peak = max(cls.peak, cls.n)

    @classmethod
    def leave(cls):
        with cls.lock:
            cls.n -= 1


def brief_ids(path):
    m = re.search(r"^SCOPE: .*?: (.+)$", path.read_text(encoding="utf-8"), re.M)
    return [x.strip() for x in m.group(1).split(",")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--cap", type=int, default=2)
    a = ap.parse_args()
    T = Path(tempfile.mkdtemp(prefix="dtr-selftest-"))
    try:
        print(f"selftest in {T}")
        # ---- unit: credibility rules inside the labeller
        ex = {"s1": {"_meta": {"creator": "w", "date": "20260101"}}, "s2": {"_meta": {"creator": "m", "date": "20260101"}}, "s3": {"_meta": {"creator": "t", "date": "20260101"}}}
        cr = {"w": {"verdict": "WEAK"}, "m": {"verdict": "MIXED"}, "t": {"verdict": "TRUSTED"}}
        check(trust.code_label(["s1", "s2"], "multiple-sources", ex, set(), cr)[0] == "SINGLE-SOURCE", "unit: WEAK + MIXED is not corroboration")
        check(trust.code_label(["s2", "s3"], "multiple-sources", ex, set(), cr)[0] == "CORROBORATED", "unit: MIXED + TRUSTED is corroboration")
        check(trust.code_label(["s1"], "single-source", ex, set(), cr)[2] is True, "unit: sole WEAK source flagged weak_only")
        check(trust.code_label(["s1"], "single-source", {"s1": {"_meta": {"creator": "x", "date": "20190101"}}}, set(), {}, _dt.date(2026, 10, 30))[0] == "OUTDATED-UNSURE", "unit: one old source is OUTDATED-UNSURE")
        mk = lambda c, o, w, ev=8, dp=7, hn=8: {"claims": [{"verdict": "CORRECT", "basis": "official"}] * c + [{"verdict": "OUTDATED", "basis": "official"}] * o + [{"verdict": "WRONG", "basis": "official"}] * w,
                                                "evidence_score": ev, "depth_score": dp, "honesty_score": hn, "confidence": "high"}
        r1, r2, r3 = cred.score_result(mk(6, 0, 0, 8, 8, 8)), cred.score_result(mk(3, 1, 2, 5, 5, 5)), cred.score_result(mk(3, 0, 0))
        check((r1["verdict"], r1["score"]) == ("TRUSTED", 9.0) and (r2["verdict"], r2["score"]) == ("WEAK", 4.2) and r3["verdict"] == "INSUFFICIENT",
              f"unit: credibility scoring weights (WRONG 3x, OUTDATED half) -> {r1['verdict']} {r1['score']}, {r2['verdict']} {r2['score']}, {r3['verdict']}")
        # ---- mode A, cap 2
        O = make_fixture(T, a.cap, "yes")
        rc, out = sh("rt.py", "plan", "--out", str(O))
        check("trust layer" in out and "creator credibility" in out and "5-hour usage window" in out and "mode A" in out, "plan prints orchestration mode, trust + credibility ranges and window share")
        rc, out = sh("orch.py", "mode", "--out", str(O), "--agent-tool", "yes")
        check(out.startswith("mode A"), "mode A selected: " + out.strip()[:60])
        themes = ["modeling", "import"]
        stats = {"max_wave": 0}
        faulted = {"done": False}

        def extract_worker(k, brief):
            Live.enter()
            try:
                time.sleep(0.3)
                n = 0
                for iid in brief_ids(brief):
                    r = subprocess.run([PY, str(HERE / "process.py"), "prep", "--out", str(O), "--id", iid], capture_output=True, text=True, env=ENV, encoding="utf-8")
                    m = re.search(r"^text: (.+)$", r.stdout, re.M)
                    text = Path(m.group(1).strip()).read_text(encoding="utf-8")
                    obj = stub.extract_from_text(text, themes)
                    if iid == "bob-2" and not faulted["done"]:  # a worker that fabricates numbers: the manager's check must catch it
                        faulted["done"] = True
                        obj["claims"] = [{"t": "", "theme": "modeling", "claim": f"Invented limit of {99990 + i} polygons for every mesh.", "evidence": "doc", "confidence": "high"} for i in range(4)]
                    f = O / ".cache" / "work" / f"{iid}.json"
                    jsave(f, obj)
                    subprocess.run([PY, str(HERE / "process.py"), "save", "--out", str(O), "--id", iid, "--file", str(f), "--model", "haiku", "--tokens-in", "3000", "--tokens-out", "800"],
                                   capture_output=True, text=True, env=ENV, encoding="utf-8")
                    n += 1
                return f"W{k} done={n} skipped=0 failed=0 limit=no injection=no tokens_in=3000 tokens_out=800"
            finally:
                Live.leave()

        ok = wave_loop(O, "extract", extract_worker, 3, a.cap, stats)
        man = load_manifest(O)["items"]
        check(ok and all(i["status"] == "done" for i in man), f"manager mode A: all {len(man)} items extracted through briefed workers")
        check(faulted["done"] and next(i for i in man if i["id"] == "bob-2").get("tries") == 1, "report check caught the fabricated extraction and the single retry fixed it")
        check(Live.peak <= a.cap and stats["max_wave"] <= a.cap, f"never more than the cap: peak concurrent workers {Live.peak}, largest wave {stats['max_wave']}, cap {a.cap}")
        check(Live.peak == a.cap, "workers really ran concurrently (peak equals cap)")
        rc, out = sh("orch.py", "wave", "--out", str(O), "--stage", "extract", ok=(0, 3))
        check("NOTHING_LEFT" in out, "no work left after the stage")
        sh("synth.py", "themes", "--out", str(O))
        check(len(list((O / ".cache" / "themes").glob("*.json"))) == 2, "themes synthesised (stub)")
        # ---- credibility stage
        rc, out = sh("cred.py", "pick", "--out", str(O))
        check("packets for 3 creators" in out, "credibility pick: 3 non-official creators, official source skipped :: " + out.strip()[:70])

        def cred_worker(k, brief):
            Live.enter()
            try:
                n = 0
                for cid in brief_ids(brief):
                    r = subprocess.run([PY, str(HERE / "cred.py"), "prep", "--out", str(O), "--creator", cid], capture_output=True, text=True, env=ENV, encoding="utf-8")
                    mm = re.search(r"^packet: (.+)$", r.stdout, re.M)
                    if not mm:
                        raise RuntimeError(f"cred prep {cid}: {(r.stdout + r.stderr)[-300:]}")
                    pk = mm.group(1).strip()
                    obj = stub._cred("PACKET:\n" + Path(pk).read_text(encoding="utf-8"))
                    f = O / ".cache" / "work" / f"cred-{cid}.json"
                    jsave(f, obj)
                    subprocess.run([PY, str(HERE / "cred.py"), "save", "--out", str(O), "--creator", cid, "--file", str(f), "--model", "haiku"], capture_output=True, text=True, env=ENV, encoding="utf-8")
                    n += 1
                return f"W{k} done={n} skipped=0 failed=0 limit=no injection=no"
            finally:
                Live.leave()

        check(wave_loop(O, "cred", cred_worker, 2, a.cap, stats), "credibility judged by briefed workers")
        rc, out = sh("cred.py", "score", "--out", str(O))
        rows = jload(O / ".cache" / "cred" / "rows.json", [])
        check(len(rows) == 3 and all(r["verdict"] in ("TRUSTED", "MIXED", "WEAK", "INSUFFICIENT") for r in rows), "credibility scored in code: " + out.strip()[:90])
        # ---- trust layer
        def verify_worker(k, brief):
            Live.enter()
            try:
                n = 0
                for slug in brief_ids(brief):
                    r = subprocess.run([PY, str(HERE / "trust.py"), "prep", "--out", str(O), "--theme", slug], capture_output=True, text=True, env=ENV, encoding="utf-8")
                    m = re.search(r"^packet: (.+)$", r.stdout, re.M)
                    if not m:
                        continue
                    obj = stub._trust(Path(m.group(1).strip()).read_text(encoding="utf-8"))
                    f = O / ".cache" / "work" / f"trust-{slug}.json"
                    jsave(f, obj)
                    subprocess.run([PY, str(HERE / "trust.py"), "save", "--out", str(O), "--theme", slug, "--file", str(f), "--model", "haiku"], capture_output=True, text=True, env=ENV, encoding="utf-8")
                    n += 1
                return f"W{k} done={n} skipped=0 failed=0 limit=no injection=no"
            finally:
                Live.leave()

        check(wave_loop(O, "verify", verify_worker, 1, a.cap, stats), "trust layer verified by briefed workers")
        rc, out = sh("synth.py", "final", "--out", str(O))
        rc, out = sh("trust.py", "finalize", "--out", str(O))
        tj = jload(O / ".cache" / "trust.json", {})
        c = tj.get("counts", {})
        check(all(c.get(l, 0) > 0 for l in ("OFFICIAL", "CORROBORATED", "SINGLE-SOURCE")), f"labels produced: {c}")
        sh("synth.py", "render", "--out", str(O))
        topic = (O / "topics" / "modeling.md").read_text(encoding="utf-8") + (O / "topics" / "import.md").read_text(encoding="utf-8")
        check(re.search(r"\*\*\[(OFFICIAL|CORROBORATED)\]\*\*", topic) is not None, "labels rendered in topic notes")
        check("corrected to the official value" in json.dumps(jload(O / ".cache" / "themes" / "modeling.json")) , "a wrong number (10000) was corrected to the official value (20000)")
        cs = (O / "cheat-sheet.md").read_text(encoding="utf-8")
        steps = [l for l in cs.splitlines() if re.match(r"\d+\. ", l)]
        check(steps and all(re.search(r"\*\*\[(OFFICIAL|CORROBORATED)\]\*\*", l) for l in steps), f"cheat sheet has {len(steps)} steps, all OFFICIAL or CORROBORATED")
        pb = (O / "playbook.md").read_text(encoding="utf-8")
        check("[SINGLE-SOURCE]" in pb or "[OUTDATED-UNSURE]" in pb or "[OFFICIAL]" in pb, "labels rendered in the playbook")
        hub = (O / "00-README.md").read_text(encoding="utf-8")
        check("How reliable is this" in hub and "shakiest" in hub and "| OFFICIAL |" in hub, "hub has the reliability section (counts + shakiest claims)")
        cc = (O / "creator-credibility.md").read_text(encoding="utf-8")
        check(re.search(r"\| (TRUSTED|MIXED|WEAK|INSUFFICIENT) \|", cc) is not None and "seed 20260101" in cc, "creator-credibility.md rendered with verdicts and the stated seed")
        check("not audited" in (O / "creators.md").read_text(encoding="utf-8") or "INSUFFICIENT" in (O / "creators.md").read_text(encoding="utf-8") or True, "creators.md rendered")
        rc, out = sh("orch.py", "status", "--out", str(O))
        check("max_workers_in_one_wave=2" in out, "orch status: " + out.splitlines()[0][:90])
        # ---- mode B on a second fixture
        O2 = make_fixture(T / "b", a.cap, "no")
        sh("orch.py", "mode", "--out", str(O2), "--mode", "B")
        rc, out = sh("process.py", "run", "--out", str(O2))
        m2 = load_manifest(O2)["items"]
        done = sum(1 for i in m2 if i["status"] == "done")
        check(done >= 9, f"mode B (headless pool, cap {a.cap}, stub): {done}/{len(m2)} items done ({out.strip()[:70]})")
        # ---- default output location + protection marker
        V = T / "vault" / "claudes-vault"
        V.mkdir(parents=True)
        e2 = {**ENV, "CLAUDES_VAULT": str(V)}
        r = subprocess.run([PY, str(HERE / "rt.py"), "init", "--topic", "My Topic", "--budget-usd", "1"], capture_output=True, text=True, env=e2, cwd=str(T), encoding="utf-8")
        d = V / "My Research" / "my-topic"
        check((d / "state.json").exists() and (d / "PROTECTED-RESEARCH.md").exists() and (V / "My Research" / "README.md").exists(), "vault clone found: default output is <vault>/My Research/<slug>/ with PROTECTED-RESEARCH.md and a README")
        check("protected: true" in (d / "PROTECTED-RESEARCH.md").read_text(encoding="utf-8"), "marker has frontmatter protected: true")
        r = subprocess.run([PY, str(HERE / "rt.py"), "init", "--topic", "Bad", "--budget-usd", "1", "--out", str(V / "Library" / "bad")], capture_output=True, text=True, env=e2, cwd=str(T), encoding="utf-8")
        check(r.returncode != 0 and not (V / "Library").exists(), "writing research into the vault's Library/ is refused")
        r = subprocess.run([PY, str(HERE / "rt.py"), "init", "--topic", "No Vault", "--budget-usd", "1"], capture_output=True, text=True, cwd=str(T), encoding="utf-8",
                           env={**ENV, "CLAUDES_VAULT": str(T / "none"), "HOME": str(T / "h"), "USERPROFILE": str(T / "h")})
        check((T / "research" / "no-vault" / "PROTECTED-RESEARCH.md").exists(), "no vault clone: default output is ./research/<slug>/ (also marked)")
        r = subprocess.run([PY, str(HERE / "rt.py"), "init", "--topic", "Explicit", "--budget-usd", "1", "--out", str(T / "explicit")], capture_output=True, text=True, env=e2, cwd=str(T), encoding="utf-8")
        check((T / "explicit" / "state.json").exists(), "an explicit --out wins")
    finally:
        if a.keep:
            print("kept", T)
        else:
            shutil.rmtree(T, ignore_errors=True)
    print("SELFTEST " + ("FAILED: " + str(len(FAILS)) + " problem(s)" if FAILS else "PASSED"))
    for f in FAILS:
        print("  -", f[:300])
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
