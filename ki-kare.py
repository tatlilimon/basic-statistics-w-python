import numpy as np
from scipy.stats import chisquare
from colorama import Fore, Style

# Gözlenen frekansları alta yazınız.
observed_frequencies = np.array([1,2,3])

# Beklenen frekanslar
# Eğer belirli beklenen frekanslar verilmediyse, tüm sonuçların eşit olarak dağıtılması beklenir.
expected_frequencies = np.full_like(observed_frequencies, np.mean(observed_frequencies))

# Ki-Kare istatistiği ve p-değeri hesaplama kısmı
chi2_stat, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)

print(Fore.GREEN +"Chi-Square istatistiği: " + Fore.RESET, chi2_stat)
print(Fore.GREEN +"p-değeri: " + Fore.RESET, p_val)

#BURASI ÖNEMLİ!!!!
#ki-kare istatistik değeri hesaplandıktan sonra;
#alttaki link'e gidin
#https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html
#v=toplam veri adeti-1
#kırmızı alan=0.05 eğer soruda 0.01 isteniyorsa 0.01 yazın
#ardından size x değerini verecektir.
#çıkan x değeri, ki kare istatistik değerinden fazla ise h0 Reddedilir.
#çıkan x değeri, ki kare istatistik değerinden küçük ise h0 Kabul edilir.
