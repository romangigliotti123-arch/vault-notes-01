#!/usr/bin/env python3
"""make_checklist.py - turn a tailored checklist JSON into a self-contained, phone-friendly interactive HTML checklist (and a markdown copy).

  python make_checklist.py items.json out.html [--md out.md]

items.json:
{
  "game": "Obby Kingdom", "launch_date": "2026-11-20", "stage": "pre-launch", "note": "optional one-liner",
  "items": [
    {"phase": "1. Packaging", "text": "Upload 3 thumbnails at 1920x1080", "priority": "must|should|could",
     "due": "T-14", "owner": "the user", "why": "short reason", "source": "https://youtu.be/...?t=12", "flag": "official|indie|mixed|devforum"}
  ]
}
Checkbox state, a progress bar and a hide-done filter persist in the browser (localStorage, wrapped in try/catch). No external requests.
"""
import argparse
import html
import json
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--bg:#f6f7fb;--card:#fff;--ink:#14161f;--mut:#5b6072;--line:#e3e6ef;--acc:#2f6bff;--ok:#1a9d5c;--must:#d6336c;--should:#e8890c;--could:#6b7280}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0f1117;--card:#181b25;--ink:#eceef5;--mut:#9aa0b4;--line:#2a2e3d;--acc:#6c93ff;--ok:#3ccf86;--must:#ff6b9d;--should:#ffb04a;--could:#98a2b3}}
:root[data-theme="dark"]{--bg:#0f1117;--card:#181b25;--ink:#eceef5;--mut:#9aa0b4;--line:#2a2e3d;--acc:#6c93ff;--ok:#3ccf86;--must:#ff6b9d;--should:#ffb04a;--could:#98a2b3}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:16px}
h1{font-size:1.35rem;margin:.2rem 0}.sub{color:var(--mut);font-size:.9rem;margin-bottom:12px}
.bar{position:sticky;top:0;background:var(--bg);padding:10px 0;z-index:2;border-bottom:1px solid var(--line)}
.prog{height:10px;background:var(--line);border-radius:6px;overflow:hidden}.prog i{display:block;height:100%;width:0;background:var(--ok);transition:width .2s}
.stats{display:flex;justify-content:space-between;font-size:.85rem;color:var(--mut);margin-top:6px;gap:8px;flex-wrap:wrap}
button,select{font:inherit;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:6px 10px}
details{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:12px 0;overflow:hidden}
summary{cursor:pointer;padding:12px 14px;font-weight:600;display:flex;justify-content:space-between;gap:8px}
summary span.c{color:var(--mut);font-weight:400;font-size:.85rem}
.it{display:flex;gap:10px;padding:10px 14px;border-top:1px solid var(--line);align-items:flex-start}
.it input{width:22px;height:22px;margin-top:2px;flex:none;accent-color:var(--acc)}
.it.done .t{text-decoration:line-through;color:var(--mut)}
.t{flex:1;min-width:0}.meta{font-size:.78rem;color:var(--mut);margin-top:3px;display:flex;gap:8px;flex-wrap:wrap}
.tag{border-radius:999px;padding:0 8px;border:1px solid currentColor;font-size:.72rem}
.tag.must{color:var(--must)}.tag.should{color:var(--should)}.tag.could{color:var(--could)}
a{color:var(--acc)}.why{font-size:.85rem;color:var(--mut)}
.hide{display:none}
@media print{.bar button,.bar select{display:none}details{break-inside:avoid}}
</style></head><body><div class="wrap">
<h1>__TITLE__</h1><div class="sub">__SUB__</div>
<div class="bar"><div class="prog"><i id="pb"></i></div>
<div class="stats"><span id="st">0 / 0 done</span><span><label><input type="checkbox" id="hd"> hide done</label> <select id="pf"><option value="">all priorities</option><option>must</option><option>should</option><option>could</option></select> <button id="rs">reset</button></span></div></div>
<div id="list"></div>
<p class="sub">Generated from the Roblox knowledge base. Flags: official = Roblox docs/sessions; indie = creator self-reported. Verify live Creator Hub settings before relying on any number.</p>
</div>
<script>
var DATA=__DATA__;
var KEY="rbxchk:"+DATA.game+":"+(DATA.launch_date||"");
var st={};try{st=JSON.parse(localStorage.getItem(KEY)||"{}")}catch(e){st={}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(st))}catch(e){}}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function render(){
 var list=document.getElementById("list");list.innerHTML="";
 var phases={},order=[];DATA.items.forEach(function(it,i){it._i=i;if(!phases[it.phase]){phases[it.phase]=[];order.push(it.phase)}phases[it.phase].push(it)});
 order.forEach(function(p){
  var its=phases[p],done=its.filter(function(x){return st[x._i]}).length;
  var d=document.createElement("details");d.open=done<its.length;
  var h='<summary>'+esc(p)+'<span class="c">'+done+' / '+its.length+'</span></summary>';
  its.forEach(function(it){
   var pr=it.priority||"should";
   h+='<label class="it'+(st[it._i]?' done':'')+'" data-p="'+esc(pr)+'"><input type="checkbox" data-i="'+it._i+'"'+(st[it._i]?' checked':'')+'><div class="t">'+esc(it.text)+
   '<div class="meta"><span class="tag '+esc(pr)+'">'+esc(pr)+'</span>'+(it.due?'<span>due '+esc(it.due)+'</span>':'')+(it.owner?'<span>'+esc(it.owner)+'</span>':'')+
   (it.flag?'<span>'+esc(it.flag)+'</span>':'')+(it.source?'<a href="'+esc(it.source)+'" target="_blank" rel="noopener">source</a>':'')+'</div>'+
   (it.why?'<div class="why">'+esc(it.why)+'</div>':'')+'</div></label>';
  });
  d.innerHTML=h;list.appendChild(d);
 });
 var tot=DATA.items.length,dn=DATA.items.filter(function(x){return st[x._i]}).length;
 document.getElementById("pb").style.width=(tot?100*dn/tot:0)+"%";
 document.getElementById("st").textContent=dn+" / "+tot+" done ("+(tot?Math.round(100*dn/tot):0)+"%)";
 filt();
}
function filt(){
 var hide=document.getElementById("hd").checked,pf=document.getElementById("pf").value;
 document.querySelectorAll(".it").forEach(function(el){
  var cb=el.querySelector("input"),off=(hide&&cb.checked)||(pf&&el.getAttribute("data-p")!==pf);
  el.classList.toggle("hide",!!off);
 });
}
document.addEventListener("change",function(e){
 var t=e.target;if(t.matches&&t.matches("input[data-i]")){st[t.getAttribute("data-i")]=t.checked;save();render()}
 else if(t.id==="hd"||t.id==="pf"){filt()}
});
document.getElementById("rs").onclick=function(){if(confirm("Clear all ticks?")){st={};save();render()}};
render();
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("json_in")
    ap.add_argument("html_out")
    ap.add_argument("--md")
    a = ap.parse_args()
    d = json.load(open(a.json_in, encoding="utf-8"))
    d.setdefault("items", [])
    title = "%s: launch checklist" % d.get("game", "Roblox game")
    sub = " | ".join(x for x in [("Launch " + d["launch_date"]) if d.get("launch_date") else "", d.get("stage", ""), d.get("note", ""), "%d items" % len(d["items"])] if x)
    data = json.dumps(d, ensure_ascii=False).replace("</", "<\\/")
    with open(a.html_out, "w", encoding="utf-8", newline="\n") as f:
        f.write(PAGE.replace("__TITLE__", html.escape(title)).replace("__SUB__", html.escape(sub)).replace("__DATA__", data))
    print("wrote", a.html_out, len(d["items"]), "items")
    if a.md:
        out = ["# " + title, "", sub, ""]
        cur = None
        for it in d["items"]:
            if it.get("phase") != cur:
                cur = it.get("phase")
                out += ["", "## " + str(cur), ""]
            bits = [it.get("priority", ""), ("due " + it["due"]) if it.get("due") else "", it.get("owner", ""), it.get("flag", "")]
            line = "- [ ] %s (%s)" % (it["text"], ", ".join(b for b in bits if b))
            if it.get("source"):
                line += " [source](%s)" % it["source"]
            out.append(line)
        open(a.md, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
        print("wrote", a.md)


if __name__ == "__main__":
    main()
