import numpy as np
from scipy import stats
from colorama import Fore, Style

# Kullanıcıdan veri setini girmesini iste
input_data1 = input(Fore.BLUE + "1. veri grubunuzun elemanlarını; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
input_data2 = input(Fore.BLUE + "2. veri grubunuzun elemanlarını; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)

# Kullanıcının girdiği veriyi virgülle böl ve numpy dizisine dönüştür
sample1 = np.array([float(x) for x in input_data1.split(",")])
sample2 = np.array([float(x) for x in input_data2.split(",")])

# Kullanıcıdan güven seviyesini girmesini iste
confidence_level_input = float(input(Fore.BLUE + "Güven seviyesini belirtiniz:(0.05 yada 0.01) " + Fore.RESET))
confidence_level = 0.95 if confidence_level_input == 0.05 else 0.99 if confidence_level_input == 0.01 else None

if confidence_level is None:
    print(Fore.RED + "Geçerli bir güven seviyesi girilmedi!" + Fore.RESET)
    exit()

# t-test hesaplama kısmı
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

# Güven aralığı hesaplama
degrees_freedom = len(sample1) + len(sample2) - 2
standard_error_difference = np.sqrt(np.var(sample1)/len(sample1) + np.var(sample2)/len(sample2))

confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=np.mean(sample1)-np.mean(sample2), scale=standard_error_difference)

print(Fore.GREEN +"T istatistiği: " + Fore.RESET, t_statistic)
print(Fore.GREEN +"P değeri: " + Fore.RESET, p_value)
print(Fore.GREEN +"Güven aralığı: " + Fore.RESET, confidence_interval)
