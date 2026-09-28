# Run Log — İç not sızıntısı taraması, ddl1-batch1…5 (Vepine) — 2026-09-02

Bu log beş batch'in run-log'larına ek olarak okunur (`claude/run-log-ddl1-batchN.md`).

## Tespit (kullanıcıdan)

ddl1-batch5 kontrolünde yazarın kendi iç notlarının müşteri metnine sızdığı görüldü:
"the supplier states no level count, so we claim none", "the safety wording the source
omits", "we make no leather claim", Winter Boots FAQ "leather wording on the images is
leftover text from another listing", spec başlığı `What Is Not Claimed:`, parantez hedge
`(which fingers is not stated)`, "The supplier's two timer figures contradict, so no
duration is quoted", makyaj çantasında `Also Sold As:` alias listesi.

## Kural

`description-format-rule.md`'ye üç push-engelleyici hard rule eklendi: (1) iç not /
kaynak dili yasağı, (2) üç yasaklı Specifications formu (yokluk başlığı, parantez hedge,
çelişki notu), (3) `Also Sold As:` ve her türlü alias listesi yasağı. Gate:
`claude/desc-check.py` — sabit regex listesi + semantik olumsuzlama taraması, title /
descriptionHtml / seo.title / seo.description alanlarında; isabet = o ürün için push durur.

## Yöntem

- Beş batch canlıdan çekildi (50'şer ürün, `tag:ddl1-batchN`), snapshot `bN.json`.
- İsabet alan elementler (`<p>|<li>|<h2>|<h3>`) tek tek çıkarıldı, elle yeniden yazıldı,
  element-düzeyinde geri yerleştirildi (tam tek eşleşme assert'i; `<img>` listesi, FAQ
  sayısı, boş element ve kelime sayısı kontrolü).
- Gate gün içinde **dokuz kez** genişletildi ("published", "unconfirmed", "listed for",
  "nothing states", "(maker stated)", "no size chart is supplied", "unstated",
  "uncertified", "spec list", "source spec line … contradicted" vb.). Her genişletmeden
  sonra beş batch'in tamamı yeniden tarandı. Son üç kusurlu ürün (nemlendirici, ısıtmalı
  yelek, yüz maskesi) yalnızca canlıdan yeniden çekilen veride yakalandı — genişletilen
  gate'in yalnızca fix set üzerinde çalıştırılması yetmedi. **Kural: genişletme sonrası
  tarama her zaman taze canlı çekimden yapılır.**
- Push: 10'ar (sonra ≤9'ar) ürünlük aliased `productUpdate(product:)`, yalnızca `id` +
  `descriptionHtml`; hepsi 0 userError.

## Düzeltme kalıpları

Değeri yalnızca "not stated" olan spec satırı → satır silindi · gerçek değer + hedge
parantezi → parantez düşürüldü · "the supplier omits" giriş cümlesi → nötr giriş ·
cevabı "bilmiyoruz" olan FAQ → kaynağın cevaplayabildiği soruyla değiştirildi (her zaman
5 FAQ) · güvenlik talimatı korunup kaynak atfı düşürüldü · "the maker rates it to X" →
"rated to X" · "uncertified" → özellik düz yazıldı ya da sorumluluk cümlesi düz yazıldı
("not personal protective equipment and not a medical device") · "the spec list gives
16 x 15 x 18 cm" → "About 16 x 15 x 18 cm" · satranç tahtası 39/40 cm çelişkisi sessizce
39 cm · alias listeleri prose'a doğal biçimde yeniden dokundu.

Bilinçli olarak yasaklanmayanlar (mağaza sesi): "sold as/in/for", "not included",
"not for submersion", "not a medical device", "no child sizing is offered".

## Sonuç — batch başına

| Batch | Taranan | Düzeltilip yeniden push edilen | Canlı son doğrulama |
|---|---|---|---|
| ddl1-batch1 | 50 | 2 | temiz |
| ddl1-batch2 | 50 | 0 | temiz |
| ddl1-batch3 | 50 | 21 | temiz |
| ddl1-batch4 | 50 | 45 | temiz |
| ddl1-batch5 | 50 | 43 | temiz |
| **Toplam** | **250** | **111** | **0 isabet** |

Son push sonrası beş batch canlıdan yeniden çekildi: gate 0 isabet; semantik tarama 0
gerçek isabet (tek eşleşme "at a glance without opening the lid" — yanlış pozitif);
250 üründe `<img src>` listesi tarama öncesi snapshot ile birebir aynı (görsel eklenmedi,
silinmedi, yer değiştirmedi); tüm seo.title < 70, seo.description < 160; her üründe 5 FAQ;
boş `<p>/<li>/<ul>` yok.

## Bu taramanın dışında kalan, önceden bilinen açık konular

- batch4 #31 puffer mont (`15869035315486`): ikinci açıklama görseli başka mağazanın
  CDN'indeydi (`1/0654/9028/8866/...FLORA-Jacket_Model_Image`, kaynak 404). **Kullanıcı
  kararı (2026-09-02): 404 veren görsel silinir, yerine ürünün kendi galeri fotoğrafı
  konur.** Uygulandı: `src` galerideki `..._Black_8_...jpg` (Vepine CDN) ile değiştirildi,
  etiket/sarmalayıcı/attribute'lar aynı, görsel sayısı 2; push 0 hata, canlıda doğrulandı.
  Beş batch'te artık yabancı host'ta hiçbir açıklama görseli yok. Kural
  `description-format-rule.md` Hard rules'a eklendi.
- batch2 "Shipping Protection" hizmet ürünü: FAQ yok, tek boş `<p>` — gerçek ürün değil,
  dokunulmadı.

## Düzeltilen ürünler

### ddl1-batch1 (2)

- 15869044326686 — Bathroom Wall Sconces Vanity Light, Frosted Glass Globe Wall
- 15869044392222 — Led Wall Lights Dimmable, Square Modern Wall Light Fixture 1

### ddl1-batch2 (0)

- yok

### ddl1-batch3 (21)

- 15869038559518 — Fairy Lights, Solar Fairy Lights Battery Operated, Warm Whit
- 15869038625054 — Olive Branches with Lights, Faux Olive Branch Greenery Stems
- 15869038723358 — Gift Boxes for Packaging, Custom Gift Boxes with Ribbon, Mag
- 15869038821662 — Car Seat Cushion for Baby, Infant Car Seat Insert with Head 
- 15869039116574 — Mouse Repellent Plug In, Ultrasonic Pest Repeller for Indoor
- 15869039444254 — Ratchet Straps Heavy Duty Retractable with Soft Loops, Cargo
- 15869039477022 — Socks for Women, Thick Winter Socks 6 Pairs, Warm Knit Socks
- 15869039837470 — Side Tables for Living Room, Round Side Table Small Accent T
- 15869039968542 — Baby Carrier Shirt Hands Free, Baby Wrap Carrier T Shirt for
- 15869040165150 — Plush Toys Talking Parrot Toy, Interactive Plush Toy That Re
- 15869040197918 — Christmas Tree Artificial Slim, Pencil Christmas Tree with S
- 15869040263454 — Kitchen Faucet Vintage, Antique Brass Faucet with Swivel Spo
- 15869040296222 — Dish Drying Mat for Kitchen Counter, Diatomaceous Earth Mat 
- 15869040427294 — External Hard Disk, Portable Storage Drive for Mac and Windo
- 15869040460062 — Tissue Box Cover Decorative, Tissue Box Holder in Dancing Fi
- 15869040558366 — Humidifier and Air Cooler 2 in 1, Mini Humidifier for Bedroo
- 15869040591134 — String Lights, Outdoor String Lights with Copper Wire and 20
- 15869040623902 — Night Light Acrylic Moon, Village Scene Table Decor with Sof
- 15869040656670 — Key Finder, Bluetooth Tracker for Keys and Bags, Bluetooth K
- 15869040722206 — Wireless CarPlay Adapter, Apple CarPlay and Android Auto Don
- 15869040754974 — Apple CarPlay Screen, Portable Car Stereo with CarPlay and A

### ddl1-batch4 (45)

- 15869030957342 — Clear Gel for Face and Body, Face Gel Tube with Precision Ap
- 15869031022878 — Foot Pads with Bamboo and Mineral Powder, Adhesive Foot Patc
- 15869031088414 — Work Gloves with Reinforced Knuckle Panel, Grip Palm Mechani
- 15869031153950 — Wall Shelf with Rail for Bottles, Barrel Style Wall Mounted 
- 15869031285022 — Lounge Bra with Adjustable Straps, Towel Bra Sweat Wrap with
- 15869031350558 — Pedicure Liners for Foot Spa Tubs, Disposable Pedicure Liner
- 15869031383326 — Foot Spa Machine with Ionic Array Module, Ionic Foot Bath Ma
- 15869031448862 — Glasses Cleaners for Eyeglass Lenses, Portable Eyeglass Clea
- 15869031481630 — Bird Feeder Cameras with Solar Roof, Smart Bird Feeder with 
- 15869031514398 — Interactive Plush Toys, Giraffe Stuffed Animal that Sings Nu
- 15869031579934 — Photo Paper and Printer Refill Cartridges, 4x6 Photo Paper R
- 15869031612702 — 4x6 Photo Printers, Bluetooth Printer for Smartphone Photos,
- 15869031645470 — STEM Toys for Kids, Take Apart Animal Construction Toys with
- 15869031678238 — Hair Curlers, Heatless Curlers and Heatless Curling Rods, So
- 15869031711006 — Bird Feeders for Outside, Squirrel Proof Bird Feeders with R
- 15869031776542 — Mini Cameras with Audio, Small Camera with Motion Detection,
- 15869031809310 — Seat Cushions for Home, Tufted Velvet Dining Chair Cushions,
- 15869031907614 — Adjustable Focus Eyeglasses, Adjustable Reading Glasses, Non
- 15869032104222 — Interactive Dog Toys, Light Up Dog Ball with Flashing LED Li
- 15869032202526 — Screen Repair Kit for Phones, DIY Glass Repair Kit with Liqu
- 15869032333598 — Rechargeable Flashlight for Power Outage, Everyday Carry Fla
- 15869032497438 — Car Phone Holder for Dashboard, Silicone Phone Stand for Car
- 15869034561822 — Hardwood Floor Cleaner for Mopping, Multi Surface Cleaner fo
- 15869034725662 — Dog Chew Toy for Puppies, Plush Dog Toy for Tug of War, Soft
- 15869034889502 — Blow Dryer Brush, One Step Hair Dryer Brush and Hot Air Styl
- 15869035217182 — Winter Jackets for Women, Plus Size Quilted Jacket, Womens P
- 15869035315486 — Puffer Jackets, Black Puffer Jacket for Women with Hood and 
- 15869035512094 — Wireless Bras for Women, Comfortable Bra with Underbust Supp
- 15869035708702 — Liquid Foundation Makeup, Cushion Foundation Compact with Ap
- 15869035872542 — Cord Organizer Bag, Travel Cable Organizer Case for Chargers
- 15869036134686 — Mandoline Slicers, Handheld Mandoline Slicer with Stainless 
- 15869036298526 — Label Makers and Label Printer for Phone, Portable Thermal P
- 15869036429598 — Solar Lights, Outdoor Solar Light for Walkway, Crackle Glass
- 15869036626206 — Gift Boxes with Pop Up Cards, Birthday and Christmas Gift Bo
- 15869036790046 — Running Shoes for Women, Womens Walking Shoes and Casual Sne
- 15869036953886 — Buffing Pads, Angle Grinder Buffing Wheel and Wool Polishing
- 15869037248798 — Robot Puppy Toy for Kids, German Shepherd Plush Toy Puppy, I
- 15869037478174 — Vanity Mirror with Lights, Lighted Vanity Mirrors with 3x Ma
- 15869037674782 — Heated Vest for Women, Electric Heated Vests with 3 Heat Set
- 15869037904158 — Small Outdoor Table with Ground Spike, Wooden Wine Table, Wi
- 15869038133534 — Chess Board Game with Storage, Wooden Chess Boards with 32 P
- 15869038297374 — Dinosaur Toys and Dinosaur Truck Playset with Cage Back, 4 D
- 15869038330142 — Face Masks for Cycling and Commuting, Reusable Face Masks wi
- 15869038362910 — GPS Tracker for Kids, Portable GPS Tracking Device for Kids,
- 15869038395678 — Portable Heating Pad for Knee, Adjustable Heated Knee Wraps,

### ddl1-batch5 (43)

- 15869028335902 — Strainers for Pasta and Vegetables, Clip On Pot Strainer for
- 15869028401438 — Warmers for Hands, Metal Hand Warmers Reusable, Aluminum Ele
- 15869028466974 — Warmers for Hands, Rechargeable Hand Warmers, Multiple Heat 
- 15869028499742 — Warmers for Hands, One Button Rechargeable Hand Warmers, Adj
- 15869028532510 — Winter Gloves for Women and Men, Warm Gloves with Non Slip G
- 15869028565278 — Warmers for Hands, Electric Hand Warmers with LED Display, 5
- 15869028598046 — Warmers for Hands, Hot Hand Warmer with LCD Display, Plush E
- 15869028630814 — Warmers for Hands, Magnetic Rechargeable Hand Warmers, 4000m
- 15869028663582 — Warmers for Hands, Hand Warmers Reusable, 4 Heat Levels, Lig
- 15869028729118 — Bird Feeders with Camera, Smart Bird Feeder Camera with App 
- 15869029122334 — Garden Decor Wind Spinners for Yard, Stainless Steel Metal W
- 15869029155102 — Coffee Cup, 3D Sculpted Monster Mug, Ceramic Coffee Mug for 
- 15869029286174 — Cute Frog Garden Decor, Resin Frog Figurine for Plant Pot Ri
- 15869029318942 — Wireless CarPlay Adapter for iPhone, Mini USB and USB C CarP
- 15869029384478 — Bottle Washer and Sterilizer, Automatic Bottle Washer for Ba
- 15869029417246 — Karaoke Machine for Kids, Portable Karaoke Machine with Blue
- 15869029450014 — Kids Games Reflex Reaction Trainer, Falling Stick Game, Hand
- 15869029646622 — Monocular for Hiking and Sightseeing, Compact Monocular Tele
- 15869029679390 — Car Scratch Remover for Light Scratches, Swirl Marks, Car Po
- 15869029777694 — Vanity Mirror with Lights, Rechargeable Travel Makeup Mirror
- 15869029810462 — Back Massager with Heat for Car and Home Chair, Massage Seat
- 15869029875998 — Oversized Hoodie for Women and Men, Wearable Blanket Hoodie 
- 15869029941534 — UV Light Wand, Handheld UV Light for Cleaning Surfaces, Port
- 15869029974302 — Heating Pad for Back and Shoulders, Large Electric Heating P
- 15869030007070 — Chainsaw Cordless, Mini Electric Chainsaw with 2 Spare Chain
- 15869030072606 — Meat Thermometer for Grilling, Instant Read Meat Thermometer
- 15869030105374 — Funny Games Chameleon Mask Party Game Set with 2 Extendable 
- 15869030138142 — Math Games for Kids, Wooden Board Game with 2 Dice for 2-4 P
- 15869030170910 — Microfiber Mop for Gap Cleaning Under Furniture, Bendable Fl
- 15869030236446 — Makeup Bags for Travel, Travel Toiletry Bags for Women, Zipp
- 15869030269214 — Dog Leash for Two Dogs, Dual Retractable Dog Leash for Small
- 15869030301982 — Toys for 2 Year Olds, Large Felt Board for Wall, Felt Story 
- 15869030334750 — Sensory Toys, Montessori Toys and Toddler Toys, Travel Busy 
- 15869030433054 — Transforming Toys for 3 Year Old Boys, Magnetic Building Toy
- 15869030564126 — Matching Game for Kids, Magnetic Board with Color Matching G
- 15869030596894 — Dog Toys Snuffle Mat for Small and Large Dogs, Interactive D
- 15869030629662 — Dog Toys Large Snuffle Mat 20 x 28 in, Machine Washable Dog 
- 15869030662430 — Winter Gloves for Men and Women, Water Resistant Thermal Ski
- 15869030695198 — Bike Lights with Phone Mount and Bike Horn, 400 Lumen LED He
- 15869030760734 — Cat Toys Interactive Cat Play Mat with Moving Chase Ball, Ba
- 15869030826270 — Mens Shoes for Winter, Warm Winter Boots for Men with Grip S
- 15869030859038 — Driving Gloves for Men, Mens Dress Gloves with Touchscreen F
- 15869030924574 — Cargo Pants and Jacket for Men, Mens Hiking Pants and Hooded


## Ek — yaş aralığı düzeltmesi (2026-09-02, aynı gün)

Kullanıcı tespiti: manyetik eşleştirme oyunu (4-5+) açıklamada üç kez "4 year olds" diyor,
5'i hiç anmıyor. Kural eklendi (`description-format-rule.md`, "Age ranges"): yaş aralığı
olan üründe aralık ifadesi kullanılır (`ages 4-5+`); tek-yaş keyword ifadeleri yalnızca
title'dan gelen keyword ise, bir kez ve aralığı da söyleyen cümlede geçer; ölçülmüş yaş
aileleri aralığın tek ucuna yığılmaz.

Beş batch tarandı; tek-yaş ifadesi olup aralığı yansıtmayan 4 ürün batch5'te çıktı ve
düzeltilip push edildi (0 hata): felt board 15869030301982 · travel busy board
15869030334750 · transforming magnetic toys 15869030433054 · magnetic matching game
15869030564126. batch2'deki üç "3 year old" ürünü "ages 3 and up" ile birlikte geçtiği
için kurala uygun, dokunulmadı. Title'lar değiştirilmedi.
