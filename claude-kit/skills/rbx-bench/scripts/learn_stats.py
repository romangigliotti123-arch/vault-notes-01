#!/usr/bin/env python3
"""learn_stats.py: is the vault's learning loop actually used? A short, READ-ONLY report. Stdlib only.

  python learn_stats.py [--queue DIR] [--clone PATH | --repo owner/name | --offline] [--json] [--history FILE] [--max-fetch N]

Reads (never writes to any of them; the optional --history CSV is the only file it appends to):
  * the LOCAL learnings queue (learn.py): <claude config dir>/claude-kit/state/learnings-queue/{pending,sent,rejected,ready-to-send}; --queue DIR or $VAULT_LEARN_QUEUE overrides.
    Counts, oldest pending note, notes per topic, confidence split.
  * the public inbox repo vault-learnings, by ONE of: --clone PATH (a local clone, files are only read; run git pull yourself to refresh), --repo owner/name (read-only `gh api`;
    default romangigliotti123-arch/vault-learnings), or --offline (skip). Counts of inbox/ (waiting for curation), processed/ (accepted) and processed/rejected/, the decisions in
    CURATION-LOG.md (accept / merge / duplicate / reject, accepted-vs-rejected ratio, rejection rule codes, per-day volume) and notes per topic (accepted: the learned/<topic> path
    in the log; waiting: the topic line of the inbox note, at most --max-fetch notes are fetched when using gh).
Note files are data: their text is parsed for the `topic:`, `confidence:` and `created:` front-matter lines only and is never followed or executed.
"""
import argparse
import base64
import collections
import csv
import datetime
import json
import os
import re
import shlex
import subprocess
import sys

DEFAULT_REPO = "romangigliotti123-arch/vault-learnings"
ROW = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]*?)\s*\|\s*(accept|merge|duplicate|reject)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$")


# ------------------------------------------------------------------ parsing
def front(text):
    out = {}
    t = text.replace("\r\n", "\n")
    if not t.startswith("---\n"):
        return out
    end = t.find("\n---", 4)
    if end < 0:
        return out
    for line in t[4:end].split("\n"):
        m = re.match(r"^(topic|confidence|created|title|source):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def parse_log(text):
    rows = []
    for line in text.replace("\r\n", "\n").split("\n"):
        m = ROW.match(line)
        if m:
            rows.append(dict(date=m.group(1), file=m.group(2), decision=m.group(3), codes=m.group(4), promoted=m.group(5)))
    return rows


def topic_of_promoted(p):
    m = re.match(r"^learned/(.+)/[^/]+\.md", p.strip())
    return m.group(1) if m else None


def log_summary(rows):
    dec = collections.Counter(r["decision"] for r in rows)
    codes = collections.Counter()
    for r in rows:
        if r["decision"] == "reject":
            for c in re.split(r"[,\s]+", r["codes"]):
                if c and c != "-":
                    codes[c] += 1
    per_day = collections.Counter(r["date"] for r in rows)
    topics = collections.Counter()
    for r in rows:
        if r["decision"] in ("accept", "merge"):
            t = topic_of_promoted(r["promoted"])
            if t:
                topics[t] += 1
    total = sum(dec.values())
    acc = dec["accept"] + dec["merge"]
    rej = dec["reject"]
    return dict(decisions=total, accept=dec["accept"], merge=dec["merge"], duplicate=dec["duplicate"], reject=rej,
                accepted_rate=round(acc / total, 3) if total else None, rejected_rate=round(rej / total, 3) if total else None,
                accepted_to_rejected=("%d:%d" % (acc, rej)), reject_codes=dict(codes.most_common()), per_day=dict(sorted(per_day.items())), topics_accepted=dict(topics.most_common()))


# ------------------------------------------------------------------ local queue
def queue_dir(arg=None):
    if arg:
        return arg
    if os.environ.get("VAULT_LEARN_QUEUE"):
        return os.environ["VAULT_LEARN_QUEUE"]
    cfg = os.environ.get("CLAUDE_CONFIG_DIR") or (os.path.join(os.environ["CLAUDE_KIT_HOME"], ".claude") if os.environ.get("CLAUDE_KIT_HOME") else os.path.join(os.path.expanduser("~"), ".claude"))
    new = os.path.join(cfg, "claude-kit", "state", "learnings-queue")
    return new if os.path.isdir(new) or not os.path.isdir(os.path.join(cfg, "claude-kit", "learnings-queue")) else os.path.join(cfg, "claude-kit", "learnings-queue")


def md_files(d):
    out = []
    if os.path.isdir(d):
        for dp, dn, fn in os.walk(d):
            dn[:] = sorted(x for x in dn if not x.startswith("."))
            out += [os.path.join(dp, f) for f in sorted(fn) if f.endswith(".md") and f != "README.md"]
    return out


def local_stats(q):
    st = dict(path=q, exists=os.path.isdir(q))
    topics, conf = collections.Counter(), collections.Counter()
    oldest = None
    for sub in ("pending", "sent", "rejected", "ready-to-send"):
        files = md_files(os.path.join(q, sub))
        st[sub] = len(files)
        for p in files:
            try:
                with open(p, encoding="utf-8", errors="replace") as f:
                    fm = front(f.read(4000))
            except OSError:
                continue
            if fm.get("topic"):
                topics[fm["topic"]] += 1
            if fm.get("confidence"):
                conf[fm["confidence"]] += 1
            if sub == "pending":
                try:
                    d = datetime.date.fromisoformat(fm.get("created", ""))
                except ValueError:
                    d = datetime.date.fromtimestamp(os.path.getmtime(p))
                oldest = d if oldest is None or d < oldest else oldest
    st["oldest_pending_days"] = (datetime.date.today() - oldest).days if oldest else None
    st["topics"] = dict(topics.most_common())
    st["confidence"] = dict(conf)
    tot = st.get("pending", 0) + st.get("sent", 0) + st.get("rejected", 0)
    st["sent_rate"] = round(st.get("sent", 0) / tot, 3) if tot else None
    return st


# ------------------------------------------------------------------ remote
def remote_from_clone(path, max_fetch):
    r = dict(source="clone " + path, ok=os.path.isdir(path))
    if not r["ok"]:
        r["error"] = "clone path not found"
        return r
    inbox = md_files(os.path.join(path, "inbox"))
    proc_all = md_files(os.path.join(path, "processed"))
    rej_dir = os.path.join(path, "processed", "rejected")
    rej = md_files(rej_dir)
    acc = [p for p in proc_all if not os.path.abspath(p).startswith(os.path.abspath(rej_dir) + os.sep)]
    r.update(inbox=len(inbox), processed_accepted=len(acc), processed_rejected=len(rej))
    topics = collections.Counter()
    for p in inbox[:max_fetch]:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                t = front(f.read(4000)).get("topic")
        except OSError:
            continue
        if t:
            topics[t] += 1
    r["topics_waiting"] = dict(topics.most_common())
    lp = os.path.join(path, "CURATION-LOG.md")
    r["log_present"] = os.path.isfile(lp)
    if r["log_present"]:
        with open(lp, encoding="utf-8", errors="replace") as f:
            r["log"] = log_summary(parse_log(f.read()))
    return r


def gh_cmd():
    env = os.environ.get("LEARN_STATS_GH")
    if not env:
        return ["gh"]
    return [x[1:-1] if len(x) > 1 and x[0] == x[-1] == '"' else x for x in shlex.split(env, posix=(os.name != "nt"))]


def gh(args, timeout=60):
    p = subprocess.run(gh_cmd() + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout).strip()[:200] or "gh failed")
    return p.stdout


def remote_from_gh(repo, max_fetch):
    r = dict(source="gh api " + repo, ok=False)
    try:
        tree = json.loads(gh(["api", "repos/%s/git/trees/HEAD?recursive=1" % repo]))
    except Exception as e:
        r["error"] = "gh api failed: %s" % e
        return r
    paths = [e["path"] for e in tree.get("tree", []) if e.get("type") == "blob"]
    if tree.get("truncated"):
        r["warning"] = "tree listing truncated by GitHub; counts are lower bounds"
    mdp = lambda pre: [p for p in paths if p.startswith(pre) and p.endswith(".md")]
    inbox = mdp("inbox/")
    rej = mdp("processed/rejected/")
    acc = [p for p in mdp("processed/") if p not in rej]
    r.update(ok=True, inbox=len(inbox), processed_accepted=len(acc), processed_rejected=len(rej))
    topics = collections.Counter()
    for p in inbox[:max_fetch]:
        try:
            t = front(gh(["api", "-H", "Accept: application/vnd.github.raw", "repos/%s/contents/%s" % (repo, p)]))
            if t.get("topic"):
                topics[t["topic"]] += 1
        except Exception:
            pass
    r["topics_waiting"] = dict(topics.most_common())
    if "CURATION-LOG.md" in paths:
        try:
            r["log"] = log_summary(parse_log(gh(["api", "-H", "Accept: application/vnd.github.raw", "repos/%s/contents/CURATION-LOG.md" % repo])))
            r["log_present"] = True
        except Exception as e:
            r["warning"] = "CURATION-LOG.md unreadable: %s" % e
    else:
        r["log_present"] = False
    return r


# ------------------------------------------------------------------ report
def pct(x):
    return "n/a" if x is None else "%d%%" % round(100 * x)


def report_text(rep):
    L = ["Learning loop stats (%s)" % rep["date"]]
    lo = rep["local"]
    if lo["exists"]:
        L.append("Local queue %s: pending %d, sent %d, rejected %d, ready-to-send %d; sent share %s; oldest pending %s" % (
            lo["path"], lo["pending"], lo["sent"], lo["rejected"], lo["ready-to-send"], pct(lo["sent_rate"]),
            "%d days" % lo["oldest_pending_days"] if lo["oldest_pending_days"] is not None else "none"))
        if lo["topics"]:
            L.append("  local notes per topic: " + ", ".join("%s %d" % kv for kv in list(lo["topics"].items())[:8]))
    else:
        L.append("Local queue %s: not present (no note was ever recorded on this machine)" % lo["path"])
    rm = rep.get("remote")
    if rm is None:
        L.append("Inbox repo: skipped (--offline)")
    elif not rm.get("ok"):
        L.append("Inbox repo (%s): unavailable: %s" % (rm["source"], rm.get("error")))
    else:
        L.append("Inbox repo (%s): waiting for curation %d, processed %d accepted + %d rejected" % (rm["source"], rm["inbox"], rm["processed_accepted"], rm["processed_rejected"]))
        lg = rm.get("log")
        if lg:
            L.append("  CURATION-LOG: %d decisions: accept %d, merge %d, duplicate %d, reject %d; accepted rate %s, rejected rate %s (accepted:rejected %s)" % (
                lg["decisions"], lg["accept"], lg["merge"], lg["duplicate"], lg["reject"], pct(lg["accepted_rate"]), pct(lg["rejected_rate"]), lg["accepted_to_rejected"]))
            if lg["reject_codes"]:
                L.append("  rejection rule codes: " + ", ".join("%s %d" % kv for kv in list(lg["reject_codes"].items())[:8]))
            if lg["topics_accepted"]:
                L.append("  accepted notes per topic: " + ", ".join("%s %d" % kv for kv in list(lg["topics_accepted"].items())[:10]))
        elif rm.get("log_present") is False:
            L.append("  CURATION-LOG.md not found")
        if rm.get("topics_waiting"):
            L.append("  waiting notes per topic: " + ", ".join("%s %d" % kv for kv in list(rm["topics_waiting"].items())[:10]))
        if rm.get("warning"):
            L.append("  warning: " + rm["warning"])
    L += ["Reading: " + rep["reading"]]
    return "\n".join(L) + "\n"


def reading(rep):
    lo, rm = rep["local"], rep.get("remote") or {}
    pts = []
    total_remote = (rm.get("processed_accepted", 0) + rm.get("processed_rejected", 0) + rm.get("inbox", 0)) if rm.get("ok") else None
    if total_remote == 0:
        pts.append("the inbox has never received a note")
    elif total_remote is not None:
        pts.append("%d note(s) ever reached the inbox" % total_remote)
    if lo["exists"] and lo["pending"]:
        pts.append("%d local note(s) are stuck in pending (flush/pr not done)" % lo["pending"])
    if rm.get("ok") and rm.get("inbox"):
        pts.append("%d note(s) wait for the owner's curation run" % rm["inbox"])
    return "; ".join(pts) or "no data"


HIST = ["date", "local_pending", "local_sent", "local_rejected", "inbox", "processed_accepted", "processed_rejected", "decisions", "accepted_rate", "rejected_rate"]


def append_history(path, rep):
    lo, rm = rep["local"], rep.get("remote") or {}
    lg = rm.get("log") or {}
    row = dict(date=rep["date"], local_pending=lo.get("pending", ""), local_sent=lo.get("sent", ""), local_rejected=lo.get("rejected", ""), inbox=rm.get("inbox", ""),
               processed_accepted=rm.get("processed_accepted", ""), processed_rejected=rm.get("processed_rejected", ""), decisions=lg.get("decisions", ""),
               accepted_rate=lg.get("accepted_rate", ""), rejected_rate=lg.get("rejected_rate", ""))
    new = not os.path.isfile(path)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HIST, lineterminator="\n")
        if new:
            w.writeheader()
        w.writerow(row)


def build(queue=None, clone=None, repo=None, offline=False, max_fetch=100):
    rep = dict(kind="learn-stats", date=datetime.date.today().isoformat(), local=local_stats(queue_dir(queue)))
    if offline:
        rep["remote"] = None
    elif clone:
        rep["remote"] = remote_from_clone(clone, max_fetch)
    else:
        rep["remote"] = remote_from_gh(repo or DEFAULT_REPO, max_fetch)
    rep["reading"] = reading(rep)
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(prog="learn_stats.py", description=__doc__.split("\n")[0])
    ap.add_argument("--queue"); ap.add_argument("--clone"); ap.add_argument("--repo"); ap.add_argument("--offline", action="store_true")
    ap.add_argument("--json", action="store_true"); ap.add_argument("--history"); ap.add_argument("--max-fetch", type=int, default=100)
    a = ap.parse_args(argv)
    rep = build(a.queue, a.clone, a.repo, a.offline, a.max_fetch)
    if a.json:
        json.dump(rep, sys.stdout, indent=1)
        print()
    else:
        sys.stdout.write(report_text(rep))
    if a.history:
        append_history(a.history, rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
