import numpy as np
from scipy import stats
GREEN = '\033[92m'
END = '\033[0m'
# Veri setinizi alta girin
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 3])

# Aritmetik ortalama bulmak için
mean = np.mean(data)
print(GREEN +"Aritmetik Ortalama: " + END, mean)

# Medyan bulmak için
median = np.median(data)
print(GREEN +"Medyan: " + END, median)

# Mod bulmak için
mode = stats.mode(data)
print(GREEN +"Mod: " + END, mode[0][0])

# Çeyrek değerler bulmak için
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
print(GREEN +"Q1: " + END, q1)
print(GREEN +"Q3: " + END, q3)

# Standart sapma bulmak için
std_dev = np.std(data)
print(GREEN +"Standart Sapma: " + END, std_dev)

# Varyans bulmak için
variance = np.var(data)
print(GREEN + "Varyans: " + END, variance)
