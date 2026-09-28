# run-log-ddl2-batch5 — Worfa, 2026-09-12 (scheduled run, no human present)

Brief: Q1 tag DDL2-Batch5 (50 products, all DRAFT) · Q2 keep prices · Q3 none · Q4 no rounding · Q5 keep status · Q6 rewrite titles (title-format-rule.md) · Q7 rewrite descriptions · Q8 auto-infer season · Q9 own format · Q10 scheduled, full batch · Q11 CTA benefits · Q12 productType + category · Q13 collections · Q14 re-host · Q15 backup titles · Q16 alt text · Q17 comparison table · Q18 skip · Q19 fit block.
Store: Worfa (ymjviw-rz.myshopify.com), script route via shopify_api.py. Fresh container; no earlier backup-titles-ddl2-batch5 existed, live titles = supplier titles (50/50) — first run of this batch.

## Step 0 — toolkit copy
57 files copied by 3 Sonnet agents (Write tool); `sha256sum -c MANIFEST.sha256 --quiet` → TOOLKIT OK after 3 genuine copy corruptions were fixed by re-copy in the agents' own pass (rules/title-format-rule.md — a dropped paragraph; fit_build.py; para_feat.py). 0 stale manifest lines. Every .py compiles.

## Step 1–2
brief_flags.json {q17 true, q19 true, q18 false, run_mode scheduled}. Fetch: 50 products, 526 media, 99 foreign description images (other stores' CDNs). collections.json refreshed: 31 collections.

## Step 3 — extraction
extract_html + keyfeat_cover --extract + usage_tips --extract (2 of 50 with a Usage Tips block) + sections --extract: `46 of 50 products carry a fact section, 72 dismissed (description lead 26 / long marketing heading 46), 47 UNMAPPED, 4 key_features lines moved`. Main-context read: all 47 unmapped headings were "What's in the Box?" (= extract.package) and p07's two were mis-parsed spec-table rows → all 48 dismissed by the main context; keyfeat_cover --extract re-run to restore the moved lines. sections: 0 products with sections this batch.
5 Sonnet agents × 10 (identity, notes, facts, specs by eye, key_features, candidates 40–70 each). Agents also rebuilt the spec tables the parser missed on p16 / p19 (no colon after the bold name).
para_feat: 67 KF flagged, 1 added (p25 multi-zone massage), 66 dismissed (marketing restatements of the list) | 9 SPEC flagged, 4 pairs added (p27 length 86 cm / 33.9 in, width 150 cm / 59 in, weight 1.2 kg / 2.6 lb, one size — the agent had written "no spec table exists" as its reason), 2 ruled (rulings_omit.json: p27 0.86 m / 1.5 m = same values), 1 resolved by a typo fix (p00 "227°Cm" → 227°C, source prose confirms). para_feat --gate: 0 unruled.
extract-check: 0 FAIL across 50 products; agent additions KF 6, spec 31; main-context additions KF 1, spec 4.
KF/spec independent review: 2 eligible of 50 (p27, p37), 0 marked.
RULINGS.md: 12 rulings — p00 typo; p06 "Electronics: Does not contain electronic components" omitted (contradicts LCD / heat levels / auto-off); p07 boilerplate kept; p13 / p27 "Gray 2" / "Burgundy 2" variants named as they are; p15 "Wine / Beverage / Bottle Frog" = style names; p26 "Power Source: Vehicle 12V DC outlet" AND the KF line "manual, no power source" both omitted (contradict each other and the LED light); p35 Orange variant vs colour spec line; p43 Grey/Gray; p46 leather / orthopedic only in foreign alt text → never written; p49 productType "Warts Remover Ointment" contradicted by the source → cosmetic gel, no medical claim.

## Step 4 — keywords
source_windows: 50 titles → 893 windows, 0 dropped. kw_measure: 3304 raw → 2883 unique, 0 dropped, 2883 measured in 5 call(s) over 3 round(s) — 72 word-order variant(s) moved to later rounds; 0 not returned; cost $0.45. Title step 1b: one extra call, 661 terms → 684 lines, 2 rounds (~$0.18); kw.txt 3567 lines. kw-cache-ddl2-batch5.md sent to chat (twice — after step 4 and again after 1b).

## Step 5 — titles
One title agent (main model), all 50. title-check: 0 FAIL, 55 WARN, 81 MANUAL REVIEW; head-check 0 FAIL of 50. All 50 titles 105–120 chars, no trigger claimed. Fit-clean captured volume 4,941,910 (title-check's nested sum 4,354,410). Old-vs-new product-naming gate passes on all 50 (p12 / p23 re-cut to keep `metal wind spinner` / `scratch removal`). A 1b-measured keyword sits in 29 of 50 final titles (`candle warmer` 135,000, `heating pad for back pain` 33,100, `ceramic coffee mug` 22,200, `hummingbird feeder with ant moat` 12,100 …). Skip reasons: p00 `pot strainer`, p01/03/05–09 `portable hand warmer` (3rd Warmer), p11 `yard hose`, p12 three over-120 phrases, p29 `heating pad for shoulders`. Large fit rejections logged in fit_rejects.json (p15 `garden gnome` 550,000, p19 `classroom game` 368,000, p32 `board game` 246,000, p29 `heating blanket` 165,000, p24 `vanity mirror` 74,000, p27 `oversized hoodie` 90,500, p46 `mens work boots` 90,500, p44 `power bank` 74,000). productType set per §10b on 47 of 50 (e.g. p10 Bird Feeder Camera, p12 Wind Spinner, p17 Baby Bottle Washer, p20 Candle Warmer Lamp, p24 Compact Mirror, p41/42 Snuffle Mat, p49 Cosmetic Gel). backup-titles-ddl2-batch5.md written to the project before the push.

## Step 5b — re-host
rehost.py: 99 mapped, 0 failed, 99 srcs rewritten, 0 still foreign.

## Step 6 — descriptions
5 Sonnet agents × 10; gate.py CLEAN over all 50 after the correction round (struct-check WARN only: prose > 110 on 23 products after trimming — down from 42 — and total > 500 on a few; no FAIL). Categories: 39 of 50 resolved to taxonomy gids by search (category_map.json) after 18 proposals were renamed to real leaves (Polishes, Electric Steam Sterilizers, Candle & Oil Warmers, Motor Vehicle Electronics, Outfit Sets, Double Pet Leashes, Tumblers, Educational Toys, Garden Sculptures, Karaoke Systems, Compact & Pocket Mirrors, Cooking Thermometers, Bird Feeders, Sensory Toys, Skin Care, Strainers); KEEP (category None, no fitting leaf) on the 8 electric hand warmers (p01–03, p05–09 — taxonomy has only "Chemical Hand Warmers") and p28 UV wand. Collections used: 18 existing, 0 new.
6b fact_cover: run 1 — 5 lines under 55%, all (b) same meaning in other words (p05 heat levels + intro sentence, p20 timer, p37 / p45 marketing intros); 0 genuinely missing. Run 2 after corrections: 6 lines (+ p43 marketing intro, same class); diff otherwise empty.
6c read on all 50 products: corrected p00 (invented "folds flat" / "without warping") p01 p02 p04 p05 p06 p07 p08 p10 (invented "no drilling") p11 p12 p13 (5 vs 6 colours) p15 p17 p18 p19 p20 (invented "no smoke / soot / wick") p21 p22 (invented "pocket") p23 p24 (invented "shadow-free") p26 (invented "trucks and SUVs") p28 (invented "zap germs / in seconds") p30 (invented "season's worth", "no gas") p31 p32 (invented "no reading") p33 (invented "no screens", comparison) p34 (comparisons) p36 p37 (invented "screen-free" ×4, "no hard small parts") p38 (invented "handwriting") p39 (age range) p40 (invented "screen-free", "safe") p41 (invented "chewing") p43 p44 (invented "traffic noise") p45 p46 (invented "wet or icy") p47 (invented "jacket cuff") p49 ("treat", "no residue"); plus a global trim of padded prose and removal of universal "any / every" claims on all 50.
CTA read on all 50 products, corrected: p04 p06 p10 p11 p20 p22 p24 p28 p30 p34 p40 p44 p49.
CTA independent review: 25 marked on 20 products, 24 confirmed and corrected (p02 ×3, p05, p06, p07, p08, p10, p13, p15 ×2, p18, p19, p22, p23, p33, p36, p37, p39, p45 ×2, p46, p47, p49), 1 dismissed (p42 "Slows down fast eaters" — source: "slow treat discovery").
KF read on all 50 products: copies 0 (keyfeat_cover), paragraph additions on 1 product (p25 + agents' 6); products 40–49 had passive-inversion items ("various skin areas are covered by this…") rewritten as natural sentences in the correction round.
6d: one correction message per agent; changed lines re-read by eye — p20 "instead of burning a wick" (×2) and an FAQ "wick to trim" removed by the main context, p44 duplicated bullet payoff rewritten; gate CLEAN over 50 after the round.

## Step 7 — push
dim-keep: 0 restored, 0 warned, 50 untouched. Payloads: push/mut0–4 (aliased productUpdate: title, descriptionHtml, seo whole, productType, tags = snapshot ∪ season, category gid where proposed, collectionsToJoin), cta0–1 (metafieldsSet custom.cta_benefits ×50), alt0–10 (fileUpdate 526 alts, unique across the batch). backup-alt-ddl2-batch5.md sent to chat before the alt push. Live titles re-checked equal to the snapshot immediately before the push (50/50). All 18 payloads: clean (0 userErrors).
Seasons: {'evergreen': 28, 'winter': 17, 'spring': 3, 'summer': 2}.

## Step 8 — verify
`verify: 50 products, 901 checks, 0 failures` · `head-check: 0 FAIL of 50` · 0 [note] lines.

## Phase 3 summary
50 of 50 products updated, 0 failed. Nothing to retry.

## Open items
- p46 title carries "Traction Sole" (source: "patterned base … consistent traction", "stable grip") — accepted as the same meaning; flag if the user prefers the source's own words.
- 23 products keep prose above 110 words after trimming (WARN only); the agents judged the remaining sentences source-bearing.
- Hand warmers (8 products) and p28 have no Shopify taxonomy category (none fits); set by hand if a category is wanted.

## coverage.md (extract_check)
| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 5 | 0 | 0 | 5 | 4 | 1 | 0 | 6 |
| 01 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 7 |
| 02 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 7 |
| 03 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 04 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 6 |
| 05 | 4 | 0 | 0 | 4 | 7 | 0 | 0 | 8 |
| 06 | 4 | 0 | 0 | 4 | 8 | 0 | 0 | 8 |
| 07 | 4 | 0 | 0 | 4 | 9 | 2 | 0 | 12 |
| 08 | 5 | 0 | 0 | 5 | 6 | 1 | 0 | 8 |
| 09 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 6 |
| 10 | 4 | 1 | 0 | 5 | 6 | 0 | 0 | 6 |
| 11 | 4 | 1 | 0 | 4 | 6 | 0 | 0 | 7 |
| 12 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 13 | 4 | 1 | 0 | 5 | 6 | 0 | 0 | 7 |
| 14 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 7 |
| 15 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 6 |
| 16 | 5 | 0 | 0 | 5 | 0 | 5 | 0 | 6 |
| 17 | 5 | 1 | 0 | 6 | 7 | 0 | 0 | 8 |
| 18 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 6 |
| 19 | 5 | 0 | 0 | 5 | 1 | 5 | 0 | 7 |
| 20 | 5 | 0 | 0 | 5 | 0 | 5 | 0 | 6 |
| 21 | 5 | 0 | 0 | 5 | 0 | 6 | 0 | 6 |
| 22 | 5 | 1 | 0 | 6 | 6 | 0 | 0 | 6 |
| 23 | 5 | 0 | 0 | 5 | 0 | 4 | 0 | 4 |
| 24 | 4 | 0 | 0 | 4 | 5 | 0 | 0 | 5 |
| 25 | 1 | 0 | 1 | 2 | 6 | 0 | 0 | 6 |
| 26 | 4 | 0 | 0 | 3 | 3 | 0 | 0 | 3 |
| 27 | 5 | 0 | 0 | 5 | 0 | 0 | 4 | 5 |
| 28 | 5 | 0 | 0 | 5 | 7 | 0 | 0 | 7 |
| 29 | 5 | 1 | 0 | 6 | 6 | 0 | 0 | 6 |
| 30 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 8 |
| 31 | 5 | 0 | 0 | 5 | 4 | 0 | 0 | 4 |
| 32 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 33 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 6 |
| 34 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 6 |
| 35 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 8 |
| 36 | 4 | 0 | 0 | 4 | 7 | 0 | 0 | 7 |
| 37 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 6 |
| 38 | 5 | 0 | 0 | 5 | 7 | 0 | 0 | 7 |
| 39 | 4 | 0 | 0 | 4 | 6 | 0 | 0 | 6 |
| 40 | 5 | 0 | 0 | 5 | 4 | 0 | 0 | 4 |
| 41 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 42 | 4 | 0 | 0 | 4 | 7 | 0 | 0 | 7 |
| 43 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 8 |
| 44 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 8 |
| 45 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 8 |
| 46 | 5 | 0 | 0 | 5 | 0 | 1 | 0 | 2 |
| 47 | 5 | 0 | 0 | 5 | 0 | 0 | 0 | 5 |
| 48 | 5 | 0 | 0 | 5 | 0 | 1 | 0 | 3 |
| 49 | 5 | 0 | 0 | 5 | 4 | 0 | 0 | 4 |
