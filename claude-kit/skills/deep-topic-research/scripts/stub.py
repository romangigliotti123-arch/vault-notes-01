#!/usr/bin/env python3
"""stub.py: deterministic offline stand-in for model calls (DTR_STUB=1). Used only by selftest.py and tests; never by real runs.
It builds schema-shaped answers from the prompt text so every stage can be exercised without spending anything."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

_W = re.compile(r"[a-z0-9_.#+]{3,}")


def _toks(s):
    return set(_W.findall(s.lower()))


def _nums(s):
    return re.findall(r"\d[\d,]*(?:\.\d+)?", s)


def extract_from_text(text, themes):
    """claims = first sentences of the body; numbers = digits found in them. Grounded by construction."""
    body = text.split("\n\nExtract everything")[0]
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", body) if len(s.strip()) >= 40 and not s.strip().startswith(("SOURCE:", "TITLE:", "DATE:"))]
    claims, numbers = [], []
    for i, s in enumerate(sents[:5]):
        claims.append({"t": "", "theme": themes[i % len(themes)], "claim": s[:240], "evidence": "doc" if i % 2 == 0 else "opinion", "confidence": "high" if i % 2 == 0 else "medium"})
        for n in _nums(s)[:1]:
            numbers.append({"t": "", "theme": themes[i % len(themes)], "metric": " ".join(s.split()[:4]), "value": n, "context": ""})
    return {"summary": (sents[0] if sents else "empty")[:300], "relevance": 4, "density": "medium", "claims": claims, "numbers": numbers,
            "techniques": [], "code": [], "links": [], "quotes": [], "contradictions": [], "confidence": "medium"}


def _extract(prompt, schema):
    th = schema["properties"]["claims"]["items"]["properties"]["theme"]["enum"]
    return extract_from_text(prompt, th[:-1] or th)


def _theme(prompt):
    rows = [(m.group(1), m.group(2)) for m in re.finditer(r"^\[(S\d+\.[cnt]\d+)\] (.*)$", prompt, re.M)]
    cl = [(r, t) for r, t in rows if ".c" in r]
    kps, used = [], set()
    for r, t in cl[:8]:
        if r in used:
            continue
        refs, tk = [r], _toks(t)
        for r2, t2 in cl:
            if r2 != r and r2 not in used and r2.split(".")[0] != r.split(".")[0] and len(tk & _toks(t2)) >= 4:
                refs.append(r2)
                break
        used.update(refs)
        text = re.sub(r"^\([^)]*\)\s*", "", t)
        kps.append({"point": text[:300], "refs": refs, "confidence": "high" if len(refs) > 1 else "medium", "agreement": "multiple-sources" if len(refs) > 1 else "single-source"})
    nums = []
    for r, t in rows:
        m = re.match(r"NUMBER (.*?) = (.*)$", t)
        if m and len(nums) < 4:
            nums.append({"metric": m.group(1)[:80], "value": m.group(2)[:60], "refs": [r]})
    return {"summary": "stub theme summary", "key_points": kps, "numbers": nums, "techniques": [], "disagreements": [], "gaps": ["stub gap"]}


def _final(prompt):
    pts = [(m.group(1), m.group(2)) for m in re.finditer(r"^\[(T\d+\.\d+)\] \(.*?\) (.*)$", prompt, re.M)]
    steps = [{"action": "Do: " + re.sub(r"^\*\*\[[A-Z-]+\]\*\*\s*|^\[[A-Z-]+\]\s*", "", t)[:150], "why": "stub reason", "support": [i], "confidence": "medium"} for i, t in pts[:8]]
    rec = [{"q": "Stub question %d?" % (n + 1), "a": pts[n % len(pts)][1][:120], "support": [pts[n % len(pts)][0]]} for n in range(10)] if pts else []
    return {"overview": "stub overview", "sections": [{"title": "Core steps", "steps": steps}], "pitfalls": [{"text": "stub pitfall", "support": [pts[0][0]]}] if pts else [],
            "contradictions": [], "open_questions": [{"q": "stub open question", "why": "stub"}], "recall": rec}


def _trust(prompt):
    facts_part, _, claims_part = prompt.partition("CLAIMS TO CHECK:")
    facts = [(m.group(1), m.group(2)) for m in re.finditer(r"^\[([DF]\d+)\] (.*)$", facts_part, re.M)]
    items = []
    for m in re.finditer(r"^\[([PNT]\d+)\] (.*)$", claims_part, re.M):
        cid, txt = m.group(1), m.group(2)
        best, bs = None, 0
        for fid, ft in facts:
            s = len(_toks(txt) & _toks(ft))
            if s >= 3:  # deterministic tie-break: prefer facts that carry numbers, then facts sharing a number with the claim
                s += 0.5 * bool(_nums(ft)) + 0.25 * bool(set(_nums(txt)) & set(_nums(ft)))
            if s > bs:
                best, bs = (fid, ft), s
        if not best or bs < 3:
            items.append({"id": cid, "verdict": "unverified", "fact_ids": []})
            continue
        cn, fn = _nums(txt), _nums(best[1])
        if cn and fn and not (set(cn) & set(fn)):
            items.append({"id": cid, "verdict": "corrected", "fact_ids": [best[0]], "official_value": fn[0], "corrected_text": txt.replace(cn[0], fn[0], 1)})
        else:
            items.append({"id": cid, "verdict": "confirmed", "fact_ids": [best[0]]})
    return {"items": items}


def _cred(prompt):
    pk = json.loads(prompt.split("PACKET:\n", 1)[1])
    claims = []
    for v in pk["videos"]:
        for tip in v["tips"][:6]:
            txt, hits = tip["tip"], (tip.get("docs") or []) + (tip.get("others") or [])
            cn = _nums(txt)
            hn = [n for h in hits for n in _nums(h)]
            if hits and cn and hn and not (set(cn) & set(hn)):
                vd, basis = "WRONG", "official" if tip.get("docs") else "other-sources"
            elif hits:
                vd, basis = "CORRECT", "both" if tip.get("docs") and tip.get("others") else ("official" if tip.get("docs") else "other-sources")
            else:
                vd, basis = ("UNVERIFIABLE", "none") if cn else ("OPINION", "none")
            claims.append({"video": v["id"], "claim": txt[:160], "verdict": vd, "basis": basis, "note": "stub check"})
    return {"claims": claims, "evidence_score": 6.0, "depth_score": 5.0, "honesty_score": 7.0, "signals": "stub signals", "reason": "stub reason", "confidence": "medium"}


def stub_call(stage, prompt, schema, model):
    if stage.startswith("extract"):
        return _extract(prompt, schema)
    if stage == "synth-theme":
        return _theme(prompt)
    if stage == "synth-final":
        return _final(prompt)
    if stage == "trust-verify":
        return _trust(prompt)
    if stage == "cred":
        return _cred(prompt)
    if stage == "rank":
        ids = re.findall(r'"id": "([^"]+)"', prompt)
        return {"ratings": [{"id": i, "relevance": 4, "depth": 3, "credibility": 3, "originality": 3, "reason": "stub"} for i in ids]}
    raise RuntimeError("stub has no handler for stage " + stage)
