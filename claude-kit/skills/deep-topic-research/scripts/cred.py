#!/usr/bin/env python3
"""cred.py: creator credibility stage (optional; set by depth/tier). For each selected creator or publisher (official sources are not audited):
  pick exactly 2 pieces of content from the cache (no re-download): 1 most-cited in the topic notes + 1 random with a FIXED seed (recorded in the output);
  list up to 6 checkable claims per piece; check them against official facts and against the other sources; record non-claim signals;
  score in CODE (accuracy 50% with WRONG counted 3x and OUTDATED half, evidence 20%, depth 15%, honesty 15%); write creator-credibility.md.
Verdicts: TRUSTED >= 7.5 | MIXED 5.0-7.4 | WEAK < 5.0 | INSUFFICIENT (fewer than 4 verified claims). Wording is factual; a verdict describes the sampled pieces.
Commands (all take --out DIR):
  pick                      choose the creators and their 2 pieces, build evidence packets (.cache/cred/packets/)
  judge                     one model call per creator (pool = worker cap), headless; saves .cache/cred/results/
  prep --creator C / save --creator C --file F      the same judging step for an Agent-tool worker (manager mode)
  score                     compute scores + verdicts in code -> .cache/cred/rows.json
  render                    write creator-credibility.md (also run by synth.py render)
"""
import argparse, concurrent.futures as cf, random, sys, threading
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *  # noqa

DEFAULT_SEED = 20260101
MODES = {"off": 0, "top5": 5, "top10": 10, "all": 10 ** 6}
SCHEMA = {"type": "object", "properties": {
    "claims": {"type": "array", "items": {"type": "object", "properties": {
        "video": {"type": "string"}, "claim": {"type": "string"},
        "verdict": {"type": "string", "enum": ["CORRECT", "OUTDATED", "WRONG", "UNVERIFIABLE", "OPINION"]},
        "basis": {"type": "string", "enum": ["official", "other-sources", "both", "own-knowledge", "none"]},
        "note": {"type": "string"}}, "required": ["video", "claim", "verdict", "basis", "note"]}},
    "evidence_score": {"type": "number"}, "depth_score": {"type": "number"}, "honesty_score": {"type": "number"},
    "signals": {"type": "string"}, "reason": {"type": "string"}, "confidence": {"type": "string", "enum": ["low", "medium", "high"]}},
    "required": ["claims", "evidence_score", "depth_score", "honesty_score", "signals", "reason", "confidence"]}
SYSTEM = ("You audit content creators for factual credibility on one topic. Be strict, factual and non-defamatory: describe claims and evidence, never character. "
          "Only judge claims you can ground in the given official facts or other sources. Never invent. Output only the JSON required.")
INSTR = """Packet below = 1-2 pieces of content (video, post, README, article) from ONE creator or publisher on the topic "{topic}". For each piece: extracted claims/numbers, and for each claim the best-matching OFFICIAL facts ("docs", may be irrelevant or empty) and matching claims from OTHER sources ("others"), plus regex signal counts from the cached text.
Task: for EACH piece pick up to 6 CHECKABLE claims (numbers, limits, setting/API/command names, versions, platform rules, performance claims, code correctness). Skip pure opinion unless nothing else (then verdict OPINION). Verdict per claim:
CORRECT (matches a shown official fact or agrees with other sources), OUTDATED (was true, superseded; compare the piece date with today {today}), WRONG (contradicts an official fact or the weight of other sources), UNVERIFIABLE (cannot be grounded), OPINION.
basis: official | other-sources | both | own-knowledge (no shown evidence; use sparingly, never for WRONG) | none. Claims are AI-extracted summaries: mark WRONG only when clearly contradicting; extraction slop is not the creator's fault. Note: one short line.
Scores 0-10 (one decimal): evidence_score = shows own results/code/proof vs bare promises; depth_score = original depth vs rehash/basic; honesty_score = low hype/clickbait/undisclosed pitching (sig counts are noisy regex hits: judge from titles, summaries and snippets).
signals: one line of non-claim signals (unsupported results or income promises, clickbait, hype, sponsor/affiliate pitching, outdated advice, original depth vs rehash). reason: max 2 short factual lines citing specific right/wrong claims. confidence: your confidence in the overall judgement given the small sample.
PACKET:
"""
HYPE = re.compile(r"secret|insane|guaranteed|millionaire|get rich|overnight|easy money|free money|passive income|100% (?:safe|works)|\$\s?\d[\d,]{3,}", re.I)
SPON = re.compile(r"sponsor|affiliate|use code|link in (?:the )?description|discount|join my (?:discord|patreon)|my course|check out my", re.I)
BAD_WORDS = re.compile(r"\b(liar|lying|scam|scammer|fraud|fake|con ?artist|cheat|dishonest|stupid|idiot)\b", re.I)


def cdir(out):
    return out_paths(out)["cache"] / "cred"


def cites(out):
    c = Counter()
    d = out_paths(out)["cache"] / "themes"
    for p in sorted(d.glob("*.json")) if d.exists() else []:
        t = jload(p) or {}
        for k in ("key_points", "numbers", "techniques"):
            for x in t.get(k, []):
                c.update(set(x.get("sources", [])))
    return c


def snippets(rx, text, k=2, w=80):
    out = []
    for m in rx.finditer(text):
        out.append(text[max(0, m.start() - w):m.end() + w].replace("\n", " "))
        if len(out) >= k:
            break
    return out


def cached_text(out, it):
    cache = out_paths(out)["cache"]
    f = it.get("fetch") or {}
    for p in ((cache / "yt" / f["vid"] / "transcript.txt") if f.get("vid") else None, cache / "text" / f"{it['id']}.txt"):
        if p and p.exists():
            return p.read_text(encoding="utf-8", errors="replace")
    return ""


def select_creators(out, st):
    mode = st["limits"].get("credibility", "off")
    off = official_ids(out)
    cre = jload(out_paths(out)["creators"], {})
    order = sorted((c for c in cre if c not in off), key=lambda c: -cre[c].get("score", 0))
    return order[: MODES.get(mode, 0)], cre


def cmd_pick(a):
    st = load_state(a.out)
    seed = int(st["limits"].get("cred_seed", DEFAULT_SEED))
    sel, cre = select_creators(a.out, st)
    if not sel:
        print(f"credibility stage is '{st['limits'].get('credibility', 'off')}' or no non-official creators selected; nothing to do")
        return
    ex = load_extracts(a.out)
    man = {i["id"]: i for i in load_manifest(a.out)["items"]}
    ct = cites(a.out)
    off_idx = Index(official_corpus(a.out, ex))
    allc = [((e["_meta"].get("creator"), sid), t) for sid, e in ex.items() for t in claim_lines(e) if len(t) > 20]
    oth_idx = Index(allc)
    pk_dir = cdir(a.out) / "packets"
    pk_dir.mkdir(parents=True, exist_ok=True)
    made, skipped = 0, []
    for c in sel:
        mine = [(sid, e) for sid, e in ex.items() if (e.get("_meta") or {}).get("creator") == c and e.get("claims")]
        if not mine:
            skipped.append(c)
            continue
        mine.sort(key=lambda x: (-ct[x[0]], -x[1].get("relevance", 0), x[0]))
        picks = [(mine[0], f"most-cited({ct[mine[0][0]]})")]
        if len(mine) > 1:
            b = random.Random(f"{seed}-{c}").choice(mine[1:])
            picks.append((b, f"random(seed {seed}, cites {ct[b[0]]})"))
        vids = []
        for (sid, e), why in picks:
            m = e["_meta"]
            it = man.get(sid, {})
            tx = cached_text(a.out, it)
            tips = []
            for cl in sorted(e["claims"], key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x.get("confidence"), 1))[:10]:
                q = cl["claim"]
                tips.append({"t": cl.get("t", ""), "tip": q[:240], "docs": [f"[{r}] {x[:170]}" for r, x, _ in off_idx.top(q, 2, 3)],
                             "others": [f"[{r[0]}/{r[1]}] {x[:170]}" for r, x, _ in oth_idx.top(q, 4, 3) if r[0] != c][:2]})
            vids.append({"id": sid, "title": m.get("title"), "date": m.get("date"), "url": m.get("url"), "pick": why, "summary": (e.get("summary") or "")[:300], "tips": tips,
                         "numbers": [{"m": n.get("metric", "")[:70], "v": str(n.get("value", ""))[:50]} for n in e.get("numbers", [])[:6]],
                         "sig": ({"hype_n": len(HYPE.findall(tx)), "hype": snippets(HYPE, tx), "sponsor_n": len(SPON.findall(tx)), "sponsor": snippets(SPON, tx), "words": len(tx.split())}
                                 if tx else {"note": "no cached full text; signals judged from the extraction only"})})
        jsave(pk_dir / f"{safe_id(c)}.json", {"creator": c, "name": cre[c].get("name", c), "n_items": len(mine), "videos": vids})
        made += 1
    st["cred_creators"] = sel
    save_state(a.out, st)
    print(f"packets for {made} creators (seed {seed}); no extracted items for: {', '.join(skipped) or 'none'}")


def packet_prompt(out, st, c):
    pk = (cdir(out) / "packets" / f"{safe_id(c)}.json").read_text(encoding="utf-8")
    return INSTR.format(topic=st["topic"], today=today().isoformat()) + pk


def cred_model(st, rank):
    return "haiku" if st["tier"] == "light" or (st["tier"] == "moderate" and rank >= 10) else "sonnet"


def todo_creators(out, st):
    done = {p.stem for p in (cdir(out) / "results").glob("*.json")} if (cdir(out) / "results").exists() else set()
    sel = st.get("cred_creators") or []
    return [c for c in sel if safe_id(c) not in done and (cdir(out) / "packets" / f"{safe_id(c)}.json").exists()]


def cmd_judge(a):
    st = load_state(a.out)
    todo = todo_creators(a.out, st)
    if not todo:
        print("nothing to judge (run pick first, or all done)")
        return
    (cdir(a.out) / "results").mkdir(parents=True, exist_ok=True)
    lock, stop, n_ok = threading.Lock(), {"v": None}, {"n": 0}
    order = {c: i for i, c in enumerate(st.get("cred_creators", []))}

    def job(c):
        if stop["v"]:
            return
        r = check_limits(a.out, st, "synth")
        if r:
            stop["v"] = r
            return
        model = cred_model(st, order[c])
        try:
            obj, cost = call_claude(a.out, packet_prompt(a.out, st, c), SCHEMA, model, "low", SYSTEM, "cred-" + safe_id(c), "cred", budget=0.4)
        except RateLimit:
            stop["v"] = "usage-limit"
            return
        except Exception as e:  # noqa
            print(f"ERR {c}: {str(e)[:120]}")
            return
        obj["_model"], obj["_cost"] = model, cost
        jsave(cdir(a.out) / "results" / f"{safe_id(c)}.json", obj)
        with lock:
            n_ok["n"] += 1

    with cf.ThreadPoolExecutor(max(1, st["limits"]["max_concurrent"])) as ex:
        list(ex.map(job, todo))
    if stop["v"] == "usage-limit":
        st["stop_reason"] = "usage-limit"
        save_state(a.out, st)
    print(f"judged {n_ok['n']}/{len(todo)} creators" + (f"; stopped: {stop['v']} (rerun to resume)" if stop["v"] else ""))


def cmd_prep(a):
    st = load_state(a.out)
    p = cdir(a.out) / "packets" / f"{safe_id(a.creator)}.json"
    if not p.exists():
        sys.exit("no packet for that creator; run pick first")
    d = cdir(a.out) / "work"
    d.mkdir(parents=True, exist_ok=True)
    if not (d / "instructions.txt").exists():  # shared by all workers: write once, never rewrite while others read
        instr = INSTR.format(topic=st["topic"], today=today().isoformat()).split("PACKET:")[0]
        (d / "instructions.txt").write_text(f"SYSTEM: {SYSTEM}\n\n{instr}\nOUTPUT: one JSON object matching the schema in schema.json.", encoding="utf-8")
    if not (d / "schema.json").exists():
        jsave(d / "schema.json", SCHEMA)
    print(f"instructions: {d / 'instructions.txt'}\nschema: {d / 'schema.json'}\npacket: {p}")


def cmd_save(a):
    st = load_state(a.out)
    obj = jload(a.file)
    if not obj or not isinstance(obj.get("claims"), list):
        sys.exit("invalid result: needs claims[]")
    ok_v = {"CORRECT", "OUTDATED", "WRONG", "UNVERIFIABLE", "OPINION"}
    if any(c.get("verdict") not in ok_v for c in obj["claims"]):
        sys.exit("invalid result: claim verdicts must be CORRECT|OUTDATED|WRONG|UNVERIFIABLE|OPINION")
    for k in ("evidence_score", "depth_score", "honesty_score"):
        if not isinstance(obj.get(k), (int, float)):
            sys.exit(f"invalid result: {k} must be a number 0-10")
    obj.setdefault("signals", "")
    obj.setdefault("reason", "")
    obj.setdefault("confidence", "low")
    cost = (a.tokens_in * price_for(a.model)["in"] + a.tokens_out * price_for(a.model)["out"]) / 1e6
    obj["_model"], obj["_cost"] = a.model, cost
    (cdir(a.out) / "results").mkdir(parents=True, exist_ok=True)
    jsave(cdir(a.out) / "results" / f"{safe_id(a.creator)}.json", obj)
    log_cost(a.out, "cred-" + safe_id(a.creator), "cred-subagent", a.model, {"input_tokens": a.tokens_in, "output_tokens": a.tokens_out}, cost, 0)
    print("saved " + a.creator)


# ----------------------------------------------------------------------------- scoring (code, no model)
def score_result(r):
    cnt = Counter(x["verdict"] for x in r["claims"])
    C, O, W, U, P = (cnt.get(k, 0) for k in ("CORRECT", "OUTDATED", "WRONG", "UNVERIFIABLE", "OPINION"))
    ver = C + O + W
    acc = round(10 * (C + 0.5 * O) / (C + O + 3 * W), 2) if ver else None
    ev, dep, hon = (max(0.0, min(10.0, float(r[k]))) for k in ("evidence_score", "depth_score", "honesty_score"))
    if ver >= 4:
        score = round(0.5 * acc + 0.2 * ev + 0.15 * dep + 0.15 * hon, 1)
        verdict = "TRUSTED" if score >= 7.5 else ("MIXED" if score >= 5.0 else "WEAK")
    else:
        score, verdict = None, "INSUFFICIENT"
    grounded = sum(1 for x in r["claims"] if x["verdict"] in ("CORRECT", "OUTDATED", "WRONG") and x["basis"] in ("official", "other-sources", "both"))
    conf = r.get("confidence", "low")
    if ver and grounded / ver < 0.5:
        conf = "low"  # most verified claims rest on model knowledge, not on shown evidence
    return dict(verdict=verdict, score=score, acc=acc, C=C, O=O, W=W, U=U, P=P, ver=ver, ev=ev, dep=dep, hon=hon, grounded=grounded, conf=conf)


def cmd_score(a):
    rows = []
    for f in sorted((cdir(a.out) / "results").glob("*.json")) if (cdir(a.out) / "results").exists() else []:
        r = jload(f)
        pk = jload(cdir(a.out) / "packets" / f.name, {})
        if not r or not pk:
            continue
        row = score_result(r)
        if len(pk["videos"]) < 2 and row["conf"] == "high":
            row["conf"] = "medium"
        reason = (r.get("reason") or "").strip()
        if BAD_WORDS.search(reason) or BAD_WORDS.search(r.get("signals", "")):
            reason = f"{row['C']} claims matched evidence, {row['W']} did not, {row['O']} were outdated, {row['U']} could not be verified."
            r["signals"] = ""
        row.update(c=pk["creator"], name=pk.get("name", pk["creator"]), reason=reason, signals=(r.get("signals") or "").strip(), model=r["_model"], cost=r["_cost"],
                   n_items=pk.get("n_items", 0), vids=[(v["id"], v["pick"].split("(")[0], v.get("url")) for v in pk["videos"]], claims=r["claims"])
        rows.append(row)
    jsave(cdir(a.out) / "rows.json", rows)
    print(dict(Counter(r["verdict"] for r in rows)), f"cost ${sum(r['cost'] for r in rows):.3f}")


def clean(s):
    return re.sub(r"\s+", " ", s or "").replace("|", "/").strip()


def render_md(out):
    rows = jload(cdir(out) / "rows.json", [])
    if not rows:
        return None
    st = load_state(out)
    seed = st["limits"].get("cred_seed", DEFAULT_SEED)
    order = {"TRUSTED": 0, "MIXED": 1, "WEAK": 2, "INSUFFICIENT": 3}
    rows = sorted(rows, key=lambda r: (order[r["verdict"]], -(r["score"] or 0), r["c"]))
    cnt = Counter(r["verdict"] for r in rows)
    L = ["---", "type: creator-credibility", f'topic: "{st["topic"]}"', f"generated: {now_iso()[:10]}", f"seed: {seed}", "---", "",
         f"# Creator credibility: {st['topic']}", "",
         f"Sample audit of {len(rows)} creators/publishers. Per creator: the piece most cited in the topic notes plus one random piece (fixed seed {seed}), up to 6 checkable claims each, checked "
         "against official sources read during the run and against the other sources, plus non-claim signals (hype, income promises, sponsor pitching, outdated advice, original depth). "
         "Official sources are not audited.", "",
         f"Counts: TRUSTED {cnt['TRUSTED']}, MIXED {cnt['MIXED']}, WEAK {cnt['WEAK']}, INSUFFICIENT {cnt['INSUFFICIENT']}.", "",
         "## How the synthesis uses this", "",
         "- TRUSTED (7.5+): may be a primary source; numbers and limits are still checked against official sources.",
         "- MIXED (5.0-7.4): needs a second source before a recommendation is trusted.",
         "- WEAK (below 5.0): never the sole source of a recommendation, and does not count as corroboration.",
         "- INSUFFICIENT (fewer than 4 verified claims): credibility unknown, treated as unverified, not as bad.",
         "- Score = 50% claim accuracy (WRONG counted 3x, OUTDATED half credit) + 20% evidence + 15% depth + 15% honesty. Computed in code from the claim verdicts.",
         "- A verdict describes the sampled pieces and how their claims checked out. It is not a judgement of the person, and claims are AI-extracted summaries, so an apparent error can be an extraction slip.", "",
         "## Table", "", "| creator | verdict | score | right / wrong / outdated / unverifiable | pieces | note |", "|---|---|---|---|---|---|"]
    for r in rows:
        pcs = ", ".join(f"[{v[0][:14]}]({v[2]}) ({'top' if v[1].startswith('most') else 'rand'})" if v[2] else f"{v[0][:14]} ({'top' if v[1].startswith('most') else 'rand'})" for v in r["vids"])
        note = clean(r["reason"]) + (f" Signals: {clean(r['signals'])}" if r["signals"] else "")
        if r["conf"] == "low":
            note += " (LOW CONFIDENCE: small sample or little shown evidence)"
        L.append(f"| {clean(r['name'])} | {r['verdict']} | {r['score'] if r['score'] is not None else 'n/a'} | {r['C']} / {r['W']} / {r['O']} / {r['U']} | {pcs} | {note} |")
    L += ["", "## Method and limits", "",
          f"- Pieces come from the run's cache (no re-download). Pick 1 = most cited by the synthesised topic notes; pick 2 = random with seed {seed} per creator (only 1 piece if the creator has one extracted item).",
          "- Each judge call sees the extracted claims, the best-matching official facts, matching claims from other creators, and regex counts for hype/sponsor wording in the cached text.",
          "- The judge model is listed per creator in `.cache/cred/rows.json`. Judge output is not hand-audited claim by claim; small samples can mislead.",
          f"- Model cost of this stage: about ${sum(r['cost'] for r in rows):.2f} (see costs.csv, stages cred / cred-subagent).", ""]
    (Path(out) / "creator-credibility.md").write_text("\n".join(L), encoding="utf-8")
    return len(rows)


def cmd_render(a):
    n = render_md(a.out)
    print(f"creator-credibility.md written ({n} creators)" if n else "no scored creators; run pick, judge, score first")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    for n in ("pick", "judge", "score", "render", "prep", "save"):
        p = sp.add_parser(n)
        p.add_argument("--out", required=True)
        if n in ("prep", "save"):
            p.add_argument("--creator", required=True)
        if n == "save":
            p.add_argument("--file", required=True)
            p.add_argument("--model", default="haiku")
            p.add_argument("--tokens-in", type=int, default=0)
            p.add_argument("--tokens-out", type=int, default=0)
    a = ap.parse_args()
    {"pick": cmd_pick, "judge": cmd_judge, "score": cmd_score, "render": cmd_render, "prep": cmd_prep, "save": cmd_save}[a.cmd](a)


if __name__ == "__main__":
    main()
