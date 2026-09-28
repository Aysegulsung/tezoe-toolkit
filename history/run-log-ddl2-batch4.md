# run-log-ddl2-batch4 — Worfa, 2026-09-11 (session 2 — the 2026-09-10 attempt never pushed; egress 403, see checkpoint-ddl2-batch4.md)

Brief: Q1 tag DDL2-Batch4 (50 products, all DRAFT) · Q2 keep prices · Q5 keep status · Q6 rewrite titles (title-format-rule.md) · Q7 rewrite descriptions · Q8 auto-infer season · Q10 manual, full batch approved · Q11 CTA benefits · Q12 productType + category · Q13 collections · Q14 re-host · Q15 backup titles · Q16 alt text · Q17 comparison table · Q18 skip · Q19 fit block.
Store: Worfa (ymjviw-rz.myshopify.com), script route via shopify_api.py. Work dir was a fresh container: live titles were fetched and found equal to the old titles of backup-titles-ddl2-batch4.md (50/50), so the batch was re-run from step 0 (the previous session's finals were lost with its container).

## Step 0 — toolkit copy
57 files copied by a Sonnet agent; `sha256sum -c`: 2 genuine copy corruptions fixed by re-copy (rules/description-format-rule.md, dim_image.py), 1 stale manifest line — `./kw_measure.py` (project doc updated 2026-09-11 18:36 with the proxy-backoff paragraph after the manifest's 11:55 refresh; two independent copies agree; new sha256 of the verified copy: see below). Every .py compiles.
**shopify_api.py edited on disk (user-approved 2026-09-11 before the brief):** `gql()` retries an empty/non-JSON response (the sandbox egress proxy intermittently refuses CONNECT with 403 for ~20 s) after 10/30/60 s, retries 3 → 6. The project copy is NOT updated in this run (pending the user's approval — see open items).

## Step 1–2
brief_flags.json {q17 true, q19 true, q18 false, run_mode manual}. Fetch: 50 products, 472 media, 100 foreign description images (99 on another store's CDN + 1 dead). collections.json refreshed: 31 collections.

## Step 3 — extraction
5 Sonnet agents × 10. "What's in the Box?" blocks (47 products) dismissed as sections — identical to extract.package. Two [UNMAPPED] headings named: p11 "Activation Method" → Functions, p43 "Estimated Usage Time" → Safety Warnings.
sections: 3 products with 10 sections (p11 4, p16 3, p43 3), 66+47 dismissed (description lead 24 / long marketing heading 42 / package list 47), 2 unmapped named.
para_feat: 63 KF flagged, 1 added (p21 flashing lights and sound), 62 dismissed (marketing restatements) | 25 SPEC flagged, 1 added (p38 Weight 20 g / 0.7 oz), 24 ruled (rulings_omit.json: same value as a table pair in another form on p04/p12/p15/p26/p33/p44/p46/p48/p20; conflicts p16 2.27 kg vs table 451.5 g, p45 40×40 cm vs table 39×39 cm — table kept). para_feat --gate: 0 unruled.
extract-check: 0 FAIL; agent additions KF 12, spec 12; main-context additions KF 2, spec 1.
KF/spec independent review: 2 eligible of 50, 2 marked, 1 confirmed and added (p18 tufted design), 1 dismissed.
RULINGS.md: 12 rulings (p16/p20/p45 figure conflicts, p41 material, p47 filter layers, p18 "Doctor Recommended" omitted, p31 dead image, supplier policy lines).

## Step 4 — keywords
source_windows: 50 titles → 994 windows, 0 dropped. kw_measure: 3242 raw → 3048 unique, 0 dropped, 3048 measured in 6 call(s) over 3 round(s) — 77 word-order variant(s) moved to later rounds; 0 not returned; cost $0.54. kw-cache-ddl2-batch4.md sent to chat.

## Step 5 — titles
One title agent, all 50. title-check: 0 FAIL, 75 WARN, 101 MANUAL REVIEW; head-check 0 FAIL of 50. All 50 titles in the 70–120 zone (108–120 chars), no trigger claimed. Fit-clean multi-word captured volume 5,097,610 (toolkit figure 16.48M inflated by single-word candidates). Old-vs-new product-naming volume ≥ old on all 50. Step 1b not needed. backup-titles-ddl2-batch4.md rewritten in the project before the push.

## Step 5b — re-host
rehost.py: 99 mapped, 1 failed (p31 second image, another store's CDN, HTTP 404 dead link — fileCreate "Media processing failed"). Ruling: replaced with the product's own gallery image 2 so no broken image is published; count and position unchanged. Re-run: 0 still foreign. One FAILED MediaImage file (36759814799396) left in Files — can be deleted by hand.

## Step 6 — descriptions
5 Sonnet agents × 10; gate.py CLEAN over all 50 (struct-check WARN only: total words > 500 on 2 products, prose > 110 on 4 — source length). productType aligned to the title agent's §10b draft on 11 products.
6b fact_cover: run 1 — 13 lines under 55%, all (b) same meaning in other words; 0 genuinely missing. Run 2 after corrections: identical 13 lines (diff empty).
6c read on all 50 products: corrected p00 p01 p02 p03 p04 p05 p06 p08 p09 p10 p11 p12 p13 p14 p15 p18 p19 p21 p22 p23 p25 p26 p27 p29 p31 p35 p38 p44 p45 p49 (variant/pack facts, occasion and aesthetics lines, universal "any", unsourced "years"/"fumes", invented Others figure "480p typical").
CTA read on all 50 products, corrected: p00 p03 p04 p05 p06 p08 p09 p11 p12 p14 p18 p19 p21 p22 p23 p26 p27 p29 p38 p45 p49.
CTA independent review: 25 marked on 20 products, 24 confirmed and corrected, 1 dismissed (p41 "Acts like a real puppy" — the companion benefit itself).
KF read on all 50 products: copies 0 (keyfeat_cover), paragraph additions on 3 products (p18, p21 + agents' 12); p45 "years of play" reworded to the source's "long-lasting use" meaning.
6d: one correction message per agent; changed lines re-read by eye — p26 "fumes" corrected again by the main context; gate CLEAN over 50 after the round.
Category: 50 taxonomy gids resolved by search (category_map.json); p49 collection "Health & Wellness" → "Health". Collections used: 22 existing, 0 new.

## Step 7 — push
dim-keep: 0 restored, 0 warned, 50 untouched. Payloads: push/mut0–4 (aliased productUpdate: title, descriptionHtml, seo whole, productType, tags = snapshot ∪ season, category, collectionsToJoin), cta0–1 (metafieldsSet custom.cta_benefits ×50), alt0–9 (fileUpdate 472 alts; two agents had dropped the last media item on p18/p48 — added before the push). backup-alt-ddl2-batch4.md sent to chat before the alt push. Live titles re-checked equal to the snapshot immediately before the push (50/50). All 17 payloads: clean (0 userErrors).
Seasons: {'evergreen': 43, 'summer': 3, 'winter': 4}.

## Step 8 — verify
`verify: 50 products, 901 checks, 0 failures` · `head-check: 0 FAIL of 50` · 0 [note] lines.

## Open items
- shopify_api.py proxy-retry edit is on disk only; MANIFEST line for kw_measure.py is stale in the project. Both need a project write (user approval).
- p31: the supplier's 2nd description image was a dead link; the page now shows gallery image 2 there.
- One FAILED MediaImage file from the p31 attempt sits in Worfa Files (gid 36759814799396).

## coverage.md (extract_check)
| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 4 | 0 | 0 | - | 6 | 0 | 0 | - |
| 01 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 02 | 4 | 0 | 0 | - | 7 | 0 | 0 | - |
| 03 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 04 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 05 | 5 | 1 | 0 | - | 6 | 0 | 0 | - |
| 06 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 07 | 4 | 0 | 0 | - | 5 | 0 | 0 | - |
| 08 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 09 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 10 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 11 | 8 | 0 | 0 | - | 10 | 0 | 0 | - |
| 12 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 13 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 14 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 15 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 16 | 5 | 1 | 0 | - | 7 | 1 | 0 | - |
| 17 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 18 | 5 | 0 | 1 | - | 5 | 0 | 0 | - |
| 19 | 5 | 0 | 0 | - | 5 | 1 | 0 | - |
| 20 | 5 | 3 | 0 | - | 2 | 0 | 0 | - |
| 21 | 5 | 0 | 1 | - | 5 | 0 | 0 | - |
| 22 | 4 | 0 | 0 | - | 5 | 1 | 0 | - |
| 23 | 5 | 0 | 0 | - | 6 | 1 | 0 | - |
| 24 | 5 | 1 | 0 | - | 3 | 1 | 0 | - |
| 25 | 4 | 1 | 0 | - | 5 | 1 | 0 | - |
| 26 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 27 | 5 | 1 | 0 | - | 4 | 1 | 0 | - |
| 28 | 5 | 1 | 0 | - | 4 | 1 | 0 | - |
| 29 | 5 | 1 | 0 | - | 4 | 0 | 0 | - |
| 30 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 31 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 32 | 4 | 0 | 0 | - | 5 | 0 | 0 | - |
| 33 | 4 | 0 | 0 | - | 4 | 0 | 0 | - |
| 34 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 35 | 3 | 0 | 0 | - | 3 | 0 | 0 | - |
| 36 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 37 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 38 | 3 | 0 | 0 | - | 4 | 0 | 1 | - |
| 39 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 40 | 5 | 0 | 0 | - | 3 | 2 | 0 | - |
| 41 | 4 | 1 | 0 | - | 7 | 0 | 0 | - |
| 42 | 5 | 0 | 0 | - | 5 | 1 | 0 | - |
| 43 | 5 | 0 | 0 | - | 12 | 0 | 0 | - |
| 44 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 45 | 5 | 0 | 0 | - | 5 | 1 | 0 | - |
| 46 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 47 | 4 | 1 | 0 | - | 6 | 0 | 0 | - |
| 48 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 49 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |

