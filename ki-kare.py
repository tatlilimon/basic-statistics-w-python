import numpy as np
from scipy.stats import chisquare
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

# Kullanıcıdan veri setini girmesini iste
input_data = input(Fore.BLUE + "Gözlenen frekanslarınızı; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
# Kullanıcının girdiği veriyi virgülle böl ve numpy dizisine dönüştür
observed_frequencies = np.array([float(x) for x in input_data.split(",")])

# Beklenen frekanslar
# Eğer belirli beklenen frekanslar verilmediyse, tüm sonuçların eşit olarak dağıtılması beklenir.
expected_frequencies = np.full_like(observed_frequencies, np.mean(observed_frequencies))

# Ki-Kare istatistiği ve p-değeri hesaplama kısmı
chi2_stat, p_val = chisquare(observed_frequencies, f_exp=expected_frequencies)

print(Fore.GREEN +"Chi-Square istatistiği: " + Fore.RESET, chi2_stat)
print(Fore.GREEN +"p-değeri: " + Fore.RESET, p_val)
print(Fore.MAGENTA +"Eğer Hipotez Testi yapılacaksa; ki-kare istatistik değeri hesaplandıktan sonra Alttaki link'i tarayıcınızda açın" + Fore.RESET)
print(Fore.BLUE +"https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html" + Fore.RESET)
print(Fore.MAGENTA +"v=(toplam veri adeti-1), Kırmızı alan=0.05 eğer soruda 0.01 isteniyorsa 0.01 yazın ardından size x değerini verecektir. çıkan x değeri, ki kare istatistik değerinden fazla ise h0 Reddedilir. küçük ise h0 Kabul edilir." + Fore.RESET)

