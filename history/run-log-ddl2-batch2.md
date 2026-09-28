# Run log — DDL2-Batch2 (Worfa), 2026-09-11

**Route note (user decision 2026-09-11):** `ymjviw-rz.myshopify.com` and `api.dataforseo.com` were both refused by the egress
proxy (CONNECT 403) and the previous session's container had been reclaimed (all first-run artefacts lost). The user
approved the Shopify MCP for this batch only. Implementation: `shopify_api.gql` gained a file-queue bridge
(`SHOPIFY_MCP_BRIDGE=1` → bridge/req_N.json served by a Sonnet worker agent calling `graphql_query` / `graphql_mutation`);
DataForSEO went through `kw_mcp.py` (same normalisation / rounds as kw_measure.py, MCP `kw_data_google_ads_search_volume`).
Fetches were done twice by independent agents and `cmp`-identical before use (retyping guard). Lesson: a worker RETYPED one
10-product mutation's `ip9` from memory (mut3, p39) — description FAQ altered, seo/type/tags/category/collections dropped;
caught by verify.py, re-pushed alone, clean. Workers must read payloads in chunks and pass them verbatim; never from memory.

## Scope
Tag DDL2-Batch2: 50 fetched, all DRAFT; p45 "Shipping Protection" excluded → 49 processed. Brief: Q2 keep prices, Q5 keep
status, Q6/Q7 rewrite (title-format-rule / description-format-rule), Q8 auto season, Q11 CTA, Q12 type+category, Q13
collections, Q14 re-host, Q16 alt, Q17 table, Q18 skip, Q19 fit. Store row / theme colours as verified 2026-09-10.

## Steps
- Toolkit copy: 55 lines, 2 genuine copy corruptions (description-format-rule.md, title-format-rule.md — dropped lines),
  fixed by a second independent copy; `sha256sum -c` → TOOLKIT OK.
- Extraction 49/49 (5 Sonnet agents). sections --extract: 46 of 49 flagged a "What's in the Box?" block as [UNMAPPED] — it is
  the package list (already extract.package); all 46 dismissed by main ("package block"), 0 sections kept. Suggest adding a
  box/package dismissal to sections.py. 78 other blocks dismissed (description lead 32 / long marketing heading 46).
- para_feat: 70 KF flagged, 2 added (p03 rotating shade, p17 folding design), 68 dismissed | 18 SPEC flagged, 3 added
  (p05 12 × 7 × 2 in, p07 24 days, p42 13.1 × 1.9 ft), 15 ruled (equivalent notation or table conflict — rulings_omit.json).
  extract-check: 0 FAIL; agent additions KF 8 / spec 10; main KF 2+1 / spec 3.
- KF/spec independent review: 4 eligible of 49, 1 marked, 1 confirmed and added (p08 secure no-slip fit), 0 dismissed.
- RULINGS.md: 27 rulings (p00 height conflict, p02 wood-look, p13 rounding, p21 ABS not alloy, p30 no heating element, p34
  pencils not included, p39 marbles small-parts warning, p47 age 4–6 …).
- DataForSEO via MCP: 3,394 raw → 2,986 unique, 0 oversize, 2,986 measured in 14 call(s) over 3 round(s) — 92 word-order
  variant(s) moved to later rounds; 0 not returned. kw-cache-ddl2-batch2.md sent to chat.
- Titles (one opus subagent): title-check 0 FAIL / 67 WARN / 134 MANUAL, head_check 0 FAIL of 49; 0 extra keyword calls;
  25 skip reasons; all 49 in the 70–120 tier; total captured volume 9,358,760 (agent's figure). Main edit: p15 "Insulated
  Cooler Compartment" → "Insulated Food Compartment" (source says food compartment). backup-titles-ddl2-batch2.md rewritten
  in the project BEFORE the push.
- Re-host: 98 foreign srcs → 97 mapped, 1 failed (p20 `…tplv-fhlh96nyum…jpg` "Media processing failed", same as first run) →
  gallery image 2 substituted per the dead-source rule; 0 still foreign. (Duplicates of the first run's 97 files now exist
  in Files — first-run ids were lost with the container.)
- Descriptions: 5 Sonnet agents, gate CLEAN 49/49. 6b fact_cover run 1: 9 lines < 55 % — all (a) rulings / (b) marketing
  headings, 0 sent back; run 2 after 6c: no new line. 6c read on all 49: corrected p00 01 02 04 05 06 10 11 13 14 17 22 28
  29 31 32 33 34 35 37 38 40 41 43 45 47 48 (audience / gift / variant / aesthetic bullets and CTA lines). CTA read on all 49,
  corrected: p00 01 02 04 05 06 10 13 32 33 35 37 38 40 41 43 45 48. CTA independent review: 33 marked, 18 confirmed and
  corrected, 15 dismissed (capability / benefit lines such as "Climbs walls too", "Doubles as a nap pillow"). KF read on all 49:
  copies 0 (keyfeat_cover), paragraph additions on 3 products; p47 4 items vs 5 source lines (1 ruled out). Rule 1: 0 WARN
  after corrections; remaining second-net WARNs (p00 01 02 03 06 07 19 24 30 33 35) each carry a written reason. 6d re-read of
  changed lines: p29 bullet 4 (variant sizes) and p35 bullet 2 (stuffed phrase) corrected again by main; gate CLEAN.
  struct-check: only p21 WARN (prose 131 / total 560 — source has 6 vehicles + sound spec).
- dim-keep: 0 restored, 0 warned, 49 untouched.
- Collections: created Christmas & Holiday (12 products), Apparel (8), Bags & Travel (2) — same three as the first run's plan;
  collections.json now 27. Categories: taxonomy search via MCP; 12 fuzzy picks overridden by hand (Throw Blankets, Figurines,
  Robotic Toys ×2, Night Lights & Ambient Lighting, String Lights, Stuffed Animals, Socks ×3, Women's Period Underwear, Wall
  Clocks, Hiking Poles, Mobile Phone Car Mounts); final_categories.json.
- Push: 5 mut + 2 cta + 9 alt = 16 payloads, all clean (pre-check: 0 titles changed since snapshot). p39 corrupted by the
  worker retype (above) and p47 alts duplicated p28's (same title blocks) → p47 alts rebuilt on its own "Plush Toy Dog"
  block; fix_mut (p39 + p47) and fix_alt47 pushed clean. backup-alt-ddl2-batch2.md (421 alts) sent to chat before the alt push.

## Verify
`verify: 49 products, 883 checks, 49 failures` — ALL 49 are the `variant prices` check and nothing else; head-check: 0 FAIL of 49.
**Prices were changed OUTSIDE this run:** every variant's price dropped by ~27.5 % (e.g. 64.99 → 47.12) with
`updatedAt 2026-09-11T12:52:34Z` on all products — before our first push (14:20Z+) and by something other than this session
(no variant mutation was built or sent; the bridge log holds every request). Looks like a store-wide sale script. Not
reverted (Q2 = keep current, and it is not ours to undo) — user to confirm. All other 834 checks pass: title, description,
seo (+limits), productType, tags = snapshot ∪ season (19 winter, 28 evergreen, 1 summer p19, 1 fall p24), status DRAFT
unchanged, category, CTA metafield, collections, media alts (unique in batch after the p47 fix), media order, description
img srcs on our CDN, brand absent, comparison + fit blocks live exactly once.

## Operator notes
- p29 giant teddy: source package says "Outer Cover" with "PP cotton filling (optional)" — description states the optional
  filling as the source does; confirm with the supplier whether the bear ships stuffed.
- p30 was tagged/typed "Heated Gloves" by the supplier — no heating element in the source; typed "Winter Gloves".
- p34 "Coloring Set": pencils not included (stated on the page).
- Notes per product in final/dNN.json `notes_for_log` (34 products).

## Coverage (extract_check.py)
| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 5 | 2 | 0 | - | 2 | 1 | 0 | - |
| 01 | 4 | 0 | 0 | - | 4 | 0 | 0 | - |
| 02 | 4 | 0 | 0 | - | 5 | 1 | 0 | - |
| 03 | 4 | 0 | 1 | - | 5 | 0 | 0 | - |
| 04 | 4 | 1 | 0 | - | 4 | 0 | 0 | - |
| 05 | 5 | 0 | 0 | - | 5 | 0 | 1 | - |
| 06 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 07 | 5 | 1 | 0 | - | 5 | 1 | 1 | - |
| 08 | 5 | 2 | 0 | - | 0 | 0 | 0 | - |
| 09 | 5 | 1 | 0 | - | 4 | 0 | 0 | - |
| 10 | 5 | 0 | 0 | - | 5 | 1 | 0 | - |
| 11 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 12 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 13 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 14 | 3 | 0 | 0 | - | 5 | 0 | 0 | - |
| 15 | 4 | 0 | 0 | - | 5 | 1 | 0 | - |
| 16 | 5 | 0 | 0 | - | 0 | 3 | 0 | - |
| 17 | 5 | 0 | 1 | - | 5 | 0 | 0 | - |
| 18 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 19 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 20 | 5 | 0 | 0 | - | 8 | 1 | 0 | - |
| 21 | 4 | 0 | 0 | - | 8 | 0 | 0 | - |
| 22 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 23 | 5 | 0 | 0 | - | 9 | 0 | 0 | - |
| 24 | 5 | 0 | 0 | - | 3 | 0 | 0 | - |
| 25 | 4 | 0 | 0 | - | 8 | 0 | 0 | - |
| 26 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 27 | 3 | 0 | 0 | - | 5 | 0 | 0 | - |
| 28 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 29 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 30 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 31 | 3 | 0 | 0 | - | 7 | 0 | 0 | - |
| 32 | 4 | 0 | 0 | - | 7 | 0 | 0 | - |
| 33 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 34 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 35 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 36 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 37 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 38 | 5 | 1 | 0 | - | 5 | 1 | 0 | - |
| 39 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 40 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 41 | 5 | 0 | 0 | - | 7 | 0 | 0 | - |
| 42 | 5 | 0 | 0 | - | 5 | 0 | 1 | - |
| 43 | 5 | 0 | 0 | - | 5 | 0 | 0 | - |
| 44 | 4 | 0 | 0 | - | 3 | 0 | 0 | - |
| 45 | 4 | 0 | 0 | - | 6 | 0 | 0 | - |
| 46 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 47 | 5 | 0 | 0 | - | 6 | 0 | 0 | - |
| 48 | 4 | 0 | 0 | - | 7 | 0 | 0 | - |

