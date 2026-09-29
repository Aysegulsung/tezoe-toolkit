#!/usr/bin/env python3
"""normalise_cm.py pre|snap|post — CM supplier template normaliser (h1..h6 headed blocks).
pre : specs (SPECIFICATIONS), package (WHAT'S IN THE BOX) and key_features (WHY … list) from h1–h6 headed blocks.
snap: save key_features to _kf_snap.json (before sections.py --extract).
post: move WHY/lead sections sections.py proposed into sections_dismissed; restore key_features from the snap.
"""
import json, re, sys, glob, html
def clean(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()
HEAD = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.S | re.I)
SPEC = re.compile(r"specification|technical data|details|product data", re.I)
PACK = re.compile(r"box|package|contain|content|included|scope of delivery|delivery includes", re.I)   # CM-batch29 p32: "CONTENTS"
WHY = re.compile(r"\bwhy\b|advantages|benefits|features|highlights", re.I)
def blocks(h):
    hs = [(m.start(), m.end(), clean(m.group(2))) for m in HEAD.finditer(h)]
    hs = [x for x in hs if x[2]]
    for i, (s, e, t) in enumerate(hs):
        nxt = hs[i + 1][0] if i + 1 < len(hs) else len(h)
        yield t, h[e:nxt]
def lines(block):
    li = [clean(x) for x in re.findall(r"<li[^>]*>(.*?)</li>", block, re.S | re.I)]
    li = [x for x in li if x]
    if li: return li
    return [clean(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", block, re.S | re.I) if clean(x) and not re.match(r"\s*<img", x)]
def boldspec(raw):
    """CM-batch29 p00/p02: "<strong>Material</strong> High-quality plastic." — no colon, the bold lead is the name."""
    m = re.match(r"\s*<(strong|b)[^>]*>(.*?)</\1>(.*)", raw, re.S | re.I)
    if not m: return None
    n, v = clean(m.group(2)).rstrip(":").strip(), clean(m.group(3)).lstrip(":–—- ").strip().rstrip(".")
    return {"name": n, "value": v} if n and v else None
def rawlines(block):
    li = [x for x in re.findall(r"<li[^>]*>(.*?)</li>", block, re.S | re.I) if clean(x)]
    return li or [x for x in re.findall(r"<p[^>]*>(.*?)</p>", block, re.S | re.I) if clean(x) and not re.match(r"\s*<img", x)]
def splitspec(t):
    m = re.match(r"([^:–—]{2,40}?)\s*(?::|\s[–—-]\s)\s*(.+)", t)
    return {"name": m.group(1).strip(), "value": m.group(2).strip().rstrip(".")} if m else None
mode = sys.argv[1]
for f in sorted(glob.glob("extract/p*.json")):
    e = json.load(open(f)); n = f[-7:-5]
    if mode == "pre":
        h = json.load(open(f"raw/p{n}.json"))["descriptionHtml"] or ""
        specs, pack, kf = [], [], []
        seen_spec = False
        for t, b in blocks(h):
            if SPEC.search(t) and seen_spec and not pack:
                pack += [x for x in lines(b) if len(x) < 200]   # CM-batch29 p08: box list under a 2nd "SPECIFICATIONS" heading
            elif SPEC.search(t):
                seen_spec = True
                for raw in rawlines(b):
                    s = splitspec(clean(raw)) or boldspec(raw)
                    if s: specs.append(s)
            elif PACK.search(t):
                pack += [x for x in lines(b) if len(x) < 200]
            elif WHY.search(t):
                kf += [x for x in re.findall(r"<li[^>]*>(.*?)</li>", b, re.S | re.I)]
        kf = [clean(x) for x in kf if clean(x)]
        if specs and not e["specs"]: e["specs"] = specs
        if pack and not e["package"]: e["package"] = pack
        if kf: e["key_features"] = kf
        print(n, len(e["specs"]), len(e["package"]), len(e.get("key_features", [])))
    elif mode == "snap":
        snap = json.load(open("_kf_snap.json")) if glob.glob("_kf_snap.json") else {}
        snap[n] = e.get("key_features", []); json.dump(snap, open("_kf_snap.json", "w"), indent=1)
    elif mode == "post":
        snap = json.load(open("_kf_snap.json"))
        keep, moved = [], 0
        for s in e.get("sections", []):
            if WHY.search(s["heading_source"]) or s.get("heading") is None:
                e.setdefault("sections_dismissed", []).append({"heading_source": s["heading_source"], "reason": "source feature/benefit list (key_features is its home)", "lines": s["lines"]}); moved += 1
            else: keep.append(s)
        e["sections"] = keep; e["key_features"] = snap.get(n, e.get("key_features", []))
        if moved or keep: print(n, "moved", moved, "kept", [s["heading"] for s in keep])
    json.dump(e, open(f, "w"), indent=1, ensure_ascii=False)
