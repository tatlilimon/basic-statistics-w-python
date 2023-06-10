import numpy as np
from scipy.stats import chi2_contingency
from colorama import Fore, Style

# Gözlenen frekansları ilk dizi ve ikinci dizi olarak yerleştir. 
#ilk dizi; 1.satır, ikinci dizi; 2.satır olacak şekilde yerleştir
#Eğer tablo daha geniş ise dizi eklemesi yapabilirsiniz.
observed_frequencies = np.array([[1,2,3], [4,5,6]])

# Ki-Kare istatistiği, p-değeri, serbestlik derecesi ve beklenen frekansları hesaplama
chi2_stat, p_val, dof, expected_frequencies = chi2_contingency(observed_frequencies)

print(Fore.GREEN +"Chi-Square istatistiği: " + Fore.RESET, chi2_stat)
print(Fore.GREEN +"p-değeri: " + Fore.RESET, p_val)
print(Fore.GREEN +"Serbestlik Derecesi: " + Fore.RESET, dof)

#BURASI ÖNEMLİ!!!!
#ki-kare bağımsızlık istatistik değeri hesaplandıktan sonra;
#alttaki link'e gidin
#https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html
#v=(satırSayısı-1)*(sütunSayısı-1)
#kırmızı alan=0.05 eğer soruda 0.01 isteniyorsa 0.01 yazın
#ardından size x değerini verecektir.
#çıkan x değeri, ki kare bağımsızlık istatistik değerinden fazla ise h0 Reddedilir.
#çıkan x değeri, ki kare bağımsızlık istatistik değerinden küçük ise h0 Kabul edilir.
