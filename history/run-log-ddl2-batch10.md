# Run log — DDL2-Batch10 (Worfa, 2026-09-10, scheduled)

Store **Worfa** (`ymjviw-rz.myshopify.com`), tag `DDL2-Batch10`, **50 products** (all DRAFT, none with a category).
Brief: Q1 by tag · Q2 keep prices · Q3 none · Q4 no rounding · Q5 keep status · Q6 rewrite titles (Q9 = title-format-rule.md) ·
Q7 rewrite descriptions · Q8 auto-infer season · Q10 **scheduled**, full batch pre-approved · Q11 CTA benefits · Q12 productType +
category per product · Q13 collections per product · Q14 re-host to our CDN · Q15 title backup · Q16 alt text ·
Q17 comparison table · Q18 **skip** dimension image · Q19 fit block.

**Result: HALTED at step 4 on a tool error — NOTHING WAS PUSHED. The store is unchanged** (no productUpdate, metafieldsSet,
fileCreate or fileUpdate call was made; titles, descriptions, SEO, tags, prices, status, categories, collections and alts of
the 50 products are exactly as before the run). No `backup-titles-ddl2-batch10.md` was written because no title was built.

## Why it stopped
`kw_measure.py` → `urllib.error.URLError: <urlopen error Tunnel connection failed: 403 Forbidden>`. The session's agent
proxy status shows `connect_rejected — gateway answered 403 to CONNECT — host api.dataforseo.com:443` at 22:21:44 UTC.
This scheduled cloud environment's egress policy does not allow **api.dataforseo.com** (the Shopify host
`ymjviw-rz.myshopify.com` is allowed and worked). Per the proxy rules a policy 403 is not retried or routed around.
Without keyword volumes, `title-check.py` is push-blocking by design (every source-title window must be in kw.txt), so no
title could pass and the run could not continue to titles → descriptions → push. Per the RUN MODE block, a genuine tool
error halts a scheduled run with a report.

**To fix:** add `api.dataforseo.com` to the egress allowlist of the environment this scheduled task runs in (the same way
`ymjviw-rz.myshopify.com` was added on 2026-09-10), then re-run the task. The next run starts from step 0; the extraction
below will be redone (≈0.85M sub-agent tokens), or reused from the archive sent to the chat.

## What was done before the halt (steps 0–3e)
- **Step 0:** 54 toolkit/rule files copied by 4 Sonnet agents; `sha256sum -c MANIFEST.sha256` → **TOOLKIT OK on the first pass**.
- **Step 1:** `shopify_api.py shop` → **Worfa**. `brief_flags.json`: q17 true, q19 true, q18 false, run_mode scheduled.
- **Step 2:** 50 products fetched. All 50 carry foreign description images (supplier CDN `cdn.shopify.com/s/files/1/0973/4773/1805/`) — not yet re-hosted.
- **Step 3 / 3e — sections.py: 64 kept blocks on 45 products, all rejected by the main context.** `sections --extract: 45 of 50
  products carry a fact section, 71 dismissed (lead 22 / long marketing heading 49), 61 UNMAPPED, 6 key_features lines moved`.
  Every kept block was a misdetection: 43 × "What's in the Box?" (= `package`), ~20 single spec rows already in `specs`
  (Thickness, Use, Material, Size, Power, Weight, Care, Small/Medium/Large…), and p42 "Scratch protection" (= the source's own
  Key Features list, which the script had emptied to one line). The 6 moved key_features lines (p22 ×1, p42 ×4, p44 ×1) were
  restored by re-running `keyfeat_cover.py --extract`; `extract.sections` = [] on all 50. Same failure family as DDL2-Batch1
  ("What's in the Box?" and one-word spec-row headings pass the shape tests) — batch1's "For the next run" item 1 still stands.
- **Extraction agents:** 5 Sonnet × 10. `extract-check: 0 FAIL across 50 products; agent additions total KF 12, spec 2;
  main-context additions KF 4, spec 0`. `usage_tips --extract: 0 of 50`.
- **para_feat: 75 KF flagged, 4 added (p36 metal shell, p37 spandex fabric + elastic waistband, p48 non-stretch fabric), 71
  dismissed | 1 SPEC flagged, 0 added, 1 ruled (p44 "3 color" = count of the three listed colour modes, rulings_omit.json).**
  `para_feat --gate: 0 unruled prose spec figure(s)`.
- **KF/spec independent review: 0 eligible of 50** (no source paragraph over 80 words) — nothing for the reader.
- **RULINGS.md written** (in the archive): p13 plastic bird lamp in 4 colours — never "glass / cardinal / parrot"; p16
  heart plus LOVE / concentric-circle options; p18 a lighted tabletop tree, not a lamp; p21 message options include family
  messages; p23 four colours; p24 fabric never named; p28 no material; p31 cosmetic wording only; p32 omit boilerplate
  "Up to 36V"; p38 variant colours win (omit "light gray"); p42 inconsistent Large inch range omitted, cm kept; p48 no
  pocket claim; kids supervision on p13 p20 p41 p43.
- **Step 4:** `source_windows.py: 50 titles -> 1030 windows, 1 dropped over the DataForSEO limit`. The DataForSEO call
  failed as above; kw.txt is empty; no cost incurred.

## Found in the source data (for the operator, not changed — Q2 = keep prices)
- Variant price outliers that look like supplier data errors: p24 table runner Red at 60in/90in $64.99/$79.99 vs
  $39.99/$49.99 for other colours; p28 winter jacket Navy blue/L $289.99, Green/XL $294.99, Green/3XL $244.99 vs $149.99;
  p29 running shoes Gray EU45/US11/AU10 $114.99 vs $69.99.
- p01 slippers carry a `sandals` tag (legacy/mismatched; non-seasonal tags are never touched).

## Phase 3 / Phase 4
Phase 3 summary: 0 products updated, 0 failed pushes (nothing was pushed). Phase 4 verification: not applicable — the
live products were fetched once at step 2 and no write followed.

## Artefacts
`ddl2-batch10-extraction-state.tgz` (extract/, candidates/, RULINGS.md, rulings_omit.json, para_feat_added.json,
extract_claims.json, sections_rejected.json, coverage.md, products.json snapshot) — sent to the chat, not a project doc.
