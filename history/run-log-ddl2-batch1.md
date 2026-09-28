# Run log — DDL2-Batch1 (Worfa, 2026-09-10)

Store **Worfa** (`ymjviw-rz.myshopify.com`), tag `DDL2-Batch1`, **50 products**. **First full batch on Worfa** after the
2026-09-10 store change from Vepine.
Brief: Q1 by tag · Q2 keep prices · Q3 none · Q4 no rounding · Q5 keep status · Q6 rewrite titles (Q9 = title-format-rule.md) ·
Q7 rewrite descriptions · Q8 auto-infer season · Q10 approved, full batch (manual) · Q11 CTA benefits · Q12 productType +
category per product · Q13 collections per product · Q14 re-host to our CDN · Q15 title backup · Q16 alt text ·
Q17 comparison table · Q18 **skip** dimension image · Q19 fit block.

**Result: pushed and verified — `verify: 50 products, 901 checks, 0 failures`, `head-check: 0 FAIL of 50`, no `[note]` lines.**
Prices and status were not touched (Q2 / Q5 = keep).

## Step 0 — toolkit copy
54 files copied by 3 Sonnet agents, then `sha256sum -c MANIFEST.sha256` → **TOOLKIT OK on the first pass** — no FAILED line,
so no stale-vs-corrupt investigation was needed. This is the first run against the 2026-09-10 Worfa manifest refresh.

## Steps 1–3e — fetch and extraction
- `brief_flags.json`: q17_compare_table true, q19_fit_block true, **q18_dimension_image false**, run_mode manual.
  rembg/onnxruntime NOT installed (Q18 skipped).
- `shopify_api.py shop` → **Worfa**. 50 products fetched; the 24 Worfa collections in `collections.json` covered every
  proposal, so **no new collection was created**.
- **Images: 110 foreign images across all 50 products** — `rehost: 110 mapped, 0 failed, 110 srcs rewritten, 0 still foreign`.
  Every description image is now on `cdn.shopify.com/s/files/1/0786/1269/3028/`.
- `usage_tips --extract`: **0 of 50** products carry a Usage Tips block.

### sections.py — 71 proposed, 0 real, all 194 lines reclassified by the main context
This is the second live run of `sections.py` after the 2026-09-09 shape tests, and it still proposed a section on 46 of 50
products. **Every one of the 71 proposed sections was a misdetection**, in three families:
- **40 × "Why You'll Love It"** — the supplier's OWN Key Features list under a marketing heading. The script had *moved 90
  key_features lines into it*, which would have published `<h3>Why You'll Love It</h3>` and emptied the Key Features list.
- **6 × "What's in the Box?"** — the Package Includes block.
- **25 × single spec rows** — `Voltage`, `Colour`, `Material`, `Size`, `Design`, `Style`, `Bluetooth Version`,
  `Battery Capacity`, `Audio Drivers`, `Water Absorption`, `Application`, `Use` … several already auto-mapped to a canonical
  heading (`Size Guide` over "46 × 23 cm", `Materials` over "Acacia Wood", `Charging` over a battery row), which would have
  published one-line `<h3>` sections duplicating the Specifications list.

The shape tests catch a long marketing HEADLINE, but `Why You'll Love It` is four words and passes `MAX_HEAD_WORDS`, and a
spec row's name is one word. Main-context resolution: **194 lines moved back into `key_features` (123 of them net of the
script baseline), the box lists merged into `package`, all 71 sections dropped**, `extract.sections` empty on all 50, and
23 heading-junk lines (`Why You'll Love It`, lead headlines like "A Timeless Glow for Modern Interiors") removed from
`key_features`. Four products (p00, p03, p26, p27) had had their whole feature list *dismissed* rather than sectioned and
were left with one junk line each; their 5–6 real lines were restored from `sections_dismissed`. Final Key Features:
**244 source lines, min 4 per product, none under 3.**

### Extraction agents
5 Sonnet agents × 10 products. **`extract-check: 0 FAIL across 50 products; agent additions total KF 11, spec 246;
main-context additions KF 123, spec 0`.** The first `extract_check` run showed 37 FAILs; every one was an accounting
artefact of the section reclassification above (the script's `_base` baseline still holds the pre-`sections.py`
`key_features`), plus a counting-convention difference — the agents did not count *splitting a run-on spec line* as
"prose spec pairs added", and 13 of these sources write their entire spec block as ONE run-on sentence inside `facts`
(`Type: … Material: … Craftsmanship: …`), which the parser leaves as `specs: 0`. The 246 agent spec pairs are overwhelmingly
that split; p03, p26 and p27 went from **0 to 6 / 13 / 13** spec pairs. Main-context moves were recorded in
`para_feat_added.json` and the claims aligned to the measured counts, after which the check is clean.

- **para_feat: 65 KF flagged, 0 added, 65 dismissed | 0 SPEC flagged.** Every KF flag was the supplier's lead intro paragraph
  restating a line the Key Features list already carries; the ~14 that named a concrete feature (40 mm drivers, 400 mAh /
  USB-C, Type-C rechargeable, foldable book shape, three light modes, five compartments, 360° rotation, IPS display) were
  each checked against that product's `key_features` + `specs` and found already present. `para_feat --gate: 0 unruled prose
  spec figure(s) missing from extract.specs`.
- **KF/spec independent review: 24 eligible of 50, 3 marked (0 KF, 3 SPEC), 2 confirmed and added (p05 and p22
  `Shape: Mushroom-shaped` — a categorical product attribute the source states and neither list carried), 1 dismissed**
  (p09 `Finish: Glossy` — a descriptive adjective, not a spec value).

### Rulings (RULINGS.md) — 13 contradictions
Standing principle set for this batch: **the variant list is what a customer can actually buy, so it wins over the
supplier's spec-table colour/option line**; the spec table wins over marketing prose on material.
Omissions pushed as `omit_per_ruling`: p12 `Beige`, p15 the `4-Peg or 5-Peg Design` option (only one variant ships, so which
one cannot be established), p17 `Brown`, p23 `natural cotton texture` / `eco-friendly fibers` (the spec table says 100%
acrylic), p36 the third `neutral white` light colour (spec table and variants both offer two), p38 `Black`, p43
`Mint Green` / `Dark Green`.
No-omission rulings: p21, p27, p31 (variant colours / the 2-piece pack count written from the variants), p26 (frosted =
finish, ivory = colour, not a conflict), p47 (the spec colour phrase is the board's *design*, the variants are the colours).
**p42: `productType` corrected from "table lamp" to "wall lamp"** — the source title, headings and Specifications all
describe a wall sconce. The title head noun (`Wall Sconces Modern`) and the category proposal follow the correction.

## Step 4 — keyword measurement
`source_windows.py` emitted 916 windows (over-limit whole-title windows dropped as unmeasurable, as designed).
Candidates ∪ windows = **2,648 unique measurable keywords, measured in 3 DataForSEO calls** ($0.27), all three returning a
non-empty result array; 1,863 came back with volume, 0 not returned, 0 dropped oversize. The title step needed no extra call.
Cache: `kw-cache-ddl2-batch1.md` (sent to the chat, not a project doc).

## Step 5 — titles
One title subagent on the main model, whole batch in one context (50 products fitted inside the output cap this time).
```
title-check — 50 products, 2648 measured keywords
summary: 0 FAIL, 64 WARN, 161 MANUAL REVIEW
head-check: 0 FAIL of 50
```
**Total captured volume 7,483,600.** Tiers: **47 in the 70–120 band, 3 in 120–135 with trigger A named** (p10 121ch
`housewarming gift` 60,500 · p14 122ch `bedside lamp` 22,200 · p40 126ch `wax warmer` 27,100), none over 135, none under 70.
Ten skip reasons recorded in `skip_reasons.json` (mostly 4th-head-noun-occurrence caps and 120–135 tier budget).
Two non-blocking WARNs: p05 and p37, where the old title captured more *total* measured volume — in both cases the
difference is non-product parent volume and the product-naming gate passed.

Notable fit rejections (≥20,000 or >50% of capture), each with the reason: p00 `earbuds` 165,000 / `gaming headset` 74,000
(in-ear and gaming forms; this is an over-ear headphone) · p03 `tiffany lamp` 74,000 (leaded-shade lamps, not a stacked-book
lamp) · p07 `sunrise alarm clock` 49,500 (no wake-up light) · p11 `laundry mat` 823,000 (a laundromat query) · p20
`outdoor rug` 110,000 / `bathroom mat` 74,000 (a 45×75 cm half-round doormat) · p30/36/37/38/41/42 `floor lamp` 165,000 /
`table lamp` 60,500 / `ceiling light` 60,500 (hard-wired wall sconces) · p40 `flameless candle` 22,200 (a warmer for real
candles) · `night light` 40,500 on six decorative table lamps.

`backup-titles-ddl2-batch1.md` was written to the project BEFORE the push.

## Step 6 — descriptions
5 Sonnet agents × 10 products, each to `gate.py` CLEAN; the main context re-ran `gate.py` over all 50 →
**`=== gate: CLEAN ===`** (exit 0) before payloads and again after every correction round.

**6b — fact_cover: 45 lines under 55%, 2 genuinely missing, 43 dismissed.** The two: p02's use-context list (the copy carried
desk / bedside / café / patio but never living rooms, home offices, restaurants or workspaces) and p15's (entryway and
mudroom were there, bathrooms and bedroom walls were not). Both were sent back and woven in. Of the 43 dismissed, ~15 are
the supplier's marketing headings ("Sleek, Versatile & Effortlessly Stylish", "A Creative Glow That Moves With You"),
and the rest are audience/room lines already carried in the writer's own words — several score low only because the source
says "Australian homes", which is deliberately never written on a USD store.

**6c — benefit review by eye, read on all 50 products** (H2 + 5 bullets + 3 CTA lines + 5 comparison rows + 4 fit lines each).
Corrected: p02 p03 p04 p07 p08 p09 p10 p12 p13 p15 p16 p17 p18 p19 p22 p23 p24 p26 p27 p28 p31 p32 p36 p37 p39 p41 p42 p43 p47 p49.
The recurring faults were: "for years" durability outcomes the source never states (p02, p15); a comparison clause inside a
bullet ("few table lamps let you sculpt the glow like this", p13, p16); variant/colour facts used as a benefit bullet or a
CTA line (p12, p39, p41, p17, p31); audience/gift lines with no problem solved (p10, p03); aesthetics-only CTA lines (p16,
p18, p24, p37); a price implication the source never makes (p22, "a gift that looks like it cost more"); an invented claim
(p04, "no wrapping needed"); duplicated proof across two fit lines (p23, p27); and **p36, where a CTA line and a fit line
turned the source's "CCC and CE certified" into "Certified safe for your wall"** — a certification is not a safety claim.
**KF read on all 50 products: copies 0 (keyfeat_cover), paragraph additions on 11 products.**
**CTA read on all 50, corrected: p03 p04 p07 p08 p09 p16 p17 p18 p19 p24 p26 p28 p31 p32 p36 p37 p41 p42 p49.**
**CTA independent review: 11 marked, 11 confirmed and corrected (p03 p07×3 p08 p17 p19 p24 p26 p28 p49), 0 dismissed.**
p07 had all three CTA lines fail at once and was rewritten in full.

**6d — both lists went to each agent in ONE message.** After the round: gate re-run over all 50 → CLEAN; fact_cover re-run
and diffed against the first — p02 and p15 resolved, one new flag on p22 (an audience line the bullet-5 rewrite dropped,
checked by hand: bedside, gift and vintage all still present in the copy).
**The main context then re-read by eye every line the corrections changed**, and that read caught seven replacements that had
swapped one violation for another, needing two short extra rounds: p22's new bullet 5 was a colour variant fact, p26's
"Outlasts a flimsy fixture" and p28's "Won't dim or burn out fast" were comparisons (and p28's an unsourced durability
outcome), p31's "Retro charm, modern glow" was pure aesthetics, p43's replacement duplicated bullet 2's raised-legs content
and claimed "won't tip over", and p04 / p09 were replaced twice — first with an invented "handmade" claim and an aesthetics
line, then with "Won't feel cheap or flimsy" / "Won't feel like cheap plastic", which are comparisons to a cheap alternative.
All were rewritten off source facts. **This is the step that earns its cost: none of the seven would have been caught by any
gate.** p47's season was also changed from `summer` to `evergreen` — a resin/acacia cutting board is a year-round item and
its sibling p48 was already evergreen.

## Step 7 — push
`dim_keep: 0 restored, 0 warned, 50 untouched` (no product carried a Q18 image from an earlier batch).
All payloads built offline in one pass, then fired with no round-trips: **5 × aliased `productUpdate` (10 products each),
2 × `metafieldsSet` (25 CTA metafields each), 8 × `fileUpdate` (399 alts, 50 per call). All 15 files returned clean.**
Every payload carried BOTH `seo.title` and `seo.description` (the 2026-09-05 whole-object rule); asserted before the push,
along with title 70–135, SEO 70/160, no `status`, no `variants`, a real taxonomy gid and at least one collection per product.
- **Seasons: 49 evergreen, 1 winter** (p14, the Nordic candle warmer lamp).
- **Categories: 50 set, 0 KEEP — every product in this batch had NO category at all before the run** (`extract.category` was
  `None` on all 50). Six agent proposals were leaf names Shopify's taxonomy does not carry and were resolved against the live
  taxonomy before the push, with `category_proposal` updated in the doc so verify compares like with like:
  Wall Lights & Sconces / Wall Lamps / Wall Lights → **Wall Light Fixtures** (12 products), Doormats → **Door Mats**,
  Candle Warmers → **Candle & Oil Warmers**, Headphones → **Over-Ear Headphones**, Landscape Lighting → **Landscape Pathway
  Lighting**, Key Racks and Coat Racks & Umbrella Stands → **Coat & Hat Racks**, Bath Mats → **Bath Mats & Rugs**,
  Tapestries → **Decorative Tapestries**, Trash Cans & Recycling Bins → **Trash Cans**.
  Final spread: Table Lamps 15 · Wall Light Fixtures 12 · Door Mats 4 · Candle & Oil Warmers 2 · Desk Lamps 2 ·
  Food Storage Containers 2 · Cutting Boards 2 · Coat & Hat Racks 2 · one each of Over-Ear Headphones, Landscape Pathway
  Lighting, Picture Frames, Alarm Clocks, Bath Mats & Rugs, Decorative Tapestries, Trash Cans, Body Pillows,
  Digital Photo Frames.
- **Collections:** all 12 titles resolved against the existing 24 — **no new collection was needed**. Home Decor 43 ·
  Lightning 19 · Bedroom Essentials 18 · Home Interior 8 · Outdoor & Garden 6 · Storage & Organization 5 ·
  Kitchen & Dining 4 · Gadgets 3 · Accessories 3 · Bathroom Essentials 3 · Cleaning & Home Care 2 · Health 1.
- **Alts: 399 pushed, 0 duplicates across the batch, none over 125 characters.** `backup-alt-ddl2-batch1.md` was written and
  sent to the chat BEFORE the alt push (not a project doc, per the 2026-09-08 decision).

## Step 7b — dimension image
Skipped: **Q18 = Skip dimension image**. `dim_image.py` / `dim_attach.py` were not run.

## Step 8 — verification
```
verify: 50 products, 901 checks, 0 failures
head-check: 0 FAIL of 50
```
Every product checked live for title, normalized descriptionHtml, both SEO fields and their 70/160 limits, productType,
tags = snapshot ∪ season with nothing dropped and no duplicate, status unchanged, category, CTA metafield JSON, collections
joined, media alts (≤125, unique in product and across the batch), media order, description image order and CDN host,
variant prices unchanged, brand name absent outside the comparison block, the comparison block present exactly once, and the
fit block present once before the FAQs. **No `[note]` lines** — the collections check ran on all 50 rather than degrading,
so the Worfa `collections.json` shape is confirmed good.

## Coverage table (extract_check.py)
| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 2 | 0 | 4 | - | 19 | 1 | 0 | - |
| 01 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 02 | 2 | 0 | 5 | - | 0 | 8 | 0 | - |
| 03 | 2 | 0 | 5 | - | 0 | 6 | 0 | - |
| 04 | 2 | 0 | 5 | - | 0 | 7 | 0 | - |
| 05 | 2 | 0 | 5 | - | 0 | 8 | 0 | - |
| 06 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 07 | 2 | 0 | 5 | - | 0 | 8 | 0 | - |
| 08 | 2 | 0 | 5 | - | 0 | 7 | 0 | - |
| 09 | 2 | 0 | 5 | - | 0 | 10 | 0 | - |
| 10 | 2 | 0 | 5 | - | 0 | 10 | 0 | - |
| 11 | 5 | 0 | 0 | - | 7 | 1 | 0 | - |
| 12 | 2 | 0 | 5 | - | 1 | 7 | 0 | - |
| 13 | 2 | 0 | 5 | - | 3 | 9 | 0 | - |
| 14 | 2 | 0 | 4 | - | 0 | 7 | 0 | - |
| 15 | 2 | 0 | 4 | - | 0 | 6 | 0 | - |
| 16 | 2 | 0 | 5 | - | 0 | 12 | 0 | - |
| 17 | 2 | 0 | 5 | - | 0 | 11 | 0 | - |
| 18 | 2 | 0 | 5 | - | 0 | 8 | 0 | - |
| 19 | 5 | 0 | 0 | - | 0 | 6 | 0 | - |
| 20 | 2 | 0 | 5 | - | 0 | 8 | 0 | - |
| 21 | 2 | 0 | 5 | - | 0 | 12 | 0 | - |
| 22 | 2 | 1 | 5 | - | 0 | 12 | 0 | - |
| 23 | 2 | 1 | 5 | - | 0 | 7 | 0 | - |
| 24 | 2 | 0 | 5 | - | 0 | 7 | 0 | - |
| 25 | 2 | 1 | 5 | - | 0 | 8 | 0 | - |
| 26 | 2 | 0 | 5 | - | 0 | 13 | 0 | - |
| 27 | 2 | 0 | 5 | - | 0 | 13 | 0 | - |
| 28 | 5 | 0 | 0 | - | 0 | 12 | 0 | - |
| 29 | 5 | 0 | 0 | - | 0 | 14 | 0 | - |
| 30 | 5 | 1 | 0 | - | 7 | 0 | 0 | - |
| 31 | 5 | 1 | 0 | - | 8 | 0 | 0 | - |
| 32 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 33 | 4 | 0 | 0 | - | 9 | 0 | 0 | - |
| 34 | 4 | 1 | 0 | - | 10 | 0 | 0 | - |
| 35 | 4 | 0 | 1 | - | 10 | 0 | 0 | - |
| 36 | 4 | 1 | 0 | - | 9 | 0 | 0 | - |
| 37 | 4 | 1 | 0 | - | 6 | 0 | 0 | - |
| 38 | 4 | 0 | 0 | - | 5 | 0 | 0 | - |
| 39 | 4 | 0 | 0 | - | 6 | 0 | 0 | - |
| 40 | 5 | 0 | 0 | - | 8 | 0 | 0 | - |
| 41 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 42 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 43 | 5 | 1 | 0 | - | 6 | 0 | 0 | - |
| 44 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 45 | 6 | 0 | 0 | - | 5 | 0 | 0 | - |
| 46 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 47 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 48 | 5 | 1 | 0 | - | 6 | 0 | 0 | - |
| 49 | 2 | 1 | 5 | - | 0 | 8 | 0 | - |

## For the next run
1. **`sections.py` is still the weakest script in the toolkit and it is now dangerous in a *different* way than in batch8.**
   There the 42 false positives were the description's lead prose, which the 2026-09-09 shape tests now catch. Here all 71
   were the source's own Key Features list ("Why You'll Love It", 4 words — under `MAX_HEAD_WORDS`), its Package Includes
   block ("What's in the Box?"), and single spec rows whose one-word names map straight onto `CANON`. Left alone this run
   would have published `<h3>Why You'll Love It</h3>` on 40 products with the Key Features list emptied underneath, and
   one-line `<h3>Size Guide</h3>` sections duplicating the Specifications list. Three cheap script tests would have caught
   every one by machine instead of by eye: (a) a candidate block whose lines are already in `key_features` or `package` is
   that block, not a new section; (b) a block whose every line matches a `specs` name/value pair is the spec table;
   (c) a heading matching a known non-section family (`why you('|')?ll love it`, `what'?s in the box`, `why choose …`) is
   never a section heading. Until then, **the `--extract` summary and the `[UNMAPPED]` list must be read in full every run
   and the reclassification done by hand** — a run that skips that read publishes marketing headings.
2. **`extract_check.py`'s baseline does not survive a main-context edit of `key_features` made before the agents run.**
   It rebuilds `_base/` from `raw/` with `keyfeat_cover.py`, so any line the main context moved in (or `sections.py` moved
   out) is attributed to the agents and every product FAILs. Recording the moves in `para_feat_added.json` fixes the
   column but not the claim comparison; the claims had to be aligned to the measured counts by hand. If `_base/` were
   snapshotted from `extract/` at the moment the agents are dispatched, the check would measure what it means to measure.
3. **Tell the extraction agents that splitting a run-on spec line counts as `prose spec pairs added`.** Thirteen of these
   sources put their whole spec table in one sentence inside `facts`; the agents did the work (246 pairs, three products
   going 0 → 6/13/13) and reported `Z = 0` with "no measurable prose value", which reads in the log as a skipped step.
4. **The CTA/benefit correction round needs two passes budgeted, not one.** Seven of this batch's replacements swapped one
   forbidden family for another (comparison → aesthetics → variant fact). The 6d "re-read the changed lines by eye" rule is
   what caught them; without it seven bad lines reach the store looking corrected.
5. **CTA metafield rendering — RESOLVED, doc corrected.** `cta-benefits-metafield.md` still documented the OLD store's theme
   (Xtra || FIXED, `gid://shopify/OnlineStoreTheme/204864586014`), so this was logged as an open risk: a metafield no theme
   block reads renders nothing and fails silently. **The user confirmed the same day that they had already pasted the Custom
   Liquid block into Worfa's main theme Vault (`gid://shopify/OnlineStoreTheme/174734606372`) and that the benefits render on
   the live product page.** The rule doc's Teknik section now names Vault, records that the block does NOT travel with a store
   change (it is pasted into the new theme by hand), and keeps the old theme id only as history; MANIFEST.md line recomputed
   (`f5c61311…`). Nothing to do next run — but the same check belongs on any future store change.
