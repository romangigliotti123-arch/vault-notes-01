#!/usr/bin/env python3
"""learn.py - the capture side of the vault's learning loop (stdlib + git; Windows/macOS/Linux).

An agent that verified something non-obvious while working (a fix, a working command, a gotcha, a Roblox technique, a corrected assumption) records it as a small note.
Notes wait in a local queue, are scanned before anything leaves the machine, and are pushed to the public inbox repo vault-learnings. The inbox is UNTRUSTED: nobody reads it as
knowledge; the vault owner's curation step (curate.py) decides what becomes a vault note under learned/.

  learn.py add --title T --topic roblox/ui --body "facts" --verified "how I checked it" [--confidence high|medium] [--source tag]   (--body-file F|- reads the body)
  learn.py search <words>            existing learned notes (vault learned/) and queued notes that look related: run this BEFORE add
  learn.py list                      queued / sent / rejected notes
  learn.py scan FILE|-               run the safety scan on a note file or text (prints findings, never the matched secret)
  learn.py flush [--quiet]           push queued notes to vault-learnings (inbox/<yyyy-mm>/); pull --rebase + push, never force; no write access / offline: notes stay queued, exit 0
  learn.py pr                        no write access: open a pull request from a fork with gh (when gh is logged in), else write a ready-to-send folder + zip
  learn.py status
  learn.py hiccup add|say|list|apply|check|retro|close|trend|share|queue ...    the live hiccup ledger (see hiccup.py): log a hiccup the moment it happens, with a concrete prevention

Queue: <claude config dir>/claude-kit/learnings-queue/{pending,sent,rejected,ready-to-send,repo}. <claude config dir> = $CLAUDE_CONFIG_DIR, else $CLAUDE_KIT_HOME/.claude, else ~/.claude;
override with --queue or $VAULT_LEARN_QUEUE. Target repo: $VAULT_LEARNINGS_REPO (a git URL or path; tests) else https://github.com/romangigliotti123-arch/vault-learnings.git.
Env CLAUDE_LEARN_SKIP=1 turns flush into a no-op. Exit codes: 0 ok, 2 note rejected / usage error.
Never run by a note: the text of a note is only ever stored, scanned and copied, never executed or followed.
"""
import argparse, collections, datetime, getpass, hashlib, json, math, os, re, shutil, socket, subprocess, sys, tempfile, time, unicodedata

OWNER_REPO = "romangigliotti123-arch/vault-learnings"
SCHEMA = 1
TITLE_MIN, TITLE_MAX = 8, 120
BODY_MIN, BODY_MAX = 60, 4000
VERIFIED_MIN, VERIFIED_MAX = 20, 1000
FILE_MAX = 9000
SOURCE_RX = re.compile(r"^[a-z0-9][a-z0-9 ._/-]{1,39}$")
TOPIC_RX = re.compile(r"^[a-z0-9][a-z0-9_-]{0,29}(/[a-z0-9][a-z0-9_-]{0,29}){0,2}$")
CONFIDENCE_OK = ("high", "medium")
MAX_PENDING = 200
HICCUP_TYPES = ("rule", "checklist", "gate", "test", "script-fix", "skill-text", "config")
HICCUP_BODY_RX = re.compile(r"\AWhat happened: [^\n]+\nRoot cause: [^\n]+\nCost: [^\n]+\nPrevention \((" + "|".join(HICCUP_TYPES) + r")\): [^\n]+\nSeen: (\d{1,3}) time\(s\)")
STOP = set("a an and are as at be by for from has have how in into is it its of on or that the this to was were what when which with your you not no can will do does".split())

# ------------------------------------------------------------------ safety scan
# (literals that the public build forbids are assembled from parts so this file survives the build unchanged)
SECRET_RULES = [
    ("github-token", r"\bgh[pousr]" + r"_[A-Za-z0-9]{20,}"),
    ("github-pat", r"\bgithub" + r"_pat_[A-Za-z0-9_]{20,}"),
    ("anthropic-key", r"\bsk-" + r"ant-[A-Za-z0-9_-]{10,}"),
    ("openai-style-key", r"\bsk-(?:proj-)?[A-Za-z0-9]{32,}"),
    ("aws-key", r"\bAK" + r"IA[0-9A-Z]{16}\b"),
    ("google-key", r"\bAI" + r"za[0-9A-Za-z_-]{35}"),
    ("private-key-block", r"-----BEGIN [A-Z ]*PRIV" + r"ATE KEY"),
    ("slack-token", r"\bxox[abprs]-[A-Za-z0-9-]{10,}"),
    ("slack-webhook", r"hooks\.slack" + r"\.com/services/"),
    ("discord-webhook", r"discord(?:app)?\.com/api/webhooks/"),
    ("jwt", r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}"),
    ("bearer-token", r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{20,}"),
    ("credential-assignment", r"(?i)\b(?:password|passwd|secret|api[_-]?key|apikey|auth[_-]?token)\b[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9_\-+/=.]{12,}"),
    ("url-credentials", r"(?i)\bhttps?://[^\s/@:]+:[^\s/@]+@"),
    ("forbidden-token-word", r"(?i)\b(?:access|refresh)" + r"_token\b"),     # the public build refuses this literal: rephrase
]
SECRET_RX = [(n, re.compile(p)) for n, p in SECRET_RULES]
B64_RX = re.compile(r"[A-Za-z0-9+/_-]{32,}={0,2}")
HEX_RX = re.compile(r"^[0-9a-fA-F]+$")

# prompt-injection / unsafe-instruction rules: (code, regex, weight). weight 9 = hard reject; weights below add up, 2 or more rejects.
INJ = [
    ("override-instructions", r"(?i)\b(?:ignore|disregard|forget|override|bypass|discard)\b[^.\n]{0,40}\b(?:previous|prior|above|earlier|preceding|all|any|your|the|these)\b[^.\n]{0,30}\b(?:instruction|prompt|rule|guideline|direction|polic|constraint|restriction)", 9),
    ("new-instructions", r"(?i)\b(?:new|updated|real|actual|hidden|secret) (?:system )?(?:instruction|prompt|directive|rule)s?\b\s*[:\-]", 9),
    ("system-prompt", r"(?i)\b(?:system|developer) (?:prompt|message)\b", 9),
    ("role-hijack", r"(?i)\byou are (?:now|no longer)\b|\bpretend (?:to be|you)\b|\bfrom now on\b|\bjailbreak|\bDAN mode\b|\bact as (?:an? )?(?:unrestricted|different|new)\b", 9),
    ("chat-markers", r"(?im)^\s*(?:system|assistant|user|human|ai)\s*:|<\|(?:im_start|im_end|system|user|assistant)\|>|\[/?INST\]|^#{1,4}\s*(?:system|instruction)s?\b", 9),
    ("addressed-to-agent", r"(?i)\b(?:dear|hey|hello|attention|note to|message to|instructions? for|attn)[:,]?\s+(?:the\s+)?(?:ai|a\.i\.|agents?|assistants?|claude|llms?|models?|bots?)\b|\bAI READER\b|\bif you are an? (?:ai|llm|assistant|agent|language model)\b", 9),
    ("agent-must", r"(?i)\b(?:ai|llm|assistant|claude|language model|agent)s?\s+(?:must|should|shall|needs? to|has to|have to|will|is required to)\b", 9),
    ("conceal-from-user", r"(?i)\b(?:do not|don't|never|without)\s+(?:tell|tell(?:ing)?|inform|mention|show|notify|alert|warn|ask)\w*\b[^.\n]{0,25}\b(?:user|human|owner|operator|roman|them)\b|\bsecretly\b|\bsilently\s+(?:run|send|install|upload|execute|delete|write|modify)\b|\bwithout\s+(?:asking|confirmation|consent|permission|telling)\b", 9),
    ("exfiltration", r"(?i)\b(?:send|post|upload|exfiltrate|forward|email|leak|transmit|reveal)\b[^.\n]{0,60}\b(?:credential|secret|token|password|api[ _-]?key|ssh|private key|cookies?|\.env|keychain|id_rsa|id_ed25519|environment variables?)", 9),
    ("pipe-to-shell", r"(?i)\b(?:curl|wget|iwr|irm|invoke-webrequest|invoke-restmethod|fetch)\b[^\n]{0,200}\|\s*(?:sudo\s+)?(?:sh|bash|zsh|python\d?|pwsh|powershell|iex|invoke-expression|node|perl|ruby)\b", 9),
    ("eval-exec", r"(?i)\b(?:iex|invoke-expression)\b|\beval\s*\(|\bexec\s*\(\s*(?:base64|urllib|requests)|(?:powershell|pwsh)[^\n]{0,60}\s-(?:enc|encodedcommand|e)\s|base64\s+(?:-d|--decode)|frombase64string|\bos\.system\s*\(|\bsubprocess\.", 9),
    ("destructive-command", r"(?i)\brm\s+-[a-z]*r[a-z]*f?\s|\brm\s+-rf\b|remove-item\b[^\n]{0,60}-recurse|\bformat-volume\b|\bdel\s+/[sq]\b|\bmkfs\b|\bdd\s+if=|\bshutdown\s+[/-]|:\(\)\s*\{|\bchmod\s+(?:-r\s+)?[0-7]*777\b|\bgit\s+push\s+[^\n]{0,30}--force|\bgit\s+reset\s+--hard|\bsudo\b", 9),
    ("reverse-shell", r"(?i)\bnc\s+-[a-z]*e\b|/dev/tcp/|\bbash\s+-i\b|\bsocat\b[^\n]{0,40}exec|\bncat\b", 9),
    ("fetch-instruction", r"(?i)\b(?:download|fetch|curl|wget|clone|install from|pip install|npm install|npm i|git clone)\b[^.\n]{0,80}https?://", 9),
    ("persistence", r"(?i)\b(?:add|append|write|put|insert|modify|edit|change|update|create|register|set up|schedule)\b[^.\n]{0,50}(?:CLAUDE\.md|settings(?:\.local)?\.json|\.bashrc|\.zshrc|\.profile|crontab|authorized_keys|startup folder|scheduled task|schtasks|launchd|systemd|hooks?\b)", 9),
    ("remote-image-or-link-trick", r"!\[[^\]]*\]\(\s*(?:https?:|data:|//)|\]\(\s*(?:javascript:|data:|vbscript:|file:)|\bdata:[a-z]+/[a-z0-9.+-]+;base64", 9),
    ("hidden-html", r"(?is)<!--|<\s*/?\s*(?:script|iframe|object|embed|img|style|link|meta|form|input|svg|a|div|span|details|summary|base|video|audio|source|button|textarea|template|noscript)\b[^>]*>", 9),
    ("shortener-or-ip-url", r"(?i)https?://(?:bit\.ly|tinyurl\.com|t\.co|goo\.gl|is\.gd|cutt\.ly|rb\.gy|ow\.ly|\d{1,3}(?:\.\d{1,3}){3})\b", 9),
    ("encoded-blob", r"[A-Za-z0-9+/]{80,}={0,2}|\b[0-9a-fA-F]{96,}\b", 9),
    ("second-person-command", r"(?i)\byou (?:must|have to|need to|are required to|shall)\b", 1),
    ("always-never-directive", r"(?im)^\s*(?:[-*]\s*)?(?:always|never)\s+(?:use|run|do|call|trust|follow|obey|execute|write|send|open|ask|answer)\b", 1),
    ("urgency-marker", r"(?i)\b(?:important|critical|urgent|mandatory|required)\s*[:!]|\bmust (?:be )?(?:followed|obeyed)\b|\bobey\b|\bcomply\b|\bfollow (?:these|the following) (?:steps|instructions|commands)\b", 1),
    ("trust-me", r"(?i)\b(?:trust (?:this|me)|highest priority|takes? precedence|overrides?)\b", 1),
    ("run-this", r"(?im)^\s*(?:[-*]\s*)?(?:run|execute|paste|enter|type|launch)\b[^\n]{0,40}\b(?:this|following|below|these)\b", 1),
]
INJ_RX = [(c, re.compile(p), w) for c, p, w in INJ]
HTML_ALLOWED_NOTE = "inline code and fenced code are scanned too: a note must not smuggle instructions in code"


INVISIBLE = set("\u034f\u115f\u1160\u17b4\u17b5\u180b\u180c\u180d\u180e\u2800\u3164\uffa0") | {chr(c) for c in range(0xFE00, 0xFE10)} | {chr(c) for c in range(0xE0100, 0xE01F0)}
LOOKALIKE_SCRIPTS = ("CYRILLIC", "GREEK", "ARMENIAN", "CHEROKEE", "COPTIC", "LISU")


def hidden_chars(text):
    bad = collections.Counter()
    for ch in text:
        if ch in "\n\t\r":
            continue
        cat = unicodedata.category(ch)
        if cat in ("Cc", "Cf", "Co", "Cn", "Cs", "Zl", "Zp"):
            bad[cat] += 1
        elif ch in INVISIBLE:
            bad["invisible"] += 1
    return bad


def mixed_script_words(text):
    """words that mix Latin letters with look-alike letters of another script (Cyrillic a/e/o ... inside an English word) -> count"""
    n = 0
    for w in re.findall(r"\w+", text):
        if w.isascii():
            continue
        sc = set()
        for ch in w:
            if ch.isalpha():
                sc.add(unicodedata.name(ch, "?").split(" ")[0])
        if "LATIN" in sc and sc & set(LOOKALIKE_SCRIPTS):
            n += 1
    return n


def entropy(s):
    c = collections.Counter(s)
    n = float(len(s))
    return -sum(v / n * math.log(v / n, 2) for v in c.values())


def high_entropy_hits(text):
    hits = 0
    for m in B64_RX.finditer(text):
        s = m.group(0)
        if len(s) < 32 or HEX_RX.match(s) or "/" in s and s.count("/") > 2 and len(s) < 60:
            continue
        if re.search(r"[a-z]", s) and re.search(r"[A-Z]", s) and re.search(r"\d", s) and entropy(s) >= 4.2:
            hits += 1
    return hits


def _names_to_redact():
    out = set()
    for fn in (socket.gethostname, getpass.getuser):
        try:
            out.add(fn())
        except Exception:
            pass
    for k in ("COMPUTERNAME", "HOSTNAME", "USERNAME", "USER", "LOGNAME"):
        if os.environ.get(k):
            out.add(os.environ[k])
    skip = {"user", "users", "admin", "root", "administrator", "guest", "default", "pc", "home", "test", "localhost", "runner", "docker", "ubuntu", "claude"}
    try:
        out.add(os.path.basename(os.path.expanduser("~")))
    except Exception:
        pass
    return sorted({n.strip() for n in out if n and len(n.strip()) >= 3 and n.strip().lower() not in skip and re.match(r"^[\w.-]+( [\w.-]+)*$", n.strip())}, key=len, reverse=True)


RX_WINHOME = re.compile(r"(?i)[A-Z]:[\\/]+Users[\\/]+[^\\/\s\"'`<>|:*?)\]]+")
RX_UNIXHOME = re.compile(r"(?<![\w.])/(?:Users|home)/[A-Za-z0-9._-]+")
RX_UNC = re.compile(r"\\\\[A-Za-z0-9._-]+\\[A-Za-z0-9$._-]+")
RX_EMAIL = re.compile(r"(?<![\w.%+-])([A-Za-z0-9._%+-]+)@([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,})")
RX_IP = re.compile(r"(?<![\w.])(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})(?![\w]|\.\d)")


def sub_home(name, text, n):
    rx = re.compile(r"(?i)(?:[A-Z]:[\\/]+Users[\\/]+|(?<![\w.])/(?:Users|home)/)" + re.escape(name) + r"(?![\w-])")
    text, k = rx.subn("~", text)
    if k:
        n["home-path"] += k
    return text


def redact(text):
    """-> (text, Counter of what was replaced). Personal/machine details are replaced, never kept."""
    n = collections.Counter()
    for name in _names_to_redact():
        if " " in name:
            text = sub_home(name, text, n)

    def sub(rx, rep, t, key, fn=None):
        def r(m):
            if fn and not fn(m):
                return m.group(0)
            n[key] += 1
            return rep(m) if callable(rep) else rep
        return rx.sub(r, t)

    text = sub(RX_WINHOME, "~", text, "home-path")
    text = sub(RX_UNIXHOME, "~", text, "home-path")
    text = sub(RX_UNC, "[unc-path]", text, "unc-path")
    text = sub(RX_EMAIL, "[email]", text, "email", lambda m: m.group(1) != "git")

    def ip_ok(m):
        o = [int(x) for x in m.groups()]
        if any(x > 255 for x in o) or o[0] == 127 or o == [0, 0, 0, 0] or o[0] == 255 and o[1] == 255:
            return False
        return True
    text = sub(RX_IP, "[ip]", text, "ip", ip_ok)
    for name in _names_to_redact():
        text = sub(re.compile(r"(?i)(?<![\w-])" + re.escape(name) + r"(?![\w-])"), "[host]", text, "machine-or-user-name")
    return text, n


def scan_text(text):
    """-> dict(ok, rejects=[(code, hint)], text=<redacted text>, redactions=Counter). A reject means the note must not leave the machine."""
    rejects = []
    for code, rx in SECRET_RX:
        if rx.search(text):
            rejects.append((code, "looks like a secret/token or a literal the public build forbids; remove it or describe it in words"))
    if high_entropy_hits(text):
        rejects.append(("high-entropy-string", "a long random-looking string (key/token/hash blob); describe it in words instead"))
    hc = hidden_chars(text)
    if hc:
        rejects.append(("hidden-characters", "invisible/control/format characters (%s)" % ", ".join("%s x%d" % kv for kv in sorted(hc.items()))))
    if mixed_script_words(text):
        rejects.append(("mixed-script-word", "a word mixes Latin and look-alike letters of another script (Cyrillic/Greek); write plain text"))
    clean, red = redact(text)
    folded = unicodedata.normalize("NFKC", clean)
    score = 0
    for code, rx, w in INJ_RX:
        if rx.search(clean) or (folded != clean and rx.search(folded)):
            if w >= 9:
                rejects.append((code, "instruction-like or unsafe content"))
            else:
                score += w
    if score >= 2:
        rejects.append(("directive-wording", "second-person/imperative directives add up to %d (a note states facts; it does not give orders)" % score))
    return {"ok": not rejects, "rejects": rejects, "text": clean, "redactions": red}


# ------------------------------------------------------------------ note format
def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def tokens(s):
    return {w for w in re.findall(r"[a-z0-9]{2,}", s.lower()) if w not in STOP}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / float(len(a | b))


RESERVED = {"con", "prn", "aux", "nul"} | {"com%d" % i for i in range(1, 10)} | {"lpt%d" % i for i in range(1, 10)}


def slugify(title, n=60):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    s = s[:n].strip("-")
    if s in RESERVED:
        s += "-note"
    return s or "note"


def note_hash(title, body, verified):
    return hashlib.sha256((norm(title) + "\n" + norm(body) + "\n" + norm(verified)).encode("utf-8")).hexdigest()[:16]


def render_note(n):
    return ("---\nschema: %d\ntitle: %s\ntopic: %s\nconfidence: %s\nsource: %s\ncreated: %s\nhash: %s\n---\n\n%s\n\n## How verified\n\n%s\n"
            % (SCHEMA, n["title"], n["topic"], n["confidence"], n["source"], n["created"], n["hash"], n["body"].strip(), n["verified"].strip()))


FM_RX = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.S)
VER_RX = re.compile(r"(?im)^##[ \t]+How verified[ \t]*\n")


def parse_note(text):
    """strict parse of a note file -> dict or raises ValueError. Unknown front matter keys are ignored (never copied)."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if len(text.encode("utf-8", "replace")) > FILE_MAX:
        raise ValueError("file-too-large")
    m = FM_RX.match(text)
    if not m:
        raise ValueError("no-frontmatter")
    fm = {}
    for line in m.group(1).split("\n"):
        mm = re.match(r"^([a-z_]+):[ \t]*(.*)$", line)
        if mm and mm.group(1) not in fm:
            fm[mm.group(1)] = mm.group(2).strip()
    rest = text[m.end():].strip("\n")
    v = VER_RX.search(rest)
    if v:
        body, verified = rest[:v.start()].strip(), rest[v.end():].strip()
    else:
        body, verified = rest.strip(), ""
    n = {k: fm.get(k, "") for k in ("title", "topic", "confidence", "source", "created", "hash")}
    n["schema"] = fm.get("schema", "")
    n["body"], n["verified"] = body, verified
    return n


def validate_fields(n):
    """-> list of (code, hint) for the shape of a note (limits, formats). Content safety is scan_text."""
    out = []
    if not (TITLE_MIN <= len(n["title"]) <= TITLE_MAX) or "\n" in n["title"]:
        out.append(("title-length", "title must be %d-%d characters on one line" % (TITLE_MIN, TITLE_MAX)))
    if not TOPIC_RX.match(n["topic"]) or any(seg in RESERVED for seg in n["topic"].split("/")):
        out.append(("topic-format", "topic must be 1-3 lowercase segments like roblox/ui or windows/powershell"))
    if n["confidence"] not in CONFIDENCE_OK:
        out.append(("confidence", "confidence must be high or medium (guesses are not recorded)"))
    if not SOURCE_RX.match(n["source"]):
        out.append(("source-tag", "source must be a short generic tag like claude-code/windows (no names)"))
    if not (BODY_MIN <= len(n["body"]) <= BODY_MAX):
        out.append(("body-length", "body must be %d-%d characters" % (BODY_MIN, BODY_MAX)))
    if not (VERIFIED_MIN <= len(n["verified"]) <= VERIFIED_MAX):
        out.append(("verified-length", "'How verified' must be %d-%d characters: say what you ran or saw" % (VERIFIED_MIN, VERIFIED_MAX)))
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", n["created"]):
        out.append(("created-date", "created must be YYYY-MM-DD"))
    return out


def check_note(n):
    """full check of a parsed note -> (problems, cleaned note). Redaction is applied to title/body/verified; the hash is recomputed after it."""
    problems = validate_fields(n)
    whole = "\n".join([n["title"], n["topic"], n["source"], n["body"], n["verified"]])
    s = scan_text(whole)
    problems += s["rejects"]
    c = dict(n)
    if s["redactions"]:
        for k in ("title", "body", "verified", "source"):
            c[k] = redact(n[k])[0]
        if not SOURCE_RX.match(c["source"]):
            problems.append(("source-tag", "source tag had to be redacted; use a generic tag"))
    c["hash"] = note_hash(c["title"], c["body"], c["verified"])
    return problems, c, s["redactions"]


# ------------------------------------------------------------------ paths and config
def config_dir():
    if os.environ.get("CLAUDE_CONFIG_DIR"):
        return os.path.abspath(os.path.expanduser(os.environ["CLAUDE_CONFIG_DIR"]))
    if os.environ.get("CLAUDE_KIT_HOME"):
        return os.path.join(os.path.abspath(os.path.expanduser(os.environ["CLAUDE_KIT_HOME"])), ".claude")
    return os.path.join(os.path.expanduser("~"), ".claude")


def queue_dir(arg=None):
    q = arg or os.environ.get("VAULT_LEARN_QUEUE") or os.path.join(config_dir(), "claude-kit", "learnings-queue")
    return os.path.abspath(os.path.expanduser(q))


def sub(q, name):
    p = os.path.join(q, name)
    os.makedirs(p, exist_ok=True)
    return p


def target_repo():
    return os.environ.get("VAULT_LEARNINGS_REPO") or "https://github.com/%s.git" % OWNER_REPO


def find_vault():
    for c in (os.environ.get("CLAUDES_VAULT"), os.path.join(os.path.expanduser("~"), "Obsidian", "claudes-vault"), os.path.join(os.environ.get("USERPROFILE", ""), "Obsidian", "claudes-vault")):
        if c and os.path.isdir(c):
            return c
    return None


def read_notes(d):
    out = []
    if not os.path.isdir(d):
        return out
    for dp, dn, fn in os.walk(d):
        dn[:] = sorted(x for x in dn if not x.startswith("."))
        for f in sorted(fn):
            if f.endswith(".md"):
                p = os.path.join(dp, f)
                try:
                    with open(p, encoding="utf-8", errors="replace") as fh:
                        out.append((p, fh.read()))
                except OSError:
                    pass
    return out


def known_notes(q, vault=None):
    """titles/topics/hashes/body tokens of everything already queued, sent, or curated, for duplicate detection."""
    items = []
    for d in ("pending", "sent"):
        for p, t in read_notes(os.path.join(q, d)):
            try:
                n = parse_note(t)
            except ValueError:
                continue
            items.append({"where": d, "path": p, "title": n["title"], "topic": n["topic"], "hash": n["hash"], "hashes": {n["hash"]}, "tok": tokens(n["body"])})
    vault = vault or find_vault()
    if vault:
        for p, t in read_notes(os.path.join(vault, "learned")):
            m = FM_RX.match(t.replace("\r\n", "\n"))
            if not m:
                continue
            fm = dict((k, v.strip()) for k, v in re.findall(r"(?m)^([a-z_]+):[ \t]*(.*)$", m.group(1)))
            hs = set(re.findall(r"[0-9a-f]{16}", fm.get("hashes", "")))
            items.append({"where": "learned", "path": p, "title": fm.get("title", ""), "topic": fm.get("topic", ""), "hash": "", "hashes": hs, "tok": tokens(t[m.end():])})
    return items


def find_duplicate(n, items):
    for it in items:
        if n["hash"] in it["hashes"]:
            return it, "same content (hash)"
    tt, bt = tokens(n["title"]), tokens(n["body"])
    for it in items:
        if it["topic"] == n["topic"] and jaccard(tt, tokens(it["title"])) >= 0.75:
            return it, "near-duplicate title"
        if jaccard(bt, it["tok"]) >= 0.8:
            return it, "near-duplicate body"
    return None, ""


# ------------------------------------------------------------------ commands
def cmd_add(a):
    q = queue_dir(a.queue)
    body = a.body
    if a.body_file:
        body = sys.stdin.read() if a.body_file == "-" else open(a.body_file, encoding="utf-8").read()
    if body is None:
        print("learn: --body or --body-file is required", file=sys.stderr)
        return 2
    n = {"title": " ".join((a.title or "").split()), "topic": (a.topic or "").strip().lower(), "confidence": (a.confidence or "").strip().lower(),
         "source": (a.source or "claude-code").strip().lower(), "created": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
         "body": body.replace("\r\n", "\n").strip(), "verified": (a.verified or "").replace("\r\n", "\n").strip(), "schema": str(SCHEMA)}
    n["hash"] = note_hash(n["title"], n["body"], n["verified"])
    problems, c, red = check_note(n)
    if problems:
        print("learn: NOT recorded. Problems:", file=sys.stderr)
        for code, hint in problems:
            print("  - %s: %s" % (code, hint), file=sys.stderr)
        return 2
    pend = sub(q, "pending")
    if len(os.listdir(pend)) >= MAX_PENDING:
        print("learn: NOT recorded: %d notes already queued; run flush or pr first" % MAX_PENDING, file=sys.stderr)
        return 2
    dup, why = find_duplicate(c, known_notes(q, a.vault))
    if dup:
        print("learn: NOT recorded: %s of an existing %s note %r (%s). Record only what is new." % (why, dup["where"], dup["title"], dup["path"]), file=sys.stderr)
        return 2
    path = os.path.join(pend, "%s-%s.md" % (slugify(c["title"]), c["hash"][:8]))
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_note(c))
    if red:
        print("learn: redacted before saving: " + ", ".join("%s x%d" % kv for kv in sorted(red.items())))
    print("learn: queued %s" % path)
    return 0


def cmd_search(a):
    q = queue_dir(a.queue)
    want = tokens(" ".join(a.words))
    if not want:
        print("learn: give search words", file=sys.stderr)
        return 2
    rows = []
    for it in known_notes(q, a.vault):
        sc = len(want & (tokens(it["title"]) | it["tok"]))
        if sc:
            rows.append((sc, it))
    rows.sort(key=lambda r: -r[0])
    for sc, it in rows[:10]:
        print("%-8s %-24s %s  (%s)" % (it["where"], it["topic"], it["title"], it["path"]))
    if not rows:
        print("learn: nothing related found (queue, sent, vault learned/)")
    return 0


def cmd_list(a):
    q = queue_dir(a.queue)
    for d in ("pending", "sent", "rejected"):
        notes = read_notes(os.path.join(q, d))
        print("%s: %d" % (d, len(notes)))
        for p, t in notes[:50]:
            try:
                print("  - %s" % parse_note(t)["title"])
            except ValueError:
                print("  - (unreadable) %s" % os.path.basename(p))
    return 0


def cmd_scan(a):
    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8", errors="replace").read()
    try:
        n = parse_note(text)
        problems, c, red = check_note(n)
    except ValueError:
        s = scan_text(text)
        problems, red = s["rejects"], s["redactions"]
    for code, hint in problems:
        print("REJECT %s: %s" % (code, hint))
    if red:
        print("REDACT " + ", ".join("%s x%d" % kv for kv in sorted(red.items())))
    print("scan: %s" % ("clean" if not problems else "%d problem(s)" % len(problems)))
    return 0 if not problems else 2


def run(cmd, cwd=None, timeout=180, env=None):
    e = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never", GIT_ASKPASS="", SSH_ASKPASS="")
    e.update(env or {})
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, env=e, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError) as ex:
        return subprocess.CompletedProcess(cmd, 127, "", str(ex))


_GH = {}


def gh_login():
    """login of the gh CLI user or '' (gh missing / not logged in). Cached."""
    if "login" not in _GH:
        r = run(["gh", "api", "user", "--jq", ".login"], timeout=30)
        _GH["login"] = r.stdout.strip() if r.returncode == 0 else ""
    return _GH["login"]


def git_cmd(use_gh):
    base = ["git", "-c", "core.autocrlf=false", "-c", "core.longpaths=true", "-c", "user.name=rbx-learn", "-c", "user.email=rbx-learn" + "@users.noreply.github.com", "-c", "commit.gpgsign=false", "-c", "core.protectNTFS=false", "-c", "core.symlinks=false"]
    if use_gh:
        base += ["-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential"]
    return base


def pending_notes(q):
    """validated pending notes [(path, cleaned note)]; unsafe ones are moved to rejected/ with a .reason file."""
    out = []
    for p, t in read_notes(os.path.join(q, "pending")):
        try:
            n = parse_note(t)
            problems, c, red = check_note(n)
        except ValueError as ex:
            problems, c = [(str(ex), "unreadable note")], None
        if problems:
            rej = sub(q, "rejected")
            shutil.move(p, os.path.join(rej, os.path.basename(p)))
            with open(os.path.join(rej, os.path.basename(p) + ".reason"), "w", encoding="utf-8") as fh:
                fh.write("; ".join("%s: %s" % pr for pr in problems) + "\n")
            continue
        out.append((p, c))
    return out


def stage_files(work, notes):
    """copy notes into <work>/inbox/<yyyy-mm>/; returns relative paths added."""
    added = []
    for p, c in notes:
        rel = "inbox/%s/%s-%s.md" % (c["created"][:7], slugify(c["title"]), c["hash"][:8])
        dst = os.path.join(work, *rel.split("/"))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(render_note(c))
        added.append(rel)
    return added


def mark_sent(q, notes):
    sent = sub(q, "sent")
    for p, c in notes:
        if os.path.exists(p):
            shutil.move(p, os.path.join(sent, os.path.basename(p)))


SKIPPED_PATHS = []        # inbox paths of the last sync_clone that are not usable as files on Windows/macOS/Linux (never checked out)
WIN_BAD_CH = re.compile(r'[<>:"|?*\\\x00-\x1f]')


def unsafe_name(path):
    """True for a repository path that cannot be a plain file on Windows (reserved device names, trailing dot/space, forbidden characters, .git aliases) or is absurdly long"""
    if len(path) > 180:
        return True
    for seg in path.split("/"):
        if not seg or WIN_BAD_CH.search(seg) or seg[-1] in " ." or seg.split(".")[0].lower() in RESERVED or seg.lower() == ".git" or re.match(r"(?i)git~\d", seg):
            return True
    return False


def checkout_safe(work, g, rev):
    """check out `rev` in the staging clone but leave out the paths that unsafe_name rejects (a public inbox may contain them; they would make a plain checkout fail on Windows)"""
    del SKIPPED_PATHS[:]
    tr = run(g + ["ls-tree", "-r", "-z", "--name-only", rev], cwd=work)
    SKIPPED_PATHS.extend(n for n in tr.stdout.split("\0") if n and unsafe_name(n))
    info = os.path.join(work, ".git", "info")
    os.makedirs(info, exist_ok=True)
    run(g + ["config", "core.sparseCheckoutCone", "false"], cwd=work)
    if SKIPPED_PATHS:
        esc = lambda s: re.sub(r"([\\*?\[\]])", r"\\\1", s).replace("\n", "")
        with open(os.path.join(info, "sparse-checkout"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("/*\n" + "".join("!/" + esc(n) + "\n" for n in SKIPPED_PATHS))
        run(g + ["config", "core.sparseCheckout", "true"], cwd=work)
    else:
        run(g + ["config", "core.sparseCheckout", "false"], cwd=work)
    return run(g + ["reset", "-q", "--hard", rev], cwd=work).returncode == 0


def sync_clone(work, url, use_gh):
    """make `work` a clone of url at origin/main (a staging area only: it is reset to origin/main each time). -> True / False (offline, no access, missing)."""
    g = git_cmd(use_gh)
    if not os.path.isdir(os.path.join(work, ".git")):
        if os.path.isdir(work):
            shutil.rmtree(work, ignore_errors=True)
        os.makedirs(os.path.dirname(work), exist_ok=True)
        r = run(g + ["clone", "-q", "--depth", "1", "--no-tags", "--no-checkout", url, work], timeout=120)
        if r.returncode != 0:
            return False
        return checkout_safe(work, g, "HEAD")
    r = run(g + ["fetch", "-q", "--depth", "1", "origin", "main"], cwd=work, timeout=120)
    if r.returncode != 0:
        return False
    checkout_safe(work, g, "FETCH_HEAD")
    run(g + ["clean", "-qfd"], cwd=work)
    return True


def push_with_rebase(work, g, restage, tries=4):
    """push; on a non-fast-forward rejection pull --rebase and push again. Never force. restage() redoes the commit on a fresh tip if the rebase cannot run (shallow history).
    -> (ok, last stderr)"""
    err = ""
    for i in range(tries):
        r = run(g + ["push", "-q", "origin", "HEAD:refs/heads/main"], cwd=work, timeout=120)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or r.stdout)[-400:]
        if not re.search(r"(?i)non-fast-forward|fetch first|rejected|failed to update ref|stale info", err) or re.search(r"(?i)denied|403|protected branch|permission", err):
            return False, err
        pr = run(g + ["pull", "-q", "--rebase", "origin", "main"], cwd=work, timeout=120)
        if pr.returncode != 0:
            run(g + ["rebase", "--abort"], cwd=work)
            if run(g + ["fetch", "-q", "--depth", "1", "origin", "main"], cwd=work, timeout=120).returncode != 0:
                return False, err
            run(g + ["reset", "-q", "--hard", "FETCH_HEAD"], cwd=work)
            restage()
    return False, err


def cmd_flush(a):
    q = queue_dir(a.queue)
    say = (lambda m: None) if a.quiet else print
    if os.environ.get("CLAUDE_LEARN_SKIP") == "1":
        return 0
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import hiccup
        hiccup.queue_shared(a.queue, True)
    except Exception:
        pass
    if not os.path.isdir(os.path.join(q, "pending")):
        return 0
    notes = pending_notes(q)
    if not notes:
        return 0
    url = a.repo or target_repo()
    local = os.path.exists(url)
    use_gh = (not local) and bool(gh_login())
    work = os.path.join(q, "repo")
    if not sync_clone(work, url, use_gh):
        say("learn: %d note(s) stay queued (target repo not reachable or no read access). Try again later." % len(notes))
        return 0
    g = git_cmd(use_gh)
    added = stage_files(work, notes[: a.max])
    run(g + ["add", "--", "inbox"], cwd=work)
    st = run(g + ["status", "--porcelain"], cwd=work).stdout.strip()
    batch = notes[: a.max]
    if not st:                                  # already in the inbox (an earlier push whose bookkeeping failed)
        mark_sent(q, batch)
        return 0
    srcs = sorted({c["source"] for p, c in batch})
    msg = "inbox: %d note(s) from %s" % (len(batch), ", ".join(srcs)[:60])
    r = run(g + ["commit", "-q", "-m", msg], cwd=work)
    if r.returncode != 0:
        say("learn: commit failed (%s); notes stay queued" % (r.stderr or r.stdout).strip()[-120:])
        return 0
    def restage():
        stage_files(work, batch)
        run(g + ["add", "--", "inbox"], cwd=work)
        run(g + ["commit", "-q", "-m", msg], cwd=work)
    ok, err = push_with_rebase(work, g, restage)
    if ok:
        mark_sent(q, batch)
        say("learn: pushed %d note(s) to %s inbox/" % (len(batch), url if local else OWNER_REPO))
        return 0
    run(g + ["reset", "-q", "--hard", "FETCH_HEAD"], cwd=work)
    with open(os.path.join(q, "last-flush.json"), "w", encoding="utf-8") as fh:
        json.dump({"when": int(time.time()), "result": "kept", "queued": len(notes), "detail": err.strip()[-160:]}, fh)
    say("learn: %d note(s) stay queued: no write access to the inbox (or offline). Use `learn.py pr` to contribute through a pull request." % len(notes))
    return 0


def bundle(q, notes, repo_url):
    day = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    out = os.path.join(sub(q, "ready-to-send"), "vault-learnings-" + day)
    shutil.rmtree(out, ignore_errors=True)
    stage_files(out, notes)
    with open(os.path.join(out, "SEND-THIS.txt"), "w", encoding="utf-8") as fh:
        fh.write("These %d note(s) are ready for the vault-learnings inbox (public, CC0).\n\nEasiest: open a pull request on %s adding the inbox/ folder from this directory, "
                 "or open an issue there and attach the zip next to this folder. Nothing in here is run by anyone; the maintainer reviews it as untrusted data.\n"
                 % (len(notes), "https://github.com/" + OWNER_REPO))
    z = shutil.make_archive(out, "zip", out)
    return out, z


def cmd_pr(a):
    q = queue_dir(a.queue)
    notes = pending_notes(q)
    if not notes:
        print("learn: nothing queued")
        return 0
    url = a.repo or target_repo()
    login = gh_login()
    if os.path.exists(url) or not login:
        out, z = bundle(q, notes, url)
        print("learn: no gh login (or local target): ready-to-send folder %s and zip %s" % (out, z))
        return 0
    fork_url = None
    if login.lower() == OWNER_REPO.split("/")[0].lower():
        return cmd_flush(argparse.Namespace(queue=a.queue, quiet=False, repo=a.repo, max=200))
    r = run(["gh", "repo", "fork", OWNER_REPO, "--clone=false"], timeout=120)
    fork_url = "https://github.com/%s/%s.git" % (login, OWNER_REPO.split("/")[1])
    work = os.path.join(q, "fork")
    shutil.rmtree(work, ignore_errors=True)
    g = git_cmd(True)
    c = run(g + ["clone", "-q", "--depth", "1", "--no-tags", "--no-checkout", "https://github.com/%s.git" % OWNER_REPO, work], timeout=120)
    if c.returncode == 0 and not checkout_safe(work, g, "HEAD"):
        c.returncode = 1
    if c.returncode != 0:
        out, z = bundle(q, notes, url)
        print("learn: could not clone the inbox repo; ready-to-send folder %s and zip %s" % (out, z))
        return 0
    branch = "notes-%s-%s" % (datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S"), notes[0][1]["hash"][:6])
    run(g + ["checkout", "-q", "-b", branch], cwd=work)
    stage_files(work, notes)
    run(g + ["add", "--", "inbox"], cwd=work)
    run(g + ["commit", "-q", "-m", "inbox: %d note(s) from %s" % (len(notes), login and "a contributor")], cwd=work)
    run(g + ["remote", "add", "fork", fork_url], cwd=work)
    p = run(g + ["push", "-q", "fork", branch], cwd=work, timeout=120)
    if p.returncode != 0:
        out, z = bundle(q, notes, url)
        print("learn: push to your fork failed (%s); ready-to-send folder %s and zip %s" % ((p.stderr or "").strip()[-120:], out, z))
        return 0
    body = "Adds %d note(s) to inbox/. Generated by learn.py; scanned for secrets, personal data and instruction-like text before sending. Contributed under CC0 (see CONTRIBUTING.md)." % len(notes)
    pr = run(["gh", "pr", "create", "--repo", OWNER_REPO, "--head", "%s:%s" % (login, branch), "--title", "Inbox: %d note(s)" % len(notes), "--body", body], timeout=120)
    if pr.returncode != 0:
        out, z = bundle(q, notes, url)
        print("learn: pull request could not be opened (%s); branch %s is on your fork; ready-to-send folder %s" % ((pr.stderr or "").strip()[-120:], branch, out))
        return 0
    mark_sent(q, notes)
    print("learn: pull request opened: %s" % pr.stdout.strip().splitlines()[-1])
    return 0


def cmd_status(a):
    q = queue_dir(a.queue)
    cnt = {d: len(read_notes(os.path.join(q, d))) for d in ("pending", "sent", "rejected")}
    print("queue %s: %s" % (q, ", ".join("%s %d" % kv for kv in cnt.items())))
    lf = os.path.join(q, "last-flush.json")
    if os.path.exists(lf):
        print("last flush:", open(lf, encoding="utf-8").read().strip())
    return 0


def main(argv=None):
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(prog="learn.py", description="record verified findings and send them to the vault-learnings inbox")
    ap.add_argument("--queue")
    sp = ap.add_subparsers(dest="cmd")
    s = sp.add_parser("add")
    s.add_argument("--title"); s.add_argument("--topic"); s.add_argument("--body"); s.add_argument("--body-file")
    s.add_argument("--verified"); s.add_argument("--confidence", default="medium"); s.add_argument("--source", default="claude-code"); s.add_argument("--vault")
    s = sp.add_parser("search"); s.add_argument("words", nargs="+"); s.add_argument("--vault")
    sp.add_parser("list")
    s = sp.add_parser("scan"); s.add_argument("file")
    s = sp.add_parser("flush"); s.add_argument("--quiet", action="store_true"); s.add_argument("--repo"); s.add_argument("--max", type=int, default=50)
    s = sp.add_parser("pr"); s.add_argument("--repo")
    sp.add_parser("status")
    s = sp.add_parser("hiccup", add_help=False); s.add_argument("rest", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    if a.cmd == "hiccup":
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import hiccup
        return hiccup.main(a.rest)
    fn = {"add": cmd_add, "search": cmd_search, "list": cmd_list, "scan": cmd_scan, "flush": cmd_flush, "pr": cmd_pr, "status": cmd_status}.get(a.cmd)
    if not fn:
        ap.print_help()
        return 2
    try:
        return fn(a)
    except KeyboardInterrupt:
        return 130
    except Exception as ex:                      # flush must never break the caller (kit-refresh); other commands report
        if a.cmd == "flush" and getattr(a, "quiet", False):
            return 0
        print("learn: error: %s" % ex, file=sys.stderr)
        return 1 if a.cmd == "flush" else 2


if __name__ == "__main__":
    sys.exit(main())
