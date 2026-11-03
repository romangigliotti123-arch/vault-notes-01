#!/usr/bin/env python3
"""rt.py: run state, plan/estimate, limits check, work ordering, gap report.
  init     --topic T --budget-usd X --minutes M|--until ISO --cap N --depth quick|thorough|exhaustive
           --sources github,youtube,reddit,web,papers [--out DIR] [--allow-opus] [--allow-whisper] [--visuals auto|off]
  plan     [--out DIR]     print the plan (models per stage, cost range, quotas, stop conditions)
  status   [--out DIR]     compact counts + spend + time left
  check    [--out DIR] [--phase extract|synth]   exit 0 = may continue, 2 = stop (prints reason)
  next     [--out DIR] [--n 10]                  next pending item ids in value order
  gaps     [--out DIR]     what was NOT processed and why (also used for 00-README)
  extend   [--out DIR] [--budget-usd TOTAL] [--minutes M|--until ISO] [--cap N]   resume a stopped run with new limits
"""
import argparse, sys, time
from collections import Counter
from datetime import datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *  # noqa

TIERS = {"light": 1.0, "moderate": 5.0, "heavy": 15.0}
DEPTH = {"quick": {"creators": 3, "per_creator": 12, "themes": 8},
         "thorough": {"creators": 6, "per_creator": 50, "themes": 16},
         "exhaustive": {"creators": 10, "per_creator": 100000, "themes": 24}}
W_SRC = {"youtube": .30, "github": .25, "reddit": .15, "web": .20, "papers": .10}
# estimated USD per call (low, high). Estimates from small real runs; see references/models.md
EST = {"extract_haiku": (0.002, 0.008), "extract_sonnet": (0.02, 0.07), "rank_batch_haiku": (0.003, 0.01),
       "rank_batch_sonnet": (0.015, 0.05), "theme_sonnet": (0.05, 0.20), "final_sonnet": (0.10, 0.40),
       "final_opus": (0.50, 2.00), "verify_theme_haiku": (0.01, 0.04), "verify_theme_sonnet": (0.04, 0.15),
       "cred_haiku": (0.01, 0.04), "cred_sonnet": (0.04, 0.12)}
CRED_N = {"off": 0, "top5": 5, "top10": 10, "all": 10 ** 6}
CRED_DEFAULT = {"light": "off", "moderate": "top10", "heavy": "all"}
WINDOW_PCT_PER_USD = 5.0  # author's measurement: a Light run of about $1 used roughly 5% of a 5-hour window on one plan; NOT a promise


def tier_of(usd):
    return "light" if usd <= 2 else ("moderate" if usd <= 8 else "heavy")


def models_for(tier, allow_opus, cred="off", synth_model="sonnet"):
    return {
        "scout_list_dedupe": "no model (scripts); haiku only for ambiguous dedupe",
        "creator_judging": "haiku" if tier == "light" else "sonnet",
        "extract": "haiku (effort low)",
        "extract_dense": "haiku" if tier == "light" else "sonnet (effort medium), max %d%% of items" % (20 if tier == "moderate" else 30),
        "theme_synthesis": f"{synth_model} (effort medium)",
        "contradiction_check": f"{synth_model} (inside theme synthesis)",
        "trust_verify": ("haiku" if tier == "light" else "sonnet") + " (effort medium; one call per theme)",
        "credibility": ("off" if cred == "off" else (("haiku" if tier == "light" else "sonnet (haiku beyond the first 10 creators in Moderate)") + f" (effort low; mode {cred})")),
        "final_playbook": "opus (effort high)" if (tier == "heavy" and allow_opus) else f"{synth_model} (effort medium)",
    }


def sonnet_share(tier):
    return {"light": 0.0, "moderate": 0.20, "heavy": 0.30}[tier]


def cmd_init(a):
    topic = a.topic.strip()
    slug = slugify(topic)
    out = Path(a.out).resolve() if a.out else default_out(slug)
    check_out_allowed(out)
    out.mkdir(parents=True, exist_ok=True)
    write_marker(out, topic)
    p = out_paths(out)
    if p["state"].exists() and not a.force:
        print(f"state.json already exists in {out} (resume it, or pass --force to reset limits)")
        return
    now = time.time()
    if a.until:
        dl = datetime.fromisoformat(a.until).timestamp()
    else:
        dl = now + float(a.minutes) * 60
    usd = float(a.budget_usd)
    tier = tier_of(usd)
    srcs = [s.strip() for s in a.sources.split(",") if s.strip()]
    dp = dict(DEPTH[a.depth])
    for k, v in (("creators", a.creators), ("per_creator", a.per_creator), ("themes", a.themes)):
        if v:
            dp[k] = int(v)
    cred = a.credibility or CRED_DEFAULT[tier]
    agent = a.agent_tool or "auto"
    mode = (a.mode.upper() if a.mode and a.mode != "auto" else ("A" if agent == "yes" else ("B" if tool_cmd("claude") else "C")))
    st = {"topic": topic, "slug": slug, "created": now_iso(), "started_ts": now,
          "tier": tier, "depth": a.depth, "depth_params": dp, "sources": srcs,
          "orch": {"mode": mode, "agent_tool": agent, "forced": a.mode if a.mode and a.mode != "auto" else None},
          "keywords": keywords(topic, [k for k in (a.keywords or "").split(",") if k]),
          "limits": {"budget_usd": usd, "deadline_ts": dl, "minutes": round((dl - now) / 60), "max_concurrent": int(a.cap),
                     "extract_budget_share": 0.75, "allow_opus": bool(a.allow_opus), "allow_whisper": bool(a.allow_whisper),
                     "visuals": a.visuals if tier != "light" else "off", "max_visuals": 10 if tier == "moderate" else 30,
                     "sonnet_share": sonnet_share(tier), "lang": a.lang, "credibility": cred, "verify": a.verify != "off",
                     "cred_seed": int(a.cred_seed), "synth_model": a.synth_model},
          "models": models_for(tier, a.allow_opus, cred, a.synth_model), "stage": "planned", "stop_reason": None, "history": []}
    save_state(out, st)
    if not p["manifest"].exists():
        jsave(p["manifest"], {"items": []})
    print(f"initialised {out}\n  tier={tier} budget=${usd:g} minutes={st['limits']['minutes']} cap={a.cap} depth={a.depth}")


def plan_numbers(st):
    L = st["limits"]
    tier = st["tier"]
    ss = L["sonnet_share"]
    lo = (1 - ss) * EST["extract_haiku"][0] + ss * EST["extract_sonnet"][0]
    hi = (1 - ss) * EST["extract_haiku"][1] + ss * EST["extract_sonnet"][1]
    mid = (lo + hi) / 2
    cred = L.get("credibility", "off")
    n_av_cre = st["depth_params"]["creators"] * len(st["sources"])
    n_cred = min(CRED_N.get(cred, 0), n_av_cre)
    # budget split: ~5% ranking, ~50% extraction (+7% when credibility is off), ~25% synthesis, ~8% verify, ~7% credibility, ~5% reserve
    ext_budget = L["budget_usd"] * (0.50 if n_cred else 0.57)
    themes = min(st["depth_params"]["themes"], max(2, int(0.25 * L["budget_usd"] / 0.125)))
    n_lo, n_hi = int(ext_budget / hi), int(ext_budget / lo)
    n_time = int(L["minutes"] * 0.8 * min(L["max_concurrent"] * 3.0, 7.0))  # yt-dlp/politeness bound real throughput
    n_avail = st["depth_params"]["creators"] * min(st["depth_params"]["per_creator"], 200) * len(st["sources"])
    n_plan = max(1, min(int(ext_budget / mid), n_time, n_avail))
    fk = "final_opus" if (tier == "heavy" and L["allow_opus"]) else "final_sonnet"
    rank_k = "rank_batch_haiku" if tier == "light" else "rank_batch_sonnet"
    nb = max(3, len(st["sources"]) * 2)
    sm = L.get("synth_model", "sonnet")
    k_theme = (EST["theme_sonnet"][0] * (0.25 if sm == "haiku" else 1), EST["theme_sonnet"][1] * (0.25 if sm == "haiku" else 1))
    k_final = tuple(x * (0.25 if sm == "haiku" and fk == "final_sonnet" else 1) for x in EST[fk])
    vk = "verify_theme_haiku" if tier == "light" else "verify_theme_sonnet"
    ck = "cred_haiku" if tier == "light" else "cred_sonnet"
    verify = (themes * EST[vk][0], themes * EST[vk][1]) if L.get("verify", True) else (0.0, 0.0)
    credc = (n_cred * EST[ck][0], n_cred * EST[ck][1])
    return dict(n_lo=n_lo, n_hi=n_hi, n_time=n_time, n_plan=n_plan, themes=themes, n_cred=n_cred,
                synth=(themes * k_theme[0] + k_final[0], themes * k_theme[1] + k_final[1]), verify=verify, cred=credc,
                rank=(nb * EST[rank_k][0], nb * EST[rank_k][1]), ext=(n_plan * lo, n_plan * hi))


def window_share(usd):
    return f"{usd * WINDOW_PCT_PER_USD:.0f}%"


def cmd_plan(a):
    st = load_state(a.out)
    L = st["limits"]
    n = plan_numbers(st)
    srcs = st["sources"]
    wsum = sum(W_SRC.get(s, 0) or 0.05 for s in srcs) or 1
    quotas = {s: max(1, int(n["n_plan"] * (W_SRC.get(s, 0) or 0.05) / wsum)) for s in srcs}
    st["quotas"] = quotas
    save_state(a.out, st)
    parts = ("rank", "ext", "synth", "verify", "cred")
    lo = sum(n[p][0] for p in parts)
    hi = min(L["budget_usd"], sum(n[p][1] for p in parts))
    mode = st.get("orch", {}).get("mode", "?")
    print(f"PLAN for '{st['topic']}'  (tier={st['tier']}, depth={st['depth']})")
    print(f"  limits: budget ${L['budget_usd']:g} (API-equivalent), time {L['minutes']} min, concurrent workers cap {L['max_concurrent']} (subagents + headless claude calls combined; workers never spawn workers)")
    print("  orchestration: mode " + mode + " = " + {"A": "manager: this session briefs up to the cap of Agent-tool workers, checks every report, retries once",
                                                      "B": "headless pool of `claude -p` calls sized to the cap", "C": "sequential, this session does the work one item at a time"}.get(mode, "?"))
    print("  models:")
    for k, v in st["models"].items():
        print(f"    {k:20s} {v}")
    print(f"  creators per source: up to {st['depth_params']['creators']}; items per creator: up to {st['depth_params']['per_creator']}")
    print(f"  items: {n['n_lo']}-{n['n_hi']} affordable by budget, ~{n['n_time']} by time -> planning for ~{n['n_plan']}; theme notes: {n['themes']}")
    print("  source quotas (soft; unspent quota flows to sources that still have good items): " + ", ".join(f"{k}={v}" for k, v in quotas.items()))
    print(f"  stages and cost ranges (ESTIMATES; real spend is logged in costs.csv):")
    print(f"    ranking              ${n['rank'][0]:.2f}-{n['rank'][1]:.2f}")
    print(f"    extraction           ${n['ext'][0]:.2f}-{n['ext'][1]:.2f}  (~{n['n_plan']} items)")
    print(f"    synthesis            ${n['synth'][0]:.2f}-{n['synth'][1]:.2f}  ({n['themes']} themes + playbook)")
    print(f"    trust layer (verify) " + (f"${n['verify'][0]:.2f}-{n['verify'][1]:.2f}  (labels every claim; official facts reused, pages fetched only when needed)" if L.get("verify", True) else "off"))
    print(f"    creator credibility  " + (f"${n['cred'][0]:.2f}-{n['cred'][1]:.2f}  ({n['n_cred']} creators, 2 pieces each, mode {L.get('credibility')})" if n["n_cred"] else "off (set --credibility top5|top10|all to add it)"))
    print(f"  expected total: ${lo:.2f}-${hi:.2f}  = very roughly {window_share(lo)} to {window_share(hi)} of one 5-hour usage window.")
    print("    (window share is a rough rule of thumb of about 5% per dollar from one measured Light run; plans differ a lot. Subscription users pay nothing extra: this is API-equivalent value. Check /usage.)")
    print("  stop conditions: time reaches 80% of limit (extraction) / 100% (synthesis); spend reaches 75% of budget (extraction) / 100% (synthesis); manifest exhausted; usage-limit error from the API (stops cleanly, resumable)")
    print(f"  visuals: {L['visuals']}; whisper fallback: {'allowed' if L['allow_whisper'] else 'off'}; opus: {'allowed for final synthesis (heavy tier)' if L['allow_opus'] else 'off'}")
    print(f"  the budget is a hard stop: if real costs run high, extraction ends early (resumable) and the later stages still get their reserve.")


def ordered_pending(out, st=None):
    st = st or load_state(out)
    man = load_manifest(out)
    cre = jload(out_paths(out)["creators"], {})
    items = man["items"]
    by_c = {}
    for it in items:
        by_c.setdefault(it["creator"], []).append(it)
    scored = []
    for cid, its in by_c.items():
        its.sort(key=lambda x: x.get("priority", 1e9))
        cs = cre.get(cid, {}).get("score", 0.3)
        for i, it in enumerate(its):
            if it.get("status", "pending") != "pending":
                continue
            v = cs * (0.5 + it.get("rel", 0.5)) / (1 + i / 20.0)
            scored.append((v, it))
    scored.sort(key=lambda x: -x[0])
    quotas = st.get("quotas", {})
    done = Counter(it["source"] for it in items if it.get("status") == "done")
    within, beyond = [], []
    planned = Counter()
    for v, it in scored:
        s = it["source"]
        if not quotas or done[s] + planned[s] < quotas.get(s, 10**9):
            within.append(it)
            planned[s] += 1
        else:
            beyond.append(it)
    return within + beyond


def cmd_extend(a):
    """Resume with fresh limits: new budget (total, not additional) and/or a new time window starting now."""
    st = load_state(a.out)
    L = st["limits"]
    if a.budget_usd:
        L["budget_usd"] = float(a.budget_usd)
        st["tier"] = tier_of(L["budget_usd"])
        L["sonnet_share"] = sonnet_share(st["tier"])
        st["models"] = models_for(st["tier"], L["allow_opus"], L.get("credibility", "off"), L.get("synth_model", "sonnet"))
    if a.minutes or a.until:
        now = time.time()
        L["deadline_ts"] = datetime.fromisoformat(a.until).timestamp() if a.until else now + float(a.minutes) * 60
        st["started_ts"] = now
        L["minutes"] = round((L["deadline_ts"] - now) / 60)
    if a.cap:
        L["max_concurrent"] = int(a.cap)
    st["stop_reason"] = None
    st.setdefault("history", []).append({"ts": now_iso(), "event": "extend", "limits": {k: L[k] for k in ("budget_usd", "minutes", "max_concurrent")}})
    save_state(a.out, st)
    print(f"limits updated: budget ${L['budget_usd']:g} (already spent ${spent(a.out):.2f}), {L['minutes']} min, cap {L['max_concurrent']}")


def cmd_status(a):
    st = load_state(a.out)
    man = load_manifest(a.out)
    c = Counter(it.get("status", "pending") for it in man["items"])
    left = (st["limits"]["deadline_ts"] - time.time()) / 60
    print(f"{st['topic']} | stage={st['stage']} | spent ${spent(a.out):.3f}/${st['limits']['budget_usd']:g} | "
          f"time left {left:.0f} min | items: " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())) +
          f" | stop={st.get('stop_reason')}")


def cmd_check(a):
    st = load_state(a.out)
    r = check_limits(a.out, st, a.phase)
    if r:
        print("STOP " + r)
        sys.exit(2)
    print("OK")


def cmd_next(a):
    for it in ordered_pending(a.out)[: a.n]:
        print(f"{it['id']}\t{it['source']}\t{it['creator']}\t{(it.get('title') or '')[:70]}")


def cmd_gaps(a):
    st = load_state(a.out)
    man = load_manifest(a.out)
    items = man["items"]
    c = Counter((it["source"], it.get("status", "pending")) for it in items)
    print("by source/status: " + ", ".join(f"{k[0]}:{k[1]}={v}" for k, v in sorted(c.items())))
    pend = Counter(it["creator"] for it in items if it.get("status", "pending") == "pending")
    print("pending by creator (top 10): " + ", ".join(f"{k}={v}" for k, v in pend.most_common(10)))
    sk = Counter(it.get("reason", "?") for it in items if it.get("status") in ("skipped", "failed"))
    print("skipped/failed reasons: " + ", ".join(f"{k}={v}" for k, v in sk.most_common(8)))
    unr = jload(out_paths(a.out)["cache"] / "unreachable.json", [])
    if unr:
        print("unreachable: " + "; ".join(f"{u['source']}:{u['what']} ({u['why']})" for u in unr[:10]))
    print(f"stop_reason={st.get('stop_reason')}")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    i = sp.add_parser("init")
    i.add_argument("--topic", required=True)
    i.add_argument("--out")
    i.add_argument("--budget-usd", required=True)
    i.add_argument("--minutes", default=60)
    i.add_argument("--until")
    i.add_argument("--cap", type=int, default=1)
    i.add_argument("--depth", choices=list(DEPTH), default="quick")
    i.add_argument("--sources", default="github,youtube,reddit,web")
    i.add_argument("--keywords")
    i.add_argument("--lang", default="en")
    i.add_argument("--visuals", default="auto", choices=["auto", "off"])
    i.add_argument("--allow-opus", action="store_true")
    i.add_argument("--allow-whisper", action="store_true")
    i.add_argument("--force", action="store_true")
    i.add_argument("--credibility", choices=list(CRED_N), help="creator credibility stage: off | top5 | top10 | all (default by tier: light off, moderate top10, heavy all)")
    i.add_argument("--verify", choices=["on", "off"], default="on", help="trust layer: label every claim and check numbers against official sources")
    i.add_argument("--agent-tool", choices=["yes", "no", "auto"], default="auto", help="yes when this session has the Agent/subagent tool (selects manager mode A)")
    i.add_argument("--mode", choices=["A", "B", "C", "a", "b", "c", "auto"], default="auto", help="force the orchestration mode")
    i.add_argument("--creators", type=int, help="override creators per source")
    i.add_argument("--per-creator", type=int, help="override items per creator")
    i.add_argument("--themes", type=int, help="override max theme notes")
    i.add_argument("--cred-seed", type=int, default=20260101, help="fixed seed for the random credibility pick")
    i.add_argument("--synth-model", choices=["sonnet", "haiku"], default="sonnet", help="haiku = cheapest synthesis (lower quality)")
    e = sp.add_parser("extend")
    e.add_argument("--out"); e.add_argument("--budget-usd"); e.add_argument("--minutes"); e.add_argument("--until"); e.add_argument("--cap")
    for name in ("plan", "status", "check", "next", "gaps"):
        p = sp.add_parser(name)
        p.add_argument("--out", default=None)
        if name == "check":
            p.add_argument("--phase", default="extract", choices=["extract", "synth"])
        if name == "next":
            p.add_argument("--n", type=int, default=10)
    a = ap.parse_args()
    if a.cmd not in ("init",) and not a.out:
        v = find_vault()
        cands = list(Path("research").glob("*/state.json")) + (list((v / RESEARCH_DIR).glob("*/state.json")) if v else [])
        if len(cands) == 1:
            a.out = str(cands[0].parent.resolve())
        else:
            sys.exit("pass --out DIR (research folders found: " + (", ".join(str(c.parent) for c in cands) or "none") + ")")
    {"init": cmd_init, "plan": cmd_plan, "status": cmd_status, "check": cmd_check, "next": cmd_next, "gaps": cmd_gaps, "extend": cmd_extend}[a.cmd](a)


if __name__ == "__main__":
    main()
