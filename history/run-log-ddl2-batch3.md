# run-log-ddl2-batch3 — Worfa, 50 products, 2026-09-11 (full re-process from scratch, user instruction; supersedes claude/checkpoint-ddl2-batch3.md of 2026-09-11 04:05 UTC — that checkpoint's tarball was NOT used)

## Brief
Q1 By Tag DDL2-Batch3 · Q2 keep prices · Q3 none · Q4 no rounding · Q5 keep status (all 50 DRAFT, unchanged) · Q6 rewrite titles (title-format-rule.md) · Q7 rewrite descriptions · Q8 auto-infer season · Q10 manual (user pre-approved store + full batch, no test run) · Q11 CTA benefits · Q12 productType + category per product · Q13 collections from existing (none new needed) · Q14 re-host · Q15 backup-titles · Q16 alt text · Q17 Add table · Q18 Skip · Q19 Add fit block.

## Route deviations this session (both hosts 403 through the session proxy)
- `ymjviw-rz.myshopify.com` CONNECT 403 → every Shopify call (fetch, fileCreate/poll, push, verify fetch) went through the Shopify MCP tools; `shopify_api.py` was not usable. Shims: `rehost_mcp.py` (rehost.py's file/rewrite logic, MCP makes the calls), payload files pushed by an MCP agent. **The MCP push retyped and altered 2 of 50 descriptions in transit (p17: `70°F`→`70°C`; p36: fit-block line order)** — caught by verify.py, re-pushed as descriptionHtml-only fixes, second verify clean. Reason to prefer the script route whenever the host is reachable.
- `api.dataforseo.com` CONNECT 403 → DataForSEO MCP tool, which returns ≤10 items per call: **3,060 keywords in 308 calls over 3 word-order rounds — 73 word-order variant(s) moved to later rounds** (`kw_mcp.py`, same guards/bucketing as kw_measure.py; user approved the cost). +20 step-1b extras in 2 calls → 3,075 measured. 0 dropped over the limit (2 oversize supplier titles dropped by source_windows.py).
- Toolkit copy: 57/57 manifest lines OK (two first-copy corruptions — fit_build.py, comparison-table-rule.md — fixed by JSON round-trip re-copy; one file initially skipped and re-copied).

## Extraction (step 3)
- sections.py --extract: 49 of 50 proposed a section, 59 UNMAPPED — every one was "What's in the Box?" (= package), p19 spec rows or p29 feature/spec headings → all dismissed, 9 key_features lines restored; agents added 2 Size Guide sections on p29. sections: 1 product with 2 sections, 70 dismissed by script (lead 27 / long heading 43) + 59 by main context, 0 unmapped left.
- extract_check: 0 FAIL across 50; agent additions KF 6, spec 25; main-context additions KF 14 (11 source Key Features lines the script parser had skipped as spec-duplicates: p02 p08 p19 p24 p28 p30×4 p43 p44 p46 p47 p48 — user rule: a source KF line is always a list item), spec 1.
- para_feat: 76 KF flagged, 0 added, 76 dismissed (marketing restatements) | 18 SPEC flagged, 2 added (p16 size, p45 length — p45 later ruled OUT: contradicts table + Battery/Mains variants), 16 dismissed (same value in table format, rulings_omit.json). para_feat --gate: 0 unruled.
- KF/spec independent review: 1 eligible of 50, 2 marked, 2 confirmed and added (p16 Lighthouse Projection Design; Light Source: LED), 0 dismissed.
- usage_tips: 1 of 50 carries a Usage Tips block. RULINGS.md: 12 rulings (p03 p04 olive branch identity, p13 placement height, p20 boilerplate spec, p26 variant names, p29 length conflict, p30 4 missed KF lines, p35 Christmas tree, p37 no-value dimension, p41 500GB not 8TB, p45 length claim omitted, p48 supplier policy line).

## Keywords / titles (steps 4–5)
- Total captured volume 9,694,050 across 50 titles; 42 at 70–120, 8 at 120–135 with named trigger A (#17 #20 #31 #33 #35 #42 #46 #49); none above 135. title-check: 0 FAIL, 60 WARN, 111 MANUAL; head-check 0 FAIL of 50 (titles_final.json and live_after.json). One main-context correction: #36 metric figure in a title → "98 Inch" (US-only store). backup-titles-ddl2-batch3.md written to the project BEFORE the push; kw-cache-ddl2-batch3.md sent to the chat.
- Notable fit rejections: nintendo switch 1,220,000 (brand), pest control 201,000 (service query), christmas lights 246,000 (#03 is a maple-leaf garland), car battery charger 135,000 (#17 is a jump starter), lantern 165,000 (#30), bathroom rug 60,500 (#21/#22 suction mats).

## Images (5b)
rehost: 100 foreign images (all on the supplier's cdn.shopify.com/s/files/1/0973/4773/1805/), 100 mapped, 0 failed, 100 srcs rewritten, 0 still foreign. Note: the aborted 2026-09-10 session had already created the same 100 files in Worfa Files; this run created them again (image_ids.json of that session was not available) → ~100 duplicate files in Files, harmless to the pages.

## Descriptions (6, 6b–6d)
- 5 Sonnet agents × 10; gate.py over all 50: `=== gate: CLEAN ===`, rule 1 = 0 WARN after corrections (p11 p14 p16 p40), second-net WARNs all carry a notes_for_log reason. First live run of list_bold.py (bold lead-ins + image-2 gap) and of the US-units-only budgeted elements — both applied on all 50.
- fact_cover run 1: 1 line (p46 marketing heading, b); run 2 after corrections: 13 lines, all (b) — marketing headings/leads or the same fact in other words (p30 Blinding Brightness ↔ Maximum Brightness item; p38 Durable ↔ Built to Hold Up) → (c) = 0.
- 6c read on all 50 products (H2, bullets, CTA, compare rows, fit lines): corrected 25 products — p04 p05 p06 p09 p10 p11 p12 p13 p14 p16 p19 p23 p25 p26 p30 p34 p35 p36 p37 p40 p43 p44 p45 p46 p48 (forbidden "for good" ×2, "safe"/"no drilling"/"no plumber"/"charges in minutes"/"years" inventions, variant-fact and aesthetics bullets, a supplier delivery promise in a fit line, duplicate bullets).
- KF read on all 50 products: copies 0 (keyfeat_cover), paragraph additions on 6 products (agents) + main additions on 12; two invented "safe" claims removed from KF items (p35 p36).
- CTA read on all 50 products, corrected: p04 p05 p06 p09 p10 p12 p14 p16 p19 p23 p25 p26 p35 p36 p44 p46.
- CTA independent review: 19 marked on 15 products, 19 confirmed and corrected, 0 dismissed.
- 6d re-read of every changed line by eye: p13 (keyword repeated twice in one bullet), p14 (duplicate bullet, then "without smudging" → source-safe wording), p36 (bullet 2 and prose/fit "no drilling" — a ceiling hook is not drill-free) corrected again.
- Seasons: 39 evergreen · 9 winter (01 03 19 20 31 32 33 35 39) · 1 fall (40) · 1 summer (44). Categories: 50 taxonomy ids resolved via the MCP taxonomy search (category_ids.json); 5 main-context overrides (p00/p48/p49 → Motor Vehicle A/V Players & In-Dash Systems, p13 → Animal & Pet Repellents, p32 Chemical Hand Warmers accepted as the only hand-warmer leaf); category_proposal in every final set to the resolved leaf name. Collections: 30 live (24 + 6 created 2026-09-10 incl. Packaging & Gift Boxes, Footwear, Christmas & Holiday, Apparel, Bags & Travel); 0 NEW proposed.

## Push (7) and verify (8)
- dim-keep: 0 restored, 0 warned, 50 untouched. backup-alt-ddl2-batch3.md (473 alts, 0 duplicates) sent to the chat before the alt push. seo carried both halves on all 50.
- push: mut0–4 (10 aliased productUpdate each: title, descriptionHtml, seo, productType, tags = snapshot ∪ season, category, collectionsToJoin), cta0–1 (metafieldsSet ×25), alt0–9 (fileUpdate ×50) → 17/17 clean; fix17 + fix36 (descriptionHtml only) → clean.
- **verify: 50 products, 901 checks, 0 failures** (first run: 2 failures p17 p36 — the MCP transit corruption above; fixed and re-verified). `head-check: 0 FAIL of 50`. Status DRAFT on all 50 (Q5 keep).

## For the next run (open items)
1. unit_dual.py mangles a dual-written temperature RANGE (`-20°F to 70°F / -29°C to 21°C` → `… -29°C to 70°F (21°C)`) and converts engine displacement litres to fl oz (`10.0 L` engines → `338.1 fl oz`). Both appeared on p17 and were hand-fixed to forms the script leaves alone (`-20°F (-29°C) to 70°F (21°C)`, `10.0-liter`). Worth a script fix: skip `L` after "engine(s)" / displacement context, and handle an `A to B / C to D` dual range.
2. kw_mcp.py / rehost_mcp.py are session shims — not toolkit docs; they exist only because both API hosts were 403 here. If the allowlist applies to new sessions, the script route (6 DataForSEO calls, byte-exact pushes) is cheaper and safer.
3. claude/checkpoint-ddl2-batch3.md (04:05 UTC) is obsolete after this run — delete it on the user's word.

## Coverage table (extract_check.py --table)
| # | KF source (script) | KF added by agent | KF added by main | KF final items | Spec source (script) | Spec added by agent | Spec added by main | Spec final items |
|---|---|---|---|---|---|---|---|---|
| 00 | 5 | 0 | 0 | 5 | 10 | 0 | 0 | 10 |
| 01 | 5 | 0 | 0 | 5 | 4 | 1 | 0 | 5 |
| 02 | 4 | 0 | 1 | 5 | 5 | 0 | 0 | 6 |
| 03 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 04 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 05 | 5 | 0 | 0 | 5 | 0 | 9 | 0 | 9 |
| 06 | 5 | 0 | 0 | 5 | 11 | 0 | 0 | 11 |
| 07 | 5 | 0 | 0 | 5 | 4 | 0 | 0 | 4 |
| 08 | 4 | 0 | 1 | 5 | 10 | 0 | 0 | 10 |
| 09 | 5 | 0 | 0 | 5 | 14 | 0 | 0 | 14 |
| 10 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 8 |
| 11 | 5 | 1 | 0 | 6 | 5 | 2 | 0 | 7 |
| 12 | 5 | 0 | 0 | 5 | 5 | 1 | 0 | 6 |
| 13 | 5 | 0 | 0 | 5 | 5 | 1 | 0 | 6 |
| 14 | 5 | 0 | 0 | 5 | 5 | 1 | 0 | 6 |
| 15 | 5 | 0 | 0 | 5 | 9 | 0 | 0 | 9 |
| 16 | 5 | 0 | 1 | 6 | 5 | 0 | 2 | 7 |
| 17 | 5 | 1 | 0 | 6 | 8 | 1 | 0 | 9 |
| 18 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 7 |
| 19 | 4 | 0 | 1 | 5 | 7 | 1 | 0 | 8 |
| 20 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 5 |
| 21 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 22 | 5 | 0 | 0 | 5 | 3 | 0 | 0 | 3 |
| 23 | 5 | 0 | 0 | 5 | 2 | 0 | 0 | 3 |
| 24 | 4 | 1 | 1 | 6 | 5 | 0 | 0 | 5 |
| 25 | 5 | 0 | 0 | 5 | 3 | 0 | 0 | 4 |
| 26 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 5 |
| 27 | 5 | 1 | 0 | 6 | 5 | 0 | 0 | 6 |
| 28 | 4 | 1 | 1 | 6 | 5 | 0 | 0 | 7 |
| 29 | 7 | 0 | 0 | 7 | 10 | 0 | 0 | 12 |
| 30 | 1 | 0 | 4 | 5 | 11 | 1 | 0 | 12 |
| 31 | 5 | 0 | 0 | 5 | 7 | 0 | 0 | 7 |
| 32 | 5 | 0 | 0 | 5 | 7 | 2 | 0 | 9 |
| 33 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 8 |
| 34 | 5 | 0 | 0 | 5 | 10 | 0 | 0 | 10 |
| 35 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 6 |
| 36 | 5 | 0 | 0 | 5 | 6 | 0 | 0 | 6 |
| 37 | 5 | 0 | 0 | 5 | 4 | 1 | 0 | 5 |
| 38 | 5 | 0 | 0 | 5 | 3 | 0 | 0 | 3 |
| 39 | 4 | 1 | 0 | 5 | 5 | 0 | 0 | 5 |
| 40 | 5 | 0 | 0 | 5 | 0 | 0 | 0 | 6 |
| 41 | 5 | 0 | 0 | 5 | 8 | 0 | 0 | 9 |
| 42 | 5 | 0 | 0 | 5 | 4 | 1 | 0 | 6 |
| 43 | 4 | 0 | 1 | 5 | 6 | 1 | 0 | 8 |
| 44 | 4 | 0 | 1 | 5 | 7 | 0 | 0 | 9 |
| 45 | 4 | 0 | 0 | 4 | 5 | 1 | 0 | 7 |
| 46 | 4 | 0 | 1 | 5 | 4 | 0 | 0 | 5 |
| 47 | 4 | 0 | 1 | 5 | 5 | 0 | 0 | 6 |
| 48 | 4 | 0 | 1 | 4 | 5 | 1 | 0 | 7 |
| 49 | 5 | 0 | 0 | 5 | 5 | 0 | 0 | 6 |
