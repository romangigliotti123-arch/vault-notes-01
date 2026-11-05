#!/usr/bin/env python3
"""ui_assets.py: source-of-truth folder, naming and bookkeeping for UI art assets. Stdlib only. It makes NO network call and never uploads: upload is a manual Studio step or a documented
Open Cloud call the user runs with their own key (`steps` prints both).

  ui_assets.py layout <project>                          creates <project>/ui/{assets-src,assets-export} and ui/uploads.json
  ui_assets.py name --game G --screen S --element E [--state st] --size WxH [--ext png]   -> the canonical file name <game>_<screen>_<element>[_<state>]_<W>x<H>.png
  ui_assets.py check <file>                              name pattern, extension, size limits (png/jpg/bmp/tga, <= 20 MB, < 8000x8000 for png)
  ui_assets.py export <project>                          copies valid ui/assets-src files to ui/assets-export, records sha256/bytes/size in ui/uploads.json (unchanged files keep their ids)
  ui_assets.py record <project> --file NAME --asset-id N [--moderation approved|pending|rejected] [--source TEXT]    note an id the user got from Studio or Open Cloud
  ui_assets.py ref <project> NAME                        prints rbxassetid://<id> for a recorded file
  ui_assets.py steps                                     manual and Open Cloud upload steps (documentation only)
"""
import hashlib
import json
import os
import re
import shutil
import struct
import sys

NAME_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+){2,3}_\d{2,4}x\d{2,4}\.(png|jpg|jpeg|bmp|tga)$")
MAX_BYTES = 20 * 1024 * 1024
STEPS = """UPLOAD STEPS (documentation; this tool never uploads and never reads a key)
Manual (default, no key): open Roblox Studio > View > Asset Manager > Images > Bulk Import (or Import), choose the files in ui/assets-export/, wait for moderation, then copy each asset id
  (right-click the image > Copy Asset ID) and note it with: ui_assets.py record <project> --file <name> --asset-id <id>. Use rbxassetid://<id> in Image properties and test in Studio.
Open Cloud (optional, your own key, run by you): per Roblox's Assets API guide (create.roblox.com/docs/cloud/guides/usage-assets): create an API key with the Assets read+write permission in the
  Creator Hub, send a multipart POST to https://apis.roblox.com/assets/v1/assets (JSON `request` part: assetType Decal, displayName, description, creationContext with your userId or groupId; `fileContent`
  part: the file) with header x-api-key, then poll GET /assets/v1/operations/<id> until done; the response holds the assetId and a moderationResult. Never put the key in a project file or this vault.
Rules: every upload passes Roblox moderation; no real-world brands, characters or other games' UI in the art; keep prompt, model and date next to the file (the `source` field of ui/uploads.json);
  a decal cannot be updated, a re-upload gets a new id; ask the user before any upload."""


def png_size(p):
    with open(p, "rb") as f:
        h = f.read(24)
    if h[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", h[16:24])


def check_file(p):
    errs = []
    n = os.path.basename(p)
    if not NAME_RE.match(n):
        errs.append("name %r must look like game_screen_element_state_WxH.png (lowercase letters, digits, underscores)" % n)
    if not os.path.isfile(p):
        return errs + ["file not found"]
    if os.path.getsize(p) > MAX_BYTES:
        errs.append("larger than 20 MB")
    sz = png_size(p) if n.lower().endswith(".png") else None
    if n.lower().endswith(".png"):
        if not sz:
            errs.append("not a valid PNG")
        elif sz[0] >= 8000 or sz[1] >= 8000:
            errs.append("PNG %dx%d must be under 8000x8000" % sz)
        else:
            m = re.search(r"_(\d+)x(\d+)\.png$", n.lower())
            if m and (int(m.group(1)), int(m.group(2))) != sz:
                errs.append("name says %sx%s but the PNG is %dx%d" % (m.group(1), m.group(2), sz[0], sz[1]))
    return errs


def uploads_path(project):
    return os.path.join(project, "ui", "uploads.json")


def load_uploads(project):
    try:
        with open(uploads_path(project), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {"version": 1, "assets": {}}


def save_uploads(project, d):
    os.makedirs(os.path.join(project, "ui"), exist_ok=True)
    with open(uploads_path(project), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=1, sort_keys=True)
        f.write("\n")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "", str(s).lower())


def make_name(game, screen, element, state, size, ext="png"):
    parts = [slug(game), slug(screen), slug(element)] + ([slug(state)] if state else [])
    if not all(parts) or not re.fullmatch(r"\d{2,4}x\d{2,4}", size):
        raise SystemExit("name needs non-empty game, screen, element and --size WxH (two to four digits each)")
    return "_".join(parts) + "_" + size + "." + ext.lower().lstrip(".")


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a and a.index(n) + 1 < len(a) else d
    c = a[0]
    if c == "steps":
        print(STEPS)
        return 0
    if c == "name":
        print(make_name(opt("--game"), opt("--screen"), opt("--element"), opt("--state"), opt("--size", ""), opt("--ext", "png")))
        return 0
    if c == "check":
        errs = check_file(a[1])
        for e in errs:
            print("ERROR " + e)
        print("ui_assets check: %s" % ("ok" if not errs else "%d problems" % len(errs)))
        return 1 if errs else 0
    if len(a) < 2:
        print("usage: ui_assets.py layout|export|record|ref <project> ...", file=sys.stderr)
        return 2
    proj = a[1]
    if c == "layout":
        for d in ("assets-src", "assets-export"):
            os.makedirs(os.path.join(proj, "ui", d), exist_ok=True)
        if not os.path.isfile(uploads_path(proj)):
            save_uploads(proj, {"version": 1, "assets": {}})
        print("ui_assets: %s ready (assets-src = source of truth, assets-export = what you import)" % os.path.join(proj, "ui"))
        return 0
    if c == "export":
        src, dst = os.path.join(proj, "ui", "assets-src"), os.path.join(proj, "ui", "assets-export")
        if not os.path.isdir(src):
            print("ui_assets: no ui/assets-src folder (run layout first)")
            return 1
        os.makedirs(dst, exist_ok=True)
        up = load_uploads(proj)
        n = bad = 0
        for f in sorted(os.listdir(src)):
            p = os.path.join(src, f)
            if not os.path.isfile(p):
                continue
            errs = check_file(p)
            if errs:
                bad += 1
                print("SKIP %s: %s" % (f, "; ".join(errs)))
                continue
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()
            old = up["assets"].get(f, {})
            shutil.copyfile(p, os.path.join(dst, f))
            sz = png_size(p)
            ent = {"sha256": h, "bytes": os.path.getsize(p), "size": list(sz) if sz else None, "asset_id": old.get("asset_id") if old.get("sha256") == h else None,
                   "moderation": old.get("moderation") if old.get("sha256") == h else None, "source": old.get("source")}
            up["assets"][f] = ent
            n += 1
        save_uploads(proj, up)
        print("ui_assets: exported %d, skipped %d (see messages); import them by hand: ui_assets.py steps" % (n, bad))
        return 1 if bad and not n else 0
    if c == "record":
        f, aid = opt("--file"), opt("--asset-id", "")
        if not f or not re.fullmatch(r"\d{4,20}", aid):
            print("usage: ui_assets.py record <project> --file NAME --asset-id <digits> [--moderation approved|pending|rejected] [--source TEXT]", file=sys.stderr)
            return 2
        up = load_uploads(proj)
        ent = up["assets"].setdefault(f, {})
        ent["asset_id"] = aid
        if opt("--moderation") in ("approved", "pending", "rejected"):
            ent["moderation"] = opt("--moderation")
        if opt("--source"):
            ent["source"] = opt("--source")[:200]
        save_uploads(proj, up)
        print("ui_assets: recorded %s -> rbxassetid://%s" % (f, aid))
        return 0
    if c == "ref":
        ent = load_uploads(proj)["assets"].get(a[2] if len(a) > 2 else "", {})
        if not ent.get("asset_id"):
            print("no asset id recorded for that file")
            return 1
        print("rbxassetid://" + str(ent["asset_id"]))
        return 0
    print("unknown command " + c, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
