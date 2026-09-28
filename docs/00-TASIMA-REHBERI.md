# Backend-DataForSEO projesini başka bir Claude hesabına taşıma rehberi (2026-09-09, mağaza değişikliği 2026-09-10)

> **2026-09-10 — mağaza Vepine'den Worfa'ya geçti.** Aşağıdaki adımlar geçerli; mağazaya bağlı değerler (host,
> CDN prefix, BRAND, kimlik bilgileri) Worfa'ya güncellendi. `claude/` altındaki run-log / backup-titles /
> backup-alt / kw-cache kayıtları ve `store-migration-vepine-2026-09-07.md` bilerek Vepine olarak bırakıldı —
> bunlar Vepine ürünlerinin geri-alma anlık görüntüleridir.

Bu zip, "Backend-DataForSEO-Updated" projesinin tamamıdır: proje açıklaması + 91 proje dokümanı.

## Adımlar
1. Yeni hesapta yeni bir Proje aç (adı serbest; öneri: Backend-DataForSEO-Updated).
2. `00-PROJE-ACIKLAMASI-GUNCEL.md` içeriğini olduğu gibi projenin **açıklama / özel talimat** alanına yapıştır.
   (Kökteki eski `PROJECT-DESCRIPTION.md` 2026-09-03 sürümüdür; güncel olan bu dosyadır.)
3. Aşağıdaki klasör yapısını **aynı yol adlarıyla** projeye yükle — README-toolkit.md ve MANIFEST.md bu yolları sabit bekler:
   - `toolkit/…`  (42 dosya: shopify_api.py, gate.py, verify.py, README-toolkit.md, MANIFEST.md, kimlik bilgileri …)
   - kökteki kural ve kontrol dosyaları (description-format-rule.md, title-format-rule.md, title-check.py, desc-check.py,
     cta-benefits-metafield.md, image-alt-text-rule.md, usage-efficiency-runbook.md, dataforseo-credentials.md, README.md …)
   - `claude/…`  (comparison-table-rule.md, dimension-image-rule.md, fit-block-rule.md, rule-overlap-deferred.md,
     store-migration-vepine-2026-09-07.md + run-log / backup-titles / backup-alt / kw-cache geçmiş kayıtları)
   Proje aracı köke yazamadığı için kural dokümanlarının üçü `claude/` altındadır — öyle kalsın.
4. Yükledikten sonra ilk oturumda doğrula: dosyaları diske kopyalat ve `sha256sum -c 00-EXPORT-CHECKSUMS.sha256` çalıştır.
   Bu liste bu zip'teki dosyalardan üretildi; toolkit/MANIFEST.md'deki blok da çalışır (bkz. not 2).
5. Yeni hesapta ayrıca yapılması gerekenler (projeyle taşınmaz):
   - Shopify bağlayıcısını (MCP) bağla — sadece mağaza kimliği için kullanılıyor; fetch/push script yoluyla.
   - Egress allowlist: `ymjviw-rz.myshopify.com` (Worfa), `cdn.shopify.com`, `api.dataforseo.com` erişilebilir olmalı.
     Bu host container'dan hiç çağrılmadı; ilk çalıştırmada 403 CONNECT ihtimali var.
   - Google Drive bağlayıcısı (eski batch arşivleri `Vepine/<tag>/` klasöründe; Worfa arşivleri `Worfa/<tag>/`).

## Zorunlu olmayan dosyalar
`claude/run-log-*`, `backup-titles-*`, `backup-alt-*`, `kw-cache-*` geçmiş kayıtlarıdır; çalıştırma için gerekmez.
Ancak `backup-titles-*` ve `backup-alt-*` **Vepine** ürünlerinin geri-alma yedekleridir; Worfa'ya geri yüklenemezler.
Vepine hâlâ elindeyse sakla, değilse bu dosyalar sadece arşiv değeri taşır.
Proje 2 MB sınırına yakın (675 KB dolu); yer açmak istersen önce kw-cache dosyalarını dışarıda bırak.

## Değiştirilmesi gereken bilgiler
- **Aynı mağaza (Worfa) + aynı DataForSEO hesabı:** hiçbir şey değişmez. Shopify Client ID/secret mağazaya bağlıdır,
  hesaba değil. `toolkit/shopify-api-credentials.md` ve `dataforseo-credentials.md` aynen çalışır.
  Güvenlik: bu iki dosya düz metin gizli anahtar içerir; zip'i başkasıyla paylaşıyorsan secret'ları Shopify Dev
  Dashboard / DataForSEO panelinden yenile.
- **Farklı mağaza:** `claude/store-migration-vepine-2026-09-07.md` (Tuzwa→Vepine) ve toolkit/MANIFEST.md'deki
  2026-09-10 "STORE CHANGE Vepine → Worfa" notu birlikte tam listedir — kısaca: shopify-api-credentials.md
  (host, Client ID, secret; yeni mağazaya kurulu custom app, scope: write_files, write_products, write_publications),
  CDN prefix (gate.py, struct-check.py, build_check.py, verify.py, rehost.py, extract_html.py, DESC-SPEC.md,
  README-toolkit.md), BRAND sabitleri (compare_build.py, verify.py, gate.py), tablo renkleri/başlığı (compare_build.py),
  collections.json yeniden çekilir, sonra toolkit/MANIFEST.md hash'leri yeniden hesaplanır.

## Notlar
1. Bu dışa aktarma proje aracıyla okunup diske yazıldı; her dosya en az iki bağımsız kopyayla (toolkit dosyaları ayrıca
   MANIFEST sha256 ile) doğrulandı. Tüm .py dosyaları `py_compile` ile derlendi.
2. `toolkit/MANIFEST.md` içindeki `unit_dual.py` satırı projedeki güncel dosyaya göre eskidir (dosya 2026-09-09 10:41'de
   güncellendi, satırı yenilenmemiş). İki bağımsız kopya birebir aynı çıktı; MANIFEST kural 6'ya göre satır bayat sayılır.
   `dim_image.py` de (12:54 güncellemesi) MANIFEST satırıyla eşleşmiyor; içerik projedeki kaynakla satır satır doğrulandı.
   Yeni hesapta ilk oturumda bu iki satırı `sha256sum` ile yeniden hesaplatıp MANIFEST.md'ye yazdır.
