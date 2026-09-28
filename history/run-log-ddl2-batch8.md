# Run log — DDL2-Batch8 (Worfa, 2026-09-12, manual run, full batch approved)

Store **Worfa** (`ymjviw-rz.myshopify.com`), tag `DDL2-Batch8`, 50 products.
Brief: Q1 tag DDL2-Batch8 · Q2 keep prices · Q3 none · Q4 no rounding · Q5 keep status · Q6 rewrite titles
(Q9 = title-format-rule.md) · Q7 rewrite descriptions (description-format-rule.md) · Q8 auto-infer season ·
Q10 manual, user approved the full batch up front (no test-run question) · Q11 CTA benefits · Q12 product type +
category · Q13 collections · Q14 re-host images · Q15 title backup · Q16 alt text · Q17 comparison table ·
Q18 skip dimension image · Q19 fit block.

**Result: pushed and verified — `verify: 50 products, 901 checks, 0 failures`, `head-check: 0 FAIL of 50` on the live copy.**
This is the batch the 2026-09-10 scheduled run halted on (egress denial); nothing had been changed then, so this ran from step 0.

## Step 0 — toolkit copy
56 toolkit/rule files copied by 5 Sonnet agents (no Haiku anywhere). `sha256sum -c MANIFEST.sha256 --quiet` → **TOOLKIT OK
on the first copy**: 0 FAILED, 0 stale lines, manifest unchanged.
Note for the manifest keeper: `./README-toolkit.md` — the line the DDL2-Batch7 note recorded as *knowingly stale* because
no copy could be certified — **passed here on the first copy** (`2e76d59c…`), in a clean session. That note can be closed.

## Step 1 — credentials and flags
`secrets/shopify.json` from toolkit/shopify-api-credentials.md; `shopify_api.py shop` → **Worfa**.
`brief_flags.json` = `{"q17_compare_table": true, "q19_fit_block": true, "q18_dimension_image": false, "run_mode": "manual"}`.
Q18 skipped, so rembg/onnxruntime were not installed and step 7b did not run.

## Steps 2–3 — fetch and extraction
`fetch DDL2-Batch8 products.json` → 50 products. `extract_html.py` → raw/ + extract/ skeletons, 50 products with foreign images.
`keyfeat_cover.py --extract`, `usage_tips.py --extract` (**4 of 50 products carry a Usage Tips block**), then `sections.py --extract`.
5 Sonnet agents × 10 products per EXTRACT-SPEC.md filled identity, notes, safety_flags, season_hint and completed
key_features / specs; candidates/cNN.json written for all 50.

**sections (§7c): `45 of 50 products carry a fact section, 55 block(s) dismissed by the script (marketing 0 / policy 1 /
description lead 13 / long marketing heading 41), 49 UNMAPPED heading(s), 6 key_features line(s) moved into sections`.
Main-context triage then dismissed ALL 52 kept blocks** and restored the 6 moved key_features lines: every proposed block was
either the supplier's **package block** (`What's in the Box?`, 45 products — already `extract.package`) or a **spec-table
heading** (`Material`, `Weight`, `Functions`, `Operation Type`, `Size` — already `extract.specs`). Writing them would have
duplicated Package Includes and Specifications. `extract.sections` is empty on all 50; gate's sections check ran and printed
`0 FAIL across 50 products`.
*For the next run:* this is a second shape the script cannot see — a source whose spec table and package list are written as
short `<h3>` headings (1–2 words, so `MAX_HEAD_WORDS` does not catch them, and not heading index 0, so the description-lead
test does not either). A cheap guard would be to dismiss a block whose lines are already present in `extract.package` or
`extract.specs`. Not implemented here — recorded for the script's owner.

**para_feat (3b): `69 KF flagged, 0 SPEC flagged across 50 products` — 9 added, 60 dismissed | 0 SPEC flagged, 0 added.**
Added (source "Why Choose" lines the parser had missed, one per line): p06 ×1 (500°F Max Heat), p07 ×2 (Convenient Auto Timer,
Cozy Warm White Glow), p16 ×1 (Machine Washable), p30 ×5 (the product's whole feature list — its `key_features` had held only
the headline, which was removed). The other 60 flags are the intro paragraph restating the captured list. `para_feat.py --gate`
→ `0 unruled prose spec figure(s) missing from extract.specs`.

**extract_check: `0 FAIL across 50 products; agent additions total KF 3, spec 7; main-context additions KF 9, spec 0`.**
coverage.md is pasted at the end of this log.

**KF/spec independent review (3c): 0 eligible of 50 (min 80 words), 0 marked, 0 confirmed** — the sources in this batch are
short bullet lists, none over the word threshold.

**RULINGS.md** (17 source contradictions; full text kept with the run artefacts):
boilerplate spec values dropped on p03, p05, p22, p47; spec figures contradicting what is actually sold dropped on p10, p14,
p16 (p09 and p31 kept verbatim with the figure attributed to its own size/variant); foreign brand name dropped from p06's
package line; p17 renamed from "Storage Bag" to **storage box** (dominant evidence); p20 and p40 use the variant names as sold;
p35 carries no waterproof and no heavy-duty claim (the old title's, unsupported); p07 never promises mains power; p08 is a
seasonal/holiday mug, not Christmas-only; p49's source is truncated (no spec or package block at all). 14 values in
`rulings_omit.json`, each mirrored in that product's `omit_per_ruling`.

## Step 4 — keyword measurement
`source_windows.py` → **959 windows from 50 titles, 0 dropped over the DataForSEO limit**.
`kw_measure.py` over all cNN.json ∪ source_windows.txt: `3287 raw -> 3001 unique (22 normalised, 0 empty), 0 dropped over the
DataForSEO limit, 3001 to measure **in 5 call(s) over 2 round(s) — 56 word-order variant(s) moved to later rounds**`;
`done — 3001 lines appended to kw.txt, 0 not returned, 0 dropped oversize`. Cost ≈ $0.45.
kw-cache sent to the chat (not a project doc).

## Step 5 — titles
One title agent per TITLE-SPEC.md. **`title-check.py`: 0 FAIL** (69 WARN, 119 MANUAL REVIEW) and **`head_check.py`: 0 FAIL of 50**.
Total captured volume 4,081,170; 49 titles inside the 70–120 base zone, p39 at 128 on trigger A (`christmas tree ornaments` 33,100).
Three logged skips (`skip_reasons.json` → rejects.json): p07 `led lights for christmas` 74,000 (its own "for" clause splits the
opener segment), p15 `ebike accessories` 8,100 (beaten by `motorcycle accessories` 12,100 for the third cluster),
p22 `gold necklace women` 60,500 (needs a 4th "Necklace", cap is 3).
`backup-titles-ddl2-batch8.md` written to the project **before** any push (and rewritten after the two §6 corrections below).

**§6 product-fit corrections (main context, 6c reading) — two titles rebuilt:**
- **p34** `Clear Plastic Storage Box … Stackable Storage Containers` → `Ornament Storage Box for Christmas Decorations,
  Plastic Storage Box for Ornaments, Under Bed Storage Containers`. The source never says clear, transparent, see-through or
  stackable — the same class as the rule's `shower slippers` example. The description had built a bullet, a comparison row, a
  fit line, an FAQ answer, two CTA lines and both SEO fields on "see what's inside"; all were rebuilt.
- **p31** `… Stackable Plastic Storage Bins` → `… Foldable Plastic Storage Bins`. The source says **foldable**, never stackable,
  and the Key Features intro had invented "built to handle stacked weight without cracking".
A title-word audit against each product's own source text was run over all 50; every other flagged word was a synonym,
audience term or category name that describes the same product (couch/sofa, toddlers/children, ushanka/trapper), not an
unsupported attribute.

## Step 5b — image re-host (Q14)
`rehost.py`: **89 mapped, 14 failed, 89 srcs rewritten**. The 14 failures are on 9 products (p18, p29, p31, p32, p33, p34, p35,
p37, p38): `fileCreate` returned `Media processing failed` and a direct fetch of each URL returns **HTTP 404** — the supplier
store's CDN (`/s/files/1/0973/4773/1805/`) no longer serves them; they are dead on the live pages today. Two further re-runs
changed nothing. Ruling: a dead link is not a source image, so the Forbidden Action "never push a description with an image
outside our own CDN" governs. Each dead `<img>` kept its position and count and its `src` was replaced with one of that
product's **own Shopify gallery images** — the remedy description-format-rule.md already prescribes for a product with no
source image. Originals kept in `images[].src_original`; full list in `dead_images_replaced.json`. **0 images still foreign.**
No image was deleted and none added.

## Step 6 — descriptions
5 Sonnet agents × 10 products per DESC-SPEC.md; each returned gate-clean on its own range, and the main context re-ran
`gate.py` over all 50 → **`=== gate: CLEAN ===`** (exit 0), before and after every correction round.

**6b fact coverage:** `fact-cover: 715 source fact lines scored, 4 below 55%` — p05 (bunny movements), p15 (13.5 × 9.5 cm size),
p31 ×2 (carry handles, intro paragraph). All four are case **(b)**, the same meaning in different words: each fact is present in
the prose, Key Features, Specifications, the comparison table, the fit block and an FAQ answer. **0 genuine misses, 0 products
sent back for 6b.** The post-correction re-run is **byte-identical** to the first (`diff` empty) — no 6c edit moved a fact.

**6c benefit review, read on all 50 products** (H2 + 5 bullets + 3 CTA lines + 5 comparison rows + 4 fit lines).
Corrected: **p08, p10, p18, p19, p22, p31, p33, p34, p35, p37, p39, p40, p41, p44** — occasion / gift bullets (p08, p18, p19,
p22, p37, p39, p41, p44), variant-fact bullets (p10 colours, p33 sizes, p35 colours, p39 six styles, p40 sizes **and** colours),
p40's three near-duplicate "couch or bed" bullets, and the two §6 rebuilds (p31, p34). p40 needed a second round: the first
rebuild replaced one weak bullet pair with two fresh variant facts.

**Key Features list read on all 50 products: copies 0 (keyfeat_cover), paragraph additions on 4 products (p06, p07, p16, p30).**
One shortfall found and fixed by eye: **p10** had dropped its whole `Universal Fit` source line because its two figures are
ruled out — only the figures are, so the line came back as an item written through the sizes actually sold.

**CTA read on all 50 products as its own pass, corrected: p00, p03, p04, p05, p08, p09, p18, p19, p22, p34 ×2, p35, p39, p40,
p44, p48, p49.**
**CTA independent review: 16 marked on 15 products, 16 confirmed and corrected, 0 dismissed** (`cta-review: 16 lines marked on
15 products`). Cost ≈ 0.15M tokens. Every mark was real: 7 occasion/gift lines, 4 what-it-does lines, 2 unsourced claims
(p34 ×2, on a product whose title was also wrong), 1 pack-count line, 1 battery overstatement (p00 "All-day warmth" against an
8–10 hour spec), 1 season overclaim (p49 "all season" on a winter-only hat). My own reading added p22's `A gift that feels
personal`, which the reader had not marked.

**6d:** each agent received 6b and 6c in **one** message and returned once; gate re-run over all 50 (CLEAN), fact_cover re-run
and diffed (identical), and every H2/bullet/CTA line the corrections changed was re-read by eye — that re-read is what caught
p40's second variant-bullet pair and p10's missing Key Features item, both corrected in a follow-up.

## Step 7 — push
`dim_keep.py`: **`dim-keep: 0 restored, 0 warned, 50 untouched`** (no product in this batch carried a Q18 image).
**Q12 — product type and category:** all 50 products had **no category at all** before this run. Each `category_proposal` was
resolved against the live Shopify Standard Product Taxonomy and rewritten to the exact node name, e.g. p06 → *Electric Griddles
& Grills*, p18 → *Spice Organizers*, p19 → *Remote Control Cars & Trucks*, p21 → *Vehicle GPS Trackers*, p24 → *Hand Grippers*,
p26 → *Surveillance Cameras*, p36 → *Food Warmers*, p46 → *Toy Kitchens*, p17/p29/p31/p34 → *Household Storage Containers*,
p32/p33/p35 → *Household Storage Bags*. Three had no honest leaf and took the nearest true parent (p02 *Clothing Accessories*,
p23 *Pet Supplies*, p25 *Electronics Accessories*).
**Q13 — collections:** existing Worfa collections used where they fit (Toys 7, Kids 7, Home Decor 7, Storage & Organization 7,
Accessories 6, Kitchen & Dining 6, …). One agent wrote `Kitchen`, corrected to the real `Kitchen & Dining`. **Four collections
created**: *Women's Apparel* (p01, p04), *Motorcycle Accessories* (p15), *Fitness & Exercise* (p38), *Seasonal & Holiday* (p17).
Payloads built offline in one pass, then fired with no bash round-trips between them:
5 × `productUpdate` (10 aliased products each: title, descriptionHtml, seo{title,description}, productType, tags =
snapshot ∪ season, category, collectionsToJoin), 2 × `metafieldsSet` (25 CTA metafields each), 8 × `fileUpdate`
(396 media alts, 50 per call). No price and no status mutation (Q2/Q5 keep). **All 15 payloads returned `clean` — 0 userErrors.**
`backup-alt-ddl2-batch8.md` (396 rows) was written to /mnt/user-data/outputs/ and sent to the chat **before** the alt push.

## Step 8 — verification
`shopify_api.py fetch DDL2-Batch8 live_after.json`, then
**`verify.py products.json live_after.json collections.json` → `verify: 50 products, 901 checks, 0 failures` (exit 0)** —
18 checks per product, no `[note]` and no skipped check; collections.json resolved by title on every product.
**`head_check.py live_after.json` → `head-check: 0 FAIL of 50`.**

## For the next run
1. `sections.py` proposed a section on 45 of 50 products in this batch and every one was the supplier's package block or a
   spec-table row written as a short `<h3>`. The two 2026-09-09 shape tests do not catch it (headings are 1–2 words and not at
   index 0). A `extract.package` / `extract.specs` overlap test would; see Step 3 above.
2. Supplier CDN rot is now a live failure mode: 14 of 103 foreign description images were already 404 before we touched them.
   `rehost.py` reports them correctly but has no remedy; the gallery-image substitution used here was a main-context decision.
   Worth a flag in the script's summary line so a future run does not read "14 failed" as something to retry.
3. Two of 50 titles carried an attribute the source never states (p34 clear/stackable, p31 stackable). `title-check.py` cannot
   see this — the words are measured keywords with real volume and they name the same product. The audit that caught them
   (every content word of the new title checked against that product's own source text) is cheap and scriptable.

## coverage.md — extract_check table
| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 01 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 02 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 03 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 04 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 05 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 06 | 4 | 0 | 1 | - | 6 | 1 | 0 | - |
| 07 | 3 | 0 | 2 | - | 7 | 2 | 0 | - |
| 08 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 09 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 10 | 5 | 0 | 0 | - | 5 | 1 | 0 | - |
| 11 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 12 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 13 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 14 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 15 | 5 | 0 | 0 | - | 7 | 2 | 0 | - |
| 16 | 4 | 0 | 1 | - | 5 | 0 | 0 | - |
| 17 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 18 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 19 | 5 | 0 | 0 | - | 9 | 0 | 0 | - |
| 20 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 21 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 22 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 23 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 24 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 25 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 26 | 4 | 1 | 0 | - | 8 | 0 | 0 | - |
| 27 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 28 | 4 | 1 | 0 | - | 7 | 0 | 0 | - |
| 29 | 4 | 1 | 0 | - | 7 | 0 | 0 | - |
| 30 | 1 | 0 | 5 | - | 8 | 0 | 0 | - |
| 31 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 32 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 33 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 34 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 35 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 36 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 37 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 38 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 39 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 40 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 41 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 42 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 43 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 44 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 45 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 46 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 47 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 48 | 6 | 0 | 0 | - | 10 | 1 | 0 | - |
| 49 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
