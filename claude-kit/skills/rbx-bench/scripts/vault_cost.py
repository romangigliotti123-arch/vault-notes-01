#!/usr/bin/env python3
"""vault_cost.py: what the vault costs a Claude Code session (stdlib only, no tokenizer library).

  python vault_cost.py --kit <kit source dir>                    measure the kit as /rbx-load would load it (always-on set read from mode/always-on.txt)
  python vault_cost.py --config <claude config dir>              measure an INSTALLED kit (<config>/skills = always-on, <config>/claude-kit/vault-mode = the on-demand store)
  python vault_cost.py --kit <dir> --install-test                also run the real installer into a temp HOME, time it, and measure what it installed
Options: --threshold-chars N (flag descriptions longer than N, default 600) --top N (default 10) --cpt F (characters per token, default 4.0)
         --json | --md FILE | --out DIR (writes vault-cost-<date>.json and .md) --history FILE (append one line to a CSV, default <out>/cost-history.csv) --no-history
         --vault-version TXT (default: env VAULT_VERSION, kit KIT-VERSION file, a git commit of the kit dir, else a short hash of the kit's skills/agents/mode files)
         --install-with auto|bash|ps1 (default auto: install.ps1 on Windows, install.sh elsewhere)

METHOD (stated so the numbers can be challenged; no tiktoken):
  tokens ~= ceil(characters / CPT), CPT = 4.0 (the usual rule of thumb for English prose and code; real tokenizers vary about +-25%, non-ASCII text and long
  identifiers cost more). Characters = Unicode code points of the UTF-8 text. Treat the numbers as an estimate for COMPARING vault versions, not as a bill.
  What costs context in a session:
   * ALWAYS-ON: every skill in <config>/skills (the 5 maintenance commands) lists `name: description` in every session, loaded mode or not.
   * LOAD MODE (after /rbx-load): every store skill and agent copied into the project lists `name: description` too; a skill with
     `disable-model-invocation: true` lists nothing (cost 0 until the user types its command). The mode rules (mode/CLAUDE.md) are printed once at load and stay in the chat.
   * ON INVOKE: the SKILL.md body (and any reference file the model opens) is read only when the skill runs; reported separately (body tokens), never added to the listing total.
  Not counted: tool schemas, Claude Code's own system prompt, the project's CLAUDE.md, the text of command output.
"""
import argparse
import csv
import datetime
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ALWAYS_ON_DEFAULT = ["rbx-load", "rbx-unload", "rbx-update", "rbx-check", "rbx-uninstall"]
CPT = 4.0


def toks(n_chars, cpt=None):
    return int(math.ceil(n_chars / (cpt or CPT))) if n_chars > 0 else 0


# ------------------------------------------------------------------ frontmatter
def read_text(p):
    try:
        with open(p, encoding="utf-8-sig", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def frontmatter(text):
    """-> (dict of top-level scalar keys, body). Handles quoted, plain, folded (> |) and continued multi-line values. Not a general YAML parser."""
    t = text.replace("\r\n", "\n")
    if not t.startswith("---\n"):
        return {}, t
    end = t.find("\n---", 4)
    if end < 0:
        return {}, t
    head, body = t[4:end], t[end + 4:].lstrip("\n")
    fm, key, buf = {}, None, []

    def flush():
        if key is not None:
            v = " ".join(x.strip() for x in buf).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
                v = v.replace('\\"', '"').replace("\\\\", "\\")
            fm[key] = v
    for line in head.split("\n"):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            flush()
            key, v = m.group(1), m.group(2)
            buf = [] if v in (">", "|", ">-", "|-", ">+", "|+") else [v]
        elif key is not None:
            buf.append(line)
    flush()
    return fm, body


def truthy(v):
    return str(v).strip().lower() in ("true", "yes", "1")


def item_info(path, kind, cpt):
    """One skill (dir with SKILL.md) or agent (.md file)."""
    mdp = os.path.join(path, "SKILL.md") if kind == "skill" else path
    text = read_text(mdp)
    fm, body = frontmatter(text)
    name = fm.get("name") or (os.path.basename(path) if kind == "skill" else os.path.basename(path)[:-3])
    desc = fm.get("description", "")
    hidden = truthy(fm.get("disable-model-invocation", ""))
    list_chars = 0 if hidden else len(name) + 2 + len(desc)
    size, files = 0, 0
    if kind == "skill":
        for d, dn, fn in os.walk(path):
            dn[:] = [x for x in dn if x != "__pycache__"]
            for f in fn:
                if not f.endswith(".pyc"):
                    files += 1
                    try:
                        size += os.path.getsize(os.path.join(d, f))
                    except OSError:
                        pass
    else:
        files, size = 1, len(text.encode("utf-8"))
    return dict(kind=kind, name=name, folder=(os.path.basename(path) if kind == "skill" else name), desc_chars=len(desc), hidden=hidden, listing_tokens=toks(list_chars, cpt),
                body_tokens=toks(len(body), cpt), md_tokens=toks(len(text), cpt), files=files, bytes=size, has_description=bool(desc))


def scan_items(skills_dir, agents_dir, cpt):
    out = []
    if skills_dir and os.path.isdir(skills_dir):
        for n in sorted(os.listdir(skills_dir)):
            d = os.path.join(skills_dir, n)
            if os.path.isfile(os.path.join(d, "SKILL.md")):
                out.append(item_info(d, "skill", cpt))
    if agents_dir and os.path.isdir(agents_dir):
        for f in sorted(os.listdir(agents_dir)):
            p = os.path.join(agents_dir, f)
            if f.endswith(".md") and os.path.isfile(p):
                out.append(item_info(p, "agent", cpt))
    return out


def dir_size(path, skip=()):
    total, files = 0, 0
    for d, dn, fn in os.walk(path):
        dn[:] = [x for x in dn if x != "__pycache__" and x not in skip]
        for f in fn:
            if f.endswith(".pyc"):
                continue
            try:
                total += os.path.getsize(os.path.join(d, f))
                files += 1
            except OSError:
                pass
    return total, files


def read_always_on(p):
    out = []
    for line in read_text(p).splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s)
    return out or list(ALWAYS_ON_DEFAULT)


# ------------------------------------------------------------------ version
def tree_hash(kit):
    h = hashlib.sha256()
    for sub in ("skills", "agents", "mode"):
        root = os.path.join(kit, sub)
        for d, dn, fn in os.walk(root):
            dn[:] = sorted(x for x in dn if x != "__pycache__")
            for f in sorted(fn):
                if f.endswith(".pyc"):
                    continue
                p = os.path.join(d, f)
                h.update(os.path.relpath(p, kit).replace(os.sep, "/").encode())
                try:
                    h.update(open(p, "rb").read())
                except OSError:
                    pass
    return h.hexdigest()[:10]


def vault_version(kit=None, config=None, explicit=None):
    """-> short version string. Order: explicit/env, KIT-VERSION file, git commit of the kit dir (or its repo), installed.tsv hash, tree hash."""
    v = explicit or os.environ.get("VAULT_VERSION")
    if v:
        return v
    for base in (kit, config and os.path.join(config, "claude-kit")):
        if base and os.path.isfile(os.path.join(base, "KIT-VERSION")):
            t = read_text(os.path.join(base, "KIT-VERSION")).strip().splitlines()
            if t:
                return t[0][:40]
    if kit and os.path.isdir(kit):
        try:
            r = subprocess.run(["git", "-C", kit, "rev-parse", "--short=10", "HEAD"], capture_output=True, text=True, timeout=20)
            if r.returncode == 0 and r.stdout.strip():
                return "git-" + r.stdout.strip()
        except Exception:
            pass
    if config:
        m = os.path.join(config, "claude-kit", "installed.tsv")
        if os.path.isfile(m):
            return "manifest-" + hashlib.sha256(open(m, "rb").read()).hexdigest()[:10]
    if kit and os.path.isdir(kit):
        return "tree-" + tree_hash(kit)
    return "unknown"


# ------------------------------------------------------------------ measure
def measure_source_kit(kit, cpt, threshold, top):
    ao = read_always_on(os.path.join(kit, "mode", "always-on.txt"))
    all_sk = scan_items(os.path.join(kit, "skills"), None, cpt)
    always = [i for i in all_sk if i["folder"] in ao]
    store = [i for i in all_sk if i["folder"] not in ao] + scan_items(None, os.path.join(kit, "agents"), cpt)
    return _from_lists(always, store, read_text(os.path.join(kit, "mode", "CLAUDE.md")), "source kit " + kit, cpt, threshold, top)


def _from_lists(always, store, rules_text, label, cpt, threshold, top):
    rules_tokens = toks(len(rules_text), cpt)
    al_tok = sum(i["listing_tokens"] for i in always)
    st_tok = sum(i["listing_tokens"] for i in store)
    allitems = always + store
    sk_store = [i for i in store if i["kind"] == "skill"]
    ag_store = [i for i in store if i["kind"] == "agent"]
    flagged = sorted([i for i in allitems if i["desc_chars"] > threshold], key=lambda i: -i["desc_chars"])
    return dict(
        label=label,
        always_on=dict(skills=len(always), listing_tokens=al_tok, names=[i["name"] for i in always]),
        load_mode=dict(skills=len(sk_store), agents=len(ag_store), listing_tokens=st_tok,
                       hidden_from_listing=sorted(i["name"] for i in store if i["hidden"]), rules_chars=len(rules_text), rules_tokens=rules_tokens),
        totals=dict(session_without_load_tokens=al_tok, session_with_load_tokens=al_tok + st_tok + rules_tokens,
                    load_adds_tokens=st_tok + rules_tokens, description_tokens_all=sum(i["listing_tokens"] for i in allitems), items=len(allitems)),
        top_by_listing=[dict(name=i["name"], kind=i["kind"], listing_tokens=i["listing_tokens"], desc_chars=i["desc_chars"])
                        for i in sorted(allitems, key=lambda i: (-i["listing_tokens"], i["name"]))[:top]],
        top_by_body=[dict(name=i["name"], kind=i["kind"], body_tokens=i["body_tokens"])
                     for i in sorted(allitems, key=lambda i: (-i["body_tokens"], i["name"]))[:top]],
        top_by_disk=[dict(name=i["name"], kind=i["kind"], bytes=i["bytes"], files=i["files"])
                     for i in sorted(allitems, key=lambda i: (-i["bytes"], i["name"]))[:top]],
        flagged=dict(threshold_chars=threshold, count=len(flagged),
                     items=[dict(name=i["name"], kind=i["kind"], desc_chars=i["desc_chars"], tokens_over=max(0, toks(i["desc_chars"] - threshold, cpt))) for i in flagged],
                     tokens_saved_if_trimmed_to_threshold=sum(max(0, toks(i["desc_chars"] - threshold, cpt)) for i in flagged)),
        missing_description=[i["name"] for i in allitems if not i["has_description"]],
    )


def measure_installed(config, cpt, threshold, top):
    store = os.path.join(config, "claude-kit", "vault-mode")
    ao_names = read_always_on(os.path.join(store, "always-on.txt"))
    # always-on = the kit skills in <config>/skills (the user's own skills are not the vault's cost)
    sk = os.path.join(config, "skills")
    all_sk = scan_items(sk, None, cpt) if os.path.isdir(sk) else []
    always = [i for i in all_sk if i["folder"] in ao_names]
    st = scan_items(os.path.join(store, ".claude", "skills"), os.path.join(store, ".claude", "agents"), cpt)
    return _from_lists(always, st, read_text(os.path.join(store, "CLAUDE.md")), "installed kit " + config, cpt, threshold, top)


def disk_report(kit=None, config=None):
    out = {}
    if kit and os.path.isdir(kit):
        b, n = dir_size(kit)
        out["kit_source"] = dict(path=kit, bytes=b, files=n, mb=round(b / 1048576, 2),
                                 by_folder={s: dir_size(os.path.join(kit, s))[0] for s in sorted(os.listdir(kit)) if os.path.isdir(os.path.join(kit, s))})
    if config and os.path.isdir(os.path.join(config, "claude-kit")):
        ck = os.path.join(config, "claude-kit")
        b, n = dir_size(ck, skip=("backup", "learnings-queue", "roblox-reference"))
        sk_b = 0
        for d in os.listdir(os.path.join(config, "skills")) if os.path.isdir(os.path.join(config, "skills")) else []:
            sk_b += dir_size(os.path.join(config, "skills", d))[0]
        out["kit_installed"] = dict(path=ck, bytes=b + sk_b, files=n, mb=round((b + sk_b) / 1048576, 2),
                                    by_folder={s: dir_size(os.path.join(ck, s))[0] for s in sorted(os.listdir(ck)) if os.path.isdir(os.path.join(ck, s)) and s not in ("backup", "learnings-queue", "roblox-reference")})
    return out


def run_install(kit, how="auto"):
    """Install the kit into a fresh temp HOME with the real installer. -> (config_dir, seconds, tool, tmp_home, output_tail). The caller removes tmp_home."""
    home = tempfile.mkdtemp(prefix="vaultcost-home-")
    env = dict(os.environ, CLAUDE_KIT_HOME=home)
    env.pop("CLAUDE_CONFIG_DIR", None)
    if how == "auto":
        how = "ps1" if os.name == "nt" and shutil.which("powershell") else "bash"
    t0 = time.time()
    if how == "ps1":
        cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", os.path.join(kit, "install.ps1"), "-KitHome", home]
    else:
        bash = shutil.which("bash")
        if not bash:
            raise RuntimeError("bash not found for install.sh")
        cmd = [bash, os.path.join(kit, "install.sh"), "--home", home]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=1800)
    secs = time.time() - t0
    tail = (r.stdout + r.stderr).strip().splitlines()[-3:]
    if r.returncode != 0:
        shutil.rmtree(home, ignore_errors=True)
        raise RuntimeError("installer failed (%s): %s" % (r.returncode, " | ".join(tail)))
    return os.path.join(home, ".claude"), secs, ("install.ps1" if how == "ps1" else "install.sh"), home, tail


# ------------------------------------------------------------------ output
def md_report(rep):
    t = rep["totals"]
    L = ["# Vault cost: %s" % rep["label"], "",
         "Date %s | vault version %s | method: tokens ~ ceil(chars / %.1f) (no tokenizer; compare versions, do not treat as a bill)" % (rep["date"], rep["vault_version"], rep["cpt"]), "",
         "| what | skills | agents | est. tokens |", "|---|---|---|---|",
         "| session WITHOUT load mode (always-on commands) | %d | 0 | %d |" % (rep["always_on"]["skills"], t["session_without_load_tokens"]),
         "| load mode adds (listing of store skills + agents) | %d | %d | %d |" % (rep["load_mode"]["skills"], rep["load_mode"]["agents"], rep["load_mode"]["listing_tokens"]),
         "| load mode rules text (mode/CLAUDE.md, %d chars) | | | %d |" % (rep["load_mode"]["rules_chars"], rep["load_mode"]["rules_tokens"]),
         "| **session WITH load mode** | %d | %d | **%d** |" % (rep["always_on"]["skills"] + rep["load_mode"]["skills"], rep["load_mode"]["agents"], t["session_with_load_tokens"]), ""]
    if rep["load_mode"]["hidden_from_listing"]:
        L += ["Not listed in context (disable-model-invocation): " + ", ".join(rep["load_mode"]["hidden_from_listing"]), ""]
    L += ["## Heaviest 10 by description (always paid once loaded)", "", "| # | name | kind | desc chars | est. tokens |", "|---|---|---|---|---|"]
    for i, x in enumerate(rep["top_by_listing"], 1):
        L.append("| %d | %s | %s | %d | %d |" % (i, x["name"], x["kind"], x["desc_chars"], x["listing_tokens"]))
    L += ["", "## Heaviest 10 by SKILL.md/agent body (paid only when invoked)", "", "| # | name | est. body tokens |", "|---|---|---|"]
    for i, x in enumerate(rep["top_by_body"], 1):
        L.append("| %d | %s | %d |" % (i, x["name"], x["body_tokens"]))
    L += ["", "## Heaviest 10 on disk (not context)", "", "| # | name | KB | files |", "|---|---|---|---|"]
    for i, x in enumerate(rep["top_by_disk"], 1):
        L.append("| %d | %s | %.0f | %d |" % (i, x["name"], x["bytes"] / 1024, x["files"]))
    f = rep["flagged"]
    L += ["", "## Descriptions over %d chars: %d (trimming them to the threshold would save about %d tokens)" % (f["threshold_chars"], f["count"], f["tokens_saved_if_trimmed_to_threshold"]), ""]
    for x in f["items"][:30]:
        L.append("- %s (%s): %d chars, %d tokens over" % (x["name"], x["kind"], x["desc_chars"], x["tokens_over"]))
    if rep["missing_description"]:
        L += ["", "No description (will never trigger): " + ", ".join(rep["missing_description"])]
    d = rep.get("disk") or {}
    L += ["", "## Disk"]
    for k, v in d.items():
        L.append("- %s: %.2f MB in %d files (%s)" % (k, v["mb"], v["files"], ", ".join("%s %.1f MB" % (a, b / 1048576) for a, b in sorted(v["by_folder"].items(), key=lambda kv: -kv[1])[:6])))
    if rep.get("install"):
        L.append("- install time: %.1f s with %s into a fresh temp HOME" % (rep["install"]["seconds"], rep["install"]["tool"]))
    return "\n".join(L) + "\n"


HIST_COLS = ["date", "vault_version", "label", "skills_always_on", "skills_load", "agents_load", "listing_tokens_always_on", "listing_tokens_load", "rules_tokens",
             "session_with_load_tokens", "flagged_descriptions", "kit_mb", "install_seconds"]


def history_row(rep):
    d = rep.get("disk") or {}
    mb = (d.get("kit_installed") or d.get("kit_source") or {}).get("mb", "")
    return {"date": rep["date"], "vault_version": rep["vault_version"], "label": rep["label"].split(" ")[0] + " " + rep["label"].split(" ")[1] if " " in rep["label"] else rep["label"],
            "skills_always_on": rep["always_on"]["skills"], "skills_load": rep["load_mode"]["skills"], "agents_load": rep["load_mode"]["agents"],
            "listing_tokens_always_on": rep["always_on"]["listing_tokens"], "listing_tokens_load": rep["load_mode"]["listing_tokens"],
            "rules_tokens": rep["load_mode"]["rules_tokens"], "session_with_load_tokens": rep["totals"]["session_with_load_tokens"],
            "flagged_descriptions": rep["flagged"]["count"], "kit_mb": mb, "install_seconds": round(rep["install"]["seconds"], 1) if rep.get("install") else ""}


def append_history(path, row):
    new = not os.path.isfile(path)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HIST_COLS, lineterminator="\n")
        if new:
            w.writeheader()
        w.writerow(row)


def build_report(kit=None, config=None, install_test=False, install_with="auto", threshold=600, top=10, cpt=4.0, version=None, date=None):
    global CPT
    CPT = cpt
    tmp_home = None
    install = None
    try:
        if install_test:
            if not kit:
                raise SystemExit("--install-test needs --kit")
            config, secs, tool, tmp_home, tail = run_install(kit, install_with)
            install = dict(seconds=secs, tool=tool, output_tail=tail)
        if kit and not config:
            rep = measure_source_kit(kit, cpt, threshold, top)
        elif config:
            rep = measure_installed(config, cpt, threshold, top)
        else:
            raise SystemExit("give --kit DIR or --config DIR")
        rep["disk"] = disk_report(kit, config)
        if install:
            rep["install"] = install
            rep["label"] = "installed kit (temp install of %s)" % kit
        rep["date"] = date or datetime.date.today().isoformat()
        rep["vault_version"] = vault_version(kit, config if not install_test else None, version)
        rep["cpt"] = cpt
        rep["kind"] = "vault-cost"
        rep["method"] = "tokens = ceil(chars / %.1f); listing = name + ': ' + description (0 for disable-model-invocation skills); body = SKILL.md after the frontmatter" % cpt
        return rep
    finally:
        if tmp_home:
            shutil.rmtree(tmp_home, ignore_errors=True)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="vault_cost.py", description=__doc__.split("\n")[0])
    ap.add_argument("--kit"); ap.add_argument("--config"); ap.add_argument("--install-test", action="store_true")
    ap.add_argument("--install-with", default="auto", choices=["auto", "bash", "ps1"])
    ap.add_argument("--threshold-chars", type=int, default=600); ap.add_argument("--top", type=int, default=10); ap.add_argument("--cpt", type=float, default=4.0)
    ap.add_argument("--json", action="store_true"); ap.add_argument("--md"); ap.add_argument("--out"); ap.add_argument("--history"); ap.add_argument("--no-history", action="store_true")
    ap.add_argument("--vault-version"); ap.add_argument("--date")
    a = ap.parse_args(argv)
    rep = build_report(a.kit, a.config, a.install_test, a.install_with, a.threshold_chars, a.top, a.cpt, a.vault_version, a.date)
    md = md_report(rep)
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        stem = os.path.join(a.out, "vault-cost-%s" % rep["date"])
        json.dump(rep, open(stem + ".json", "w", encoding="utf-8", newline="\n"), indent=1)
        open(stem + ".md", "w", encoding="utf-8", newline="\n").write(md)
    if a.md:
        open(a.md, "w", encoding="utf-8", newline="\n").write(md)
    if a.json:
        json.dump(rep, sys.stdout, indent=1)
        print()
    else:
        sys.stdout.write(md)
    hist = a.history or (os.path.join(a.out, "cost-history.csv") if a.out else None)
    if hist and not a.no_history:
        append_history(hist, history_row(rep))
        print("HISTORY " + hist, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
