# Run log: Q11 CTA benefits — ddl1 batch 1-6 (2026-09-02)

Tümü conversion odaklı benefit diliyle (problem→çözüm, spec değil) yazıldı. Format: custom.cta_benefits, 3 madde, `icon_key|Metin`, ~30 kr altı, İngilizce.

Sonuçlar (hepsi userErrors=0):
- batch1: 49 ürün — önce spec dille yazıldı, sonra conversion diliyle ÜZERİNE YAZILDI ✓
- batch2: 49 ürün (Shipping Protection atlandı) — conversion diliyle üzerine yazıldı ✓
- batch3: 50 ürün — conversion diliyle üzerine yazıldı ✓
- batch4: 50 ürün — doğrudan conversion diliyle ✓
- batch5: 50 ürün — doğrudan conversion diliyle ✓
- batch6: 50 ürün — doğrudan conversion diliyle ✓ (2026-09-02, spot-check: nut milk maker, snowflake projector)
- Test ürünü (Digital Picture Frame): orijinal outcome-dilli değerler korundu ✓
TOPLAM: 299 ürün, ~22 metafieldsSet çağrısı.

Spot-check örnekleri: "Never stranded again", "Never buy ink again", "Ends gulped-down meals", "Breeze through security", "Fresh milk at one touch", "A wall of falling snow".

Notlar:
- Benefit dili kuralı claude/cta-benefits-metafield.md'de (❌spec → ✓çözüm örnekleriyle).
- Fallback ikon çember+tik olarak kurala girdi; kullanıcının temadaki cta-benefits bloğunu tam güncel kodla değiştirmesi bekleniyor (kod konuşmada verildi; Klaviyo script'li custom_liquid bloğuna DOKUNULMAYACAK).
- Draft ürünlerde benefitler yayına alınınca otomatik görünür; tema tarafına dokunulmadı.
