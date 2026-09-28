# run-log-ddl2-batch6 — Worfa, 2026-09-12

Brief: Q1 By Tag `DDL2-Batch6` (50 products) · Q2 keep prices · Q3 none · Q4 no rounding · Q5 keep status ·
Q6 rewrite titles (Q9 = title-format-rule.md, 70–120) · Q7 rewrite descriptions (description-format-rule.md) ·
Q8 auto-infer season · Q10 **manual, user approved the full batch** · Q11 write CTA benefits ·
Q12 productType + category per product · Q13 collections per product · Q14 re-host images · Q15 title backup ·
Q16 add alt text · Q17 add comparison table · Q18 **skip** dimension image · Q19 add fit block.

`brief_flags.json` = `{"q17_compare_table": true, "q19_fit_block": true, "q18_dimension_image": false, "run_mode": "manual"}`

## 0. Toolkit copy
55 of 57 manifest lines OK on the first copy. Two FAILED and were resolved per MANIFEST §6 as **STALE manifest
lines, not corrupted copies**: `./rules/title-format-rule.md` (`8c9ff354…`, 42,828 bytes) and `./title-check.py`
(`26ad735d…`, 21,317 bytes). Two independent copy agents produced byte-identical files for both, and both project
docs were edited at 08:15 UTC on 2026-09-12 — after the manifest's 06:21 refresh. **Both lines need recomputing in
toolkit/MANIFEST.md** (not done in this session — open item).

## 1–2. Store + fetch
`shopify_api.py shop` → Worfa. `fetch DDL2-Batch6` → 50 products, all `DRAFT`, tags `["DDL2","DDL2-Batch6"]`,
`seo.title` / `seo.description` empty on every product, `category` null on every product.

## 3. Extraction
`extract_html.py` → 50 raw/ + extract/ skeletons, 50 with foreign images.
`keyfeat_cover.py --extract`, `usage_tips.py --extract` (2 of 50 carry a Usage Tips block), `sections.py --extract`.

**sections: 0 products with 0 sections, 66 blocks dismissed by the script (marketing 0 / policy 0 / description
lead 18 / long marketing heading 48), 41 UNMAPPED headings resolved by the main context — all 42 proposed sections
removed as duplicates: 40 were the source's "What's in the Box?" block, line-for-line identical to
`extract.package` (the skeleton already carries Package Includes), and 2 were p49's "Interior" and "Material"
blocks, every line already an `extract.specs` pair.** This is the first batch since 2026-09-08 where the whole
section proposal was duplicate-of-an-existing-field; the shape tests did their job on marketing headings, but the
"What's in the Box?" family is a *package* duplicate the script has no test for — worth a `sections.py` guard.

5 Sonnet extraction agents × 10 products. `extract_check.py` → **0 FAIL across 50; agent additions KF 12, spec 37;
main-context additions KF 0, spec 0.** Eight claim lines were reconciled by the main context to the measured
counts (p32–p35 / p38 restored colon-less source spec-table rows and reported them as "restored" rather than
"added"; p11 / p15 / p47 claimed a line that was already in the script baseline).

**para_feat: 67 KF flagged, 0 added, 67 dismissed | 1 SPEC flagged, 0 added, 1 dismissed.** Every flagged sentence
restates a feature already in `extract.key_features` or a value already in `extract.specs`; the SPEC flag was
`2 in` from "magnetic 2 in 1 hand warmer design" (p40) — a product-name phrase, ruled out in `rulings_omit.json`.
`para_feat.py --gate` → 0 unruled prose spec figures.

**KF/spec independent review: 0 eligible of 50 (min 80 words), 0 marked, 0 confirmed, 0 dismissed.**

## 4. Keywords
`source_windows.py` → 902 windows from 50 titles, 1 dropped over the DataForSEO limit (the p17 bra title).
`kw_measure.py` over candidates/ ∪ source_windows → **3,301 raw → 3,131 unique, 3,131 measured in 6 call(s) over
3 round(s) — 73 word-order variant(s) moved to later rounds** (kw-order-variant-rule.md). 0 not returned,
0 dropped oversize, ~$0.54. Cache sent to the chat as `kw-cache-ddl2-batch6.md` (not a project doc since 2026-09-08).

## 5. Titles
One title subagent per TITLE-SPEC.md. **`title-check.py`: 0 FAIL, 66 WARN, 111 MANUAL REVIEW.
`head_check.py`: 0 FAIL of 50.** `skip_reasons.json`: 6 entries (p03, p05, p31, p42).
Main-context eye check on the numeric/material claims in the new titles: p13 "24 Piece" = spec `Total Containers`,
p19 "12 Inch" = the variant `30 cm / 12 inch`, p26 "6 ft" = spec `Size`, p30 "10.1 Inch" = spec `Screen Size`,
p40 "4 Heat Settings" = spec `Heating Levels`, p42 "Snowflake" = the variant name — all sourced.
p19's title says **stainless steel**, not titanium (spec table `304 Three Layer Steel Plate`).
`claude/backup-titles-ddl2-batch6.md` written to the project BEFORE the push.

## 5b. Image re-host (Q14)
`rehost.py`: 96 mapped, 4 failed in one pass. All 4 recovered by the main context — **100 of 100 description
images are on the Worfa CDN, 0 foreign**:
- p07 ×2 — the source `src` carried HTML entities (`&amp;`); `fileCreate` rejects that URL. Unescaped, re-created, READY.
- p09 ×1 — `.avif`, `UNSUPPORTED_IMAGE_FILE_TYPE`. Downloaded, converted to JPEG, `stagedUploadsCreate` +
  `fileCreate` (the staged PUT works from this container — confirms the 2026-09-09 finding).
- p00 ×1 — the supplier `src` is a **dead link** (HTTP 404 on the previous store's CDN, with and without the query
  string). It can never be re-hosted and would render as a broken tag, so it was replaced with p00's own gallery
  image #3. Image count and position unchanged.
**For the next run:** `rehost.py` should `html.unescape()` every src before `fileCreate` (3 of the 4 failures were
avoidable), and should report a dead source URL separately from a processing failure.

## 6. Descriptions
5 Sonnet agents × 10 products per DESC-SPEC.md. `gate.py` over all 50 → **`=== gate: CLEAN ===`**
(compare-build, fit-build, list-bold, struct-check, spec-cover, unit-dual, keyfeat-cover, value-check,
assume-check, age-check, cta-check, howto-check, usage-tips, sections, title-check all 0 FAIL).

## 6b. Fact coverage
`fact_cover.py`: **639 source fact lines scored, 2 below 55%** — p03 "Hanging Storage Hole…" and p40 "Four
Adjustable Heat Levels…". Both are case (b), the same meaning in different words: read in the live copy, each
appears in a bullet, the comparison table, the Specifications list, the fit block and an FAQ answer.
**0 genuinely missing, 0 sent back.** Re-run after the 6c corrections: **identical to the first run, 0 new flags.**

## 6c. Benefit review by eye
**6c read on all 50 products** (H2 + 5 bullets + 3 CTA lines + 5 comparison rows + 4 fit lines).
**KF read on all 50 products: copies 0 (keyfeat_cover), paragraph additions on 12 products.**
**CTA read on all 50, corrected: p07 p11 p18 p27 p28 p29 p31 p33 p36 p37 p42 p43 p46 p47.**
**CTA independent review: 17 marked, 15 confirmed and corrected, 2 dismissed** (p34 "Built to reuse every year" —
the source's "solid build supports repeated seasonal display" carries it; p43's material list was traceable, but it
was corrected anyway as a capability line rather than a problem removed).
Main-context finds beyond the reader's marks:
- p09 bullet 3 and p45 bullet 5 both claimed "use for weeks" — the sources state **no** runtime, battery life or
  hours at all. Rewritten to the rechargeable battery / USB charging the sources do state.
- p47 claimed a lifespan in three places ("keeps its shine for years", "for years of display", "survive years on a
  desk"). The source's only "years" sentence is about the *moment* being easy to remember. All three rewritten.
- p33 comparison row 5 paired the feature "Runs on batteries, ready for another dance" with an Others cell reading
  "1 color" — two different subjects, so the row was untraceable. Rewritten.
- p18's first CTA replacement introduced a **new** unsourced claim ("No bending down to put on"): the p18 source
  never says slip-on / step-in / no-fastening anywhere. That line and the matching comparison row were sent back a
  second time. Worth remembering: a correction round can add a claim the first pass did not have.
Re-read by eye of every line the corrections changed: no meaning drift, no further correction.

**Files clobbered by an agent, caught by the main context:** the p40–p49 agent's correction round reverted
`collections` and `category_proposal` to null on all ten of its files — exactly the DESC-SPEC 2026-09-07 failure
mode. Restored from `category_map.json` before the payload build and re-verified; the 6c edits themselves survived.

## 7. Push
`dim_keep.py`: **0 restored, 0 warned, 50 untouched** (Q18 skipped, and no product carried a live `vp-dim` image).
Payloads built offline in one pass: 5 × `productUpdate` (10 aliased each: title, descriptionHtml, seo{title,
description}, productType, category, tags, collectionsToJoin), 2 × `metafieldsSet` (25 each, `custom.cta_benefits`,
`list.single_line_text_field`), 9 × `fileUpdate` (439 media alts, 50 per call). No `productVariantsBulkUpdate`
(Q2 keep prices) and no `status` (Q5 keep status).
Pre-push script check: 439 alts, every one unique inside its product and across the batch, all ≤125 characters;
every `seo.title` < 70 and `seo.description` < 160.
`backup-alt-ddl2-batch6.md` written to /mnt/user-data/outputs and sent to the chat BEFORE the alt push.
**All 16 mutation files: clean, 0 userErrors.**

### Q12 category (Shopify Standard Product Taxonomy)
48 of 50 resolved to a taxonomy node and pushed. Three have no honest leaf and use the nearest correct parent:
p09 `Night Lights & Ambient Lighting` (its leaves are Lava Lamps / Night Light Projectors / Salt Lamps),
p26 `Seasonal & Holiday Decorations` (no inflatable leaf), p27 `Motor Vehicle Lighting` (leaves are Fog Lights /
Headlights / Light Bars / Light Bulbs / Light Covers / Light Switches / Tail Lights / Turn Signals).
**p39 and p40 are `KEEP`** — the only hand-warmer leaf in the taxonomy is `Chemical Hand Warmers`, and both are
*electric rechargeable* warmers, so no category was set rather than a wrong one. p48 (disposable, air-activated) is
correctly `Chemical Hand Warmers`.

### Q13 collections
24 existing Worfa collections were not enough — the batch is a third apparel and footwear. **Four new collections
created:** `Women's Clothing` (485154357284), `Footwear` (485154390052), `Winter Essentials` (485154422820),
`Christmas & Holiday` (485154455588). Every product joined 1–3 collections; `collections.json` on disk now has 28.

## 8. Verification
`shopify_api.py fetch DDL2-Batch6 live_after.json` → 50 products.
**`verify: 50 products, 901 checks, 0 failures`.**
**`head_check.py live_after.json` → 0 FAIL of 50.**
Live spot check on p00: title, productType `Can Opener`, category `Can Openers`, tags
`["DDL2","DDL2-Batch6","evergreen"]`, collection `Kitchen & Dining`, `custom.cta_benefits` rendering three lines,
media alts written, seo 63 / 113 characters.

## Open items for the next run
1. **`toolkit/MANIFEST.md`**: recompute the `./rules/title-format-rule.md` and `./title-check.py` lines
   (`8c9ff354b4da2f61807966834d0659d1873367d197c8b0ab2a256edcf737e187` and
   `26ad735d271e55c2cba847c356123f5f38e1cf072171e2ba07be4589c9324bad`) — verified stale, not corrupted.
2. **`rehost.py`**: `html.unescape()` the src before `fileCreate`, and report a dead source URL (HTTP 404) as its
   own outcome instead of a generic "Media processing failed".
3. **`sections.py`**: dismiss a proposed section whose lines are already `extract.package` or `extract.specs` —
   40 of 42 proposals in this batch were the "What's in the Box?" package block.
4. **DESC-SPEC read-modify-write rule**: a correction round wiped `collections` / `category_proposal` on 10 files
   again. A `gate.py` check that FAILs a final whose `collections` was set and then emptied would catch it.
5. The Shopify taxonomy has no **electric** hand-warmer leaf (p39, p40 left `KEEP`).

## Source conflicts resolved silently (RULINGS.md)
p19 titanium vs `304 Three Layer Steel Plate` (steel wins) · p17 Supima Cotton vs "Smooth" on one colorway ·
p42 variant 9.3×7.6 cm vs spec 9.6 cm (table wins) · p44 style options vs colour variants ·
p48 boilerplate electronics spec rows · p20 no certified-safety-shoe claim · p41 no "platform shoes" claim ·
p47 productType misspelled "Thropy" in the source · p24 Size/Weight explicitly "Not Specified".

## coverage.md (extract_check.py)
| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 2 | 2 | 0 | - | 5 | 0 | 0 | - |
| 01 | 5 | 1 | 0 | - | 6 | 0 | 0 | - |
| 02 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 03 | 5 | 1 | 0 | - | 6 | 0 | 0 | - |
| 04 | 5 | 0 | 0 | - | 3 | 0 | 0 | - |
| 05 | 5 | 0 | 0 | - | 9 | 0 | 0 | - |
| 06 | 5 | 1 | 0 | - | 0 | 0 | 0 | - |
| 07 | 5 | 0 | 0 | - | 3 | 0 | 0 | - |
| 08 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 09 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 10 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 11 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 12 | 5 | 1 | 0 | - | 7 | 0 | 0 | - |
| 13 | 5 | 1 | 0 | - | 6 | 0 | 0 | - |
| 14 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 15 | 5 | 1 | 0 | - | 5 | 0 | 0 | - |
| 16 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 17 | 5 | 1 | 0 | - | 0 | 0 | 0 | - |
| 18 | 5 | 1 | 0 | - | 0 | 0 | 0 | - |
| 19 | 4 | 0 | 0 | - | 5 | 0 | 0 | - |
| 20 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 21 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 22 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 23 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 24 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 25 | 4 | 1 | 0 | - | 6 | 0 | 0 | - |
| 26 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 27 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 28 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 29 | 4 | 1 | 0 | - | 12 | 0 | 0 | - |
| 30 | 5 | 0 | 0 | - | 10 | 0 | 0 | - |
| 31 | 5 | 0 | 0 | - | 6 | 1 | 0 | - |
| 32 | 5 | 0 | 0 | - | 0 | 5 | 0 | - |
| 33 | 5 | 0 | 0 | - | 0 | 6 | 0 | - |
| 34 | 5 | 0 | 0 | - | 0 | 7 | 0 | - |
| 35 | 5 | 0 | 0 | - | 0 | 10 | 0 | - |
| 36 | 5 | 0 | 0 | - | 9 | 0 | 0 | - |
| 37 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 38 | 5 | 0 | 0 | - | 0 | 8 | 0 | - |
| 39 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 40 | 4 | 0 | 0 | - | 7 | 0 | 0 | - |
| 41 | 5 | 0 | 0 | - | 0 | 0 | 0 | - |
| 42 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 43 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 44 | 4 | 0 | 0 | - | 5 | 0 | 0 | - |
| 45 | 4 | 0 | 0 | - | 6 | 0 | 0 | - |
| 46 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 47 | 5 | 0 | 0 | - | 4 | 0 | 0 | - |
| 48 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 49 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
