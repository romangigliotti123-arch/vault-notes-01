#!/usr/bin/env python3
"""gen_image.py - generate game art with Google's newest "Nano Banana" (Gemini image) model, from the user's own API key.

Standard library only (urllib). The key is read from env GEMINI_API_KEY or GOOGLE_API_KEY and is never stored, printed or logged.
No hard-coded model name: `lookup` asks the user's own account for its model list and picks the newest image-capable Gemini model.

  gen_image.py lookup   [--prefer default|pro|fast] [--mock-models FILE] [--out DIR]
  gen_image.py generate (--prompt TEXT | --prompt-file FILE) [--ref IMG ...] [--aspect 16:9] [--size 2K] [--name NAME]
                        [--out DIR] [--model ID] [--prefer default|pro|fast] [--api auto|interactions|generatecontent] [--dry-run]
  gen_image.py batch    --prompts-file prompts.json [same options]      # [{"name": "...", "prompt": "...", "aspect": "16:9", "refs": ["a.png"]}, ...]
  gen_image.py --selftest

Exit codes: 0 ok · 2 bad usage / API error · 3 NO KEY (prompts are still written to OUT/prompts.md, with instructions; stop gracefully).
Outputs go to --out (default ./art): <name>.png|jpg + <name>.json (prompt, model, api, aspect, size, refs, time) + image-model.json (what lookup found).
All images from these models carry a provider watermark (SynthID); treat them as AI-generated, review against Roblox content rules before upload.
"""
import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.request

BASE = os.environ.get("GEN_IMAGE_API_BASE", "https://generativelanguage.googleapis.com/v1beta")  # override only for tests against a mock server
MAX_REFS = 14
BAD_WORDS = ("imagen", "embedding", "tts", "audio", "live", "aqa", "robotics", "veo", "video", "computer-use", "learnlm", "gemma", "text-")


def get_key():
    for n in ("GEMINI_API_KEY", "GOOGLE_API_KEY"):
        v = os.environ.get(n, "").strip()
        if v:
            return v
    return ""


def scrub(text, key):
    return text.replace(key, "***") if key else text


def http(method, url, key, body=None, timeout=120):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("x-goog-api-key", key)
    if body is not None:
        req.add_header("Content-Type", "application/json")
    last = None
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", "replace")[:600]
            last = (e.code, {"error": scrub(raw, key)})
            if e.code in (429, 500, 502, 503) and attempt == 1:
                time.sleep(5)
                continue
            return last
        except Exception as e:  # network down, timeout
            last = (0, {"error": scrub(str(e), key)})
            if attempt == 1:
                time.sleep(2)
    return last


# ---------- model lookup ----------
def list_models(key, mock=None):
    if mock:
        with open(mock, encoding="utf-8") as f:
            d = json.load(f)
        return d["models"] if isinstance(d, dict) else d
    out, tok = [], ""
    for _ in range(10):
        st, d = http("GET", BASE + "/models?pageSize=200" + ("&pageToken=" + tok if tok else ""), key, timeout=40)
        if st != 200:
            raise RuntimeError("model list failed: HTTP %s %s" % (st, d.get("error", "")))
        out += d.get("models", [])
        tok = d.get("nextPageToken", "")
        if not tok:
            break
    return out


def _num(s):
    return tuple(int(p) for p in s.split("."))


def classify(m):
    """Return None if not an image-generation Gemini model, else a dict with the ranking facts."""
    mid = m.get("name", "").split("/")[-1].lower()
    dn = (m.get("displayName") or "").lower()
    desc = (m.get("description") or "").lower()
    if any(b in mid for b in BAD_WORDS):
        return None
    banana = "nano banana" in dn or "nano-banana" in mid or "nano banana" in desc
    imagey = banana or re.search(r"(^|-)image($|-)", mid) is not None
    if not imagey:
        return None
    methods = m.get("supportedGenerationMethods") or []
    if methods and not any(x in methods for x in ("generateContent", "createInteraction", "interactions")):
        return None
    pro = "pro" in mid.split("-") or "pro" in dn.split()
    lite = "lite" in mid or "lite" in dn
    flash = "flash" in mid or "flash" in dn
    nick = re.search(r"nano[ -]banana(?:[ -]pro)?[ -]*(\d+(?:\.\d+)?)", dn) or re.search(r"nano-banana-(\d+(?:\.\d+)?)", mid)
    gen = re.search(r"gemini-(\d+(?:\.\d+)?)", mid)
    if nick:
        ver = _num(nick.group(1))
    elif banana and not pro:
        ver = (1,)  # the original, un-numbered "Nano Banana"
    elif gen:
        ver = _num(gen.group(1))
    else:
        ver = (0,)
    return {"id": mid, "display": m.get("displayName", ""), "version": ver, "pro": pro, "lite": lite, "fast": lite or (flash and not pro),
            "preview": "preview" in mid or "exp" in mid.split("-"), "banana": banana}


def choose_model(models, prefer="default"):
    cands = [c for c in (classify(m) for m in models) if c]
    if not cands:
        return None, []
    pool = [c for c in cands if c["banana"]] or cands
    if prefer == "pro":
        sub = [c for c in pool if c["pro"]] or pool
    elif prefer == "fast":
        sub = [c for c in pool if c["fast"]] or pool
    else:
        sub = [c for c in pool if not c["pro"] and not c["lite"]] or pool
    sub.sort(key=lambda c: (c["version"], not c["preview"], not c["lite"], c["id"]), reverse=True)
    return sub[0], cands


def lookup(key, prefer, mock=None, out=None, quiet=False):
    models = list_models(key, mock)
    best, cands = choose_model(models, prefer)
    rec = {"checked": time.strftime("%Y-%m-%d %H:%M:%S"), "prefer": prefer, "chosen": best["id"] if best else None,
           "candidates": [{"id": c["id"], "display": c["display"], "version": ".".join(map(str, c["version"])), "pro": c["pro"], "lite": c["lite"], "preview": c["preview"]}
                          for c in sorted(cands, key=lambda c: c["version"], reverse=True)]}
    if out:
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "image-model.json"), "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=1)
    if not quiet:
        print("image model lookup (%s): chosen=%s" % (rec["checked"], rec["chosen"]))
        for c in rec["candidates"]:
            print("  candidate %-40s v%-5s %s%s%s" % (c["id"], c["version"], "pro " if c["pro"] else "", "lite " if c["lite"] else "", "preview" if c["preview"] else ""))
    return best, rec


# ---------- request / response ----------
def b64_file(path):
    mime = mimetypes.guess_type(path)[0] or "image/png"
    if not mime.startswith("image/"):
        raise ValueError("reference is not an image: " + path)
    with open(path, "rb") as f:
        return mime, base64.b64encode(f.read()).decode("ascii")


def build_interactions(model, prompt, refs, aspect, size):
    parts = [{"type": "text", "text": prompt}] + [{"type": "image", "mime_type": m, "data": d} for m, d in refs]
    fmt = {"type": "image"}
    if aspect:
        fmt["aspect_ratio"] = aspect
    if size:
        fmt["image_size"] = size
    return "/interactions", {"model": model, "input": parts, "response_format": fmt}


def build_generate_content(model, prompt, refs, aspect, size):
    parts = [{"text": prompt}] + [{"inline_data": {"mime_type": m, "data": d}} for m, d in refs]
    ic = {}
    if aspect:
        ic["aspectRatio"] = aspect
    if size:
        ic["imageSize"] = size
    gc = {"responseModalities": ["TEXT", "IMAGE"]}
    if ic:
        gc["imageConfig"] = ic
    return "/models/%s:generateContent" % model, {"contents": [{"role": "user", "parts": parts}], "generationConfig": gc}


def find_images(node, found=None):
    """Walk any response shape and collect (mime, bytes) for base64 image payloads (Interactions or generateContent)."""
    found = [] if found is None else found
    if isinstance(node, dict):
        data = node.get("data")
        mime = node.get("mime_type") or node.get("mimeType")
        if isinstance(data, str) and isinstance(mime, str) and mime.startswith("image/") and len(data) > 100:
            try:
                found.append((mime, base64.b64decode(data)))
            except Exception:
                pass
        for v in node.values():
            find_images(v, found)
    elif isinstance(node, list):
        for v in node:
            find_images(v, found)
    return found


def generate_one(key, model, api, prompt, ref_paths, aspect, size, out, name, dry):
    refs = [b64_file(p) for p in ref_paths[:MAX_REFS]]
    order = {"interactions": ["interactions"], "generatecontent": ["generatecontent"], "auto": ["interactions", "generatecontent"]}[api]
    errors = []
    for which in order:
        path, body = (build_interactions if which == "interactions" else build_generate_content)(model, prompt, refs, aspect, size)
        if dry:
            red = json.loads(json.dumps(body))
            print("DRY RUN %s POST %s%s\n%s" % (which, BASE, path, json.dumps(_redact(red), indent=1)[:1500]))
            return [], which
        st, resp = http("POST", BASE + path, key, body)
        if st == 200:
            imgs = find_images(resp)
            if imgs:
                saved = []
                for i, (mime, raw) in enumerate(imgs):
                    ext = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp"}.get(mime, "bin")
                    fn = os.path.join(out, "%s%s.%s" % (name, "" if i == 0 else "-%d" % (i + 1), ext))
                    with open(fn, "wb") as f:
                        f.write(raw)
                    saved.append(fn)
                with open(os.path.join(out, name + ".json"), "w", encoding="utf-8") as f:
                    json.dump({"prompt": prompt, "model": model, "api": which, "aspect": aspect, "size": size, "refs": [os.path.basename(p) for p in ref_paths[:MAX_REFS]],
                               "time": time.strftime("%Y-%m-%d %H:%M:%S"), "files": [os.path.basename(s) for s in saved]}, f, indent=1)
                return saved, which
            errors.append("%s: HTTP 200 but no image in the response (blocked or text-only): %s" % (which, json.dumps(resp)[:300]))
            continue
        errors.append("%s: HTTP %s %s" % (which, st, json.dumps(resp.get("error", resp))[:300]))
        if st in (401, 403):
            break  # key problem, the other transport will not help
    raise RuntimeError(" | ".join(errors))


def _redact(o):
    if isinstance(o, dict):
        return {k: ("<base64 omitted>" if k == "data" and isinstance(v, str) and len(v) > 100 else _redact(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [_redact(v) for v in o]
    return o


def no_key_exit(jobs, out):
    os.makedirs(out, exist_ok=True)
    lines = ["# Prompts (no API key found, nothing was generated)", ""]
    for j in jobs:
        lines += ["## " + j["name"], "aspect: %s  refs: %s" % (j.get("aspect") or "-", ", ".join(j.get("refs") or []) or "-"), "", j["prompt"], ""]
    with open(os.path.join(out, "prompts.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("NO KEY: set GEMINI_API_KEY (or GOOGLE_API_KEY) in your shell environment to generate images here. The key is only read from the environment; this script never stores or prints it.")
    print("Get a key from Google AI Studio (https://aistudio.google.com/apikey), then re-run. Nothing was sent anywhere.")
    print("Meanwhile: paste each prompt from %s into Google AI Studio or the Gemini app with the newest image model selected, attach the reference photos, and download the results." % os.path.join(out, "prompts.md"))
    return 3


def selftest():
    mock = [
        {"name": "models/gemini-2.5-flash-image", "displayName": "Nano Banana", "supportedGenerationMethods": ["generateContent"]},
        {"name": "models/gemini-3-pro-image-preview", "displayName": "Nano Banana Pro", "supportedGenerationMethods": ["generateContent"]},
        {"name": "models/gemini-3.1-flash-image-preview", "displayName": "Nano Banana 2", "supportedGenerationMethods": ["generateContent"]},
        {"name": "models/gemini-nano-banana-2.1", "displayName": "Nano Banana 2.1", "supportedGenerationMethods": ["generateContent"]},
        {"name": "models/gemini-3.1-flash-lite-image", "displayName": "Nano Banana 2 Lite", "supportedGenerationMethods": ["generateContent"]},
        {"name": "models/imagen-4.0-generate-001", "displayName": "Imagen 4", "supportedGenerationMethods": ["predict"]},
        {"name": "models/gemini-2.5-pro", "displayName": "Gemini 2.5 Pro", "supportedGenerationMethods": ["generateContent"]},
        {"name": "models/text-embedding-004", "displayName": "Embedding", "supportedGenerationMethods": ["embedContent"]},
    ]
    b, c = choose_model(mock)
    assert b["id"] == "gemini-nano-banana-2.1", b
    assert len(c) == 5, [x["id"] for x in c]
    assert choose_model(mock, "pro")[0]["id"] == "gemini-3-pro-image-preview"
    assert choose_model(mock, "fast")[0]["id"] == "gemini-3.1-flash-lite-image"
    future = mock + [{"name": "models/gemini-nano-banana-3", "displayName": "Nano Banana 3", "supportedGenerationMethods": ["generateContent"]}]
    assert choose_model(future)[0]["id"] == "gemini-nano-banana-3"
    assert choose_model([{"name": "models/gemini-2.5-pro"}])[0] is None
    png = base64.b64encode(b"\x89PNG" + b"0" * 200).decode()
    for shape in ({"output_image": {"data": png, "mime_type": "image/png"}},
                  {"steps": [{"content": [{"type": "image", "mime_type": "image/png", "data": png}]}]},
                  {"candidates": [{"content": {"parts": [{"text": "x"}, {"inlineData": {"mimeType": "image/png", "data": png}}]}}]}):
        assert len(find_images(shape)) == 1, shape
    assert find_images({"candidates": [{"content": {"parts": [{"text": "blocked"}]}}]}) == []
    assert scrub("abc SECRET def", "SECRET") == "abc *** def"
    print("selftest ok")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["lookup", "generate", "batch"])
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--prompts-file")
    ap.add_argument("--ref", action="append", default=[])
    ap.add_argument("--aspect")
    ap.add_argument("--size")
    ap.add_argument("--name", default="image")
    ap.add_argument("--out", default="art")
    ap.add_argument("--model")
    ap.add_argument("--prefer", choices=["default", "pro", "fast"], default="default")
    ap.add_argument("--api", choices=["auto", "interactions", "generatecontent"], default="auto")
    ap.add_argument("--mock-models")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    jobs = []
    if a.cmd == "generate":
        p = a.prompt if a.prompt else (open(a.prompt_file, encoding="utf-8").read().strip() if a.prompt_file else "")
        if not p:
            print("generate needs --prompt or --prompt-file", file=sys.stderr)
            return 2
        jobs = [{"name": a.name, "prompt": p, "aspect": a.aspect, "size": a.size, "refs": a.ref}]
    elif a.cmd == "batch":
        if not a.prompts_file:
            print("batch needs --prompts-file", file=sys.stderr)
            return 2
        with open(a.prompts_file, encoding="utf-8") as f:
            jobs = json.load(f)
        for j in jobs:
            j.setdefault("aspect", a.aspect)
            j.setdefault("size", a.size)
            j.setdefault("refs", a.ref)

    key = get_key()
    if a.cmd in ("generate", "batch") and not key and not a.dry_run:
        return no_key_exit(jobs, a.out)
    if a.cmd == "lookup" and not key and not a.mock_models:
        print("NO KEY: lookup asks your own account for its model list, so it needs GEMINI_API_KEY or GOOGLE_API_KEY in the environment (or --mock-models FILE for a test). Nothing was sent.")
        return 3

    os.makedirs(a.out, exist_ok=True)
    model = a.model
    try:
        if not model and not (a.dry_run and not key):
            best, rec = lookup(key, a.prefer, a.mock_models, a.out, quiet=(a.cmd != "lookup"))
            if a.cmd == "lookup":
                return 0 if best else 2
            if not best:
                print("no image-capable Gemini model found in this account's model list (see image-model.json)", file=sys.stderr)
                return 2
            model = best["id"]
            print("using model %s (looked up now; recorded in %s)" % (model, os.path.join(a.out, "image-model.json")))
        elif not model:
            model = "<model looked up at run time>"
        failed = 0
        for j in jobs:
            try:
                saved, which = generate_one(key, model, a.api, j["prompt"], j.get("refs") or [], j.get("aspect"), j.get("size"), a.out, re.sub(r"[^A-Za-z0-9_.-]", "_", j["name"]), a.dry_run)
                for s in saved:
                    print("saved %s (%s via %s)" % (s, model, which))
            except (RuntimeError, ValueError, OSError) as e:
                failed += 1
                print("FAILED %s: %s" % (j["name"], scrub(str(e), key)), file=sys.stderr)
        return 2 if failed else 0
    except RuntimeError as e:
        print(scrub(str(e), key), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
