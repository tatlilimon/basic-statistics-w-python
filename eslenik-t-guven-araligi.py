#eşlenik örneklem için t istatistiği %95 güven aralığında alt sınır ve üst sınır bulma
import numpy as np
from scipy import stats
from colorama import Fore, Style

# Eşleşlenik örneklem için veriler. 1,2,3 yerine a grubunu, 4,5,6 yerine ise b grubunu yazınız.
paired_sample1 = np.array([1,2,3])
paired_sample2 = np.array([4,5,6])

# Eşleştirilmiş t-test hesaplama
t_statistic, p_value = stats.ttest_rel(paired_sample1, paired_sample2)

# Güven aralığı hesaplama
confidence_level = 0.95 #güven aralığı default olarak %95 verilir. Değiştirmek için değeri değiştiriniz.
degrees_freedom = len(paired_sample1) - 1
mean_difference = np.mean(paired_sample1 - paired_sample2)
standard_error_difference = np.std(paired_sample1 - paired_sample2, ddof=1) / np.sqrt(len(paired_sample1))

confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=mean_difference, scale=standard_error_difference)

print(Fore.GREEN +"T istatistiği: " + Fore.RESET, t_statistic)
print(Fore.GREEN +"P değeri: " + Fore.RESET, p_value)
print(Fore.GREEN +"Güven aralığı: " + Fore.RESET, confidence_interval)
