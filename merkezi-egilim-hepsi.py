import numpy as np
from scipy import stats
from colorama import Fore, Style
# Veri setinizi alta girin
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 3])

# Aritmetik ortalama bulmak için
mean = np.mean(data)
print(Fore.GREEN +"Aritmetik Ortalama: " + Fore.RESET, mean)

# Medyan bulmak için
median = np.median(data)
print(Fore.GREEN +"Medyan: " + Fore.RESET, median)

# Mod bulmak için
mode = stats.mode(data)
print(Fore.GREEN +"Mod: " + Fore.RESET, mode[0][0])

# Çeyrek değerler bulmak için
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
print(Fore.GREEN +"Q1: " + Fore.RESET, q1)
print(Fore.GREEN +"Q3: " + Fore.RESET, q3)

# Standart sapma bulmak için
std_dev = np.std(data)
print(Fore.GREEN +"Standart Sapma: " + Fore.RESET, std_dev)

# Varyans bulmak için
variance = np.var(data)
print(Fore.GREEN + "Varyans: " + Fore.RESET, variance)
