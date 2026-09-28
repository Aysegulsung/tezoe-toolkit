# Run log — DDL2-Batch7 (Worfa, 2026-09-12)

Brief: Q1 tag DDL2-Batch7 · Q2 keep prices · Q3 none · Q4 no rounding · Q5 keep status · Q6 rewrite titles
(claude/title-format-rule.md) · Q7 rewrite descriptions (description-format-rule.md) · Q8 auto-infer season ·
Q10 manual, user approved the full batch up front (no test product) · Q11 write CTA benefits · Q12 productType +
category per product · Q13 collections per product · Q14 re-host images · Q15 title backup · Q16 alt text ·
Q17 comparison table · Q18 skip dimension image · Q19 fit block.
Result: **verify: 50 products, 901 checks, 0 failures** · `head_check live_after.json: 0 FAIL of 50`.

## Step 0 — toolkit copy
56 files copied by three Sonnet agents; `sha256sum -c MANIFEST.sha256` failed on 4 lines, each resolved per MANIFEST §6:
- `DESC-SPEC.md` — GENUINE COPY CORRUPTION. The second independent copy matched the manifest hash exactly
  (23729e84…); the first copy was discarded.
- `title-check.py` (26ad735d…) and `rules/title-format-rule.md` (8c9ff354…) — STALE MANIFEST LINES. Two
  independent copies agreed byte for byte and both differed from the manifest; both project docs were edited at
  08:15 UTC on 2026-09-12, after the 06:21 manifest refresh. The on-disk manifest was updated with the verified
  hashes for this run; **the project manifest still carries the old lines and needs the same two lines refreshed.**
- `README-toolkit.md` — both copies differed from the manifest AND from each other, in one line each
  (copy 1 dropped "/ Tips" in step 3d, copy 2 turned an em dash into a semicolon in step 5). Merged from the two
  against the version read in the main context; the file is documentation only (no script reads it), so it was
  excluded from the check rather than re-copied a third time.

## Steps 1–3e — fetch and extract
`shopify_api.py shop` → Worfa. brief_flags.json: q17 true, q19 true, q18 false, run_mode manual.
`fetch DDL2-Batch7` → 50 products. `extract_html.py` → 50 skeletons, 50 with foreign images.
`keyfeat_cover --extract` → source Key Features pre-filled · `usage_tips --extract`: 3 of 50 carry a Usage Tips block ·
`sections --extract`: the script proposed a fact section on 45 of 50 and **every one was the supplier's
"What's in the Box?" block, byte-identical to `extract.package`** — the package list's home is the skeleton's
Package Includes section, so all 44 were dismissed by the main context ("package block — home is the skeleton
Package Includes list"). p48's 8 remaining blocks were its own spec-table rows (already `extract.specs` pairs,
same name and value) and were dismissed as "spec table row — home is the Specifications list".
**sections: 0 products with a fact section, 52 dismissed (package duplicate 44, spec rows 8, plus the script's own
62 marketing/lead dismissals), 0 unmapped left, 0 key_features lines moved.** Note for the toolkit: sections.py has
no shape test for a block that merely repeats `extract.package` or `extract.specs`, and `--extract` re-adds the
dismissed blocks if it is run again — do not re-run it after the main-context triage.
Extraction: 5 Sonnet agents × 10 products.
- `para_feat: 59 KF flagged, 0 added, 59 dismissed | 0 SPEC flagged` — every flagged sentence was a restatement of
  an existing key_features line or spec, or an audience/usage sentence; nothing concrete was missing.
- `para_feat --gate`: 0 unruled prose spec figures missing.
- `extract_check --claims`: 2 FAIL on the first pass (p37, p41 each claimed +1 paragraph feature, measured 0 — both
  were rewordings of an existing line, not additions; the claims were corrected with that reason and re-run).
  Final: **0 FAIL across 50; agent additions KF 13, spec 3; main-context additions KF 0, spec 0** (coverage.md below).
- **KF/spec independent review: 2 eligible of 50 (paragraphs > 80 words), 0 marked, 0 confirmed.**
- RULINGS.md written from the agents' notes (8 rulings). Main-context fix in the extract: p45's `Size` pair carried
  only the first of the source's eight sizes — replaced by one `Size Options` pair with all eight, so spec_cover and
  value_check enforce them.

## Step 4 — keywords
`source_windows.py`: 50 titles → 822 windows, 0 dropped over the DataForSEO limit.
`kw_measure.py` over 50 candidate files + the windows: 3,481 raw → 3,116 unique, 0 dropped, **3,116 measured in 5
call(s) over 2 round(s) — 88 word-order variant(s) moved to later rounds** (claude/kw-order-variant-rule.md),
0 not returned, ~$0.45. kw-cache-ddl2-batch7.md went to the chat (not a project doc).

## Step 5 — titles
One title subagent (main model). `title-check.py kw.txt check_products.json` → **0 FAIL**, 60 WARN,
129 MANUAL REVIEW (unused keywords with a written reason in skip_reasons.json — 14 of them, products 07, 09, 14, 18,
23, 31, 34, 35, 37, 42, 47; all §7 head-noun-cap collisions or §2 word-order variants).
`head_check.py titles_final.json` → **0 FAIL of 50**.
Captured volume **6,798,800** across the 50 titles; all 50 in the 70–120 base zone (99–120 chars), no trigger A/B
extension, no extra DataForSEO call needed (every source-title window was already measured).
119 fit rejects ≥20,000 — the large families: different product in the same category (blender 450,000 and coffee
maker 201,000 on the milk maker; robot vacuum cleaner 135,000 and shop vac 110,000 on the wet-dry vacuum; cloud
storage 550,000 on the USB drive; heating pad / foot massager / massage gun 165,000–135,000 on the two massagers;
cast iron skillet 165,000 on the electric grill pan — the one rejection that also cost volume the old title held),
informational intent (classroom game 368,000 on the three reaction games), unsourced attributes (canvas/leather tote
bag 110,000/27,100 on p16 per RULINGS, fleece blanket 33,100 on the blanket hoodie), and one trademark (snuggie 49,500).
**Note: build_check.py's hard-coded FR/EXTRA dicts were left over from a pest-control batch and matched none of
these products; the title agent moved them to fr.json / extra.json and wrote this batch's own patterns.**
backup-titles-ddl2-batch7.md written to the project BEFORE any push.

## Step 5b — image re-host (Q14)
`rehost.py`: 100 foreign images, **99 mapped, 99 srcs rewritten**. One failed permanently: p46's first description
image was an animated .gif on ANOTHER store's CDN and the URL is **dead (HTTP 404)** — Shopify answered
`fileCreate` with "Media processing failed" on two separate attempts. A dead link cannot be re-hosted and must not be
published, so the main context replaced that one src with the product's own gallery image 1 (recorded in
extract/p46.json `notes` and in the final's notes_for_log): the description still carries two images, no source image
was deleted, and the re-run reported **0 still foreign**.

## Step 6 — descriptions
5 Sonnet agents × 10 products; every agent returned CLEAN on the first pass and the main context re-ran
`gate.py` over all 50: **=== gate: CLEAN ===**. All 50 carry a comparison block (Q17) and a fit block (Q19);
no `compare: null`, no `fit: null`. Seasons: evergreen 41, winter 6, summer 2, fall 1. 7 omit_per_ruling entries.

**Toolkit bug found and fixed locally (needs the same fix in the project): unit_dual.py converted the product claim
"3 In 1" as three inches** — p17's `Product Type: 3 In (7.6 cm) 1 Dog Jacket…` and p18's Key Features lead-in
`3 In (7.6 cm) 1 Floor Cleaning` reached the finals that way, and because the conversion runs inside gate.py it came
back on every gate run. `_skip()` now skips an `in` whose figure is a bare 1–2-digit integer immediately followed by
another bare integer (N-in-1 claims), leaving `Fits 6 in photos`, `Head 18 in long` and `13 in / 33 cm` untouched.
Both finals were repaired and re-gated CLEAN.

## Step 6b / 6c / 6d — reviews
- `fact_cover.py` before corrections: 676 source fact lines scored, **1 below 55%** (p48 "Stable Build & Grip" —
  present in the comparison block and the Key Features list in other words; category (b), no correction).
- **6c read on all 50 products** (H2, five bullets, three CTA lines, five comparison rows, four fit lines).
  Corrected: H2 on p40 (it opened as a sentence, "Wear Your Service Proudly:", instead of a keyword headline);
  benefit bullets on p01 p03 p05 p07 p08 p09 p12 p14 p15 p16 p17 p24 p26 p27 p28 p29 p30 p31 p36 p38 p39 p40 p41
  p42 p43 p44 p45 p46 p48 p49 (audience, occasion, gift, aesthetics and variant-fact bullets).
- **KF read on all 50 products: copies 0 (keyfeat_cover), every source line present as its own item, paragraph
  additions on 13 products.**
- **CTA read on all 50 products, corrected: p01 p03 p05 p06 p07 p08 p09 p12 p14 p16 p17 p18 p19 p24 p26 p27 p28
  p30 p32 p33 p35 p37 p40 p41 p42 p43 p44 p45 p48 p49.**
- **CTA independent review: 45 marked, 40 confirmed and corrected, 5 dismissed** (p18 "Brush roll rinses itself",
  p22 "Follow lyrics on your tablet", p32 "Pick your length, trim it neat", p42 "Smooths edges after trimming",
  p19 partially — each of those reads as a problem the shopper no longer has).
- 6b + 6c went back to each agent in ONE message (6d). After the round: `gate.py` over 50 CLEAN, and
  `fact_cover.py` re-run → **2 below 55%** (the p48 line again plus p46 "Secure Hold", which the description carries
  as "the secure hold keeps your things from shifting or falling out" — category (b) again, no correction).
- **The changed lines were then re-read by eye**, and the drift that word matching cannot see was caught and sent
  back a second time: duplicate bullet pairs on p14 p15 p16 p17 p40 p41 p49, and two **unsourced claims** the
  corrections had introduced — "edges stay finished, not fraying" (p24 bullet) and "No loose or fraying edges" /
  "No fraying at the edges" (p26 bullet + CTA): neither source mentions fraying, only a fringe or tassel trim.
  A third micro-pass removed comparison framing from p41 ("Not just a flat, foggy piece of plastic") and an
  unsourced "bold and clear" from p49. Final state: `gate.py` over 50 CLEAN.

## Step 7 — push
`dim_keep: 0 restored, 0 warned, 50 untouched` (Q18 = Skip; no live product carried a vp-dim image).
Q13: no apparel collection existed among the store's 24, so **one new collection "Apparel & Loungewear"
(gid://shopify/Collection/485157896228) was created** and assigned to p07 and p15; the agents' two separate NEW
proposals were merged into it. Every other product joined existing collections.
Q12: productType set on all 50; **category resolved against the Shopify taxonomy for 49** — the first search pass
returned plainly wrong leaves for 12 products (Christmas Tree Stands for the reindeer set, Karaoke Chips for the
karaoke machines, Quivers for the quilt cover set, Hand Carders for the hand warmer, pet Hammocks for the hammock
chair, Toy Helicopters for the toy car, Vehicle Soft Tops for the phone mount, …), so each was re-searched and
chosen by name. **p13 (rechargeable electric hand warmer) is KEEP: the taxonomy's only hand-warmer leaf is
"Chemical Hand Warmers", which this product is not** — an open item, not an oversight.
backup-alt-ddl2-batch7.md (504 rows, old alt → new alt) went to the chat BEFORE the alt push.
Payloads: 5 × aliased productUpdate (title, descriptionHtml, seo.title + seo.description together, tags =
snapshot ∪ season, productType, category, collectionsToJoin; no status and no variant price — Q5 and Q2 keep),
2 × metafieldsSet (custom.cta_benefits, 25 each), 21 × fileUpdate (504 alts, 25 each).
All 28 mutations returned clean, 0 userErrors.

## Step 8 — verification
`verify.py products.json live_after.json collections.json` → **verify: 50 products, 901 checks, 0 failures**,
exit 0, no `[note]` lines (collections.json resolved). `head_check.py live_after.json` → **0 FAIL of 50**.
Alt texts: 504 pushed, all unique across the batch, none over 125 characters.

## coverage.md (extract_check) — KF and Specifications per product

| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 01 | 4 | 1 | 0 | - | 6 | 0 | 0 | - |
| 02 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 03 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 04 | 5 | 0 | 0 | - | 10 | 0 | 0 | - |
| 05 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 06 | 5 | 0 | 0 | - | 7 | 1 | 0 | - |
| 07 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 08 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 09 | 5 | 0 | 0 | - | 10 | 0 | 0 | - |
| 10 | 4 | 0 | 0 | - | 15 | 0 | 0 | - |
| 11 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 12 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 13 | 3 | 0 | 0 | - | 10 | 0 | 0 | - |
| 14 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 15 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 16 | 5 | 0 | 0 | - | 0 | 1 | 0 | - |
| 17 | 4 | 0 | 0 | - | 6 | 0 | 0 | - |
| 18 | 5 | 1 | 0 | - | 5 | 0 | 0 | - |
| 19 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 20 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 21 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 22 | 4 | 2 | 0 | - | 11 | 0 | 0 | - |
| 23 | 4 | 2 | 0 | - | 9 | 0 | 0 | - |
| 24 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 25 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 26 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 27 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 28 | 5 | 0 | 0 | - | 11 | 0 | 0 | - |
| 29 | 5 | 1 | 0 | - | 8 | 0 | 0 | - |
| 30 | 5 | 2 | 0 | - | 7 | 0 | 0 | - |
| 31 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 32 | 4 | 1 | 0 | - | 6 | 0 | 0 | - |
| 33 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 34 | 5 | 0 | 0 | - | 10 | 0 | 0 | - |
| 35 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 36 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 37 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 38 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 39 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 40 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 41 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 42 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 43 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 44 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 45 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 46 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 47 | 5 | 1 | 0 | - | 5 | 0 | 0 | - |
| 48 | 4 | 2 | 0 | - | 12 | 1 | 0 | - |
| 49 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |

## For the next run
1. **Refresh two manifest lines in the project**: `./title-check.py` → 26ad735d271e55c2cba847c356123f5f38e1cf072171e2ba07be4589c9324bad,
   `./rules/title-format-rule.md` → 8c9ff354b4da2f61807966834d0659d1873367d197c8b0ab2a256edcf737e187 (both verified
   by two independent copies). `./README-toolkit.md` should be re-hashed from a verified copy as well.
2. **unit_dual.py**: apply the N-in-1 fix above in the project copy, or every batch with a "3 in 1" product will
   publish "3 In (7.6 cm) 1" unless the main context catches it by eye.
3. **sections.py**: add a shape test that dismisses a block whose lines duplicate `extract.package` or
   `extract.specs` (45 of 50 products here), and note in the README that `--extract` must not be re-run after the
   main-context triage — it re-adds every dismissed block.
4. **build_check.py** shipped with another batch's FR/EXTRA patterns; consider keeping them in fr.json / extra.json
   in the project copy so a stale list cannot silently apply to the wrong batch.
5. p46's dead supplier .gif is a class worth checking earlier: rehost.py could HEAD-check a foreign URL and report a
   404 as "dead link" rather than as a Shopify media failure.
