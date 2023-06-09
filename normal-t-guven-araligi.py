import numpy as np
from scipy import stats
GREEN = '\033[92m'
END = '\033[0m'
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

print(GREEN +"T istatistiği: " + END, t_statistic)
print(GREEN +"P değeri: " + END, p_value)
print(GREEN +"Güven aralığı: " + END, confidence_interval)
