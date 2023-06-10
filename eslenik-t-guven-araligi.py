import numpy as np
from scipy import stats
from colorama import Fore, Style

# Kullanıcıdan her iki grubun verilerini al
paired_sample1_data = input(Fore.BLUE + "Birinci veri setinizi; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
paired_sample1 = np.array([float(x) for x in paired_sample1_data.split(",")])
paired_sample2_data = input(Fore.BLUE + "İkinci veri setinizi; aralarında virgül olacak şekilde giriniz ve ardından enter'a basınız: " + Fore.RESET)
paired_sample2 = np.array([float(x) for x in paired_sample2_data.split(",")])

# Kullanıcıdan güven seviyesini al ve bunu güven aralığına dönüştür
confidence_level_input = float(input(Fore.BLUE + "Güven seviyesini belirtiniz:(0.05 yada 0.01) " + Fore.RESET))
confidence_level = 0.95 if confidence_level_input == 0.05 else 0.99 if confidence_level_input == 0.01 else None

if confidence_level is None:
    print(Fore.RED + "Geçerli bir güven seviyesi girilmedi!" + Fore.RESET)
    exit()

# Eşleştirilmiş t-test hesaplama
t_statistic, p_value = stats.ttest_rel(paired_sample1, paired_sample2)

# Güven aralığı hesaplama
degrees_freedom = len(paired_sample1) - 1
mean_difference = np.mean(paired_sample1 - paired_sample2)
standard_error_difference = np.std(paired_sample1 - paired_sample2, ddof=1) / np.sqrt(len(paired_sample1))
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=mean_difference, scale=standard_error_difference)

print(Fore.GREEN +"T istatistiği: " + Fore.RESET, t_statistic)
print(Fore.GREEN +"P değeri: " + Fore.RESET, p_value)
print(Fore.GREEN +"Güven aralığı: " + Fore.RESET, confidence_interval)
