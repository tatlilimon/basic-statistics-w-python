import numpy as np
from scipy.stats import f_oneway
from colorama import Fore, Style
from colorama import just_fix_windows_console
just_fix_windows_console()
# Kullanıcıdan grup sayısını girmesini iste
num_groups = int(input(Fore.BLUE + "Veri setinizde kaç grup var?: " + Fore.RESET))

# Her bir grup için, kullanıcıdan verileri girmesini iste
groups = []
for i in range(num_groups):
    group_data = input(Fore.BLUE + f"{i+1}. grubun verilerini; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
    groups.append(np.array([float(x) for x in group_data.split(",")]))

# F istatistiği ve p-değeri hesaplama
F, p = f_oneway(*groups)

print(Fore.GREEN +"F istatistiği: " + Fore.RESET, F)
print(Fore.GREEN +"p-değeri: " + Fore.RESET, p)

print(Fore.MAGENTA +"Kritik değeri hesaplamak için Alttaki linki tarayıcınızda açın! " + Fore.RESET)
print(Fore.BLUE +"https://www.danielsoper.com/statcalc/calculator.aspx?id=4" + Fore.RESET)
print(Fore.MAGENTA +"degrees of freedom 1: (toplam grup sayısı-1)'dir" + Fore.RESET)
print(Fore.MAGENTA +"degrees of freedom 2: (tüm gruptakilerin toplam veri sayısı - grup sayısı)'dır" + Fore.RESET)
print(Fore.MAGENTA +"Çıkan F istatistik değeri; eğer kritik değerden büyük ise h0 Reddedilir, küçük ise Kabul edilir" + Fore.RESET)
