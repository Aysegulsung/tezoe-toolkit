# checkpoint — DDL2-Batch3 (Worfa), session started 2026-09-10 ~10:00 UTC

Status at 2026-09-11 04:05 UTC: **NOTHING PUSHED YET — this session's proxy still refuses the store host.** The user
re-added `ymjviw-rz.myshopify.com` to the allowlist, but the CONNECT still returns 403 here: the allowlist applies to NEW
sessions (same rule as noted in rules/dataforseo-credentials.md). So the push must happen from a fresh session.

Everything up to the push is complete and was sent to the chat as `ddl2-batch3-work.tar.gz` (804 KB; no credentials
inside): 50 final/dNN.json (gate CLEAN, 6b/6c/6d + independent CTA review done), titles_final.json (title-check 0 FAIL,
head-check 0 FAIL), products.json (pre-push snapshot), collections.json (24 + the two collections created live on
2026-09-10: Packaging & Gift Boxes gid://shopify/Collection/485061066788, Footwear gid://shopify/Collection/485061099556),
category_ids.json, brief_flags.json, kw.txt, extract/, push/mut0-4.json + push/cta0-1.json + push/alt0-9.json (473 alts,
0 duplicates, seo both halves asserted), and the whole toolkit copy. 100 description images already re-hosted. dim_keep
0/0/50. backup-titles doc is in the project; kw-cache and backup-alt were sent to the chat.

## How a NEW session finishes the batch (do not re-process anything)
1. Attach `ddl2-batch3-work.tar.gz` to the chat; `tar xzf` it so the files land at /home/claude/work (it contains
   `work/…`). Re-create `work/secrets/shopify.json` from toolkit/shopify-api-credentials.md and
   `work/rules/dataforseo-credentials.md` from the project doc (both were excluded from the bundle on purpose).
2. `python3 shopify_api.py shop` → Worfa. Then `python3 shopify_api.py fetch DDL2-Batch3 live_pre.json` and confirm the
   live titles still equal products.json (nothing pushed). If they already equal titles_final.json, skip to step 4.
3. `for f in push/mut*.json push/cta*.json push/alt*.json; do python3 shopify_api.py mutate $f; done` — 17 files, expect
   `clean` on each.
4. `python3 shopify_api.py fetch DDL2-Batch3 live_after.json` → `python3 verify.py products.json live_after.json
   collections.json` → `python3 head_check.py live_after.json` → write `claude/run-log-ddl2-batch3.md` (numbers for the
   log: para_feat 78 KF flagged / 7 added / 71 dismissed, 15 SPEC flagged / 0 added / 15 dismissed (rulings_omit);
   KF/spec independent review 1 eligible of 50, 2 marked, 2 confirmed (p16); sections 0 of 50 (49 "What's in the Box"
   = package, p19/p29 spec/feature headings dismissed; p29 and p40 Size Guide added by agents); fact_cover 14 → 0 (c);
   6c read on all 50, corrected 33 products; CTA read on all 50; CTA independent review 38 marked, 29 confirmed, 9
   dismissed; re-read after corrections: p21, p31, p46 corrected again; DataForSEO 4,276 keywords, 5 calls ≈ $0.45;
   titles 46 at 70–120, 4 at 120–135 (trigger A); seasons 36 evergreen · 9 winter · 2 fall · 2 summer (+1 evergreen
   p04); coverage.md is in the bundle for the table).
