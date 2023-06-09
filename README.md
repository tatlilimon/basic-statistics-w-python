## <ins>Giriş</ins>

Bu repoda, basit istatistiksel kalıpları kolaylıkla hesaplayan python programları mevcuttur.

Hangi konuda hesaplama yapılması gerekiyorsa o başlıkta bulunan python dosyası açılmalıdır. Çünkü bazı programlarda değişebilecek faktörler olduğu için ve ekstra hesaplamalar yapılabildiği için <ins>**kodun içindeki açıklama satırları kontrol edilmelidir**</ins> **!**

* * *

## <ins>Gereksinimlerin Yüklenme Aşaması</ins>

Python ile veri analizi yapmak için belirli kütüphanelere ihtiyaç duyulur.

- İlk olarak python'ın 3.3 ve üzeri sürümünün cihazınızda yüklü olması gerekir. Bunu kontrol etmek için, cmd veya terminal vasıtası ile  `python --version` komutu ile kontrol edilir. Eğer yüklü değil ise; python, cihaza mutlaka kurulmalıdır.
- Gerekli tüm kütüphaneleri bir anda kurmak için **terminal veya cmd** de bu kodu çalıştırınız. `pip3 install -r requirements.txt`
- Eğer programlar haladaha çalışmıyor ise; requirements.txt adlı dosyadaki kütüphaneleri: `pip show kütüphaneAdi` olarak yüklü olup olmadığını kontrol edin.
- Eğer değil ise manuel olarak yükleyin. `pip install kütüphaneAdi`

* * *

## <ins>Nasıl Kullanılır?</ins>

1.  Projedeki python dosyalarının isimleri, işlevlerini yansıtır. İstenilen işlem için gerekli python dosyası bulunur.
2.  Gerekli python dosyasının içinde **<ins>istatistiği yapılacak verilerin girilmesi gerekir</ins>**. VSCode, notepad++ ve vim gibi metin düzenleyiciler ile bunu çok rahat yapabilirsiniz.
3.  CMD veya Terminal kullanarak proje dizinine `cd` komutu ile gidilir. Ya da VSCode kullanıyorsanız ve projeyi VSCode içinde açtıysanız, editörün içinde terminal açarsanız direkt olarak proje dizininde açar. cd komutuna gerek kalmaz.
4.  Komut satırına; `python3 dosyaAdi.py` yazılır ve program çalışır. Örneğin; `python3 ki-kare.py`
5.  Komut satırında istenilen istatistiği veren çıktıyı görürsünüz. Yeşil renk ile belirtilen değerler, istediğiniz istatistiksel değerlerdir.

* * *

## <ins>Projeye Katkıda Bulunmaktan Çekinmeyin!</ins>

Projede bulunan istatistiksel hesaplama araçlarından farklı olarak başka araçlar da <ins>**PR**</ins> açarak ekleyebilirsiniz.

> Proje GPL 3 lisanslaması altındadır. Yani bu yazılımı istediğiniz gibi kopyalayıp herhangi bir yerde kullanabilirsiniz lakin bunun tek şartı var o da; GPL 3 lisansı altında yayınlamanız. Yani bu kodları başka yerde kullanacaksanız o projenin de açık kaynaklı olması gerekiyor.
> 
> GPL 3 hakkında daha fazla bilgi için [Tıkla!](https://github.com/tatlilimon/basic-statistics-w-python/blob/main/LICENSE)