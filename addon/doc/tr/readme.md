# Kolay Tablo Gezgini #

* Yazarlar: Corentin Bacqué-Cazenave, Joseph Lee
* [Kararlı sürüm][1]ü indir
* [Geliştirme sürümü][2]nü indir
* NVDA uyumluluğu: 2019.3 ve sonrası

Bu eklenti, tablo hücrelerinde gezinmek için basitleştirilmiş tuş
kombinasyonunu kullanmak üzere bir katman komutu ekler. Katmanlı komutlar
etkinleştirildiğinde, aşağıdaki eylemleri gerçekleştirebilirsiniz:

* Ok tuşlarını kullanarak yatay veya dikey olarak önceki veya sonraki
  hücreye gidin
* Control+ok tuşlarını veya Home, End, PageUp ve PageDown'u kullanarak
  satırın veya sütunun ilk veya son hücresine gidin
* Windows+sol ok / windows+yukarı ok kullanarak sistem imlecini hareket
  ettirmeden tüm satırı veya sütunu okuyun
* Geçerli hücreden başlayarak satırı veya sütunu windows+sağ ok /
  windows+aşağı ok kullanarak okuyun

Şu anda desteklenen tablolar şunlardır:

* Tarama kipi modu (Internet Explorer, Firefox, vb.).
* Microsoft Word.

## Komutlar

* Tablo gezgini katmanını açar ve kapatır (atanmamış).

## 2.4 için değişiklikler

Bu sürüm için, çalışmalarından dolayı Cyrille Bougot'ya çok teşekkürler.

* Tablo navigasyonu MS Word'de düzeltildi
* NVDA 2022.2 ve 2022.4'teki değişiklikleri takiben yeni komutlar tanıtıldı

    * başlangıç ​​noktasına atlamak için home/end/pgUp/pgDown/satır/sütun
      sonu
    * satır/sütun başına/sonuna atlamak için control+sol/sağ/yukarı/aşağıOk
      (aynı sonuç için alternatif kısayol tuşu)
    * İmlecin mevcut konumunu hareket ettirmeden ilk hücreden başlayarak tüm
      satırı/sütun okumak için NVDA+sol/yukarı
    * NVDA + sağ / aşağı diyelim ki Satırda / sütunda tümü, yani geçerli
      satırın / sütunun hücrelerini okuyun, geçerli hücreden başlayın ve
      satırın / sütunun son hücresine kadar okurken imlecin konumunu hareket
      ettirin.

* Çakışmaları önlemek için bazı tuşlar yeniden eşlendi:

    * NVDA+yukarı ok/sol ok, windows+yukarı ok/sol ok olur (tam sütun/satır
      okumak için)
    * NVDA+aşağı ok/sağ Ok, windows+aşağı ok/sağ Ok olur (tümünü sütun/satır
      olarak söyleyin)

* Artık NVDA 2023.1 ile uyumlu

## 2.3 için değişiklikler

* Tablo gezinme katmanını her yerden devre dışı bırakmak artık mümkün
* Artık NVDA 2022.1 ile uyumlu
* Eklentiyi yeniden yüklerken hata düzeltildi

## 2.2.1 için Değişiklikler

* Word ve Outlook dahil bazı belge türlerindeki bir hata düzeltildi

## 2.2 için değişiklikler

* Eklenti şablonundan belge stili güncellendi
* İlk tercüme edilmiş sürüm

## 2.1.1 için Değişiklikler

* Manifest dosyasında  ve belgelerde yeni yazar

## 2.1 için değişiklikler

* Artık NVDA 2021.1 ile uyumlu

## 2.0 için değişiklikler

* NVDA 2019.3 veya sonraki bir sürümü gerektirir.
* Çeşitli eklenti mesajları çevrilebilir hale getirildi.

## 1.2 için değişiklikler

* Gelecekteki NVDA sürümlerini desteklemek için değişiklikler.

## 1.1 için değişiklikler

* Outlook'ta bir iletide yazım denetimi yapılırken hataların duyulabileceği
  bir sorun düzeltildi.

## 1.0 için değişiklikler

*   İlk sürüm.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=etn

[2]: https://www.nvaccess.org/addonStore/legacy?file=etn-dev
