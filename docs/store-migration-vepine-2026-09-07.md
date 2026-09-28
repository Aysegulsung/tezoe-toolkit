# Store migration — Tuzwa → Vepine (2026-09-07)

User instruction: nothing Tuzwa is used any more; the project runs on the **Vepine** store and brand only.

## Vepine constants (measured, not assumed)

| Constant | Value | How it was obtained |
|---|---|---|
| Store name | `Vepine` | Shopify connector `shop { name }` |
| Storefront | `vepine.com` | connector `primaryDomain` |
| Admin host | `ate3yx-gz.myshopify.com` | connector `myshopifyDomain` — there is no `vepine.myshopify.com` alias |
| CDN prefix | `cdn.shopify.com/s/files/1/0992/7645/6222/` | read off live Vepine file URLs |
| Navy (heading band, our column, dimension lines, fit heading) | `#000096` | rendered Add-to-cart button on vepine.com, 2026-09-07 |
| Light blue (table header row) | `#d2def6` | header section band on vepine.com, 2026-09-07 |
| Green circle-tick | `#2e9e4f` (unchanged) | fixed success colour, not a theme colour |

## What was changed (19 forward-looking files)

- **CDN prefix** in `gate.py`, `struct-check.py`, `build_check.py`, `verify.py`, `rehost.py`, `extract_html.py`,
  `DESC-SPEC.md`, `README-toolkit.md`.
- **Brand constants**: `compare_build.BRAND = 'Vepine'`, `verify.BRAND = 'vepine'`, the brand-in-copy scan in `gate.py`.
- **Comparison table**: heading `Why choose Vepine`, header cells `Vepine <name>` · `Vepine` · `Others`, navy and
  light-blue swapped to the Vepine values. Rendering + `parse_block()` round-trip smoke-tested after the change.
- **CSS hooks renamed** `tz-` → `vp-`: `vp-compare`, `vp-store`, `vp-fit` — changed together in `compare_build.py`,
  `fit_build.py`, `struct-check.py`, `verify.py`, `unit_dual.py`, `description-format-rule.md`,
  `comparison-table-rule.md`, `fit-block-rule.md`. No live Vepine description carries the old class, so nothing
  needs re-rendering.
- **`shopify-api-credentials.md` rewritten** for Vepine. The previous store's Client ID / secret were removed, not
  carried over — they grant no access to Vepine.
- Rule docs (`comparison-table-rule.md`, `dimension-image-rule.md`, `fit-block-rule.md`): brand, colours, and the
  provenance line now reads "User decision 2026-09-06 (now applied to Vepine)".

## What was deliberately NOT changed

The 86 run logs, kw-caches, audits and pre-push backups under `claude/` still say Tuzwa, and two root docs keep a
historical mention (`cta-benefits-metafield.md` blr-batch11 line, `usage-efficiency-runbook.md` §9 measurement).
These are records of work done on the Tuzwa store — in particular the `backup-titles-*` and `backup-alt-*` files are
restore snapshots of Tuzwa products. Relabelling them Vepine would make it possible to restore another store's titles
onto Vepine products. User decision 2026-09-07: leave them as history.

## Blockers before the first Vepine run

1. ~~App credentials pending.~~ **Supplied 2026-09-07** — the pair is in `toolkit/shopify-api-credentials.md`.
   (That 2026-09-07 pair was replaced on 2026-09-10; the ID that used to be quoted here has been removed with it.
   `toolkit/shopify-api-credentials.md` is the only place credentials live.)
2. ~~Egress allowlist.~~ **Done 2026-09-07** — `ate3yx-gz.myshopify.com` connects from the container; the earlier
   403 CONNECT failures are gone.
3. ~~App not installed on Vepine.~~ **Done 2026-09-07** — first attempt returned `Oauth error app_not_installed`;
   after the user installed the app the token call succeeds.

**All blockers cleared. Verified end to end 2026-09-07 through `shopify_api.py`:** token issued; `shop { name }` →
Vepine / ate3yx-gz.myshopify.com / USD; app `Claude Backend` with `read/write_files`, `read/write_products`,
`read/write_publications`; and a CDN sweep over 200 products / 1,620 media images found every image on
`/s/files/1/0992/7645/6222/` with 0 foreign hosts — the prefix hard-coded in the checkers matches live data.

Still open before the first batch: `collections.json` must be refreshed for Vepine (`README-toolkit.md`, store
constants), and the comparison block's colours (`#000096` / `#d2def6`) should be confirmed by screenshot on the
first live Vepine push.
