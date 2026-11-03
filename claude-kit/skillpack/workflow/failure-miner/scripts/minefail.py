#!/usr/bin/env python3
"""minefail.py - count the most repeated tool failures in Claude Code session transcripts. Stdlib only, read-only.

  python minefail.py <session.jsonl | folder> [more ...] [--top 10] [--last 20]
  python minefail.py --selftest

Reads the plaintext transcripts Claude Code keeps (~/.claude/projects/<project>/<session>.jsonl; folders are scanned for *.jsonl,
newest --last files). A failure is a tool_result block with is_error true; its signature is the tool name plus the first line of the
error with numbers, paths and quoted strings normalised, so "same mistake, different file" counts as one. Prints count, tool,
signature, model(s) seen. Transcripts can hold secrets: the output is truncated to 110 chars per line and nothing is copied anywhere.
"""
import argparse
import collections
import glob
import json
import os
import re
import sys
import tempfile


def sig(text):
    lines = [x.strip() for x in (text or "").strip().splitlines() if x.strip()]
    lines = [x for x in lines if not re.match(r"exit code \d+$", x, re.I)] or lines
    t = lines[0] if lines else ""
    t = re.sub(r"[A-Za-z]:[\\/][^\s'\"]+|/[\w.\-/]+", "<path>", t)
    t = re.sub(r"'[^']*'|\"[^\"]*\"", "<str>", t)
    t = re.sub(r"\d+", "N", t)
    return t[:110]


def flat(content):
    if isinstance(content, str):
        return content
    return " ".join(b.get("text", "") for b in content if isinstance(b, dict))


def mine(paths):
    names, models = {}, collections.defaultdict(set)
    cnt = collections.Counter()
    for p in paths:
        with open(p, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                m = d.get("message") if isinstance(d, dict) else None
                if not isinstance(m, dict) or not isinstance(m.get("content"), list):
                    continue
                for b in m["content"]:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "tool_use":
                        names[b.get("id")] = (b.get("name") or "?", m.get("model") or "")
                    elif b.get("type") == "tool_result" and b.get("is_error"):
                        tool, model = names.get(b.get("tool_use_id"), ("?", ""))
                        key = (tool, sig(flat(b.get("content"))))
                        cnt[key] += 1
                        if model:
                            models[key].add(model)
    return cnt, models


def collect(args, last):
    files = []
    for a in args:
        if os.path.isdir(a):
            files += sorted(glob.glob(os.path.join(a, "*.jsonl")), key=os.path.getmtime, reverse=True)[:last]
        else:
            files.append(a)
    return files


def selftest():
    rows = [
        {"message": {"model": "m1", "content": [{"type": "tool_use", "id": "a", "name": "Bash"}]}},
        {"message": {"content": [{"type": "tool_result", "tool_use_id": "a", "is_error": True, "content": "rg: C:\\x\\y.lua: line 12 bad"}]}},
        {"message": {"model": "m1", "content": [{"type": "tool_use", "id": "b", "name": "Bash"}]}},
        {"message": {"content": [{"type": "tool_result", "tool_use_id": "b", "is_error": True, "content": [{"type": "text", "text": "rg: D:\\z\\q.lua: line 99 bad"}]}]}},
        {"message": {"content": [{"type": "tool_result", "tool_use_id": "b", "is_error": False, "content": "ok"}]}},
    ]
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "s.jsonl")
        with open(p, "w", encoding="utf-8") as f:
            f.write("\n".join(json.dumps(r) for r in rows) + "\nnot json\n")
        cnt, models = mine([p])
    assert len(cnt) == 1 and list(cnt.values()) == [2], cnt
    (key,) = cnt
    assert key[0] == "Bash" and "<path>" in key[1] and "N" in key[1], key
    assert models[key] == {"m1"}
    print("selftest ok (3 cases)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--last", type=int, default=20)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    files = collect(a.paths, a.last)
    if not files:
        print("no transcripts given")
        return 1
    cnt, models = mine(files)
    print("files %d, distinct failures %d, total %d" % (len(files), len(cnt), sum(cnt.values())))
    for (tool, s), n in cnt.most_common(a.top):
        print("%4d  %-10s %s  [%s]" % (n, tool, s, ",".join(sorted(models[(tool, s)]))[:40]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
