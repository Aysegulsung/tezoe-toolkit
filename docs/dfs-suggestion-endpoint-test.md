# DataForSEO öneri endpoint'leri — tek ürün testi (blr-batch13 #09, bidet attachment)

Tarih: 2026-09-04 · Ürün: `gid://shopify/Product/10076466544864` (Bidet Attachment for Toilet Seat, non-electric, dual nozzle)
Karşılaştırma tabanı: bu ürün için `kw-cache-blr-batch13.md`'de ölçülmüş 65 aday (Haiku'nun ürün verisinden ürettiği set).

Amaç: adayları modelin tahmininden değil DataForSEO'nun kendi öneri verisinden almak, mevcut süreçten ne kadar farklı sonuç veriyor ve ne kadara mal oluyor — ölçmek.

---

## 1. Çalıştırılan çağrılar ve gerçek maliyet

Dördü de container'dan doğrudan `curl`/urllib ile, US (2840) / en. Maliyetler API yanıtının kendi `cost` alanından okundu, tahmin değil.

| Endpoint | Dönen kayıt | Maliyet |
|---|---|---|
| `keywords_data/google_ads/keywords_for_keywords/live` (3 tohum) | 1.441 | **$0,09** |
| `dataforseo_labs/google/keyword_suggestions/live` (limit 300) | 300 | **$0,048** |
| `dataforseo_labs/google/related_keywords/live` (depth 2) | 48 | **$0,01776** |
| `dataforseo_labs/google/keyword_ideas/live` (limit 300) | 300 | **$0,048** |
| **Toplam — 1 ürün** | 1.872 tekil | **$0,20376** |

Ölçek: 50 ürünlük bir batch'te dördü birden ≈ **$10,19**. Sadece en verimli tek endpoint (`keyword_suggestions`, $0,048) ≈ **$2,40**. Bugünkü tüm batch'in keyword maliyeti (3.304 keyword, 4 çağrı) **$0,36**.

---

## 2. Ne çıktı

- 1.872 tekil öneri; bunların **18'i** zaten mevcut aday setinde vardı, **1.854'ü** yeniydi (1.818'i hacim döndürdü).
- Yeni olanların 1.246'sı "bidet/washlet" içeriyor. Onları ayırınca:
  - **579 marka/perakendeci terimi** — tushy, luxe bidet neo 120/185/320, brondell, toto, samodra, veken, home depot… Bunlar bizim ürünümüz için kullanılamaz.
  - **30 salt permütasyon** — zaten ölçtüğümüz bir keyword'ün kelime sırası değişmiş hâli; hacim ve CPC birebir aynı (ör. `bidet attachment for toilet` 33.100 ↔ `toilet with bidet attachment`, `bidet attachment toilet`, `attachment bidet` — hepsi 33.100 / 1,43). Google Ads bunları aynı arama olarak raporluyor; contiguous-phrase kuralı açısından yeni bir şey kazandırmıyorlar.
  - **637 gerçekten yeni, marka dışı** keyword. Bunların **16'sı ≥1.000**, **88'i ≥100** hacimli.

### ≥1.000 hacimli 16 yeni keyword'ün ürün-fit denetimi (§6)

| Hacim | Keyword | Fit |
|---|---|---|
| 40.500 | bidet toilet seat | ✗ farklı ürün formu (koltuk, attachment değil) |
| 27.100 | portable bidet | ✗ sabit montaj ürünü |
| 14.800 | electric bidet toilet seat | ✗ hem elektrikli hem koltuk |
| 8.100 | toilet with bidet | ✗ klozetin kendisi |
| 8.100 | electric bidet seats | ✗ |
| 6.600 | luxebidet | ✗ marka |
| 3.600 | best bidet attachment | ✗ "best" iddiası — kaynakta yok |
| 3.600 | non electric bidet toilet seat | ✗ koltuk |
| 3.600 | toilet seat bidet non electric | ✗ koltuk |
| 3.600 | bidet attachment best | ✗ "best" |
| 1.300 | best bidet attachment for toilet | ✗ "best" |
| 1.300 | non electric bidet seat | ✗ koltuk |
| 1.300 | best bidet attachment for toilets | ✗ "best" |
| 1.000 | best non electric bidet | ✗ "best" |
| 1.000 | non electric bidet toilet | ~ sınırda (ürün klozet değil, klozete takılan parça) |
| 1.000 | affordable bidet attachment | ✗ fiyat iddiası |

**≥1.000 bandında fit geçen keyword sayısı: 0 (biri sınırda).**

Fit'i geçebilecek gerçek yeni bulgular hep düşük hacimde ve uzun kuyrukta:
`bidet hose attachment` (320) · `bidet attachment for existing toilet` (390) · `bidet adapter` (260) · `bidet attachment for round toilet` (260) · `bidet attachment for standard toilet` (140) · `portable bidet attachment` (110) · `bidet attachment with dryer` (110, ürün fit değil).
Sıcak su ailesi (`warm water bidet attachment` 590, `hot water bidet attachment` 590, `heated bidet attachment` 390) hacim olarak cazip ama bu üründe sıcak su kaynakta doğrulanmıyor — RULINGS mantığıyla zaten reddedilir.

---

## 3. En önemli bulgu — öneri endpoint'i mevcut seti kapsamıyor

Mevcut aday setinde hacim dönen 39 keyword'ün **yalnızca 18'i** dört endpoint'ten herhangi biri tarafından geri döndürüldü. Döndürülmeyen 21 tanesinin içinde şunlar var:

`bidet` (165.000) · `bidets` (165.000) · `bidet sprayer` (4.400) · `bidet for toilet` (4.400) · `toilet seat bidet` (3.600) · `self cleaning bidet` (1.000) · `hand held bidet sprayer` (1.000) · `bidet t adapter` (880) · `toilet bidet sprayer` (2.900) · `bidet attachment for elderly` · `bidet attachment no electricity` · …

Yani öneri endpoint'leri mevcut üretimin üst kümesi değil. Ürünün kendi verisinden çıkan aday listesinin yerini alamaz, olsa olsa yanına eklenir — bu da adım eksiltmez, ekler.

Ayrıca: bu testte tohum keyword'leri (`bidet attachment`, `non electric bidet`, `bidet attachment for toilet`) ben elle seçtim. Yani endpoint model tahminini ortadan kaldırmıyor, sadece "40–70 aday tahmin et"i "1–3 tohum tahmin et"e çeviriyor. Tohum yanlışsa dönen 1.400 satırın tamamı yanlış eksende oluyor.

`keyword_ideas` bu açıdan en kötüsü: aynı *kategoriden* keyword döndürüyor ve ilk 50 sonucu `washer and dryer set` (246.000), `dyson hair dryer` (201.000), `toilet flapper` (135.000), `dryer vent cleaning service` gibi tamamen alakasız terimlerdi. Bu endpoint bu iş için kullanılamaz.

---

## 4. Sonuç

| | Mevcut süreç | Öneri endpoint'i eklenirse |
|---|---|---|
| Batch keyword maliyeti | $0,36 | $2,76 – $10,55 (hangi endpoint'lerle) |
| Süreçteki adım | 1 (ölç) | 2 (öner + ölç) |
| Bu üründe fit geçen yeni ≥1.000 keyword | — | 0 |
| Bu üründe fit geçen yeni uzun kuyruk | — | ~5 adet, 110–390 hacim |

Bu tek ürün için ölçülen fark, maliyeti karşılamıyor. Marka terimleri ve farklı ürün formları (koltuk/elektrikli/taşınabilir) fit kapısında zaten eleniyor; geriye kalan gerçek katkı 110–390 hacimli birkaç uzun kuyruk.

**Yapılmadı / doğrulanmadı:**
- Test tek üründe yapıldı; başka kategorilerde (oyuncak, aydınlatma, seyahat çantası) sonuç farklı olabilir — özellikle Haiku'nun ürün verisinden çıkaramayacağı jargonlu kategorilerde.
- Bu yeni keyword'lerle #09'un başlığı yeniden kurulup mevcut başlıkla captured-volume karşılaştırması **yapılmadı**.
- Hesap bakiyesi bu oturumda doğrulanamadı (kontrol komutu bloklandı); yalnızca çağrıların kendi `cost` alanları raporlandı.

Süreç değiştirilmedi; bu bir ölçüm notudur.
