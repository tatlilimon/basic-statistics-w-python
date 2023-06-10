import numpy as np
from scipy.stats import chi2_contingency
from colorama import Fore, Style

# Kullanıcıdan satır sayısını girmesini iste
num_rows = int(input(Fore.BLUE + "Veri setinizin kaç satırı var?: " + Fore.RESET))

# Her bir satır için, kullanıcıdan verileri girmesini iste
observed_frequencies = []
for i in range(num_rows):
    row_data = input(Fore.BLUE + f"{i+1}. satırın verilerini; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
    observed_frequencies.append([float(x) for x in row_data.split(",")])

# Kullanıcının girdiği verileri numpy dizisine dönüştür
observed_frequencies = np.array(observed_frequencies)

# Ki-Kare istatistiği, p-değeri, serbestlik derecesi ve beklenen frekansları hesaplama
chi2_stat, p_val, dof, expected_frequencies = chi2_contingency(observed_frequencies)

print(Fore.GREEN +"Chi-Square istatistiği: " + Fore.RESET, chi2_stat)
print(Fore.GREEN +"p-değeri: " + Fore.RESET, p_val)
print(Fore.GREEN +"Serbestlik Derecesi: " + Fore.RESET, dof)

print(Fore.MAGENTA +"Eğer Hipotez Testi yapılacaksa; ki-kare istatistik değeri hesaplandıktan sonra Alttaki link'i tarayıcınızda açın" + Fore.RESET)
print(Fore.BLUE +"https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html" + Fore.RESET)
print(Fore.MAGENTA +"v=(satırSayısı-1)*(sütunSayısı-1), Kırmızı alan=0.05 eğer soruda 0.01 isteniyorsa 0.01 yazın ardından size x değerini verecektir. çıkan x değeri, ki kare istatistik değerinden fazla ise h0 Reddedilir. küçük ise h0 Kabul edilir." + Fore.RESET)

#BURASI ÖNEMLİ!!!!
#ki-kare bağımsızlık istatistik değeri hesaplandıktan sonra;
#alttaki link'e gidin
#https://homepage.divms.uiowa.edu/~mbognar/applets/chisq.html
#v=(satırSayısı-1)*(sütunSayısı-1)
#kırmızı alan=0.05 eğer soruda 0.01 isteniyorsa 0.01 yazın
#ardından size x değerini verecektir.
#çıkan x değeri, ki kare bağımsızlık istatistik değerinden fazla ise h0 Reddedilir.
#çıkan x değeri, ki kare bağımsızlık istatistik değerinden küçük ise h0 Kabul edilir.  
