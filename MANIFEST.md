# toolkit MANIFEST — sha256 of every toolkit/rule doc as it should land on disk (refreshed 2026-09-07b, Tuzwa→Vepine store migration: 18 files re-hashed — CDN prefix, BRAND, comparison-table colours/heading and the tz-→vp- CSS hooks; desc-check.py re-hashed too — its line was already stale before the migration and the file was verified complete and compiling before rehashing)

Last refresh: 2026-09-29 — CM-batch26: gate.py (cta_count from brief_flags.json), build_payloads.py (category_map.json), verify.py (tags case-insensitive, duplicate collection titles first-wins), unit_dual.py (3M brand skip), DESC-SPEC.md (Tezoe CDN prefix), normalise_cm.py added (CM template normaliser); on top of 2026-09-28 — STORE CHANGE Worfa → Tezoe, whole block recomputed (see the 2026-09-28 refresh note), on top of 2026-09-15 unit_dual.py recomputed (word-form units, bag litres, count × value, axis label; see the last refresh note), on top of 2026-09-11 (later still) — list_bold.py added as a 57th line (bold Key Features / Specifications lead-ins, gap under image 2; gate.py, struct-check.py, rules/description-format-rule.md recomputed), after the same day's US units only in the budgeted elements (6 lines recomputed: unit_dual.py, compare_build.py, fit_build.py, rules/comparison-table-rule.md, rules/fit-block-rule.md, rules/description-format-rule.md), on top of the same day's kw_measure.py word-order guard (3 lines recomputed, a 56th line added: rules/kw-order-variant-rule.md),
on top of the 2026-09-10 Worfa go-live checks (7 lines: theme colours, store row, verified credentials),
after the same day's store change Vepine → Worfa (17 lines: BRAND, CDN prefix, host, rule docs, credentials),
on top of the same day's comparison-table mobile/desktop width fix and the rotated Shopify credential pair.

Purpose (clone route since 2026-09-17): the toolkit is cloned from https://github.com/Aysegulsung/worfa-toolkit into
/home/claude/work/, so nothing is re-typed any more. This manifest still proves, at zero model cost, that the clone and the
two credential docs written from the project are exactly the versions the rules below were tested with. (Before
2026-09-17 a copy agent re-typed each project doc; in blr-batch13 a Haiku copy agent truncated DESC-SPEC.md and
title-format-rule.md and doubled regex backslashes — the history notes below refer to that route.)

**Refresh note (2026-09-28, STORE CHANGE Worfa → Tezoe):** the whole block recomputed after the store change to Tezoe
(UK, GBP, host j4en3t-rf.myshopify.com, primary domain tezoe.com, main theme "Metro", CDN prefix
`cdn.shopify.com/s/files/1/0762/0873/4373/`). Changed: BRAND (compare_build.py, gate.py, verify.py), CDN prefix (gate.py,
struct-check.py, build_check.py, verify.py, rehost.py, extract_html.py, README-toolkit.md, usage-efficiency-runbook.md),
theme colours #121212 / #f6f6f6 (compare_build.py, fit_build.py, dim_image.py, comparison-table-rule.md, fit-block-rule.md),
store row 30-day returns confirmed by the user for Tezoe, DataForSEO location_code 2826 = United Kingdom (kw_measure.py,
title-format-rule.md §1), collections.json refetched (16 collections), and the UNIT SYSTEM flipped to metric-first /
metric-only for a UK store (unit_dual.py `metric_only()`, compare_build.py, fit_build.py, dim_image.py, title-check.py §5
now FAILs imperial units in titles; rule docs title-format-rule.md §5, description-format-rule.md, comparison-table-rule.md,
fit-block-rule.md, dimension-image-rule.md, EXTRACT-SPEC.md, DESC-SPEC.md). Both credential docs rewritten for Tezoe
(project: toolkit/shopify-api-credentials.md and claude/dataforseo-credentials.md — the second lives under claude/ because
the project tool cannot write to the root; README step 0 reads it from there). Copy spelling (US English) unchanged — separate decision.

**Refresh note (ddl2-batch28, 2026-09-21):** three lines ADDED — `./fix_sections.py`, `./spec_parse.py` and
`./build_payloads.py`, new toolkit scripts written for this batch's supplier template and committed with it.
No existing line changed. Why they exist:
- `fix_sections.py` — `sections.py --extract` mis-read this supplier's template: it filed the "Why You'll Love It"
  feature block as a fact SECTION on 49 of 50 products (moving 91 lines out of `key_features`), and auto-mapped six
  marketing lead headlines to canonical section names off a stray keyword ("Refined Glow, Architectural Design" →
  `Design`), the failure class the 2026-09-09 shape tests were added to catch. The script does the [UNMAPPED] triage
  that README step 3e hands to the main context as CODE, so all 50 products are treated identically instead of by
  eye: WYLI block → `key_features`, a pseudo-section whose heading is a spec label already in `extract.specs` →
  dropped, a comma-pair marketing headline over prose → dismissed as the description's own lead.
- `spec_parse.py` — 37 of 50 sources wrote the whole spec table as ONE run-on sentence in a single `<p>`, so
  `extract_html.py`'s list parser found nothing and `spec_cover.py` would have had no source side. Splitting on
  "capitalised words + colon" does not work here because the VALUES are capitalised too, so the label boundary is
  decided by a LEXICON of spec labels, matched longest-first at each colon; a colon whose preceding words are not in
  the lexicon is left alone rather than guessed. 324 spec rows recovered. The extraction agents still verify every
  row by eye against the source sentence — in ddl2-batch28 they fixed 8 products' parses, and on p46 the lexicon's
  duplicate-label dedupe had silently dropped 7 of 11 pairs, so read that check as load-bearing, not a formality.
- `build_payloads.py` — README step 7's payload pass as a committed script instead of ad hoc code per batch:
  rewrites.json plus push/mut*.json (10 aliased `productUpdate`), push/cta*.json (`metafieldsSet`, 25 per call) and
  push/alt*.json (`fileUpdate`). It also picks the Shopify taxonomy leaf per product and rewrites
  `category_proposal` in final/dNN.json to that leaf's exact name — five description agents wrote three different
  names for one leaf ("Wall Lights" / "Wall Lighting" / "Wall Lamps"), and verify.py check 8 compares the LIVE
  category name with the proposal, so unifying it in the builder is what keeps that check meaningful. The per-product
  leaf map at the top is store-agnostic but batch-specific: review it for a batch of other product families.

**Refresh note (2026-09-21b, Safety Notes rule change):** seven lines recomputed after a deliberate RULE CHANGE the
user made the same day — the Backend doc's Safety Notes medical-claims paragraph was rewritten, so a health benefit
the SOURCE itself states is now KEPT rather than softened or removed, while disease-treatment claims ("heals",
"treats", "cures", "prevents" a named condition) and "clinically proven" / "doctor recommended" / "FDA approved" stay
forbidden unless the source states them. The seven docs carrying that sentence were updated in the project and then
uploaded to the repo: `./rules/PROJECT-DESCRIPTION.md`, `./rules/description-format-rule.md`,
`./rules/comparison-table-rule.md`, `./rules/cta-benefits-metafield.md`, `./DESC-SPEC.md`, `./README-toolkit.md`
(step 6b, both of its lines) and `./fact_cover.py` (its 6b triage docstring). Each file was diffed against the
pre-change commit before its line was recomputed and carried ONLY that rule change — so this is §6's "stale manifest
on a correct copy", not a corrupted upload. Two files were uploaded into the repo by mistake in the same round and
should be deleted from it: `MANIFEST.sha256` (generated by step 0 every run, gitignored) and `gitignore.txt`
(it was meant to replace `.gitignore`, which still needs the per-batch lines DESC-BATCH-NOTE.md, rewrites.json,
build_NN_NN.py).

## Use (README-toolkit.md step 0)
1. Write the two credential docs from the project to `./shopify-api-credentials.md` and `./rules/dataforseo-credentials.md`.
2. `sed -n '/^```$/,/^```$/p' MANIFEST.md | grep -v '^```' > MANIFEST.sha256 && sha256sum -c MANIFEST.sha256 --quiet && echo TOOLKIT OK`
3. A FAILED script / rule line: the repo and this manifest disagree — stop and report, never patch by hand.
4. A FAILED credential line: the project doc changed after the last refresh — re-read it once; still failing = recompute
   that line here and commit it.
5. build_check.py is edited by the title step (FR/EXTRA per batch) — its checksum is for the pristine repo version only.

## Keep in sync
Whenever a toolkit or rule doc changes in the project, recompute its line (`sha256sum <file>`) and replace it here in the same
turn — a stale manifest fails on a correct copy.

**Refresh note (BLR-BATCH19, 2026-09-04):** four lines were stale — README-toolkit.md, rules/description-format-rule.md,
rules/rule-overlap-deferred.md and usage-efficiency-runbook.md failed against the previous hashes. README-toolkit.md was
verified against the source read in the main context; the other three were verified by an independent second copy. All four
lines below were recomputed from verified copies of the current project docs. The remaining 21 lines are unchanged from the
TRIMMERYENI refresh and passed on the first copy.

**Refresh note (BLR-BATCH21, 2026-09-04):** one line was stale — `rules/description-format-rule.md`. Two independent copies of
the project doc agreed byte-for-byte with each other and disagreed with the manifest, so per §6 the manifest line was stale,
not a corrupted copy. That line was recomputed from the verified copy. The remaining 24 lines passed on the first copy.

**Refresh note (BLR-BATCH22, 2026-09-04):** two lines were stale on the session copy — `./EXTRACT-SPEC.md` and
`./rules/description-format-rule.md`. For each, two independent copies agreed byte-for-byte and disagreed with the manifest,
so per §6 both manifest lines were stale, not corrupted copies. Both were recomputed.

**Refresh note (BLR-BATCH22 follow-up, 2026-09-04):** two lines recomputed after a deliberate RULE CHANGE, not a copy problem
— `./rules/description-format-rule.md` (whole-description ceiling raised 430 → 500 words by user decision) and
`./struct-check.py` (the same number in code). Both project docs were updated in the same turn as this manifest.

**Refresh note (BLR-BATCH22 follow-up 2, 2026-09-04):** a 26th line — `./spec_cover.py`, a new script gate added at the
user's request after the 112 missing spec lines. `./gate.py` (wires the new check), `./DESC-SPEC.md` and
`./README-toolkit.md` (document it) were recomputed in the same turn.

**Refresh note (2026-09-05, opener identity clause):** one line recomputed after a deliberate RULE CHANGE —
`./rules/title-format-rule.md` (§3 rule 2 opener identity clause, §1 product-type lookup, §10b consistency; user decision
after the blr-batch21 door-knocker review). The project doc and this manifest were updated in the same turn. Recomputed again the same day after §5
"measured specs are keywords" was added (user decision).

**Refresh note (2026-09-05, opener-fix run):** `./README-toolkit.md` recomputed after step 7 gained the "seo is replaced
whole" note (user-approved) — the opener-fix push had cleared seo.description on 42 products by sending seo.title alone.

**Refresh note (2026-09-05, head-noun test):** a 27th line — `./head_check.py`, the §3 rule 2 head-noun test script
(user decision after the cat-hammock review). `./rules/title-format-rule.md` (the "typical member" exception replaced by
the head-noun test + synonym list) and `./README-toolkit.md` (steps 5 and 8 call head_check.py) recomputed in the same
turn.

**Refresh note (2026-09-05, ceiling never drops a source line):** `./struct-check.py` (total words > 500 is now a WARNING,
not a FAIL — spec_cover.py / value_check.py remain the failing gates) and `./rules/description-format-rule.md` (the same
sentence in the length-budget section) recomputed after a user instruction. Recomputed again the same day: prose has no
paragraph cap and no word ceiling any more (source meaning decides, no padding) — struct-check warns above 110, never fails. Third recompute the same day: a description with no source image gets two gallery
images at the skeleton slots (user instruction); struct-check fails on fewer than two images.

**Refresh note (BLR-BATCH23, 2026-09-05):** two lines were stale on the session copy — `./EXTRACT-SPEC.md` and
`./rules/cta-benefits-metafield.md`. For each, THREE independent copies of the project doc (the copy agent's two, plus a
third read in the main context diffed against the file on disk) agreed byte-for-byte and disagreed with the manifest, so
per §6 both manifest lines were stale, not corrupted copies. Both were recomputed. The remaining 25 lines passed on the
first copy.

**Refresh note (BLR-BATCH23 run, 2026-09-05):** two lines were stale on this session's copy —
`./rules/description-format-rule.md` and `./rules/title-format-rule.md`. Both project docs had been edited (09:52 and 09:58 UTC)
after the previous manifest refresh took its hashes from an earlier on-disk copy. Two independent copy agents produced
byte-identical files for both docs and both disagreed with the manifest, so per §6 the manifest lines were stale, not
corrupted copies. Both were recomputed. The remaining 25 lines passed on the first copy.

**Refresh note (BLR-BATCH23 run, gate/image-floor mismatch, 2026-09-05):** `./gate.py` recomputed after a code fix, not a
copy problem. The same-day "never fewer than two images" decision was written into `rules/description-format-rule.md` and
`./struct-check.py` but NOT into `./gate.py`, whose older image check still demanded `src_new == src_old` exactly — so a
product with 0 or 1 source image could not pass both gates at once (three did so in this batch: p29, p37, p43). gate.py now requires the source images to be an unchanged PREFIX of
the description's images and the total to equal `max(len(source), 2)`; for a product with 2+ source images this is exactly
the old equality check, so nothing was relaxed. The project doc was updated in the same turn as this manifest.

**Refresh note (BLR-BATCH23 run, a 28th line, 2026-09-05):** `./rules/PROJECT-DESCRIPTION.md` added at the user's request.
DESC-SPEC.md has required this doc read in full since 2026-09-04, but it was never added to this list, so every run
discovered it missing and fetched it with a separate agent (~0.08M subagent tokens per batch). Its hash was taken from a
copy verified per §6: two independent copies agreed on every byte of content, differing only in a trailing newline; the
newline-terminated form is canonical because that is what a heredoc copy produces. `./README-toolkit.md` recomputed in the
same turn — step 0 now says the rule docs are exactly the `./rules/…` lines of this manifest and names this one.

**Refresh note (BLR-BATCH23 run, a 29th line — fact coverage, 2026-09-05):** `./fact_cover.py` added at the user's
decision, and `./README-toolkit.md` recomputed for its step 6b. Reason: the user read the live blr-batch23 listing for
p05 and found the source line `Hygienic and non-absorbent, which helps prevent bacterial buildup` missing from the new
description. Nothing had checked it — `value_check.py` covers numbers, list items, package items and variant options,
so a source sentence carrying no number could be dropped silently. `fact_cover.py` scores every `facts` line against
the finished description and prints those under 55% for main-context review; it is NOT part of gate.py, so the
description agents never see it and it costs no agent turns. It is a review aid, not a gate — it always exits 0,
because word overlap cannot tell a rewrite from an omission.

**Refresh note (2026-09-05, medical-claim rule rewritten):** `./rules/PROJECT-DESCRIPTION.md` recomputed after a
deliberate RULE CHANGE, not a copy problem. The Safety Notes line "Medical/health claims: remove or soften" was too
blunt — it was pushing the customer's own problem out of the copy on products bought precisely for that problem. At the
user's decision it now permits naming the problem and the intended use (pain relief, sciatica, back support) and forbids
only unevidenced physiological outcomes (reduces inflammation / blocks pain signals / speeds recovery / heals / treats /
cures), and requires the source's own disclaimer sentence to be kept. Note: the doc is a mirror of the project's
description field, which the tools cannot edit — the user updates that field in the UI so the two do not drift.

**Refresh note (BLR-BATCH24 run, 2026-09-05):** five lines FAILED on this session's copy; per §6 a second independent
copy agent re-copied all five and the two copies were compared.
- Four were STALE manifest lines, not corrupted copies — both copies agreed byte-for-byte and disagreed with the manifest:
  `./TITLE-SPEC.md`, `./build_check.py`, `./title-check.py` and `./rules/title-format-rule.md`. All four project docs were
  edited at 13:12 UTC on 2026-09-05, after the previous refresh took its hashes. All four lines were recomputed below.
- One was a GENUINE COPY CORRUPTION: `./EXTRACT-SPEC.md`. The second copy matched the existing manifest line exactly
  (`e34f6ce3…`) while the first copy did not, so the first copy was discarded and replaced with the verified one. That
  manifest line is unchanged.
The remaining 24 lines passed on the first copy. After the fix, `sha256sum -c MANIFEST.sha256 --quiet` printed TOOLKIT OK.

**Refresh note (2026-09-06, source-title windows — a 30th line):** `./source_windows.py` added at the user's decision after
the blr-batch24 source-title audit. Every 2–4-word contiguous window of the 50 source titles was checked against the batch's
kw-cache: 368 phrases had never been measured; one $0.09 call returned 74 of them at ≥ 1,000 and 22 at ≥ 20,000, among them
`essential oil diffuser` 74,000 (#35 had opened on `aromatherapy diffuser` 14,800 — a rule 2 miss), `flip flops` 135,000,
`card holder` 60,500, `coat rack` 49,500, `salt lamp` 27,100. The §1 "source title's own keywords are always measured"
split is now this script (exhaustive, zero model tokens) instead of the extraction agent's judgment. `./README-toolkit.md`
(step 4) and `./rules/title-format-rule.md` (§1, header note, §10.2 worked example) recomputed in the same turn. Measurements saved
in `claude/kw-cache-blr-batch24-addendum.md`.

**Refresh note (2026-09-06, source-window gate in title-check.py):** three lines recomputed after a deliberate RULE CHANGE
(user decision, same day as the script): `./title-check.py` now FAILS the batch when any 2–4-word window of a source title is
missing from kw.txt, or when products.json is not on disk — so a skipped README step 4 cannot reach the store. It imports
`source_windows.py` for the split. `./README-toolkit.md` (step 4 push-blocking note) and `./TITLE-SPEC.md` (inputs + step 3
third FAIL) recomputed in the same turn. Tested: missing windows → FAIL, windows present → 0 FAIL, snapshot absent → FAIL.

**Refresh note (2026-09-06, cluster-core gate):** four lines recomputed after a deliberate RULE CHANGE (user decision, after
the same blr-batch24 audit). `./title-check.py` now FAILS any comma cluster of a title that contains no measured 2+-word
phrase — the cluster's core must be a measured keyword; attributes and for/with tails stay free; `10 Pack`-type clusters are
exempt; apostrophes and word order are ignored. On the 50 pushed blr-batch24 titles it fails exactly the 5 clusters the audit
found by hand (#05 #09 #12 #16 #38) and passes the other 149. `./rules/title-format-rule.md` (§2 clause + header note),
`./TITLE-SPEC.md` (step 3 fourth FAIL) and `./README-toolkit.md` (step 5) recomputed in the same turn.

**Refresh note (2026-09-06, old-vs-new volume gate):** four lines recomputed after a deliberate RULE CHANGE (user decision).
`./title-check.py` now FAILS a title when the OLD title captured more product-naming volume (last word = productType head,
fit-rejects excluded) than the new one, and WARNs on total volume. Needs `old_title` in check_products.json (or product_id /
index against products.json) — build_check.py must supply it; when absent the check reports NOT RUN as a WARN. Tested on 7
blr-batch24 products with their real volumes: #35 fails (96,460 → 15,060, `essential oil diffuser` dropped), the other six
pass, and parent-category words in supplier titles are excluded with or without a fit_reject list. `./rules/title-format-
rule.md` (§2 clause + header note), `./TITLE-SPEC.md` (step 3 fifth FAIL), `./README-toolkit.md` (step 5) and `./build_check.py` (now writes `old_title` +
`product_id` per entry from products.json) recomputed.

**Refresh note (2026-09-06, unused-keyword gate, option b):** five lines recomputed after a deliberate RULE CHANGE (user
decision). `./title-check.py` now FAILS a title when a measured, fit-clean candidate (>= 1,000, not captured, not a twin of a
captured keyword) beats the weakest non-opener cluster's value and no reason is written for skipping it; with a reason
(`skip_reasons.json`, copied into check_products.json by `./build_check.py`) the line is MANUAL and the reason is saved in
rejects.json. A reason for a longer/shorter form of the phrase covers the family. Tested on the TRIMMERYENI #08 case: FAIL
without a reason, MANUAL with one. `./rules/title-format-rule.md` (§3 rule 2 clause + header note), `./TITLE-SPEC.md` (step 3
sixth FAIL, inputs) and `./README-toolkit.md` (step 5) recomputed.

**Refresh note (2026-09-06, cta-check restored in gate.py):** two lines recomputed after a CODE FIX, not a copy problem
(user instruction). `./cta_check.py` was wired into `./gate.py` as its last step in blr-batch21 (2026-09-04), but the
2026-09-05 image-floor rewrite of gate.py (the BLR-BATCH23 note above) was written from a version that did not carry the
call, so the project's gate.py has run without the CTA language check since then — the blr-batch23 run log's
"cta-check 0 FAIL" line came from the on-disk file of that session, not from this project copy. gate.py now calls
`cta_check.py` again after value-check; tested on a fixture: `Sizes S-XXXL` and `Adjustable brightness` FAIL, `Runs 7 days
per charge` passes. A 31st line — `./cta_check.py` — is added below: the blr-batch21 note said the manifest carried it, but the
list had no such line, so the session-start copy had no reason to fetch the file at all; the hash is of the project copy
re-written from the tested fixture in the same turn. `./DESC-SPEC.md` recomputed in the same turn: its gate list names cta-check, and its struct-check
summary no longer says "total 350–430 words" / "prose 65–110 in ≤2 <p>" (both superseded on 2026-09-05 — above 500 / above
110 are WARNs, never FAILs, and never a reason to drop a source line).

**Refresh note (2026-09-06, gate.py exit code + README step 6):** three lines recomputed after a CODE FIX (user decision).
`./gate.py` used to exit 0 whatever its sub-checks printed, although its docstring said "exit 0 only if all clean"; it now
counts its own [FAIL] lines, title-check [FAIL] lines and the non-zero exit codes of desc-check, struct-check, spec_cover,
value_check and cta_check, prints `=== gate: CLEAN ===` or `=== gate: N problem section(s)/lines ===`, and exits 1 on any
problem. Tested on a fixture: two bad CTA lines → exit 1; same product with benefit CTA lines → CLEAN, exit 0. WARN-only
output (prose > 110, total > 500, verbal-value warnings) still exits 0. `./README-toolkit.md` step 6 recomputed: it now
names cta_check.py among the gate's checks and states the exit-code contract. `./DESC-SPEC.md` recomputed: its gate
paragraph states the same contract instead of the earlier "exit code is not the verdict" sentence.

**Refresh note (2026-09-06, link / URL / price gate):** two lines recomputed after a CODE ADDITION (user instruction).
`./gate.py` now FAILS a product when any customer-facing field (descriptionHtml with `<img>` tags removed, title,
seo.title, seo.description) carries an `<a>` tag, a URL (`http(s)://`, `www.`, `mailto:`), an e-mail address, or a price
(`$ € £ ₺` + digit, `USD/EUR/GBP/TRY/TL`, `dollars/euros/pounds`). Until now gate.py checked only our own brand name, so the
format rule's "delete any link, brand name, or price found in the source" had no script behind its link and price halves.
Tested on a fixture: `<a href>`, `www.shop.com`, `$12.99`, `20 USD` → 4 FAIL, exit 1; a clean description with `32 oz` and
`24 hours` → CLEAN. A foreign BRAND name cannot be detected by a generic script and remains a RULINGS / review matter — this
gate does not claim to cover it. `./DESC-SPEC.md` recomputed: its gate list names the check.

**Refresh note (2026-09-06, a 32nd line — verify.py):** `./verify.py` added at the user's decision. README step 8 has
asked since 2026-09-03 for a script comparison of every live field after the push, and every run log reports
"verify.py … 0 failures" — but the script was never a project doc, so each session re-wrote it from the step-8 sentence
and no two batches necessarily checked the same fields (the same "session-only code" failure that spec_cover.py fixed
for the spec check in blr-batch22). The file was written from README step 8 plus the blr-batch13 / blr-batch23 run-log
descriptions of the checks, not recovered from any earlier session (none was saved). Fixture-tested: a correct live copy
→ 17 checks, 0 failures, exit 0; a copy with a wrong title, changed description text, 161-char seo.description, a dropped
tag + a duplicated season tag, changed status, wrong CTA JSON, a missing collection, a swapped media alt, a changed
variant price and a duplicate alt → 10 failures named one per line, exit 1. Shopify's own HTML re-formatting (whitespace
between tags, entity encoding) is normalized away; a mismatch says whether the tag-stripped TEXT differs or only the
formatting. First real-batch use: read its output in full — it has run on a fixture, not yet on a live batch.
`./README-toolkit.md` step 8 recomputed: it now names the command and the check list.

**Refresh note (2026-09-06, verbal spec values FAIL):** two lines recomputed after a deliberate RULE CHANGE (user decision).
`./value_check.py`: a numberless, non-list spec value ("Material: cotton", "Closure: zipper") whose content-word stems are
fewer than half present in the description is now a FAIL, not a WARN — until now "cotton" → "polyester" only warned while
"300 g" → nothing failed, and spec_cover.py passes such a line as long as the NAME word matches. `omit_per_ruling` now also
accepts the `Name: value` form ("Type: Other") beside the bare value. Fixture-tested: cotton/zipper present + "Type: Other"
exempted → 0 FAIL; polyester/magnetic instead → 3 FAIL, exit 1. `./DESC-SPEC.md` gate line recomputed. Expect a few more
gate FAILs per batch on supplier boilerplate lines; each is resolved by a RULINGS.md omission, never by silence.
`rules/description-format-rule.md` was NOT edited (its "Gate" paragraph already says value_check FAILs on dropped values).

**Refresh note (2026-09-06, a 33rd and 34th line — assume_check.py, age_check.py):** two scripts added at the user's
decision, and `./gate.py`, `./DESC-SPEC.md`, `./README-toolkit.md` recomputed for them.
- `./assume_check.py` — the "ADD NOTHING BEYOND THE SOURCE" gate. DESC-SPEC.md has carried the forbidden-assumption family
  since blr-batch12 (machine washable / no app / free app / BPA-free / food-safe / dishwasher / hand wash / power-cut memory /
  lifetime / warranty / certified / universal / waterproof vs water-resistant / sweat-dust-shock-proof / fast charging /
  silent / eco / non-toxic / natural / odorless / hypoallergenic / printed / "than ordinary" / "stronger than" / "X times"),
  but nothing enforced it — value_check, spec_cover and fact_cover only look for what is MISSING. For each family the
  description and SEO fields are scanned; a hit FAILs unless the extract (facts, specs, package, how_to_use, faq_source,
  variants, old title/seo, productType, identity) contains the family's own source pattern. Wired into gate.py before
  cta-check; exit code counts. Exemption: `add_per_ruling` in final/dNN.json (new optional field in DESC-SPEC's schema).
  Fixture-tested on the blr-batch12 inventions: "machine washable" from "washable", "waterproof" from "water-resistant",
  "no app required" and "free app" from "smartphone app", "remembers settings after a power cut" from "memory function:
  yes", "printed manual" from "user manual", "stronger than ordinary", "BPA-free", "certified" in seo.title, "universal" in
  seo.description → all FAIL; the same product written from the source's own words → 0 FAIL; "CE certified" with an
  `add_per_ruling` entry → [exempt]. The product TITLE is not scanned (title fit is title-check's job, §6).
- `./age_check.py` — description-format-rule.md "Age ranges", WARN only (user decision): a single-age phrase ("toys for 4
  year olds") whose sentence states no range, one that is not a title keyword, or more than one such phrase per product.
  Wired into gate.py after assume-check; never sets the exit code. Tested on the ddl1-batch5 magnetic-game text (three
  single-age sentences, no range) → 5 WARN; the corrected sentence ("… 4 year olds through age five, ages 4-5+") → 0.

**Refresh note (2026-09-06, README step 6c — benefit review by eye):** `./README-toolkit.md` recomputed after a PROCESS
RULE was added at the user's decision: before payloads, the main context reads every product's H2 + 5 bullets + 3 CTA
lines against the "Which five benefits" / "HANGİ 3 BENEFIT" filters and writes the outcome to the run log (corrected
product numbers, or an explicit "no correction" line). This was done ad hoc in blr-batch13 and skipped in blr-batch21;
it is not scriptable, so the rule makes the omission visible in the log instead. Cost: main-context reading of ~10 short
lines per product; no new agent, no new call.


**Refresh note (2026-09-06, a 35th line — rehost.py):** `./rehost.py` added at the user's decision after blr-batch25. README
step 5b (image re-host, Q14) had been written ad hoc every batch; in blr-batch25 the ad hoc script kept the `fileCreate`
ids only in memory, crashed on three Shopify "Internal Server Error" responses, and the three overlapping re-runs left
~50 duplicate copies in Files. The script now writes the created ids to image_ids.json after every group of 10, retries
every Admin API call up to 6 times, resumes from that file on a re-run (nothing uploaded twice), polls to READY, rewrites
the extract srcs (old value kept as `src_original`) and prints one summary line; exit 1 while anything is still foreign.
Tested with a mocked Admin API: a hard crash after the first group → the re-run creates only the remaining 6 of 16, no
duplicates; a second run on a finished batch is a no-op. `./README-toolkit.md` recomputed in the same turn (step 5b added,
store-constants note updated). First live run of the toolkit copy is the next batch — read its summary line.

**Refresh note (2026-09-06, DESC-SPEC "before you return" list):** `./DESC-SPEC.md` recomputed after a PROCESS note was added
at the user's decision — no rule, gate or threshold changed. In blr-batch25 all five description agents passed gate.py on the
first pass and were still sent back four times for things the rule documents already say: rule-1 WARNs on 30 products,
keywords doubled inside one bullet, all ten H2s of one agent written as sentences, aesthetics/variant CTA lines, synonym-only
second-net sentences, one agent altering the product title, a fit-rejected head word in a description. Each correction round
re-reads the agent's whole accumulated context, so those rounds cost about as much as the first pass. The seven-point list
puts those existing requirements in the agent's working spec so the first pass is the finished pass; the documents are
still read in full and the main-context 6b/6c review is unchanged.

**Refresh note (2026-09-06, README 6d — 6b + 6c in one message):** `./README-toolkit.md` recomputed after a PROCESS note
was added at the user's decision — no rule, gate or threshold changed. The main context still reads every fact_cover line
and every product's H2 / bullets / CTA lines; it now sends both correction lists to each description agent in one message
(one return per agent instead of two — blr-batch25 spent ≈1.2M tokens on the second round for the same output) and re-runs
fact_cover.py after the corrections, diffing against the first run, because a 6c edit can move a fact. Same turn: 6d also requires the main context to re-read by eye the lines the 6c
corrections changed (word matching cannot see a meaning drift) — user decision.

**Refresh note (2026-09-06, DESC-SPEC item 8 — prose two paragraphs, customer first):** `./DESC-SPEC.md` recomputed after
a PROCESS note was added at the user's decision (no rule, gate or threshold changed — description-format-rule.md already
allows a second paragraph and, since 2026-09-05, sets no prose ceiling). Reason: the user read the live blr-batch25 p38
(candle warmer) and found the single 90-word paragraph opening on the mechanism ("GU10 halogen bulb…") while the source's
three paragraphs carried the customer's moment (scent fills the room, no flame, no tunnelling). Item 8 fixes the order —
paragraph 1 = customer scene/benefit, paragraph 2 = how it works — and states that 65–110 is the norm, not a ceiling, so
agents stop treating it as one; every extra sentence must carry a source fact or a new keyword. Same day, same item: paragraph 1's last sentence closes the
buyer's biggest objection the source answers (user decision) — no new claim, source words only.

**Refresh note (2026-09-06, comparison table — a 36th and 37th line):** `./compare_build.py` and
`./rules/comparison-table-rule.md` (project path `claude/comparison-table-rule.md`) added at the user's decision (CVR element: a "Vepine vs Others" table in every
description). The agent writes only a `compare` object (2–5-word name + 5 source-fact rows, at least one Others cell
neutral); the script renders the fixed theme-coloured HTML, inserts it directly before `<h3>Key Features</h3>`, and FAILs
a missing / untraceable / all-✘ table. Six lines recomputed in the same turn: `./gate.py` (calls compare_build.py first;
brand scan now ignores the block — the store name is allowed there and nowhere else), `./struct-check.py` (block
mandatory, exactly one, before Key Features; its words excluded from the word budget), `./verify.py` (check 15 ignores the
block, new check 17: exactly one block live), `./DESC-SPEC.md` (schema + gate list), `./README-toolkit.md` (steps 6, 6c,
8, store constants), `./rules/description-format-rule.md` (skeleton line + hard-rule note). Fixture-tested: clean object →
rendered, idempotent on re-run, brand check silent; all-✘ / untraceable row / comparison wording / missing object / brand
inside name → FAIL; `Vepine` in prose → still FAIL; struct-check without the block → issue. First live use is the next
batch — screenshot the block on the theme and compare with the rule's colour list.
Same day, follow-up (user decision): the table is OPTIONAL per batch — brief question **Q17 — Comparison table: (Add
"Vepine vs Others" table / No table)**, unanswered = No table. `brief_flags.json` (`{"q17_compare_table": true|false}`,
written in README step 1) is read by compare_build.py / struct-check.py / verify.py; with No table the script removes any
existing block and nothing is required. Seven lines recomputed (all but gate.py). Tested: no flag → block removed, struct
silent; flag true → block required, rendered, struct silent.
Third note, same day (user decision): thin source still gets five rows — plain facts become NEUTRAL rows, nothing
invented; a source with fewer than five separable parts opts out with `"compare": null` + notes_for_log "compare: source
too thin" (compare_build.py FAILs a null without the log line; struct-check / verify.py expect no block for it). Five lines
recomputed. Tested: null unlogged → FAIL; null logged → no block, all three checks silent; normal → rendered.

**Refresh note (2026-09-06, Q18 dimension image — lines 38–40):** `./dim_image.py`, `./dim_attach.py` and
`./rules/dimension-image-rule.md` (project path `claude/dimension-image-rule.md`) added at the user's decision: an optional
per-batch size infographic built by script (rembg u2netp cut-out of the product's own gallery photo + navy dimension lines
+ size table, figures only from the source's L×W×H pattern), attached as gallery image 3 with the existing images shifted
down. `./README-toolkit.md` (step 1 flag, new step 7b, step 8) and `./verify.py` (media order = snapshot + inserted image;
alt checked) recomputed. Fixture-tested: build from a local photo → correct cut-out, lines on the product edges, M/L table;
`:g` float formatting replaced so `11.0` prints as the source wrote it. NOT tested live: the staged-upload PUT (storage
host may need the egress allowlist) and productReorderMedia — first Q18 batch reads dim_attach.py's output line by line.

**Refresh note (2026-09-06, Q19 fit block — lines 41–42):** `./fit_build.py` and `./rules/fit-block-rule.md` (project
path `claude/fit-block-rule.md`) added at the user's decision: an optional per-batch "Right for you if / Not the right
fit if" two-column block, content from the description agent's `fit` object (3–4 for / 2–3 not-for lines, every not-for
line derived from a source fact), HTML by script, rendered after the comparison block before `<h3>Key Features</h3>`;
`"fit": null` + logged reason opts a product out. `./gate.py` (calls fit_build.py after compare_build.py; brand scan
strips both blocks), `./struct-check.py` (block count / position per Q19; words outside the budget; the comparison-block
position check tolerates the fit block between it and Key Features), `./verify.py` (check "fit block"), `./DESC-SPEC.md`
(schema + gate list) and `./README-toolkit.md` (steps 1, 6, 6c, 8, rule-doc paths) recomputed. Fixture-tested: both
blocks render in order compare → fit → Key Features, re-run idempotent, struct silent; one not-for line / untraceable
line → FAIL; null + log line → no block, silent; "larger than the L size" passes (limit, not comparison).
Same day, RULE CHANGE (user decision — a wrong "not for" line kills a sale silently): `./fit_build.py`,
`./rules/fit-block-rule.md`, `./DESC-SPEC.md` recomputed. not_for is now 0–2 lines, each must carry a measurable limit
(number+unit, size label, indoor/outdoor, compatibility) and must not contain a preference/behaviour verb; with no such
limit the block renders as the left column only. Tested: preference line → FAIL; no-limit line → FAIL; 3 lines → FAIL;
one dimension line → two columns; [] → one column, struct silent, re-run idempotent.
Same day: `./compare_build.py` and `./fit_build.py` recomputed — every NUMBER written in a comparison row or a fit line
must occur in the source text (user question: value_check guards presence of source values, nothing guarded a number
invented in a block). Tested: 22.4 passes, 24.2 → FAIL, 23.4 in a compare row → FAIL.
Same day, two corrections (user asked "any other gaps?"): `./rules/comparison-table-rule.md` and `./DESC-SPEC.md`
recomputed — (1) text printed on source images is NOT a source (the agents never see images; the earlier wording
suggested it was); (2) "when in doubt, neutral, not ✘" — an Others ✘ is written only for a feature a cheap alternative
plainly lacks; 2–3 neutral cells of 5 is normal.

**Refresh note (BLR-BATCH26 test product, 2026-09-06 — fit block one column, before FAQs, exactly 4 lines):** seven lines
recomputed after a deliberate RULE CHANGE (user decision, after reviewing the live test product p00 of blr-batch26).
`./rules/fit-block-rule.md` (project path `claude/fit-block-rule.md`): the block is a single column "Right for you if"
only — the "Not the right fit if" column and the `not_for` key are removed for good (a wrong "not for" line kills a sale
silently); the block moves from before Key Features to directly before `<h3>FAQs</h3>`; the line count is fixed at
exactly 4 (three lines look empty in one column; a product that cannot fill four honest lines opts out with `"fit": null`).
The comparison block stays before Key Features (same decision: the table persuades early, the fit block closes the
decision late). `./fit_build.py` (single-column render, insert before FAQs, exactly 4 `for` lines, `not_for` ignored and
reported), `./struct-check.py` (fit block directly before FAQs, no "Not the right fit if" text; the comparison-block
position check no longer tolerates a fit block between it and Key Features), `./verify.py` (check "fit block" now also
requires the before-FAQs position and the one-column condition live), `./gate.py` (comment), `./DESC-SPEC.md` (schema:
`fit.for` exactly 4 lines, no `not_for`; gate list) and `./README-toolkit.md` (steps 6, 6c, 8) recomputed in the same
turn. Tested on p00: 4 lines → rendered before FAQs, gate CLEAN, live verify 19 checks 0 failures; 3 lines → FAIL; a
stray `not_for` key → ignored with a printed line; the pushed p00 carries the new layout.

**Refresh note (BLR-BATCH26, 2026-09-06 — cta_check.py two gaps closed):** three lines recomputed after a CODE ADDITION
(user decision, after checking p45 and p47 live). `./cta_check.py`: (1) the DESC-SPEC "≤30 chars text" limit is now
measured — a longer line FAILs (11 live lines in this batch were 31–33 characters and nothing had caught them);
(2) counts written as words ("Seven colors, one remote", "Six modes for every need") and included-accessory lines
("with remote", "4 nozzles included") now FAIL like digit counts do — the old pattern matched `\d+` only, so eight
products reached the store with feature-count CTA lines that the 6c reading also missed. `./gate.py` format check
tightened from 34 to 30 characters to match. `./DESC-SPEC.md` gate line names both. Fixture-tested: the three bad forms
→ 3 FAIL; `Runs 7 days per charge` and `Up to 4 hours cordless` still pass; a 33-character line → FAIL; all 50 live
blr-batch26 CTA sets → 0 FAIL after the same-day corrections.

**Refresh note (BLR-BATCH26, 2026-09-06 — CTA examples + named CTA pass):** two lines recomputed after a PROCESS addition
(user decision, no gate or threshold changed). `./rules/cta-benefits-metafield.md` gains a "Gerçek örnekler — blr-batch26"
section: the eight ❌ CTA lines that passed cta_check and the 6c reading in this batch and were caught only by the user
(feature counts, mode descriptions, audience lines, aesthetics), each with the ✓ line written from the same source facts,
plus the one-sentence test ("can it be read as 'that problem is gone'?") and the script-measured 30-character limit.
`./README-toolkit.md` 6c: the CTA lines are now read as their own named pass after the bullet / table / fit reading and the
run log carries a separate "CTA read on all N …" line — a log without it means the pass was skipped.

**Refresh note (BLR-BATCH26, 2026-09-06 — a 43rd line: CTA-REVIEW-SPEC.md, independent CTA reader):** `./CTA-REVIEW-SPEC.md`
added at the user's decision (CTA lines are the page's most important element; "I don't want to miss anything there").
One Sonnet agent per batch reads only each product's facts/specs + its three CTA lines — no description, no title — and
marks CERTAIN failures only (feature counts, what-it-does lines, audience/occasion lines, variant facts, unsourced
outcomes); runtime-per-charge figures and borderline lines are deliberately NOT marked so the pass adds no false-alarm
load. It never rewrites; the main context reads every mark, sends real misses back in the 6b/6c message and logs
`CTA independent review: N marked, K confirmed …`. Cost ≈ 0.1M tokens per 50 products; zero risk to output (it only
marks). `./README-toolkit.md` 6c recomputed (the step and its log line). The session-start copy list now has 43 lines.

**Refresh note (BLR-BATCH26, 2026-09-06 — CTA order rule):** `./rules/cta-benefits-metafield.md` recomputed after a
one-paragraph RULE ADDITION (user decision): the three CTA lines are written in order of importance — the customer's
biggest problem (the reason to buy) first, the other two descending — because on mobile most visitors read only the
first line. No gate or threshold changed.

**Refresh note (BLR-BATCH26, 2026-09-06 — a 44th line: keyfeat_cover.py, every source Key Features line in the list):**
`./keyfeat_cover.py` added at the user's decision after comparing p11's source Key Features (7 lines) with the live list
(5 items): "FLAME-LIKE LED EFFECT" and "MIST OUTPUT" sat in a bullet and the prose but not in the list. value_check and
fact_cover only ask whether a fact is somewhere; spec_cover covers the Specifications list only. The new script is
spec_cover's twin for Key Features: `--extract` writes `extract.key_features` from raw/ (the supplier's `<li>` and bold
"Name:" lines outside the spec / package / FAQ sections; headings as a fallback), and the check FAILs any of those lines
that is not an item of the new `<h3>Key Features</h3>` list (half the content words, or the Name half + one text word,
in one item). The user's rule: the line is ALSO a list item even when a bullet or the prose already carries the fact —
bullet = why buy, list = what is there. Fact-free marketing headings and forbidden-outcome lines go to `omit_per_ruling`
with a reason. Wired into `./gate.py` before value-check; `./rules/description-format-rule.md` §4, `./DESC-SPEC.md`
(read list + gate list) and `./README-toolkit.md` (steps 3 and 6) recomputed. Applied to the pushed batch: 145 source
lines were missing across 38 products; all added or logged, gate CLEAN over 50, only the Key Features list changed (checked
against the live copy), re-pushed, `verify: 50 products, 901 checks, 0 failures`. Session-start copy list is now 44 lines.

**Refresh note (BLR-BATCH26, 2026-09-06 — key_features completed by the extraction agent, paragraph features included):**
four lines recomputed after a PROCESS addition (user decision, no gate threshold changed). `./EXTRACT-SPEC.md`: the
extraction agent now COMPLETES `key_features` by eye after the script pre-fills it — (a) source feature lines the parser
missed (heading + paragraph, plain paragraph lists) and (b) the concrete features the source states only inside its
paragraphs (material, mechanism, function, mode, capacity, control, mounting, setting); never marketing sentences, specs
or package lines. `./keyfeat_cover.py --extract` no longer overwrites a non-empty list — it adds only parser lines not
already present, so the agent's additions survive a re-run. `./rules/description-format-rule.md` §4 and
`./README-toolkit.md` step 3 recomputed. Cost: inside the extraction agent's existing read, a few lines per product.

**Refresh note (BLR-BATCH26, 2026-09-06 — prose spec values enforced via extract.specs):** three lines recomputed after a
PROCESS addition (user decision). description-format-rule.md §5 has said since 2026-09-05 that a value the source gives
only inside a sentence gets its own Specifications line — but spec_cover.py compared only the supplier's table
(`extract.specs`), so nothing enforced that paragraph. `./EXTRACT-SPEC.md`: the extraction agent now appends every
measurable prose value (capacity, power, runtime, charge time, dimensions, weight, magnification, LED count, colour
temperature, lumens, ingress rating, material, mode/level counts, pack count, compatibility) to `extract.specs` as its own
`{name, value}` pair in the source's figure and unit — never a duplicate of a table value in another form, never an
estimate; a prose/table conflict keeps the table's pair and goes into `notes`. spec_cover.py then FAILs any pair missing
from the new list. `./rules/description-format-rule.md` §5 (enforcement sentence) and `./README-toolkit.md` step 3
recomputed. Applied to the pushed batch in one description-agent round: 33 pairs added across 17 products (the first
pass had already mined most prose values), gate CLEAN over 50, only the Specifications lists changed, re-pushed,
`verify: 50 products, 901 checks, 0 failures`.

**Refresh note (BLR-BATCH26, 2026-09-06 — a 45th line: unit_dual.py, dual units in Specifications):** `./unit_dual.py`
added at the user's decision: a Specifications measurement the source gives in one unit system only gets the other
system appended in parentheses (cm/mm/m ↔ in/ft, g/kg ↔ oz/lb, ml/l ↔ fl oz, °C ↔ °F; a tank/capacity "oz" is treated as
fluid ounces); the source figure stays first and verbatim; items already carrying both systems are untouched; electrical
units, hours, lumens, mAh, percentages are never converted; only the `<h3>Specifications</h3>` list is touched. Zero
tokens, idempotent, runs inside `./gate.py` before keyfeat-cover / value-check. Fixture-tested including negative
temperatures (-20°F → -29°C), ranges (113-131°F → 45-55°C), slash lists (50/65/80°C), dimension runs (28.8 x 27.8 x 0.3 cm
→ 11.3 x 10.9 x 0.1 in) and already-dual items (unchanged); two bugs found and fixed on the way (sign handling, "113-131"
parsed as a negative). `./rules/description-format-rule.md` §5, `./DESC-SPEC.md` gate line and `./README-toolkit.md`
step 6 recomputed. Applied to the pushed batch: 45 Specifications items across 50 products gained the second unit,
nothing else changed (field diff against the live copy), re-pushed, `verify: 50 products, 901 checks, 0 failures`.
Session-start copy list is now 45 lines.

**Refresh note (BLR-BATCH26, 2026-09-06 — unit_dual.py scope widened):** four lines recomputed after a RULE CHANGE (user
decision, same day as the script): dual units now apply to the prose paragraphs, the Key Features intro and list, the
Specifications list and the FAQ answers — and deliberately NOT to the H2, the five benefit bullets, CTA lines, the
comparison and fit blocks, FAQ questions, image alt texts or SEO fields (budgeted elements; a parenthesis there breaks a
limit or pushes a title keyword out of the first 500 characters). `./unit_dual.py` converts text nodes only (tags and
attributes untouched), protects the two blocks with compare_build / fit_build's own BLOCK_RE, treats a repeated-unit run
("75 cm x 45 cm") as one measurement and skips any measurement already adjacent to its conversion. `./rules/description-
format-rule.md` §5, `./DESC-SPEC.md`, `./README-toolkit.md` recomputed. Applied to the pushed batch: 48 more items
outside Specifications; protected parts confirmed unchanged; `verify: 50 products, 901 checks, 0 failures`.

**Refresh note (BLR-BATCH26, 2026-09-06 — unit_dual.py: imperial first):** two lines recomputed after a RULE CHANGE
(user decision: a US shopper who sees cm first reads the listing as imported). `./unit_dual.py` now writes the imperial
figure first and the metric one in parentheses whichever the source wrote (`5.1 oz (145g)`, `11.3 x 10.9 x 0.1 in (28.8 x
27.8 x 0.3 cm)`, `122/149/176°F (50/65/80°C)`), reorders pairs it or the source had already written metric-first, and
reorders source slash pairs (`15.2cm/5.98in` → `5.98in/15.2cm`); the source figure stays verbatim so value_check /
spec_cover still find it. Idempotent. `./rules/description-format-rule.md` §5 recomputed. Applied to the pushed batch:
every pair in the 50 products now imperial-first (0 metric-first pairs left), `verify: 50 products, 901 checks, 0 failures`.

**Refresh note (2026-09-07, comparison table — value columns centred):** two lines recomputed after a LAYOUT FIX (user
instruction, from a screenshot of a live blr-batch26 product: the ticks and the "Varies" / ✘ cells sat off-centre under
the `Vepine` / `Others` headers). `./compare_build.py`: the theme overrode the cells' inline `text-align:center`, so every
value cell and both value headers now centre their content with a flex wrapper inside the th/td (immune to theme
text-align rules), th and td of a value column share one width (120 px) and padding so header and cells have the same
centre, and the feature column is pinned `text-align:left !important`. New helper `parse_block()` reads name + rows out of
a rendered block (old or new template) so a template change can be applied to live products by re-rendering. Checks,
insertion point and BLOCK_RE unchanged. Fixture-tested: render → parse_block round-trip exact; strip_block exact; under a
hostile stylesheet (`td, th {text-align:right !important}`) a Playwright screenshot shows both value columns centred
under their headers; all 50 live blr-batch26 blocks parse to 5 rows + a 2–5-word name. `./rules/comparison-table-rule.md`
(format-rules bullet) recomputed in the same turn. Live re-render of the 50 blr-batch26 blocks: payloads built and
verified (outside-block text byte-identical on all 50) but the PUSH was not executed in this session — see the
2026-09-07 note in the run log / chat; it must be pushed and verified (`verify.py`, check 17) before this note is read
as "applied live".

**Refresh note (2026-09-07, fit block — conversion revision: situation — proof, no generic audience, closing sentence):**
four lines recomputed after a deliberate RULE CHANGE (user decision, from a screenshot of a live blr-batch26 fit block:
the four lines described the reader but gave no reason to believe the product delivers, the fourth line "someone of any
age who could use comfort" persuaded nobody, and the block ended dead before the FAQs). `./rules/fit-block-rule.md`
(project path `claude/fit-block-rule.md`): every line is now `situation — proof` (buyer's situation, one em dash, the
source fact that answers it), 30–110 chars; generic-audience lines (`any age`, `anyone`, `everyone`, `everybody`) are
forbidden; the script renders a FIXED closing sentence under the list — "If two or more of these sound like you, this is
the one." — which the agent never writes. `./fit_build.py`: checks exactly one ` — ` per line, proof ≥ 8 chars and
traceable to the extract on its own, generic-audience regex, new length range; constant `CLOSE`; render adds the navy bold
closing `<p>` inside the column (BLOCK_RE and the before-FAQs regex in struct-check / verify.py unchanged and re-tested).
`./struct-check.py`: a fit block without the closing sentence FAILs (old layout → re-run fit_build.py); imports `CLOSE`
from fit_build. `./DESC-SPEC.md`: `fit.for` schema line and gate line. Fixture-tested: four proof lines → rendered before
FAQs, closing sentence present, position regex matches, re-run idempotent, Q19 = Skip removes the block; a line without
the dash / a number not in the source / an "any age" line / a 5-char proof → 4 FAILs named one per line. NOT done in this
session: no live product was re-rendered or pushed, and `./verify.py` and `./README-toolkit.md` were NOT edited (verify's
position + one-column checks still hold for the new layout; the closing-sentence check lives in struct-check only). The
50 live blr-batch26 fit blocks still carry the old layout — re-rendering them needs new `situation — proof` lines from a
description-agent pass (the old lines have no proof half), so it is a batch task, not a script re-render.
**Refresh note (DENEME batch, 2026-09-07 — supplier policy promises never in copy):** three lines recomputed after a
deliberate RULE CHANGE (user instruction after the DENEME summary: "bunları hiçbir zaman açıklamaya dahil etme").
Warranty, guarantee, money-back / refund / risk-free trial, return policy and customer-support / after-sales promises
are a third-party seller's policy, not a product fact, and are never written anywhere — prose, lists, comparison block,
fit block, FAQ, CTA lines, SEO — even when the source carries them as a spec line (`Motor warranty: 2 years`); every
such source line goes into `omit_per_ruling` ("supplier policy, not product fact"). `./gate.py` FAILs the family in
every customer-facing field and in the CTA lines (no `add_per_ruling` exemption); `./DESC-SPEC.md` (standing user
rules) and `./rules/description-format-rule.md` (Hard rules) state the rule. Fixture-tested: a p04 copy with "2-year
motor warranty and a 30-day money-back guarantee" in prose and "Risk-free 30-day trial" as a CTA line → 2 FAIL, exit 1;
the 7 live DENEME finals → CLEAN. Note: `assume_check.py` still lists "warranty" among its source-sourced families —
that check is now moot for this family because gate.py fails it regardless of the source.


**Refresh note (STR-DUB-2-batch1, 2026-09-07):** one line recomputed — `./rules/description-format-rule.md` was STALE, not a corrupted copy: two independent copies of the project doc agreed byte-for-byte and both differed from the manifest, because the doc had gained the 2026-09-07 §5 "attribute name before the colon is bold" note and the supplier-policy hard rule after the previous hash was taken. New hash 4221db1a…d0523 taken from the verified copy (sha256 of the file on disk that passed the batch). The other 44 lines passed (three genuine copy corruptions in that session — README-toolkit.md, dim_image.py, fit_build.py, all dash/quote retyping — were fixed by re-copy and match the existing lines).

68d0bf45181514726364bba16a3e1eafa62d40f78e3d9ffc31b19540fefc4b95  ./para_feat.py
**Refresh note (STR-DUB-2-batch1 follow-up, 2026-09-07 — Key Features copies + paragraph sweep, a 46th line):** five lines recomputed
after a deliberate RULE CHANGE (user decision) and `./para_feat.py` added. The user found that 88 of 240 source Key Features
lines had reached the store pasted verbatim (keyfeat_cover.py only asked "is it present?", and pasting is the cheapest way
to be present) and that 45 of 48 products had left extraction with exactly the script's pre-filled list — the paragraph
features and prose spec values EXTRACT-SPEC asks for had not been added and nothing made that visible. `./keyfeat_cover.py`
now FAILs a pasted line ([COPY]: sentence fabric >= 90% identical in sequence after removing every value word — numbers,
units, spec/package/variant tokens — so a fact can never be changed to pass; <= 6 fabric words exempt). `./para_feat.py`
(new, zero tokens, always exit 0) lists paragraph sentences with a feature marker not covered by key_features and prose
figures absent from specs; the main context sorts them into added / dismissed and the run log carries the counts.
`./EXTRACT-SPEC.md` (mandatory `NN | script X | paragraph features added Y | prose specs added Z` reply line, reason for
every 0), `./DESC-SPEC.md` (gate line), `./README-toolkit.md` (step 3b, step 6, 6c "KF read" line) and
`./rules/description-format-rule.md` (§4 copy gate sentence) recomputed. Tested on the live batch: 94 [COPY] lines on 34
products → rewritten by the description agents, values unchanged (value_check / spec_cover clean), 0 copies; para_feat
44 KF flagged → 5 added (p08 no-soaking, p11 light reduction, p22 diffused glow, p30 ABS shell, p44 4-inch cushioning),
39 dismissed; 4 SPEC flagged → 1 added (p45 inflation time 30 s), 3 dismissed (p20 ruled conflict); re-pushed, verify 0 failures.

**Refresh note (STR-DUB-2-batch1 follow-up 3, 2026-09-07 — independent KF/spec reader, lines 48–49):** `./KF-REVIEW-SPEC.md`
and `./kf_review_input.py` added at the user's decision, `./README-toolkit.md` recomputed (step 3c). One Sonnet agent per
batch reads only the source paragraphs and the extract's two lists — never the description — and marks certain misses;
the main context confirms or dismisses. Validated live on this batch with `--all`: 8 marked, 8 confirmed and pushed
(verify 47 products, 847 checks, 0 failures); every mark had passed para_feat.py's word match, which is the gap the
reader closes (sentence-type features and numberless spec values). Eligibility: paragraphs > 80 words (3 of 47 here).

**Refresh note (STR-DUB-2-batch1 follow-up 4, 2026-09-07 — How to Use steps only, Usage Tips section; lines 50–51):**
`./howto_check.py` and `./usage_tips.py` added at the user's decision; `./gate.py` (both wired after cta-check),
`./struct-check.py` (an audience line under How to Use is an issue; Usage Tips position), `./rules/description-format-
rule.md` (§7 rewritten, §7b added, skeleton line), `./EXTRACT-SPEC.md` (how_to_use = steps only; usage_tips field),
`./DESC-SPEC.md` (schema + gate list) and `./README-toolkit.md` (step 3d, step 6) recomputed. Reason: 9 products had the
supplier's "Usage Recommendations" audience lines pasted verbatim under a How to Use heading (the old §7 said "reproduce
it"). Applied live: 47 audience lines moved from how_to_use to facts, 9 How to Use sections removed, 23 products gained a
<h3>Usage Tips</h3> list written in the agents' own sentences (3 lines ruled out: p18/p24 CPAP comparison, p28 medical
implication), 23 descriptions re-pushed, `verify: 47 products, 847 checks, 0 failures`.

**Refresh note (STR-DUB-2-batch1 follow-up 5, 2026-09-07 — no wholesale regeneration of final files):** `./DESC-SPEC.md`
recomputed after a PROCESS rule was added at the user's decision: a description agent edits only the named field of an
existing final/dNN.json (read-modify-write) and never rebuilds files from a script — one agent's build script had reverted
the main context's `category_proposal` values three times in that batch (caught by verify.py each time).

**Refresh note (STR-DUB-2-batch1 follow-up 6, 2026-09-07 — three consistency fixes, user decision):** `./unit_dual.py`
(scope now includes the Usage Tips and How to Use lists; fixture: "12 L" in a tip → "405.8 fl oz (12 L)"),
`./fact_cover.py` (a facts line that is also a usage-tip line is skipped — usage_tips.py enforces it item by item, scoring the
rewrite was noise: 40 → 29 lines on the live batch), `./para_feat.py` (a prose figure counts as ruled only through an explicit
omission — final omit_per_ruling or the new `rulings_omit.json` written with RULINGS.md — never a text search in RULINGS.md),
`./rules/description-format-rule.md` (§5 scope sentence) and `./README-toolkit.md` (step 3b) recomputed.

**Refresh note (STR-DUB-2-batch2, 2026-09-07):** one line recomputed — `./rules/cta-benefits-metafield.md` was STALE, not a corrupted copy. Two independent copies of the project doc agreed byte-for-byte (`4417d0aa…521a`) and both differed from the manifest (`f9c809f2…`), so per §6 the manifest line was stale: the doc had gained its blr-batch26 CTA-order paragraph and the "Gerçek örnekler" section after the previous hash was taken. New hash taken from the verified copy that passed the batch. The other 50 lines passed; one genuine copy corruption in that session (`./title-check.py`, first copy `430c480b…`, second independent copy matched the manifest exactly) was fixed by re-copy, so that line is unchanged.

**Refresh note (STR-DUB-2-batch3, 2026-09-07 — unit_dual.py: three parsing bugs fixed):** one line recomputed after a CODE FIX
(main-context finding while reading the finished Key Features lists; scheduled run, no user present). `./unit_dual.py`:
(1) `4G` / `5G` (network generation) was converted as 4 grams → `0.1 oz (4G)` on p04/p06/p07 — an uppercase `G` unit is now
skipped (grams are written lowercase); (2) `9.45 in L` / `23.99 cm L` (L = length label after a unit) was read as litres →
`319.5 fl oz (9.45 in L)` on p16 — an uppercase `L` after a run that already carries a unit is skipped; (3) a single-unit
value backtracked into run + unit (`49mm` → `49m` + `m` → `160.8 ft (49mm)` on p05/p07/p08/p09/p22; `250ml` → `250m` + `l`)
— the inner unit of a run now needs a following separator (x / - / to). Also: `60 oz tank` in prose/FAQ is treated as fluid
ounces even when the item has a `Name:` prefix. Fixture-tested: `Display Size: 49mm` → `1.9 in (49mm)`; `Tank: 250ml` →
`8.5 fl oz (250ml)`; `Network: 4G` unchanged; `Size: 14.17 in H × 9.45 in L × 7.09 in W` → only the in-values converted;
the earlier fixtures (`145 g`, `12 L`, `28.8 * 27.8 * 0.3 cm`, `113-131°F`, `15.2cm/5.98in`, already-dual items) unchanged.
The wrong pairs were reverted in the batch's finals before the push; `verify: 50 products, 902 checks, 0 failures`.

**Refresh note (2026-09-08, run artefacts leave the project):** `./README-toolkit.md` recomputed after a PROCESS CHANGE (user
decision — the project hit its 2 MB knowledge cap; 129 of the ~200 docs were per-batch backup-alt / kw-cache / run-log /
backup-titles files). From now on only `claude/backup-titles-<tag>.md` (before the push) and `claude/run-log-<tag>.md` (after
verify) are project docs; `kw-cache-<tag>.md` and `backup-alt-<tag>.md` are written to /mnt/user-data/outputs/ and sent to the
chat with SendUserFile instead (README header note; steps 4 and 7). No gate, rule or threshold changed. Older run docs were
copied to Google Drive `Vepine/<tag>/` the same day and 45 of them deleted from the project after byte-size verification.
Hash taken from the file written on disk in the main context (24623 bytes, newline-terminated).

**Refresh note (2026-09-08, source_windows.py — DataForSEO length gate):** one line recomputed after a CODE FIX (user
decision, from the STR-DUB-2-batch4 run log's "For the next run" item 1). `./source_windows.py` now drops any window over
DataForSEO's per-keyword limit (80 characters / 10 words) before it is emitted. Reason: `google_ads/search_volume/live`
rejects an over-limit keyword with `40501 Invalid Field: 'keywords'. Keyword text exceeds the allowed limit` and ONE bad
keyword voids the WHOLE task — the call returns a top-level `20000 Ok` with zero results, which reads as a successful
call. In batch4, 49 of 1,277 windows were whole supplier titles over that limit; the first attempt returned nothing on
every chunk and the run recovered only because the main context noticed the empty result. The filter lives inside
`windows()` (new `measurable()` helper, new `keep_oversize` argument used only by `main()` for its stderr report), NOT
only in `main()`, so both consumers agree: the phrase is not offered as a candidate, and `./title-check.py` — which
imports `windows()` for its push-blocking "source windows NOT measured" gate — no longer demands a phrase DataForSEO
cannot measure. Nothing measurable is lost: an over-limit window is always a whole supplier title, and every 2–4-word
phrase inside it is still emitted separately. `main()` prints the dropped count and lists each dropped phrase on stderr,
so a batch with unusually long titles is visible in the run log. Fixture-tested: a 91-char / 13-word title → 23 windows
emitted, 1 dropped and named on stderr, exit 0; `windows(norm(title))` (the title-check path) returns nothing over the
limit; a short title's whole-title phrase is still emitted. `./title-check.py` was NOT edited — it needed no change, and
its gate is now satisfiable by construction. `./README-toolkit.md` was NOT edited: step 4's description ("every
contiguous 2–4-word window") stays true and the dropped phrases were never measurable candidates.

**Refresh note (2026-09-08, verify.py — collections.json in any shape):** two lines recomputed after a CODE FIX (user
decision, from the STR-DUB-2-batch4 run log's "For the next run" item 2 — the second of the two batch4 traps; the first,
source_windows.py, is the note above). `./verify.py` read collections.json ONLY as a `{title: id}` map, while README step 8's
refresh snippet produces the raw GraphQL response; written the README way, every title was "not in collections.json",
check 10 printed a `[note] … not resolvable by title` on every product and never actually ran, and the summary line still read
"0 failures" — in batch4 this hid on 43 products until the file was rewritten by hand. New `load_colmap()` accepts the map,
the raw response (`{"data": {"collections": {"edges": …}}}`), its inner `{"collections": …}` / `{"edges": …}` objects, and a
plain list of `{id, title}` or `{node: {id, title}}`; an unrecognised shape or a file that yields no collections is a hard
exit (1) with the reason — never a note. Fixture-tested: all five shapes → 18 checks, 0 failures; a product missing its
collection → `[FAIL] collections` under both the map and the raw shape; empty response and `{"foo": "bar"}` → exit 1 with
the message; no file given → the existing `[note]` + 17 checks, unchanged. Everything outside the loader is byte-identical
to the previous version (the pristine copy re-hashed to the old line before the edit). `./README-toolkit.md` recomputed:
the collections.json line under "Store-specific constants" now says either shape is accepted (pristine copy re-hashed to
`10369ac2…` before the three added lines).

**Refresh note (2026-09-09, a 53rd line — kw_measure.py, the one DataForSEO path):** `./kw_measure.py` added at the user's
decision and `./README-toolkit.md` recomputed (step 4). Reason: the DataForSEO error log showed two `40501 Invalid Field:
'keywords'. Keyword text exceeds the allowed limit` errors on 2026-09-09 (07:50 and 08:18 UTC) — a day AFTER the
source_windows.py gate — because that gate covers only the windows the script itself emits; the extraction agents'
candidates/cNN.json and the step-1b extra list went to the API unfiltered, and the two rejected keywords were whole supplier
titles (14 and 17 words) from that side. Step 4 was an ad hoc curl until now, so the filter had no fixed place to live and a
future session could skip it. The new script is the ONLY route from a candidate list to the API: it unions .json / .txt
candidates in any shape, normalises them as source_windows.norm() does (apostrophes closed up, other non-alphanumerics
removed — DataForSEO rejects those too), dedupes, skips what kw.txt already has, applies `measurable()` (imported from
source_windows.py — one definition of the 80-char / 10-word limit) BEFORE chunking and names each drop on stderr, sends ≤950
per call, EXITS 1 on any task status other than 20000 (40501; a 4020x rate-limit answer is retried once after 65 s) and on a
chunk with ZERO results (the silent-void case: one bad keyword empties the chunk while the call reads `20000 Ok`), appends
`keyword|volume|competition|cpc` to kw.txt and the --cache doc after each good chunk (a crash keeps earlier chunks, a re-run
measures only what is missing), records a keyword the API did not echo at 0 and counts it as `[not returned]`, and reads
the credentials from dataforseo-credentials.md without ever printing them. `--dry-run` costs nothing. Fixture-tested with a
mocked API on the two keywords from the error log plus normal candidates: dry run → 2 dropped and named, 5 to measure;
void response → exit 1, nothing written; 40501 task → exit 1, nothing written; good response → 5 lines appended to kw.txt
and cache, one non-echoed keyword recorded at 0 and named; re-run → 0 to measure, no call. `./source_windows.py`,
`./title-check.py` and `./TITLE-SPEC.md` were NOT edited (1b keeps its wording; README step 4 says the same command
serves it). Not yet run on a live batch — the first batch after this date reads its stderr summary lines into the run log.
No gate, rule or threshold changed; nothing that DataForSEO could measure is dropped.
Same day, second pass after the user shared the account's full error export (100 rows, 2026-09-08/09) — both files
recomputed. The export showed two more families beside the five over-limit keywords: (a) four 40501 "too many words" rows
whose keyword was source_windows.py's OWN stderr summary line (`source windows 50 titles - 1253 windows 1253 not yet
measured`) — captured into candidates/source_windows.txt with `2>&1`; after normalisation it is exactly 10 words and would
have passed the length gate, so kw_measure.py now refuses report-shaped lines (REPORT_RE: `source_windows:` / `kw_measure:`
prefixes, `[oversize]` / `[not returned]` tags, `N titles -> N windows`, `not yet measured`, `dropped over the DataForSEO`)
and names each on stderr; (b) ~90 40202 rows in one minute (`The rates limit per minute has been exceeded: 12 >= 12`) — the
account's live limit is 12 calls/min, not 2,000, and a failed call was retried in a tight loop; kw_measure.py now paces
calls 6 s apart (≤ 10/min) and retries a 4020x answer exactly once after 65 s, then exits 1 — never a loop. The three
`id_list` / `Invalid Path` rows of 2026-09-08 17:53 are from a hand query of the error endpoint, not from the pipeline.
Fixture re-run with the three report-line shapes appended to source_windows.txt: all three refused and named, keyword
output unchanged. README step 4 carries both traps in one sentence each.
Third pass, same day, after the account's ERROR DYNAMICS chart (02–09 Sep: 804 errors, ~800 on 08 Sep alone — 40202 ×672,
40501 ×128, 50301 ×3): `./kw_measure.py` recomputed once more — the single 65-s retry now also covers a 5xxxx task status
(DataForSEO server-side, e.g. 50301 Internal Error), so a transient API fault does not end a run on the first chunk; a second
failure still exits 1. Tested with a mock: 50301 then Ok → 2 calls, chunk written. The 126 40501 rows (the export showed 9)
are the same bad chunk re-sent in the 2026-09-08 loop — no new keyword family.

**Refresh note (2026-09-08, additional source sections — a 52nd line: sections.py):** `./sections.py` added at the user's
decision, and eight lines recomputed after a deliberate RULE CHANGE. Reason (user question, same day): the extraction kept
only the known source blocks as fields (specs, package, how_to_use, usage_tips, key_features, faq_source); every other
headed block of the supplier's description — Care Instructions, Warnings / Safety, Materials, Design, Applications,
Compatibility, Storage, Charging, Installation, Size Guide, Notes — fell into `facts` as loose lines, lost its heading and
was dissolved into the prose. Decisions: (1) a block that carries a product fact (Tip A) becomes its own `<h3>` section —
list or paragraphs, every line own words, values verbatim, no copy, no merge, no invented `<h3>`, position; (2) headings are a NORMALISED
vocabulary (`CANON` in sections.py — Care Instructions, Safety Warnings, Materials, Design, Applications, Compatibility,
Storage, Charging, Installation, Size Guide, Notes), never the supplier's own; (3) a fact already in the prose / Key Features
is still written in its section — same fact, different sentence (the §4 rule); (4) applies from the first batch after this
date — NO pushed product is re-processed. `./sections.py` (`--extract` writes extract.sections / sections_dismissed, moves
section lines out of key_features; check FAILs missing section / line / [COPY] / [MERGED] / invented `<h3>` / position,
WARNs on order), `./gate.py` (wired after usage-tips), `./struct-check.py` (a non-skeleton `<h3>` only between Package
Includes / How to Use / Usage Tips and the fit block / FAQs), `./unit_dual.py` (scope: every `<h3>` section after Package
Includes, Package Includes itself excluded — How to Use / Usage Tips fall in the same rule), `./fact_cover.py` (section lines
skipped, like usage tips), `./rules/description-format-rule.md` (§7c, skeleton line, §4 and §5 sentences), `./EXTRACT-SPEC.md`
(`sections` / `sections_dismissed` fields, reply line `| sections S`), `./DESC-SPEC.md` (read list, standing rule, schema,
gate list), `./README-toolkit.md` (step 3e, steps 6 and 6b). Fixture-tested on a fleece blanket source with four extra
blocks: Care Instructions (list, 3 lines) and Safety (prose, 1 line → `Safety Warnings`) kept, "Elegance That Takes Off"
dismissed as marketing-only, "Warranty" dismissed as policy, the 3 care lines removed from key_features; a good page → exit
0; pasted lines → 2 [COPY]; two lines in one item → [MERGED]; missing section → FAIL; an invented `<h3>Why You Will Love
It</h3>` → FAIL; sections before Package Includes → 2 FAIL (sections.py and struct-check both); swapped order → WARN only;
a ruled-out line with the section absent → clean, with the section present → FAIL. unit_dual: `40°C` in Care Instructions
and `1.5 m` in Safety Warnings converted, the bullets and Package Includes untouched, idempotent. Not run on a live batch
yet — the first batch after this date reads the `sections --extract` summary line and the [UNMAPPED] lines in full.

**Refresh note (2026-09-09, STR-DUB-2-batch8 — sections.py shape tests):** two lines recomputed after a deliberate RULE
CHANGE (user decision, after the script's FIRST LIVE RUN). `./sections.py` proposed a section on 42 of 50 products and every
one was the supplier's LEAD HEADLINE + intro paragraph — the description's own opening, not an additional headed block. Worse,
7 had already been auto-mapped to a canonical name by a stray keyword inside that marketing sentence: `Charging` from "High
Power Blue Laser Pointer for Long-Distance Targeting", `Safety Warnings` from "Reflective Cat GPS Tracker Collar for Enhanced
Safety", plus `Care Instructions`, `Design` ×2, `Storage`. gate.py cannot catch this class of error — once a block is in
`extract.sections` it only asks whether the page reproduces it — so the only guard was the main context reading the --extract
summary, and a run that skipped that read would have published `<h3>Safety Warnings</h3>` over a marketing sentence. Two SHAPE
tests now dismiss such a block before the fact test: (1) `MAX_HEAD_WORDS = 4` — a heading longer than four words is a marketing
headline, not a section heading (all 42 mis-detected headings were 5-8 words; every heading the fixtures keep is 1-3);
(2) the source's FIRST heading over prose is the description's lead, kept only when it is a short heading that also names a
canonical family (so a source genuinely opening with "Care Instructions" survives). Both were measured on the batch first:
all 42 mis-detected blocks were heading index 0 AND 5-8 words, so either test alone catches them. The `--extract` summary line
now breaks the dismissals down by reason (marketing / policy / description lead / long marketing heading);
`./README-toolkit.md` step 3e recomputed for the two tests and the new summary format. Fixture-tested: the fleece-blanket
fixture is unchanged — Care Instructions (list, 3 lines) and Safety (prose, 1 line → `Safety Warnings`) still kept, "Elegance
That Takes Off" still dismissed as marketing-only, "Warranty" still dismissed as policy, the 3 care lines still moved out of
key_features — plus its `<h2>` product headline now correctly dismissed as the lead; a source whose FIRST heading is
"Care Instructions" over prose is KEPT (the exception); a non-first 6-word heading is dismissed and stays visible in
`sections_dismissed` so the main context can move it back. Check mode is untouched and re-tested: good page → exit 0;
invented `<h3>` → FAIL; missing section → FAIL; [MERGED] → FAIL; section before Package Includes → FAIL; a ruled-out line with
the section absent → clean, with the section present → FAIL; a pasted line → [COPY] FAIL. Re-run over the 50 live
STR-DUB-2-batch8 products: `0 of 50 products carry a fact section, 42 dismissed (description lead 42), 0 UNMAPPED` — exactly
the outcome the main context had reached by hand — and `gate.py` over all 50 still prints `=== gate: CLEAN ===`.

**Refresh note (2026-09-09, Q18 dimension image — gallery position 2, not 3):** three lines recomputed after a deliberate
RULE CHANGE (user decision, in the user's words: the "actual size" image is the product page's 2nd image; the source's
images from the 2nd onwards shift one place down, nothing is removed). `./dim_attach.py`: new `POSITION = 2` constant at
the top; the reorder index is `min(POSITION - 1, n_before)` so a product with one existing image gets it appended (position
2 anyway); docstring carries the rule and the date. `./rules/dimension-image-rule.md` (project path
`claude/dimension-image-rule.md`): "Where it goes" section rewritten for position 2, with the note that products attached
before this date keep their position-3 order unless re-attached. `./README-toolkit.md` (steps 7b and 8) recomputed.
`./verify.py` was NOT edited — it reads the position from `dim/media.json`, so old (3) and new (2) batches both verify
against what was actually done. Compile-checked, not run live in this session. Q18's first live run was STR-DUB-2-batch9
(same day, other session, before this change): 5 products — p07, p34, p36, p09, p49 — attached at position 3; the staged
PUT worked (no egress problem). Those five stay at position 3 until re-ordered (one productReorderMedia each; the media
is findable by its alt "… – actual size and dimensions"). That run log also records a `DIM_RE` gap in `./dim_image.py`
(a source that repeats the unit after each figure — `12.91 in x 2.96 in x 2.96 in`, `46cm x 32cm x 16cm` — never
matches; two products were rebuilt by hand) — NOT fixed here, open item. The stale duplicate `./README-toolkit.md` line
in the block below (two lines carried the file since 2026-09-08) is now the same hash on both lines.

**Refresh note (2026-09-09, Q18 dimension image — axes must be labelled):** three lines recomputed after a deliberate RULE
CHANGE (user decision, in the user's words: "yanlış görsel daha kötü" — a wrong image is worse than no image). `./dim_image.py`:
a three-figure triple is used only when the source NAMES the axes — an order key next to the figures or once anywhere in the
source (`(L x W x H)`, `LxWxH`, `Length x Width x Height`, `H x W x D`, a spec row named that way) or labelled figures
(`L 46 cm x W 32 cm x H 16 cm`, `Length: 46 cm, Width: …`, `46 cm (L) x …`, three Length / Width / Height spec rows); a
bare `2 x 5 x 6 cm` is skipped with `axes not labelled` (dim/build.json + the summary line lists the products) instead of
being drawn in source order (batch9 p49). Same edit closes the batch9 open item — the unit may now follow every figure
(`46cm x 32cm x 16cm`) — and never reads a package / box / carton / shipping / parcel measurement as the product's size;
mixed units, two axes only and diameter × height are skipped. Fixture-tested (22 cases): bare triple in spec / variant →
skip with the note; order key in spec name, after the figures with repeated units, `H x W x D` reordering, a global order
key applied to two variant sizes, labelled inline / worded / after-figure, three spec rows → the expected (L, W, H, unit);
package-only → skip, package + product → product; mixed units / two axes / diameter → skip; `3"` inches quote → in.
`./rules/dimension-image-rule.md` (rule 1 widened, rule 1b added) and `./README-toolkit.md` (step 7b) recomputed. compose()
and the attach step are untouched. Not run live in this session.

**Refresh note (2026-09-09, Q18 — unlabelled figures resolved by the photo, not skipped; same session, minutes later):**
three lines recomputed after the user relaxed the rule above (user decision: "kuralı gevşetelim" — the safe way to more
images is ours, not the supplier's). `./dim_image.py`: labelled sources are used as written (no change); an UNLABELLED
triple is no longer skipped outright — `resolve_axes()` compares the cut-out's width/height (the same rembg cut-out the
picture is drawn from, now produced once by `cutout()` and passed to `compose()`) with the six possible assignments of the
three figures and uses the single assignment that fits within `PHOTO_TOL` 20 % when the runner-up is ≥ `PHOTO_GAP` 30 %
off; GAP > TOL means a photo measured within tolerance can never select a wrong assignment, only an ambiguous one (skipped
as `axes ambiguous (photo): …` with the ratios). Equal figures collapse so a 20×20×10 is not "ambiguous" against itself;
with several sizes the largest is tested and the mapping applied positionally to all. `dim/build.json` gains `axes` per
product ("labelled" / "photo-ratio: photo 0.70 vs best 32/46=0.70, next 16/32=0.50 -> L=b D=c H=a"); the summary line
counts labelled / photo-ratio / ambiguous. Fixture-tested: backpack 46×32×16 at photo 0.70 → L=32 H=46 (the batch9 p49
case, now right by itself); 0.80 → same; 0.62 → ambiguous (skip); 2.90 → L=46 H=16; 1.00 → no fit (skip); 30×25×20 at
1.20 → two fit (skip); 20×20×10 at 1.00 → resolved; two variant sizes → same mapping on both; the 22 labelled/parse cases
from the note above unchanged. `./rules/dimension-image-rule.md` (rule 1b now "labelled = as written", new rule 1c) and
`./README-toolkit.md` (step 7b summary-line format) recomputed. The rembg part of the test is not run in this session
(no model here); the ratio logic is pure arithmetic and is what the fixtures cover. First live batch: read the `axes`
value of every photo-ratio product next to its picture in the rule-5 look.

**Refresh note (2026-09-09, Q18 — two figures are enough; same session):** three lines recomputed after a RULE ADDITION
(user decision: "bunu da ekleyelim"). `./dim_image.py`: when no source text carries a three-figure run, a TWO-figure
measurement is read — `DIM2_RE` (`200 x 150 cm`, `46cm x 32cm`), labelled pairs through `roles2()` (`W 46 cm x H 32 cm`,
`Diameter 20 cm, Height 30 cm`, `Length 200 x Width 150 cm` → length horizontal / width vertical, two Diameter / Height spec
rows; `diameter` / `dia` / `ø` added to AXIS), unlabelled pairs through the same photo-ratio test with two candidates.
Three figures anywhere always win. Entries carry `W = None`; `compose()` then draws no depth text and a Size / Length /
Height table; `resolve_axes()` handles both arities and labels the pair result `photo-ratio (2 figures): …`. Fixture-tested
(14 parse cases + 8 resolutions + 2 renders looked at): 3-figure cases unchanged and precedence over a 2-figure line in
another field; raw / repeated-unit / labelled / spec-row / variant pairs; package and mixed-unit pairs → none; yoga mat
200×150 at photo 1.33 → L=200 H=150, at 0.75 → L=150 H=200, at 1.00 → no fit, at 1.15 → resolved; 30×28 at 1.05 →
ambiguous; 20×20 → resolved; `pack of 2 x 5 cm hooks` at a square photo → no fit (skip). `./rules/dimension-image-rule.md`
(rule 1d; the 1c sentence that had skipped two-axis sources corrected) and `./README-toolkit.md` (step 7b) recomputed.

**Refresh note (2026-09-09, Q18 — three gaps closed after the user asked "what did we miss?"; same session):** four lines
recomputed. (1) `./dim_image.py`: a decimal comma (`46,5 x 32 x 16 cm`) was read as `5 x 32 x 16` — a WRONG figure the
photo test cannot always catch; `NUM` now accepts `46,5` and `dec()` normalises it (a `1,200` thousands separator becomes
1200; the first figure may not be preceded by a digit / comma / dot). (2) same file: the measurement of the thing a
product FITS (`fits mattresses up to 200 x 150 cm`, `for 15 inch laptops`, `compatible with 40 x 60 cm frames`) was read
as the product's own size, and for a sheet / case / frame the photo test passes because the proportions match — the
package exclusion now also covers fits / for / compatible / suitable / up to / accommodates / holds / designed for; a
two-axis order key `(L x W)` / `W x H` / `Dia x H` is recognised (ORDER2_RE) and no longer mistaken for a size letter `L`;
`2 x 3 in stock` / `in packs` is not inches (NOT_IN). (3) `./dim_attach.py`: a product entering a second batch or a re-push
would have received a SECOND dimension image — before uploading it now reads the live gallery and skips any product whose
media alt already ends with `– actual size and dimensions`, recording it in `dim/media_existing.json` (kept OUT of
dim/media.json because verify.py reads that file's `position` as an insertion). Fixture-tested: 12 parse cases (comma
decimal labelled + raw, thousands, fits/for → none, fits + own `(L x W)` row → own size, `W x H` / `Dia x H` keys, a real
`Size L` label kept, all earlier 3- and 2-figure cases unchanged, `in stock` / `in packs` → none while `12 x 8 in` and
"… in size" still read); dim_attach mock: product with an existing dimension alt → skipped and listed, product without →
uploaded, reordered to position 2, summary line counts both. `./rules/dimension-image-rule.md` (rule 1, steps) and
`./README-toolkit.md` (step 7b) recomputed. Known and accepted, not scripted: straps / cords / shadows / white-on-white /
multi-item photos distort the cut-out → the photo test fails safe (skip); a source with folded + unfolded triples lists
both as "sizes" in the table (visible in the rule-5 look and the run log).

**Refresh note (2026-09-09, Q18 — US units first on the image; same session):** two lines recomputed after a RULE CHANGE
(user decision: the image always shows the American unit). `./dim_image.py`: `fmt()` now prints inches first with the source
unit in brackets whatever the source wrote (`18.1 in (46 cm)`, `47.2 in (1200 mm)`, an inch source `22.4 in (56.9 cm)`),
the height line too (two rows so it stays inside the canvas), the size table in inches with `(in)` in its headers; new
`inches()` helper (1 decimal, `.0` dropped). Also fixed on the way: the table box was as wide as the product cut-out, so a
narrow product's four columns overflowed it — width now follows the column count. Rendered and looked at: 2-size backpack
(cm source) and 1-size mat (inch source). `./rules/dimension-image-rule.md` ("What is produced") recomputed.

**Refresh note (2026-09-09, Q18 — gallery position back to 3; same session):** three lines recomputed after the user
REVERSED the position-2 decision made earlier today. Reason (raised when asked "what else should we think about"): most
Shopify themes show the 2nd gallery image as the collection-card HOVER image, so at position 2 the size diagram would have
replaced the product's second photo on every collection page. `./dim_attach.py` `POSITION = 3` (docstring rewritten with
the reason), `./rules/dimension-image-rule.md` ("Where it goes" + steps) and `./README-toolkit.md` (steps 7b, 8)
recomputed. Net effect on the store: none — no product was attached at position 2 between the two decisions; the five
STR-DUB-2-batch9 products are at position 3 already and now match the rule (they still carry the earlier cm-first
figures; re-rendering them is a separate decision).

**Refresh note (2026-09-09, Q18 — the drawn image also on the page, under Specifications; same session):** five lines
recomputed after a RULE ADDITION (user decision: "çizildiyse Specifications altına koy"). `./dim_attach.py`: after the
gallery attach (or when the gallery already had the image from an earlier batch) `describe()` reads the media's CDN url,
inserts `<p><img class="vp-dim" src=… alt="<first title block> – actual size chart"></p>` directly after the first `</ul>`
that follows `<h3>Specifications</h3>`, writes final/dNN.json and pushes a productUpdate carrying ONLY descriptionHtml;
idempotent (a description already carrying a vp-dim image is untouched); the outcome is recorded per product in
dim/media.json (`description`) and printed. `./gate.py` (source-image prefix / count check) and `./struct-check.py` (image
count) strip `<img class="vp-dim" …>` before counting; struct-check additionally FAILs a vp-dim image off our CDN or
inserted twice. Both pristine copies were verified against this manifest's hashes BEFORE editing (retyped copies matched
byte for byte), so the edits are the only change. `./verify.py` NOT edited: check 2 (live == final descriptionHtml) and 13
(img list == final's, all on CDN) hold because final is updated before the push; check 16 (alt unique) holds because the
description alt (`– actual size chart`) differs from the gallery alt (`– actual size and dimensions`). Mock-tested: new
product → attached at position 3 + inserted + pushed; product with an existing gallery image → not re-attached, description
inserted + pushed; second run → nothing pushed, one vp-dim image per description; struct-check fixture with 2 source
images + the vp-dim image → no image-count issue; a foreign-CDN or doubled vp-dim image → the two new FAILs.
`./rules/dimension-image-rule.md` ("On the page as well") and `./README-toolkit.md` (step 7b) recomputed. Not run live.

**Refresh note (STR-DUB-2-batch3 Q18 re-run, 2026-09-09 — dim_image.py size-row names):** one line recomputed after a
small CODE FIX (main context, while looking at the built images per rule 5). The size-table row name was taken only from
letter sizes (`XS|S|M|L|XL|XXL|\d+XL`), so a source that writes `Large: 14.96" … / Extra Large: 18.90" …` produced a first
row named `Size` (p17 beach tote). The regex now also accepts the word forms `Extra Small | Small | Medium | Large | Extra
Large` (longest first). Figures, axes and every other rule unchanged. Note: the copy check in this session found the
manifest lines for `./dim_image.py`, `./rules/dimension-image-rule.md` and `./unit_dual.py` STALE (two independent copies
byte-identical, both differing from the manifest — the docs were edited after the last refresh); the two lines this
session did not edit were left as they are for their author to recompute.

**Refresh note (STR-DUB-2-batch2 Q18 re-run, 2026-09-09 — three guards after a wrong image reached the store):** two lines recomputed after a deliberate RULE CHANGE (user decision). The user read the live batch2 p05 dimension image and found the axes swapped: a 195 x 130 x 5 cm camping mattress drawn 195 wide / 130 tall, when the two pillows sit side by side along the 130 cm edge. Rule 1c's photo-ratio test had "confirmed" the wrong assignment at 6 % because the 3/4 camera angle foreshortens the long axis — the first case where the test did not fail safe but selected a wrong assignment inside tolerance. `./dim_image.py` gains three guards, all documented as rule 1f in `./rules/dimension-image-rule.md`: (a) a LIE-FLAT lock — a triple whose smallest figure is under 15 % of its largest (mat, mattress, cushion, strap) is never assigned by photo, labelled axes or skip; (b) PHOTO_TOL tightened 20 % -> 15 % (batch2 p39 passed at 18.75 % with the wrong assignment), PHOTO_GAP unchanged at 30 % so GAP > TOL still holds; (c) a connected-blob isolation test, MAIN_PART = 90 % of the cut-out's pixels in one blob, because 1e(b)'s span/fill guard misses a product photographed with its accessories. MAIN_PART was calibrated on that batch's real cut-outs and the classes separate widely: several objects 65.4 / 74.8 / 81.6 %, one product 99.3 / 100 %. Fixture- and batch-tested: on batch2's 50 products the guards block 8 of the 9 images the eye had rejected (7 not-isolated, 2 flat, and p39 now ambiguous) and leave the correct ones alone; p14 still builds, and the synthetic control cases still pass. Rule 5's eye check now asks its question by name ("is the horizontal line on the product's real long axis?") because two residual risks are deliberately not automated: a TWO-figure flat measurement has no thin third figure to detect, and a cut-out can be one clean blob of the WRONG object (batch2 p28: 99.3 % single blob of the car seat the product sits on).

**Refresh note (STR-DUB-2-batch2 Q18 re-run, 2026-09-09 — three guards after a wrong image reached the store):** two lines recomputed after a deliberate RULE CHANGE (user decision). The user read the live batch2 p05 dimension image and found the axes swapped: a 195 x 130 x 5 cm camping mattress drawn 195 wide / 130 tall, when the two pillows sit side by side along the 130 cm edge. Rule 1c's photo-ratio test had "confirmed" the wrong assignment at 6 % because the 3/4 camera angle foreshortens the long axis — the first case where the test did not fail safe but selected a wrong assignment inside tolerance. `./dim_image.py` gains three guards, all documented as rule 1f in `./rules/dimension-image-rule.md`: (a) a LIE-FLAT lock — a triple whose smallest figure is under 15 % of its largest (mat, mattress, cushion, strap) is never assigned by photo, labelled axes or skip; (b) PHOTO_TOL tightened 20 % -> 15 % (batch2 p39 passed at 18.75 % with the wrong assignment), PHOTO_GAP unchanged at 30 % so GAP > TOL still holds; (c) a connected-blob isolation test, MAIN_PART = 90 % of the cut-out's pixels in one blob, because 1e(b)'s span/fill guard misses a product photographed with its accessories. MAIN_PART was calibrated on that batch's real cut-outs and the classes separate widely: several objects 65.4 / 74.8 / 81.6 %, one product 99.3 / 100 %. Fixture- and batch-tested: on batch2's 50 products the guards block 8 of the 9 images the eye had rejected (7 not-isolated, 2 flat, and p39 now ambiguous) and leave the correct ones alone; p14 still builds, and the synthetic control cases still pass. Rule 5's eye check now asks its question by name ("is the horizontal line on the product's real long axis?") because two residual risks are deliberately not automated: a TWO-figure flat measurement has no thin third figure to detect, and a cut-out can be one clean blob of the WRONG object (batch2 p28: 99.3 % single blob of the car seat the product sits on).

**Refresh note (2026-09-09, cut-out never shaved — rule only, script not yet changed):** one line recomputed after a RULE ADDITION (user instruction, from a live batch3 mushroom-lamp image whose dome and sides were visibly cut off). New rule 1g in `./rules/dimension-image-rule.md`: the cut-out is cropped to the product's TRUE bounding box — every pixel of the mask — never to a density-thresholded box, because a rounded or tapered outline has very few pixels in its outermost rows and columns (a dome shade's apex, a lamp head's flare, an animal figure's ears) and those rows fail the density test and are cut away. It is not cosmetic: the dimension lines are drawn on the crop's edges, so a shaved crop draws the measurement SHORT while the label still reads the source figure. Measured on real batch2 cut-outs, density box vs true box: elephant lamp -12.6 % of the width, camping mattress -3.4 %, inflatable chair -2.2 % of the height, mini washing machine -1.9 %; a mushroom lamp (wide dome, thin stem) is the worst case because the stem rows set the threshold. Speckles are dropped by blob (keep blobs >= 1 % of the mask, rule 1f(c) already guarantees one blob holds >= 90 %), with a small transparent margin so the lines do not sit flush on the outermost pixel. **Implemented in `./dim_image.py` the same day** (the user's first instruction was rule-only, then corrected to "write it wherever it needs to be written"): `cutout()` now takes the bounding box of the mask's significant blobs (>= 1 % each) instead of the `>= 0.06 * frame` density rows/columns, and adds a transparent margin of `max(4 px, 1 % of the longer side)`. Verified on real cut-outs — the elephant lamp's trunk and tail and the owl lamp's ear tufts are no longer clipped, and the box grows 692x725 -> 792x731 before padding. Re-running batch2's build after the change altered exactly one decision, an improvement: p28 moved from a hand-written rule-5 skip to the script's own `axes ambiguous`, because the corrected crop yields a truer ratio. With this and rule 1f the script now blocks all 9 of the images that batch's eye review had rejected, and only the correct p14 still builds.

**Refresh note (2026-09-09 evening, Q18 SCOPE CUT — labelled only, manual only, two live-bug fixes; a 54th line: dim_keep.py):**
five lines recomputed and one added after a deliberate RULE CHANGE (user decision, after asking "is it best to give up the
dimension image?" and answering "vazgeçme, küçült" — keep it, shrink it). Every wrong image of the day (batch9 p49, batch2
p05 / p39 / p03, batch3) had come through the photo-ratio test; no labelled source produced one; the operator's eye was the only
reliable catch. So: (1) `./dim_image.py` — `PHOTO_TEST = False`: an unlabelled triple or pair is skipped as `axes not labelled
in source` BEFORE any photo is downloaded; `resolve_axes()` and the 1f guards stay in the file for a logged, deliberate
re-enable only; the summary line counts `axes not labelled: NN …` and prints a `[WARN] … PHOTO_TEST is on` line if the test
ever runs. New `run_mode()` / `q18_gate()`: both scripts build and attach nothing unless brief_flags.json carries
`"q18_dimension_image": true` AND `"run_mode": "manual"` (a missing key reads as scheduled) — the rule-5 eye check does not
exist in a scheduled run, so the feature must not either. (2) `./dim_attach.py` — REPLACE no longer leaves a dead link:
`insert_in_description()` rewrites an existing vp-dim tag whose src differs (the media was deleted and re-attached), instead of
returning unchanged on the class alone; `describe()` reports "src replaced". Imports `q18_gate` from dim_image. (3) new
`./dim_keep.py` — README step 7, every batch, independent of Q18 and run mode: a product whose live description (products.json)
carried a vp-dim image that the new final lacks (a Q7 rewrite dropped it; gate.py / struct-check.py ignore vp-dim by design)
gets the tag restored under the new Specifications list — only while its media is still in the live gallery, otherwise a
[WARN], never a re-published dead link; one summary line for the run log. (4) `./rules/dimension-image-rule.md` — new "Scope
cut" section; rule 1c marked RETIRED, 1d's unlabelled-pair path marked retired, steps updated (run-mode gate, replace, dim_keep).
(5) `./README-toolkit.md` — step 1 (`run_mode` flag), step 7 (dim_keep first), step 7b (labelled only, retired test). All three
pristine copies were verified against this manifest's hashes BEFORE editing (retyped copies matched byte for byte:
dim_image 3440e415…, dim_attach d63975f4…, rule a5b2cf6d…, README 6c19063e…), so the edits are the only change. Fixture-tested
with a stubbed shopify_api: run_mode scheduled / missing → both scripts print the reason and exit 0 with nothing built;
manual → unlabelled triple `46 x 32 x 16 cm` and unlabelled pair `200 x 150 cm` skipped as not labelled with no photo
downloaded, labelled `L 46 cm x W 32 cm x H 16 cm` reaches the cut-out step; insert_in_description: old src → replaced once,
same src → unchanged, no tag → inserted after the Specifications `</ul>`; dim_keep: dropped tag with live media → restored in
position, tag whose media is gone → [WARN] not restored, no live tag → untouched, second run 0 restored. Not run live.
Live effect expected: fewer products per batch get an image; the five batch9 / batch2 / batch3 images already live are
untouched by this change.

**Refresh note (2026-09-09 evening, description images served resized — `?width=1200` on still images only):** four lines
recomputed after a user decision that followed the Q18 scope cut. Description `<img>` tags are loaded as written — the
theme's `image_url` filter resizes only GALLERY media — so every re-hosted source image and the Q18 PNG (1–2 MB, white
background) shipped at full file size to every phone. New `cdn_sized()` in `./dim_attach.py` (one definition) appends
`?width=1200` (or `&width=1200` after an existing `?v=`) to a src whose file is jpg / jpeg / png / webp; a `.gif` is never
touched (the CDN flattens an animated GIF to one frame under width=), nor is `.svg`; idempotent, an existing width= is kept.
`./rehost.py` step 4 applies it to every still image on our CDN in the extract (the extract is the source of truth for
gate.py's image-prefix check, so the agents' copies carry the same src) and its summary line counts them; `describe()` in
dim_attach.py applies it to the Q18 image's description src (the gallery media is untouched). `./README-toolkit.md` (step 5b)
and `./rules/dimension-image-rule.md` ("On the page as well") recomputed. Pristine `./rehost.py` verified against this
manifest's line (3a7534b5…) before editing. Fixture-tested with a stubbed API and no foreign images: a.jpg → `?width=1200`,
b.png?v=123 → `?v=123&width=1200`, c.gif and d.svg untouched, e.webp?width=800 kept, F.JPEG (upper case) sized; second
run 0 changed. Not run live; products pushed before this date keep their raw srcs (no re-processing).

**Refresh note (2026-09-09 evening, `?width=1200` REVERTED — measured, no benefit):** the note above is superseded; four lines
recomputed back. Applied live to 24 products / 58 still images first and measured with a mobile browser UA: the CDN already
serves WebP for a raw src and every description image was ≤ 1200 px, so the parameter saved 18 KB in total (one image). The
24 live descriptions were restored byte-for-byte from the backup (0 push errors, 0 verify failures — Shopify stores `&` as
`&amp;`, normalised in the check). `./rehost.py` is back at its pristine hash (3a7534b5…), `./dim_attach.py` at its pre-width
hash (18ff02a4…, `cdn_sized` removed), `./README-toolkit.md` at its pre-width hash (7090a3c4…); only
`./rules/dimension-image-rule.md` carries a one-sentence record of the measurement so the idea is not tried again. The
"1–2 MB PNG" premise in the earlier note was wrong — the Q18 PNG reaches a phone as a 32 KB WebP. Page-weight work, if any,
belongs to animated GIFs in supplier descriptions (untouched by decision, a separate task), not to still images.

**Refresh note (2026-09-10, comparison table — mobile + desktop widths):** two lines recomputed after a LAYOUT FIX
(user instruction, from a live phone screenshot of the USB-charger camera page: the two 120 px value columns left ~100 px
for the feature text on a 360 px phone, `Looks and works like a real charger` broke into five lines and the block ran
~1400 px tall). `./compare_build.py`: (a) the product name moved out of the first `<th>` and became the SECOND line of the
navy heading band (13 px, `opacity:.85`), so the header row is one line — `FEATURE` (12 px uppercase) · `Vepine` ·
`Others`; (b) the value columns are percentages, `COL_V` 14 % and `COL_O` 24 %, padding `10px 4px`, replacing the single
`COL` constant; (c) `table-layout:fixed` plus `max-width:none;margin:0` on the table (the theme's own table margin was
leaving a ~35 px gap at the card's right edge); (d) table 14 px, row padding 10 px, Others cells 12 px / 1.25 and
wrappable, with `text-align:center` added to their flex wrapper (new `CENTER_T`) so a second line stays centred; (e) new
constant `MAXW = '680px'` on `div.vp-compare` — percentage columns in a 1470 px theme container gave the feature column
~1300 px and stranded the ticks at the right edge. `clamp()` widths were tried first and are IGNORED by the browser under
`table-layout:fixed` (three equal columns; measured with Playwright) — do not reintroduce them. `parse_block()` now reads
the name from the band's second line and falls back to the old first-`<th>` form, so live blocks from either template
re-render. Checks, insertion point, BLOCK_RE, `strip_block`, `q17()` and the gate wiring are unchanged (struct-check.py,
verify.py and unit_dual.py match on `<div class="vp-compare"` only and were not touched).
`./rules/comparison-table-rule.md` (diagram, header-cells line, new Mobile and Desktop bullets in the format rules)
recomputed in the same turn. Fixture-tested: render → parse_block round-trip exact; an old-template block parses to the
same name + rows; strip_block exact; re-render idempotent; under a hostile stylesheet (`td, th {text-align:right
!important}`) a Chromium measurement gives 186 / 54 / 86 px at a 328 px block and 406 / 103 / 171 px at 680 px, with the
ticks centred and Others phrases on one line at desktop width. NOT done in this session: no live product was re-rendered
or pushed — the live blocks still carry the 120 px template and must be re-rendered from `parse_block()` and verified
(`verify.py`, check 17) before this note is read as "applied live".

**Refresh note (2026-09-10, STORE CHANGE Vepine → Worfa):** seventeen lines recomputed (README-toolkit.md is listed twice
in the block below — both copies updated). User instruction: the store is now **Worfa**, a DIFFERENT Shopify store, not a
rename of the old one. Confirmed through the connector (identity lookup only): Worfa / `worfa.com` /
`ymjviw-rz.myshopify.com` / USD, CDN prefix `cdn.shopify.com/s/files/1/0786/1269/3028/` read off live product media.
Changed: `BRAND` in `./compare_build.py` (also the rendered heading "Why choose Worfa" and the "Worfa vs Others" block),
`./verify.py` and `./gate.py` (the brand scan now fails `worfa` in copy, not `vepine`); the hard-coded CDN prefix in
`./gate.py`, `./struct-check.py`, `./build_check.py`, `./verify.py`, `./extract_html.py`, `./rehost.py` and
`./DESC-SPEC.md`; store name and host throughout `./shopify-api-credentials.md` (rewritten) and `./README-toolkit.md`;
brand name in `./rules/comparison-table-rule.md`, `./rules/dimension-image-rule.md`, `./rules/fit-block-rule.md`
and `./rules/description-format-rule.md` (the "Worfa vs Others" block name in the skeleton); the CDN prefix in
`./usage-efficiency-runbook.md`; and the root transfer guide `00-TASIMA-REHBERI.md` (not hashed here — host, Drive
folder and the same-store/different-store branches).

Three deliberate NON-changes, all user decisions of the same day:
- **The `vp-` CSS hooks stay** (`vp-compare`, `vp-fit`, `vp-dim`, `vp-store`). The Tuzwa→Vepine migration renamed
  `tz-`→`vp-`, but renaming again would make every live block invisible to BLOCK_RE, struct-check.py, verify.py and
  unit_dual.py until it was re-rendered and pushed. The hook is an internal selector, not a brand string.
- **History is not rewritten.** Run logs, `backup-titles-*`, `backup-alt-*`, `kw-cache-*` and
  `claude/store-migration-vepine-2026-09-07.md` still say Vepine, because the backups are restore snapshots of live
  Vepine titles and alt texts — rewriting them would make them restore the wrong thing. Same decision as the Tuzwa
  backups in the previous migration.
- **`vepine.com` is left in one place on purpose**: the colour-provenance sentence in
  `./rules/comparison-table-rule.md`, which records where the navy / light-blue hex values came from.

Three things NOT verified and flagged in the docs, not silently carried over:
- **The store row `30-day easy returns` is the previous store's policy** (user, 2026-09-06), unconfirmed for Worfa.
  compare_build.py's `STORE_ROW` writes it into EVERY comparison block, so an unchecked figure becomes a returns
  promise on every product page. Confirm Worfa's window and change `STORE_ROW` and the rule doc together.
- **Theme colours are still the OLD store's.** `NAVY = #000096` and `LIGHT = #d2def6` were measured on vepine.com
  2026-09-07 and have NOT been re-measured on worfa.com. The rule doc carries a "Colour provenance — STALE" block and
  README-toolkit.md and `./rules/fit-block-rule.md` carry the same caveat. Measure Worfa's Add-to-cart button and header
  band and update `NAVY` / `LIGHT` in compare_build.py AND the rule doc together before the first Worfa push.
- **The script route is unproven on this store.** The client-credentials token call for the new pair was not run (the
  attempt was blocked in this session), `ymjviw-rz.myshopify.com` has never been called from the container, and the CDN
  prefix comes from 3 products / 6 images rather than a full sweep. See the status block in
  `./shopify-api-credentials.md`.

Scripts re-tested after the rename: all toolkit .py files compile; compare_build render → parse_block round-trip exact,
re-render idempotent, rendered block contains "Why choose Worfa", no occurrence of the old brand, and still carries
`class="vp-compare"`.

**Refresh note (2026-09-10, Worfa go-live checks — the four open items closed):** seven lines recomputed after the four
things the store-change note left unverified were actually run against Worfa, not assumed.
1. **Script route works.** `shopify_api.py` `token(force=True)` issued a `shpat_…` from `ymjviw-rz.myshopify.com` (the
   user added the host to the egress allowlist), `{ shop { name myshopifyDomain } }` → Worfa, and the app
   `Claude Backend` reports `read_files, read_products, read_publications, write_files, write_products,
   write_publications` — all three needed writes granted.
2. **CDN prefix confirmed on the full catalogue**, not a spot check: 4,150 products / 35,675 media images, every one on
   `cdn.shopify.com` with the prefix `/s/files/1/0786/1269/3028/` — 0 foreign hosts, 0 off-prefix.
3. **Theme colours re-read for Worfa** from the live MAIN theme "Vault"
   (`gid://shopify/OnlineStoreTheme/174734606372`, `config/settings_data.json`, default `scheme-1`): NAVY is the
   theme's own `buy_button_color` `#2c374d` (the Add-to-cart button), LIGHT is `secondary_bg` `#eef5f7`. Applied in
   `./compare_build.py`, `./fit_build.py` and `./dim_image.py` (the last as RGB tuples (44,55,77) / (238,245,247)).
   Taken from the theme's declared settings rather than sampled off a rendered page. Contrast: white on navy 11.9:1,
   navy on light 10.8:1. The previous store's `#000096` / `#d2def6` are retired.
4. **Store row confirmed by the user**: Worfa's return window is also 30 days, so `STORE_ROW` is unchanged — the
   UNCONFIRMED comment in `./compare_build.py` and the matching block in `./rules/comparison-table-rule.md` were
   replaced with the confirmation and a standing instruction to re-confirm it whenever the store or policy changes.
Also fetched, not hashed here because it is run data rather than a toolkit file: `collections.json`, 24 Worfa
collections as `{title: gid}` — the shape DESC-SPEC and verify.py expect. `./shopify-api-credentials.md` and
`./README-toolkit.md` recomputed with the verified status. Block re-run after this refresh: 55 of 55 OK.

**Refresh note (DDL2-Batch1, 2026-09-10 — CTA metafield theme is Worfa/Vault, block confirmed live):** one line recomputed after a
DOC CORRECTION, not a copy problem. `./rules/cta-benefits-metafield.md` still named the PREVIOUS store's theme in its "Teknik"
section — Xtra || FIXED (`gid://shopify/OnlineStoreTheme/204864586014`), block id `custom_liquid_apEFqN`) — which the
2026-09-10 Vepine→Worfa store change left stale; the DDL2-Batch1 run log flagged it as an open item because a metafield that
no theme block reads renders nothing and fails silently. The user confirmed they had already pasted the Custom Liquid block
into Worfa's main theme **Vault** (`gid://shopify/OnlineStoreTheme/174734606372`) and that the benefits render on the live
product page. The doc's Teknik section now names Vault as the current theme, records the user confirmation and the standing
fact that the block does NOT travel with a store change (it is pasted into the new theme by hand), and keeps the old theme id
in a separate line marked "yalnızca kayıt için". A DDL2-Batch1 line was also added to "Uygulama durumu" (50/50 metafields
verified, rendering confirmed). No gate, rule or threshold changed.

**Refresh note (2026-09-11, kw_measure.py word-order guard — a 56th line: rules/kw-order-variant-rule.md):** three lines
recomputed and one added after a deliberate RULE CHANGE (user decision, from DDL2-batch1 p00, product 11212354748452: the
title dropped `noise cancelling headphones` 165,000 — the old title's own opener — as "low volume"). Reproduced: Google Ads
folds keywords that are the same words in a different order into ONE close variant when they arrive in the SAME request and
reports the low variant's volume for both — `noise cancelling headphones` returns 165,000 alone and 2,400 next to `headphones
noise cancelling`; measured alone the two orders are different keywords (`vintage table lamp` 3,600 vs `lamp table vintage`
2,900). The pair is routine here: source_windows.py emits the supplier title's order, the extraction agents give the natural
order. `./kw_measure.py`: the todo list is bucketed by sorted word bag (`bag()`) and the members of one bag are spread over
separate ROUNDS (`rounds_of()` — round 0 = first member of every bag, round 1 = second, …); each round is chunked and called
on its own, and an assert guarantees no two variants share a request. Both variants are still measured with their own volume;
the title step picks the higher one — "dedupe to one variant" was rejected because the reversed form can be the lower one.
Cost: one extra call (~$0.09) per round beyond the first. New stderr lines for the run log: `… in N call(s) over R round(s) —
V word-order variant(s) moved to later rounds` and one `[order variant, own call]` line per moved keyword. Tested with a
stubbed source_windows on 6 keywords (two 2-member bags, one 3-member bag): 3 calls over 3 rounds, 3 variants named, no bag
repeated inside a round. `./rules/kw-order-variant-rule.md` (project path `claude/kw-order-variant-rule.md` — the tool cannot
write to the root) is the rule doc and carries the open question (plural / singular folding, not reproduced) and the audit
recipe for kw-caches produced before this date (bucket by sorted word bag, re-measure every 2+ bag in separate calls).
`./README-toolkit.md` step 4 recomputed (word-order guard paragraph after the ≤950-per-call sentence; both README lines
below updated). The pristine README copy was verified against this manifest's line (06e71b25…) byte for byte before the
edit, so the paragraph is the only change. Not yet run on a live batch — the first batch after this date copies the round
line into the run log.

**Refresh note (2026-09-11, US units only in the budgeted elements):** six lines recomputed after a deliberate RULE CHANGE
(user decision — the live ddl2 pregnancy pillow's comparison table read `155 x 75 x 60 cm`; the store sells only in the USA
and the copy is written for a US shopper, so a metric figure never stands alone on the page). Until now the dual-unit pass
deliberately skipped the budgeted elements (H2, benefit bullets, comparison / fit blocks, FAQ questions) because a
"(155 cm)" parenthesis would break a limit — so whatever unit the agent wrote there reached the store as written.
`./unit_dual.py`: new `imperial_only()` — metric → imperial with the metric figure DROPPED (`155 x 75 x 60 cm` → `61 x 29.5 x
23.6 in`, `61 in (155 cm)` → `61 in`, `5.98in/15.2cm` → `5.98in`, `40°C` → `104°F`; imperial text unchanged; the dual pass's
exemptions — 4G/5G, "L" as a length label, waterproof mm ratings, liquid oz — reused through a shared `_skip()`); `process()`
now applies it to the H2 + first `<ul>` (bullets) and to FAQ QUESTIONS, keeps the dual pass everywhere it ran before, and
returns a third count (`… N budgeted element(s) made imperial-only` on the per-product line). `./compare_build.py`: `render()`
passes name, feature rows and non-✘ Others cells through `imperial_only()` (lazy import — unit_dual imports this module's
BLOCK_RE); the 20–60 length check runs on the converted row, the traceability and number-in-source checks on the agent's own
text, so a source-metric row still passes. `./fit_build.py`: the same for the four lines (30–110 measured after conversion;
proof / source / number checks on the agent's text). `./rules/comparison-table-rule.md` (content rule 8, format-rules bullet,
"Where it runs" — including how a live metric block is fixed by `parse_block()` → `render()` + a descriptionHtml-only push),
`./rules/fit-block-rule.md` (content rule 7) and `./rules/description-format-rule.md` (§5 dual-units paragraph: the "NOT
converted" sentence replaced — budgeted elements are imperial-only; CTA lines, alt texts and SEO fields stay untouched by
script and are written in US units by the agent). Fixture-tested: the twelve conversions above plus `Waterproof rating 3000mm`,
`Supports 5G`, `32 oz water bottle` and an already-imperial dimension run all unchanged; every result idempotent; a fixture
description → H2 and bullet imperial-only, prose and Specifications dual (`61 x 29.5 x 23.6 in (155 x 75 x 60 cm)`), FAQ
question imperial-only and its answer dual; compare render → `parse_block()` round-trip returns the converted row; fit render
carries no metric figure. gate.py, struct-check.py, verify.py and value_check.py were NOT edited (gate calls unit_dual as a
subprocess and reads only its last line; a metric figure that lived ONLY in a bullet now fails value_check and must also get its
Specifications line — the intended outcome). Not run on a live batch yet; products pushed before this date keep their metric
rows until re-rendered.

**Refresh note (2026-09-11, a 57th line — list_bold.py: bold lead-ins + gap under image 2):** `./list_bold.py` added and
three lines recomputed after a user instruction from the live ddl2 pregnancy pillow. (1) Key Features items reached the store
as plain `U-Shape Support: Back, hips, legs …` although §4 / §5 of the format rule have asked for `<li><strong>Name:</strong>
text</li>` since 2026-09-07 — no script enforced it. list_bold.py (gate.py, right after fit-build, before the finals are loaded
for the other checks; zero tokens, idempotent) wraps a plain leading `Name:` (1–7 words) in `<strong>` in the Key Features and
Specifications lists and normalises `<strong>Name</strong>:` / `<strong>Name: </strong>` to the canonical form; an item with no
`Name:` lead is reported, never invented. `./struct-check.py` now FAILs a Key Features / Specifications item without a bold
`Name:` lead. (2) The second description image (between Key Features and Specifications; the vp-dim image not counted) sat flush
on the Specifications heading: list_bold.py appends `display:block;margin-bottom:24px` to that `<img>`'s style (other attributes
untouched, src unchanged — gate.py / verify.py compare srcs only); struct-check.py FAILs a second image without `margin-bottom`.
`./rules/description-format-rule.md` §4 (markup + enforcement sentence) and the skeleton's image-2 line recomputed. Fixture-tested:
three plain / malformed lead-ins bolded, an already-canonical item untouched, a no-colon item reported, a spec line bolded, the
gap added once to image 2 (existing `style="width:100%"` extended), second run changes nothing; `<img …/>` self-closing form
handled. Not run on a live batch; products pushed before this date are unchanged until re-processed.

**Refresh note (DDL2-Batch4, 2026-09-12 — proxy backoff in both API scripts):** two lines recomputed (user approval
2026-09-12). `./shopify_api.py`: `gql()` now retries an empty / non-JSON response after 10, 30, 60 s (retries 3 → 6) — the
sandbox egress proxy intermittently answered CONNECT with 403 for ~20 s on 2026-09-11 (seen on the Shopify host three
times in a row, recovered 20 s later); the token call and the HTTP/GraphQL error handling are unchanged. `./kw_measure.py`:
the line was STALE, not a corrupted copy — the project doc gained its "Proxy backoff" paragraph (`TUNNEL_BACKOFF`, transport
errors retried after 5/10/20/40 s) at 18:36 UTC on 2026-09-11, after this manifest's 11:55 refresh; two independent copies
agreed byte for byte. DDL2-Batch4 ran to `verify: 50 products, 901 checks, 0 failures` on these two files.

**Refresh note (DDL2-Batch3, 2026-09-12 — unit_dual.py: engine litres and dual temperature ranges):** two lines recomputed after a CODE FIX (user approval "tamam yaz"). On p17 (jump starter) the script had turned engine displacement into liquid volume (`engines up to 10.0 L` → `338.1 fl oz (10.0 L)`) and converted a range the source already wrote in both scales piecewise (`-20°F to 70°F / -29°C to 21°C` → `-20°F (-29°C) to 70°F / -29°C to 70°F (21°C)`); both reached the final and were hand-fixed before the push. `./unit_dual.py`: new `ENGINE` regex in `_skip()` — an l/ml figure whose 40 chars before or 25 after name an engine / displacement / cylinder / diesel / gasoline / petrol / motor is left as written (dual and imperial_only); new `has_both_temp()` — a text that already carries both °C and °F is never temperature-converted again in `dual()` or `imperial_only()`; new `DROP_SLASH_T` — imperial_only drops the `/ …°C` half of such a range (`-20°F to 70°F / -29°C to 21°C` → `-20°F to 70°F`). Fixture-tested (11 cases incl. `Tank: 250ml`, `86°F to 122°F`, `40°C`, `3000mm` rating, `5G`, `32 oz water bottle` unchanged in behaviour; every result idempotent); gate.py re-run over the 50 DDL2-Batch3 finals: CLEAN and all 50 files byte-identical. `./rules/description-format-rule.md` §5 gained the two-sentence rule. Note: this manifest's list carries `./README-toolkit.md` twice; both lines are unchanged.

**Refresh note (DDL2-Batch7, 2026-09-12 — unit_dual.py N-in-1 fix; two stale lines recomputed):** three lines
recomputed (user approval "tamam işle").
1. **CODE FIX — `./unit_dual.py`.** "3 In 1" was read as three inches: p17 reached its final as
   `Product Type: 3 In (7.6 cm) 1 Dog Jacket Winter Pet Coat` and p18 as the Key Features lead-in
   `3 In (7.6 cm) 1 Floor Cleaning`. Because the conversion runs inside gate.py, hand-reverting it in the final was
   undone on the next gate run, so the fix had to be in the script. `_skip()` now skips an `in` / `in.` unit whose
   figure is a bare 1-2-digit integer and which is immediately followed by another bare integer — the N-in-1 product
   claim shape. Fixture-tested: `3 In 1 Dog Jacket`, `3 in 1 floor cleaning` and `12 in 1 pack` unchanged, while
   `Fits 6 in photos` -> `6 in (15.2 cm)`, `Head 18 in long` -> `18 in (45.7 cm)` and the already-dual
   `13 in / 33 cm` still behave as before; the p17/p18 finals were repaired and re-gated CLEAN, and gate.py over all
   50 DDL2-Batch7 products printed `=== gate: CLEAN ===` with the fix in place. Known and accepted trade-off: a
   genuine `12 in` immediately followed by a bare integer (`12 in 1 pack`) is now left unconverted — the N-in-1
   reading is the far more common one in supplier copy.
2. **STALE LINES, not corrupted copies — `./title-check.py` and `./rules/title-format-rule.md`.** Both failed on the
   DDL2-Batch7 session copy; two independent copies of each agreed byte for byte and both differed from the manifest,
   and both project docs had been edited at 08:15 UTC on 2026-09-12, after the 06:21 refresh. Recomputed from the
   verified copies (26ad735d... / 8c9ff354...). In the same session `./DESC-SPEC.md` failed as a GENUINE COPY
   CORRUPTION (the second copy matched this manifest exactly) and its line is unchanged.
3. **`./README-toolkit.md` is still NOT re-hashed and its line is knowingly stale.** In that session both independent
   copies differed from the manifest AND from each other, each in one line (one dropped "/ Tips" in step 3d, the
   other turned an em dash into a semicolon in step 5), so no copy could be certified as the project's bytes. The
   file is documentation only — no script reads it — so the run continued with a merged copy excluded from the check.
   Whoever next reads README-toolkit.md in a clean session should re-hash it from a verified copy.

**Refresh note (2026-09-15 — unit_dual.py: word-form units, bag litres, count × value, axis label):** two lines recomputed
after a CODE FIX (user instruction "bunları sende yap", carrying over a patch first made in the sibling project; this project's
copy was verified against the manifest line `9f1cf384…` byte for byte before editing, so the edits are the only change — the
sibling's file was NOT copied over, because the two versions had diverged: this copy already carried the 2026-09-12 ENGINE and
N-in-1 fixes). Found on a DDL2 batch: `800 meters` (p27 — the same product's `800m` WAS converted), `5000 meters` (p06),
`800-5500 meters` (p16) reached the finals metric-only; a 3.5L backpack pocket became `118.3 fl oz (3.5L)` (p07) and a 50L bag
`1690.7 fl oz` with the FAQ line `How much can this 1690.7 fl oz backpack hold?` (p08) — 8 places hand-fixed before that push.
`./unit_dual.py`, four changes: (a) `WORD_UNITS` — meters / metres / liters / litres (singular too) are recognised in `UNIT_RE`,
`has_both` and `MET_RUN` and folded onto m / l in `_skip()`: `800 meters` → `2624.7 ft (800 meters)`, `800-5500 meters` →
`2624.7-18044.6 ft (800-5500 meters)`; (b) `BAG` regex — an `l` figure whose 40 chars before / 25 after name a backpack,
rucksack, bag, compartment, luggage, suitcase, duffel, tote, pouch, sack, daypack or knapsack stays in litres (a size class,
like engine displacement), and `process()` sets `BAG_PRODUCT` when the H2 / benefit bullets name a bag, so EVERY litre figure
of that description stays (`Volume: 3.5 liters` in a spec line carries no bag word); ml is still liquid; `capacity` alone is
deliberately not a bag word (a water bottle's `capacity: 1 L` IS liquid — user's caveat); (c) `COUNT_X` in `convert_run()` —
for a weight / volume unit an integer count before `x` is a count: `Pack of 2 x 500 ml` → `2 x 16.9 fl oz (2 x 500 ml)`, not
`0.1 x 16.9 fl oz`; (d) `(?P<axis>)` in `MEAS` — an axis label straight after the unit travels with it so the parenthesis lands
after the label: `9.45 in L x 7 in W` → `9.45 in L (24 cm) x 7 in W (17.8 cm)`; `imperial_only` keeps the label and
`DROP_PAREN` tolerates it. Fixture-tested: 25 dual cases (the five above, `2 metres`, `Capacity: 1 L water bottle` →
`33.8 fl oz (1 L)`, `Set of 3 x 200 g`, `24 cm L x 18 cm W` → `9.4 in L (24 cm) x 7.1 in W (18 cm)`, and every earlier fixture —
`Tank: 250ml`, `engines up to 10.0 L`, `3000mm` rating, `4G`, `3 In 1`, `49mm`, `28.8 * 27.8 * 0.3 cm`, `145 g`, `15.2cm/5.98in`,
`113-131°F`, the dual °F/°C range — unchanged), 7 imperial_only cases, and two full-description fixtures (a backpack: litres
kept everywhere incl. the FAQ question, its `750 ml` bottle holder and `60 cm` still converted; a water bottle: `1 L` / `1.5
liters` converted in prose, list and bullet); every result idempotent; `BAG_PRODUCT` reset after `process()`.
`./rules/description-format-rule.md` §5 gained two sentences (bag litres stay litres like engine displacement; a unit written
as a word converts like its short form). gate.py, struct-check.py, verify.py NOT edited (gate calls unit_dual as a subprocess).
Not run on a live batch yet; the 8 hand-fixed places on the pushed batch already match what the script now produces.

**Refresh note (2026-09-17, GitHub clone route):** `./README-toolkit.md` recomputed (both lines) after a PROCESS CHANGE (user
decision): the toolkit now lives in https://github.com/Aysegulsung/worfa-toolkit, whose root is the work dir, and a session
starts with `git clone` instead of a copy agent re-typing project docs. Only the README header and step 0 changed. The two
credential docs stay in the project and are written to disk at session start. Same day, second pass: the header "Purpose / Use"
sections rewritten for the clone route, README step 0 now writes both credential docs to the manifest paths before the check (so all
57 lines must pass), and the stale "project path claude/…" notes removed from README.
**Refresh note (2026-09-26 — description image layout):** `./spread.py` and `./rules/description-image-layout-rule.md` added at the user's decision (rule: no two images back to back in a description; extras go to section breaks, leftovers into one `div.fewpe-img-grid`; image count/order/src/attributes unchanged). `spread.py` is the user's version plus one patch — `blocks()` splits a `<p>`/`<div>` holding several images into one block per image so `<p><img><img></p>` is detected and verified — and a `--handle` option for a one-product manual test. First store-wide sweep the same day: 3,171 active, 9 changed, 0 grids, verify mismatch 0 / adjacent 0 / style missing 0. README step 7 (`spread.py final`) and verify.py check 18 are NOT wired yet — deferred by the user.

**Refresh note (2026-09-26, second pass — wiring):** `./README-toolkit.md` step 7 now runs `python3 spread.py final` after dim_keep and before the payloads (and step 8 lists the new check); `./verify.py` gained check 18 `image layout` (spread.adjacent() == 0 outside the grid, grid <style> present; 18 checks per product). The 'not wired yet' note in the project description is obsolete from this refresh.


```
6e36cdf2eceaef90f7b31ad30cf75e0a09adef653d41f276e904429840544900  ./DESC-SPEC.md
280607e85b67d6d4cc89d2f56ff1468f546ca5d9b2a39f8026e39d64cd65ca0d  ./EXTRACT-SPEC.md
887ba5c59c4228f224ec6c86fb68732da9ecdc30bd537445f22be12416e8ea35  ./README-toolkit.md
9fefaf0e8e6df0c5152d95672fa161857eefed6bdd55c1e977a978a76f304fdb  ./TITLE-SPEC.md
f8adac2961d2e22f5d62834cae161e565a3747c3b2b2c4dc01e8f27b75ae8544  ./build_check.py
18af4fa1108f5c83e8773ec4d1a27cf8fc2bdfa77ce14e11f979e44055cf15e7  ./cap.py
f68add61a780c188c1811b927cd6e3bc03973a629034276ab089b70c5ffacad4  ./age_check.py
3ba66e25cdf8c1d3f116548e00197b2553a3e1907e4e2e7e8a95c97dd2585b5c  ./assume_check.py
263197d3a05fbb8286e4846f957e14e493b510c90793fff4b33cf179379d103a  ./claims_check.py
b0757ad4fb2b1dd0ca20d03c64aeff9dc878467fe2397235c1f385fef76794bc  ./cta_check.py
96a8718c232e6e2b645c142c0392ea7ee0867269a43ffefb2e3f0744be3c34be  ./desc-check.py
b118dc60532f867439efbc078ac906dbbfda644583f3aa100befab4d1a3ad317  ./extract_html.py
f869bd34e0e4fc64dcb9a92945814d41fd26eb59fbfebb31df51ceb258ab9f4b  ./fact_cover.py
cde1242bc9ef0068eab3e0dc6eb3448da487a390c8ef85c75000c438408f3746  ./factcheck_prompt.md
4dd33c41642f8157bc78d897c4b60ac1d395902675926d84819666c9ecb0d3fa  ./gate.py
b172ebe12906d7f84182c11605cec312000d2847718cf93c40cc58a7e622fdba  ./head_check.py
2e2e2eb2493ba4ab84ab958e7681d5b278a00ca35da3a6abe594a15d41d076ff  ./novel_words.py
e707095eb797499bba92ca2c7dfe4874f772ea6217bf9cb82b1c2af10cf5a23b  ./ov.py
a50108d622e9e91eb5b8e78790968e511b2efd3e786b477f5f39a8ad7bd6da37  ./rules/cta-benefits-metafield.md
e7edcad13e104de345cc1b18aa899ca7d560358f24bfbcaa7510f44a5e02e231  ./rules/dataforseo-credentials.md
5b9435090b4bdbbf3b018b79242d3c9a00e2b465d66bf065819db3162ad553ca  ./rules/description-format-rule.md
1009ea65ea1015faa372ae468977c555b4c986c18e1573c291e295de177bfc4f  ./rules/image-alt-text-rule.md
77ea823f6befff40870ea417021c5ffd602525ed841c891688799bc6a31268bb  ./rules/PROJECT-DESCRIPTION.md
20f2560a880ecc6a627411a27ab77df075ea6f444ae6890fa1e6b76f459e08e2  ./rules/rule-overlap-deferred.md
509ead0d6ada67d244f3e58abc2504037f6ffd2ebbca9bd353eddea1f5192853  ./rules/title-format-rule.md
57c8dfd0dc944c0f2295e8ef7f10f856fd2fe11ad6c87a2f0e341ed3a5491c71  ./source_windows.py
568215e8999a7f380787eb4ba5838628d259ba0ce01a8b183e37d38b8e40d15e  ./spec_cover.py
89949faf996e111896c0c36449da33e6ac1c69fbc2742f28281c1ba8513eb996  ./shopify-api-credentials.md
b3c841c7ad513400ad71311935a3c8d2c65d901caefaea7da65a1e91cb7c1931  ./shopify_api.py
79d0718a36858571738ed08b771852510c4c327f872afdcade82bac0fcc98d7e  ./struct-check.py
4b18033b4652390bc8158aa636878f0ec5940a7392854ace0a1712ba93e59344  ./title-check.py
daa5a5569314a46cd6893b57e75409ac344700d33729d8c4c2cb264e2804ac16  ./usage-efficiency-runbook.md
420431d7b50507a524c1140eb0bcdd7ad6e04c6290246d99a0b5dd767db12205  ./value_check.py
0218c9810e40e32ab4848ef1cc3bd0b5d9fbd69d1b4d0a6157b9dbd9f8ac4f9c  ./verify.py
cc3eb76be50368dd7309c11ecf7397ba7c28e406c26c71f8b484588b9c6ad4aa  ./rehost.py
64204063ef248cb55cf67a53b0fcaf3321947962c8550452e075d13e7808afc4  ./compare_build.py
33b8474d720f7967de0e899893789ed0bba9c0ff1db14f2ef610859fafba27ce  ./rules/comparison-table-rule.md
89924d661367c9ab8a70594193e9749f093ed70f0f372a11832d899b4f98272b  ./dim_image.py
18ff02a467edfa90758d943af8851d5878bc4609c7550cb6687a222f44b8bace  ./dim_attach.py
2e8bd0864f237bfba8ea0fb0c0b804cfe30fc2a24623c9daca3de7b03e512da0  ./dim_keep.py
4bb7a28cfb2df4328f8e6562896390e09a3d3bc73d73154444706102560334dd  ./rules/dimension-image-rule.md
1a52c1a05eb7182eb8dc3e1d27e9f6063a579949c4b07b43a3b1cf2ebfbfc874  ./fit_build.py
6ad7803d930d50538a84d18d3df1d28d56101c976f2111165a31d68780f79c9b  ./rules/fit-block-rule.md
1d5a90d740c28cd881d617ce9b89a0a5b3efbc6d7e9525389c50ef433ddc5b7d  ./CTA-REVIEW-SPEC.md
e15cebe0fde55247966cb6eab106660a3c0c44a0eb6db2f40151b6e9bde079d8  ./keyfeat_cover.py
a7b306d3d560c8e315c2b2d7f30ea833478b8889695cafdffe8e81c97fd4455f  ./unit_dual.py
e08c21d0b6fe0951e3c929318b2e2d7a757a4ed724d48bcc6369fb1fd047baff  ./para_feat.py
87b17ae7b1e631dee6996441a52bfa46a66cc7961fe9f7a35777ebd18f1af356  ./extract_check.py
e4c4050841aeea9b3b8180386f3bdc2eef070b8936c6a240d766bcd58bd08875  ./KF-REVIEW-SPEC.md
ca3d7b1753cfc850588e7f746886fb6bc161bf6c65f488553b017dc3d6be70b3  ./kf_review_input.py
91abc9b4f3a73b1b70372a91e965ee14be01feee93892ee2443ce9ffa3e2aaac  ./howto_check.py
02b0d2e9de323b1167d42c637d13ff244a3e0833667087cbee2dbb3b1a0d80d9  ./usage_tips.py
39a98da89746f08bc685f4858c7e8edd1bfbc36d31b373f8fdef5c71436d6996  ./sections.py
b9e5e7c8d227335dd3dbf75f54f9efe02968b49ecf34d38c9b360f9f6d24416c  ./kw_measure.py
887ba5c59c4228f224ec6c86fb68732da9ecdc30bd537445f22be12416e8ea35  ./README-toolkit.md
ecf9731e745ef965f65733a7c7cf530046dc25bea32681c40c6bc05a87e67ea2  ./rules/kw-order-variant-rule.md
7c86386a6f77ab101bd60957e78df39449751dce01cf61c7f0eb6da2ffad4d74  ./list_bold.py
b3b64dd58e7faff215653dd17d1d7cd74d1ccd9e4ae76c2580c273a5273fbb51  ./fix_sections.py
3b8daef9a896547894840edc1503d009e2f553fc9eebae2140f14ee1d01003f9  ./spec_parse.py
c764be4b770640f37ca52694f7badc893d8a7499e2d9f8deeaa78dd263ec985a  ./build_payloads.py
e1a23bcabc124e327d07c0d3d6441e416c0dbdba53cf08d2b93600e36a6a4957  ./spread.py
55e1c514315857a0b72eed43a09e2b42233996e2d2aeb4892cb3d439f4e066bf  ./rules/description-image-layout-rule.md
f6a30feb43e76f614cf6a9ad95a329b183c6ea70a6a98a80aec5f9d4590d5a41  ./normalise_cm.py
```
