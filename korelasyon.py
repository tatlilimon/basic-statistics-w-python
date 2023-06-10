import numpy as np
from colorama import Fore, Style

# İki veri setini de giriniz. Eğer veri setinde belirli veriler verilmemiş ise gözardı edin.
data1 = np.array([1,2,3])
data2 = np.array([4,5,6])

# Korelasyon katsayısının hesaplama kısmı
correlation_matrix = np.corrcoef(data1, data2)

# Korelasyon katsayısı, korelasyon matrisinin dış köşegenlerinde yer alır
correlation_coefficient = correlation_matrix[0, 1]

print(Fore.GREEN + "Korelasyon katsayısı: " + Fore.RESET, correlation_coefficient)
