import numpy as np
from scipy import stats
from colorama import Fore, Style
# Örneklem verileri 1,2,3 yerine a grubunu, 4,5,6 yerine ise b grubunu yazınız.
sample1 = np.array([1, 2, 3])
sample2 = np.array([4, 5, 6])

# t-test hesaplama kısmı
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

# Güven aralığı 
confidence_level = 0.95 #guven araligi default olarak %95'tir. Eğer başka değer isteniyorsa, bu sayı değiştirilir.
#Hesaplama kısmı
degrees_freedom = len(sample1) + len(sample2) - 2
standard_error_difference = np.sqrt(np.var(sample1)/len(sample1) + np.var(sample2)/len(sample2))

confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=np.mean(sample1)-np.mean(sample2), scale=standard_error_difference)

print(Fore.GREEN +"T istatistiği: " + Fore.RESET, t_statistic)
print(Fore.GREEN +"P değeri: " + Fore.RESET, p_value)
print(Fore.GREEN +"Güven aralığı: " + Fore.RESET, confidence_interval)
