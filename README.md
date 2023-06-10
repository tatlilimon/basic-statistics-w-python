## <ins>Giriş</ins>

Bu repoda, basit istatistiksel kalıpları kolaylıkla hesaplayan python programları mevcuttur. Program aşağıdaki **ana menü** ile başlar.

![cli-ss](https://github.com/tatlilimon/basic-statistics-w-python/assets/43828285/0de22404-8669-434b-a690-7e3aeb125f1a)


Hangi konuda hesaplama yapılması gerekiyorsa, ana menüden ilgili konu seçilir ve veri seti girilmeye başlanır. Veri seti ve istenilen bilgiler girildikten sonra hesaplama sonucu komut satırında çıktı olarak verilecektir.

* * *

## <ins>Gereksinimlerin Yüklenme Aşaması</ins>

Python ile veri analizi yapmak için belirli kütüphanelere ihtiyaç duyulur.

- İlk olarak python'ın 3.3 ve üzeri sürümünün cihazınızda yüklü olması gerekir. Bunu kontrol etmek için, cmd veya terminal vasıtası ile  `python --version` komutu ile kontrol edilir. Eğer yüklü değil ise; python, cihaza <ins>**mutlaka**</ins> kurulmalıdır.
- Gerekli tüm kütüphaneleri bir anda kurmak için **terminal veya cmd** de proje dizinine `cd` komutu ile gidin ve bu kodu çalıştırınız. `pip install -r requirements.txt`
- Eğer programlar haladaha çalışmıyor ise; **requirements.txt** adlı dosyadaki kütüphaneleri: `pip show kütüphaneAdi` olarak yüklü olup olmadığını kontrol edin.
- Eğer değil ise **manuel** olarak yükleyin. `pip install kütüphaneAdi`

* * *

## <ins>Nasıl Kullanılır?</ins>

1.  **CMD** veya **Terminal** kullanarak proje dizinine `cd` komutu ile gidilir. Ya da VSCode kullanıyorsanız ve projeyi VSCode içinde açtıysanız, editörün içinde terminal açarsanız direkt olarak proje dizininde açar. cd komutuna gerek kalmaz.
2.  Komut satırına `python3 main.py` girilerek **ana menü**ye erişilir.
3.  Ana menüden hangi konuda istatistik hesaplamalar yapılacaksa; ilgili konunun başındaki **rakam**, <ins>direkt girdi</ins> olarak komut satırına girilir.
4.  Veri setini komut satırına girerken, <ins>**her bir veri arasına virgül**</ins> koyup <ins>**son veriden sonra virgül koymamaya**</ins> dikkat edin!

* * *

## <ins>Projeye Katkıda Bulunmaktan Çekinmeyin!</ins>

Projede bulunan istatistiksel hesaplama araçlarından farklı olarak başka araçlar da <ins>**PR**</ins> açarak ekleyebilirsiniz.

> Proje GPL 3 lisanslaması altındadır. Yani bu yazılımı istediğiniz gibi kopyalayıp herhangi bir yerde kullanabilirsiniz lakin bunun tek şartı var o da; GPL 3 lisansı altında yayınlamanız. Yani bu kodları başka yerde kullanacaksanız o projenin de açık kaynaklı olması gerekiyor.
> 
> GPL 3 hakkında daha fazla bilgi için [Tıkla!](https://github.com/tatlilimon/basic-statistics-w-python/blob/main/LICENSE)
