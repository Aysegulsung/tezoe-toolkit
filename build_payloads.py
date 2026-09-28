#!/usr/bin/env python3
"""build_payloads.py — ddl2-batch28: final/dNN.json -> rewrites.json + push/*.json, in ONE offline pass.

README step 7. Nothing is fired here; every mutation is written to its own file so the push is a
bare `for f in push/mut*.json push/cta*.json push/alt*.json; do python3 shopify_api.py mutate $f; done`
with zero bash round-trips carrying data.

What each payload carries, from the brief:
  Q5 Make Active      -> status: ACTIVE on every product
  Q6 Rewrite titles   -> title + seo.title
  Q7 Rewrite descr.   -> descriptionHtml + seo.description
                         (`seo` is replaced WHOLE — README step 7 — so both halves always travel together)
  Q8 Auto-infer       -> tags = snapshot tags ∪ {season}, deduped, nothing dropped
  Q2 Keep current     -> NO productVariantsBulkUpdate alias at all
  Q12                 -> productType + category (Shopify taxonomy gid)
  Q13                 -> collectionsToJoin (existing collections only; this batch proposed no new one)
  Q11                 -> custom.cta_benefits, list.single_line_text_field, 25 per metafieldsSet call
  Q16                 -> fileUpdate alt text, batched

The taxonomy leaf is chosen per product below, not parsed from the agents' `category_proposal`
strings — five different agents wrote "Wall Lights", "Wall Lighting" and "Wall Lamps" for the same
Shopify leaf, and verify.py check 8 compares the LIVE category name with `category_proposal`, so the
proposal is rewritten in final/dNN.json to the exact leaf name assigned here.
"""
import json, glob, os, collections

TAX = {  # taxonomy leaf -> (gid suffix, exact leaf name as Shopify returns it)
    "WLF":       ("hg-13-9-4",    "Wall Light Fixtures"),
    "TABLE":     ("hg-13-5-5",    "Table Lamps"),
    "CLOCK":     ("hg-3-17-4",    "Wall Clocks"),
    "PATH":      ("hg-13-6",      "Landscape Pathway Lighting"),
    "MIRROR":    ("hg-3-47-2",    "Wall Mirrors"),
    "PLANTER":   ("hg-12-1-16-1", "Planters"),
    "NIGHT":     ("hg-13-10",     "Night Lights & Ambient Lighting"),
    "SAIL":      ("hg-12-2-8-3",  "Shade Sails"),
    "STAND":     ("hg-12-1-14",   "Plant Stands"),
    "SHELF":     ("fr-19-2-2",    "Floating Wall Shelves & Ledges"),
}
CAT = {}
for nn in "00 01 02 03 04 06 08 09 11 12 13 14 15 16 17 18 19 31 32 33 42 45".split(): CAT[nn] = "WLF"
for nn in "23 24 30 35 38 39 40 44".split():                                        CAT[nn] = "TABLE"
for nn in "07 10 25 26 27 28 29".split():                                           CAT[nn] = "CLOCK"
for nn in "22 43 46".split():                                                       CAT[nn] = "PATH"
for nn in "47 48 49".split():                                                       CAT[nn] = "MIRROR"
for nn in "21 34 36".split():                                                       CAT[nn] = "PLANTER"
CAT["05"] = "NIGHT"; CAT["20"] = "SAIL"; CAT["37"] = "STAND"; CAT["41"] = "SHELF"

MUT_PER_CALL, CTA_PER_CALL, ALT_PER_CALL = 10, 25, 40


def main():
    os.makedirs("push", exist_ok=True)
    snap = {n["id"]: n for n in (e["node"] for e in json.load(open("products.json"))["data"]["products"]["edges"])}

    colmap = {}
    raw = json.load(open("collections.json"))
    edges = raw["data"]["collections"]["edges"] if isinstance(raw, dict) and "data" in raw else raw
    for e in edges:
        n = e.get("node", e)
        colmap.setdefault(n["title"], n["id"])          # duplicate titles: first wins

    rewrites, cta_rows, alt_rows, missing_col = [], [], [], []
    for f in sorted(glob.glob("final/d*.json")):
        nn = f[-7:-5]
        d = json.load(open(f))
        pid = d["product_id"]
        s = snap[pid]
        tags = list(dict.fromkeys((s.get("tags") or []) + [d["season"]]))
        cat_key, cat_name = TAX[CAT[nn]]
        if d.get("category_proposal") != cat_name:      # keep verify.py check 8 honest
            d["category_proposal"] = cat_name
            json.dump(d, open(f, "w"), indent=1, ensure_ascii=False)
        cols = []
        for t in d.get("collections") or []:
            if t in colmap:
                cols.append(colmap[t])
            else:
                missing_col.append((nn, t))
        rewrites.append({
            "product_id": pid, "idx": nn,
            "title": d["title"],
            "descriptionHtml": d["descriptionHtml"],
            "seo": {"title": d["seo"]["title"], "description": d["seo"]["description"]},
            "status": "ACTIVE",
            "tags": tags,
            "productType": d["productType"],
            "category": f"gid://shopify/TaxonomyCategory/{cat_key}",
            "collectionsToJoin": cols,
        })
        cta_rows.append({"ownerId": pid, "namespace": "custom", "key": "cta_benefits",
                         "type": "list.single_line_text_field",
                         "value": json.dumps(d["cta_benefits"], ensure_ascii=False)})
        for a in d.get("media_alts") or []:
            alt_rows.append({"id": a["id"], "alt": a["alt"]})

    json.dump(rewrites, open("rewrites.json", "w"), indent=1, ensure_ascii=False)

    # --- productUpdate, 10 aliased per call -------------------------------------------------
    n_mut = 0
    for i in range(0, len(rewrites), MUT_PER_CALL):
        chunk = rewrites[i:i + MUT_PER_CALL]
        decl, body, vrs = [], [], {}
        for j, r in enumerate(chunk):
            decl.append(f"$ip{j}: ProductUpdateInput!")
            body.append(f"  p{j}: productUpdate(product: $ip{j}) {{ userErrors {{ field message }} }}")
            vrs[f"ip{j}"] = {k: v for k, v in r.items() if k not in ("idx",)}
            vrs[f"ip{j}"]["id"] = vrs[f"ip{j}"].pop("product_id")
        q = "mutation(" + ", ".join(decl) + ") {\n" + "\n".join(body) + "\n}"
        json.dump({"query": q, "variables": vrs}, open(f"push/mut{n_mut}.json", "w"), ensure_ascii=False)
        n_mut += 1

    # --- metafieldsSet, 25 per call --------------------------------------------------------
    n_cta = 0
    for i in range(0, len(cta_rows), CTA_PER_CALL):
        q = ("mutation($m: [MetafieldsSetInput!]!) { metafieldsSet(metafields: $m) "
             "{ userErrors { field message } } }")
        json.dump({"query": q, "variables": {"m": cta_rows[i:i + CTA_PER_CALL]}},
                  open(f"push/cta{n_cta}.json", "w"), ensure_ascii=False)
        n_cta += 1

    # --- fileUpdate alt text --------------------------------------------------------------
    n_alt = 0
    for i in range(0, len(alt_rows), ALT_PER_CALL):
        q = ("mutation($f: [FileUpdateInput!]!) { fileUpdate(files: $f) "
             "{ userErrors { field message } } }")
        json.dump({"query": q, "variables": {"f": alt_rows[i:i + ALT_PER_CALL]}},
                  open(f"push/alt{n_alt}.json", "w"), ensure_ascii=False)
        n_alt += 1

    print(f"build_payloads: {len(rewrites)} products -> {n_mut} productUpdate calls, "
          f"{n_cta} metafieldsSet calls ({len(cta_rows)} metafields), "
          f"{n_alt} fileUpdate calls ({len(alt_rows)} alts)")
    if missing_col:
        print("[WARN] collection titles not in collections.json:", missing_col)
    else:
        print("build_payloads: every proposed collection resolved to an existing collection id")


if __name__ == "__main__":
    main()
