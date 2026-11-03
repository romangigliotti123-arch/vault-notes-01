#!/usr/bin/env python3
"""moddoc.py - draft API docs for a Luau ModuleScript from its source. Stdlib only.

  python moddoc.py src/shared/Util.luau [--fail-undocumented]
  python moddoc.py --selftest

Extracts: the module name (file stem), `export type` first lines (a multi-line type shows only its first line), and public functions `function M.name(args): ret` /
`function M:name(args)` / `M.name = function(...)`. A function counts as documented when the line above it is a `---` doc
comment (or a `--` comment block). Output is a markdown skeleton: Purpose (to fill by a human from the code), API table with
signatures and the doc line, and a list of UNDOCUMENTED functions. The tool never invents behaviour: a function without a
doc comment gets "(undocumented)". Private functions (leading underscore or `local function`) are skipped.
Exit 0; with --fail-undocumented exit 1 if any public function lacks a doc comment.
"""
import os
import re
import sys

FUNC = re.compile(r"^function\s+([A-Za-z_][\w]*)([.:])([A-Za-z][\w]*)\s*\(([^)]*)\)\s*(?::\s*([^\n]+))?")
ASSIGN = re.compile(r"^([A-Za-z_][\w]*)\.([A-Za-z][\w]*)\s*=\s*function\s*\(([^)]*)\)\s*(?::\s*([^\n]+))?")
TYPE = re.compile(r"^export type\s+(.+)$")


def parse(src):
    lines = src.splitlines()
    funcs, types = [], []
    for i, ln in enumerate(lines):
        m = FUNC.match(ln)
        a = ASSIGN.match(ln)
        t = TYPE.match(ln)
        if t:
            types.append(t.group(1).strip())
        if not (m or a):
            continue
        if m:
            name, sep, args, ret = m.group(3), m.group(2), m.group(4), (m.group(5) or "").strip()
        else:
            name, sep, args, ret = a.group(2), ".", a.group(3), (a.group(4) or "").strip()
        j, doc = i - 1, []
        while j >= 0 and lines[j].strip().startswith("--"):
            doc.insert(0, lines[j].strip().lstrip("-").strip())
            j -= 1
        funcs.append(dict(name=name, sep=sep, sig="%s%s(%s)%s" % (sep, name, args.strip(), (": " + ret) if ret else ""), doc=" ".join(d for d in doc if d)))
    return types, funcs


def render(stem, types, funcs):
    out = ["# " + stem, "", "## Purpose", "(write one sentence from the code; this tool does not guess)", ""]
    if types:
        out += ["## Types"] + ["- `export type %s`" % t for t in types] + [""]
    out += ["## API", "", "| Function | What it does |", "|---|---|"]
    for f in funcs:
        out.append("| `%s` | %s |" % (f["sig"], f["doc"] or "(undocumented)"))
    und = [f["name"] for f in funcs if not f["doc"]]
    out += ["", "## Example", "(add a 3-line usage taken from a real caller)", "", "## Undocumented", ", ".join(und) if und else "none"]
    return "\n".join(out) + "\n", und


SAMPLE = """--!strict
export type Item = { id: string, count: number }
local M = {}
local function helper() end
--- Adds n to the stack.
function M.add(item: Item, n: number): Item
	return item
end
function M:reset()
end
M.clamp = function(x: number): number
	return x
end
return M
"""


def selftest():
    types, funcs = parse(SAMPLE)
    assert types == ["Item = { id: string, count: number }"], types
    assert [f["name"] for f in funcs] == ["add", "reset", "clamp"], funcs
    assert funcs[0]["doc"] == "Adds n to the stack." and funcs[0]["sig"] == ".add(item: Item, n: number): Item"
    assert funcs[1]["sig"] == ":reset()" and funcs[1]["doc"] == ""
    text, und = render("Inv", types, funcs)
    assert und == ["reset", "clamp"] and "(undocumented)" in text and "| `.add(" in text
    print("selftest ok (5 cases)")
    return 0


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if not argv:
        print(__doc__)
        return 1
    path = argv[0]
    types, funcs = parse(open(path, encoding="utf-8").read())
    text, und = render(os.path.splitext(os.path.splitext(os.path.basename(path))[0])[0], types, funcs)
    sys.stdout.write(text)
    return 1 if (und and "--fail-undocumented" in argv) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
