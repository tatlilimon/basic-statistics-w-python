import numpy as np
from scipy.stats import f_oneway
from colorama import Fore, Style

# Veri setleri grup halinde dizilere yazılır. 3'ten fazla ise group4,group5 diye ekelyiniz.
group1 = np.array([1, 2, 3, 4, 5, 6])
group2 = np.array([2, 3, 4, 5, 6, 7])
group3 = np.array([3, 4, 5, 6, 7, 8])

# F istatistiği ve p-değeri hesaplama. 3'ten fazla grup var ise () içine grup adlarını yazmayı unutmayınız!!!
F, p = f_oneway(group1, group2, group3)

print(Fore.GREEN +"F istatistiği: " + Fore.RESET, F)
print(Fore.GREEN +"p-değeri: " + Fore.RESET, p)
#BURASI ÖNEMLİ!!!!
#Çıkan F istatistik değeri; eğer kritik değerden büyük ise h0 Reddedilir.
#Çıkan F istatistik değeri; eğer kiritk bölgeden küçük ise h0 Kabul edilir 
#Kritik değeri hesaplamak için https://www.danielsoper.com/statcalc/calculator.aspx?id=4 linkine gidin
#degrees of freedom 1: toplam grup sayısı-1'dir
#degrees of freedom 2: tüm gruptakilerin toplam veri sayısı - grup sayısı'dır.
#bu iki bilgi ile kritik değeri öğrenenebilirsiniz.